# Dark Patterns & Data Practices in Seven Android Apps

**Static reverse-engineering study**, 13 Oct 2026.
Apps: Snapchat, Duolingo, Instagram, Reddit, Dexcom G7, Proton Mail, Claude (Claude: not analysed — see §7).

Everything below comes from the shipped APKs: decompiled code, manifests and bundled UI text. Each finding points at the file and line in the decompiled tree (`work/<app>/jadx*/sources/...`, which can be regenerated with `tools/setup.sh` and the commands in §6). Where something depends on a server-side switch or experiment, I say so. **I can show that the code exists and what it does when it's switched on. I can't show how many people it's switched on for.**

---

## 1. The worst findings

| # | App | Finding | Severity |
|---|-----|---------|----------|
| 1 | **Duolingo** | "Streak in danger" notifications you **can't swipe away** until a set time the next day, plus red countdown timers, angry or "terminator" mascot animations, and the home-screen icon and name changing to things like `Duolingo🚨` | **Critical** (manipulation) |
| 2 | **Instagram** | Checks which **AI assistants, AI-companion apps and automation tools** you have installed (ChatGPT, Claude, Replika, Character.AI, Tasker, Home Assistant…) and reports the list to Meta analytics | **Critical** (tracking) |
| 3 | **Snapchat** | Uploads your **whole address book with "closeness" metadata**: which contacts you starred, which have a saved birthday or photo, and (via a remote switch) which other messaging apps each contact uses. It does this during sign-up. | **Critical** (tracking, including non-users) |
| 4 | **Instagram** | On-device profiling pipeline: training data for an **under-13 age model** (`AGE_SIGMA` / `u13_example`) is uploaded; your **installed keyboards and their languages** are uploaded; and a **"device state snapshot"** (volume, music playing, Do Not Disturb, lock state, brightness…) can be triggered on phone **unlock** by Meta services that phone makers preinstall | **High** |
| 5 | **Snapchat** | **Churn-risk targeting.** Users the server marks as new or likely to leave get up to **15 full-screen "Added Me" takeovers per session, against 5 for everyone else**. People who abandon sign-up get pushes, and lost streaks can be bought back (the code even handles a child's purchase waiting for parent approval). | **High** |
| 6 | **Duolingo** | A language-learning app with a large child audience bundles **~25 advertising networks** (Pangle/ByteDance, ironSource, Unity, Vungle, Meta, Mintegral, InMobi…). An experiment **fingerprints your home Wi-Fi** (hashed gateway IP and subnet) so reminders arrive when you get home. | **High** |
| 7 | **Reddit** | **You can't delete your account until you've cancelled Premium.** Notification-permission prompts are wired into about 15 actions (voting, commenting, posting, chatting, app launch…). | **Medium** |
| 8 | **Dexcom G7** | A **medical-device** app asks for far more access than it uses (`QUERY_ALL_PACKAGES`, microphone, phone state, always-on location). Its code is **string-encrypted and calls key APIs by reflection**, which makes independent auditing hard. Followers' "Share" alerts and data restore need cloud data-sharing consent. | **Medium** |
| — | **Proton Mail** | The cleanest app: 14 permissions, no ad or analytics SDKs, self-hosted crash reporting. The only dark patterns found were seasonal "SALE" banners. | Low |

The details follow, worst first within each app.

---

## 2. Duolingo 6.101.2 (`com.duolingo`)

### 2.1 Notifications you can't dismiss *(Critical)*
- `defpackage/oms.java:1502-1525`: for `NotificationType.STREAK_SAVER`, if notifications are on, the phone runs Android 13+ (Samsung on API > 34 and a list of phone makers are excluded, presumably where the trick doesn't work), **your streak is ≥ 7 days**, and a remote flag is on, Duolingo schedules `UnstickNotificationWorker` for a configured time **the next day** (`plusDays(1).atTime(...)`).
- `defpackage/lg40.java`: that worker finds the live notification carrying `FLAG_NO_CLEAR` (`flags & 32`), removes the flag, and logs `sticky_notification_unstuck` with `unstuck_delay_minutes`. So the notification really is posted as non-swipeable, and stays that way overnight.
- Streak-saver notifications get their own **IMPORTANCE_HIGH** (heads-up) channel, while other types get default importance (`oms.java:559`).
- The debug catalogue (`defpackage/sks.java`) shows the production variants: *"Watch out! Your streak is in danger!"* with a red **3,600-second countdown** "to save your streak", and mascot animations named **`terminator_duo`, `mad_duo`, `laser_duo`, `jaw_open_duo`, `surprised_duo`**. There's also *"XP Boost expires soon…"* with its own timer.

**Why it matters.** Taking away the user's ability to dismiss a notification turns a reminder into a nag that can't be ignored. Combined with loss aversion (a streak built over weeks), threatening animations and countdowns, it's a textbook coercive dark pattern, aimed at exactly the users most invested in their streak.

### 2.2 Changing the app's icon and name *(High)*
The manifest declares activity aliases that swap the launcher icon and label (`apktool/AndroidManifest.xml`):
- `PreStreakSaver1…9Launcher`: **nine escalating icons** (`ic_launcher_pre_streak_saver_3…9`) as the day goes on;
- `StreakSaverLauncher{Hourglass,Siren,AlarmClock,ExclamationMarks,EmojiQuestionMark,Eyes…}` with labels **"Duolingo⏳", "Duolingo🚨", "Duolingo⏰", "Duolingo‼️", "Duolingo❓", "Duolingo👀", "Duolingo⁉️"**;
- `FixedRetentionChallengeLauncher` (`ic_launcher_boiling_cucumber`), plus a push type `APP_ICON_UPDATE`.

The pressure reaches the home screen, even if notifications are off.

### 2.3 A notification taxonomy built for retention *(High)*
`com/duolingo/data/notifications/NotificationType.java` defines, among others: **`PASSIVE_AGGRESSIVE`**, `ABANDONED_CART_BASICS`, `ABANDONED_CART_PLACEMENT` (re-targeting after you leave a paywall or placement test), `REACTIVATION`, `RESURRECTION`, `CONTINUOUS_RESURRECTION`, `RESURRECTED_QUEST`, `COMEBACK_BOOST`, `FRIENDS_RESURRECTION` (friends asked to nudge lapsed friends), `PASSED` ("someone has passed you"), `LEADERBOARDS_FRIEND_NUDGE`, and `REMOVE_AND_RESEND_NOTIFICATION` (silently re-posting a notification so it jumps back to the top of the shade). The signal object that drives notifications (`defpackage/uls.java`: `NotificationSignal(…, isRiskUserInHapticBucket=…, streak=…)`) also carries a haptics experiment for users flagged as at-risk.

### 2.4 Learning where "home" is, without location permission *(High)*
- `com/duolingo/notifications/TriggeredNotificationWifiWorker.java`: the experiment **`wifiTriggeredPracticeReminderExperiment`**. A practice push arrives flagged `should_drop_notification=true` and is held until the device is on Wi-Fi. It logs `is_device_idle_mode`, `is_power_save_mode`, `is_ignoring_battery_optimizations` and **`network_days_seen_before_today`**.
- `defpackage/gde.java`: identifies the network by **hashing the default-gateway IPv4 address and subnet prefix**, and counts the days each network has been seen. That's effectively "you're at a place you visit every day" detection, with no location permission involved.

### 2.5 Pay-to-escape mechanics and confirmshaming *(Medium)*
Shipped copy (`res/values/strings.xml`):
- *"Get a **League Repair** to reclaim your spot…"*, *"Don't get demoted! Keep moving up with a Timer Boost."*: paying to avoid social demotion.
- *"Add Widget to Repair"*, *"Never lose your streak again with Duo on your phone's home screen!"*: a streak repaired in exchange for a permanent home-screen widget.
- *"Wait, don't go! If you quit, you'll lose your progress."*, *"Losing makes me cry on the outside AND inside!"*, *"Hello, sadness…"*, *"Come back today to protect your streak…"*
- *"Reaching a N day streak will put you in the top X% of all streaks"* (social comparison).
- Cancellation: *"Are you sure you want to leave? You'll lose access to Max."*, *"You'll lose access to Super Family Plan in N hours"*.

### 2.6 Advertising surface *(High, given the audience)*
32 Exodus-catalogued SDKs (`evidence/trackers_exodus.json`). These are **fully bundled** (hundreds to thousands of classes each): Pangle/ByteDance, ironSource, Unity Ads, Vungle, Meta Audience Network, AppLovin MAX, Adjust, Mintegral, InMobi, Smaato, Fyber, Chartboost, HyprMX, BidMachine, PubNative, Moloco, SuperAwesome. Yandex, myTarget, Ogury, Tapjoy and maio appear only as mediation-adapter references. The manifest requests `AD_ID` and Privacy Sandbox `ADSERVICES_AD_ID/ATTRIBUTION/TOPICS`.
*Mitigation found:* children are tagged `setTagForChildDirectedTreatment(1)` for AdMob (`com/duolingo/data/ads/u.java:157`), and Adjust has COPPA switches. I didn't verify that every mediated network receives the child flag.

### 2.7 Telemetry on whether Android is throttling the app *(Low)*
`defpackage/pu60.java:771+`: every analytics event carries `app_standby_bucket` (whether Android is restricting Duolingo), `audio_output_volume`, SIM country, timezone, font scale and more.

---

## 3. Instagram 451.0.0.53.80 (`com.instagram.android`)

### 3.1 AI and automation app detector *(Critical)*
- `X/EnumC525730Kkl.java` lists 23 packages: **Manus, Replit, YouWare, Emergent, a0.dev, NotebookLM, ChatGPT, Gemini, Copilot, Perplexity, Claude, Replika, Character.AI, Poe, Pi, Tasker, IFTTT, Zapier, MacroDroid, Automate, Home Assistant, Notion, Airtable**. Each is also declared in the manifest's `<queries>`, so Android lets Instagram see them.
- `X/C367410Ebz.java:58-104` (startup task `com.facebook.odinusecases.aiappsdetector.ig4a.AiAppsDetectorStartupTaskBinder`): behind MobileConfig flag `36330376737612461`, at most once per configurable interval (default 24 h, stored in prefs `ig_ai_apps_detector_prefs`), it calls `getPackageInfo` on each package, builds the list of installed ones, and logs it as **`installed_apps`** in the analytics event **`odin_ai_apps_detector`** (`X/C627202di` is Instagram's analytics logger; the event is sampled).
- I located the caller independently with REA's reference tracer (`evidence/rea/instagram.0Kkl.refs.json`).

**Why it matters.** Which AI companion apps someone uses (Replika, Character.AI, Pi) is a sensitive signal: it can reveal loneliness, mental-health use, or relationship status. Which automation tools they use reveals technical sophistication. Neither is needed to run a photo-sharing app, and none of it is visible to the user.

### 3.2 Training data for an under-13 age model *(High)*
`X/C1582206Ke.java:470-520`: reads an on-device store called **`underage_storage`**, packages it as an Odin training example named **`u13_example`**, and uploads it under use case **`AGE_SIGMA` v0.0.1**. Performance markers `ODIN_AGE` and `ODIN_AGE_U13_UPLOAD` match. Age assurance can serve child safety, but it's done invisibly, from behavioural features, and the client doesn't show which features go into `underage_storage`.

### 3.3 Uploading keyboards and languages *(High)*
`X/C1582206Ke.java:125-330`: enumerates `getEnabledInputMethodList()` and each keyboard's language subtypes, together with `CurrentKeyboardLanguages`, and uploads them via the GraphQL mutation **`ZeroDayLanguageSignalUploadMutation`** (`input_methods`). Installed keyboards are both a device fingerprint and a proxy for language or ethnicity.

### 3.4 Device-state snapshot, triggerable on unlock *(High)*
- `X/C2111108Rp.java` (`device_state_snapshot_client`) has collectors for: audio mode, ringer mode and volume, **is music playing**, screen brightness, connectivity, display state, airplane mode, **Do Not Disturb filter**, media routing (cast/Bluetooth), **device locked / interactive**, and app foreground state. It feeds `IG_ODIN_DEVICE_SIGNALS_COLLECTION` → `pdp_signals_mobile` (`X/EnumC703502q1.java:125`).
- The manifest declares an exported receiver `PreloadsFbnsUnlockSignalReceiver` for `com.facebook.oxygen.services.fbns.SYS_ENTER`. That action is broadcast by **Meta's "Oxygen" system services, which phone makers preinstall** (`com.facebook.services`, `appmanager`, `system`; all are in Instagram's `<queries>`). The receiver ships disabled and is switched on at runtime.

**Why it matters.** This is context sensing: knowing whether you're on Do Not Disturb, listening to music, or have just unlocked your phone is exactly what you'd want for timing engagement pushes. The unlock trigger relies on bloatware most users can't remove.

### 3.5 Visibility of nearly every installed app *(Medium)*
Instagram doesn't request `QUERY_ALL_PACKAGES`, but its `<queries>` includes a bare `<intent><action android:name="android.intent.action.MAIN"/></intent>` plus `VIEW` with `scheme="*"`. On Android 11+ that makes practically every launchable app visible: a well-known way around the package-visibility restrictions. (Snapchat does the same; Duolingo limits it to launchers.)

### 3.6 A "you have unseen likes" timer *(Medium)*
`X/C2456109l1.java` and `X/AnonymousClass0297.java` (case 36): when a session ends, Instagram sets an `AlarmManager` alarm for **+24 h** that posts a local `UNSEEN_LIKES` notification. It's a client-side re-engagement trigger that doesn't depend on any real new activity.

---

## 4. Snapchat 14.27.0.53 (`com.snapchat.android`)

### 4.1 Contact upload with "closeness" metadata *(Critical)*
- `defpackage/C0111Ac0.java:403` reads the entire `ContactsContract.Data` table: `contact_id, display_name, contact_last_updated_timestamp, starred, photo_uri, mimetype, data1-3`.
- For each contact it builds `Contact(contactId, name, type, phoneNumbers, lastUpdatedTimestamp, emailAddresses, starred, hasEvent, hasPhoto, firstSocialLink)` (`defpackage/C40594pf4.java:103-193`).
- **`firstSocialLink`**: if a contact row has a mimetype matching a **server-supplied keyword list** (`frnd_contact_social_link_mime_type_keywords`, empty by default; `defpackage/WR8.java:114`), that mimetype is recorded. Other apps add these rows (e.g. `vnd.com.whatsapp.profile`), so this can reveal which messaging apps each of your contacts uses.
- These fields are serialised per number as `{number, hasStarred, hasPhoto, hasSavedDate, hasSocialLink, contactType}` (`defpackage/C16092Zh4.java`) into `contacts_with_meta_data` (`defpackage/C54695yr8.java`, built in `AbstractC13515Vh4.a`).
- They're sent to **`/bq/find_friends_reg` during registration** (header `early_contact_sync=first|second`) and to `/ph/find_friends` (`com/snap/identity/FriendingHttpInterface.java:23-28`). The request also carries a flag `enable_find_friends_for_UK_under_age`.
- Contact changes are re-detected through `contact_last_updated_timestamp` (`defpackage/C43861rn5.java:199`).

**Why it matters.** "Starred" and "has a saved birthday" are strong signals of how close you are to someone, and they describe people who never agreed to anything and may not use Snapchat at all. The social-app field can be switched on from the server without an app update.

### 4.2 Churn-risk targeting *(High)*
- Server-assigned user segments: `is_new_user`, `is_14_days_new_user`, **`is_deep_churn`, `is_high_churn_risk_active/new/resurrected`** (`defpackage/EnumC23587eaa.java:663-677`, mapped in `HB3.java`).
- The "Added Me" full-screen takeover on the camera is capped at **15 per session for new or churn-risk users and 5 for normal users** (`EnumC23587eaa.java:654-660`, consumed by `AddedMeTakeOverOnCameraProviderImpl` in `C20018cG.java:45-46`).
- `RegistrationReengagementPushManager` / `GROWTH_NOTIFICATION_REGISTRATION_REENGAGEMENT`: push notifications to people who **started but didn't finish** signing up.
- Free streak restores for returning users: `ResurrectedRestoreEligibilityCheck`, `RESURRECTED_RESTORE_ELIGIBILITY_WINDOW`, `resurrection_7_days_or_greater`. There's also a Snapchat+ win-back SKU, `winback-1m-599`.

### 4.3 Streaks *(Medium–High)*
- *"Get notified 1 hour before your streak ends"*, ⌛ expiry indicators, *"YOUR $0-DAY STREAK ENDED"*.
- **Paid streak restores**: *"Snapstreaks that have ended in the past 48 hours can be restored through an in-app purchase"*, *"Restore for %1$s"*, plus monthly free restores as a Snapchat+ perk. The copy *"You already have a pending purchase waiting to be approved"* is Google Play's family-approval state, i.e. a child asking a parent to pay to restore a streak.

### 4.4 Location consent bundled with ads *(Medium)*
The location prompt (`app_permission_description`): *"Improve your Snap Map by enabling location – this will **not** share your location with friends. Snapchat will also use your location for Filters, **Ads**, and more."* Advertising rides along with a consent framed as being about the map. The in-app browser has the same pattern: *"Snapchat will use your activity within the in-app browser to … personalize … the ads"*.

### 4.5 Smaller items
- Bare `MAIN` intent query (see §3.5), giving visibility of almost all apps.
- `READ_PHONE_NUMBERS`/`getLine1Number` used for phone-number autofill at sign-up (`defpackage/C50121vs7.java`). Expected behaviour.

---

## 5. Reddit 2026.40.0, Dexcom G7 2.2.1, Proton Mail 7.11.10

### Reddit (`com.reddit.frontpage`)
- **Account deletion blocked by the subscription** *(Medium)*: *"To delete your account, you need to cancel your Reddit Premium subscription first."*
- **Constant notification prompting** *(Medium)*: pre-prompt, re-prompt and re-enablement states (`com/reddit/notification/domain/model/NotificationEnablementState.java`) with entry points on **AppLaunch, SessionChange, VoteComment, CommentCreation, PostCreation, FollowComment/Post/User, Chat, StartChat, DirectMessage, AcceptChatInvite, SetAMAReminder…** Escalating banners: *"Don't miss out"*, *"Be in the know"*. The consent is bundled: *"Get notified of the best content for you, **as well as** replies to your posts"*. If you choose "Only post & comment notifications", you get an upsell back to all notifications (`isEligibleForAllNotificationUpsell`).
- **Ads that send you notifications** *(Low–Medium)*: an "ad reminder" feature, *"Get a notification so you don't miss out."*
- **Asks for more than it uses** *(Low)*: `PACKAGE_USAGE_STATS` is declared, but the only call is `getAppStandbyBucket()` for Reddit itself (`defpackage/z090.java`). `READ_GSERVICES` exists so Google reCAPTCHA can read the **GSF Android ID**, a persistent device identifier (`com/google/android/recaptcha/internal/zzcx.java:43`).
- **Reasonable:** AppsFlyer only starts when `TrackingAndAttributionLevel != NONE`, with partner sharing filters (`com/reddit/mmp/appsflyer/c.java`).

### Dexcom G7 (`com.dexcom.g7`)
- **Permissions beyond what's needed** *(Medium)*: `QUERY_ALL_PACKAGES` (the only use I found is checking for Dexcom's own Clarity app, which a one-line `<queries>` entry would cover), `RECORD_AUDIO` (voice entry), `READ_PHONE_STATE`, `CALL_PHONE`, `ACCESS_BACKGROUND_LOCATION`, and Health Connect reads of heart rate, steps, exercise and calories. Copy: *"You must **always** allow location permission to continue."* Location is also used to check your country of residence (`com/dexcom/dexcomone/utils/CountryOfResidenceService.java`).
- **Code that's hard to audit** *(Medium)*: all string literals are encrypted (e.g. `HandlerC2189.m53923(...)`) and `PackageManager` calls go through reflection (`PackageManagerUtils.java`). For software that drives insulin-dosing decisions, this makes independent privacy and safety review much harder.
- **Features gated on consent** *(Low–Medium)*: *"You can't use Share if you don't allow data sharing to the cloud"*, *"Must Share with Dexcom"* (to use the Lilly Tempo pen), *"If you'd like to be able to restore data next time, change your data consents…"* Sharing to followers genuinely needs the cloud, but the consent text itself comes from Dexcom's server (CAMS), so **I can't tell from the APK whether it's bundled with research or marketing uses.**
- Firebase Analytics is turned off by default in the manifest. Qualtrics survey SDK and Crashlytics are present.

### Proton Mail (`ch.protonmail.android`)
- 14 permissions (3 dangerous: camera, notifications, contacts for autocomplete and import). Only Sentry is detected, and it reports to Proton's own server (`api.protonmail.ch/core/v4/reports/sentry`, `androidx/activity/b0.java:228`) with session replay not configured. Firebase analytics, ad-ID collection and messaging auto-init are all off.
- There's a `crashReports` user setting. I didn't confirm that it gates the SDK.
- Dark patterns are limited to drawer banners (*"Black Friday Sale"*, *"SPECIAL OFFER"*) and upgrade gates. Auto-renew prices are disclosed (*"Welcome offer. Auto-renews at %s"*).

---

## 6. Checked and cleared (false positives)
These looked suspicious at first but turned out to be benign. They're listed so the findings above can be weighed fairly.
- Snapchat reads the Wi-Fi BSSID only as a local key for a bandwidth-estimate cache (`E1b.java`). Its queries for phone makers' "security center" apps are deep links to permission settings, and Netflix/Spotify are "open in app" targets.
- Instagram's `READ_CALL_LOG` is used for **flash-call phone verification**: it reads only the latest call within a short window (`X/AbstractC1331880pRm.java:287`). Its cell-tower and Wi-Fi scan reads sit inside an internal `IgLocationRequestDetector` audit hook.
- Reddit's `getInstalledPackages` only checks whether the Play Store is installed. Its accessibility-service query only affects snackbar timing.
- Clipboard reads in all apps happen on paste into OTP, chat or comment fields.

## 7. Method and limitations
- **Getting the apps:** APKPure via `apkeep` (EFF), arm64 splits. Every base APK's **signing certificate was checked** against the developer's known identity (Instagram "Kevin Systrom", Snapchat "Captain Captcha", Proton Technologies AG, Duolingo, reddit Inc., Dexcom via Play App Signing); see `evidence/apk_identity.txt` and `evidence/apk_sha256.txt`. Nothing was installed or run.
- **Tools:** **REA (Reverse Engineer Anything)** 6.4.0 with the audited `jadx-headless-mcp` 0.7.1 engine and Apktool 2.12.1 (set up in this repo: `.mcp.json`, `.claude/skills/reverse-engineer-anything`, `tools/setup.sh`), used for evidence-bound package inspection and cross-reference tracing. JADX 1.5.3 for full decompilation. Exodus Privacy tracker signatures. The repo's own scanners are in `scripts/`.
- **Coverage:** Duolingo, Proton, Dexcom and Instagram were decompiled fully. Reddit's tree is about 84% complete (JADX stalled on one class). Snapchat's tree is about 76% complete (the first pass ran out of memory), with gaps filled by searching raw DEX strings.
- **Static analysis only.** Remote config, A/B flags and server behaviour can't be seen from the APK. Many findings are **capabilities behind server-side flags**, and are worded that way.
- **Claude (`com.anthropic.claude`) was not analysed.** It isn't on APKPure or Aptoide, and APKMirror, APKCombo and Aurora's anonymous Google Play token service all blocked this container (Cloudflare 403 or proxy denial). With a Google Play AAS token for `apkeep`, or the APK uploaded to `apks/`, it can be run through the same pipeline.
