# Snapchat 14.27.0.53 — working notes (evidence pointers into work/snapchat/jadx/sources)

## Contact upload with "closeness" metadata
- defpackage/C0111Ac0.java:403 — queries ContactsContract.Data for contact_id, display_name, contact_last_updated_timestamp, starred, photo_uri, mimetype, data1-3 (entire address book).
- Builds Contact(contactId, name, type, phoneNumbers, lastUpdatedTimestamp, emailAddresses, starred, hasEvent, hasPhoto, firstSocialLink) (defpackage/C40594pf4.java:103-193).
- "firstSocialLink": mimetype of other apps' rows on the contact (e.g. vnd.com.whatsapp.profile) matched against server-config list `frnd_contact_social_link_mime_type_keywords` (defpackage/WR8.java:114, default "" → remotely switchable).
- Serialized per-number JSON {number, hasStarred, hasPhoto, hasSavedDate, hasSocialLink, contactType} (defpackage/C16092Zh4.java) in request `contacts_with_meta_data` (defpackage/C54695yr8.java) built in AbstractC13515Vh4.a.
- Sent to /bq/find_friends_reg (during registration, header early_contact_sync=first/second) and /ph/find_friends (com/snap/identity/FriendingHttpInterface.java:23-28).
- Request also carries `enable_find_friends_for_UK_under_age` flag (C54695yr8.java:43), value from FindFriendsEligbilityImpl (C45498sr8).
- Contact change detection: contact_last_updated_timestamp > lastSync (C43861rn5.java:199); job analytics distinguish app_state foreground/background (C0111Ac0.java:382).
- Hidden SyncAdapter/AccountAuthenticator for contacts (userVisible=false), service is a no-op stub; used to write "Snapchat" raw contacts into the system address book (FB6.java:802 RawContacts insert).

## Churn-risk targeting
- User segments from server: is_new_user, is_14_days_new_user, is_deep_churn, is_high_churn_risk_active/new/resurrected (defpackage/EnumC23587eaa.java:663-677; HB3.java maps).
- "Added Me" full-screen takeover on camera: default max per session 15 for new/churn users vs 5 for normal users (EnumC23587eaa.java:654-660), consumed by AddedMeTakeOverOnCameraProviderImpl (C20018cG.java:45-46) with HB3 segment check.
- Registration re-engagement pushes to users who abandon signup: RegistrationReengagementPushManager, GROWTH_NOTIFICATION_REGISTRATION_REENGAGEMENT.
- Resurrected-user streak restores: ResurrectedRestoreEligibilityCheck, RESURRECTED_RESTORE_ELIGIBILITY_WINDOW, STREAK_RESURRECTED_RESTORE_USED, "resurrection_7_days_or_greater".
- Snapchat+ win-back SKU "winback-1m-599".

## Benign / false positives checked
- BSSID read (E1b.java) used only as local key for bandwidth estimate cache.
- Queried packages (MIUI/Huawei security centers) = deep links to permission settings (C46472tUe.java); Netflix/Spotify etc. = "open in app" link handling (C23005eCe.java); TikTok = share target (QJc.java).
- Clipboard reads only on paste in OTP/chat/comment inputs.

## Sponsored Snaps (ads in chat inbox)
- strings: "New in Your Chat Feed: Sponsored Snaps", "Choose Your Ad Experience" with only "Smaller In-Feed Ads" / "Larger Banner Ads" (no "no ads"), "I'm In!" / "Not Now"; framed as "personalized messages from your favorite artists, creators, brands".
- defpackage/AKi.java:2481-2489 defaults: sponsored_snaps_eu_modal_dismissal_reprompt_ttl_seconds=172800 (48h), ..._dismissal_reprompt_frequency_cap=10, ..._opt_in_reprompt_ttl_days=183.
## Snap Pixel identity cookie
- AKi: pixel_tracking_host tr.snapchat.com, path /cm/wv, cookie sc_at, ttl 120h. defpackage/C41823qSg.java:229-237 GET https://tr.snapchat.com/cm/wv?scut=<pixel token>; AdsCookieManagerV2 (defpackage/C33862lH.java) caches; attached for WEB ad attachments (defpackage/C34056lOk.java:472-482).
## Other ad config defaults (AKi)
- ads_mushroom_location_in_ad_req=false (remote switch), snapads_mushroom_enable_check_on_device_can_open_url=false, ads_mushroom_remove_isshow_unskippable=true, ads_device_cluster.

## Location history / Footsteps / background location
- strings: "Clear your location history, including travel updates and Places you've visited while location is turned on" (separate carve-outs: "not including Footsteps", "not including Places you tagged in Snaps"); "Your location history updates while you have Snapchat open"; Places "Visited", "Highly Revisited", "Recently Visited", "Visited by $0".
- Footsteps: "Your first steps will be based on Snaps in your Memories" (backfill from Memories location metadata); Snapchat+ feature; "Get Footsteps!" upsell.
- "Allow all the time" upsell trays; com/snap/map_me_tray/MeTrayUpsellType BackgroundLocationRecovery; LodaDaemonService (foregroundServiceType=location), GeofenceBroadcastReceiver (enter/exit/dwell), LodaPushNotificationHandler, LodaLocationAccumulator + disk buffer + upload client.
- UK U18: "Your last location is shared for 24 hours after app close".
## My AI
- Disclosure: uses content + location; "Content you share is retained until you delete it"; "We use My AI information to improve our products and ads"; "We share information with our service providers and advertising partners"; group: "My AI can read all messages in the chat".
- Snapchat+ ad-free plan: "You may still see sponsored places and My AI responses."
## Snapchat+ cancellation: "Don't Cancel" → "You will lose access to the following features..." → exit survey → "Finish canceling in settings".
## Minors
- "If you open this message, $0 may be able to determine that you have their phone number in your contact book."
- Public profile for 16+ ("Grow Your Audience" — "Anyone can see your Public Profile"); Spotlight payouts to minors 16+ with parental consent.
- "Solar Systems" Best Friend orbit ranking (Snapchat+).

## Camera roll + Memories processing
- Memories DB (defpackage/C44243s2b.java): detected_face(snap_id, cluster_id, bbox, encoding BLOB), face_cluster(tagged_user_id), face_cluster_blocklist; snap_indexing_process_status (visual tagging, visual tag cluster, TinyClip caption + embeddings); camera_roll_metadata(date_taken, is_favorite, path, relative_path, is_uploaded); save_operations(latitude, longitude).
- Face Tagging toggle copy: "organized by face for easier searching, resurfacing, and future manual or automatic creative use"; turn-off: "All your face groups and group names will be deleted ... start over" ("Keep On"/"Turn Off").
- Config: FACE_CLUSTERING_ENABLED default false (MEMORIES_ANDROID_FACE_CLUSTERING), FACE_TAGGING_MAX_BACKFILL_SIZE 10000.
- Camera-roll metadata: CameraRollMetadataScanRecurringDurableJob (every 8h default, 50 items/page), CameraRollMetadataGrpcService, ENABLE_CAMERA_ROLL_FS_METADATA_UPLOAD default false (defpackage/Q1d.java:1142-1160); Flashback "featured stories" from camera roll.
