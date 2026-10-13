"""Scan a JADX output tree for privacy- and dark-pattern-relevant code and copy.

Usage: python scan_patterns.py <jadx_dir> <strings_dir_or_-> <out.md>
Library packages (androidx, kotlin, okhttp, ...) are excluded from code
categories so hits reflect the app's own code where names survive.
"""
import os, re, subprocess, sys, json, collections

CODE = {
 # --- data collection / tracking ---
 "installed_apps": r"getInstalledPackages|getInstalledApplications|queryIntentActivities\(|getPackageInfo\(\"com\.",
 "usage_stats": r"UsageStatsManager|queryUsageStats|queryEvents\(|\"usagestats\"",
 "clipboard": r"getPrimaryClip\(|addPrimaryClipChangedListener|hasPrimaryClip\(",
 "contacts": r"ContactsContract",
 "call_log": r"CallLog\.Calls|content://call_log",
 "sms": r"Telephony\.Sms|content://sms|SmsRetriever",
 "location": r"requestLocationUpdates|getLastKnownLocation|getCurrentLocation\(|FusedLocationProviderClient|requestGeofences|addGeofences",
 "wifi_bt_scan": r"getScanResults\(|\.startScan\(|getBSSID\(|getSSID\(|BluetoothLeScanner|startDiscovery\(",
 "device_ids": r"\"android_id\"|Settings\.Secure\.ANDROID_ID|getDeviceId\(|getImei\(|getMeid\(|getSubscriberId\(|getSimSerialNumber\(|getLine1Number\(|Build\.getSerial|getSerial\(\)",
 "gsf_id": r"com\.google\.android\.gsf\.gservices|\"android_id\".*gservices",
 "advertising_id": r"AdvertisingIdClient|getAdvertisingIdInfo|AdIdManager|TopicsManager|MeasurementManager",
 "install_referrer": r"InstallReferrerClient|getInstallReferrer",
 "sensors": r"TYPE_ACCELEROMETER|TYPE_GYROSCOPE|TYPE_MAGNETIC_FIELD|TYPE_PRESSURE|TYPE_LIGHT|TYPE_PROXIMITY|TYPE_STEP_COUNTER",
 "accounts": r"AccountManager\.get\(|getAccountsByType|getAccounts\(\)",
 "battery_state": r"ACTION_BATTERY_CHANGED|BatteryManager\.EXTRA_LEVEL|isCharging\(",
 "screen_capture_detect": r"ScreenCaptureCallback|registerScreenCaptureCallback|addScreenRecordingCallback|SCREENSHOT",
 "audio_capture": r"new AudioRecord\(|MediaRecorder\.AudioSource|SpeechRecognizer",
 "accessibility": r"AccessibilityManager|isTouchExplorationEnabled|getEnabledAccessibilityServiceList",
 "root_emulator": r"/system/xbin/su|\"/system/bin/su\"|ro\.kernel\.qemu|isEmulator|isRooted|Magisk|frida|xposed",
 "js_bridge": r"addJavascriptInterface",
 "boot_persist": r"BOOT_COMPLETED|MY_PACKAGE_REPLACED|setExactAndAllowWhileIdle|setAlarmClock|ignoreBatteryOptimizations|IGNORE_BATTERY_OPTIMIZATIONS",
 "full_screen_intent": r"setFullScreenIntent|USE_FULL_SCREEN_INTENT",
 "health_connect": r"HealthConnectClient|readRecords|ReadRecordsRequest|HeartRateRecord|StepsRecord",
 "keystroke_text_capture": r"addTextChangedListener|onTextChanged",
 "webview_tracking": r"setThirdPartyCookies|setAcceptThirdPartyCookies",
 # --- engagement / dark patterns (code identifiers) ---
 "streaks": r"(?i)streak",
 "reengagement": r"(?i)re_?engage|resurrect|lapsed|dormant|win_?back|churn",
 "notif_permission_nag": r"(?i)push_?prime|soft_?prompt|pre_?prompt|notification_?permission_?(nudge|reprompt|upsell|reminder)|reprompt",
 "cancellation_retention": r"(?i)cancel(lation)?_?(flow|survey|offer)|retention_?offer|save_?offer|winback_?offer",
 "urgency_countdown": r"(?i)countdown|expires_?in|limited_?time|flash_?sale|time_?left|timer_?offer",
 "infinite_autoplay": r"(?i)autoplay|auto_?advance|infinite_?scroll|endless",
 "badges": r"ShortcutBadger|setNumber\(|badge_?count|setBadgeIconType",
 "minors_age": r"(?i)age_?(estimation|prediction|verification|gate)|predicted_?age|is_?teen|under_?13|underage|minor_?account",
 "screen_time": r"(?i)time_?spent|session_?length|daily_?limit|take_?a_?break|quiet_?mode",
}
STRINGS = {
 "loss_aversion_copy": r"(?i)lose your|don.t lose|you.ll lose|before it.s too late|about to (end|expire|break|lose)|will (end|break|be lost)|freeze|repair",
 "urgency_copy": r"(?i)last chance|limited time|ends in|expires|only today|hurry|act now|hours? left|minutes? left|ending soon|don.t miss",
 "confirmshaming_copy": r"(?i)no thanks|no, i|i don.t want|i.d rather|maybe later|not now|i.ll pass|i.m okay|lose my|give up",
 "social_pressure_copy": r"(?i)friends? (is|are) (waiting|watching)|is typing|seen by|viewed your|screenshot|snapscore|best friends?|fire|someone (viewed|liked|mentioned)",
 "guilt_copy": r"(?i)sad|disappoint|miss you|we miss|haven.t (seen|practiced|opened)|come back|you forgot|forgot to|on fire|cry|tears",
 "subscription_copy": r"(?i)free trial|cancel anytime|auto.?renew|renews|billed|subscription|unlock|super|premium|plus|max",
 "data_copy": r"(?i)contacts|sync your|upload your|find friends|location|personaliz|advertis|partners|share data|third.part",
}
LIB = ("androidx/", "android/support/", "kotlin/", "kotlinx/", "okhttp3/", "okio/", "retrofit2/",
       "com/google/", "io/reactivex", "com/squareup/", "dagger/", "javax/", "org/", "j$/", "com/bumptech/",
       "io/grpc/", "com/fasterxml/", "io/sentry/", "com/airbnb/lottie/", "coil/", "com/apollographql/")

def rg(pattern, path, globs):
    cmd = ["rg", "-n", "--no-heading", "-o", "-M", "300", "-e", pattern, path] + sum([["-g", g] for g in globs], [])
    r = subprocess.run(cmd + ["--max-columns", "300"], capture_output=True, text=True)
    return r.stdout.splitlines()

def ctx(pattern, path, globs, limit):
    cmd = ["rg", "-n", "--no-heading", "-M", "260", "--max-columns-preview", "-e", pattern, path] + sum([["-g", g] for g in globs], [])
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout.splitlines()[:limit]

def main(jadx, strings, out):
    src = os.path.join(jadx, "sources")
    globs = ["*.java"] + [f"!{l}**" for l in LIB]
    res = {}
    with open(out, "w") as f:
        f.write(f"# Pattern scan: {jadx}\n\n## Code categories (library packages excluded)\n\n")
        for k, p in CODE.items():
            lines = ctx(p, src, globs, 100000)
            files = collections.Counter(l.split(":", 1)[0].replace(src + "/", "") for l in lines)
            res[k] = {"hits": len(lines), "files": len(files)}
            f.write(f"### {k} — {len(lines)} hits in {len(files)} files\n\n")
            for fn, c in files.most_common(12):
                f.write(f"- `{fn}` ({c})\n")
            f.write("\n```\n")
            for l in lines[:12]:
                f.write(l.replace(src + "/", "")[:300] + "\n")
            f.write("```\n\n")
        if strings != "-":
            f.write("## UI string categories (default locale)\n\n")
            for k, p in STRINGS.items():
                lines = ctx(p, strings, ["strings.xml", "plurals.xml"], 100000)
                res[k] = {"hits": len(lines)}
                f.write(f"### {k} — {len(lines)} strings\n\n```\n")
                for l in lines[:400]:
                    f.write(l.replace(strings + "/", "")[:300] + "\n")
                f.write("```\n\n")
    json.dump(res, open(out + ".json", "w"), indent=1)

if __name__ == "__main__":
    main(*sys.argv[1:4])
