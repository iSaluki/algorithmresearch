# Duolingo 6.101.2 — working notes (paths under work/duolingo/jadx/sources)

## Non-dismissible streak notifications
- defpackage/oms.java:1502-1525 — for NotificationType.STREAK_SAVER, if notifications enabled, Android 13+ (excl. Samsung on API>34 and a manufacturer blocklist), streak >= 7 days and remote flag on: schedules UnstickNotificationWorker for a configured LocalTime *the next day* ("UnstickStickyNotification_<tag>").
- defpackage/lg40.java — the unstick worker finds the active notification with FLAG_NO_CLEAR (flags & 32), clears it and sets FLAG_ONLY_ALERT_ONCE, logs "sticky_notification_unstuck" with unstuck_delay_minutes.
- Streak saver channel created at IMPORTANCE_HIGH (4) vs default 3 (oms.java:559).
- Live countdown "to save your streak" red timer 3600s with animated Duo variants terminator_duo, mad_duo, jaw_open_duo, laser_duo, surprised_duo (defpackage/sks.java debug catalog).

## Notification taxonomy (com/duolingo/data/notifications/NotificationType.java)
ABANDONED_CART_BASICS, ABANDONED_CART_PLACEMENT, PASSIVE_AGGRESSIVE, REACTIVATION, RESURRECTION, CONTINUOUS_RESURRECTION, RESURRECTED_QUEST, COMEBACK_BOOST, STREAK_EARNBACK, STREAK_SAVER, PASSED, LEADERBOARDS_FRIEND_NUDGE, FRIENDS_RESURRECTION, FRIEND_STREAK_NUDGE, APP_ICON_UPDATE, REMOVE_AND_RESEND_NOTIFICATION (remove_and_resend_silent), EARLY_BIRD, NIGHT_OWL ...
Debug sample for resurrection: "Don't give up" / "Give learning spanish another try!"; comeback_boost "XP Boost expires soon…" with timer.

## Launcher icon/label manipulation
activity-alias launchers: PreStreakSaver1..9Launcher (escalating icons ic_launcher_pre_streak_saver_3..9), StreakSaverLauncher{,Hourglass,Siren,AlarmClock,ExclamationMarks,EmojiQuestionMark,Eyes,...} with labels "Duolingo⏳", "Duolingo🚨", "Duolingo⏰", "Duolingo‼️", "Duolingo❓", "Duolingo👀", "Duolingo⁉️"; FixedRetentionChallengeLauncher (ic_launcher_boiling_cucumber); NotificationType.APP_ICON_UPDATE.

## Wi-Fi-triggered practice reminders + network fingerprinting
- com/duolingo/notifications/TriggeredNotificationWifiWorker.java — "wifiTriggeredPracticeReminderExperiment": a practice push arrives with should_drop_notification=true and is shown only when device is on Wi-Fi (hasTransport(TRANSPORT_WIFI)); logs is_device_idle_mode, is_power_save_mode, is_ignoring_battery_optimizations, network_days_seen_before_today.
- defpackage/gde.java — fingerprints network from default-route gateway IPv4 + subnet prefix (hashed; NoSuchAlgorithmException path) and counts days each network was seen → "familiar place" detection without location permission.

## Global analytics properties (defpackage/pu60.java:771+)
app_standby_bucket (monitors OS throttling), audio_output_volume, sim_network_country, sim_provider_country, timezone, font_scale, is_dark_mode, recognizer_package_name, webview version, low-end device flags.

## Ads
32 Exodus trackers; full SDKs bundled: Pangle/ByteDance (2743 class refs), ironSource (4139), Unity Ads (1475), Vungle (403), Meta Audience Network (309), AppLovin MAX, Adjust (279), Mintegral, InMobi, Smaato, Fyber, Chartboost, HyprMX, BidMachine, PubNative, SuperAwesome, Moloco; adapter-only refs: Yandex, myTarget, Ogury, Tapjoy, maio.
Manifest: ACCESS_ADSERVICES_AD_ID/ATTRIBUTION/TOPICS + AD_ID.

## Copy (apktool res/values/strings.xml)
"Wait, don't go! If you quit, you'll lose your progress." / "Losing makes me cry on the outside AND inside!" / "Hello, sadness…" / "Streak's in danger!" / "Come back today to protect your streak…" / "Don't get demoted! Keep moving up with a Timer Boost." / "Get a League Repair to reclaim your spot" / "Add Widget to Repair" / "Never lose your streak again with Duo on your phone's home screen!" / "Reaching a N day streak will put you in the top X% of all streaks" / "You'll lose access to Super Family Plan in N hours" / "Are you sure you want to leave? You'll lose access to Max."
