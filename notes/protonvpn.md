# Proton VPN 5.20.57.0 — ch.protonvpn.android — working notes

Paths under work/protonvpn/jdex (classesN/sources/...). Build flavor in Kotlin metadata: `app_productionVanillaOpenSourceRelease`, the open-source/F-Droid flavor with no Play Billing permission. The coordinator says the APK is signed by F-Droid, not Proton. I did not re-verify the signing cert. The Play build differs: it has billing and the MMP/Sentry wiring noted below.

Trackers (Exodus): Sentry. Permissions: 12, dangerous only CAMERA (QR login) and POST_NOTIFICATIONS. QUERY_ALL_PACKAGES declared (split tunnelling app picker). allowBackup=false. `android.webkit.WebView.MetricsOptOut=true`.

## 1. Usage telemetry is opt-out (default ON) and includes ISP and real country (Medium-Low)
- `classes2/sources/com/protonvpn/android/settings/data/LocalUserSettings.java:459-460`: `telemetry` defaults to `true` when absent.
- Settings copy: "Share anonymous usage statistics" / "Usage data helps us overcome VPN blocks and improve app performance." / "These statistics do not contain your IP address, and they cannot be used to identify you. We'll never share them with third parties."
- Events (`telemetry/TelemetryEvent.java`: `timestamp, event, values, dimensions`) are batched by `telemetry/a.java` and uploaded by `TelemetryUploadWorker` to `data/v1/stats/multiple` (`sf/k.java:73`). Groups seen: `vpn.any.connection`, `vpn.any.upsell`, `vpn.any.onboarding`, `vpn.any.settings`, `vpn.any.product_prompts`, `vpn.profiles`, `vpn.any.tv_signin`.
- Connection dimensions (`jj/b.java`) include `isp`, `user_country` (the pre-VPN location returned by Proton's API, `models/vpn/UserLocation.java`), `user_tier`, `vpn_status`. Others include `vpn_country`, `server_features`, `outcome`, `vpn_trigger`. These are coarse, but ISP + country + tier + timing is quasi-identifying for a privacy product, and they are collected by default.

## 2. Free-tier "Change server" cooldown upsell (Low)
- `appconfig/AppConfigResponse.java:234-244` defaults: `changeServerAttemptLimit=4`, `changeServerShortDelayInSeconds=90`, `changeServerLongDelayInSeconds=1200` (20 min). Server-configurable via app config (`vf/k.java:68`, `vf/i.java`).
- Copy `server_change_upsell` "Get unlimited changes with VPN Plus." This is an artificial wait used as an upgrade lever. It is disclosed but is a friction pattern.

## 3. Server-driven promo offers with countdowns, plus upsell surfaces (Low)
- `promooffers/` handles API notifications (`ApiNotification` StartTime/EndTime, Offer panels, prominent banners, full-screen image offers, `PromoOfferActivity`). Copy `offer_time_left` "%1$s %2$s left", `plans_limited_offer` "Limited time offer". NPS survey (`promooffers/usecase/PostNps.java`, `NpsActivity`).
- Upsell copy: "Access all countries with VPN Plus", "Upgrade to choose any server", `notification_streaming_blocked_title/text` "Streaming not working? ... Upgrade to Proton VPN Plus to bypass these blocks", restrictions upsell (`restrictonsupsell/RestrictionState.java`). Price disclosure is good ("Welcome offer. Auto renews at %1$s/year").

## 4. Proton Core anti-abuse "challenge" frames during sign-up/login (Low, disclosed by Proton generally)
- `classes3/sources/me/proton/core/challenge/` (`ProtonMetadataInput`, `ProtonCopyPasteEditText`, `data/frame/ChallengeFrame.java`). Records per-field behaviour on username/recovery inputs: `timeOnField, clickOnField, copy/paste lists (pasted text read from clipboard on paste, ProtonCopyPasteEditText.java:62-90), keydown lists (keyList)`. Device frame: `appLanguage, timezone, timezoneOffset, deviceName (numeric), regionCode, rooted, fontSize, storageCapacity, darkMode, keyboards`. This is bot-detection fingerprinting sent with auth requests. Scoped to auth screens.

## Sentry / attribution in this (F-Droid) build — effectively off
- Sentry: `pl/s0.java:100-103` initialises with `setDsn("")` (empty string, `CoreConstants.EMPTY_STRING`), so no events can be sent. Session tracking and user-interaction/activity breadcrumbs are disabled anyway. `beforeSend` (`s0.i`) also drops events unless the crash-report setting allows (`a.n()`). A random `sentry_installation_id` UUID is generated locally (`s0.f`). The Play build presumably sets a real DSN; the toggle "Share anonymous crash reports" gates it.
- MMP (in-house install/purchase attribution: `mmp/events/data/MmpEventRequestBody` fields `asid, install_ref, is_reinstall, price, currency, coupon_code, transaction_id, is_free_to_paid`): in this flavor `lh/a.java` `saveMmpEvent` is an empty no-op, so nothing is recorded. The Play build likely records purchase attribution events.

## Good practice / checked and cleared
- QUERY_ALL_PACKAGES / `getInstalledApplications` (`vg/j.java:267`) is used for the split-tunnelling app list only.
- No ad SDKs, no ad ID, no location permission, no contacts. Clipboard reads only in the auth challenge paste handler and AndroidX/Compose text fields.
- Telemetry and crash toggles exist in settings with clear copy. Kill switch relies on Android's always-on VPN / block-without-VPN, which the app links to (not audited in depth).

## Limitations
- Signing certificate not re-verified here. Play build not analysed.
- Telemetry gating on the setting was traced to a settings flow in `telemetry/a.java` (obfuscated). Exact enforcement was not line-verified.
- Promo-offer timing and change-server limits are server-driven.
