# Pattern scan: work/telegram/jdex

## Code categories (library packages excluded)

### installed_apps — 24 hits in 18 files

- `classes:fe/f.java` (3)
- `classes:t7/y.java` (3)
- `classes:f6/g.java` (2)
- `classes:c1/e.java` (2)
- `classes:p4/d.java` (1)
- `classes:org/telegram/messenger/EmuDetector.java` (1)
- `classes:b1/e.java` (1)
- `classes:t0/i.java` (1)
- `classes:org/telegram/messenger/NotificationBadge.java` (1)
- `classes:f6/e.java` (1)
- `classes:com/google/android/recaptcha/internal/zzcz.java` (1)
- `classes:org/telegram/messenger/FeedRemoteViewsFactory.java` (1)

```
classes:p4/d.java:117:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(intent, 128);
classes:fe/f.java:159:            listQueryIntentActivities = context.getPackageManager().queryIntentActivities(new Intent("android.intent.action.VIEW", Uri.parse("http://www.google.com")), 0);
classes:fe/f.java:177:            listQueryIntentActivities2 = context.getPackageManager().queryIntentActivities(new Intent("android.intent.action.VIEW", Uri.parse(str)), 0);
classes:fe/f.java:257:                    List<ResolveInfo> listQueryIntentActivities = ApplicationLoader.applicationContext.getPackageManager().queryIntentActivities(new Intent("android.intent.action.VIEW", uri), 0);
classes:org/telegram/messenger/EmuDetector.java:196:                if (launchIntentForPackage != null && !packageManager.queryIntentActivities(launchIntentForPackage, 65536).isEmpty()) {
classes:b1/e.java:275:        long j9 = packageManager.getPackageInfo("com.google.android.gms", 0).versionCode;
classes:t0/i.java:89:                for (ResolveInfo resolveInfo : packageManager.queryIntentActivities(new Intent().setAction("android.intent.action.PROCESS_TEXT").setType("text/plain"), 0)) {
classes:org/telegram/messenger/NotificationBadge.java:569:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(intent, 65536);
classes:f6/g.java:113:                packageInfo = packageManager.getPackageInfo("com.android.vending", 8256);
classes:f6/g.java:121:            PackageInfo packageInfo2 = packageManager.getPackageInfo("com.google.android.gms", 64);
classes:f6/e.java:31:            return context.getPackageManager().getPackageInfo("com.google.android.gms", 0).versionCode;
classes:com/google/android/recaptcha/internal/zzcz.java:48:            installedPackages = context.getPackageManager().getInstalledPackages(0);
```

### usage_stats — 0 hits in 0 files


```
```

### clipboard — 31 hits in 20 files

- `classes3:org/telegram/ui/of0.java` (4)
- `classes4:org/telegram/ui/Wallet/h9.java` (4)
- `classes3:org/telegram/ui/Components/yu.java` (3)
- `classes3:org/telegram/ui/i31.java` (2)
- `classes4:org/telegram/ui/Wallet/s8.java` (2)
- `classes4:org/telegram/ui/Wallet/m8.java` (2)
- `classes:ig/b.java` (1)
- `classes:l/s.java` (1)
- `classes3:org/telegram/ui/ss.java` (1)
- `classes3:org/telegram/ui/ts.java` (1)
- `classes3:org/telegram/ui/Cells/i9.java` (1)
- `classes3:org/telegram/ui/Components/ng.java` (1)

```
classes:ig/b.java:149:                if (i10 == 16908322 && (primaryClip = ((ClipboardManager) getContext().getSystemService("clipboard")).getPrimaryClip()) != null && primaryClip.getItemCount() == 1 && AndroidUtilities.charSequenceIndexOf(primaryClip.getItemAt(0).getText(), "\n") [... omitted end 
classes:l/s.java:202:        ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
classes3:org/telegram/ui/i31.java:162:        ClipData primaryClip = this.G.getPrimaryClip();
classes3:org/telegram/ui/i31.java:587:        this.G.addPrimaryClipChangedListener(this.K);
classes3:org/telegram/ui/ss.java:29:        if (qsVar != null && (clipboardManager = (ClipboardManager) tsVar.getContext().getSystemService(ClipboardManager.class)) != null && (primaryClip = clipboardManager.getPrimaryClip()) != null) {
classes3:org/telegram/ui/of0.java:160:                            charSequenceCoerceToText = ((ClipboardManager) of0Var.getContext().getSystemService("clipboard")).getPrimaryClip().getItemAt(0).coerceToText(of0Var.getContext());
classes3:org/telegram/ui/of0.java:297:                            charSequenceCoerceToText = ((ClipboardManager) of0Var.getContext().getSystemService("clipboard")).getPrimaryClip().getItemAt(0).coerceToText(of0Var.getContext());
classes3:org/telegram/ui/of0.java:445:                            charSequenceCoerceToText = ((ClipboardManager) of0Var.getContext().getSystemService("clipboard")).getPrimaryClip().getItemAt(0).coerceToText(of0Var.getContext());
classes3:org/telegram/ui/of0.java:777:        boolean z2 = TextUtils.isEmpty(this.c.getText()) && clipboardManager != null && clipboardManager.hasPrimaryClip();
classes3:org/telegram/ui/ts.java:174:                    ClipData.Item itemAt = clipboardManager.getPrimaryClip().getItemAt(0);
classes3:org/telegram/ui/Cells/i9.java:177:                        if (clipboardManager.hasPrimaryClip()) {
classes3:org/telegram/ui/Components/ng.java:232:            ClipData primaryClip = ((ClipboardManager) getContext().getSystemService("clipboard")).getPrimaryClip();
```

### contacts — 25 hits in 4 files

- `classes:org/telegram/messenger/ContactsController.java` (18)
- `classes3:org/telegram/ui/uk0.java` (3)
- `classes3:org/telegram/ui/Components/fk.java` (2)
- `classes3:org/telegram/ui/Components/hg0.java` (2)

```
classes:org/telegram/messenger/ContactsController.java:17:import android.provider.ContactsContract;
classes:org/telegram/messenger/ContactsController.java:249:        ContentProviderOperation.Builder builderNewInsert = ContentProviderOperation.newInsert(ContactsContract.RawContacts.CONTENT_URI);
classes:org/telegram/messenger/ContactsController.java:255:        Uri uri = ContactsContract.Data.CONTENT_URI;
classes:org/telegram/messenger/ContactsController.java:418:            Cursor cursorQuery = ApplicationLoader.applicationContext.getContentResolver().query(ContactsContract.RawContacts.CONTENT_URI, new String[]{"version"}, null, null, null);
classes:org/telegram/messenger/ContactsController.java:463:                ApplicationLoader.applicationContext.getContentResolver().delete(ContactsContract.RawContacts.CONTENT_URI.buildUpon().appendQueryParameter("caller_is_syncadapter", "true").appendQueryParameter("account_name", this.systemAccou
classes:org/telegram/messenger/ContactsController.java:1255:                ApplicationLoader.applicationContext.getContentResolver().registerContentObserver(ContactsContract.Contacts.CONTENT_URI, true, new MyContentObserver());
classes:org/telegram/messenger/ContactsController.java:2365:                Cursor cursorQuery = contentResolver.query(ContactsContract.RawContacts.CONTENT_URI, new String[]{"_id", "sync2"}, null, null, null);
classes:org/telegram/messenger/ContactsController.java:2482:                contentResolver.delete(ContactsContract.RawContacts.CONTENT_URI.buildUpon().appendQueryParameter("caller_is_syncadapter", "true").appendQueryParameter("account_name", this.systemAccount.name).appendQueryParameter("account_ty
classes:org/telegram/messenger/ContactsController.java:2578:            Uri uriBuild = ContactsContract.Groups.CONTENT_URI.buildUpon().appendQueryParameter("caller_is_syncadapter", "true").build();
classes:org/telegram/messenger/ContactsController.java:2579:            Uri uriBuild2 = ContactsContract.RawContacts.CONTENT_URI.buildUpon().appendQueryParameter("caller_is_syncadapter", "true").build();
classes:org/telegram/messenger/ContactsController.java:2598:            Uri uri = ContactsContract.Data.CONTENT_URI;
classes:org/telegram/messenger/ContactsController.java:2656:                Cursor cursorQuery = contentResolver.query(ContactsContract.Groups.CONTENT_URI, new String[]{"_id"}, "title=? AND account_type=? AND account_name=?", new String[]{"TelegramConnectionService", account.type, account.name}, nul
```

### call_log — 1 hits in 1 files

- `classes:org/telegram/messenger/AndroidUtilities.java` (1)

```
classes:org/telegram/messenger/AndroidUtilities.java:4012:            Cursor cursorQuery = ApplicationLoader.applicationContext.getContentResolver().query(CallLog.Calls.CONTENT_URI, new String[]{"number", "date"}, "type IN (3,1,5)", null, Build.VERSION.SDK_INT >= 26 ? "date DESC" : "date DESC LIMIT 
```

### sms — 6 hits in 4 files

- `classes:f7/e.java` (3)
- `classes:f7/f.java` (1)
- `classes:t5/a.java` (1)
- `classes:ra/a.java` (1)

```
classes:f7/f.java:35:                attachInterface(this, "com.google.android.gms.auth.api.phone.internal.ISmsRetrieverResultCallback");
classes:f7/e.java:25:        IInterface iInterfaceQueryLocalInterface = iBinder.queryLocalInterface("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService");
classes:f7/e.java:36:        return "com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService";
classes:f7/e.java:41:        return "com.google.android.gms.auth.api.phone.service.SmsRetrieverApiService.START";
classes:t5/a.java:13:    public static final e f15881k = new e("SmsRetriever.API", new r(15), new d());
classes:ra/a.java:404:        parcelObtain.writeInterfaceToken("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService");
```

### location — 27 hits in 11 files

- `classes:org/telegram/messenger/LocationController.java` (7)
- `classes3:org/telegram/ui/ThemeActivity.java` (5)
- `classes:org/telegram/messenger/SendMessagesHelper.java` (4)
- `classes:f/n.java` (2)
- `classes3:org/telegram/ui/zc.java` (2)
- `classes4:wg/q0.java` (2)
- `classes:org/telegram/messenger/ILocationServiceProvider.java` (1)
- `classes:org/telegram/messenger/GoogleLocationProvider.java` (1)
- `classes3:org/telegram/ui/zd0.java` (1)
- `classes3:org/telegram/ui/ld0.java` (1)
- `classes3:org/telegram/ui/Components/dm.java` (1)

```
classes:org/telegram/messenger/SendMessagesHelper.java:14244:                this.locationManager.requestLocationUpdates("gps", 1L, 0.0f, this.gpsLocationListener);
classes:org/telegram/messenger/SendMessagesHelper.java:14249:                this.locationManager.requestLocationUpdates("network", 1L, 0.0f, this.networkLocationListener);
classes:org/telegram/messenger/SendMessagesHelper.java:14254:                Location lastKnownLocation = this.locationManager.getLastKnownLocation("gps");
classes:org/telegram/messenger/SendMessagesHelper.java:14257:                    this.lastKnownLocation = this.locationManager.getLastKnownLocation("network");
classes:org/telegram/messenger/ILocationServiceProvider.java:65:    void requestLocationUpdates(ILocationRequest iLocationRequest, ILocationListener iLocationListener);
classes:org/telegram/messenger/LocationController.java:1285:            ApplicationLoader.getLocationServiceProvider().requestLocationUpdates(this.locationRequest, this.fusedLocationListener);
classes:org/telegram/messenger/LocationController.java:1342:            this.locationManager.requestLocationUpdates("gps", 1L, 0.0f, this.gpsLocationListener);
classes:org/telegram/messenger/LocationController.java:1347:            this.locationManager.requestLocationUpdates("network", 1L, 0.0f, this.networkLocationListener);
classes:org/telegram/messenger/LocationController.java:1352:            this.locationManager.requestLocationUpdates("passive", 1L, 0.0f, this.passiveLocationListener);
classes:org/telegram/messenger/LocationController.java:1358:                setLastKnownLocation(this.locationManager.getLastKnownLocation("gps"));
classes:org/telegram/messenger/LocationController.java:1360:                    setLastKnownLocation(this.locationManager.getLastKnownLocation("network"));
classes:org/telegram/messenger/LocationController.java:1540:    public Location getLastKnownLocation() {
```

### wifi_bt_scan — 1 hits in 1 files

- `classes4:org/webrtc/NetworkMonitorAutoDetect.java` (1)

```
classes4:org/webrtc/NetworkMonitorAutoDetect.java:395:            return (intentRegisterReceiver == null || (wifiInfo = (WifiInfo) intentRegisterReceiver.getParcelableExtra("wifiInfo")) == null || (ssid = wifiInfo.getSSID()) == null) ? "" : ssid;
```

### device_ids — 20 hits in 11 files

- `classes:androidx/core/widget/NestedScrollView.java` (6)
- `classes:org/telegram/messenger/EmuDetector.java` (3)
- `classes:com/google/android/gms/internal/clearcut/c2.java` (3)
- `classes:com/google/android/recaptcha/internal/zzbs.java` (1)
- `classes:f/m.java` (1)
- `classes:f/r.java` (1)
- `classes:f2/g0.java` (1)
- `classes3:org/telegram/ui/oh0.java` (1)
- `classes3:org/telegram/ui/lp0.java` (1)
- `classes3:org/telegram/ui/do0.java` (1)
- `classes3:org/telegram/ui/nh0.java` (1)

```
classes:org/telegram/messenger/EmuDetector.java:120:        String deviceId = ((TelephonyManager) this.mContext.getSystemService("phone")).getDeviceId();
classes:org/telegram/messenger/EmuDetector.java:147:        String subscriberId = ((TelephonyManager) this.mContext.getSystemService("phone")).getSubscriberId();
classes:org/telegram/messenger/EmuDetector.java:205:        String line1Number = ((TelephonyManager) this.mContext.getSystemService("phone")).getLine1Number();
classes:com/google/android/recaptcha/internal/zzbs.java:12:        Cursor cursorQuery = contentResolver.query(Uri.parse("content://com.google.android.gsf.gservices"), null, null, new String[]{"android_id"}, null);
classes:com/google/android/gms/internal/clearcut/c2.java:100:                Long lValueOf = (Long) f2.a(map, "android_id", 0L);
classes:com/google/android/gms/internal/clearcut/c2.java:104:                    String strB = f2.b(contentResolver, "android_id");
classes:com/google/android/gms/internal/clearcut/c2.java:113:                    f2.e(obj, map, "android_id", lValueOf);
classes:f/m.java:133:                    lVar.setQwertyMode(KeyCharacterMap.load(keyEvent.getDeviceId()).getKeyboardType() != 1);
classes:f/r.java:1332:                qVar.f5143h.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
classes:f2/g0.java:213:        if (i10 >= 34 && context != null && (deviceId = context.getDeviceId()) != 0 && deviceId != -1) {
classes:androidx/core/widget/NestedScrollView.java:697:            int deviceId = motionEvent.getDeviceId();
classes:androidx/core/widget/NestedScrollView.java:705:                int deviceId2 = motionEvent.getDeviceId();
```

### gsf_id — 3 hits in 2 files

- `classes:com/google/android/gms/internal/clearcut/f2.java` (2)
- `classes:com/google/android/recaptcha/internal/zzbs.java` (1)

```
classes:com/google/android/recaptcha/internal/zzbs.java:12:        Cursor cursorQuery = contentResolver.query(Uri.parse("content://com.google.android.gsf.gservices"), null, null, new String[]{"android_id"}, null);
classes:com/google/android/gms/internal/clearcut/f2.java:24:    public static final Uri f2846a = Uri.parse("content://com.google.android.gsf.gservices");
classes:com/google/android/gms/internal/clearcut/f2.java:27:    public static final Uri f2847b = Uri.parse("content://com.google.android.gsf.gservices/prefix");
```

### advertising_id — 0 hits in 0 files


```
```

### install_referrer — 0 hits in 0 files


```
```

### sensors — 0 hits in 0 files


```
```

### accounts — 6 hits in 1 files

- `classes:org/telegram/messenger/ContactsController.java` (6)

```
classes:org/telegram/messenger/ContactsController.java:754:        AccountManager accountManager = AccountManager.get(ApplicationLoader.applicationContext);
classes:org/telegram/messenger/ContactsController.java:756:            Account[] accountsByType = accountManager.getAccountsByType(BuildConfig.LIBRARY_PACKAGE_NAME);
classes:org/telegram/messenger/ContactsController.java:834:        AccountManager accountManager = AccountManager.get(ApplicationLoader.applicationContext);
classes:org/telegram/messenger/ContactsController.java:836:            Account[] accountsByType = accountManager.getAccountsByType(BuildConfig.LIBRARY_PACKAGE_NAME);
classes:org/telegram/messenger/ContactsController.java:2763:            AccountManager accountManager = AccountManager.get(ApplicationLoader.applicationContext);
classes:org/telegram/messenger/ContactsController.java:2764:            Account[] accountsByType = accountManager.getAccountsByType(BuildConfig.LIBRARY_PACKAGE_NAME);
```

### battery_state — 0 hits in 0 files


```
```

### screen_capture_detect — 2 hits in 1 files

- `classes:org/telegram/messenger/PushListenerController.java` (2)

```
classes:org/telegram/messenger/PushListenerController.java:193:            case "REACT_SCREENSHOT":
classes:org/telegram/messenger/PushListenerController.java:2874:                                                                                                if (string7.equals("MESSAGE_SCREENSHOT")) {
```

### audio_capture — 7 hits in 6 files

- `classes:org/telegram/messenger/MediaController.java` (2)
- `classes:org/telegram/messenger/camera/CameraView.java` (1)
- `classes3:org/telegram/ui/Components/b70.java` (1)
- `classes4:ch/n.java` (1)
- `classes4:org/webrtc/voiceengine/WebRtcAudioRecord.java` (1)
- `classes4:org/webrtc/audio/WebRtcAudioRecord.java` (1)

```
classes:org/telegram/messenger/MediaController.java:5408:            this.audioRecorder = new AudioRecord(0, this.sampleRate, 16, 2, this.recordBufferSize);
classes:org/telegram/messenger/MediaController.java:5698:        this.audioRecorder = new AudioRecord(0, this.sampleRate, 16, 2, this.recordBufferSize);
classes:org/telegram/messenger/camera/CameraView.java:1938:                AudioRecord audioRecord = new AudioRecord(0, CameraView.audioSampleRate, 16, 2, i10);
classes3:org/telegram/ui/Components/b70.java:164:            AudioRecord audioRecord = new AudioRecord(0, 48000, 16, 2, i2);
classes4:ch/n.java:104:        AudioRecord audioRecord = new AudioRecord(5, 48000, 16, 2, iMax);
classes4:org/webrtc/voiceengine/WebRtcAudioRecord.java:247:                    this.audioRecord = new AudioRecord(audioSource, i, iChannelCountToConfiguration, 2, iMax);
classes4:org/webrtc/audio/WebRtcAudioRecord.java:148:        return new AudioRecord(i, i2, i3, i4, i5);
```

### accessibility — 58 hits in 19 files

- `classes:i1/b.java` (5)
- `classes:org/telegram/messenger/AndroidUtilities.java` (5)
- `classes3:org/telegram/ui/PhotoViewer.java` (5)
- `classes3:org/telegram/ui/Components/ChatActivityEnterView.java` (5)
- `classes:org/telegram/ui/Components/voip/c.java` (4)
- `classes:androidx/recyclerview/widget/RecyclerView.java` (4)
- `classes3:org/telegram/ui/uj1.java` (4)
- `classes:i1/a.java` (3)
- `classes:androidx/mediarouter/app/u.java` (3)
- `classes:l/r3.java` (3)
- `classes3:org/telegram/ui/Components/me0.java` (3)
- `classes:q0/j0.java` (2)

```
classes:i1/a.java:5:import android.view.accessibility.AccessibilityManager;
classes:i1/a.java:57:            AccessibilityManager accessibilityManager = bVar.f6646h;
classes:i1/a.java:58:            if (accessibilityManager.isEnabled() && accessibilityManager.isTouchExplorationEnabled() && (i13 = bVar.f6649k) != i10) {
classes:i1/b.java:8:import android.view.accessibility.AccessibilityManager;
classes:i1/b.java:24:    public final AccessibilityManager f6646h;
classes:i1/b.java:51:        this.f6646h = (AccessibilityManager) view.getContext().getSystemService("accessibility");
classes:i1/b.java:99:        AccessibilityManager accessibilityManager = this.f6646h;
classes:i1/b.java:100:        if (!accessibilityManager.isEnabled() || !accessibilityManager.isTouchExplorationEnabled()) {
classes:org/telegram/ui/Components/voip/c.java:10:import android.view.accessibility.AccessibilityManager;
classes:org/telegram/ui/Components/voip/c.java:23:    public final AccessibilityManager d;
classes:org/telegram/ui/Components/voip/c.java:36:        this.d = (AccessibilityManager) eVar.getContext().getSystemService(AccessibilityManager.class);
classes:org/telegram/ui/Components/voip/c.java:42:        if (!this.d.isTouchExplorationEnabled() || (parent = (view = this.f12856a).getParent()) == null) {
```

### root_emulator — 2 hits in 2 files

- `classes:org/telegram/messenger/EmuDetector.java` (1)
- `classes:org/telegram/messenger/LinkifyPort.java` (1)

```
classes:org/telegram/messenger/EmuDetector.java:38:    private static final Property[] PROPERTIES = {new Property("init.svc.qemud", null), new Property("init.svc.qemu-props", null), new Property("qemu.hw.mainkeys", null), new Property("qemu.sf.fake_camera", null), new Property("qemu.sf.lcd_density",
classes:org/telegram/messenger/LinkifyPort.java:30:    private static String IANA_TOP_LEVEL_DOMAINS = "(?:(?:aaa|adnl|aarp|abb|abbott|abogado|academy|accenture|accountant|accountants|aco|active|actor|ads|adult|aeg|aero|afl|agency|aig|airforce|airtel|allfinanz|alsace|amica|amsterdam|android|apartment
```

### js_bridge — 11 hits in 10 files

- `classes4:org/telegram/ui/web/c1.java` (2)
- `classes:com/google/android/recaptcha/internal/zzlf.java` (1)
- `classes:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java` (1)
- `classes3:org/telegram/ui/qk1.java` (1)
- `classes3:org/telegram/ui/x1.java` (1)
- `classes3:org/telegram/ui/lp0.java` (1)
- `classes3:org/telegram/ui/PhotoViewer.java` (1)
- `classes3:org/telegram/ui/Components/pv.java` (1)
- `classes3:org/telegram/ui/Components/ab1.java` (1)
- `classes4:org/telegram/ui/web/b2.java` (1)

```
classes:com/google/android/recaptcha/internal/zzlf.java:62:                    ((WebView) obj).addJavascriptInterface(zzlyVar2.zzr(), "RN");
classes:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java:38:        public void addJavascriptInterface(Object obj, String str, List<String> list) {
classes3:org/telegram/ui/qk1.java:138:        this.a.addJavascriptInterface(new pk1(this), "TelegramWebviewProxy");
classes3:org/telegram/ui/x1.java:59:        w1Var.addJavascriptInterface(new ArticleViewer$BlockEmbedCell$TelegramWebviewProxy(this), "TelegramWebviewProxy");
classes3:org/telegram/ui/lp0.java:1984:                    this.w.addJavascriptInterface(new PaymentFormActivity$TelegramWebviewProxy(this), "TelegramWebviewProxy");
classes3:org/telegram/ui/PhotoViewer.java:1510:                    mvVar.addJavascriptInterface(new org.telegram.ui.Components.ih0(xu0Var), "YoutubeProxy");
classes3:org/telegram/ui/Components/pv.java:83:            mvVar.addJavascriptInterface(new rv(svVar), "YoutubeProxy");
classes3:org/telegram/ui/Components/ab1.java:125:        ta1Var.addJavascriptInterface(new Object(j91Var) { // from class: org.telegram.ui.Components.WebPlayerView$JavaScriptInterface
classes4:org/telegram/ui/web/b2.java:83:                                webView.addJavascriptInterface(new Object() { // from class: org.telegram.ui.web.WebInstantView$4
classes4:org/telegram/ui/web/c1.java:2816:                y0Var4.addJavascriptInterface(botWebViewContainer$WebViewProxy2, "TelegramWebviewProxy");
classes4:org/telegram/ui/web/c1.java:2818:                this.a.addJavascriptInterface(botWebViewContainer$WebViewProxy, "TelegramWebviewProxy");
```

### boot_persist — 2 hits in 2 files

- `classes:org/telegram/messenger/AppStartReceiver.java` (1)
- `classes:org/telegram/messenger/XiaomiUtilities.java` (1)

```
classes:org/telegram/messenger/AppStartReceiver.java:22:        if (intent == null || !"android.intent.action.BOOT_COMPLETED".equals(intent.getAction())) {
classes:org/telegram/messenger/XiaomiUtilities.java:15:    public static final int OP_BOOT_COMPLETED = 10007;
```

### full_screen_intent — 5 hits in 5 files

- `classes:org/telegram/messenger/voip/VoIPPreNotificationService.java` (1)
- `classes:org/telegram/messenger/voip/VoIPService.java` (1)
- `classes:org/telegram/messenger/voip/VoIPGroupNotification.java` (1)
- `classes:d0/h0.java` (1)
- `classes3:org/telegram/ui/kw.java` (1)

```
classes:org/telegram/messenger/voip/VoIPPreNotificationService.java:439:        contentIntent.setFullScreenIntent(PendingIntent.getActivity(context, i12, action, 33554432), true);
classes:org/telegram/messenger/voip/VoIPService.java:3805:        contentIntent.setFullScreenIntent(PendingIntent.getActivity(this, i11, intent, 33554432), true);
classes:org/telegram/messenger/voip/VoIPGroupNotification.java:385:        contentIntent.setFullScreenIntent(PendingIntent.getActivity(context, i13, intent, 33554432), true);
classes:d0/h0.java:375:        ((Notification.Builder) this.f3742c).setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notificatio [... omitted end
classes3:org/telegram/ui/kw.java:242:                Intent intent2 = new Intent("android.settings.MANAGE_APP_USE_FULL_SCREEN_INTENT");
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 270 hits in 201 files

- `classes3:org/telegram/ui/do0.java` (9)
- `classes3:org/telegram/ui/Components/EditTextBoldCursor.java` (7)
- `classes3:org/telegram/ui/lp0.java` (6)
- `classes:org/telegram/messenger/FactCheckController.java` (4)
- `classes3:org/telegram/ui/Components/kl.java` (4)
- `classes3:org/telegram/ui/Components/ChatActivityEnterView.java` (4)
- `classes:pg/j4.java` (3)
- `classes:pg/i4.java` (3)
- `classes3:org/telegram/ui/i31.java` (3)
- `classes3:org/telegram/ui/PasscodeActivity.java` (3)
- `classes3:org/telegram/ui/hi1.java` (3)
- `classes:ng/q.java` (2)

```
classes:l1/i.java:52:    public final void onTextChanged(CharSequence charSequence, int i10, int i11, int i12) {
classes:org/telegram/messenger/FactCheckController.java:504:            public void onTextChanged(CharSequence charSequence, int i11, int i12, int i13) {
classes:org/telegram/messenger/FactCheckController.java:505:                super/*org.telegram.ui.Components.EditTextBoldCursor*/.onTextChanged(charSequence, i11, i12, i13);
classes:org/telegram/messenger/FactCheckController.java:573:        yuVar.addTextChangedListener(new TextWatcher() { // from class: org.telegram.messenger.FactCheckController.3
classes:org/telegram/messenger/FactCheckController.java:608:            public void onTextChanged(CharSequence charSequence, int i11, int i12, int i13) {
classes:pe/g0.java:72:    public final void onTextChanged(CharSequence charSequence, int i10, int i11, int i12) {
classes:ig/f.java:101:        bVar.addTextChangedListener(new c(this, 0));
classes:pg/d2.java:42:    public final void onTextChanged(CharSequence charSequence, int i10, int i11, int i12) {
classes:ig/c.java:472:    public final void onTextChanged(CharSequence charSequence, int i10, int i11, int i12) {
classes:pg/j4.java:204:            yuVar.addTextChangedListener(new gf.y(strArr, i3Var, false, 8));
classes:pg/j4.java:249:            yuVar.addTextChangedListener(new gf.y(strArr, g3Var, false, 9));
classes:pg/j4.java:294:            yuVar.addTextChangedListener(new gf.y(strArr, h3Var, false, 10));
```

### webview_tracking — 7 hits in 6 files

- `classes3:org/telegram/ui/lp0.java` (2)
- `classes3:org/telegram/ui/qk1.java` (1)
- `classes3:org/telegram/ui/x1.java` (1)
- `classes3:org/telegram/ui/xu0.java` (1)
- `classes3:org/telegram/ui/Components/sv.java` (1)
- `classes4:org/telegram/ui/web/c1.java` (1)

```
classes3:org/telegram/ui/qk1.java:137:        CookieManager.getInstance().setAcceptThirdPartyCookies(this.a, true);
classes3:org/telegram/ui/x1.java:61:        CookieManager.getInstance().setAcceptThirdPartyCookies(w1Var, true);
classes3:org/telegram/ui/xu0.java:38:        CookieManager.getInstance().setAcceptThirdPartyCookies(mvVar, true);
classes3:org/telegram/ui/lp0.java:1983:                    CookieManager.getInstance().setAcceptThirdPartyCookies(this.w, true);
classes3:org/telegram/ui/lp0.java:2888:                            CookieManager.getInstance().setAcceptThirdPartyCookies(this.w, true);
classes3:org/telegram/ui/Components/sv.java:123:        CookieManager.getInstance().setAcceptThirdPartyCookies(mvVar, true);
classes4:org/telegram/ui/web/c1.java:2709:            cookieManager.setAcceptThirdPartyCookies(this.a, true);
```

### streaks — 3 hits in 1 files

- `classes3:org/telegram/tgnet/TLRPC.java` (3)

```
classes3:org/telegram/tgnet/TLRPC.java:28783:        public int current_streak;
classes3:org/telegram/tgnet/TLRPC.java:28795:            this.current_streak = inputSerializedData.readInt32(z);
classes3:org/telegram/tgnet/TLRPC.java:28808:            outputSerializedData.writeInt32(this.current_streak);
```

### reengagement — 1171 hits in 270 files

- `classes3:org/telegram/ui/Cells/u1.java` (53)
- `classes:org/telegram/messenger/MessagesController.java` (51)
- `classes:org/telegram/messenger/ChatObject.java` (37)
- `classes:org/telegram/messenger/MessageObject.java` (23)
- `classes:org/telegram/messenger/RichMessageLayout.java` (21)
- `classes:bb/f.java` (20)
- `classes:org/telegram/messenger/LocationController.java` (19)
- `classes:e2/i.java` (18)
- `classes4:ch/s.java` (18)
- `classes:v2/a.java` (17)
- `classes4:org/telegram/ui/Wallet/f3.java` (17)
- `classes:org/telegram/messenger/ImageLoader.java` (14)

```
classes:h4/m1.java:41:        this(i10, Bundle.EMPTY, SystemClock.elapsedRealtime(), null);
classes:h4/m1.java:48:        long j9 = bundle.getLong(g, SystemClock.elapsedRealtime());
classes:h4/g1.java:196:        return new l1(N0(), zP0 && n(), SystemClock.elapsedRealtime(), zP0 ? getDuration() : -9223372036854775807L, zP0 ? f0() : 0L, zP0 ? y() : 0, zP0 ? p() : 0L, zP0 ? o() : -9223372036854775807L, zP0 ? A() : -9223372036854775807L, zP0 ? D0() : 0L);
classes:h4/l0.java:448:        long jElapsedRealtime = SystemClock.elapsedRealtime();
classes:h4/l0.java:497:        return new i4.f0(i11, jK0, jF0, f11, j12, i12, message, jElapsedRealtime, arrayList, j9, bundle2);
classes:h4/b0.java:130:        Uri uriBuild = new Uri.Builder().scheme(b0.class.getName()).appendPath("pip-media-session").appendPath(String.valueOf(SystemClock.elapsedRealtime())).build();
classes:va/a.java:56:        long jElapsedRealtime = SystemClock.elapsedRealtime();
classes:va/a.java:75:        long jElapsedRealtime2 = SystemClock.elapsedRealtime() - jElapsedRealtime;
classes:va/a.java:78:        long jElapsedRealtime3 = SystemClock.elapsedRealtime();
classes:va/a.java:86:            if (jElapsedRealtime3 - ((Long) map.get(j7Var)).longValue() <= TimeUnit.SECONDS.toMillis(30L)) {
classes:va/a.java:90:        map.put(j7Var, Long.valueOf(jElapsedRealtime3));
classes:va/a.java:97:        s3Var.f8315a = Long.valueOf(Long.MAX_VALUE & jElapsedRealtime2);
```

### notif_permission_nag — 0 hits in 0 files


```
```

### cancellation_retention — 0 hits in 0 files


```
```

### urgency_countdown — 655 hits in 110 files

- `classes:org/telegram/messenger/MessagesStorage.java` (103)
- `classes:org/telegram/messenger/FilePathDatabase.java` (26)
- `classes:org/telegram/messenger/PushListenerController.java` (19)
- `classes:pe/e.java` (18)
- `classes3:org/telegram/ui/ic.java` (18)
- `classes3:org/telegram/ui/p5.java` (18)
- `classes:org/telegram/messenger/MediaDataController.java` (16)
- `classes3:org/telegram/ui/oo.java` (16)
- `classes:org/telegram/messenger/FileStreamLoadOperation.java` (15)
- `classes:org/telegram/messenger/AnimatedFileDrawableStream.java` (15)
- `classes:org/telegram/messenger/FileLoadOperation.java` (12)
- `classes:org/telegram/messenger/AndroidUtilities.java` (12)

```
classes:y9/c.java:134:                    } else if (strNextName2.equals("expiresIn")) {
classes:y9/c.java:162:            } else if (strNextName.equals("expiresIn")) {
classes:d2/f1.java:30:import java.util.concurrent.CountDownLatch;
classes:d2/f1.java:265:                ((MessagesStorage) this.f3896c).lambda$getSentFile$164((String) this.d, this.f3895b, (Object[]) this.f3897e, (CountDownLatch) this.f3898f);
classes:a1/c.java:47:import java.util.concurrent.CountDownLatch;
classes:a1/c.java:431:                CountDownLatch countDownLatch = (CountDownLatch) this.f11c;
classes:a1/c.java:443:                    countDownLatch.countDown();
classes:pg/d0.java:255:                    dVar.f(LocaleController.formatString(R.string.Gift2AuctionTimeLeft, LocaleController.formatTTLString(this.f13985c0.auctionStateActive.end_date - currentTime)), false);
classes:pg/a5.java:754:                dVar.f(LocaleController.formatString(R.string.Gift2AuctionTimeLeft, LocaleController.formatTTLString(i12)), z9);
classes:pg/w.java:519:                dVar.f(LocaleController.formatString(R.string.Gift2AuctionTimeLeft, LocaleController.formatTTLString(this.l0.auctionStateActive.end_date - currentTime)), z9);
classes:x9/a.java:120:        sb2.append(", expiresInSecs=");
classes:x9/b.java:82:            jSONObject.put("ExpiresInSecs", aVar.f18938e);
```

### infinite_autoplay — 139 hits in 33 files

- `classes:org/telegram/messenger/ImageLoader.java` (28)
- `classes:org/telegram/messenger/RichMessageLayout.java` (15)
- `classes3:org/telegram/ui/Cells/u1.java` (12)
- `classes:org/telegram/messenger/R.java` (9)
- `classes3:org/telegram/ui/ed0.java` (7)
- `classes3:org/telegram/ui/c21.java` (7)
- `classes3:org/telegram/ui/Cells/f2.java` (7)
- `classes:org/telegram/messenger/LiteMode.java` (6)
- `classes3:org/telegram/tgnet/tl/TL_iv.java` (5)
- `classes3:org/telegram/ui/dv.java` (5)
- `classes:org/telegram/messenger/LocaleController.java` (4)
- `classes:org/telegram/messenger/SharedConfig.java` (4)

```
classes:x5/o.java:79:        if (jSONObject.has("autoplay") && this.f18874c != (z10 = jSONObject.getBoolean("autoplay"))) {
classes:x5/o.java:145:            jSONObject.put("autoplay", this.f18874c);
classes:org/telegram/messenger/LocaleController.java:572:        addRules(new String[]{"bem", "brx", "da", "de", "el", "en", "eo", "es", "et", "fi", "fo", ImageLoader.AUTOPLAY_FILTER_NONLOOP, "he", "iw", "it", "nb", "nl", "nn", "no", "sv", "af", "bg", "bn", "ca", "eu", "fur", "fy", "gu", "ha", "is",
classes:org/telegram/messenger/LocaleController.java:4496:            this.ruTranslitChars.put("г", ImageLoader.AUTOPLAY_FILTER);
classes:org/telegram/messenger/LocaleController.java:4500:            str7 = ImageLoader.AUTOPLAY_FILTER;
classes:org/telegram/messenger/LocaleController.java:4542:            str7 = ImageLoader.AUTOPLAY_FILTER;
classes:org/telegram/messenger/MessageObject.java:1059:    public static boolean canAutoplayAnimatedSticker(TLRPC.Document document) {
classes:org/telegram/messenger/MessageObject.java:2396:            groupSpan = new SpannableStringBuilder(ImageLoader.AUTOPLAY_FILTER);
classes:org/telegram/messenger/VideoEditedInfo.java:116:    public boolean canAutoPlaySourceVideo() {
classes:org/telegram/messenger/ImageLoader.java:89:    public static final String AUTOPLAY_FILTER = "g";
classes:org/telegram/messenger/ImageLoader.java:90:    public static final String AUTOPLAY_FILTER_NONLOOP = "gl";
classes:org/telegram/messenger/ImageLoader.java:1682:                        if (ImageLoader.this.isAnimatedAvatar(this.cacheImage.filter) || ImageLoader.AUTOPLAY_FILTER.equals(this.cacheImage.filter) || ImageLoader.AUTOPLAY_FILTER_NONLOOP.equals(this.cacheImage.filter)) {
```

### badges — 12 hits in 3 files

- `classes:org/telegram/messenger/NotificationBadge.java` (10)
- `classes:d0/h0.java` (1)
- `classes:s6/a.java` (1)

```
classes:org/telegram/messenger/NotificationBadge.java:92:        private static final String INTENT_EXTRA_ACTIVITY_NAME = "badge_count_class_name";
classes:org/telegram/messenger/NotificationBadge.java:93:        private static final String INTENT_EXTRA_BADGE_COUNT = "badge_count";
classes:org/telegram/messenger/NotificationBadge.java:94:        private static final String INTENT_EXTRA_PACKAGENAME = "badge_count_package_name";
classes:org/telegram/messenger/NotificationBadge.java:129:        private static final String INTENT_EXTRA_ACTIVITY_NAME = "badge_count_class_name";
classes:org/telegram/messenger/NotificationBadge.java:130:        private static final String INTENT_EXTRA_BADGE_COUNT = "badge_count";
classes:org/telegram/messenger/NotificationBadge.java:131:        private static final String INTENT_EXTRA_PACKAGENAME = "badge_count_package_name";
classes:org/telegram/messenger/NotificationBadge.java:239:        private static final String INTENT_EXTRA_BADGEUPGRADE_COUNT = "app_badge_count";
classes:org/telegram/messenger/NotificationBadge.java:282:            contentValues.put("badgecount", Integer.valueOf(i10));
classes:org/telegram/messenger/NotificationBadge.java:334:        private static final String PROVIDER_COLUMNS_BADGE_COUNT = "badge_count";
classes:org/telegram/messenger/NotificationBadge.java:471:            AndroidUtilities.runOnUIThread(new oh(0, this, d2.r1.h(i10, "app_badge_count")));
classes:d0/h0.java:375:        ((Notification.Builder) this.f3742c).setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notificatio [... omitted end
classes:s6/a.java:64:        builder.setBadgeIconType(0);
```

### minors_age — 16 hits in 6 files

- `classes:org/telegram/messenger/R.java` (7)
- `classes3:org/telegram/ui/ThemeActivity.java` (5)
- `classes:org/telegram/messenger/MessagesController.java` (1)
- `classes3:org/telegram/ui/oc1.java` (1)
- `classes3:org/telegram/ui/Components/aj.java` (1)
- `classes4:ah/m.java` (1)

```
classes:org/telegram/messenger/R.java:2922:        public static int AgeVerificationButton = 0x7f0ffd49;
classes:org/telegram/messenger/R.java:2923:        public static int AgeVerificationFailedText = 0x7f0ffd48;
classes:org/telegram/messenger/R.java:2924:        public static int AgeVerificationFailedTitle = 0x7f0ffd47;
classes:org/telegram/messenger/R.java:2925:        public static int AgeVerificationNeedCameraPermission = 0x7f0ffd46;
classes:org/telegram/messenger/R.java:2926:        public static int AgeVerificationPassedTitle = 0x7f0ffd45;
classes:org/telegram/messenger/R.java:2927:        public static int AgeVerificationTextGB = 0x7f0ffd44;
classes:org/telegram/messenger/R.java:2928:        public static int AgeVerificationTitle = 0x7f0ffd43;
classes:org/telegram/messenger/MessagesController.java:11474:                org.telegram.ui.Components.xc.a0(s2VarT).M(LocaleController.getString(R.string.AgeVerificationFailedTitle), LocaleController.getString(R.string.AgeVerificationFailedText), R.raw.error).j();
classes3:org/telegram/ui/oc1.java:52:                    org.telegram.ui.Components.xc.a0(themeActivity).M(LocaleController.getString(R.string.AgeVerificationFailedTitle), LocaleController.getString(R.string.AgeVerificationFailedText), R.raw.error).j();
classes3:org/telegram/ui/ThemeActivity.java:272:        org.telegram.messenger.mi.j(R.string.AgeVerificationTitle, textViewB, 17);
classes3:org/telegram/ui/ThemeActivity.java:275:        textViewB2.setText(AndroidUtilities.replaceTags(LocaleController.getString("AgeVerificationText" + str2)));
classes3:org/telegram/ui/ThemeActivity.java:279:        dVar.g(LocaleController.getString(R.string.AgeVerificationButton), false, true);
```

### screen_time — 0 hits in 0 files


```
```

## UI string categories (default locale)

### loss_aversion_copy — 0 strings

```
```

### urgency_copy — 0 strings

```
```

### confirmshaming_copy — 0 strings

```
```

### social_pressure_copy — 1 strings

```
strings.xml:66:    <string name="firebase_database_url">https://tmessages2.firebaseio.com</string>
```

### guilt_copy — 0 strings

```
```

### subscription_copy — 0 strings

```
```

### data_copy — 0 strings

```
```

