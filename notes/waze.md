# Waze 5.25.0.1 (com.waze) — working notes (paths under work/waze/jdex)

Note: base APK ships NO native libs (libwaze.so etc. are in an arm64 config split that was not downloaded). Much of the logic (ads timing, consent bumps, calendar/contacts upload) lives in C++ and could not be inspected. Native UI strings are available in assets/res/lang.eng (extracted to scratchpad) — they show copy, not when/whether it is shown.

## "TIDE" drive detection: every Bluetooth connection reported to Waze with device name/class + location
- Manifest: exported receiver com.waze.tide.BluetoothConnectionReceiver on android.bluetooth.device.action.ACL_CONNECTED → app is woken on every BT connection (headphones, watch, car, medical device), even when not running.
- classes7/sources/com/waze/tide/t.java c(): on DeviceConnected, sends a "drive detection" request only if: TIDE enabled (server flag), user not opted out, NOT navigating, app is in BACKGROUND, min interval since last report (CONFIG ..._REPORT_MIN_INTERVAL_MINUTES, pref "last_blu_con"), BT permission granted.
- t.java j()/k(): builds BluetoothDeviceName / BluetoothDeviceNameAndType from BluetoothDevice.getName() + BluetoothClass mapped to strings (e.g. "AUDIO_VIDEO_CAR_AUDIO", "WEARABLE_WRIST_WATCH", "HEALTH_GLUCOSE", "HEALTH_BLOOD_PRESSURE", "HEALTH_PULSE_OXIMETER", "TOY_DOLL_ACTION_FIGURE").
- classes7/sources/com/waze/tide/s.java: if location permission is ALWAYS_ON (tide/w.java), reads LocationManager.getLastKnownLocation for every enabled provider and attaches lat/lon to the report.
- classes8/sources/com/waze/tide/g.java: DriveDetectionReport (device name/type + location) → protobuf to Waze server (log "DriveDetectionApi sendReportDriveDetectionRequest").
- classes9/sources/com/waze/tide/ab.java a(): same device name/type + timestamp also sent as a stats event (wazeStatSender).
- Config (classes6/sources/com/waze/config/ConfigValues.java ~31220): CONFIG_VALUE_DRIVE_DETECTION_TIDE_ENABLED, _USER_OPTOUT, _REPORT_MIN_INTERVAL_MINUTES, _BLUETOOTH_PERMISSION_COLLECTION_ENABLED, _COLLECT_PERMISSIONS_STATE (sends location/BT permission state as stat), _SESSION_COUNT_UNTIL_PERMISSION_REQUEST. Shipped client default for TIDE_ENABLED appears FALSE (server-pushed).
- BT permission ask for TIDE uses generic Beacons copy (classes7/sources/com/waze/l/m.java:515): BEACONS_BLUETOOTH_PERMISSIONS_RATIONALE_TITLE "Stay connected with Bluetooth" / TEXT "Get turn directions in tunnels, and traffic updates when not using Waze". No mention that names/types of every BT device you connect to (plus location) are sent to Waze.
- Re-ask cadence: classes6/sources/com/waze/tide/i.java h(): re-shown after ..._BLUETOOTH_PERMISSION_COLLECTION_COOLDOWN_PERIOD_DAYS unless user ticks "Don't show again" (UserOptOut → TIDE_USER_OPTOUT true, which also disables TIDE). Startup permission chain (classes5/sources/com/waze/ec.java): location → notifications → TIDE Bluetooth.

## Background ("Allow all the time") location pushes
- classes7/sources/com/waze/view/popups/RequestAlwaysLocationDialogActivity.java: triggered from planned-drive save, planned-drive notification toggle, calendar sync, notification settings (o.java enum FROM_PLANNED_DRIVE_SAVE / ..._NOTIFICATION_TOGGLE / FROM_SYNC_CALENDAR / FROM_NOTIFICATION_SETTINGS).
- Copy: "Wait a second..." / "Waze wants to use your location to remind you to leave on time, update you about traffic, and more – even when not using the app"; buttons "Settings" vs "No thanks"; checkbox "Don’t show this again".
- Dark pattern: the "Don’t show this again" checkbox sets CONFIG_VALUE_PRIVACY_USE_LOCATION_IN_BG_DIALOG_DONT_SHOW_AGAIN on either answer (s()), and onCreate then SKIPS the explainer and calls ActivityCompat.requestPermissions(ACCESS_BACKGROUND_LOCATION) directly next time (lines ~140-143). "Don't show again" therefore means "go straight to the OS prompt", not "stop asking".
- After a permanent denial: "Wait a sec..." / "Go to Settings and then" with "Settings" / "No thanks" (FUTURE_DRIVES_LOCATION_PERMISSION_DIALOG_*), and later attempts open app settings directly (iq.g).
- For adults the "Settings" CTA is primary; for age-restricted accounts it is rendered SECONDARY (zD ? w.SECONDARY) — i.e. the nudge styling is deliberately removed for minors.
- Native strings (lang.eng / strings.xml, display only from C++): consent bump PRIVACY_CONCENT_BUMP_BG_LOCATION_TITLE "Get even more out of Waze" then on "No thanks" a confirm "Are you sure?" ("To get these alerts and more, let Waze access your location even when not using the app.") — second-chance re-ask. Settings: "Waze can check your location even when you’re not using the app to get reminders for planned drives, updates about bad traffic, parking assistance, and more". Also "For better accuracy, choose "Always on"" footers on planned drives/time-to-leave (3 variants all same copy), and FUTURE_DRIVES_PLAN_SAVED_POPUP_TEXT "For accurate departure times based on live traffic, location change reporting is now turned on." (auto-enables reporting on saving a planned drive; pre-Android-Q path in RequestAlwaysLocationDialogActivity o() sets CONFIG_VALUE_PRIVACY_USE_LOCATION_IN_BG=true directly).

## Personalized-ads consent: asymmetric buttons, delayed until engaged
- classes7/sources/com/waze/uid/d.java ~65-110: "Personalized ads?" dialog shown only after the user has navigated ≥ CONFIG_VALUE_ADS_ALLOW_PROFILE_TARGETING_SHOW_DIALOG_MINIMUM_DRIVE_COUNT drives, if targeting currently off and selection "unset", and not age-restricted.
- Buttons: "Not personalized" styled SECONDARY; "Personalized" styled PRIMARY for adults (SECONDARY for age-restricted) — design_components/button/g.java PRIMARY/SECONDARY.
- Text: "Waze uses info you've added to your account and data from trusted ad partners to show you more relevant ads."
- Guest onboarding (classes7/sources/com/waze/uid/state_impl/d/c.java): sets ALLOW_PROFILE_TARGETING = CONFIG_VALUE_ADS_ALLOW_PROFILE_TARGETING_DEFAULT (shipped default FALSE, server-overridable) without asking.
- Choices are audit-logged with the exact string IDs shown (iq.java j()/k(), reportAuditEvent WAZE_PERSONALIZED_ADS_PERMISSION) — good practice for consent records.
- "Why this ad?" copy: "This ad is based on • Your approximate location • Places that may interest you • Your Google activity such as searches" → cross-Google-service ad targeting.

## Advertising ID sent on every login
- classes5/sources/com/waze/lu.java + c.java: AdvertisingIdClient.getAdvertisingIdInfo; classes7/sources/com/waze/network/f/v.java ~410-440 puts advertisingId + optedOutOfTracking (= isLimitAdTrackingEnabled) into login proto i.b.l.lc (fields advertisingId_, optedOutOfTracking_). LAT is forwarded (server-side honouring not verifiable).
- Client info on each session (classes8/sources/com/waze/network/c/c.java): manufacturer, model, brand, OS, locale, user agent, screen size, coarse location, plus package names of connected Waze-SDK audio/transport apps (network/c/b.java SdkConfiguration.getExternalAppPackageName).
- Android ID used as "push installation UUID" (NativeManager.java:1864 getPushInstallationUUID) and as key material for local password encryption (authentication/bi.java).

## Ads on the map / takeovers
- Takeover ads are pushed from native (AdsNativeManagerBase.showAdvertisementTakeoverJNI → AdsNativeManager.showAdvertisementTakeover); timing logic (ZERO_SPEED_* config: IDLE_SEC, NOT_MOVING_SPEED_MMSEC, START_MOVING_SPEED_MMSEC) is native — cannot confirm zero-speed gating statically, but config names are consistent with ads/popups shown when stopped.
- Labels: "Sponsored", "Ad", plus "AI" badge for generative-AI ads (AD_PREVIEW_ABOUT_THIS_GEN_AI_AD_BADGE, CONFIG_VALUE_ADS_AI_BADGE_ENABLED). "About this ad" warns "Continuing will background Waze. Only tap if it's safe to do so."

## Calendar
- Exported receiver com.waze.CalendarChangeReceiver (PROVIDER_CHANGED) + CalendarUpdateWorker re-read calendar on every change, even when app not started (OfflineNativeManager.updateCalendarEvents).
- classes5/sources/com/waze/calendar/f.java ~60-100 and d.java:127: per event reads title, begin/end, location, rrule, organizer (email normalised to mailto:); skips all-day/location-less events; hands to native (upload to server is native, unconfirmed). Debug log line includes title, location and organizer (f.java:92).
- Facebook events integration strings ("Connect Facebook", "Facebook events") still present.

## Sensors
- classes6/sources/com/waze/location/bw.java: uncalibrated gyroscope (type 16, 200 Hz, bias-corrected), linear acceleration (10, 50 Hz), gravity (9), uncalibrated magnetometer (14), aggregated every ~333 ms incl. max gyro and max linear-acceleration magnitude → LocationSensorListener.lambda$initRotationVectors$1 → native. Used for positioning/dead reckoning; whether harsh-braking style telemetry is uploaded is native/unconfirmed.

## Other nags / copy
- Notification permission request capped by server CONFIG_VALUE_PERMISSIONS_NOTIFICATIONS_MAX_REQUEST_AMOUNT (install/f.java) — bounded re-asks.
- "Find friends from contacts", "You're missing out! Connecting lets you better interact..." (Facebook friends), Carpool "You’re missing out on important carpool updates" — legacy native strings; Carpool service is discontinued, remnants only (33 Java files mention carpool).
- Microphone: "New! Report with voice" (conversational reporting) activation dialog "Turn on" / "Not now".
- Phone-number nudge copy under a key named BY_SKIPPING_THIS_STEP__..._ALL_EXISTING_DATA_..._WILL_BE_LOST (value now neutral: "By entering your phone number you're creating a secure ID...").

## Good practice / checked and cleared
- Contacts: only on-device search of contacts' postal addresses (classes5/sources/com/waze/menus/p.java:193, mimetype postal-address_v2) for "Drive to friends and family"; no Java code reading phone numbers/emails or uploading the address book (native "Find friends from contacts" not verifiable).
- BLE beacon scanning (classes5/sources/com/waze/beacons/f.java, d.java): only Eddystone (UUID FEAA) frames parsed (frame types 0x00/0x20), others dropped — tunnel positioning. Unfiltered scan mode exists if server config disables the filter, but results are still filtered in d.e().
- Installed apps: no getInstalledPackages; <queries> limited to googlequicksearchbox, spotify, com.waze + SDK intent com.waze.sdk.audio.ACTION_INIT; audio app discovery via MediaBrowserService for a specific package (sdk/a/j.java).
- Telephony: call-state listener only (u.java), country ISO for onboarding; no IMEI/phone number.
- Age gate / AADC: "Your age won't be shown publicly or used for advertising purposes"; ads-personalization dialog suppressed and nudge styling removed for age-restricted users.
- allowBackup=false, usesCleartextTraffic=false.
- Privacy settings: "Go invisible", navigation history deletion, data archive; consent/permission choices audit-logged with displayed string IDs.
- Tracker SDKs (Exodus): only Crashlytics; analytics go to Waze's own stats pipeline.
