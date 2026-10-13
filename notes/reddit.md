# Reddit 2026.40.0 — working notes (JADX tree ~84% complete; paths under work/reddit/jadx/sources)

## Notification permission nagging
- NotificationEnablementState: ShouldShowPrePrompt / ShouldShowRePrompt / ShouldShowReEnablementPrompt (com/reddit/notification/domain/model/NotificationEnablementState.java).
- NotificationReEnablementEntryPoint: AppLaunch, SessionChange, VoteComment, CommentCreation, PostCreation, FollowComment, FollowPost, FollowUser, Chat, StartChat, DirectMessage, AcceptChatInvite, SetAMAReminder, KeywordFollowingBanner, SubredditDataEntryPoint ...
- RedditNotificationReEnablementDelegate: isEligibleForAllNotificationUpsell, isInPostponeExperiment, handleReEnterPromptAsync.
- Copy: "Please turn on notifications"; "Get notified of the best content for you, as well as replies to your posts" (bundles recommendation pushes with replies); follow-up banners "Don't miss out" / "Be in the know"; "Only post & comment notifications" then upsell to all.

## Account deletion obstruction
- strings: account_deletion_failed_cancel_premium_sheet_content "To delete your account, you need to cancel your Reddit Premium subscription first."

## Ads that send you notifications
- strings: ad_reminder_modal_remind_me_description "Get a notification so you don't miss out." / ad_reminder_cancelled_messaging.

## Permissions
- PACKAGE_USAGE_STATS declared; only UsageStatsManager.getAppStandbyBucket() (own bucket) used (defpackage/z090.java) → over-declared.
- READ_GSERVICES declared; GSF android_id read by Google reCAPTCHA SDK (com/google/android/recaptcha/internal/zzcx.java:43) — persistent device identifier for anti-abuse.

## Attribution
- AppsFlyer gated by TrackingAndAttributionLevel != NONE and partner sharing filter (com/reddit/mmp/appsflyer/c.java); resolves marketing email links c.redditmail.com.

## Benign checks
- getInstalledPackages only to check for com.android.vending (defpackage/dtp0.java).
- getEnabledAccessibilityServiceList: snackbar timing (defpackage/au5.java).
