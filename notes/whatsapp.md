# WhatsApp 2.26.39.79 (com.whatsapp) — working notes (paths under work/whatsapp/jdex; 12 DEX trees, heavily obfuscated)

Method: string resources are all renamed (APKTOOL_DUMMYVAL_0x7f12xxxx); code references them by decimal id. Server "AB props" defaults were extracted from the client defaults table classes/sources/X/C014907h.java (builder.put(id, default)). These are the shipped client defaults; the server overrides them at runtime. Most monetisation and data features below are behind these flags. No Exodus tracker signatures were found (work/trackers_batch2.txt: 0). The manifest sets firebase_analytics_collection_deactivated=true.

## 1. Status/Channels ads ("WAMO"): what the ad request carries
- classes9/sources/com/whatsapp/wamo/request/WamoRequestManager.java:2412-2660 builds the Status ads fetch (POST https://www.whatsapp.com/api/wamo/status or /status/linked/). It sends:
  - access_token, user_id, app_id 1015890928915437, app_version, os_version, encrypted_yob, country, locale, abprops, family_device_id (always), specific_device, num_available_pogs/num_unseen_pogs, fetch_trigger_type.
  - Device and context signals: battery_level, is_charging, connection_type (wifi=1 / cellular=3), screen_width/height and mobile_app_build. Getters A0C/A0E/A0K (lines 2303-2358) gate these on AB prop 30327 (AbstractC2421GuH.A03, MobileConfig-backed, default false).
  - device_brand, device_manufacturer and device_model: the decompiled condition reads `!A0N()`, so they are sent when 30327 is off.
  - push_name (the user's WhatsApp profile name) only when HPH.A01() is true, i.e. the Accounts Center link state is ACTIVE (classes9/sources/X/HPH.java; X/C18M.java enum INITIALIZED/ACTIVE/PAUSED/UNLINKED).
- Lines 224-250 (WamoStartViewerSessionV2Mutation) send country, num_consumed_media_recent and updates_tab_session_id. The /newsletters (Channels ads) request at lines 856-940 has the same device-signal block.
- WamoRequestManager$createUser$2.java (WamoCreateUserMutation) sends encrypted_yob, country, locale, os_version, promo_user_id and accepted_notices_json.
- Other GraphQL operations: WamoLinkUserMutation (links the ad user to the Meta account), WamoHeartbeatMutation, WamoDYIJob* (ads data download), WamoDeleteUserMutation, WamoAdvertisersYouSawQuery.
- Ad pacing fields seen: "num_consumed_media_since_last_wamo_impression_in_last_7_days", dynamic_highest_position_rules, status_post_index.
- Targeting copy: 0x7f124fee "…wants to show ads to people who may have a general location in %2$s"; 0x7f124fef "…who may have %2$s (%3$s) as their country code".
- In-house cross-promo cohort: classes9/sources/com/whatsapp/wamo/status/WamoStatusFetcherImpl.java:1130-1147 adds "wamo_status_in_house_ad_cohort" to the ad fetch.
  - "ig_ad_cohort" is set when Instagram (or IG Lite) is installed (X/C41515hW case 35) but not linked in Accounts Center.
  - "fb_ad_cohort" is the same test for Facebook (X/C0095Fhu: katana/lite/orca/stella).
  - Gated by AB 35036 (default false). This reports installed-app state to the ad server.

## 2. EU pay-or-consent ("AFS" = ad-free subscription) and LPA auto-clear
- Strings:
  - 0x7f124f5d "Free of charge with ads" / 0x7f124f5e "No ads (%1$s/month)"
  - 0x7f124f5a "Choose to see personalized or less-personalized ads"
  - 0x7f1202b6/b7 "All set. You'll use Status & Channels free of charge with (less-)personalized ads."
- Price is tied to Accounts Center linking. 0x7f1202ae: "Since you recently removed your WhatsApp account from your Accounts Center, the price of your subscription for no ads in Status & Channels has decreased." (0x7f1202af is the Meta Account variant.)
- Nudge banner 0x7f124fed: "Discover more with relevant ads only in Status & Channels. See details and updated terms".
- Code: classes9/sources/com/whatsapp/wamo/eu/*, WamoGatingManager (separate EU and UK eligibility, youth states).
- LPA auto-clear:
  - classes9/sources/com/whatsapp/wamo/lpaautoclear/WamoLpaAutoClearDailyCron.java plus X/IHF.java:1008-1050. A daily cron runs WamoAutoClearLpaConsentMutation (string "wamo_auto_clear_lpa_consent") to clear a "less personalized ads" consent.
  - It runs when AB 31497 is on (default false), the Accounts Center state is INITIALIZED/UNLINKED and the AFS cache is in a certain state.
  - Exact server semantics are not visible client-side.
- Good practice in this area: per-advertiser hide, "Why you're seeing this ad", ads DYI report ("My Ads report"), and copy that personal messages, calls and statuses are not used for ads (0x7f124fcf).

## 3. Exported "QuickSends" provider: ranks your most frequent chats for Facebook/Instagram
- classes/sources/com/whatsapp/accountlinking/ipc/handler/quicksends/QuickSendsContactsProvider.java (manifest: exported, guarded by Meta signature permission com.whatsapp.android.fbpermission.WFL_OPERATIONS).
- Columns returned: {obfuscated_chat_id, display_name, profile_photo_uri, photo_key} (line 89).
- Ranking: top max_contacts (default 10) most-frequent chats, with a fallback ranking (lines 174-240). Chat ids are AES-GCM encrypted. Profile photos are AES-encrypted into cache/quick_sends_photos and served through openFile.
- Callers allowed by X/AbstractC1945GmV: com.instagram.android, com.facebook.katana/wakizashi, com.facebook.lite, com.facebook.stella (Meta AI/glasses).
- Preconditions: AB 26593 (default false), Accounts Center link == ACTIVE, and a server-validated nonce (AccountLinkingGraphqlNonceValidator).
- Paired IPC operations (classes10/.../accountlinking/ipc/api/models): QuickSendsMessageOperation (FB/IG send into WhatsApp chats), ExecuteCrosspostOperation, GetNotificationCountOperation, GetRegisteredPhoneNumberOperation (returns phoneNumber), GetEncryptedProfileInfoOperation. The exported service is com.whatsapp.accountlinking.ipc.service.WaAccountsCenterService (action com.whatsapp.wfl.OPERATION). The binder verifies trusted Meta callers (WaAccountsCenterServiceBinder A01, AB 20729/20726 per app).

## 4. Accounts Center link "silent unpause" triggered by FB/IG
- classes9/sources/X/C4134Hje.java (TriggerSilentUnpauseOperationHandler): when Facebook/Instagram calls the IPC service and the WhatsApp↔Accounts Center link is PAUSED, WhatsApp fetches unpause info and runs the unpause flow with no UI.
  - Log/analytics names: "foa_triggered_unpause", "silent_auto_unpause", "silent_auto_unpause_from_cron", "silent_auto_unpause_npr".
  - Gate: AB 27213 (default false).
- Related: com/whatsapp/waffle/accountlinking/unpause/BackgroundWaffleUnpauseCoordinator.java, UnpauseFlow.java. MexUnpauseWithoutFoaNonceApi.java:263-267 sends SHA-256(Android ID) (base64) as "android_id" with an RSA-encrypted metadata blob (GetUnpauseWithoutFoaNonce).
- FamilyAppsCredentialsProvider / FamilyAppsUserValuesProvider (exported, fbpermission ACCESS_LIBRARY_PROVIDER_ACCESS) hand Meta apps a time-limited "foa_nta_ipc_bundle" credential and "foa_wo_wa_link_eligibility_values".

## 5. Meta cross-app device ID (family_device_id / "phone ID")
- classes7/sources/com/whatsapp/phoneid/PhoneIdRequestReceiver.java: exported receiver for com.facebook.GET_PHONE_ID that returns WhatsApp's phone ID + timestamp.
- X/C0016Anq.java broadcasts GET_PHONE_ID to Meta-signed packages (X/CT2.java enumerates getInstalledPackages and keeps only Meta-signed ones) so the ID is synced across the family.
- The ID is sent in:
  - registration requests: KotlinRegistrationBridge.java:933-937 "fdid", plus "lc" and "expid"
  - pre-registration funnel logs (PrePnBaseFunnelLogger "fdid")
  - every Status ads fetch ("family_device_id", section 1)

## 6. Contact (address-book) sync
- classes/sources/X/C21520xT.java:430-445 builds the usync IQ (xmlns "usync", mode/context/sid/index/last). Each phonebook number becomes <contact>RAW_NUMBER</contact> in clear text; it is not hashed. No contact names are added to the node (names stay local).
- Full sync interval: "contact_full_sync_wait" defaults to 86400000 ms (24 h) (X/AXR.java:525-543). The server can rewrite it and set backoffs via the sync response (X/C21280x2.java:1478 "contact_full_sync_wait", "contact_sync_backoff").
- Delta syncs on phonebook change; separate sidelist/status/picture/business/lid/username protocols. Log tags: ContactSyncHelper/syncAll, syncDelta, syncFullNonContact (non-WhatsApp-user numbers are synced too, which is how "X joined WhatsApp" works).
- Permission copy bundles contacts with unrelated actions:
  - 0x7f123441 "To verify your number and easily send messages to friends and family, allow WhatsApp to access your contacts."
  - 0x7f121ca7 "To find and restore your backup from Google storage, allow WhatsApp to access your contacts." (technically GET_ACCOUNTS is in the contacts permission group)
  - None of the pre-prompts says every phonebook number is uploaded. Registration copy 0x7f121865 does say that others "may have uploaded your number".
- Instagram contact bridging: 0x7f1210a9 "Since you added WhatsApp to your Meta Account, you can connect with Instagram friends and be added to each other's WhatsApp contacts." This is a request/confirm flow (0x7f1210b4 "Your contact details aren't shared until you confirm"), with an off switch in Privacy.

## 7. Engagement notifications ("inorganic notifications")
- Types (X/CSP.java, X/CPT.java, X/CXJ.java):
  - message_reminder_push_notification (reply reminders)
  - missed_call_reminder_push_notification ("%1$s tried to reach you recently.")
  - recently_joined_contact_push_notification ("Your contact %1$s joined WhatsApp.")
  - status_posted_push_notification ("Added a status")
  - channels_trending_push_notification (server PSA push "com.whatsapp.psa.qp_surface")
- Recommended-Channels pushes default ON: SettingsNotifications.java:609 getBoolean("recommended_channels_setting", true). The opt-out is offered only after the fact via another push (X/CXJ.java:107; 0x7f122d02 "Getting too many notifications?" / 0x7f122d01).
- Status upsell push: X/D3F.java:180-232 posts "Added a status" notifications when one of your top-5 "frequents" (AB 34847=5) posts a status, capped by AB 35346 (default 4) and logged in status_upsell_notification_timestamps. Mute copy: 0x7f1228b2 "Mute reminders about messages or statuses you haven't seen."
- Notification permission re-prompt: HomeActivity.java:1763-1777. A bottom sheet is shown up to 3 times (notification_nag_count_key < 3), at least 21 days apart, starting 1 day after registration. AB 2581, default true. This is bounded.
- Status creation prompts: "Your day in one photo", "Last photo you took?", "Current mood?" (0x7f1242e4-e6).

## 8. Meta AI placement
- Entry points: chat-list FAB, AI tab, search, forward, contacts tab (X/EnumC03681lz CHAT_LIST_FAB, AI_TAB, SEARCH…); MetaAiAppWidgetProvider; @Meta AI in groups and calls; "Meta AI announcements" pushes (toggle 0x7f1208ea).
- FAB toggle: the button is on by default (X/C1OG.java:11 getBoolean("bonsai_meta_ai_button_setting_enabled", true)). SettingsChat.java:466-472 inflates the "Show Meta AI button" switch only when that pref is already false (`if (!zA1S && …)`). The only writer found is the switch itself (X/ViewOnClickListenerC3335Caf case 20), so a user with the button on gets no settings path to turn it off. Caveat: based on decompiled code; possibly reachable via a gesture or server path not found.
- Data copy:
  - 0x7f1203e6 "…Meta shares information with select partners so Meta AI can offer relevant responses…By using Meta AI, you agree to Meta's AI terms."
  - 0x7f12034c "Messages sent to Meta AI may be used to improve AI at Meta."
  - 0x7f1226d0 Memory: "Meta may use these details to improve AI at Meta."
  - 0x7f12038a "Meta AI can use information from your profiles connected in Account Center."
- Monetisation: 0x7f1203cf "Upgrade to Meta One %1$s to create AI images now or wait until %2$s." Meta One / Meta Verified also raise the new-chat limit (0x7f120c64).
- Good: Private Processing (TEE) for summaries/writing help (0x7f12379b); Advanced chat privacy lets a chat block Meta AI.

## 9. In-app browser (IAB) injected JavaScript (ads / business CTA links)
- res/raw has 15 iabjs scripts: autofill_form_detection, autofill_payment_detection, autofill_form_fill, autofill_language_detect, detect_login_forms (16 KB), navigation_performance_logger_android (22 KB), navigation_timing_logger_new, contentful_paint_logger, web_vital_reporter, otp_autofill, theme_color, bridge init/proxy/idle.
- None of Instagram's data-layer/pixel interceptors are present.
- iabjs_autofill_payment_detection classifies card fields by regex (cc-number, cc-csc, cc-exp…). On form submit it sends the typed values ({autocomplete, value}) to native "formSubmitted".
  - Injected for all origins ("*"): X/IeK.java:471-497.
  - Native X/C3253NHk.java:114-155 (maybeOfferToSaveEntry) keeps them in memory to offer saving them to Meta autofill (Accounts Center).
- Autofill copy: 0x7f120581 "Your autofill activity is used to improve ads and other parts of your WhatsApp experience." The payment variant says payment info is not used.
- detect_login_forms reports login field focus/submit events (no values). Opened from Status ads, CTWA and business CTA buttons (X/C2888EpU "ClickToActionButtonUtils", WaInAppBrowsingActivity).

## 10. Business-messaging analytics
- wam_business_template_message_read_stats (X/C1267OwL.java, logged from X/RunnableC3906Qeo.java:892-922) is logged per read business template/marketing message.
  - Fields: business_phone_number, business_lid, message_read_ts, message_delivered_ts, read_source, thread_dwell_time, is_muted, read_receipts_enabled, last_outgoing_ts, is_from_ads_manager_mm, per-thread message counts.
  - The read-receipts setting is recorded, not used as a gate.
- CTWA first-party conversion: X/C0954GJj.java:100-180 → wam_ctwa_1pd_conversion / wam_wamo_ctwa_1pd_conversion (X/GL8, X/C1035GMo).
  - For chats started from a Facebook/Instagram ad it logs conversation depth, repeat, direction_from, message_type (text/webPage/buttonsText), has_username, ctwa_signals and promo_user_identifier.
  - Gated by AB 7136 (default false). Also present: ctwa_ads_private_stats_conversion_info (anonymous-credential path).
- Disclosures exist: 0x7f121590 "…WhatsApp's parent company Meta receives limited info. This helps improve Meta ads…"; 0x7f1227ee ">> icon means Meta is receiving info".

## 11. Installed Meta-app census
- X/C4763Hu0.java:60-100 (RegistrationDailyCron.onRandomizedDailyCronNoMessageStore) logs wam_installed_foa_app_daily daily, with foa_app_source = category of which of com.facebook.katana/wakizashi, com.instagram.android, com.facebook.orca, com.facebook.lite, com.facebook.services are installed.

## 12. Invites (SMS)
- InviteContactUtils.java:322-380 "sendBackgroundSmsInvite" sends invite SMS directly through SmsManager from the user's SIM (needs SEND_SMS, user-initiated).
- Server-sent SMS invites: SMSPreviewServerInviteBottomSheetFragment.java:140-150, 0x7f122bf4 "%1$s was added to your contacts but isn't on WhatsApp. We'll send a one-time SMS invite for you." The non-user's number goes to WhatsApp, which texts them.
- Invite copy: "the world's most popular messaging app", "This invite expires soon".

## 13. Accounts Center linking nudges
- Username squatting pressure: 0x7f124af3 "This username matches an account on Facebook. To use it before someone else does, add your accounts to Accounts Center."
- Age check: 0x7f120abd "Confirm your age by adding your WhatsApp account to Accounts Center."
- Upsell surfaces: WHATSAPP_WAFFLE_CONTEXTUAL_UPSELL, status_creation_linking_upsell_*, status_viewer_sheet_linking_upsell_*, POST_LINKING_UPSELL.

## Lower / misc
- Registration ad ID: KotlinRegistrationBridge "advertising_id" via X/H6Q.java.
  - Gated by AB 20346 (default false).
  - Skipped when the TOS region is "eu" (line 28).
  - Skipped when Limit Ad Tracking is on (C2830H4w.A01 → null).
- India UPI (NPCI common library, X/C93.java via X/NHs/X/C5022Nx2) can collect a full device dossier (androidID, advertisingId, IMEI/subscriberId, SIM serial, wifi MAC/BSSID/SSID, bonded Bluetooth devices, lat/long…). Only when the bank's credential request sets "getDeviceDetails". Third-party payments-only code.
- Registration prefills the profile name from the device "Me" profile or the Google account name (X/IHD.java ~880-960, READ_PROFILE/GET_ACCOUNTS).
- Account deletion: survey "We hate to see you leave…" plus "Other options" interstitial (log out, change number, free up storage), then phone-number confirmation. Mild friction, not obstruction. Deleting cancels Meta Verified/channel subscriptions.
- Backup nags use loss framing (0x7f1205ce "Turn on cloud backups so you can restore your chats if you lose your device."). E2E-encrypted backup is opt-in.
- Business "Offers and announcements": per-business Stop/Resume (good). Sign-up copy 0x7f1220b4 bundles marketing consent into lead-form sign-up.
- Message/broadcast caps ("new chat limit", "Send up to %1$d broadcasts per month") are raised by paid Meta One/Meta Verified.

## Good practice / checked and cleared
- No third-party ad/analytics SDKs (0 Exodus signatures); Firebase Analytics deactivated in the manifest; own WAM/Falco analytics only.
- Link previews are generated on the sender's device (X/C35077np.java fetches og: tags with UA "WhatsApp/2.23.20.0").
- No ACCESS_BACKGROUND_LOCATION; live location uses a foreground service.
- Wi-Fi: X/H5R.java collects RSSI, frequency, standard, link speeds, BSS-load/vendor IEs for call quality, not the BSSID itself.
- No QUERY_ALL_PACKAGES. getInstalledPackages is used only to find Meta-signed apps (phone ID) and the Play Store (X/C2843Jyy). <queries> lists Meta apps, Indian UPI apps, Google Maps/TTS/AICore, Garmin, Microsoft Link to Windows.
- Clipboard read only on explicit paste (DialerActivity context menu, PhoneNumberEntry, MentionableEntry).
- UsageStatsManager: queryEventsForSelf only (own standby bucket).
- Local "frequent contacts" (times_contacted DESC LIMIT 100, starred=1) in X/C09578wK.java is used only for the on-device empty-chat-list suggestions.
- Pixel "Besties" provider (Google permission com.google.permission.besties.API) is consent-gated (get_consent/set_consent) and limited to favourites.
- Ads: "Your personal messages, calls and statuses are end-to-end encrypted and can't be used to show you ads."; per-advertiser hide and report; ads data download.
- Meta AI features that read chats use Private Processing (TEE). Advanced chat privacy blocks AI in a chat.
- Android ID sent in the Accounts Center unpause flow is SHA-256-hashed.

## Limitations
- Obfuscated names; some JADX regions failed ("Code decompiled incorrectly"), notably boolean conditions in WamoRequestManager and SettingsChat.
- AB-prop defaults are only client defaults; real values are server-delivered and unknown.
- Server semantics of WamoAutoClearLpaConsentMutation and of the pay-or-consent screens (Bloks, server-rendered) are not visible.
- WAM sampling rates were not resolved.
