# Signal 8.30.3 — org.thoughtcrime.securesms — working notes

Paths under work/signal/jdex (classesN/sources/...). Code is R8-shrunk but keeps most names. This build ships Play Billing and Google Play Services (FCM, Maps, Wallet) — it is the Play/website flavor.

Trackers (Exodus): 0. Manifest: `firebase_analytics_collection_deactivated=true`, `google_analytics_adid_collection_enabled=false`, `firebase_messaging_auto_init_enabled=false`, `android.webkit.WebView.MetricsOptOut=true`. FCM is used only as a wake-up channel. The app can fall back to a websocket (`SettingsValues.forceWebsocketMode`).

## 1. Megaphone (in-app banner) cadence — the main "nag" surface, generally restrained
`classes4/sources/org/thoughtcrime/securesms/megaphone/Megaphones.java:176-196` (buildDisplayOrder). Only the first eligible megaphone is shown (`getNextMegaphone`). Schedules:
- NOTIFICATIONS ("Turn on Notifications?" / "Never miss a message from your contacts and groups.", Not now): every 30 days (2592000000 ms) while notifications/channels are disabled. Suppressed if the copy isn't translated in the user's locale.
- GRANT_FULL_SCREEN_INTENT (Android 14+, "Turn on full screen notifications?"): every 3 days (259200000 ms) while not granted.
- BACKUP_SCHEDULE_PERMISSION (exact alarms, if backups on): every 3 days.
- Paid-backup upsells (BACKUPS_GENERIC_UPSELL "Turn on Signal Secure Backups"; BACKUP_MESSAGE_COUNT_UPSELL ">1000 messages", "Never lose a message"; BACKUP_MEDIA_SIZE_UPSELL >1 GB media on free tier, "Paid Signal Secure Backup plans keep all your media, up to 100GB"; BACKUP_LOW_STORAGE_UPSELL when <10% disk free, "Save space with paid backups"): `BackupUpsellSchedule.java` enforces a global ≥60 days between any two backup upsells, then gaps of 60/120 days per megaphone. The generic one also needs remote flag `backupsMegaphone` and >7 days since install. All have "Not now".
- REMOTE_MEGAPHONE (server-defined, includes donation asks): `RecurringSchedule.every(1 day)` as the base, but per-megaphone snooze durations come from the server (`snoozeDurationDays`, `RemoteMegaphoneRepository.checkSnooze`). Countries/conditions are filtered too. Donate condition `standard_donate` (`shouldShowDonateMegaphone`): ≥7 days since install, registered, a payment method is available, no pending donation, and the user has no Donor badge. `MIN_TIME_BETWEEN_DONATE_MEGAPHONES` = 30 days is measured against the legacy DONATE events. Real frequency is therefore server-controlled.
- PIN_REMINDER ("Verify your Signal PIN"): `SignalPinReminderSchedule` + `lock/SignalPinReminders.java`. Intervals step up 3 d → 1 w → 2 w → 4 w (cap) after each correct entry, and step back down after a failed one. Off if reminders are disabled or the user opted out of PIN. Can be disabled in settings.
- ADD_A_PROFILE_PHOTO, SET_UP_YOUR_USERNAME (3 days after choosing "not discoverable by phone"), PNP_LAUNCH: shown until completed/dismissed (ALWAYS while eligible, but dismissible "Not now"/"Dismiss" ends them).
- Security/ops megaphones: NEW_LINKED_DEVICE, LINKED_DEVICE_INACTIVE (every 3 days in the last week before unlink), INACTIVE_PRIMARY (weekly), TURN_OFF_CENSORSHIP_CIRCUMVENTION (weekly), CLIENT_DEPRECATED (fullscreen, no snooze — app expired).
- No payments (MobileCoin) or Stories promotion megaphones exist in this version (BECOME_A_SUSTAINER / DONATE_Q2_2022 are legacy keys only).

## 2. Donation asks (Low)
- Remote megaphones above, plus a Release Notes chat update type `RELEASE_CHANNEL_DONATION_REQUEST` (`database/MessageTypes.java:87`, copy `MessageRecord_like_this_new_feature_help_support_signal_with_a_one_time_donation` "Like this new feature? Help support Signal with a one-time donation."). Shown in the Signal Release Notes chat, styled with an action button (`conversation/ConversationUpdateItem.java:348-352`).
- Copy is non-manipulative ("Donate to support private messaging. Keep Signal independent and ad-free."). Donors (badge) are excluded.

## 3. Contact discovery
- `contacts/sync/ContactDiscoveryRefreshV2.java:143-149` `refreshAll`: system contact numbers (E.164 only, no names) → `CdsiV2Service` (classes5 `org/whispersystems/signalservice/api/cds/CdsiV2Service.java`) using libsignal `CdsiLookupRequest` over an attested channel to the SGX enclave. Incremental via token (`previousE164s`/`newE164s`). Numbers are not hashed but are encrypted end-to-end to the attested enclave.
- READ/WRITE_CONTACTS + account/sync adapter: Signal adds "Signal" raw contacts to the system address book (standard Signal behaviour, user-visible).
- "Notify when contact joins Signal" setting exists (`SettingsValues.isNotifyWhenContactJoinsSignal`).

## 4. Location / Google dependencies (Low, user-initiated)
- Location only when sending a location attachment (`maps/PlacePickerActivity.java:171,363,395`, `mms/AttachmentManager.java:257`). Uses Google Maps SDK + Android `Geocoder.getFromLocation` (`PlacePickerActivity.java:101`). With Play Services, the coordinates of the picked place go to Google for reverse geocoding.
- Device-transfer requests NEARBY_WIFI_DEVICES / FINE_LOCATION for Wi-Fi Direct (`devicetransfer/DeviceTransferSetupFragment.java:1131`).

## Good practice / checked and cleared
- No analytics/ads SDKs, Firebase Analytics deactivated, ad-ID collection disabled.
- Link previews fetched through Signal's content proxy `contentproxy.signal.org` (`BuildConfig.java:20`, `net/ContentProxySelector.java`), so the sender's IP is hidden from the site. Toggle `settings.link_previews`.
- Every megaphone has a dismiss/"Not now" and is rate-limited. Notification nag is monthly, not per-launch.
- Debug-log upload is user-initiated only.

## Limitations
- Remote megaphone content and snooze arrays are server-delivered, so actual donation frequency can't be fixed statically.
- Did not audit WebRTC/calling or the backup cryptography.
