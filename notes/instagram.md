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
