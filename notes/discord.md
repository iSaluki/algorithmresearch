# Discord 348.10 (Stable) — com.discord — working notes

Paths: Java under work/discord/jdex (classesN/sources/...). Most app logic is React Native JS compiled to Hermes bytecode v98 (`assets/index.android.bundle`, 67 MB). The bundle was disassembled with hermes-dec (P1sec, local scratch copy; supports v98) and the string table was parsed; JS evidence below is cited as `HBC fn #<id> "<name>"` (Hermes function id in that disassembly) plus the module path string the bundle carries (e.g. `modules/quests/native/ATTModal/ATTManager.android.tsx`). UI copy comes from `res/raw/*compiledmessages.jsona` (en-US base and en-GB files; message hash in brackets).

Trackers (Exodus): AppsFlyer, Google Analytics, Sentry. Manifest: 9 dangerous permissions (CAMERA, RECORD_AUDIO, READ_CONTACTS, POST_NOTIFICATIONS, media). No location, no PACKAGE_USAGE_STATS, no QUERY_ALL_PACKAGES. Declares `com.google.android.gms.permission.AD_ID`, `ACCESS_ADSERVICES_ATTRIBUTION`, `BIND_GET_INSTALL_REFERRER_SERVICE`, Samsung `mapsagent.permission.READ_APP_INFO`, Huawei `appmarket...GET_COMMON_DATA`.

## 1. Google Advertising ID sent in first-party analytics on every gateway connect (Quests/ads)
- Native: `classes/sources/com/discord/ads/AdsModule.java` `getGoogleAdvertisingId()` reads AdvertisingIdClient; returns `googleAdvertisingId` = null when Limit Ad Tracking / ads-ID opt-out is on (good), otherwise the raw ID.
- JS: `modules/ads/native/AdUserActionCreators.android.tsx` → `fetchAdUser` (HBC fn #136568): calls getGoogleAdvertisingId, then `track(AD_IDENTIFIER_FETCHED, {has_advertising_id, android_advertising_id: <GAID>, location, success})` and `track(AD_USER_FETCH_DURATION, {..., is_limit_ad_tracking_enabled})`; caches it as `adUser.advertisingId` / `lastFetchedAt` and re-reports the cached ID in later `ad_identifier_fetched` events.
- Trigger: `modules/quests/native/ATTModal/ATTManager.android.tsx` → `onPostConnectionOpen` (HBC fn #76599) calls `fetchAdUser("post_connection_open")`, i.e. on every gateway connection (app start/reconnect). No consent or experiment check in that handler. Other callers: `getAdUser` (fn #42955) and a store change listener (fn #93691).
- The GAID is a cross-app advertising identifier. Here it goes straight into Discord's own analytics stream, tied to the logged-in account, for Sponsored Content / Quests. AppsFlyer also collects it (see 3).

## 2. Installed-games probe sent to server for "game community" recommendations
- Manifest `<queries>` names 32 packages, among them 16 mobile games (Minecraft, Fortnite, Genshin, PUBG Mobile, CoD Mobile, Clash of Clans, Mobile Legends, Free Fire, Pokémon GO, Pokémon TCG Pocket, Clash Royale, Among Us, Monopoly GO, Brawl Stars, Brawlhalla, Wuthering Waves) plus a `roblox` scheme. The rest are social/messaging apps (Messenger, WhatsApp, Telegram, X, LINE, Spotify, Instagram, Twitch, TikTok, Snapchat, Facebook/Lite) and Discord variants.
- Native: `classes/sources/com/discord/intents/IntentsModule.java:84` `canOpenUrlScheme()` → `isPackageInstalled()` (getPackageInfo); package map in `intents/packages/InstalledPackage.java:29-51` and `intents/BuildConfig.java`.
- JS: `modules/local_app_detection/native/LocalAppDetectionStore.tsx` (`isAppInstalled`, `LOCAL_APP_DETECTION_COMPLETE`). `modules/game_community_upsell/native/GameCommunityConfig.tsx` `DETECTABLE_GAME_TO_APPLICATION_ID_MAP` maps each game to a Discord application ID. `getDetectedGameIds` (fn #151550) iterates `ALL_DETECTABLE_APP_NAMES`. The fetch (fn #143947) does `HTTP.get(MOBILE_GAME_COMMUNITIES = "/discoverable-guilds/mobile-game-communities", query {game_ids, limit: 20, ignored_guild_ids})`, which tells the server which of these games are installed.
- Analytics metadata also has `detected_game_id` (fn #33315 `getGameAnalyticsMetadata`). There is an experiment `2026-08-game-community-add-server-entry` (GameCommunityUpsellExperiment.tsx). Whether the detection itself depends on an experiment was not determined.
- The social-app checks feed the invite share sheet (fn #9290: `isAppInstalled(MESSENGER/GMAIL/TELEGRAM/TWITTER/WHATSAPP/LINE)`), which is benign.
- Not found: the older desktop-style running-game detection. There is no UsageStats, no getRunningAppProcesses and no full package enumeration (bare MAIN `<queries>` entry is used only to resolve the contacts app, `ContactSyncManagerModule.getConstants`).

## 3. AppsFlyer started unconditionally at Application start
- `classes/sources/com/discord/MainApplication.java:210` `onCreate$lambda$1` → `DeepLinks.INSTANCE.init()` runs from `onCreate()` (`com/discord/b.java` default case). `classes/sources/com/discord/deep_link/DeepLinks.java:137-139` calls `subscribeForDeepLink`, `init(APPSFLYER_KEY)` and `start(context)`.
- No consent/ATT-style gating. No calls in app code to `anonymizeUser`, `setConsentData`, `stop`, `setDisableAdvertisingIdentifiers` or `enableTCFDataCollection`. So it starts before login and before any privacy setting can apply.
- The SDK also reads Samsung preload attribution provider `content://com.samsung.android.mapsagent.providers.apptracking/info` (`classes/sources/com/appsflyer/internal/AFj1uSDK.java:35,70`, matching manifest `<queries>` and permission), Huawei AppGallery referrer and the Play Install Referrer, and declares ACCESS_ADSERVICES_ATTRIBUTION (Privacy Sandbox).
- Stated purpose in code is deferred deep links (`getDeepLinkDestinationWithAppsFlyerParam`). The SDK still performs install attribution with GAID.

## 4. Contact upload: phone numbers in plaintext, re-synced on every connection
- `classes/sources/com/discord/contact_sync/ContactSyncProvider.java:getContactsMap` reads Phone.CONTENT_URI (`data4` normalized number, display_name, photo flag, contact_id) plus given/family name (Data `vnd.android.cursor.item/name`). It can also base64-encode contact thumbnails (`getImageForContactId`, user-facing).
- `contact_sync/react/ContactSyncSerializerKt.serializeSyncContactResult` returns a local "blob" (names) and the upload payload `ContactSyncPayloadEntry{friend_id = phone}` (`ContactSyncPayloadEntry$$serializer.java:34`). No hashing.
- JS upload (fn #140811): `PUT CONNECTION_SYNC_CONTACTS {friend_list_entries, background, allowed_in_suggestions, include_mutual_friends_count:false}`. Names appear to be stored locally (`CONTACT_SYNC_STORED_CONTACTS`). No upload of names was seen.
- Re-sync: contact-sync module `handleConnectionOpen` (fn #110238) checks `isContactSyncEnabled` + permission on every POST_CONNECTION_OPEN. The copy discloses it: [BoR0dO] "Discord can connect you with your friends and help them find you. Your contacts will be regularly sent to us."
- Opt-in flow requires a verified phone number first ([qFmzyo]). Discoverability setting "Allow contacts to add me".

## 5. Loss-framing / friction when turning off analytics and personalization
- [OdPCbN] "Turn off use data to improve Discord?" + [MGWabA] "If you turn this off, we'll stop processing new data for analytics. You will lose access to new experimental features and usage-based improvements to features like voice chat. If you'd like to further assert your right to object to our processing of your data, email privacy@discord.com." So a full objection requires email.
- [gJvDDh] (personalization off): "By turning this off you lose access to things like personalized recommendations and suggestions. You won't be able to recover them in the future!"
- JS `handleUsageStatisticsChange` (fn #67548) shows the confirm modal before `setConsents(USAGE_STATISTICS)`.
- Client-side, `hasConsented(USAGE_STATISTICS)` gates only search analytics IDs (`getSearchAnalyticsIds` fn #59054). No client-side gate on the main `track()` pipeline (`/science`) was found, so honouring the opt-out appears to be server-side (not verifiable statically).

## 6. Server-switchable fine-grained touch / HTTP telemetry ("zoomed-in analytics")
- Native `classes/sources/com/discord/analytics/touch/TouchLogger.java` + `TouchEventAnalyticsModule.java:109` records every touch/gesture: `touch_action_type, screen_x/y, view_x/y, view_hierarchy, window_name, gesture, distance, velocity, duration_ms, scale_factor, memory`. It goes into `TelemetryRing` (local SQLite ring) on channel `ZOOMED`.
- JS `TouchEventAnalyticsManager.updateEnabledState` (fn #66633) enables it if `user.isStaff()` OR the user-level experiment `2025-12-zoomed-analytics` (`ZoomedInAnalyticsExperiment.tsx`, default config `{enabled:false}`). The ZOOMED channel also captures `HTTP_REQUEST` and `WEBSOCKET_MESSAGE_RECEIVED` (`ZoomedInAnalyticBuilder.tsx`, `trackZoomedInHttpRequest.android.tsx`). `exportEntries` → `buildZoomedInAnalyticsEvent` → analytics events.
- Shipped default is off for non-staff. It is a session-replay-like capability that the server can turn on per user.

## 7. Sentry (third-party, sentry.io) not consent-gated; user-interaction breadcrumbs
- `classes/sources/com/discord/crash_reporting/CrashReporting.java:823-840`: DSN on `o64374.ingest.sentry.io`. Sample rate 5% for prod (100% for staff / Meta Quest / non-prod). Disabled only on Vivo devices (`isDisabled`). `setEnableUserInteractionBreadcrumbs(true)`, system-event / app-component breadcrumbs, MAX_BREADCRUMBS 5000, `beforeSend` scrubber present. Manifest `io.sentry.auto-init=false` (manual init). No privacy setting check.

## 8. Nitro / Orbs monetisation pressure
- Trial urgency: [GPqVWT] "⏰ Only {days} left to claim your {trialPeriod} Nitro trial for $0!". Referral: "Send a 2-week trial and save 30% on Nitro for every friend who subscribes."
- Churn machinery: bundle strings `CHURN_USER_OFFER`, `fetchChurnDiscountOffer`, `CHURN_DISCOUNT_POPOVER/PERSISTENT_CTA/PREMIUM_TAB_BADGE/COACHMARK`, `TIERED_TENURE_BADGE_CHURN_REMINDER`, `PREMIUM_CHURNING`. These are retention discounts and a reminder about losing the tenure badge. Cancel flow: "Are you sure you want to cancel?", "On {date}, you'll lose access to:".
- Gifting streak nudge: [oqDrEM] "Send one more gift to unlock the coveted next level in your gifting streak." Quests upsell: "Turn your wins into mega wins with {N}x rewards when you subscribe to Nitro."
- Good: auto-renew disclosure present ([COObWR] "recurring subscription ... continue to charge you every {interval} until you cancel"), pause option exists.

## 9. Sponsored Content / Quests and teens
- Settings: "Use my Discord activity to personalize Sponsored Content" / "Use third-party data to personalize Sponsored Content" ([cf9mvV], [2QFDU/]: "If you opt out, you may still see Quests"). Family Center versions exist for teens ([cnCK6b] "your teen may still see Quests"), so teens are shown sponsored Quests. Defaults are server-side (not determinable).

## 10. Age assurance / inferred age
- [1DN29p] "We use technologies that assess user age groups based on patterns of behavior and other signals associated with user accounts on Discord." k-ID video selfie / ID scan ([2yLvkS] "Video selfie via k-ID", [ARmJ0M]). [El4aXl] "only used to confirm your age group, then it's deleted". Account deletion threat if not verified ([3axQdB]). Guardian-connection requirement for 13–16 in some regions ([5jm+T3]).

## 11. Exported, unauthenticated Social-SDK RPC service (Low)
- Manifest: `com.discord.socialrpc.DiscordRpcService` exported, no permission. `classes/sources/com/discord/socialrpc/DiscordRpcService$binder$1.java` `connect(applicationId, ...)` does not check the caller (no getCallingUid / signature check). Any installed app can open a session claiming any applicationId and send `SET_ACTIVITY` frames, setting the user's Rich Presence (rate-limited 5 s, max 10 connections). Returns a PLACEHOLDER_USER, so no identity leak (`SocialRpcSessionManager.java:548-555,866`). Whether the server validates the application ID is unknown.

## Other observations
- Notification pre-prompt (`PUSH_NOTIFICATION_PREPROMPT`, "Turn on notifications so you never miss a message from your friends."). Feature: "Allow friends to receive a push notification when you come online" (engagement; default unknown).
- Screenshot ContentObserver (`bug_reporter/ScreenshotContentObserver.java`) reads only MediaStore rows under "screenshots/" to offer "Create bug report from screenshot". Appears to be an internal/staff feature. Not exfiltrated.
- Clipboard: native module only writes (`command_clipboard/CommandClipboardModule.java`). JS reads occur only in explicit paste/login-code handlers (fns #153162, #142342). No background polling.
- Google Analytics (gms.analytics) services are in the manifest, but no app-code call site was found (`classes3/sources/qe/a.java` is SDK internal). Likely an unused transitive dependency.

## Good practice / checked and cleared
- Ad ID is nulled when Limit Ad Tracking is on (AdsModule onSuccess).
- No location permission. No usage stats. No QUERY_ALL_PACKAGES. allowBackup=false.
- Contact sync is opt-in, permission-gated, discloses the recurring upload, and has a discoverability toggle.
- Subscription auto-renew copy is clear. Pause offered as an alternative to cancel.

## Limitations
- Hermes JS was examined from disassembly, not decompiled source. Control flow was read manually for the functions cited. Server-side experiment defaults and consent enforcement cannot be seen.
- Only ~11.6k en-US/en-GB messages ship in res/raw. Some main-app copy (e.g. full Nitro cancel flow) may be downloaded at runtime.
- 37 of 153,899 Hermes functions failed to disassemble.
