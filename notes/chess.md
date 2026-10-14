# Chess.com 4.10.20-googleplay (com.chess) — working notes (paths under work/chess/jdex; app code is only lightly obfuscated, many com.chess classes were relocated to com.google.android.* by R8)

## Tracking consent fails open: every category is "consented" unless a server flag turns OneTrust on
- Consent layer = OneTrust headless SDK (classes9/sources/com/google/android/TrackingConsentImpl.java; real name com.chess.trackingconsent.TrackingConsentImpl). Categories (TrackingCategory.java): PERFORMANCE C0002, FUNCTIONAL C0003, TARGETING C0004, SOCIAL_MEDIA C0005.
- `state` = flatMapLatest over FeatureFlag TRACKING_CONSENT ("tracking_consent", shipped default **false**, classes6/sources/com/google/android/FeatureFlag.java). When the flag is false the state is `TrackingConsentState.Companion.a()` which puts **Boolean.TRUE for all four categories** (TrackingConsentState.java:38-44). OneTrust is only started (startSDK on cdn.cookielaw.org) when the flag is on; then consent = getConsentStatusForGroupId()==1.
- No `showBannerUI`/`shouldShowBanner` call exists in app code; only `showPreferenceCenterUI` from Settings (TrackingConsentImpl.c()). So any banner depends on server flag + OneTrust config (not visible statically).
- What the consent switches gate: Crashlytics/Bugsnag (PERFORMANCE, MainApplication.r0), AppsFlyer start/stop (TARGETING, classes6/.../appsflyer/impl/AppsFlyerManager$initialize$2$1$1.java), UID2 email identity (TARGETING), and Aditude "non-personalised ads" flag (TARGETING).
- Ads themselves are NOT gated on consent: AditudeAdsInitializer adsEnabled = (session show_ads || FORCE_INTERSTITIALS) && !aditude_ads_killswitch (classes8/sources/com/confiant/android/sdk/AditudeAdsInitializer.java:137 + ...$special$$inlined$combine$1.java:170-182); consent only toggles `setNonPersonalizedAdsFlag(!targeting)` (Aditude.j()).

## UID2: user's account e-mail turned into a cross-publisher ad identity
- classes8/sources/com/confiant/android/sdk/UID2Identity.java:83-90 — `UID2Manager.generateIdentity(email, subscriptionId, serverPublicKey)` (client-side token generation, UID2 operator receives normalised/hashed email); token passed to the ad wrapper as ExternalUserId source "uidapi.com" (Aditude.l(), Aditude.java) → bidstream (Prebid/GAM).
- Gate (UID2Identity$initialize$3.java): FeatureFlag ADS_UID2_SDK ("ads_uid2_sdk", default false) && ads SDK initialised && TARGETING consent (defaults TRUE when tracking_consent flag is off) && email non-blank. Targeting key `ads_uid2_sdk=1` also sent (…initializeTargeting…combine$1.java:247).
- No age check anywhere on this path (LoginData has no age field; see minors section).

## Ad stack and minors
- Ad wrapper = Aditude (com.tude.AditudeWrapper, app id/public key in Aditude.java static block) over GAM/AdMob + Prebid + Amazon APS + AppLovin/InMobi/Liftoff(Vungle) mediation; Confiant ad-quality scanner (flag "confiant").
- `setShareGeoLocation(false)` on Aditude (Aditude.java static) — good.
- Server-assigned "gam_audiences" from the user's properties_json are pushed to GAM global targeting (Aditude.k()).
- **No child-directed / under-age signals in app code**: no setTagForChildDirectedTreatment / setTagForUnderAgeOfConsent / setIsAgeRestrictedUser / max ad content rating anywhere outside SDKs (only `RequestConfiguration.Builder().setTestDeviceIds` in classes2/sources/com/google/android/e0.java:124). Whether a child sees ads is decided only by server booleans `show_ads` / `show_interstitial_ads` in LoginData (classes8/sources/com/chess/net/model/LoginData.java). UserData carries `date_of_birth` but it is not used client-side for ads. An age-assurance proto (chesscom/user_age_assurance/v1alpha ReportAgeAssuranceRequest: age_lower/age_upper, provider GOOGLE_PLAY) exists but has no callers and no Play Age Signals library is bundled.
- Signup strings contain no birthday/age gate.

## Interstitials between games, server-scheduled, including in-house "Go Premium"/"No Ads" video ads
- Proto chesscom/ads/v1 (classes4): InterstitialFrequency {daily_cap, timeout_minutes}, InterstitialSchedule {lineup, carousel}, InterstitialType FULLSCREEN / NATIVE / INTRODUCTORY / INTERNAL_VIDEO_GO_PREMIUM / INTERNAL_VIDEO_NO_ADS, InterstitialFeatureType LIVE_GAME / BOT_GAME / DAILY_MOVE, InterstitialVideoConfiguration.skip_delay_seconds, InterstitialThirdBlade NO_ADS. All caps are server-side; no client cap.
- Flags (default false): force_gameplay_interstitials, mobile_interstitials_on_every_seek, interstitials_daily_moves, interstitials_bot_games, ads_preloading_*.
- Copy: ads_primer_title "Ads Help Keep Chess Free" (used in native interstitial, classes6/.../ads/interstitials/internal/nativ/d.java:230); upgrade_no_ads_ads_help_us_grow_chess "Ads Help Us Grow Chess. But You Can Upgrade To Remove Them!".
- Rewarded-video strings ("Or Watch a Video to Unlock this Game Review") exist but have no code reference (dead/iOS-shared).

## Premium upsell / monetisation pressure
- Freemium limits with upsell: game_review_upgrade_dialog_header "You've used your free Game Review for the day."; A/B variants "Increase your rating 2.7x faster." / "Frequent users of Game Review improve 2.7x faster"; lessons_limit_reached_message "Upgrade now to improve with unlimited lessons!". Flags bypass_game_review_limit_modal_experiment, monetization_modal_updates_experiment, condensed_paywall_* experiments.
- Onboarding contains TRY_PREMIUM and SALE steps (classes9/.../welcome OnboardingStep "TRY_PREMIUM", "SALE"); home shows a periodic upgrade modal (PeriodicUpgradeDialogResolver, prefs `<user>_weeklyUpgradeLastSeenTimestamp`, `guestWeeklyUpgradeLastSeenTimestamp`; killswitch home_upgrade_modal_killswitch) plus spring-sale dialogs once per "sale group".
- Sale countdown "Offer Ends In:" (PaywallTimerKt) — **checked**: end time is the server `saleExpiresAt` and the timer is only shown inside the last N hours before that real expiry (classes7/sources/com/android/billingclient/api/n0.java). Not a fake evergreen timer (as far as the client is concerned). Preview-only fake timer in classes7/.../ui/a.java (Compose preview data).
- Winback: "Limited Time Offer", "50% Off", "Restart Premium and Get".
- Coach nudges with unverifiable performance claims: coach_nudge_game_review_1 "Players who do Game Review add +85 to their rating on average!", coach_nudge_lessons_1 "+107", "2.9x faster", coach_nudge_lessons_4 "Are you improving? If not, do this one lesson and you will!".
- Trial disclosure is good: trial_end_description_arg "You'll be charged on %s. Cancel anytime before."; trial_reminder_title "We'll Remind You 2 Days Before Your Trial Ends" (FreeTrialTimelineContentKt.java:595); no-ads plan auto-renew disclosed.

## Streak loss-aversion (widget + notifications)
- Home-screen streak widget (SmallStreakWidgetReceiver/LargeStreakWidgetReceiver) with default copy table (classes9/sources/com/google/android/datastore/C0697a.java, overridable server-side via configurator StreakCopyRepositoryImpl): "Don't lose your streak!", "1 game from a year streak!", **"Are you really going to lose your 1 year streak?"** (widget_streak_frozen_one_year_warning).
- Push copy: notification_play_streak_ending_body "Last Chance: Play a quick game to save your streak.", "Your Streak is Paused! ⏸️"; onboarding STREAK_WIDGET step "Keep your streak alive with a home screen widget".
- Local re-engagement notifications: WorkManager unique work "local_engagement_notifications" (classes6/sources/com/chess/notifications/service/local/e.java), schedule from server config "local_notification_control_config" with delay_days/delay_hours and cooldown_in_days (d.java, GetNextEligibleNotification.java); gated by flag local_push_notifications_v1 (default false). Copy e.g. "Hi %1$s! 👋", "How about a game of chess?", "How many chess puzzles can you solve in the next 3 min? Can you do 10?".

## Contact upload (hashed) with standing contact-match notifications
- classes6/sources/com/google/android/connect/invite/contacts/service/ContactsMatcherImpl$getMatchingContacts$2.java:200-233 — for every contact: each email and each phone (normalised to E.164 with SIM/network country) → **unsalted SHA-256** (ContactsMatcherImpl.g(), MessageDigest SHA-256) → UserContact{device_id (random app UUID, DeviceId.java), contact_id (local contact key), tokens} → Twirp UploadContacts. Names are not uploaded. Analytics event ContactsUploaded with counts.
- Triggered from onboarding FRIENDS_PRE_PROMPT step (SignupViewModel$loadContactsIfNeeded$2 / $uploadContacts$2) and Friends > Contacts screens, after READ_CONTACTS grant.
- Disclosure search_contacts_permission_explanation: "We ONLY use this information to search your contacts and do not share this with 3rd parties." — but the app also has a "Contacts Signups" push category ("Get notified when one of your contacts create an account"; notification_contact_matched_title_arg "%1$s is Now on %2$s 🤝"), which implies the server retains the hashes of non-users for later matching. Unsalted SHA-256 of phone numbers is trivially reversible.
- Reverse direction: social_setting_allow_friend_find_via_contacts "Allow friends to find you via contacts" (setting exists; default not visible).

## Other data collection
- Screenshot detection: DETECT_SCREEN_CAPTURE + Activity.ScreenCaptureCallback on configured activities → analytics event ScreenshotTaken (classes9/sources/com/chess/utils/android/basefragment/g0.java). Anti-cheat CheatMetadata (focus/blur per move, move hold times, pointer offsets, screenshot_detected_moves) — fair-play telemetry (CheatDataDelegateImpl, flag cheating_detection).
- Crash reporting tags user id+username, PLAYER_STATUS, SHOW_ADS and INSTALL_SOURCE (MainApplication.z0).
- Approov attestation SDK: getInstalledApplications(128) (classes9/sources/com/criticalblue/approovsdk/AttestationCallback.java:124) and SHA of ANDROID_ID (approovsdk/b.java:145) — anti-tamper; package visibility limited by <queries> (no QUERY_ALL_PACKAGES).
- AppsFlyer: customer user id = server bucketing id; events af_complete_registration, af_start_trial/af_subscribe; uninstall tracking via FCM token; enableTCFDataCollection(true).
- First-party analytics (chesscom/user_activity/v1 Context): device brand/model/random id, OS, screen; client sends Location=null and Network=null (AndroidEventContextProvider.java:104-118).

## Good practice / checked and cleared
- Facebook SDK: AutoInitEnabled=false, AutoLogAppEventsEnabled=false, and `FacebookSdk.setDataProcessingOptions(["LDU"],0,0)` (Limited Data Use, geolocated) at startup (MainApplication.n0). Only used for login/share.
- Crashlytics collection off in manifest until PERFORMANCE consent resolves (true by default though, see above).
- Location: FINE only maxSdk 30 (BLE board scanning on old Android); COARSE requested only for WebView geolocation prompts from chess.com hosts (WebViewModel.W6, WebViewFragment.I). No app-level location reads; ad wrapper geo sharing off.
- BLUETOOTH_SCAN neverForLocation (connected e-boards).
- No installed-app enumeration by app code; <queries> list is FB/IG + generic intents.
- PII redaction regex for logs (email/password/token/phone/name/date_of_birth) in classes8/sources/com/chess/net/serialization/g.java.
- Sale timer bound to real server expiry (see above).
- Trial reminder + clear auto-renew copy; cancellation via Google Play (no in-app obstruction found).
- Notification permission home prompt is a single dialog behind a killswitch (HomeDialogsManagerImpl.i(), home_notification_prompt_killswitch), no escalating re-prompt chain found.
