# Proton Mail 7.11.10 — working notes (paths under work/protonmail/jadx/sources)

- 14 permissions, 3 dangerous (CAMERA, POST_NOTIFICATIONS, READ_CONTACTS). Contacts used for recipient autocomplete ("Show device contacts") and explicit "Upload device contacts" import.
- Exodus trackers: Sentry only. Sentry DSN self-hosted: https://...@api.protonmail.ch/core/v4/reports/sentry/75 (androidx/activity/b0.java:228); session replay not configured; Timber integration (WARNING events, INFO breadcrumbs). User setting crashReports exists (mailsession/domain/model/v.java) — gating of SDK by this toggle not confirmed.
- Firebase: analytics deactivated, ad-ID collection disabled, messaging auto-init disabled in manifest (FCM used for push only).
- Upsell: drawer banners "Black Friday Sale"/"Spring Sale"/"Summer Sale"/"SPECIAL OFFER"; feature gates with "Upgrade to ..." copy; auto-renew price disclosure present ("Welcome offer. Auto-renews at %s").
- REA evidence: work/rea/protonmail.package.json (sha256 c33e4a3b...).
