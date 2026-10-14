# BBC News — UK edition 9.19.0 (bbc.mobile.news.uk) vs International edition 2026.9.0 (bbc.mobile.news.ww) — working notes
Paths: UK under work/bbcnews/jdex (native Kotlin, R8-obfuscated defpackage), WW under work/bbcnews_ww/jdex (React Native/Expo app: most logic is in Hermes bytecode assets/index.android.bundle, v98 — only string table inspected, not decompiled; native bridge modules in classes10/sources/com/mobile/*).

## Summary of the two builds
- UK: no ad SDKs at all (no com.google.android.gms.ads, Prebid, Permutive; play-services ads-identifier class not even bundled). Trackers: BBC "Echo" analytics wrapper → ATInternet/Piano (ATI), Comscore, BBC BAG, UKOM (dotmetrics/Ipsos), BARB/Kantar SpringStreams (AV), AppsFlyer, Chartbeat, Optimizely, Urban Airship (push), Firebase Crashlytics/Remote Config.
- WW: ad-funded + subscription (com.android.vending.BILLING, Piano Composer paywall). Adds Google Mobile Ads (GAM, app id in manifest + assets/app.config "This identifier will be used to deliver personalized ads to you."), Prebid, IAB OMID, **Permutive DMP**, Firebase Analytics, BBC Federated-ID, Sourcepoint CMP (GDPR + USNAT campaigns), Optimizely (JS + ODP events), Chartbeat, Comscore, UKOM, transistorsoft background-fetch, RootBeer.

## WW: Firebase Analytics on from first launch with all Google consent-mode signals defaulted to GRANTED
- AndroidManifest meta-data (work/manifests/bbcnews_ww.manifest.json): firebase_analytics_collection_enabled=true, google_analytics_adid_collection_enabled=true, google_analytics_ssaid_collection_enabled=true, google_analytics_automatic_screen_reporting_enabled=true, **google_analytics_default_allow_analytics_storage / ad_storage / ad_user_data / ad_personalization_signals = true**; com.google.android.gms.ads.DELAY_APP_MEASUREMENT_INIT=false.
- MainApplication.onCreate calls FirebaseApp.initializeApp before React Native/Sourcepoint has run (classes10/sources/com/mobile/MainApplication.java). No native setConsent call; the JS string table contains "setAnalyticsCollectionEnabled()" but no "setConsent", so any later downgrade depends on JS (not verifiable without Hermes decompile). Net: first_open/session/screen_view events with ad ID + SSAID can leave before the user sees the CMP; consent-mode defaults claim consent was given.

## WW: Permutive DMP fed with BBC federated IDs, page/video behaviour; identity call not gated by the consent flag
- classes10/sources/com/mobile/permutive/PermutiveModule.java: native flag isPermutiveAllowed (set by JS startSDK/stopSDK). createPageTracker/video trackers check it, but **updateIdentity() does not**: it lazily constructs the Permutive SDK and calls setIdentity with aliases "fed_id_v2" (BBC user federated id, priority 2) and "fed_id" (device federated id, priority 3).
- Page tracking sends title, URL, referrer and properties prod/pillar/sect/pagetype/page_id; video events send name, description, video_id, published_at, duration; video-ad events also ad_id, advertiser_name. getCohorts exposed to JS (cohorts → ad targeting). getGoogleCustomTargeting returns an empty map (stub).
- BBC Federated ID (classes4/sources/uk/co/bbc/federated_id_client_android/FederatedIDHelpers.java, com/mobile/fedid/FedIdManager.java): app-generated device id, then server endpoint ENCRYPT_FOR_ALL_THIRD_PARTIES returns per-partner encrypted device ids; JS string "gamFedIds" suggests these go to Google Ad Manager. Per-partner encryption limits cross-partner joining (mitigation), but it is still a persistent cross-session ad identifier shared with vendors.

## WW: other identifiers
- GAIDModule (com/mobile/gaid/GAIDModule.java): returns the Google Ad ID to JS, **honours Limit Ad Tracking** (returns null if LAT); JS string "GAID stored in device ID".
- AnalyticsManager.setDeviceId → Echo property device_first_party_id; Comscore consent label cs_ucfr set from JS (setComscoreceUserConsent) — good.
- READ_PHONE_STATE declared (manifest line 6, no maxSdk). Only user: Kantar SpringStreams (classes11/sources/de/spring/mobile/SpringStreamsBase.java:201/554) which calls TelephonyManager.getDeviceId() (IMEI) if the permission is held. No runtime request found in native code (JS unverified); on Android 10+ IMEI is blocked for normal apps. Over-declared, legacy IMEI capability.
- Text-selection menu (com/mobile/customtext/CustomTextSelectionHelper.java): Copy / Select all / "Web search" actions emit onTextSelectionMenuAction with **selectedText** to JS; JS has "trackTextSelectionMenuAction" → selection actions are analytics events; whether the selected text itself is sent is not verifiable statically.
- JS strings show scroll_depth tracking and Chartbeat engaged-time (Tracker.userInteracted, logged-in/anonymous flag, sections/authors) — normal publisher analytics.
- Background fetch (transistorsoft) periodic JS task; NetInfo "shouldFetchWiFiSSID" option present but no location permission → SSID not readable.

## WW consent UI
- Sourcepoint (com/mobile/sourcepoint/SourcePointModule.java): campaigns GDPR + USNAT (SUPPORT_LEGACY_USPSTRING, TRANSITION_CCPA_AUTH); privacy-manager entry points onGDPR/CCPA/USNATPrivacyManagerTap; JS has hasConsentForAdStorage / hasConsentForAdsPersonalization / hasConsentForDataUsage, so some JS gating exists. Message layout (accept vs reject symmetry) is server-rendered — not checkable statically.
- Usercentrics SDK is also bundled (pulled in by dotmetrics; com/usercentrics/sdk/mediation/*).

## UK: analytics opt-out (default ON), no consent prompt; AppsFlyer limited to signed-in personalisation-allowed users
- Pref pref_key_allow_analytics default **true** (classes5/sources/defpackage/o9g.java:187-189). AppInitialiser.initialiseAnalytics / initialiseChartBeat enable Echo (ATI + Comscore + BAG + UKOM per vo0.java config) and Chartbeat (account "50924", domain bbc.co.uk) when true (classes5/sources/uk/co/bbc/chrysalis/core/feature/AppInitialiser.java). Toggle copy: "Send app statistics — The BBC will only use this info to analyse and improve the services offered through this app." Settings also has "Privacy settings / Do not sell or share my info". No first-run consent dialog found; onboarding is edition choice + notifications.
- Optimizely initialised unconditionally (AppInitialiser.initialiseOptimizely), but decisions/events only run with a hashed BBC user id (classes4/sources/defpackage/rk4.java) and impressions go through Echo ("optimizely_v1").
- AppsFlyer (classes5/sources/defpackage/ij0.java + classes3/.../jj0.java): starts only if config appsflyer.enabled=="true" AND BBCUser.a() (signed in, valid token, allowPersonalisation) (classes5/sources/defpackage/t21.java). Customer user id = BBC hashed id; ATI session id attached as AppsFlyer additional data (joins attribution with analytics session); enableTCFDataCollection(false).
- ATI visitor id = random UUID, 397-day fixed lifetime (defaultConfiguration.json in APK root, "identifier":"UUID", "sendHitWhenOptOut":true). UKOM/dotmetrics reads ANDROID_ID (DatapointHelper.getAndroidIdOrNull) and GAID by reflection (class absent in UK build). BARB/Kantar enabled by default for AV (classes5/sources/defpackage/hug.java:71 "barb.enabled"="true"), ANDROID_ID hashed (SpringStreamsBase.getAndroidId → encrypt).
- Audience segmentation: for signed-in users the app fetches a segment and stores "<id>_<score>" (classes5/sources/defpackage/gqf.java).

## Nudges (both)
- UK notification pre-prompt has an equal "Maybe later" (notifications_maybe_later) and "You can update this any time in settings"; an "InDepth" notifications upsell card ("Turn on notifications") is remote-config controlled (key newsapp_indepth_upsell_component_selection). Push-disabled dialog: "OK" / "Go to settings".
- Sign-in is required only for My Topics personalisation ("Please sign in to access the content"); authtoolkit cross-app auto sign-in offers a warning "We do not recommend this if other people use this device." — good.
- WW: "Sign in or create a free account to get started."; subscription copy "Cancel anytime via your account settings." (paywall content from Piano server-side).

## Good practice / checked and cleared
- Exodus flags for WW Adjust, AppLovin, Unity Ads, ironSource are **false positives**: only Usercentrics mediation shims that probe by Class.forName (com/usercentrics/sdk/mediation/sdk/AdjustSDK.java, AppLovinMediationSDK.java, UnityAdsMediationSDK.java, IronSourceMediationSDK.java); no com.adjust/com.applovin/com.unity3d/com.ironsource classes are bundled.
- No location permissions in either build; Urban Airship location module not bundled in UK; local news relies on account location server-side.
- UK edition is ad-free (no ad SDKs); GAID class not bundled.
- No contacts, SMS, call log, accounts or installed-app enumeration beyond <queries> for BBC sibling apps (iPlayer, Sounds, Weather, Sport, CBeebies…), Facebook/Instagram share targets and Samsung mapsagent.
- GAID bridge honours LAT; Comscore consent label passed; Chartbeat/Echo disable when UK toggle off.
- Crashlytics collection off by default in both manifests (firebase_crashlytics_collection_enabled=false).

## Limitations
- WW business logic is Hermes bytecode; consent ordering, which identifiers reach GAM, text-selection payloads and paywall flows are inferred from strings only.
- Server-side configs (Sourcepoint message, Optimizely datafiles, remote config) not visible.
