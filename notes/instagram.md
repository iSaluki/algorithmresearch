# Instagram 451.0.0.53.80 — working notes (paths under work/instagram/jadx_full/sources)

## AI / automation app detector ("odin_ai_apps_detector")
- X/EnumC525730Kkl.java — 23 packages: Manus (tech.butterfly.app), Replit, YouWare, Emergent, a0.dev, NotebookLM, ChatGPT, Gemini, Copilot, Perplexity, Claude, Replika, Character.AI, Poe, Pi, Tasker, IFTTT, Zapier, MacroDroid, Automate, Home Assistant, Notion, Airtable. All also declared in manifest <queries>.
- X/C367410Ebz.java:58-104 — gated by MobileConfig 36330376737612461; at most once per configurable interval (default 24h) [prefs ig_ai_apps_detector_prefs/last_detection_time]; analytics event "odin_ai_apps_detector" (sampled) via X/C627202di (IG analytics logger); probes each package with getPackageInfo; logs list of installed ones under "installed_apps"; emits event.
- Startup task: com.facebook.odinusecases.aiappsdetector.ig4a.AiAppsDetectorStartupTaskBinder.
- REA trace: work/rea/instagram.0Kkl.refs.json (single incoming ref X.C0Ebz in REA naming).

## Device state snapshot ("device_state_snapshot_client")
- X/C2111108Rp.java — collectors: audio (getMode, getRingerMode, getStreamVolume, isMusicActive; X/C1371020rhs), screen_brightness (C1068904It), connectivity (C1068804Is), display (C09PV), airplane_mode_on (C1068704Ir), DND interruption filter (C1068604Iq), media_router (C1371050rhw), keyguard isDeviceLocked/power isInteractive (C1068504Ip), "AppForeground" (C0A41).
- Startup task DeviceStateSnapshotStartupTaskBinder; DeviceStateSnapshotBgService; IG_ODIN_DEVICE_SIGNALS_COLLECTION → "pdp_signals_mobile" (X/EnumC703502q1.java:125).
- Manifest receiver com.facebook.odinusecases.devicestatesnapshot.ig4a.PreloadsFbnsUnlockSignalReceiver (exported, disabled by default, toggled at runtime) on action com.facebook.oxygen.services.fbns.SYS_ENTER — broadcast by Meta "Oxygen" preinstalled system services (com.facebook.services/appmanager/system, all in <queries>).

## Under-13 age model training uploads
- X/C1582206Ke.java:470-520 — reads local store "underage_storage", builds Odin Example "u13_example" and uploads to use case "AGE_SIGMA" v0.0.1; QPL markers ODIN_AGE, ODIN_AGE_U13_UPLOAD.
## Keyboard/language signal upload
- X/C1582206Ke.java:125-330 — getEnabledInputMethodList + subtypes + CurrentKeyboardLanguages → ZeroDayLanguageSignalUploadMutation (GraphQL) with "input_methods".

## Package visibility
- Manifest <queries> includes bare <intent><action MAIN/></intent> and VIEW scheme="*" → visibility of practically all launchable apps despite no QUERY_ALL_PACKAGES.

## Re-engagement
- X/C2456109l1.java + AnonymousClass0297 case 36 — on session end schedules AlarmManager ELAPSED_REALTIME +86400000 ms for local notification UNSEEN_LIKES (LocalNotificationAlarmReceiver).

## Benign / explained
- READ_CALL_LOG: flash-call phone verification reads only last call within window (X/AbstractC1331880pRm.java:287).
- getAllCellInfo/getCellLocation/getScanResults wrapped by IgLocationRequestDetector audit hooks (X/C702502pr.java, X/C1126104bz.java).
- getInstalledPackages in intent-scope resolution limited to Meta-family set (X/AbstractC1157704h5.java:175, X/C0W8D.java).

## In-app browser (IAB) injected JavaScript — 131 named scripts (DEX sourceURL=iabjs://...), 111 bundled in res/raw/iabjs_*, others downloaded at runtime (X/C0LKR.java A00: context.openFileInput(<sha1>.js); OTA overrides via prefs X/C0KF7)
- iabjs_data_layer_interceptor: Proxy around the site's window.dataLayer (GTM); every push (and queued items) forwarded to native handler "DataLayerInterceptor" with event_data=JSON.stringify(event).
- iabjs_detect_3p_analytics_tools: scans scripts/inline/img/iframe for 26 rival analytics/ads tools (GA/GTM, Clarity, Hotjar, Bing UET, TikTok, LinkedIn, Klaviyo, HubSpot, Northbeam, Criteo, Taboola, Plausible, Segment, FullStory, Fathom, Pendo, Attentive, Elevar, Rockerbox, Pardot, Snap pixel, Intercom, Amplitude) and extracts IDs → native "IABAPMJSHandler" analytics_tool_detected.
- iabjs_credentials_api_interceptor: monkeypatches navigator.credentials.get/create; reports type (public_key/password/federated/otp) and status, not secret values.
- iabjs_detect_login_forms: login form detected / field focused / submit clicked events.
- iabjs_extract_text_for_classification: up to 10 random page text strings → native "text_classification" (X/C297930BnD.java:619).
- iabjs_get_normalized_page_text, iabjs_sim_hash_logging (text+DOM simhash), iabjs_get_outbound_links, iabjs_capture_html_source (used only for user "Report" action: X/C491680JSs.java ACTION_REPORT attaches html_source_uri + screenshot).
- iab_inner_frame (142KB): onClick captures tag/textContent/clientX/Y; onKeyboardInteraction logs keydown *timing only* (no key value); onScrollEnd; observeATCNetworkRequests = PerformanceObserver over all resource URLs.
- utm_recovery: injects Meta UTM params into page URL.
- session_replay_recorder: body not shipped; loaded from downloaded file 5b305a249260bbf624889858912cc9d247ac7640.js (X/C0LKR.java:2016-2048).

## Cross-app identity & contacts
- family_device_id attached to push token registration, ads context (AbstractC811050Vzt.java:153) etc.
- XCCU continuous contact upload: com/instagram/contacts/ccu/impl/XCCUWorker.java periodic WorkManager "xccu_periodic_upload" every N hours (network constraint) + "xccu_catchup_upload"; com/instagram/contacts/xccu/IgXCCUClient.java gated by check_xccu_setting; delta via root hashes; sends fdid.

## Location
- Location caller registry X/EnumC703502q1.java (130 entries incl. FB entries; IG_USER_VISITATION_INFO, INDOOR_SCANNER, FB_ADS_TARGETING defined but unreferenced in IG).
- X/C657102iX.java "IG4AForegroundLocation" caller IG_FOREGROUND_LOCATION_UPLOAD: foreground location scans gated by MobileConfig 2342164611333175797; params 1800000ms/10000m; logs ig_fgl_reliability.
- X/C2167908fd.java IGEventInsightsManager: every A02 seconds (default 43200 = 12h) sends last location lat/long + time window via EventInsightsUpsamplingQuery (xfb_oxsights_event_insights_query_events_for_upsampling), caller IG_NETWORK_INSIGHT.
- Friend Map (com/instagram/friendmap/*), DirectLiveLocationService (foregroundServiceType=location).

## Camera roll auto-reels (default ON)
- X/AbstractC264120AZm.java: gallery_suggestions_setting default "auto_created_reels" (else "off").
- X/C1958207mu.java: unless off, scans camera roll media within last max(60, MC 36595311796553989) days, reverse-geocodes via android.location.Geocoder, runs ExecuTorch model (Voltron module); notification auto_created_reels_from_camera_roll_notification_sent (X/AbstractC1071910fg5.java). Processing appears on-device.

## Cross-posting nags
- X/EnumC565710MJl.java: ~100 cross-posting entry points to Facebook/Threads/WhatsApp, including IG_NOTIF_XAR_OFF_EU_REACTIVATION, IG_PROFILE_XAR_OFF_EU_REACTIVATION, IG_PRODASH_XAR_OFF_EU_REACTIVATION (push/profile/dashboard prompts to reactivate cross-app sharing for EU users who had it off).

## Payment/shopping risk fingerprint
- X/C1322090ozM.java collects MobileDeviceId/AndroidID, MobileGsfId (needs READ_GSERVICES — not declared), MobileSimSerialNumber/SubscriberId (blocked on Android 10+), MobileLine1Number, IP addresses, VPN/proxy, emulator, root ("pm list packages" via Runtime.exec, magisk/supersu, selinux), disk, uptime, timezone, locale.
- Sent as "risk_features" when opening Bloks screen com.bloks.www.buyer.reconsideration.wishlist (X/C1128130iBM.java:62) unless MC 36312200435992263.

## Competitor-pixel and data-layer interception (verified native side, per-DEX tree work/instagram/jdex/classes10)
- res/raw: iabjs_data_layer_interceptor (GTM dataLayer, source 0), iabjs_tiktok_pixel_interceptor (wraps navigator.sendBeacon for analytics.tiktok.com / business.tiktok.com, source 1), iabjs_snap_pixel_interceptor (Proxy on window.snaptr incl. "init" options, source 2), iabjs_reddit_pixel_interceptor (Proxy on window.rdt, source 4), iabjs_pinterest_pixel_interceptor, iabjs_x_pixel_interceptor. Script classes named analytics_helper_1..6 (X/C0LKR name map).
- Native: X/C0BZu.java "DataLayerInjectorController" registers handler "DataLayerInterceptor"; server-supplied ExtractionConfig x4 + C0CZW flags; X/C0LJK.java handler processes sources GTM/GTAG/GTM_CONTEXT/TIKTOK/SNAP, extracted_items/extracted_fields, page_url, tracking_token, logs "iab_client_analytics_health_monitor". Factory X/C044P.java case 1.
## Alternate payment method tracking
- X/C00410Bnd.java registers "IABAPMJSHandler" with 7 scripts incl. detect_3p_analytics_tools (C0BFG, injected onDomLoaded when flag A05); domain map www.paypal.com, apay-us.amazon.com, www.amazon.com, accounts.google.com, pay.google.com, shop.app; logs IABAPMSelectedEvent (url, method, timings).
## Clipboard: IgKnotsManager adds OnPrimaryClipChangedListener on foreground; logs "copy_triggered" only (X/ClipboardManagerOnPrimaryClipChangedListenerC1172170kEN.java).
## Meta AI promotion: X/EnumC1639006cW.java 97 entry points (acquisition/retention mid-cards, megaphones COPY_1..6, IGD_PROMOTIONAL_PROACTIVE_MESSAGE, HATCH_IG_UPSELL_RETARGET_NOTIF, C50_IG_FOLLOW_JOINED_NOTIF, IG_ONE_CLICK_INSTALL_BANNER).
