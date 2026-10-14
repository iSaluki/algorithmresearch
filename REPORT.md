# Dark Patterns & Data Practices in Sixteen Android Apps

**Static reverse-engineering study, October 2026.**
- **Batch 1** (13–14 Oct): Instagram, Snapchat and Reddit (priority), plus Duolingo, Dexcom G7 and Proton Mail.
- **Batch 2** (14 Oct): Facebook, WhatsApp, Telegram, Google Photos, Discord, Chess.com, Waze, BBC News (UK and International editions), Signal and Proton VPN.

Claude was not analysed (§19).

Everything below comes from the shipped APKs: decompiled code, manifests, bundled UI text and bundled JavaScript. Findings cite the decompiled file (paths are explained in §18). Where behaviour sits behind a server-side switch, the report says so and gives the shipped default. **Static analysis shows that code exists and what it does when switched on. It can't show how many users have it switched on.**

---

## 1. Summary

### 1.1 Overview by app

| App | Verdict | Worst issue |
|-----|---------|-------------|
| **Instagram** | Worst overall | Monitors third-party websites in its in-app browser; Wi-Fi/cell/Bluetooth location packages; AI-app detector |
| **Snapchat** | Very poor | Address-book upload with closeness metadata; ads in the chat inbox with no opt-out; churn targeting |
| **Facebook** | Very poor (partial view, §9) | Autofill used for ads and page instrumentation in the in-app browser; SIM and device identifiers at login; same AI-app list as Instagram |
| **Duolingo** | Poor | Non-dismissable guilt notifications; ~25 ad networks in an app with many children |
| **Telegram** | Poor | Crypto betting on dice rolls in chats; ad-tracking claim contradicted by the client; contact scraping |
| **Chess.com** | Poor | Tracking consent assumed "yes"; personalised ads with no child-directed flags in a child-heavy app |
| **WhatsApp** | Mixed | Ad requests carry the Meta device ID and year of birth; top chats exposed to Facebook/Instagram (server-gated) |
| **Google Photos** | Mixed | Undismissable backup sheet; every "no" to Gemini, faces or location second-guessed |
| **BBC News International** | Mixed | Analytics and ad consent pre-granted; behavioural profiling tied to BBC IDs |
| **Waze** | Mixed | Can report every Bluetooth connection, including health devices, with location (server-gated) |
| **Discord** | Mixed | Advertising ID tied to the account on every connection; installed-games probe |
| **Reddit** | Fair | Account deletion blocked by Premium; notification nags |
| **Dexcom G7** | Fair | Over-broad permissions and string encryption that hinders audit |
| **BBC News UK** | Fair | Analytics on by default with no first-run prompt; no ads |
| **Proton VPN** | Good | Telemetry on by default (F-Droid build) |
| **Signal** | Good | Rate-limited, dismissible prompts only |
| **Proton Mail** | Good | Seasonal sale banners only |

### 1.2 The worst findings

| # | App | Finding | Severity |
|---|-----|---------|----------|
| 1 | **Instagram** | **The in-app browser monitors the websites you visit.** Instagram injects scripts into third-party sites opened from the app: up to 131 programs, some downloaded at runtime. They do the following:<br>• **intercept the events those sites send to Google Tag Manager and to competitors' tracking pixels** (TikTok, Snap, Reddit, Pinterest, X);<br>• list which of 26 analytics/ad tools a site uses, with their account IDs;<br>• record **which payment method you choose at checkout**;<br>• capture clicks, scroll, key-press timing, page-text samples and network-request URLs.<br>**Facebook carries switches for the same interceptors and session replay**, and says outright that it "uses your autofill activity to improve ads" (§9). | **Critical** |
| 2 | **Instagram** | **Location packages uploaded while the app is open:** GPS plus nearby **Wi-Fi access points, cell towers and Bluetooth info**, tagged with the cross-app Meta device ID. Your coordinates are also sent every 12 hours to an "event insights" query. | **Critical** |
| 3 | **Instagram** | Checks which **AI assistants, AI-companion apps and automation tools** are installed (ChatGPT, Claude, Replika, Character.AI, Tasker… 23 in all) and reports the list to Meta analytics. **Facebook declares visibility of the same 23 apps** (§9). | **Critical** |
| 4 | **Duolingo** | "Streak in danger" notifications that **can't be swiped away** until the next day, red countdowns, angry-mascot animations, the home-screen icon renamed `Duolingo🚨`, and a notification type literally called `PASSIVE_AGGRESSIVE`. | **Critical** |
| 5 | **Snapchat**, **Duolingo** | **Address-book upload with "closeness" metadata** (starred contacts, birthdays, photos, which messaging apps each contact uses), covering people who never consented. **Telegram** uploads names and numbers unhashed, re-syncs on every change, and **scrapes phone-like strings out of notes, addresses and other fields** of contacts without a phone number (§10). | **Critical** |
| 6 | **Telegram** | **Betting cryptocurrency (TON) on dice rolls inside chats** ("Emoji Stake"): server-set multipliers and a streak counter. Wins and losses are announced to the chat, and tapping anyone's dice opens your own stake sheet. **No age or region check in the client** (server-gated beta). | **High** |
| 7 | **WhatsApp** | **Status/Channels ad requests carry the Meta-wide `family_device_id`, an encrypted year of birth, country, locale and device signals**, plus your profile name if you're linked to Accounts Center. A Meta-signature-only provider can give **Facebook, Instagram and Meta AI your 10 most-frequent chats**, and they can **silently re-activate a paused Accounts Center link** (server-gated, default off). | **High** |
| 8 | **Facebook** | The login request sends **SIM serials, SIM phone numbers, device email accounts, OpenID tokens, whether WhatsApp is installed** and five device/family identifiers. Identity providers share the Meta device ID with Meta apps **including its paid research apps**. Switch names point to **clipboard ("pasteboard") and screenshot signals for ad delivery**. | **High** |
| 9 | **Chess.com** | **Tracking consent is assumed "yes".** The consent flow ships disabled, and with it disabled every category, targeting included, defaults to *true*. Ads are personalised by default, the app **never sets child-directed or under-age ad flags** and has no age gate, and a server switch turns your **email into a UID2 ad identity**. Many of its players are children. | **High** |
| 10 | **Snapchat** | **Ads inside the chat inbox** with a forced choice and no "no". In the EU the consent modal **re-appears 48 h after each dismissal, up to 10 times**. My AI chats are used for ads, and the paid ad-free plan still shows sponsored AI responses. | **High** |
| 11 | **Snapchat** | **Location history and biometrics:** "Places you've visited", back-filled "Footsteps", repeated "Allow all the time" nudges, and **on-device face recognition** across Memories, linkable to Snapchat accounts (server-enabled). | **High** |
| 12 | **Instagram** | An **under-13 age model**, upload of **installed keyboards and languages**, a **device-state snapshot** that Meta's preinstalled services can trigger on unlock, **continuous background contact upload**, and **camera-roll scanning on by default**. | **High** |
| 13 | **Google Photos** | **Backup sheet with the decline button hidden, which can't be dismissed**; turning backup off triggers "Are you sure?", and the sheet returns every 14 days. **Every "no" in Gemini/Ask Photos setup gets a second confirmation** ("Knowing who you are is essential…"). A notice-only dialog says Photos can now **match your face to locations**. **Face grouping is announced with no toggle in 171 countries** (all outside the EU/UK). | **High** |
| 14 | **BBC News International** | Firebase Analytics starts with **analytics, ad storage, ad-user-data and ad-personalisation consent all pre-granted**, before the consent platform loads. Page-by-page **Permutive behavioural profiling**, with BBC federated IDs attached without the consent check the page tracker uses. | **High** |
| 15 | **Telegram** | The ad info sheet says "Telegram **doesn't track whether you tapped** on a sponsored message", yet **the client reports every tap and impression** to Telegram over your logged-in session. Video ads can't be closed until a server-set time, "Hide ad" opens the Premium paywall, and a flag can relabel "Sponsored" as "Recommended". | **High** |
| 16 | **Waze** | An exported receiver **wakes Waze on every Bluetooth connection** and can report the device's name and class (car audio, smartwatch, **glucose meter, blood-pressure monitor**) with last known location. The Bluetooth prompt only mentions tunnel navigation (server-gated, default appears off). Ticking "Don't show this again" on the background-location dialog makes the request **more direct**, not less. | **High** |
| 17 | **Snapchat** | **Churn-risk targeting:** users likely to leave get up to **15 full-screen takeovers per session vs 5**; pushes to people who abandoned sign-up; paid streak restores, including children's purchases. | **High** |
| 18 | **Duolingo** | About **25 ad networks** in a learning app with a large child audience, plus home-network fingerprinting. | **High** |
| 19 | **Discord** | **Google advertising ID sent in Discord's own analytics on every connection**, with no consent check (only Limit Ad Tracking stops it). An **installed-games probe** feeds recommendations, AppsFlyer starts unconditionally, and the analytics opt-out is loss-framed. | **Medium–High** |
| 20 | **Facebook** | Switches for **"stealth" notifications sent only to non-daily users** and replay of notifications cleared by a reboot. Messenger messages can be rerouted through Facebook when Messenger is silenced (switch names only). | **Medium** |
| 21 | **Reddit**, **Telegram** | **Account deletion obstructed:** Reddit won't delete until Premium is cancelled; **Telegram has no in-app delete at all**, only an inactivity self-destruct timer. | **Medium** |
| 22 | **Dexcom G7** | Medical-device app that requests far more access than it uses, with string-encrypted code that hinders audit (§6). | **Medium** |
| — | **Signal**, **Proton Mail**, **Proton VPN** | Cleanest apps. No ad or analytics SDKs (Proton VPN's telemetry is first-party and opt-out); prompts are rate-limited and dismissible (§7, §16, §17). | Low |

---

## 2. Instagram 451.0.0.53.80 (`com.instagram.android`)

### 2.1 Surveillance of third-party websites in the in-app browser *(Critical)*
When you tap a link, Instagram opens it in its own browser and injects JavaScript into the page. The DEX contains **131 named scripts** (`//# sourceURL=iabjs://…`). **111 ship in `res/raw/iabjs_*`**, the rest are **downloaded at runtime** into app storage (`X/C0LKR.java`, `context.openFileInput("<sha1>.js")`), and any script can be **overridden over the air** from stored prefs (`X/C0KF7.java`). What I read:

- **Competitor-pixel and tag-manager interception** (`iabjs_data_layer_interceptor`, `iabjs_tiktok_pixel_interceptor`, `iabjs_snap_pixel_interceptor`, `iabjs_reddit_pixel_interceptor`, `iabjs_pinterest_pixel_interceptor`, `iabjs_x_pixel_interceptor`; internally named only `analytics_helper_1…6`):
  - wraps the site's `window.dataLayer` (Google Tag Manager) in a JavaScript Proxy and forwards **every event, including ones queued before injection, as full JSON**;
  - wraps `navigator.sendBeacon` to copy beacons sent to `analytics.tiktok.com`/`business.tiktok.com`;
  - proxies `window.snaptr` (Snap Pixel), **including the `init` call where sites pass advanced-matching data such as email/phone**, and `window.rdt` (Reddit Pixel).
  - Native side (`X/C0BZu.java` "DataLayerInjectorController", `X/C0LJK.java`): **server-supplied `ExtractionConfig`s** select fields; output is logged with `page_url` and the ad `tracking_token` as `iab_client_analytics_health_monitor` events. The scripts call themselves "health metrics".
- **Analytics-tool fingerprinting** (`iabjs_detect_3p_analytics_tools`): scans each page for 26 tools (GA/GTM, Clarity, Hotjar, Bing UET, TikTok, LinkedIn, Klaviyo, HubSpot, Criteo, Taboola, Segment, FullStory, Snap Pixel, Amplitude…) and **extracts their account IDs**.
- **Checkout tracking** (`X/C00410Bnd.java`, handler `IABAPMJSHandler`): watches www.paypal.com, Amazon Pay, accounts.google.com/pay.google.com and shop.app, and logs `IABAPMSelectedEvent` (page, method, timings) when you **choose an alternative payment method on a merchant's site**.
- **Interaction capture** (`iabjs_iab_inner_frame`, 142 KB): every click (element tag, its text, x/y), scroll end, **key-press timing** (the key itself is *not* captured), page show/hide, and a `PerformanceObserver` recording **the URL of every resource the page loads**.
- **Content sampling:** `extract_text_for_classification` (10 random text snippets → native `text_classification`), `get_normalized_page_text`, `sim_hash_logging` (page fingerprint), `get_outbound_links`, `detect_login_forms` (form detected/focused/submitted), `credentials_api_interceptor` (monkey-patches `navigator.credentials` to report passkey/password use; type and status only), `utm_recovery` (writes Meta UTM parameters into the URL).
- `session_replay_recorder` exists, but its body isn't shipped. It's loaded from a downloaded file (`5b305a249260bbf624889858912cc9d247ac7640.js`).
- *Benign:* `capture_html_source` (full page HTML) is used only when **you report a link** (`ACTION_REPORT`).

**Why it matters.** This turns every link you open from Instagram into a measurement point on the open web, including other companies' analytics and ad pixels and your checkout choices. The page owner never agreed to it, and the user can't see it.

### 2.2 Location collection *(Critical)*
- **Foreground location upload** (`X/C657102iX` / `jdex/classes3/…/X/C024202iX.java` "IG4AForegroundLocation", caller `IG_FOREGROUND_LOCATION_UPLOAD`, remote flag `2342164611333175797`, location permission required). Fixes are queued and uploaded with `FbLocationUpdateMutation` (`jdex/classes7/…/X/C04790JCj.java`, `X/C0FfJ.java`). Fields: **latitude, longitude, accuracy, altitude, speed, bearing, `is_spoofed`, `wifi_info` (hardware_address/BSSID, rssi, scan_results), `cell_info` (cell ID, LAC/TAC, MCC/MNC, timing advance, operator, SIM country), `bluetooth_info`, `family_device_id`, `app_use_state`**.
- **"Event insights"** (`X/C2167908fd.java`): every 43,200 s (12 h, default) after session start, sends last-known **lat/long** to `EventInsightsUpsamplingQuery`.
- Plus Friend Map (`com/instagram/friendmap`) and live location in DMs (foreground service `DirectLiveLocationService`).

### 2.3 AI and automation app detector *(Critical)*
`X/EnumC525730Kkl.java` lists 23 packages (Manus, Replit, YouWare, Emergent, a0.dev, NotebookLM, ChatGPT, Gemini, Copilot, Perplexity, **Claude, Replika, Character.AI, Poe, Pi**, Tasker, IFTTT, Zapier, MacroDroid, Automate, Home Assistant, Notion, Airtable), all also in `<queries>`. `X/C367410Ebz.java:58-104` (startup task `AiAppsDetectorStartupTaskBinder`, flag `36330376737612461`, at most once per configurable interval, default 24 h) probes each with `getPackageInfo` and logs the installed ones as `installed_apps` in analytics event `odin_ai_apps_detector`. Caller independently traced with REA (`evidence/rea/instagram.0Kkl.refs.json`).

### 2.4 More on-device profiling *(High)*
- **Under-13 age model:** `X/C1582206Ke.java:470-520` reads on-device store `underage_storage`, builds Odin training example `u13_example`, uploads to use case **`AGE_SIGMA` v0.0.1**.
- **Keyboards and languages:** same class, `getEnabledInputMethodList()` plus language subtypes → `ZeroDayLanguageSignalUploadMutation`.
- **Device-state snapshot** (`X/C2111108Rp.java`): audio mode, ringer, volume, **music playing**, brightness, connectivity, display, airplane mode, **DND filter**, media routing, **lock/interactive state**. Exported receiver `PreloadsFbnsUnlockSignalReceiver` listens for `com.facebook.oxygen.services.fbns.SYS_ENTER` from **Meta services that phone makers preinstall**. It's enabled at runtime by `DeviceStateSnapshotManager` (`jdex/classes4/…/X/C0AKu.java`) and uploads on unlock when `preloads_fbns_unlock_signal_upload_enabled = 1`.
- **Continuous contact upload** (`com/instagram/contacts/ccu/impl/XCCUWorker.java`): once contact sync is on, a periodic background WorkManager job (`xccu_periodic_upload`, every N hours) re-uploads deltas with `fdid`.
- **Camera roll scanned by default** (`X/AbstractC264120AZm.java`: `gallery_suggestions_setting` default `auto_created_reels`). `X/C1958207mu.java` scans at least the last 60 days of media, **reverse-geocodes photo locations** and runs an on-device model to auto-create Reels. As far as the code shows, processing is on-device.
- **Shopping "risk" fingerprint** (`X/C1322090ozM.java`), sent when opening the wishlist re-engagement screen (`com.bloks.www.buyer.reconsideration.wishlist`): Android ID, phone number (if granted), IP addresses, VPN/proxy, emulator/root checks via `pm list packages`, disk, uptime. SIM serial/IMSI reads exist but are blocked on Android 10+, and GSF ID needs a permission Instagram doesn't declare.
- **Package visibility:** no `QUERY_ALL_PACKAGES`, but a bare `MAIN` intent query in `<queries>` makes nearly all apps visible.

### 2.5 Engagement and self-preferencing *(Medium)*
- **97 surfaces promoting Meta's AI apps** (`X/EnumC1639006cW.java`): feed and story acquisition/retention cards, megaphones with six copy variants, promotional DMs (`IGD_PROMOTIONAL_PROACTIVE_MESSAGE`), retargeting pushes, "someone you follow joined" pushes.
- **About 100 cross-posting nudges** (`X/EnumC565710MJl.java`), including push/profile/dashboard prompts named `…_XAR_OFF_EU_REACTIVATION`, apparently aimed at EU users who had cross-app sharing switched off.
- **24-hour "unseen likes" alarm** set at session end (`X/C2456109l1.java`), local and not tied to new activity.
- Clipboard: a listener logs that you copied something (`copy_triggered`), not the content.
- *Benign:* `READ_CALL_LOG` reads only the last call, for flash-call phone verification. Cell/Wi-Fi reads are wrapped by an internal audit hook.

---

## 3. Snapchat 14.27.0.53 (`com.snapchat.android`)

### 3.1 Contact upload with closeness metadata *(Critical)*
`defpackage/C0111Ac0.java:403` reads the full contacts table and builds per-contact records with **starred, hasEvent (birthday), hasPhoto, emails, phone types and `firstSocialLink`**. The last one is the mimetype of other apps' contact rows (e.g. WhatsApp), matched against server keyword list `frnd_contact_social_link_mime_type_keywords`, which ships empty and is filled remotely. Records are serialised into `contacts_with_meta_data` and sent to `/bq/find_friends_reg` **during registration** and to `/ph/find_friends` (`com/snap/identity/FriendingHttpInterface.java`). The request also carries `enable_find_friends_for_UK_under_age`.

### 3.2 Ads in the chat inbox *(High)*
- Copy: "New in Your Chat Feed: Sponsored Snaps"; "Choose Your Ad Experience": "Smaller In-Feed Ads" or "Larger Banner Ads"; "I'm In!" or "Not Now". There's no way to say no; ads are pitched as "personalized messages from your favorite artists, creators, brands".
- `defpackage/AKi.java:2481-2489`: `sponsored_snaps_eu_modal_dismissal_reprompt_ttl_seconds = 172800` (48 h), `…_dismissal_reprompt_frequency_cap = 10`, `…_opt_in_reprompt_ttl_days = 183`.
- **Snap Pixel identity cookie** for web ads: `AdsCookieManagerV2` fetches `https://tr.snapchat.com/cm/wv?scut=<pixel token>` (cookie `sc_at`, 120 h) and attaches it when ad landing pages open, so advertisers' Snap Pixel can tie the visit to you.
- **Ad-browser autofill**: injected script reports form detection and **the values you type into advertisers' forms** (`defpackage/sQ0.java`) to offer "Save info to autofill future forms?"; saved info "may also be used to improve your ad experience".
- Remote switches present (default off): location in ad requests, probing which apps can open URLs for app-install ads.

### 3.3 My AI *(High)*
Disclosure text: My AI uses content and **location**; content "is retained until you delete it"; "We use My AI information to improve our products **and ads**"; "We share information with … **advertising partners**"; in groups "My AI can read **all messages**". The Snapchat+ ad-free plan: "You may still see **sponsored** places and **My AI responses**."

### 3.4 Location history and background location *(High)*
- "Clear your location history, including **travel updates and Places you've visited while location is turned on**" (deletion split three ways: location history / Footsteps / tagged Places). "Your location history updates while you have Snapchat open." Places "Visited", "Highly Revisited" and **"Visited by $0"** (friends).
- **Footsteps** is back-filled from "Snaps in your **Memories**" (photo location metadata).
- "Allow all the time" upsell trays, plus a `BackgroundLocationRecovery` prompt for people who downgraded. Location foreground service `LodaDaemonService`, geofences (enter/exit/dwell), a push-handler hook and a buffered uploader.

### 3.5 Face recognition and camera-roll indexing *(High, server-enabled)*
Memories DB (`defpackage/C44243s2b.java`): `detected_face(…, encoding BLOB)`, `face_cluster(tagged_user_id)`, plus visual tagging and CLIP-style captions/embeddings. The toggle copy promises use for "**future manual or automatic creative use**", and turning it off is framed as a loss ("All your face groups … will be deleted"). `FACE_CLUSTERING_ENABLED` defaults off; backfill up to 10,000 items. A **camera-roll metadata scan** runs every 8 h (`CameraRollMetadataScanRecurringDurableJob`) with a gRPC upload path, which is off by default (`ENABLE_CAMERA_ROLL_FS_METADATA_UPLOAD = false`).

### 3.6 Retention targeting and streaks *(High)*
- Segments `is_deep_churn`, `is_high_churn_risk_active/new/resurrected` (`defpackage/EnumC23587eaa.java:663-677`). "Added Me" camera takeover cap **15 per session for new/churn users vs 5** (`:654-660`, `C20018cG.java`).
- Pushes to people who abandoned sign-up (`GROWTH_NOTIFICATION_REGISTRATION_REENGAGEMENT`) and logged-out users (`RELOGIN_NOTIFICATION_SEND_TIME`); free streak restores for returning users; win-back SKU `winback-1m-599`.
- Streak expiry warnings 1 h ahead; **paid restores within 48 h**, including Google Play's "pending purchase waiting to be approved" (a child's request to a parent).
- Snapchat+ cancellation: "Don't Cancel" → feature-loss list → exit survey → "Finish canceling in settings".

### 3.7 Minors and social pressure *(Medium)*
- Snapchat itself warns: "If you open this message, $0 may be able to determine that **you have their phone number in your contact book**."
- 16–17-year-olds are prompted to "Grow Your Audience" with a public profile; **minors can be paid for viral Spotlight Snaps** (16+, parental consent).
- "Solar Systems" (your rank in a friend's orbit), and screenshot notifications even for **removed group members**.
- Location prompt bundles **ads** into a map consent: "Snapchat will also use your location for Filters, **Ads**, and more."

*Checked and cleared:* BSSID used only as a local bandwidth-cache key; no installed-package enumeration; "security center" queries are permission-settings deep links.

---

## 4. Reddit 2026.40.0 (`com.reddit.frontpage`)
Reddit came out markedly better than Instagram and Snapchat on tracking.
- **Account deletion blocked by subscription** *(Medium)*: "To delete your account, you need to cancel your Reddit Premium subscription first." After deletion, posts/comments/messages are "dissociated (not deleted)".
- **Notification nagging** *(Medium)*: pre-prompt/re-prompt/re-enablement states with entry points on AppLaunch, SessionChange, voting, commenting, posting, following, chat and more. Bundled consent ("best content for you, **as well as** replies"); upsell from "Only post & comment notifications" back to all.
- **New daily streaks** *(Low–Medium)*: streak popups and a "not progressed today" alert badge. Onboarding claims "People with longer than 50 day streaks earn **271% more karma**".
- **Ad reminders** that schedule notifications ("Get a notification so you don't miss out").
- **Over-declared permissions** *(Low)*: `PACKAGE_USAGE_STATS` never used for usage queries; `READ_GSERVICES` lets Google reCAPTCHA read the GSF device ID.
- **Good practice found:** both advertising IDs honour "limit ad tracking"; AppsFlyer only for attribution and gated by a tracking setting; equal Accept/Reject cookie buttons; no contacts or location collection; JavaScript injection only on Reddit's own pages; age checks via Persona with stated 7-day retention.

---

## 5. Duolingo 6.101.2 (`com.duolingo`)
- **Notifications you can't dismiss** *(Critical)*: `defpackage/oms.java:1502-1525`. For `STREAK_SAVER`, with streak ≥ 7 days (`uls.streak`), Android 13+ and a remote flag on, the notification is posted with `FLAG_NO_CLEAR` and un-stuck by `UnstickNotificationWorker` at a set time **the next day** (`defpackage/lg40.java`). Its own HIGH-importance channel; 60-minute red countdown; `terminator_duo`/`mad_duo`/`laser_duo` animations (`defpackage/sks.java`).
- **Launcher icon/name swaps** *(High)*: `PreStreakSaver1…9` escalating icons; labels "Duolingo🚨/⏳/⏰/‼️/❓/👀/⁉️".
- **Notification taxonomy** *(High)*: `PASSIVE_AGGRESSIVE`, `ABANDONED_CART_*`, `RESURRECTION`, `CONTINUOUS_RESURRECTION`, `FRIENDS_RESURRECTION`, `REMOVE_AND_RESEND_NOTIFICATION`, `APP_ICON_UPDATE`; haptics experiment for "risk users".
- **Contact sync with closeness flags** *(Critical, see #5)*: `defpackage/jg.java` and `com/duolingo/data/contactsync/ContactItem.java`. Per contact: display name, email, phone, hasBirthday, hasCompanyName, hasNickName, hasAddress, hasPhoto, **WhatsApp/Telegram presence**. SHA-256 hashing applies when server config enables it.
- **Home-network fingerprinting** *(High)*: Wi-Fi-triggered reminders (`TriggeredNotificationWifiWorker`), with networks identified by hashed gateway IP and subnet and counted by days seen (`defpackage/gde.java`).
- **Ad stack** *(High)*: 32 Exodus trackers, ~25 ad networks fully bundled. Child-directed flags are set for AdMob and Adjust; I didn't verify every mediated network.
- **Copy**: League Repair and Timer Boost to avoid demotion, "Add Widget to Repair", "Wait, don't go!", "Losing makes me cry…".
- *Cleared:* calendar access is limited to Duolingo's own practice events.

## 6. Dexcom G7 2.2.1 (`com.dexcom.g7`)
`QUERY_ALL_PACKAGES` is used only to find Dexcom's own Clarity app. Microphone is for voice entry. Location covers BLE and a country-of-residence check ("You must **always** allow location"). All strings are encrypted and package calls go through reflection, which hampers audit of a regulated medical device. Sharing to followers and data restore require cloud consent, and consent text is server-side, so its scope can't be judged from the APK. Bulk uploads are device settings and inventory records. Qualtrics and Crashlytics are present; Firebase Analytics is off by default.

## 7. Proton Mail 7.11.10 (`ch.protonmail.android`)
14 permissions; contacts used for autocomplete and explicit import. Only Sentry, reporting to Proton's own server with session replay not configured. Firebase analytics, ad ID and messaging auto-init are off. A `crashReports` setting exists (I didn't confirm it gates the SDK). Dark patterns are limited to seasonal sale banners; auto-renew prices are disclosed.

---

## 8. WhatsApp 2.26.39.79 (`com.whatsapp`)
No third-party tracker SDKs, and Firebase Analytics is off. Message content stays end-to-end encrypted. The problems are on the **advertising and Meta-integration** side, much of it behind server switches (shipped client defaults are given; live values come from Meta's servers). Paths are under `work/whatsapp/jdex`; full pointers are in `notes/whatsapp.md`.

### 8.1 Status/Channels ad requests carry identity and device signals *(High)*
- **Always sent:** the Status ads fetch (`www.whatsapp.com/api/wamo/status`, `classes9/sources/com/whatsapp/wamo/request/WamoRequestManager.java:2412-2660`) sends the cross-app Meta device ID `family_device_id`, country, locale, OS version, an **encrypted year of birth** and the number of unseen Status items.
- **Device block:** depending on a switch, also battery level, charging state, connection type (Wi-Fi/cellular) and screen size, or device brand, manufacturer and model.
- **Profile name:** when the account is linked to Meta Accounts Center, the WhatsApp **profile name** (`push_name`) is added.
- **Installed Meta apps:** a further switch (default off) tags the request `ig_ad_cohort`/`fb_ad_cohort` when Instagram or Facebook is installed but not linked, which tells the ad server which Meta apps are on the phone.
- **Census:** a separate daily analytics event (`wam_installed_foa_app_daily`) records which of Facebook, Facebook Lite, Messenger and Instagram are installed.

### 8.2 Your most-frequent chats exposed to Facebook, Instagram and Meta AI *(High, server-gated)*
- **The provider:** an exported provider (`classes/sources/com/whatsapp/accountlinking/ipc/handler/quicksends/QuickSendsContactsProvider.java`), protected by a Meta-signature permission, returns your top `max_contacts` (default 10) most-frequent chats. Each comes with a display name, profile photo and an encrypted chat ID.
- **Who can read it:** Instagram, Facebook, Facebook Lite and `com.facebook.stella` (Meta AI / glasses).
- **What else the bridge allows:** via the same Accounts Center bridge, those apps can send into WhatsApp chats, read the registered phone number and notification count, and, when the link is "paused", **silently re-activate it with no UI** (`TriggerSilentUnpauseOperationHandler`).
- **Gating:** switches, default off, plus an active Accounts Center link.

### 8.3 Pay-or-consent tied to account linking *(Medium)*
- **The choice:** EU users choose "Free of charge with ads" or "No ads (…/month)".
- **Price depends on linking:** copy says that removing WhatsApp from Accounts Center **lowers the subscription price**, so the price is coupled to cross-app data linking.
- **Consent auto-clear:** a daily job can clear a "less-personalised ads" consent (`WamoLpaAutoClearDailyCron`; switch default off). What the server does with this is not visible.

### 8.4 Contact upload and engagement pushes *(Medium)*
- **What's uploaded:** the full address book's phone numbers are uploaded **in plain form (not hashed; names not sent)**, including numbers of people who don't use WhatsApp. There's a full re-sync every 24 h by default (`contact_full_sync_wait`). The permission rationale talks about verification and backups, not upload.
- **Pushes:**
  - Reply and missed-call reminders.
  - "X joined WhatsApp".
  - Status pushes for your top-5 contacts.
  - **Server-pushed recommended Channels, on by default**; the opt-out is offered only through a later "Getting too many notifications?" push.

### 8.5 Meta AI and in-app browser *(Medium)*
- **Meta AI:** the button is on by default. In the decompiled settings code, the "Show Meta AI button" switch only appears once the setting is already off, and I found no other path to turn it off. Copy says Meta AI "may use information from your profiles connected in Account Center" and data "may be used to improve AI at Meta".
- **In-app browser:** a bundled script (`res/raw/iabjs_autofill_payment_detection`) is injected on **all sites** opened from ad and business links. It classifies card-number, CVC and expiry fields and passes the typed values to the app on submit, which holds them to offer saving to Meta autofill. Copy says "Your autofill activity is used to improve ads" (payment data said to be excluded). There are none of Instagram's pixel/dataLayer interceptors.
- **Business messages:** reading a business marketing message is logged (`business_template_message_read_stats`) with the business number, read time, dwell time and **whether you have read receipts turned off**, which is recorded rather than respected.

**Good practice:**
- Link previews are generated on the sender's device.
- No background location.
- The ad ID is sent only at registration, never for EU users and never with Limit Ad Tracking.
- Ads have per-advertiser hide/report and a "My Ads" report, and say that messages, calls and statuses aren't used.
- E2E backups are available, and account deletion is not obstructed.

## 9. Facebook 582.0.0.50.54 (`com.facebook.katana`)
**Caveat first: Facebook's main code could not be decompiled.** Almost everything ships compressed with Meta's proprietary Superpack format: the main DEX, the React Native bundle, 102 native libraries and the English strings. An attempt to run Facebook's own decoder under emulation got the library loaded but crashed mid-decode (`scripts/superpack/README.md`).

This section is therefore built from:
- the manifest,
- 807 resource strings,
- bundled assets (login screens, schemas, SQL pipelines),
- the small loader DEX,
- the names of **32,861 server-side MobileConfig switches** across 3,849 configs.

Items marked **[C]** are confirmed by manifest, asset, string or loader code. Items marked **[F]** are indicated by switch names only: the capability or experiment exists, but its default and use are unknown. Full pointers are in `notes/facebook.md`.

- **The in-app browser: autofill used for ads, and Instagram-style page instrumentation** *(High)*.
  - [C] A string answers "does Facebook use autofill for ads?" with "Yes, Facebook uses your autofill activity to improve ads… some of it is provided by the businesses that own the websites". The data collected is the website address, time, fields filled and whether the form was submitted (payment numbers excluded).
  - [C] A bundled on-device SQL pipeline (`assets/business_integrity_cloaking.json`) extracts page `<title>` and `<body>` text from visited pages for ad-cloaking checks and keeps it for one day.
  - [F] The browser-agent config carries the same capabilities as Instagram's injected scripts (§2.1):
    - `datalayer_interceptor_enabled`, `ga_interceptor_enabled`, `sp_interceptor_enabled` (Snap Pixel), `ttk_interceptor_enabled` (TikTok)
    - `inner_frame_session_replay_enabled`, `inner_frame_visible_elements_logging_enabled`
    - checkout-path and payment-method modelling (`android_iab_unified_checkout_modeling`, `enable_analytics_tool_detection`)
    - `ai_agent_web_chat_suppression_js_enabled`, which suppresses the merchant site's own chat widget
  - The scripts themselves aren't in the APK; the browser engine is a downloadable module.
- **The login request collects device, SIM and account identifiers** *(High)* [C].
  - The bundled login screen (`com.bloks.www.caa.login.aymh.screen_query_bundled_payload.json`) sends:
    - `family_device_id`, `machine_id`, `fb_ig_device_id`
    - `sim_serials`, `sim_phones`
    - `device_emails`, `openid_tokens`
    - `has_whatsapp_installed`
    - whether contacts and phone permissions are granted
  - The logged-out screen prefetches device emails and the phone number.
- **Same AI-app detection list as Instagram** *(Medium–High)*.
  - [C] `<queries>` names ChatGPT, Claude, Copilot, Perplexity, Character.AI, Replika, Tasker, Zapier and others. These are the same 23 packages as Instagram's AI-app detector (§2.3), plus X, Telegram and Spotify.
  - [C] A bare MAIN-intent query makes nearly every launchable app visible.
  - [F] `fb_android_derived_on_device_app_history:is_derived_app_history_enabled` with an `installed_ad_id_mutation_batch_size` suggests periodic upload of which advertised apps are installed, skipped for ad-free subscribers.
- **Cross-app identity plumbing** *(Medium–High)* [C].
  - The family-device-ID provider hands the Meta `phone_id` to Meta apps, **including Meta's paid research apps `com.facebook.study` and `com.facebook.viewpoints`**.
  - An SSO provider shares logged-in accounts with nine Meta apps.
  - Facebook can read a "device cookie" and "SIM key" from Meta's preinstalled `com.facebook.services`.
  - It declares the WhatsApp permission that guards the top-chats provider (§8.2).
  - It receives foreground signals from Instagram and Messenger.
- **Notifications aimed at lapsed users** *(Medium–High)*.
  - [C] A `StealthNotificationDeleteBroadcastReceiver`.
  - [F] `fb4a_notifications_stealth` (with `should_send_to_non_dau_only` and a periodic scheduler) reads as a low-visibility notification that badges the icon for people who don't open the app daily.
  - [C+F] Notifications cleared by reboot or update are replayed (`should_replay_on_reboot`, `should_refresh_app_badge_on_replay`).
  - [F] Messenger messages can be rerouted through Facebook when Messenger hasn't been push-reachable for 30 days (`route_to_fb_when_msgr_unpushable_30d`), which can override someone who silenced Messenger.
  - [F] Group streaks.
- **Ad signals from clipboard and screenshots** *(Medium)* [F]: the `fb4a_knots` "high value signal" config has `enable_pasteboard_logging`, `enable_screenshot_signal` and `url_hi_value_ad_keywords`. Other ad-signal configs use battery, bandwidth and Reels scroll speed.
- **Contacts and ID checks** *(Medium)*:
  - [F] Contact-upload upsells in People You May Know, plus an A/B test of the upload disclosure screen (`address_book_acquisition:disclosure_screen_design_variant`).
  - [C] The bundled contact-store schema holds server-computed per-contact ranks (`communicationRank`, `withTaggingRank`) next to imported phone entries, birthdays, current city and family relationships.
  - [C] ID-verification video selfies are stored "for up to 1 year" by default and reviewed with face recognition. Reducing that to 30 days is opt-out.
- **Meta AI everywhere** *(Medium)* [F], about 1,760 AI-related switches:
  - the Meta AI button pulls context from on-screen feed posts;
  - on-device intent detection over typed messages triggers AI prompts;
  - AI summaries extend to end-to-end-encrypted chats, with a `summary_bottom_sheet_undismissible_duration_ms`;
  - the Preloads/AppManager channel can install Threads and Instagram, and auto-open Threads after install.

**Checked and cleared:**
- No background location, Bluetooth/Wi-Fi scanning, usage-stats or QUERY_ALL_PACKAGES permission.
- No Wi-Fi/cell/Bluetooth location-package switches (unlike Instagram), and no under-13 age-model switches.
- `call_log_max_rows` and the 1,741 `assets/dsp` files are Messenger's own database procedures, not the phone's call log. READ_CALL_LOG is declared only for Android 6–9 (`uses-permission-sdk-23`, likely flash-call login).
- "ccu" switches mean concurrent users in Horizon Worlds, not contact upload.

## 10. Telegram 13.0.1 (`org.telegram.messenger`)
No tracker SDKs. Firebase Analytics is disabled, there's no advertising ID, and the call log and SIM number are used only on-device for login. The issues are Telegram's own: **crypto gambling, ads and contact harvesting**. UI copy comes from `assets/localization_en.bin`, decoded by name hash. Paths are under `work/telegram/jdex`; more in `notes/telegram.md`.

- **"Emoji Stake": betting TON cryptocurrency on dice rolls inside chats** *(High, server-gated beta)*.
  - You stake TON on a 🎲 roll. The server sets payout multipliers, min/max stake and a streak counter ("A streak resets after 3 🎲 or a stake change").
  - Wins and losses are announced to the whole chat ("won/lost 💎 …"), and tapping anyone's dice opens your own stake sheet, so every result doubles as an invitation to play.
  - There's **no age or region check in the client**; the sheet calls it "a limited play-test".
  - Evidence: `TLRPC.java` (`TL_inputMediaStakeDice`, `ton_amount`), `classes3/sources/org/telegram/ui/qa1.java:82-220`.
- **Ads: "doesn't track whether you tapped" vs the code** *(High)*.
  - The ad info sheet says "Telegram doesn't track whether you tapped on a sponsored message and doesn't profile you based on your activity" (`SponsoredMessageInfo2Description2`).
  - The client sends `messages.clickSponsoredMessage` on **every tap** (with media/fullscreen flags) and `viewSponsoredMessage` on every impression, over the logged-in session (`classes3/sources/org/telegram/ui/oo.java:14595-14603`, `video/VideoAds.java:975-998`). What the server keeps is not visible, but the claim isn't true of the client.
  - Ads appear in channels, bots, search and inside videos, where **the close button appears only after a server-set minimum duration**.
  - "Hide ad" opens the Premium paywall. A server flag can relabel "Sponsored" as **"Recommended"**.
- **Contact upload that scrapes other fields** *(High)*.
  - Sync is on by default. Names and phone numbers are uploaded unhashed, re-synced on every address-book change and force-re-imported every 24 h.
  - For contacts **without** a phone number, the code reads fields 1–4 of every data row of any type (email, notes, postal address, IM, organisation) and uploads anything that looks like `+digits` as a phone number (`ContactsController.java:3346-3400`).
  - The pre-prompt calls the destination "heavily encrypted cloud servers". "Contact joined Telegram" alerts are on by default.
- **No way to delete your account in the app** *(Medium)*.
  - "Delete my account" in Privacy settings only sets an inactivity self-destruct timer (1 month to 2 years). The delete call is reachable only from the forgot-password reset and from declining a Terms update.
  - Logging out "will … delete wallet backups".
- **Built-in crypto wallet** *(Medium)*: the recovery-phrase backup is split into shares, each encrypted to a key held by a Telegram data centre. "No one — not even Telegram — can access your key" therefore depends on Telegram's server separation, not on anything the client enforces.
- **Age check by selfie** *(Medium, UK)*: a server-named bot's mini app takes a selfie and returns age **and gender with a probability**. "Your selfie will not be stored by Telegram" can't be verified (the analysis runs in the web page).
- **Premium/Stars pressure** *(Medium)*:
  - "Download speed limited — Subscribe to Telegram Premium and increase download speeds 10 times" when the server throttles you.
  - Discount and expiry banners, birthday gift prompts.
  - The server can force **non-skippable** login-email setup.
  - One-tap paid reactions with a 5-second undo.
  - Collectible-gift scarcity copy and auctions ("You've been outbid").
  - Premium-screen interactions are logged to Telegram with no opt-out.
- **Smaller items** *(Low)*:
  - The notification-permission sheet re-asks after 1, 3 and 7 days, then **every 30 days forever**, with only a "Continue" button.
  - Mini apps get device model/OS and can stream motion sensors at 50 Hz without a prompt (phone number, location and clipboard are properly gated).

**Good practice:**
- READ_CALL_LOG is used only to match one flash-call number from the last hour.
- READ_PHONE_NUMBERS sends only a yes/no.
- People Nearby is gone, and background location is only for live-location sharing.
- In-app browser scripts don't track.
- Secret chats disable keyboard learning, and cloud chats are honestly described as not end-to-end encrypted.

## 11. Google Photos 7.97.0 (`com.google.android.apps.photos`)
No ad or attribution SDKs. The dark patterns are about **pushing backup, storage purchases and AI features**. Paths are under `work/gphotos/jdex`; more in `notes/gphotos.md`.

- **Backup "best by default" sheet** *(High, server-gated experiment)*.
  - The "Back up automatically" switch is pre-checked. The decline button is hidden and the only button reads "Turn on backup", and the sheet **can't be dismissed**.
  - Switching it off opens a second non-cancellable "Are you sure?" ("…your photos aren't protected if your device is damaged, lost or stolen…").
  - The sheet comes back **every 14 days** (client fallback) while backup is off.
  - Evidence: `classes4/sources/defpackage/tjm.java`, `tjo.java`, `syc.java`.
- **Gemini / "Ask Photos" setup: every "no" is second-guessed** *(High)*.
  - Each decline triggers a confirmation, for Gemini, the "Me" face label, face grouping and location estimation.
  - Confirmation copy includes "Knowing who you are is essential to you getting the best experience" and "Face grouping is essential…".
  - Accepting is never questioned, and progress copy says "You're so close".
  - Disclosure: "You may also be associated with photo locations based on photos with your face".
  - A dialog announcing that Photos "can now tell you more about where you've been by matching your face to the locations in your photos" has one button and can't be dismissed by back or tap-outside.
  - Ask Photos queries "may be reviewed by humans".
  - Evidence: `classes5/sources/defpackage/afjz.java`, `classes2/sources/defpackage/afia.java`.
- **Face grouping is announced, not asked, in 171 countries** *(Medium–High)*.
  - Setup shows "Google Photos uses face grouping · Learn more" with **no toggle** when the SIM, network or locale country is in a hard-coded list of 171 codes (`classes6/sources/defpackage/bfey.java`). The list includes the US, Canada, India, Japan, Brazil and Australia, and leaves out the EU/EEA, UK, Switzerland and Norway.
  - Actual enablement is server-side.
- **Storage-full upsell** *(Medium)*.
  - A full-screen "out of storage" interstitial offers Google One with struck-through prices; the alternative is "Continue with a limited experience".
  - It warns that Gmail "won't work as expected".
  - Manual cleanup is framed as "delete N+ photos to get back # month of storage".
  - Memories are used as leverage. Sharing, album-add and print are gated on backup.
- **Other** *(Low–Medium)*:
  - Magic Editor's 10 saves/month paywall.
  - "Don't miss out on new Memories!" notification copy.
  - A **CapCut** tile is added to the share sheet even when CapCut isn't installed.
  - A MANAGE_MEDIA prompt removes the OS per-delete confirmation.
  - ACCESS_MEDIA_LOCATION gives unredacted photo GPS.

**Good practice:**
- Deletion copy clearly separates device and cloud deletion.
- Memories can hide people, pets and dates.
- Location is only used for the print-store locator.
- No ad ID.
- Consent screens log the exact text shown.

## 12. Discord 348.10 (`com.discord`)
Discord is a React Native app, so most logic is Hermes bytecode. It was disassembled with hermes-dec, and evidence is cited by function ID and module path in `notes/discord.md`.

- **Advertising ID tied to the account on every connection** *(High)*: on each gateway connection, the Quests/ads module reads the Google ad ID and sends an `AD_IDENTIFIER_FETCHED` analytics event with it (`modules/quests/native/ATTModal/ATTManager.android.tsx`, `AdUserActionCreators.android.tsx`). There's no consent check in that path; the ID is null only when Limit Ad Tracking is on.
- **Installed-games probe** *(Medium)*: `<queries>` lists 16 mobile games (Minecraft, Fortnite, Genshin, PUBG, CoD…). Detected games are mapped to Discord application IDs and sent to `discoverable-guilds/mobile-game-communities` for recommendations.
- **AppsFlyer starts unconditionally** in `Application.onCreate` *(Medium)*. It also reads Samsung's preload-attribution provider and the Huawei and Play install referrers.
- **Contact sync** *(Medium)*: plaintext phone numbers, re-synced on every connection. It is opt-in and disclosed ("Your contacts will be regularly sent to us").
- **Loss-framed analytics opt-out** *(Medium)*: turning off "use data to improve Discord" warns that you "will lose access to new experimental features" and "won't be able to recover them". A full objection requires emailing privacy@discord.com.
- **Server-switchable tap and HTTP telemetry** *(Medium, default off)*: every tap with coordinates, view hierarchy and velocity, plus HTTP/websocket events. On for staff or via the experiment `2025-12-zoomed-analytics`.
- **Other** *(Low–Medium)*:
  - Sentry sends user-interaction breadcrumbs without a consent gate.
  - Nitro trial countdowns ("⏰ Only {days} left…") and churn-discount machinery.
  - Gifting streaks.
  - Sponsored Quests that teens "may still see".
  - Behavioural age inference.
  - An exported Rich-Presence RPC service any app can call.

**Good practice:**
- No location, no usage stats, no QUERY_ALL_PACKAGES.
- Ad ID honours Limit Ad Tracking.
- Clipboard is read only on paste.
- Clear auto-renew disclosure and a pause option.

## 13. Chess.com 4.10.20 (`com.chess`)
Twelve tracker SDKs in an app with a very large child audience. Paths are under `work/chess/jdex`; more in `notes/chess.md`.

- **Consent assumed "yes"** *(High)*.
  - The OneTrust consent flow only runs if the server flag `tracking_consent` is on, and **it ships off**. With it off, `TrackingConsentState.Companion.a()` sets all four categories (performance, functional, targeting, social media) to **true** (`classes9/sources/com/google/android/TrackingConsentState.java:38-44`).
  - The app never calls OneTrust's banner; only the Settings preference centre is reachable.
  - These defaults drive AppsFlyer, crash reporting, UID2 and ad personalisation.
- **Personalised ads by default, with no child-directed handling on the client** *(High)*.
  - Ads (GAM/AdMob, Prebid, Amazon, AppLovin, InMobi, Liftoff via the Aditude wrapper) are controlled only by server `show_ads` flags. Consent only toggles personalisation, which defaults on.
  - The app **never sets** AdMob's `tagForChildDirectedTreatment`/`tagForUnderAgeOfConsent` or a max ad-content rating.
  - Sign-up has no age gate. Server-assigned `gam_audiences` are pushed into ad targeting.
- **Your email turned into a UID2 ad identity** *(High, server-gated)*: when flag `ads_uid2_sdk` is on (default off) and targeting "consent" is true (default), the account email is converted to a Unified ID 2.0 token and put in the ad bidstream. There is no age check.
- **Contacts hashed without salt and kept for later matching** *(Medium)*: every contact email and phone number is SHA-256 hashed (no salt, so phone numbers are trivially reversible) and uploaded. The disclosure says it's "ONLY" used to search contacts, yet "Get notified when one of your contacts creates an account" implies non-users' hashes are retained.
- **Streak and upgrade pressure** *(Medium)*:
  - "Are you really going to lose your 1 year streak?" and "Last Chance: Play a quick game to save your streak".
  - A weekly upgrade modal.
  - "Frequent users of Game Review improve 2.7x faster".
  - Server-scheduled interstitials, including in-house "Go Premium" videos, between games, with no client-side cap.

**Good practice:**
- Facebook SDK auto-logging is off, with Limited Data Use set.
- Ad SDKs get no location.
- Logs redact PII.
- The sale countdown matches the real expiry.
- Trial terms are clear with a reminder.

## 14. Waze 5.25.0.1 (`com.waze`)
Only Crashlytics as a third-party SDK. The base APK has no native libraries (they ship in a split), so C++ logic such as ad timing couldn't be checked. Paths are under `work/waze/jdex`; more in `notes/waze.md`.

- **Every Bluetooth connection reported** *(High, server-gated)*.
  - An exported receiver (`com.waze.tide.BluetoothConnectionReceiver`) wakes Waze whenever **any** Bluetooth device connects. When Waze is backgrounded and not navigating, it reports the device's **name and class**, e.g. `AUDIO_VIDEO_CAR_AUDIO`, `WEARABLE_WRIST_WATCH`, `HEALTH_GLUCOSE`, `HEALTH_BLOOD_PRESSURE`. With "always" location, it also reports last known location from every provider.
  - The Bluetooth permission is requested as "Get turn directions in tunnels…" and doesn't mention this. The ask repeats after a cooldown.
  - Gated by `CONFIG_VALUE_DRIVE_DETECTION_TIDE_ENABLED`, shipped default appears off.
  - Evidence: `classes7/sources/com/waze/tide/t.java`.
- **"Don't show this again" makes the background-location request *more* direct** *(Medium–High)*: ticking it on the "…even when not using the app" dialog makes later triggers skip the explanation and call the system background-location request straight away. After a permanent denial it sends you to Settings (`RequestAlwaysLocationDialogActivity.java`).
- **Personalised-ads consent** *(Medium)*: asked only after a server-set number of drives, with "Personalized" as the primary button and "Not personalized" secondary.
- **Background calendar reads** *(Medium–Low)*: an exported receiver re-reads every calendar change, including event title, location and organiser email.
- **Advertising ID sent at every login**, with the Limit Ad Tracking flag *(Low–Medium)*.

**Good practice:**
- No installed-app enumeration.
- Only Eddystone beacons are parsed.
- An AADC age gate ("age won't be used for advertising").
- Consent choices are logged with the exact text shown.
- allowBackup is off.

## 15. BBC News: UK 9.19.0 (`bbc.mobile.news.uk`) and International 2026.9.0 (`bbc.mobile.news.ww`)
Two very different apps. The **UK edition** (licence-fee funded, native code) has no ad SDKs. The **International edition** is a React Native app funded by ads and subscriptions; its JS was read from strings only. Paths are under `work/bbcnews*/jdex`; more in `notes/bbcnews.md`.

- **International: Firebase Analytics with every consent signal pre-granted** *(High)*. The manifest sets analytics storage, ad storage, ad user data and ad personalisation to *granted* by default, enables ad-ID collection and automatic screen reporting, and initialises Firebase in `Application.onCreate` before the consent platform loads. No native code downgrades consent.
- **International: Permutive behavioural profiling tied to BBC IDs** *(High)*. Every page (title, URL, section, referrer) and video/ad event goes to Permutive, which returns audience cohorts. `updateIdentity()` attaches BBC federated user and device IDs **without the consent check** the page tracker uses. Per-partner encrypted copies of the federated ID are produced for third parties (strings point to Google Ad Manager).
- **UK: analytics on by default with no first-run prompt** *(Medium)*. ATInternet/Piano, Comscore, BBC BAG, UKOM and Chartbeat (engaged time, sections, logged-in state) all run from install. They can be turned off in Settings ("Send app statistics").
- **International: smaller items** *(Low)*:
  - READ_PHONE_STATE for a legacy Kantar IMEI read.
  - Custom text-selection menu emits the **selected text** to JS analytics (whether it's sent is unverified).
  - Scroll-depth tracking.

**Good practice:**
- No location permission in either edition.
- UK AppsFlyer runs only for signed-in users who allow personalisation.
- The International GAID bridge honours Limit Ad Tracking.
- Sourcepoint covers GDPR and US privacy.
- Equal-weight "Maybe later" on notification prompts.
- **Exodus flags for Adjust, AppLovin, Unity Ads and ironSource in the International edition are false positives** (consent-SDK shims only).

## 16. Signal 8.30.3 (`org.thoughtcrime.securesms`)
**Clean.** No trackers. Contact discovery sends phone numbers only, encrypted to an attested SGX enclave. Link previews go through Signal's proxy, and location is used only when you share one.
- **Prompts** *(Low)*:
  - Notification-permission megaphone every 30 days while off.
  - Paid-backup upsells at least 60 days apart.
  - A PIN reminder that backs off to monthly and can be disabled.
- **Donation asks** *(Low)*: server-controlled, not shown in the first week.

All of these are dismissible and rate-limited.

## 17. Proton VPN 5.20.57.0 (`ch.protonvpn.android`)
**Clean, with caveats.** This is the open-source F-Droid build (signed by F-Droid), so its Sentry DSN is empty and attribution code is a no-op; the Play build may differ.
- **Telemetry on by default** *(Low–Medium)*, including your ISP and real (pre-VPN) country.
- **Free-tier upsells** *(Low)*: "change server" cooldowns (4 tries, then 90 s, then 20 min), "Limited time offer" countdowns.
- **Anti-abuse "challenge" fingerprint** on login/sign-up screens *(Low)*: typing timing, keyboards, pasted text.

No ads, no ad ID, no location or contacts. QUERY_ALL_PACKAGES is used only for split tunnelling.

---

## 18. Method, evidence and limits
- **Getting the apps:**
  - Downloaded from APKPure via `apkeep`. Proton VPN came from F-Droid (signed by F-Droid, not Proton).
  - Each base APK's signing certificate was verified against the developer (`evidence/apk_identity*.txt`, `evidence/apk_sha256.txt`).
  - Nothing was installed or run.
- **Tools:**
  - **REA (Reverse Engineer Anything)** 6.4.0 (`.mcp.json`, `.claude/skills/reverse-engineer-anything`, `tools/setup.sh`) for evidence-bound package inspection and cross-reference tracing.
  - JADX 1.5.3 and Apktool 2.12.1.
  - Exodus tracker signatures; helper scripts in `scripts/`.
  - Batch 2 also needed:
    - hermes-dec, a disassembler for React Native Hermes bytecode (Discord);
    - a decoder for Telegram's hashed string bundle;
    - an emulation harness for Facebook's Superpack decoder (`scripts/superpack/`; unsuccessful).
- **Decompiled trees:**
  - **Per-DEX trees.** Most apps were decompiled one DEX file at a time (`work/<app>/jdex/classesN/sources/…`, script `scripts/decompile_per_dex.sh`). Paths in batch-2 sections are relative to `work/<app>/jdex`.
  - **Instagram.** Some citations use the earlier 83% whole-APK tree (`work/instagram/jadx_full/sources/X/…`). The same classes exist in the per-DEX tree, sometimes under different JADX aliases.
  - **Duolingo, Dexcom and Proton Mail** use `work/<app>/jadx/sources`.
  - **Facebook's** main code was not decompiled (§9).
- **Supporting files:**
  - Working notes with more pointers are in `notes/`.
  - Manifest audits are in `evidence/manifests/`. These now include `uses-permission-sdk-23` entries, which the first version of the audit missed.
  - Pattern scans are in `evidence/scans/`.
  - Excerpts and SHA-256 hashes of the injected Instagram scripts quoted in §2.1 are in `evidence/instagram_iab_js_excerpts.md`.
- **Exodus false positives:** these occur where an SDK is only probed for, not bundled (BBC News International; see §15). They are noted in the per-app sections.
- **Static only.** Remote configuration, experiments and server behaviour are invisible to static analysis. Capabilities behind switches are described with their shipped defaults where these could be read.
- **AI assistance and spot checks:** the batch-2 deep reads were run by AI agents working from the decompiled code. The most serious claims in §1 were then re-checked directly against the code: Telegram's ad-click reporting, WhatsApp's top-chats provider, Chess.com's consent default, Google Photos' face-grouping country list, and Facebook's `<queries>` list and login payload.

## 19. Not analysed
**Claude (`com.anthropic.claude`)**: the APK isn't on APKPure or Aptoide, and APKMirror, APKCombo and Aurora's anonymous token service blocked this environment. Skipped as agreed.
