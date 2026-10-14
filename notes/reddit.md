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

## Second pass (full per-DEX tree work/reddit/jdex)
- No queryUsageStats/queryEvents anywhere → PACKAGE_USAGE_STATS unused. No contacts reading (only contact photo lookup for share UI), location only AndroidX TwilightManager (no location permission).
- Daily streaks: StreakExtendedNotification, android_conditional_streak_popup, streakPopups; copy "Your current streak is %s days, not progressed today with an alert"; onboarding "People with longer than 50 day streaks earn 271% more karma."
- Push categories visible client-side: lifecycle_post_suggestions, subreddit_recommendation, top_post_deeplink, trending (from_trending_pn), upvote_post/comment etc.
- Age verification: Persona (selfie/ID) or Google age range; "won't retain ... after 7 days"; framed "Unlock all features".
- Cookie consent: Accept All / Reject Optional Cookies equal weight.
- Account deletion: posts/comments/messages "dissociated (not deleted)".
- Ad ID: honours limit_ad_tracking for Amazon/Google IDs (com/reddit/ads/impl/operator/b.java). AppsFlyer used for attribution/deeplinks only.
- WebView JS injection only on ads.reddit.com / own pages.
- Answers AI quota: "Come back tomorrow or upgrade to get more."
