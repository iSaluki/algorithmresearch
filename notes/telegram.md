# Telegram 13.0.1 (org.telegram.messenger, Google Play build) — working notes (paths under work/telegram/jdex)

UI strings are not in resources.arsc: they ship in assets/localization_en.bin (TL-serialized, keyed by Java String.hashCode() of the R.string name). Decoded locally with a scratch script (names from org/telegram/messenger/R.java, 11,387/11,395 resolved). Quoted copy below comes from that file.

## 1. "Emoji Stake": staking TON on dice rolls in chats (gambling-like, server-gated beta)
- TLRPC.TL_inputMediaStakeDice {game_hash, ton_amount, client_seed} (classes3/sources/org/telegram/tgnet/TLRPC.java:34327). TL_emojiGameDiceInfo {game_hash, prev_stake, current_streak, plays_left, params[7]} (TLRPC.java:28781). Requested with messages.getEmojiGameInfo (classes/sources/org/telegram/messenger/MessagesController.java:27448).
- Sheet classes3/sources/org/telegram/ui/qa1.java:82-220: title "Emoji Stake" + "Beta"; text "A limited play-test of the upcoming emoji mini-game platform for a small group of users."; a returns table built from the 7 server `params` (multiplier = param/1000, qa1.java:112-119); "A streak resets after 3 🎲 or a stake change."; button "Save and Roll".
- Outcome copy: StakeDiceActionYouWon "You won 💎 %s" / StakeDiceActionYouLost "You lost 💎 %s"; others in the chat see "un1 won/lost 💎 %s".
- Entry point: tapping any "stakeable" dice message in a chat loads stake info and opens the stake flow (classes3/sources/org/telegram/ui/zn.java:4085-4088). So people see other users' wins and are invited to play from there.
- Server config ton_stakedice_stake_amount_min/max/suggested_amounts (MessagesController.java:3571, 4474, 4481). The client has no age or region check. Availability is entirely server-side (TL_emojiGameUnavailable).

## 2. Sponsored-message telemetry vs. "doesn't track whether you tapped" copy
- SponsoredMessageInfo2Description2: "Unlike other apps, Telegram doesn't track whether you tapped on a sponsored message and doesn't profile you based on your activity."
- Client sends messages.clickSponsoredMessage {random_id, media, fullscreen} when a sponsored message is tapped: classes3/sources/org/telegram/ui/oo.java:14595-14603 (chat ads), classes3/sources/org/telegram/ui/kw.java:169 (sponsored peers in search), classes/sources/org/telegram/messenger/video/VideoAds.java:975-985 (logSponsoredClicked). Also sends messages.viewSponsoredMessage on impression (oo.java:15346, VideoAds.java:988-998, classes3/sources/xe/y.java:1322). Both go over the user's authenticated MTProto session, so the server can link them to the account. The copy may mean "not used for profiling", but literally it is contradicted.
- Ad surfaces: channels, bots (BotMonetization*), search results ("SearchAd" / contacts.getSponsoredPeers, xe/y.java:702), and new in-video ads (VideoAds.java). The video-ad close button only appears after server-set min_display_duration (VideoAds.java:181, 204, 255, 746). Ads can be removed only with Premium: "Hide ad" on a non-Premium account opens the Premium sheet (VideoAds.java:404-417, 440-453). Copy: RevenueSharingAdsInfo3Subtitle "You can turn off ads by subscribing to **Telegram Premium**".
- Labeling: the server flag `recommended` replaces the "Sponsored" label with "Recommended" (Cells/u1.java:15459, p20.java:179). A paid placement can therefore be labelled "Recommended".
- Fair note: ad context sent is the peer/msg only. The copy says ads are "based on the channel" / "search query", and the client does not attach device or ad IDs.

## 3. Contact upload: names + raw phone numbers, continuous, on by default; also scrapes "+number" strings from other contact fields
- UserConfig.syncContacts default true (classes/sources/org/telegram/messenger/UserConfig.java:95, 569); suggestContacts default true (:96, 571).
- Upload: TL_contacts_importContacts in batches of 500 of TL_inputPhoneContact {client_id, phone, first_name, last_name} (ContactsController.java:1546-1550, 1993-2005). Not hashed. Projection: lookup, data1 (number), data2, data3, display_name, account_type (:109). Name fields: given/family/middle (:110).
- For address-book contacts with has_phone_number=0, the code queries data1..data4 of ALL their Data rows (any mimetype: email, note, address, IM, organisation…). It regex-matches `.*(\+[0-9 \-]+).*` and treats the hit as a phone number to import (ContactsController.java:3346-3400). This means phone-like strings in notes or other fields are uploaded too.
- Re-sync via ContentObserver on Contacts (:1255) and a forced re-import at least every 86400 s (:2109).
- Pre-permission dialog (classes3/sources/org/telegram/ui/Components/g5.java:5370-5395): "Your contacts will be **continuously synced** with Telegram's **heavily encrypted cloud servers**." with Continue / Not now. "Not now" stops the prompt (kz.java:7946, 10236). A "!" badge stays on the Contacts tab until the prompt is answered (classes3/sources/org/telegram/ui/xh0.java:759-768).
- Settings copy is accurate: SyncContactsDeleteText "This will remove your contacts from the Telegram servers.\n\nIf 'Sync Contacts' is enabled, contacts will be re-synced."
- "Contact joined Telegram" notifications: EnableContactJoined default true, synced to the server (MessagesController.java:15036-15044, 15767). Joining Telegram notifies everyone who has your number in their book (server-side).
- Writes into the system address book under the Telegram account (sync adapter): "Telegram Profile/Voice Call/Video Call" rows (ContactsController.java:240-290). A hidden "TelegramConnectionService" group with placeholder numbers "+99084<id>" is used for the VoIP ConnectionService (:2566-2620). Benign.

## 4. No in-app account deletion; only an inactivity timer
- Settings › Privacy › "Delete my account" is a section header (classes3/sources/org/telegram/ui/ty0.java:274). Its only control is "If away for" with 30/90/182/365/548/730 days (account.setAccountTTL, classes3/sources/org/telegram/ui/ax.java:603-614). DeleteAccountHelp: "If you do not come online at least once within this period, your account will be deleted…". The default TTL is server-side.
- account.deleteAccount is called in only two places: the "Forgot password" reset path (oh0.java:305, xu.java:298) and declining a ToS update ("Decline ToS update", Components/e21.java:39). telegram.org/deactivate is linked only from the Passport password-recovery screen (sm0.java:80). An ordinary user cannot delete the account immediately in-app.
- AreYouSureLogoutGrams: logging out "will … **delete wallet backups holding %s**". Logging out can therefore strand wallet funds if the recovery phrase was not saved.

## 5. Built-in TON wallet; "not even Telegram" backup claim
- Self-custodial wallet (classes4/sources/org/telegram/ui/Wallet/*, native WalletEngine2; 236 "Wallet*" strings: collectibles, TonConnect, "Buy with cash or crypto", "Free (paid by Telegram)" gasless fees). Manifest <queries> for scheme ton.
- Key backup (Wallet/o.java:240-405, ig/v.java:600): the mnemonic is split into shares. Each share is encrypted via ECDH to a public key of one of three Telegram "holder DCs" (TL_wallet.getBackupHolderDcs / holderDc.public_key) and uploaded with wallet.enableBackup. Restore: wallet.exportSecretPhrase requires the 2FA password SRP (ui/mi.java:40); then each DC re-encrypts its share to a fresh client ephemeral key (Wallet/h.java:85-100).
- Copy WalletBackupEnabledDescription: "split into three parts and stored across three continents. It can only be reassembled on your devices, so no one — not even Telegram — can access your key." Cryptographically, each holder DC (operated by Telegram) can decrypt its own share. The guarantee rests on Telegram's operational separation of its own DCs, not on anything the client enforces. The default for the backup toggle was not determined.

## 6. Age verification by selfie through a server-named bot mini app (UK)
- ThemeActivity.C0 (classes3/sources/org/telegram/ui/ThemeActivity.java:248-370): gated by config needAgeVideoVerification + verifyAgeBotUsername; country default "GB", min age 18 (MessagesController.java:2505-2507). Asks for camera permission ("Telegram needs access to your camera so that you can confirm your age."), resolves the bot username and opens its Web App.
- The mini app returns {passed, age, gender, genderProbability} via web_app_verify_age (classes4/sources/org/telegram/ui/web/c1.java:1906-1918). The client uses only age ≥ min. Copy AgeVerificationTextGB: "This is a one-time process using your phone's camera. Your selfie will not be stored by Telegram." The facial analysis runs inside a WebView page whose code is not in the APK, and that page also infers gender.

## 7. Premium / Stars monetisation pressure
- Throttled transfers: on FLOOD_PREMIUM_WAIT (ConnectionsManager.java:850-862) a toast appears: "Download speed limited — Subscribe to **Telegram Premium** and increase download speeds %d times" (default 10x; uploadPremiumSpeedupDownload/Upload 10.0). It is shown at most once per uploadPremiumSpeedupNotifyPeriod (default 3600 s) (MessagesController.java:2604-2606; oo.java:16052-16064; Components/qo0.java:152-166).
- Server-pushed dialog-list suggestions: PREMIUM_UPGRADE / PREMIUM_ANNUAL ("Save on your subscription up to **%1$d%%**"), PREMIUM_RESTORE ("Get Premium back with up to **%1$d%%** off"), PREMIUM_GRACE ("⚠️ … Access to Telegram Premium is expiring!"), PREMIUM_CHRISTMAS, BIRTHDAY_CONTACTS_TODAY ("It's %s's **birthday** today! 🎂 Send them a Gift."), BIRTHDAY_SETUP, USERPIC_SETUP (kz.java:1396-1542, 4142). All are dismissible.
- SETUP_LOGIN_EMAIL_NOSKIP: the server can open a full-screen login-email setup with a no-skip flag (MessagesController.java:24777-24786 → kz.java:6529-6542, oh0.f0=true).
- Quotas with upsell: AIEditorLimitText "Get **Telegram Premium** for **50x** more AI text transformation per day", SummaryLimit, TranscriptionTrialEndBuy.
- Gifts/collectibles: limited-edition scarcity ("Sold Out!", "1 of %s", "Only %s of such collectibles have this attribute"), Stars auctions with rounds ("You've been outbid", "Raise Bid"), resale.
- Paid reactions: one tap sends Stars, with a 5 s undo bulletin (classes4/sources/qg/s5.java:47-75), then messages.sendPaidReaction (:123). "Show me in Top Senders" leaderboards.
- First-party funnel telemetry via help.saveAppLog: premium.promo_screen_show {source}, premium.promo_screen_tap {item}, premium.promo_screen_accept, premium.promo_screen_fail (PremiumPreviewFragment.java:661-715; BillingController.java:523). These events are tied to the account and have no opt-out. Also fcm/hcm token timing, plus android_dual_camera {Build.MANUFACTURER+MODEL} when the server flag collectDeviceStats is set (default false, MessagesController.java:23587; classes4/sources/ug/w0.java:135-153).

## 8. Notification-permission re-prompt forever (backoff)
- classes3/sources/org/telegram/ui/xk0.java:143-165: after dismissal, re-asks after 1 d → 3 d → 7 d → then every 30 d indefinitely (askNotificationsAfter/askNotificationsDuration). The sheet has a single "Continue"/"Open Settings" button with copy "Please allow Telegram to send you notifications to stay in touch with your friends and family."

## 9. Mini-app (bot WebView) bridge
- Events (c1.java): request_phone (confirm: "**%s** will know your phone number."), request_location / check_location (per-bot permission "requests access to your location… revoke… in the profile page"), biometry_*, device_storage_* and secure_storage_*, request_file_download, add_to_home_screen, read_text_from_clipboard, start_accelerometer/gyroscope/device_orientation, verify_age, share_to_story, set_emoji_status.
- Clipboard read only for attach-menu bots and within 10 s of a user tap (c1.java:1731-1740). Good gating.
- Motion sensors (accelerometer/gyroscope/orientation) can be streamed at up to 50 Hz (refresh_rate clamped to 20–1000 ms) with no user prompt (c1.java:1672-1683, 1787-1798, 2214-2228). This matches web-platform norms but is a fingerprinting/keystroke-inference vector.
- WebView User-Agent for bot web apps appends "Telegram-Android/<ver> (<Manufacturer> <Model>; Android <ver>; SDK <n>; LOW|AVERAGE|HIGH)" (c1.java:2745-2780). This exposes device model and a performance class to every mini app.

## 10. Emulator detection result sent to server
- EmuDetector compares IMEI (getDeviceId), IMSI (getSubscriberId), and line1 number against known emulator values (only if READ_PHONE_STATE is granted), plus emulator files/props/packages. Only a boolean leaves the device: initConnection flag 1024 (ConnectionsManager.java:678-687). Identifiers are not sent.

## Good practice / checked and cleared
- Firebase Analytics: firebase_analytics_collection_deactivated=true, google_analytics_adid_collection_enabled=false, and AppMeasurementService/Receiver declared android:enabled="false". No FirebaseAnalytics calls in org/telegram. AppCenter hooks are empty stubs (ApplicationLoader.java:658-668). No ad-ID use and no attribution SDK.
- READ_CALL_LOG: AndroidUtilities.obtainLoginPhoneCall (AndroidUtilities.java:4006-4030) reads number+date of incoming/missed/rejected calls. It returns only a number from the last hour that matches the server's flash-call pattern.
- READ_PHONE_NUMBERS: SIM numbers (getLine1Number + SubscriptionInfo.getNumber, oh0.java:268-298) are compared locally to the entered number. Only the boolean codeSettings.current_number is sent (nh0.java:666-678).
- Location: People Nearby / contacts.getLocated is gone (only a leftover NotificationCenter id). ACCESS_BACKGROUND_LOCATION is requested only for live-location sharing, with an honest pre-prompt ("We won't use your location for any purpose other than sharing it in this chat"), at most once per 24 h (zd0.java:3203-3215; Components/dm.java:945). The story weather widget uses an inline bot only when the user adds it.
- In-app browser JS (res/raw/webview_ext.js, webview_app_ext.js, webview_share.js, instant.js): swipe-gesture handling, theme-color/site-name reading, a navigator.share polyfill, and a local Readability "instant view". No tracking or exfiltration.
- Secret chats set IME_FLAG_NO_PERSONALIZED_LEARNING (ChatActivityEnterView.java:6587-6589).
- Login uses Play Integrity / reCAPTCHA (CaptchaController) only when the server asks. The reCAPTCHA SDK itself reads the GSF android_id (Google anti-abuse).
- Installed-app visibility: <queries> limited to Google Maps, a cast module, ton: scheme and billing. No QUERY_ALL_PACKAGES.
- ML Kit (image labeling, subject segmentation, language ID) runs on-device for the sticker maker (classes3/sources/hf/h3.java:2850-2890) and translation detection. ML Kit's datatransport/clearcut may send SDK usage logs to Google (not verified).
- REQUEST_INSTALL_PACKAGES: opening an .apk from a chat goes through the system installer and the "unknown sources" toggle (AndroidUtilities.java:4134-4140; "APK installation is restricted for this app…").
- Encryption copy for Secret Chats is accurate ("Use end-to-end encryption", key-visualisation). Cloud chats are not E2E by default. The only borderline marketing copy found is "heavily encrypted cloud servers" (contacts dialog).

## Limitations
- Defaults that live on the server could not be confirmed client-side: phone-number/last-seen privacy, account TTL default, ad frequency, availability of stake dice/age check/wallet.
- Mini-app age-check page code is not in the APK. Native wallet engine not reversed.
- A few JADX methods "decompiled incorrectly" (ContactsController.createOrUpdateConnectionServiceContact, parts of VideoAds).
