# Facebook 582.0.0.50.54 (com.facebook.katana): working notes (paths under work/facebook)

**Method and big caveat.** Almost all Java code (assets/secondary-program-dex-jars/store-0.dex.spo), the React Native bundle (Fb4aBundle.js.hbc.spo), most native libs (assets/lib/libs.spo, 102 libs per lib/metadata.txt) and the default English string table (assets/strings/default.frsc.spo) ship Superpack-compressed. We could not unpack them, so **no main-app code was decompiled**. Evidence comes from:
- the manifest (apktool/AndroidManifest.xml; audit work/manifests/facebook.manifest.json),
- res/values/strings.xml (807 strings, all renamed APKTOOL_DUMMYVAL_0x7f14xxxx),
- the small loader dex (loader/sources),
- assets (assets/assets/*),
- MobileConfig parameter names.

From params_map_kMobileConfigAdminId.txt, params_names_v4_*.txt, rn_params*.txt and ReactMobileConfigMetadata.json, we rebuilt **32,861 named `config:param` flags in 3,849 configs**. Only the 5,196 React Native params carry shipped defaults; for native params the default is unknown.

Confidence labels:
- **[C]** = confirmed by manifest, asset, string or loader code.
- **[F]** = indicated by flag names only: a capability or experiment exists, but use and defaults are unknown.

## 1. In-app browser (IAB): page instrumentation, and autofill activity used for ads
- [C] Autofill-for-ads disclosure strings:
  - 0x7f140175: "Yes, Facebook uses your autofill activity to improve ads and other parts of your Facebook experience. Some of your autofill activity is collected by Facebook and some of it is provided by the businesses that own the websites where you use autofill. This activity includes:"
  - 0x7f140176-179 list "The website address where you use autofill", "The time you use autofill", "The fields you fill in using autofill", "If you use autofill and submit a form".
  - Also 0x7f140049 "Your autofill activity is used to improve ads…", 0x7f140190 "some of your autofill activity is used to improve ads", 0x7f14018b (Instagram variant).
  - Payment numbers are excluded (0x7f14017c). CVV is device-only and encrypted (0x7f14004c).
- [C] 0x7f140071 "See the web pages you've visited through Facebook." (IAB link history). 0x7f1400f3 says clearing IAB cookies "will log you out of most websites. Keeping your cookies and cache can give you better browsing experience" (it nudges the user to keep them).
- [C] assets/business_integrity_cloaking.json: an on-device SQL pipeline (event `bi_new_cloaking_text_event(uuid,text)`) regex-extracts the `<title>` and the `<body>` text (scripts, styles, img, iframe and video stripped) from page HTML into `bi_cloaking_text_title_dataset` / `bi_cloaking_text_body_dataset`, kept for 86400 s. It is used for ad-landing-page cloaking detection. This confirms that IAB page HTML is captured and processed, though it is integrity-motivated.
- [F] Config `fb_iab_browser_agent`, 64 params:
  - Pixel and tag interceptors: `datalayer_interceptor_enabled`, `ga_interceptor_enabled`, `sp_interceptor_enabled`, `ttk_interceptor_enabled`.
  - Session replay and page logging: `inner_frame_session_replay_enabled`, `inner_frame_visible_elements_logging_enabled`, `inner_frame_data_offline_logging_enabled`, `inner_frame_ota_enabled`, `enable_logging_per_page_dwell_time_fb4a`, `enable_active_dwell_time`.
  - Shopping and catalog: `catalog_structured_data_extraction_enabled`, `fb_iab_atc_online_signals_enabled`, `shopify_cart_observation_api_enabled`, `qr_code_screenshot_enabled`.
  - Agent features that hide the site's own chat and email capture: `ai_agent_web_chat_suppression_js_enabled` / `_v2_js_enabled` / `_ota_js_enabled`, `ai_agent_email_suppression_config_enabled`, `ai_agent_declutter_js_enabled`.
  - The same names as Instagram's iabjs scripts (notes/instagram.md).
- [F] `fb4a_iab_telemetry`: `ga4_analytics_config`, `gtm_analytics_config`, `sn_analytics_config`, `ttk_analytics_config`, `enable_subresource_logging`.
- [F] `android_iab_unified_checkout_modeling`: `checkout_path_keywords_regex`, `apm_cookie_regex`, `domain_to_apm`, `enable_analytics_tool_detection`, `enable_passkey_detection`, `enable_structured_data_coverage_logging`.
- [F] `facebook_android_autofill_experimentation` (49 params): `is_payment_js_enabled`, `mutation_observer_enabled`, `enable_form_detection_logging`, `autoprompt_dwell_threshold_ms`, `is_high_intent_user`, `log_to_fromage`, `remove_pux_lightweight_disclosure`, `remove_meta_pay_branding`, `enable_one_click_leadgen`. `fb_iab_promo_extension_android_config:first_party_email_substitution_autofill_claim_enabled`. `lead_gen_form_ui_experiment:eligible_for_iab_prefill_android`. `fb_story_ads_vertical_tile_exploration:enable_iab_screenshot_fb4a`.
- [F] `fb_iab_info_hub:enable_on_device_html_extraction`, `enable_ai_summaries_js`, `inject_info_hub_js`. `iab_modal_detection:inject_js_client_side`. `android_ui_browser_lite_admin_id:use_pixel_handler_listener_extension`, `use_ebc_as_data_control`, `should_show_enhanced_browsing_eu_content` ("enhanced browsing" setting).
- Engine: Helium (Meta's Chromium fork) ships as downloadable Voltron modules heliumcore/heliumiab/heliumiabexp (assets/app_modules/contents/heliumiab.json → d.libhelium.so). The IAB JS is not in the APK: the 15 plain native libs contain no JS (checked with `strings`), so it lives in the superpacked dex or OTA downloads.

## 2. Notification engagement: "stealth" badge notifications, replay after reboot, rerouting Messenger pushes
- [C] Manifest receiver `com.facebook.notifications.badging.stealthnotification.controller.StealthNotificationDeleteBroadcastReceiver` (action `…stealthnotification.ACTION_DELETED`). There are launcher-badge permissions for Samsung, Sony, HTC and Motorola, plus meta-data `miui.badge.decoupling`.
- [F] Config `fb4a_notifications_stealth` (24 params): `enable_stealth_notification`, `should_send_to_non_dau_only`, `periodic_scheduler_interval_h`, `cooldown_period_in_hours`, `stealth_notification_delay_s`, `custom_title_text`, `custom_body_text`, `bypass_jewel_badge_count_check`, `exclude_xiaomi_native_badge_devices`, `exclude_day1_oem_native_badge_devices`, `enable_local_whisper_in_unagi_flow`, `dismiss_whisper_on_notif_tab_visit`.
  - This reads as a locally scheduled, low-visibility notification whose job is to put an unread badge on the launcher icon for users who are not daily-active.
  - Devices whose launcher shows native badges are excluded, which suggests the notification exists only to produce the badge.
- [C] Receiver `com.facebook.notifications.recovery.replay.NotifRecoveryReceiver` listens for BOOT_COMPLETED, MY_PACKAGE_REPLACED and `…DELAYED_REPLAY`.
- [F] `fb4a_notifications_recovery:should_replay_on_reboot`, `should_replay_on_upgrade`, `should_refresh_app_badge_on_replay`, `skip_replay_when_tray_not_empty`, `recoverable_types_csv`. Notifications cleared by a reboot or update are re-posted.
- [F] `fb4a_push_notif_rerouting:route_to_fb_when_msgr_unpushable_30d`, `enable_reroute_notification`, `enable_silent_rerouted_push`, `bypass_msgr_pushability_check`, `enable_bff_check`, `cooldown_hours`. Messages are delivered through the Facebook app when Messenger has not been pushable for 30 days, which may override a user's choice to silence Messenger.
- [F] `fb4a_smart_in_app_notification:close_friend_silent_push_msgr_enabled`, `silence_msgr_push_for_fbm_smart_in_app_notif`.
- [F] Permission and upsell prompts:
  - `fb4a_videox_radl:enable_notification_permission_on_reels_tab` plus `notification_permission_cooldown_hours_on_reels_tab`.
  - `fbm_android_notification_upsell:enable_growing_cooldown`, `dismiss_limit`, `cta_click_limit`, `only_upsell_with_unread_threads`.
  - `biz4a_pushability_defense_2024:enable_direct_notification_permission_prompting`.
- [F] Badging and streaks:
  - `dynamic_badging_explorations:enable_immediate_feed_badge_when_off_feed`, `fb4a_feed_badging:*`.
  - `chat_head_promo:enable_red_fb_entry_point_badge`.
  - `fb4a_group_home:render_group_streak` / `fetch_group_streaks_gql`.
- [F] On-device message classifiers that drive reply reminders, including on E2EE chats:
  - `odin_m4a_unread_reply_reminder:enable_heuristic_evaluation_on_e2ee_reply_reminder`, `model_confidence_threshold`, `word_deny_list`.
  - `odin_m4a_read_reply_reminder` (24 params).

## 3. Login request harvests device and SIM identifiers before sign-in
- [C] Bundled Bloks login screen assets/com.bloks.www.caa.login.aymh.screen_query_bundled_payload.json (same content as b99d1d6b…_bundled_payload.json). The `send_login_request` parameter map is:
  - Device and family IDs: `device_id`, `family_device_id`, `machine_id`, `cloud_trust_token`, `block_store_machine_id`, `fb_ig_device_id`, `secure_family_device_id`, `auth_secure_device_id`.
  - Credentials and accounts: `contact_point`, `password` (EncryptPassword), `accounts_list`, `openid_tokens`.
  - SIM and phone: `sim_serials` (GetSimSerialsV1), `sim_phones` (GetSimPhones), `encrypted_msisdn`, `flash_call_permission_status`, `has_granted_read_phone_permissions`.
  - Device accounts and contacts: `device_emails`, `has_granted_read_contacts_permissions`.
  - Other apps and preloads: `has_whatsapp_installed`, `sso_token_map_json_string`, `app_manager_id`.
  - Login state: `aymh_accounts`, `lois_settings`.
- [C] The pre-login home screen also prefetches `device_emails` via `bk.action.caa.login.GetDeviceEmails "TARGET_SIGN_IN"` (GET_ACCOUNTS is declared) and `device_phone_number` via `GetDevicePhoneNumber "TARGET_LOGIN"` (READ_PHONE_NUMBERS is declared, see §9).
- [C] Registration state carries `whatsapp_installed_on_client`, `is_too_young`, `safetynet_token`, `email_oauth_token_no_contact_perm`.
- SIM serial reads are blocked by Android 10+ for normal apps. The rest works when permissions are granted.

## 4. Cross-app identity and data plumbing with other Meta apps
- [C] `com.facebook.fdidlite.FDIDLiteProvider` (authority `com.facebook.katana.provider.phoneid`, exported, process `:fdidsync`) and `FDIDSyncLiteReceiver` (action `com.facebook.GET_PHONE_ID`, exported, no permission).
  - They return `phone_id` (the family device id), its timestamp and origin from `app_dir/light_prefs/<pkg>/default_phone_id` (loader/sources/X/AbstractC18760xC.java).
  - The caller check (loader/sources/X/AbstractC18740x8.java) allows Meta-signed apps **plus `com.facebook.study` and `com.facebook.viewpoints`**, Meta's paid research and panel apps. The family device id is therefore shared with market-research apps.
- [C] `libraries.accessv2.src.provider.AccessLibraryContentProvider` (exported, "Family" policy) returns the AccountManager SSO data (`active_account`, `inactive_logged_in_accounts`, `saved_accounts`, `sso_settings_v2`) for FACEBOOK, INSTAGRAM, MESSENGER, THREADS, OCULUS, VIBES, MWA, FBLITE and IGLITE (loader/sources/libraries/accessv2/src/provider/AccessLibraryContentProvider.java, X/C0UL.java).
- [C] Exported providers without a manifest permission (enabled at runtime; the implementation `$Impl` classes are in the superpacked dex, so caller checks cannot be verified): `AttributionIdProvider`, `FirstPartyUserValuesProvider`, `UsdidValuesProvider`, `FirstPartyUserValuesLiteProvider`, `InstallReferrerProvider`, `LastUsedTimestampProvider`, `SecureMessagingKeyContentProvider` (ShareKey), `DeferredDeeplinkProvider`. `AttributionIdProvider` is the provider that the public Facebook SDK in third-party apps queries for the attribution id (`aid`).
- [C] The manifest declares Meta fbpermissions toward WhatsApp:
  - `com.whatsapp.android.fbpermission.WFL_OPERATIONS`, which guards WhatsApp's QuickSends provider exposing the top-10 chats (notes/whatsapp.md §3).
  - `com.whatsapp.fbpermission.ACCESS_LIBRARY_PROVIDER_ACCESS`.
  - assets/fbpermissions.json pins their signatures. Toward com.facebook.services: `FEO2`, `FEO2_READ_DEVICE_COOKIE`, `FEO2_READ_SIM_KEY`, `STORAGE`.
- [C] Exported, runtime-enabled receivers for other Meta apps' foreground signals:
  - `NotificationsClientSignalFamilyStaticBroadcastReceiver` (`com.instagram.stateupdate.SYS_ENTER`).
  - `NotificationsM4aClientSignalStaticBroadcastReceiver` (`com.facebook.messaging.stateupdate.SYS_ENTER/SYS_EXIT`).
  - `NotificationsPreloadsFbnsClientSignalStaticBroadcastReceiver` (`com.facebook.oxygen.services.fbns.SYS_ENTER`, from preinstalled Meta services).
  - The same mechanism as Instagram's device-state snapshot. [F] `odin_m4a_device_features_collection:enabled`, `app_foreground_source_enabled`, `notification_trigger_enabled`, `background_refresh_interval_seconds`.
- [C] Other cross-app components:
  - Receivers `com.facebook.device_id.UniqueIdSupplier` (`GET_UNIQUE_ID`, signature permission), `IdentityHashReceiver` (`com.whatsapp.otp.ID_HASH_REQUESTED`), `CrossSigningBroadcastReceiver`/`CrossSigningService` (`com.facebook.usdid.CROSS_SIGN`).
  - Services `MfaCrossAppServiceImpl`, `TrustedDeviceFoundationServiceImpl`, `com.fbpay.w3c.ipc.AutofillKeyFetchServiceImpl` (`GET_DEVICE_KEY`; cross-app payment autofill key, fbpermission GET_CROSS_APP_KEY granted to katana and Instagram).

## 5. Installed-app detection
- [C] Manifest <queries> lists the **same 23 AI and automation apps as Instagram's `odin_ai_apps_detector`**: tech.butterfly.app (Manus), com.replit.app, com.arco.youware, com.emergentagent.app, dev.a0.android.app, NotebookLM (…labs.language.tailwind), com.openai.chatgpt, …apps.bard, com.microsoft.copilot, ai.perplexity.app.android, com.anthropic.claude, ai.replika.app, ai.character.app, com.quora.poe, com.inflection.pi, Tasker, IFTTT, Zapier, MacroDroid, Automate, Home Assistant, notion.id, com.formagrid.airtable.
  - Also listed: com.google.android.aicore, com.twitter.android, org.telegram.messenger, Spotify (4 variants), com.LogiaGroup.LogiaDeck, WhatsApp/W4B, Meta apps and Oxygen (appmanager/system/services).
  - The detector code cannot be seen. The identical list strongly suggests the shared Meta detector is present.
- [C] A `<queries><intent><action MAIN/></intent>` element with no category, plus VIEW `scheme="*"`, makes practically every launchable app visible without QUERY_ALL_PACKAGES. There is also a `com.facebook.secure.packagefinder.intent.ACTION_QUERY_PACKAGES` query.
- [F] `fb_android_derived_on_device_app_history:is_derived_app_history_enabled`, `derived_job_interval_hours`, `installed_ad_id_mutation_batch_size`, `should_enable_ads_free_subscription_check`, `should_enable_dialtone_check`. This looks like a periodic job that uploads which advertised apps are installed, skipped for ad-free subscribers.
- [F] `android_signal_platform_ads:shopee_package_names`, `shopee_log_when_not_installed`, `enable_has_ig_installed`, `enable_temu_low_value_signal`, `enable_flipkart_low_value_signal`.
- [C] Receiver `com.facebook.feed.platformads.AppInstallReceiver` on PACKAGE_ADDED (not exported). On Android 8+ manifest receivers no longer get this implicit broadcast, so it is likely a legacy or app-install-ad hook.

## 6. Ad-signal collection beyond ads
- [F] `fb4a_knots` ("high value signal" pipeline for ad delivery):
  - Clipboard, screenshots and pixels: `enable_pasteboard_logging`, `enable_screenshot_detector`, `enable_screenshot_signal`, `enable_pixel_processing`, `targeting_pixel_events`.
  - URLs: `enable_url_processing`, `url_hi_value_ad_keywords`.
  - IAB behaviour scores: `iab_autofill_*_confidence_score`, `iab_dwell_time_*`.
  - Delivery: `enable_ad_delivery_high_value_signal_listener`, `should_announce_to_external_listener`.
  - Pasteboard logging inside an ads-signal system is the most sensitive name here.
- [F] `android_signal_platform_ads`: `enable_battery_level_fix`, `enable_mf_network_bandwidth_estimate_kbps`, `enable_reels_session_scroll_speed`, `enable_reels_current_session_watch_time`, `enable_reels_time_since_app_foreground`, `enable_reels_is_setting_suitable_for_autoplay` (context signals attached to ad requests).
- [C]+[F] Android Privacy Sandbox participation:
  - Permissions ACCESS_ADSERVICES_AD_ID/ATTRIBUTION/CUSTOM_AUDIENCE/TOPICS.
  - `fb4a_privacy_sandbox_account_level:enable_privacy_sandbox_topics_for_fb4a`, `enable_attribution_reporting_api`, `should_register_click_source`/`view_source`, `pa_ad_tech_name`, `should_enable_odp_*` (On-Device Personalization training).
  - Plus Google AD_ID permission.
- [C] assets/ppa_config_asset.json: on-device "PPA" (privacy-preserving attribution) datasets `ppa_exposure_history_dataset(exposure_id, first_exposure_datestamp)`, kept for 2,764,800 s (32 days). This is a privacy-preserving design.

## 7. Preinstall (Oxygen/AppManager) channel
- [C] Permission `com.facebook.appmanager.UNPROTECTED_API_ACCESS`. Queries for com.facebook.appmanager/system/services. `PostInstallSsoReceiver` (`com.facebook.appmanager.POST_INSTALL_SSO`), `AppManagerSsoProvider`, `IsManagedAppReceiver`.
- [F] Installs of Meta apps through the preinstalled AppManager:
  - `fb_threads_in_feed_config:enable_app_manager_install`, `enable_preload_install`, `should_auto_open_threads_after_dismissed_preloads_install`.
  - `fos_ig_bookmark_app_install_preloads:enable_ig_install_preloads`, `xav_fb_switcher_app_install_preloads:should_enable`.
  - `android_fare_2025h2:oxygen_scheduled_installer_retry_job_if_failed`, `enable_preloads_oxygen_setting`.
- [C] FEO2 fbpermissions (`READ_DEVICE_COOKIE`, `READ_SIM_KEY`) toward com.facebook.services, plus FeO2InAppContentProvider: the app reads identifiers held by the preinstalled Meta service.

## 8. Contacts and social graph
- [C] READ_CONTACTS and WRITE_CONTACTS; string 0x7f140271 "Upload contacts".
- [F] Contact-upload pushes:
  - `fbm_in_app_android:enable_contact_upload_in_pymk`, `fb4a_directly_show_contact_upload`.
  - `fb4a_ci_in_feed_pymk:should_upsell_ci`, `card_position`.
  - `address_book_acquisition:disclosure_screen_design_variant`, `ci_pymk_design_variant` (A/B testing the upload-disclosure screen).
  - `android_search_serp:enable_native_people_empty_state_contact_importer`, `m4a_contact_import:enable_pymk_preload_on_contact_import`.
  - Whether upload is continuous cannot be seen.
- [C] assets/ContactOmnistoreSchema.fbs (synced contact store). Per contact it holds:
  - Ranking floats: `communicationRank`, `withTaggingRank`, `phatRank`, `messenger_invite_priority`, `mentions_messenger_sharing_score`.
  - `imported_phone_entries`, `birthdate`, `current_city`, `family_relationships`, `work_experiences`, `current_education`, `messenger_install_time`, `is_pseudo_blocked_by_viewer`.
  - `add_source` enum values including `ADDRESS_BOOK_SYNC`, `DELAYED_PHONE_NUMBER_MATCH`, `AUTO_ADD_INSTAGRAM_MATCH_FLOW`, `PARENT_APPROVAL`.
  - Server-computed closeness scores are pushed to the device.
- [C] assets/feature_config_asset.json: on-device Messenger ranking features (impression, click and send counts per `target_id`, 6h/1d/7d/30d windows, decay), kept for 32 days.

## 9. Phone and call capabilities (missed by the manifest audit: uses-permission-sdk-23)
- [C] `READ_CALL_LOG` and `ANSWER_PHONE_CALLS` with maxSdkVersion 28 (Android 6-9 only), `READ_PHONE_NUMBERS`, `CALL_PHONE`, `BLUETOOTH_ADMIN`. The audit JSON lists 18 dangerous permissions; the true count is 20 on Android 10+ and 22 on Android 6-9.
  - READ_CALL_LOG ≤28 together with `flash_call_permission_status` in the login request points to flash-call phone verification.
- [C] Click-to-call ad receivers on `android.intent.action.PHONE_STATE`: `com.facebook.clicktocall.CTCPhoneCallBroadcastReceiver`, `LeadAdsP2BCallStateChangeReceiver`, `ctm.CtmPhoneCallBroadcastReceiver`. Call state is observed to measure calls placed from ads.
- [F] `lead_ads_post_submission_call_logging:enable_signal_collecting_disclaimer`.

## 10. Identity verification video selfie: retained 1 year by default
- [C] 0x7f1401a4 "To help improve our systems that detect impersonation and fake IDs, we normally store videos for up to 1 year. You can reduce this to 30 days…".
- [C] 0x7f1401be "We use face recognition to review your video. It will be stored securely for up to 1 year…". The toggle string is 0x7f1401a1 "Store video for 1 year"; the opt-down copy is 0x7f14019e.
- Biometric-adjacent data is kept for 12 months by default for model improvement. Shortening it to 30 days is opt-out.

## 11. Meta AI pushes (all [F])
- Meta AI button with feed context:
  - `fb4a_meta_ai_fab_context:fetch_fab_post_context_on_feed_enabled`, `proactive_voice_prompt_enabled`, `voice_session_feed_contextual_awareness_enabled`, `inject_context_on_deeplink_open`.
  - `fb4a_metaai_contextual_fab:enable_screen_share`, `enable_track_post_context_in_appjob`, `enable_speculative_context_queue`.
- On-device intent detection over typed messages to show Meta AI prompts:
  - `msgr_android_meta_ai_od_intent_detection:intent_probability_threshold`, `mustache_nux_max_impression_count`, `max_number_of_cycles`, `time_in_between_cycles_in_days`.
  - `odin_msgr_android_metaai_ner:*` (on-device named-entity recognition (NER) model).
- AI summaries of unread chats, including E2EE (via TEE "private processing"):
  - `m4a_unopened_content:is_genai_inbox_summary_pill_enabled_e2ee`, `is_e2ee_tee_thread_summary_enabled`.
  - `summary_bottom_sheet_undismissible_duration_ms`.
- Other entry points:
  - `fb4a_comments_ai_invocation:enable_meta_ai_mention_pills`, `meta_ai_mention_pill_suggestion_1..5`.
  - `fb4a_ifu_standardization_h1_2026:enable_meta_ai_promotion_header/footer`.
  - `fb4a_feed_me_ai_agent:enable_iab_shop_nudge`, `disable_iab_transparency_interstitial`.
  - `fb4a_mib_genai:is_precise_location_enabled`.
  - About 1,760 AI-related params in total.
- [C] Bundled AI Studio NUX Bloks screens (com.bloks.www.gen_ai.ai_studio.*). Downloadable `ondevicellm` module. `com.google.android.apps.aicore.service.BIND_SERVICE` permission plus `com.google.mlkit.genai.DEPENDENCIES=genai_prompt` (Gemini Nano on-device).

## 12. Other permissions and meta-data of note
- SYSTEM_ALERT_WINDOW (chat heads), REQUEST_IGNORE_BATTERY_OPTIMIZATIONS, USE_FULL_SCREEN_INTENT, DOWNLOAD_WITHOUT_NOTIFICATION, DETECT_SCREEN_CAPTURE/RECORDING.
- READ_GSERVICES (GSF id), GET_ACCOUNTS/MANAGE_ACCOUNTS/AUTHENTICATE_ACCOUNTS, READ_PROFILE.
- READ/WRITE_CALENDAR, ACCESS_MEDIA_LOCATION (photo EXIF location), RECORD_AUDIO, NFC (downloadable `nfc_passport` module for ID checks), BATTERY_STATS, GET_TASKS.
- `ActivityTransitionReceiver` in notifications.tray.helpers is guarded by the GMS ACTIVITY_RECOGNITION permission, but the app declares no ACTIVITY_RECOGNITION permission. This is capability residue, likely non-functional on Android 10+.
- Boot receivers: LoginNotificationServiceScheduler, ConfirmationNotificationReScheduler, NotifRecoveryReceiver, ContinuousBatteryMonitorService$BroadcastReceiver (also POWER_CONNECTED/DISCONNECTED), UpdateQeBroadcastReceiver, mqtt BootCompleteBroadcastReceiver, WorkManager.
- Unlock: `com.facebook.rti.orca.FbnsLiteBroadcastReceiver` on USER_PRESENT and CONNECTIVITY_CHANGE (push-channel reconnect). `NotificationsClientSignalStaticBroadcastReceiver` on SCREEN_ON/OFF, BATTERY_LOW/OKAY, AIRPLANE_MODE and POWER (notification timing signals; most of these are not delivered to manifest receivers on Android 8+).
- 361 components are `enabled="false"` in the manifest and enabled in stages at runtime (`enable-stage` meta-data, appcomponentmanager).

## Good practice / checked and cleared
- No ACCESS_BACKGROUND_LOCATION, BLUETOOTH_SCAN, NEARBY_WIFI_DEVICES, QUERY_ALL_PACKAGES, PACKAGE_USAGE_STATS, BODY_SENSORS, ACTIVITY_RECOGNITION, READ_SMS or RECEIVE_SMS. SMS codes come via the SMS Retriever API (`SMSBroadcastReceiver`, `SMS_RETRIEVED`) and WhatsApp OTP hand-off.
- No Wi-Fi, cell or BT location-package flags (no bssid/wifi_scan/cell_scan names), unlike Instagram. `realtime_location_*` is only `marketplace_location_picker` (accuracy 1000 m, freshness 60 s defaults).
- No under-13 or age-model flags seen. There are youth-ads restrictions (`ama_pao_youth:*`, `ama_basic_youth_ads`) and Dating age verification (`gemstone_age_verification:*`, default false).
- `m4a_calls_tab:call_log_max_rows` and the `call_log` table in assets/dsp are Messenger's own in-app call history, not the device call log.
  - assets/dsp/*.p (1641) and eb_dsp/*.p (100) are zlib-compressed precompiled SQLite procedures for Messenger's MSYS database (threads, messages, contacts, encrypted backups).
- "ccu" flags (`tw_discovery_ux:should_show_ccu_on_world_tiles`) mean concurrent users in Horizon Worlds, not contact upload.
- The autofill disclosure is explicit, payment numbers are excluded from ads use, CVVs are device-only and encrypted, and one-time virtual cards are offered.
- On-device safety models: `odin_m4a_scam_detection`, `fbm_nudity_protections_2026`. Cloaking text is kept 1 day and PPA data 32 days.
- The FDIDLite provider verifies callers by signature allowlist (not open to arbitrary apps).
- The 15 plain native libs (lib/arm64-v8a) are loader, crash and graphics infrastructure only.

## Limitations
- No main-app Java, RN or native code. Every [F] item is a flag name, so neither defaults nor actual use could be verified.
- Only 5,196 RN flags carry defaults, and most are false or empty.
- English master strings are superpacked. Translations ship as downloadable i18n modules.
- Exported-provider implementations (`$Impl`) are not visible.
