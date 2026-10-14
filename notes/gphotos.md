# Google Photos 7.97.0 (com.google.android.apps.photos) — working notes (paths under work/gphotos/jdex)

Code is almost entirely obfuscated into `defpackage/` (Compose lambdas, inlined resource IDs). String IDs were mapped via apktool res/values/public.xml (decimal ID → name). Many decisions (eligibility, region defaults, frequencies) are server flags; client fallbacks noted where visible.

## 1. Auto-backup "best by default" sheet: pre-checked switch, non-cancelable, "Are you sure?" on decline, recurring every 14 days
- classes4/sources/defpackage/tjm.java (HalfSheetAutoBackupPromoFragment):
  - "best by default" variant (bd() = config present): backup switch "Back up photos & videos on this device automatically" pre-checked (`best_by_default_switch_state` default true, line ~281); the separate "Don’t turn on backup"/"Do not back up" button is hidden (aO GONE, ~248); single primary button "Turn on backup".
  - Sheet is `setCancelable(false)` (~258).
  - Toggling the switch off immediately opens bb() dialog (syc.java case 4 → tjm.bb ~314): title "Are you sure?", body "Without backup, your photos aren’t protected if your device is damaged, lost or stolen. Also, Memories with new photos can’t be created for you, and what you’ll see in search results won’t be complete.", buttons "Turn on backup" / "Keep backup off", `q(false)` (not cancelable). Only then the main button changes to "Continue without backup".
  - Other titles: "Your photos aren’t backing up", "{n} days of photos aren’t backed up" (backup_off_duration), "Back up now, clean up later"; bbd strings "Don’t lose your photos, turn on backup today", "Backup is off. New photos and videos may be at risk.", "# photos and videos on this device may be at risk…", comparison table "NOT BACKED UP" vs "BACKED UP" (memories/search/safety).
- Recurrence: classes4/sources/defpackage/tjo.java ~141: "half_sheet_best_by_default_migration_recurring" cooldown = server value or fallback **14 days**; shown while backup off, not out-of-storage, not unlimited; normally gated on **Google One eligibility** ("Not google one eligible" check, ~146) — i.e. backup push targeted at users who can be upsold storage.
- Reconsent sheet (classes4/sources/defpackage/abzi.java): "Keep backup on?" / "Keep backup on" vs "Turn off backup"; `id(false)` non-cancelable. Balanced buttons but backup already on by default.
- Device-setup copy: "Continue without backup" → "Most features won't be available"; Recap promo "Without backup, we can’t create your Recap"; OS-migration disclaimer: "To restore your albums, they will be backed up automatically, regardless of whether you enable backup." (photos_devicesetup_os_migration_disclaimer_learn_more; abxm.java/aabs.java).
- Good: each consent screen records the exact string resource IDs shown (chxo/chxd consent UI proto, e.g. tjm.java/abzi.java "shu.e(id)") — auditable consent records.

## 2. Gemini / "Ask Photos" onboarding: every opt-out gets a second "are you sure" dialog; face + location linking
- Three-step setup (strings photos_ellmann_*; code classes5/sources/defpackage/afjz.java, classes2/sources/defpackage/bftf.java):
  - Gemini: decline → "Continue without Gemini?" / "You won’t be able to search with Ask Photos or… ask Photos to make edits." buttons "Go back" / "Continue" (afjz.java ~2197).
  - Face/"Me" label: "Which one is you?" / "Make the app yours"; decline → "Don’t allow this type of personalization?" / "**Knowing who you are** is essential to you getting the best experience." buttons "Go back" / "Don’t allow" (afjz.java ~678).
  - Face grouping off → "Face grouping is essential to you getting the best experience. It personalizes search, albums, memories, and more." buttons "Go back" / "Not now" (bftf.java).
  - Location estimation: "Want more results when searching by location?" decline → "Don’t allow location estimation" / "Estimating locations gives you more results when you search." "Go back"/"Not now" (afjz.java ~1078).
  - Progress banner "Set up for the best experience (%1$d/%2$d)" (classes2/sources/defpackage/afia.java) and device-setup guide "%1$d of %2$d unlocked", "You’re so close, %1$s" with only "Remind me later".
- Disclosure: "Your face will be used to personalize search, memories, creations and more. **You may also be associated with photo locations based on photos with your face.**" (photos_ellmann_mecluster_disclaimer, settings faceclustering my_face_disclaimer).
- Upgrade dialog (classes5/sources/defpackage/afbd.java case 17 + afbg.java case 4 + afih.java:97): title "Improving Gemini features in Photos with location info", body "Google Photos can now tell you more about where you’ve been by matching your face to the locations in your photos with the help of Gemini models." Rendered as an AlertDialog with a single confirm button (dismissButton null) and DialogProperties(dismissOnBackPress=false, dismissOnClickOutside=false) (gjn(false,false,…,4064)) → notice-style, not a choice. Button label lambda not resolved.
- Settings opt-out: "Turn off Gemini and delete data?" "You’ll lose access to Gemini features… Your experience overall will be less personalized." / "This will permanently delete any data in your Remember List".
- Ask Photos queries: "Allow us to access your queries" — "your queries may be reviewed by humans… Queries aren’t tied to your account" (default not determinable). Feedback: "Your feedback will be used to improve Photos, even though your Ask Photos Activity is turned off."

## 3. Face grouping: notice-only at setup in 171 countries
- classes4/sources/defpackage/abye.java: device setup shows "Google Photos uses face grouping  Learn more" (no toggle) only when country ∈ hard-coded set classes6/sources/defpackage/bfey.java (171 ISO codes: includes US, CA, MX, BR, IN, JP, KR, AU, NZ, ZA, NG, IL, SG…; excludes all EU/EEA, GB, CH, NO, RU, TR, UA, CN, HK).
- Country = SIM country → network country (non-CDMA) → locale (classes/sources/defpackage/ywq.java, ywp.java).
- Actual enablement server-side (keys face_clustering_allowed / face_clustering_enabled / face_clustering_availability; RegisterPhotosUserTask "trigger_face_grouping_promo").
- Turn-off dialog: "Turn off face grouping?" "Any changes you've made to your face groups like added names will be permanently deleted." "Keep on" / "Turn off" (honest warning, but loss framing). Removing "Me" label: "You'll miss out on personalized search and creations".
- Face labels can be linked to device contacts ("Show results from contacts", "Frequent contacts" in people labeling).
- "Wardrobe"/Outfits (ellmann mft): "The Outfits collection automatically finds clothes you wear and uses AI to generate a browsable wardrobe" — automatic body/clothing analysis of the library, own notification channel; off switch "Turn wardrobe off".

## 4. Storage-full pressure / Google One upsell
- Out-of-storage full-screen interstitial "kirby" (classes4/sources/defpackage/vzu.java, eligibility wbd.java ~185-235): shown to G1-eligible non-members once quota runs out; content partly server-driven (offers "%1$s for ~~%2$s~~", "First N months, {original_price} after"); "Continue with a limited experience" escape; "kirby quiet period" only after clickthrough (server-tuned).
- "clifford" OOS screen: "Your backup for Google Photos has stopped", "If photos aren’t backed up, they’ll be lost if something happens to your phone. They also won’t show up in search, memories…", "Gmail and Drive won’t work as expected… soon you won’t be able to send or receive email"; "Continue without storage".
- Manual-delete path framed as costly: "On average, you’ll need to delete %1$d+ photos to get back # month of storage" / "deleting about {count} photos can free up a month’s worth of storage".
- Memories used as upsell lever: "Get more storage to keep your memories fresh" / "Your storage is %s%% full. Get more storage to keep seeing new photos in memories."; premium onboarding "New photos won’t be seen in search results and Memories when you run out of storage". Features gated on backup (album add, share link, print, save shared, restore from trash) → "get more storage with Google One".
- Win-back: "Come back to Google One", "Save years of treasured memories", "Get {discount}% off for # months".
- Compress nudge "defib": "You’ve been out of storage for several months" → "Compress now" (Storage saver).
- Banners: "Your storage is low (%1$s%% full)", avatar particle "Account storage almost full", payment-failure "Update your payment within %1$s day to keep your Google One storage".

## 5. AI-editing paywall
- Magic Editor metered: "You can save 10 edited photos every month or subscribe to a Google One Premium plan for unlimited saves."; "{n} saves left"; editor upsell "Unlock this feature and more with a Google One membership". Video Boost/Night Sight require backup → storage upsell.

## 6. Engagement / notifications
- Notification opt-in promos: "Don’t miss out on new Memories!", "Don’t miss comments from friends and loved ones", "Don’t miss a moment", "Don’t miss the good stuff", setup "Don’t miss anything important".
- Separate channels incl. "Promotions", "Features", "New memories", "Free up space", "Wardrobe" (user can mute individually — good).
- Crowdsource photo-donation promo inside Memories carousel ("story_general_donation_crowdsource"; zqo.java/zpz.java/CrowdsourceActivity): "Help improve Google products — Submit your photos to help develop and improve Google products" / "Take a minute and review photos to help Google". Opt-in, server-gated.
- Third-party cross-promo: CapCut (com.lemon.lvoverseas, ByteDance) tile is added to the share sheet even when NOT installed (classes6/sources/defpackage/biaw.java: install state d → add tile), leading to "Install CapCut?" dialog; also "Edit in CapCut" in memories.

## 7. Other permissions / data
- ACCESS_MEDIA_LOCATION (uses-permission-sdk-23) → reads unredacted EXIF GPS from all device media; requestLegacyExternalStorage.
- MANAGE_MEDIA prompt (classes5/sources/defpackage/alut.java case 12, amqd): "Don’t ask this every time? Change your Settings so that you don’t have to give permission every time you delete or edit photos" → removes the OS per-delete confirmation.
- Location permission only for print-store locator (classes6/sources/defpackage/bbhn.java LocationSheetMixin).
- Calendar: create event/reminder from screenshots (vgv.java "ReminderCreation", aegx.java), calendar list read (vgr.java) — user-initiated.
- READ_GSERVICES declared (GSF id, 2 hits in scan).

## Good practice / checked and cleared
- Deletion copy is explicit: "Remove from Google account & synced devices?", "Delete from device? Item will remain in your Google account", "Items not backed up. Permanently delete from device?".
- Memories: "Hide people & pets", "Hide dates", "Hide face from memories" controls.
- No advertising-ID or attribution SDK usage (scan: advertising_id 0, install_referrer 0); Exodus: only Firebase Analytics.
- Installed apps: getInstalledApplications only for VR-core check (classes8/sources/defpackage/cqzw.java); <queries> limited to Google apps + CapCut + share/edit intents.
- Usage stats: only own standby bucket (ubk.java, vft.java). Clipboard: clear-clipboard helper (wzq.java).
- GenAI provenance labels ("Edited using Generative AI"), GenAI Prohibited Use acknowledgements.
- Partner sharing: explicit choices (all/selected people/date), warnings when face grouping off.
- Consent screens log the exact string IDs displayed (auditable).
