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
