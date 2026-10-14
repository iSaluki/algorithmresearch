# Dark Patterns & Data Practices in Seven Android Apps

**Static reverse-engineering study**, 13–14 Oct 2026 (second, deeper pass on Instagram, Snapchat and Reddit).
Apps: Instagram, Snapchat, Reddit (priority), Duolingo, Dexcom G7, Proton Mail. Claude was not analysed (§9).

Everything below comes from the shipped APKs: decompiled code, manifests, bundled UI text and bundled JavaScript. Findings cite the decompiled file (paths in §8). Where behaviour sits behind a server-side switch, I say so and give the shipped default. **Static analysis shows that the code exists and what it does when switched on; it can't show how many users it's switched on for.**

---

## 1. The worst findings

| # | App | Finding | Severity |
|---|-----|---------|----------|
| 1 | **Instagram** | **The in-app browser monitors the websites you visit.** Instagram injects scripts into third-party sites opened from the app (up to 131 programs, some downloaded at runtime). They **intercept the events those sites send to Google Tag Manager and to competitors' tracking pixels (TikTok, Snap, Reddit, Pinterest, X)**, list which of 26 analytics/ad tools a site uses along with their account IDs, record **which payment method you choose at checkout** (PayPal, Amazon Pay, Google Pay, Shop Pay), and capture clicks, scroll, key-press timing, page-text samples and network-request URLs. What's extracted is set by server configuration. | **Critical** |
| 2 | **Instagram** | **Location packages uploaded while the app is open:** GPS position, speed and altitude, plus nearby **Wi-Fi access points (BSSIDs, signal), cell towers and Bluetooth info**, tagged with the cross-app Meta device ID. Separately, your coordinates are sent every 12 hours (by default) to an "event insights" query. | **Critical** |
| 3 | **Instagram** | Checks which **AI assistants, AI-companion apps and automation tools** are installed (ChatGPT, Claude, Replika, Character.AI, Tasker, Home Assistant… 23 in all) and reports the list to Meta analytics, about daily. | **Critical** |
| 4 | **Duolingo** | "Streak in danger" notifications that **can't be swiped away** until the next day, red countdowns, "terminator"/"mad" mascot animations, home-screen icon and name swapped to `Duolingo🚨`, and a notification type literally called `PASSIVE_AGGRESSIVE`. | **Critical** |
| 5 | **Snapchat** | **Address-book upload with "closeness" metadata** (starred contacts, saved birthdays, photos, and, via remote switch, which messaging apps each contact uses), sent at sign-up. **Duolingo does the same**: has-birthday, has-company, has-nickname, has-address, has-photo and WhatsApp/Telegram presence for every contact. | **Critical** (profiles people who never consented) |
| 6 | **Snapchat** | **Ads inside the chat inbox ("Sponsored Snaps")** with a forced choice: "Smaller In-Feed Ads" or "Larger Banner Ads", with no "no" option. In the EU the consent modal **re-appears 48 hours after each dismissal, up to 10 times**. My AI chats are used "to improve our products **and ads**" and shared with "advertising partners", and the **paid ad-free plan still shows "sponsored … My AI responses"**. | **High** |
| 7 | **Snapchat** | **Location history and biometrics:** keeps "Places you've visited" and "travel updates" while location is on; "Footsteps" back-fills your past whereabouts from Memories; repeated nudges to "Allow all the time"; and **on-device face recognition** across Memories with face encodings linkable to Snapchat accounts (`tagged_user_id`; server-enabled). | **High** |
| 8 | **Instagram** | Other on-device profiling: training uploads for an **under-13 age model**, upload of **installed keyboards and languages**, a **device-state snapshot** (volume, music, Do Not Disturb, lock state) that **Meta's preinstalled phone services can trigger on unlock**, **continuous background contact upload**, and **camera-roll scanning on by default** with reverse-geocoded photo locations. | **High** |
| 9 | **Snapchat** | **Churn-risk targeting:** users flagged new or likely to leave get up to **15 full-screen "Added Me" takeovers per session vs 5 for others**; pushes to people who abandoned sign-up or logged out; paid streak restores, including children's purchases awaiting parent approval. | **High** |
| 10 | **Duolingo** | About **25 ad networks** in a learning app with a large child audience, plus home-network fingerprinting so reminders arrive when you get home. | **High** |
| 11 | **Reddit** | **Can't delete your account until Premium is cancelled.** Notification nags at about 15 touchpoints, new daily streaks with a "271% more karma" claim. Otherwise noticeably cleaner than Meta and Snap (§4). | **Medium** |
| 12 | **Dexcom G7** | Medical-device app that requests far more access than it uses, with string-encrypted code that hinders audit (§6). | **Medium** |
| — | **Proton Mail** | Cleanest app: 14 permissions, no ad or analytics SDKs, self-hosted crash reporting (§7). | Low |

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

## 8. Method, evidence and limits
- **Getting the apps:** APKPure via `apkeep`; each base APK's signing certificate verified against the developer (`evidence/apk_identity.txt`, `evidence/apk_sha256.txt`). Nothing was installed or run.
- **Tools:** **REA (Reverse Engineer Anything)** 6.4.0 (`.mcp.json`, `.claude/skills/reverse-engineer-anything`, `tools/setup.sh`) for evidence-bound package inspection and cross-reference tracing; JADX 1.5.3; Apktool 2.12.1; Exodus tracker signatures; `scripts/`.
- **Decompiled trees:** Instagram, Snapchat and Reddit were decompiled **per DEX file** (`work/<app>/jdex/classesN/sources/…`, script `scripts/decompile_per_dex.sh`) after whole-APK runs ran out of memory. Some Instagram citations use the earlier 83% whole-APK tree (`work/instagram/jadx_full/sources/X/…`). The same classes exist in the per-DEX tree, sometimes under different JADX aliases. Duolingo, Dexcom and Proton use `work/<app>/jadx/sources`. Working notes with more pointers are in `notes/`; excerpts and SHA-256 hashes of the injected Instagram scripts quoted in §2.1 are in `evidence/instagram_iab_js_excerpts.md`.
- **Static only.** Remote configuration, experiments and server behaviour are invisible to static analysis; capabilities behind flags are described with their shipped defaults.

## 9. Not analysed
**Claude (`com.anthropic.claude`)**: the APK isn't on APKPure or Aptoide, and APKMirror, APKCombo and Aurora's anonymous token service blocked this environment. Skipped as agreed.
