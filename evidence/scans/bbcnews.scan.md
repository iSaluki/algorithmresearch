# Pattern scan: work/bbcnews/jdex

## Code categories (library packages excluded)

### installed_apps — 20 hits in 15 files

- `classes5:defpackage/s86.java` (3)
- `classes3:defpackage/ta7.java` (2)
- `classes4:defpackage/ux3.java` (2)
- `classes5:defpackage/yx3.java` (2)
- `classes:defpackage/byh.java` (1)
- `classes:defpackage/odd.java` (1)
- `classes3:defpackage/fwi.java` (1)
- `classes3:defpackage/ab1$a.java` (1)
- `classes3:defpackage/htk.java` (1)
- `classes3:com/android/installreferrer/api/InstallReferrerClientImpl.java` (1)
- `classes3:com/appsflyer/internal/AFb1vSDK.java` (1)
- `classes3:com/appsflyer/internal/AFa1tSDK.java` (1)

```
classes:defpackage/byh.java:92:                for (ResolveInfo resolveInfo : packageManager.queryIntentActivities(a(), 0)) {
classes:defpackage/odd.java:29:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(a.c(), 0);
classes3:defpackage/fwi.java:15:            return za7.a(context).b(context.getPackageManager().getPackageInfo("com.google.android.gms", 64));
classes3:defpackage/ta7.java:114:                packageInfo = packageManager.getPackageInfo("com.android.vending", Build.VERSION.SDK_INT >= 28 ? 134225984 : 8256);
classes3:defpackage/ta7.java:122:            PackageInfo packageInfo2 = packageManager.getPackageInfo("com.google.android.gms", Build.VERSION.SDK_INT >= 28 ? 134217792 : 64);
classes3:defpackage/ab1$a.java:41:        return r1.getPackageInfo("com.google.android.gms", 0).versionCode;
classes3:defpackage/htk.java:20:                    Signature[] signatureArr = context.getPackageManager().getPackageInfo("com.android.vending", 64).signatures;
classes3:com/android/installreferrer/api/InstallReferrerClientImpl.java:70:        return this.b.getPackageManager().getPackageInfo("com.android.vending", 128).versionCode >= 80837300;
classes3:com/appsflyer/internal/AFb1vSDK.java:85:        context.getPackageManager().getPackageInfo("com.android.vending", 0);
classes3:com/appsflyer/internal/AFa1tSDK.java:351:            context.getPackageManager().getPackageInfo("com.google.android.gms", 0);
classes4:defpackage/ih0.java:57:        List<ResolveInfo> listQueryIntentActivities = this.a.getPackageManager().queryIntentActivities(intent, 65536);
classes4:defpackage/ux3.java:67:        List<ResolveInfo> listQueryIntentActivities = this.a.queryIntentActivities(this.b, 65536);
```

### usage_stats — 0 hits in 0 files


```
```

### clipboard — 2 hits in 2 files

- `classes:defpackage/xd0.java` (1)
- `classes:defpackage/hs.java` (1)

```
classes:defpackage/xd0.java:67:        ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
classes:defpackage/hs.java:29:        ClipData primaryClip = c().getPrimaryClip();
```

### contacts — 3 hits in 1 files

- `classes3:defpackage/a3h.java` (3)

```
classes3:defpackage/a3h.java:7:import android.provider.ContactsContract;
classes3:defpackage/a3h.java:64:        Uri uriLookupContact = ContactsContract.Contacts.lookupContact(contentResolver, uri);
classes3:defpackage/a3h.java:72:        return ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uri, true);
```

### call_log — 0 hits in 0 files


```
```

### sms — 0 hits in 0 files


```
```

### location — 3 hits in 2 files

- `classes4:dotmetrics/analytics/DotmetricsSession.java` (2)
- `classes:defpackage/nmi.java` (1)

```
classes:defpackage/nmi.java:48:                return this.b.getLastKnownLocation(str);
classes4:dotmetrics/analytics/DotmetricsSession.java:347:                            lastKnownLocation = locationManager.getLastKnownLocation("gps");
classes4:dotmetrics/analytics/DotmetricsSession.java:358:                    Location lastKnownLocation2 = context.getPackageManager().checkPermission("android.permission.ACCESS_COARSE_LOCATION", context.getPackageName()) == 0 ? locationManager.getLastKnownLocation("network") : null;
```

### wifi_bt_scan — 0 hits in 0 files


```
```

### device_ids — 63 hits in 26 files

- `classes3:com/amazonaws/services/cognitosync/model/RegisterDeviceResult.java` (6)
- `classes3:com/amazonaws/services/cognitosync/model/UnsubscribeFromDatasetRequest.java` (6)
- `classes3:com/amazonaws/services/cognitosync/model/SubscribeToDatasetRequest.java` (6)
- `classes3:com/amazonaws/services/cognitosync/model/UpdateRecordsRequest.java` (6)
- `classes4:de/spring/mobile/SpringStreamsBase.java` (6)
- `classes:androidx/core/widget/NestedScrollView.java` (3)
- `classes:defpackage/a35.java` (3)
- `classes3:com/appsflyer/internal/AFg1oSDK.java` (3)
- `classes:androidx/compose/ui/platform/b.java` (2)
- `classes3:com/amazonaws/mobileconnectors/cognito/CognitoSyncManager.java` (2)
- `classes3:com/amazonaws/services/cognitosync/model/transform/UpdateRecordsRequestMarshaller.java` (2)
- `classes3:com/appsflyer/internal/AFd1kSDK.java` (2)

```
classes:androidx/core/widget/NestedScrollView.java:481:            getScrollFeedbackProvider().c(motionEvent.getDeviceId(), motionEvent.getSource(), i2, scrollY2);
classes:androidx/core/widget/NestedScrollView.java:493:                    getScrollFeedbackProvider().b(motionEvent.getDeviceId(), motionEvent.getSource(), i2, true);
classes:androidx/core/widget/NestedScrollView.java:502:                getScrollFeedbackProvider().b(motionEvent.getDeviceId(), motionEvent.getSource(), i2, false);
classes:androidx/compose/ui/platform/b.java:1046:        MotionEvent motionEventObtain = MotionEvent.obtain(motionEvent.getDownTime() == motionEvent.getEventTime() ? j2 : motionEvent.getDownTime(), j2, i2, pointerCount, pointerPropertiesArr, pointerCoordsArr, motionEvent.getMetaState(), z ? 0 : moti
classes:androidx/compose/ui/platform/b.java:1634:        return getFocusOwner().z(new dve(pij.j(viewConfiguration, getContext()) * f2, f2 * pij.f(viewConfiguration, getContext()), motionEvent.getEventTime(), motionEvent.getDeviceId()), new Function0() { // from class: xs
classes:defpackage/qxj.java:623:        menuE.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
classes:defpackage/bd0.java:1357:            boolean z2 = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;
classes:defpackage/o5i.java:240:        menuA.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
classes:defpackage/a35.java:45:        iArr[0] = pij.i(context, viewConfiguration, motionEvent.getDeviceId(), i, motionEvent.getSource());
classes:defpackage/a35.java:46:        iArr[1] = pij.h(context, viewConfiguration, motionEvent.getDeviceId(), i, motionEvent.getSource());
classes:defpackage/a35.java:57:        int deviceId = motionEvent.getDeviceId();
classes3:com/atinternet/tracker/TechnicalContext.java:434:                        return Settings.Secure.getString(appContext.getContentResolver(), "android_id");
```

### gsf_id — 0 hits in 0 files


```
```

### advertising_id — 24 hits in 7 files

- `classes3:com/atinternet/tracker/TechnicalContext.java` (10)
- `classes3:com/appsflyer/internal/AFe1eSDK.java` (3)
- `classes3:com/appsflyer/internal/w.java` (3)
- `classes4:dotmetrics/analytics/DatapointHelper.java` (3)
- `classes3:com/appsflyer/internal/v.java` (2)
- `classes3:com/appsflyer/internal/AFf1zSDK.java` (2)
- `classes4:de/spring/mobile/SpringStreamsBase.java` (1)

```
classes3:com/appsflyer/internal/v.java:3:import android.adservices.measurement.MeasurementManager;
classes3:com/appsflyer/internal/v.java:9:        return MeasurementManager.class;
classes3:com/appsflyer/internal/AFf1zSDK.java:3:import android.adservices.measurement.MeasurementManager;
classes3:com/appsflyer/internal/AFf1zSDK.java:110:        MeasurementManager measurementManagerA;
classes3:com/appsflyer/internal/AFe1eSDK.java:10:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
classes3:com/appsflyer/internal/AFe1eSDK.java:210:            Class.forName("com.google.android.gms.ads.identifier.AdvertisingIdClient");
classes3:com/appsflyer/internal/AFe1eSDK.java:211:            AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(p0);
classes3:com/atinternet/tracker/TechnicalContext.java:23:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
classes3:com/atinternet/tracker/TechnicalContext.java:24:import com.huawei.hms.ads.identifier.AdvertisingIdClient;
classes3:com/atinternet/tracker/TechnicalContext.java:386:                        if (Tool.isClassAvailable("com.google.android.gms.ads.identifier.AdvertisingIdClient")) {
classes3:com/atinternet/tracker/TechnicalContext.java:388:                                AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(appContext);
classes3:com/atinternet/tracker/TechnicalContext.java:396:                        if (Tool.isClassAvailable("com.huawei.hms.ads.identifier.AdvertisingIdClient")) {
```

### install_referrer — 383 hits in 146 files

- `classes3:com/android/installreferrer/api/InstallReferrerClientImpl.java` (24)
- `classes3:com/appsflyer/internal/AFi1aSDK.java` (12)
- `classes3:com/appsflyer/AFLogger.java` (11)
- `classes3:defpackage/yla.java` (10)
- `classes3:com/appsflyer/internal/AFd1uSDK.java` (8)
- `classes3:com/appsflyer/internal/AFe1eSDK.java` (6)
- `classes3:com/appsflyer/internal/AFe1zSDK.java` (5)
- `classes3:com/appsflyer/internal/AFe1tSDK.java` (5)
- `classes3:com/appsflyer/internal/AFj1jSDK.java` (5)
- `classes3:com/android/installreferrer/api/InstallReferrerClient.java` (4)
- `classes3:com/appsflyer/internal/AFf1iSDK.java` (4)
- `classes3:defpackage/sj9.java` (4)

```
classes3:com/urbanairship/Airship.java:5:import com.android.installreferrer.api.InstallReferrerClient;
classes3:com/urbanairship/Airship.java:25:@Metadata(d1 = {"\u0000Î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u
classes3:com/urbanairship/AirshipConfigOptions.java:5:import com.android.installreferrer.api.InstallReferrerClient;
classes3:com/urbanairship/AirshipConfigOptions.java:28:@Metadata(d1 = {"\u0000x\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0010\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\b\u0003\n\u00
classes3:com/urbanairship/meteredusage/EventsDatabase.java:4:import com.android.installreferrer.api.InstallReferrerClient;
classes3:com/urbanairship/meteredusage/EventsDatabase.java:12:@Metadata(d1 = {"\u0000\u0014\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\b!\u0018\u0000 \u00072\u00020\u0001:\u0001\bB\u0007¢\u0006\u0004\b\u0002\u0010\u0003J\u000f\u0010\u0005\u001a\u00020
classes3:com/urbanairship/meteredusage/EventsDatabase_Impl.java:5:import com.android.installreferrer.api.InstallReferrerClient;
classes3:com/urbanairship/meteredusage/EventsDatabase_Impl.java:23:@Metadata(d1 = {"\u0000P\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010$\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\b\u0002\n\u0002\u0010\
classes3:com/urbanairship/modules/Module.java:3:import com.android.installreferrer.api.InstallReferrerClient;
classes3:com/urbanairship/modules/Module.java:10:@Metadata(d1 = {"\u0000\u001c\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0010\"\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0006\b\u0017\u0018\u0000 \r2\u00020\u0001:\u0001\u000eR\u001d\u0010\b\u001a\b\u0012\u0004\u0012\u0
classes3:com/urbanairship/UALog.java:3:import com.android.installreferrer.api.InstallReferrerClient;
classes3:com/urbanairship/UALog.java:23:@Metadata(d1 = {"\u0000V\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u0011\n\u0000\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u0010\u0003\n\u0002\b\b\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u
```

### sensors — 0 hits in 0 files


```
```

### accounts — 0 hits in 0 files


```
```

### battery_state — 0 hits in 0 files


```
```

### screen_capture_detect — 0 hits in 0 files


```
```

### audio_capture — 0 hits in 0 files


```
```

### accessibility — 140 hits in 29 files

- `classes:defpackage/zq9.java` (17)
- `classes5:defpackage/x9.java` (16)
- `classes3:com/google/android/material/behavior/HideBottomViewOnScrollBehavior.java` (9)
- `classes3:com/google/android/material/behavior/HideViewOnScrollBehavior.java` (9)
- `classes3:defpackage/yd5.java` (9)
- `classes:defpackage/zt.java` (8)
- `classes3:defpackage/j6a.java` (7)
- `classes3:com/google/android/material/textfield/a.java` (6)
- `classes:defpackage/q66.java` (5)
- `classes3:com/google/android/material/snackbar/BaseTransientBottomBar.java` (5)
- `classes4:defpackage/gq.java` (5)
- `classes:defpackage/db.java` (4)

```
classes:androidx/compose/ui/platform/b.java:2087:    public y9 getAccessibilityManager() {
classes:android/view/accessibility/AccessibilityManager$AccessibilityServicesStateChangeListener.java:4:public /* synthetic */ interface AccessibilityManager$AccessibilityServicesStateChangeListener {
classes:defpackage/cij.java:28:import android.view.accessibility.AccessibilityManager;
classes:defpackage/cij.java:547:        AccessibilityManager accessibilityManager = (AccessibilityManager) view.getContext().getSystemService("accessibility");
classes:defpackage/zq9.java:5:import android.view.accessibility.AccessibilityManager;
classes:defpackage/zq9.java:6:import android.view.accessibility.AccessibilityManager$AccessibilityServicesStateChangeListener;
classes:defpackage/zq9.java:12:public final class zq9 implements AccessibilityManager.AccessibilityStateChangeListener, fxg {
classes:defpackage/zq9.java:23:        public static final void a(AccessibilityManager accessibilityManager, AccessibilityManager$AccessibilityServicesStateChangeListener accessibilityManager$AccessibilityServicesStateChangeListener) {
classes:defpackage/zq9.java:27:        public static final void b(AccessibilityManager accessibilityManager, AccessibilityManager$AccessibilityServicesStateChangeListener accessibilityManager$AccessibilityServicesStateChangeListener) {
classes:defpackage/zq9.java:33:    public static final class b implements AccessibilityManager$AccessibilityServicesStateChangeListener {
classes:defpackage/zq9.java:59:        public void onAccessibilityServicesStateChanged(AccessibilityManager accessibilityManager) {
classes:defpackage/zq9.java:66:    public static final class c implements AccessibilityManager.TouchExplorationStateChangeListener {
```

### root_emulator — 153 hits in 50 files

- `classes4:com/appsflyer/R.java` (14)
- `classes3:com/amazonaws/services/s3/model/CORSRule.java` (9)
- `classes4:defpackage/h1e.java` (8)
- `classes4:defpackage/k1e.java` (8)
- `classes5:defpackage/z0e.java` (8)
- `classes5:defpackage/v0e.java` (8)
- `classes5:defpackage/y0e.java` (8)
- `classes5:defpackage/a1e.java` (8)
- `classes5:defpackage/b1e.java` (8)
- `classes5:defpackage/j1e.java` (8)
- `classes3:com/amazonaws/services/s3/model/transform/XmlResponsesSaxParser.java` (6)
- `classes3:com/appsflyer/internal/AFf1hSDK.java` (4)

```
classes3:com/google/android/material/textfield/TextInputLayout.java:787:        int dimensionPixelOffset2 = getResources().getDimensionPixelOffset(mud.mtrl_exposed_dropdown_menu_popup_vertical_padding);
classes3:com/amazonaws/services/s3/model/transform/BucketConfigurationXmlFactory.java:514:        if (cORSRule.getExposedHeaders() != null) {
classes3:com/amazonaws/services/s3/model/transform/BucketConfigurationXmlFactory.java:515:            Iterator<String> it3 = cORSRule.getExposedHeaders().iterator();
classes3:com/amazonaws/services/s3/model/transform/XmlResponsesSaxParser.java:198:        private List<String> exposedHeaders = null;
classes3:com/amazonaws/services/s3/model/transform/XmlResponsesSaxParser.java:208:                    this.currentRule.setExposedHeaders(this.exposedHeaders);
classes3:com/amazonaws/services/s3/model/transform/XmlResponsesSaxParser.java:212:                    this.exposedHeaders = null;
classes3:com/amazonaws/services/s3/model/transform/XmlResponsesSaxParser.java:235:                    this.exposedHeaders.add(getText());
classes3:com/amazonaws/services/s3/model/transform/XmlResponsesSaxParser.java:261:                    if (this.exposedHeaders == null) {
classes3:com/amazonaws/services/s3/model/transform/XmlResponsesSaxParser.java:262:                        this.exposedHeaders = new ArrayList();
classes3:com/amazonaws/services/s3/model/CORSRule.java:13:    private List<String> exposedHeaders;
classes3:com/amazonaws/services/s3/model/CORSRule.java:60:    public List<String> getExposedHeaders() {
classes3:com/amazonaws/services/s3/model/CORSRule.java:61:        return this.exposedHeaders;
```

### js_bridge — 1 hits in 1 files

- `classes4:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java` (1)

```
classes4:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java:45:        public void addJavascriptInterface(Object obj, String str, List<String> list) {
```

### boot_persist — 2 hits in 2 files

- `classes3:com/optimizely/ab/android/datafile_handler/DatafileRescheduler.java` (1)
- `classes3:com/optimizely/ab/android/event_handler/EventRescheduler.java` (1)

```
classes3:com/optimizely/ab/android/datafile_handler/DatafileRescheduler.java:64:        if (context == null || intent == null || !(intent.getAction().equals("android.intent.action.BOOT_COMPLETED") || intent.getAction().equals("android.intent.action.MY_PACKAGE_REPLACED"))) {
classes3:com/optimizely/ab/android/event_handler/EventRescheduler.java:18:        if (intent.getAction().equals("android.intent.action.BOOT_COMPLETED") || intent.getAction().equals("android.intent.action.MY_PACKAGE_REPLACED")) {
```

### full_screen_intent — 1 hits in 1 files

- `classes:defpackage/spb.java` (1)

```
classes:defpackage/spb.java:148:        builder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, fVar.j).setVibrate(notification.vibrate).setLights(notification.ledARGB, notification.led [... om
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 18 hits in 11 files

- `classes:defpackage/hrg.java` (3)
- `classes:defpackage/sc0.java` (2)
- `classes:defpackage/ge0.java` (2)
- `classes:androidx/appcompat/widget/SearchView.java` (2)
- `classes3:com/google/android/material/textfield/TextInputLayout.java` (2)
- `classes3:com/google/android/material/button/MaterialButton.java` (2)
- `classes:defpackage/oo5.java` (1)
- `classes:defpackage/fo5.java` (1)
- `classes3:com/google/android/material/textfield/a.java` (1)
- `classes3:com/google/android/material/timepicker/ChipTextInputComboView.java` (1)
- `classes3:defpackage/eyh.java` (1)

```
classes:defpackage/sc0.java:199:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:defpackage/sc0.java:200:        super.onTextChanged(charSequence, i, i2, i3);
classes:defpackage/ge0.java:331:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:defpackage/ge0.java:332:        super.onTextChanged(charSequence, i, i2, i3);
classes:androidx/appcompat/widget/SearchView.java:465:        searchAutoComplete.addTextChangedListener(this.E0);
classes:androidx/appcompat/widget/SearchView.java:1404:        public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:defpackage/oo5.java:93:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:defpackage/hrg.java:92:        public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:defpackage/hrg.java:93:            ((TextWatcher) this.b).onTextChanged(charSequence, i, i2, i3);
classes:defpackage/hrg.java:125:            ((a) this.d.get(i)).onTextChanged(this, 0, length(), length());
classes:defpackage/fo5.java:25:            editText.addTextChangedListener(oo5Var);
classes3:com/google/android/material/textfield/a.java:101:                a.this.J.addTextChangedListener(a.this.M);
```

### webview_tracking — 0 hits in 0 files


```
```

### streaks — 0 hits in 0 files


```
```

### reengagement — 453 hits in 128 files

- `classes4:com/appsflyer/R.java` (20)
- `classes:defpackage/taa.java` (12)
- `classes3:defpackage/s1e.java` (11)
- `classes4:defpackage/etd.java` (11)
- `classes4:defpackage/v1e.java` (11)
- `classes5:defpackage/wsd.java` (11)
- `classes5:defpackage/gtd.java` (11)
- `classes5:defpackage/xsd.java` (11)
- `classes5:defpackage/y1e.java` (11)
- `classes5:defpackage/x1e.java` (11)
- `classes:defpackage/ss9.java` (10)
- `classes:defpackage/kaa.java` (9)

```
classes:androidx/appcompat/widget/SearchView.java:972:    public void onActionViewCollapsed() {
classes:androidx/media3/exoplayer/dash/DashMediaSource.java:621:                    b0(Math.max(j, (this.J + j6) - SystemClock.elapsedRealtime()));
classes:androidx/appcompat/widget/Toolbar.java:1853:                ((hc2) callback).onActionViewCollapsed();
classes:androidx/media3/exoplayer/dash/c.java:461:        long jElapsedRealtime = SystemClock.elapsedRealtime();
classes:androidx/media3/exoplayer/dash/c.java:465:            if (e56Var.f(i2, jElapsedRealtime)) {
classes:defpackage/eka.java:101:        public void onActionViewCollapsed() {
classes:defpackage/eka.java:102:            this.b.onActionViewCollapsed();
classes:defpackage/io0.java:106:            printWriter.print(DateUtils.formatElapsedTime(this.l / 1000));
classes:defpackage/io0.java:111:                str2 = "-" + DateUtils.formatElapsedTime((SystemClock.uptimeMillis() - this.m) / 1000);
classes:defpackage/uhj.java:107:                final long jElapsedRealtime = SystemClock.elapsedRealtime();
classes:defpackage/uhj.java:111:                        ((uhj) j7j.j(this.b.b)).p(obj, jElapsedRealtime);
classes:defpackage/taa.java:1628:        this.m1 = SystemClock.elapsedRealtime();
```

### notif_permission_nag — 0 hits in 0 files


```
```

### cancellation_retention — 0 hits in 0 files


```
```

### urgency_countdown — 148 hits in 27 files

- `classes4:uk/co/bbc/authtoolkit/profiles/network/AdminTokens.java` (17)
- `classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java` (12)
- `classes4:defpackage/ks0.java` (11)
- `classes3:com/appsflyer/internal/AFf1zSDK.java` (9)
- `classes3:com/appsflyer/internal/AFe1eSDK.java` (9)
- `classes3:defpackage/t7j.java` (9)
- `classes4:okhttp3/internal/concurrent/TaskQueue.java` (9)
- `classes4:defpackage/uw.java` (9)
- `classes3:com/optimizely/ab/config/PollingProjectConfigManager.java` (6)
- `classes3:defpackage/uhe.java` (6)
- `classes3:defpackage/v23.java` (6)
- `classes3:com/appsflyer/internal/AFf1xSDK.java` (5)

```
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:59:import java.util.concurrent.CountDownLatch;
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:161:        CountDownLatch countDownLatch = new CountDownLatch(1);
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:162:        downloadImpl.setMonitor(new DownloadMonitor(downloadImpl, submitDownloadTask(getObjectRequest, file, z, countDownLatch, downloadImpl)));
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:163:        countDownLatch.countDown();
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:214:    private Future<?> submitDownloadTask(final GetObjectRequest getObjectRequest, final File file, final boolean z, final CountDownLatch countDownLatch, final DownloadImpl downloadImpl) {
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:219:                    countDownLatch.await();
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:332:        CountDownLatch countDownLatch = new CountDownLatch(1);
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:333:        MultipleFileTransferStateChangeListener multipleFileTransferStateChangeListener = new MultipleFileTransferStateChangeListener(countDownLatch, multipleFileDownloadImpl);
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:348:        countDownLatch.countDown();
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:433:        CountDownLatch countDownLatch = new CountDownLatch(1);
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:434:        MultipleFileTransferStateChangeListener multipleFileTransferStateChangeListener = new MultipleFileTransferStateChangeListener(countDownLatch, multipleFileUploadImpl);
classes3:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java:461:        countDownLatch.countDown();
```

### infinite_autoplay — 61 hits in 26 files

- `classes5:uk/co/bbc/nswapps/ablmodel/dataobjects/schema/contentitems/MediaSource.java` (16)
- `classes4:uk/co/bbc/smpan/PlayerController.java` (7)
- `classes4:uk/co/bbc/smpan/stats/av/NewSessionStarted.java` (4)
- `classes4:uk/co/bbc/smpan/SMPFacade.java` (3)
- `classes4:defpackage/r0e.java` (2)
- `classes4:defpackage/c0e.java` (2)
- `classes4:defpackage/vzd.java` (2)
- `classes4:defpackage/ixg.java` (2)
- `classes4:defpackage/kxg.java` (2)
- `classes4:defpackage/jxg.java` (2)
- `classes5:defpackage/d0e.java` (2)
- `classes5:defpackage/i0e.java` (2)

```
classes3:com/airbnb/lottie/LottieAnimationView.java:332:        if (typedArrayObtainStyledAttributes.getBoolean(q1e.LottieAnimationView_lottie_autoPlay, false)) {
classes3:defpackage/q1e.java:9:    public static int LottieAnimationView_lottie_autoPlay = 3;
classes4:uk/co/bbc/smpan/SMPFacade.java:141:    private void announcePlayIntentIfLoadingForAutoPlay(vtc vtcVar) {
classes4:uk/co/bbc/smpan/SMPFacade.java:242:        announcePlayIntentIfLoadingForAutoPlay(vtcVar);
classes4:uk/co/bbc/smpan/SMPFacade.java:249:        announcePlayIntentIfLoadingForAutoPlay(vtcVar);
classes4:uk/co/bbc/smpan/media/model/PlaybackSelectionDelegate.java:299:        this.playerController.setAutoplay(playRequest.d());
classes4:uk/co/bbc/smpan/PlayerController.java:38:@Metadata(d1 = {"\u0000Ð\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u
classes4:uk/co/bbc/smpan/PlayerController.java:43:    private boolean autoplay;
classes4:uk/co/bbc/smpan/PlayerController.java:146:    public final boolean getAutoplay() {
classes4:uk/co/bbc/smpan/PlayerController.java:147:        return this.autoplay;
classes4:uk/co/bbc/smpan/PlayerController.java:191:        this.autoplay = false;
classes4:uk/co/bbc/smpan/PlayerController.java:252:    public final void setAutoplay(boolean z) {
```

### badges — 2 hits in 1 files

- `classes:defpackage/spb.java` (2)

```
classes:defpackage/spb.java:59:            return builder.setBadgeIconType(i);
classes:defpackage/spb.java:148:        builder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, fVar.j).setVibrate(notification.vibrate).setLights(notification.ledARGB, notification.led [... om
```

### minors_age — 6 hits in 5 files

- `classes4:defpackage/vw.java` (2)
- `classes3:com/amazonaws/regions/ServiceAbbreviations.java` (1)
- `classes4:defpackage/kr7.java` (1)
- `classes4:defpackage/e9j.java` (1)
- `classes4:defpackage/k5b.java` (1)

```
classes3:com/amazonaws/regions/ServiceAbbreviations.java:34:    public static final String StorageGateway = "storagegateway";
classes4:defpackage/kr7.java:70:        return "IdctaFederatedEndpoints(signInEndpoint=" + this.a + ", registerEndpoint=" + this.b + ", skipUnder13RegistrationEndpoint=" + this.c + ", callbackEndpoint=" + this.d + ", authoriseEndpoint=" + this.e + ", needHelpSigningInUrl=" + this.f + ")";
classes4:defpackage/vw.java:59:        this.a.b("storage.skip_under13_register_url_key", gr7Var.e().f());
classes4:defpackage/vw.java:133:        return this.a.a("storage.skip_under13_register_url_key");
classes4:defpackage/e9j.java:76:        return "V5AuthConfig(redirectUrl=" + this.a + ", clientId=" + this.b + ", userOrigin=" + this.c + ", idctaConfigUrl=" + this.d + ", context=" + this.e + ", isHybrid=" + this.f + ", hideUnder13Registration=" + this.g + ")";
classes4:defpackage/k5b.java:69:        return "NativeSignInDependencies(signInCallback=" + this.a + ", isAutomotive=" + this.b + ", autoSignInEnabled=" + this.c + ", autoSignInOption=" + this.d + ", hideUnder13Registration=" + this.e + ", needHelpUrl=" + this.f + ")";
```

### screen_time — 2 hits in 1 files

- `classes4:dotmetrics/analytics/JsonObjects.java` (2)

```
classes4:dotmetrics/analytics/JsonObjects.java:39:            public static final String KEY_SESSION_LENGTH_SECONDS = "ctl";
classes4:dotmetrics/analytics/JsonObjects.java:99:        public static final String KEY_SESSION_LENGTH_SECONDS = "ctl";
```

## UI string categories (default locale)

### loss_aversion_copy — 0 strings

```
```

### urgency_copy — 0 strings

```
```

### confirmshaming_copy — 4 strings

```
strings.xml:126:    <string name="authtoolkit_not_now_button">Not Now</string>
strings.xml:703:    <string name="maybe_later">Maybe later</string>
strings.xml:822:    <string name="notifications_maybe_later">Maybe later</string>
strings.xml:1152:    <string name="ua_rate_app_action_default_rate_negative_button">No Thanks</string>
```

### social_pressure_copy — 3 strings

```
strings.xml:224:    <string name="com.google.firebase.crashlytics.mapping_file_id">c7b799ee3c0a4521a0df3f252b88f3e9</string>
strings.xml:225:    <string name="com.google.firebase.crashlytics.version_control_info">"repositories {
strings.xml:444:    <string name="firebase_database_url">https://api-project-385909808280.firebaseio.com</string>
```

### guilt_copy — 2 strings

```
strings.xml:138:    <string name="authtoolkit_profile_picker_heading">Welcome back</string>
strings.xml:1088:    <string name="ua_emoji_sad">😞</string>
```

### subscription_copy — 9 strings

```
strings.xml:303:    <string name="edit_my_topics_groupConfirmPlus">groupConfirmPlus</string>
strings.xml:305:    <string name="edit_my_topics_plus">plus</string>
strings.xml:591:    <string name="m3_exceed_max_badge_text_suffix">%1$s%2$s</string>
strings.xml:733:    <string name="mtrl_exceed_max_badge_number_content_description">More than %1$d new notifications</string>
strings.xml:734:    <string name="mtrl_exceed_max_badge_number_suffix">%1$d%2$s</string>
strings.xml:978:    <string name="settings_notifications_subscription_error_dialog_body">We can’t update your notifications right now, please try again later.</string>
strings.xml:979:    <string name="settings_notifications_subscription_error_dialog_dismiss_button_text">Ok</string>
strings.xml:980:    <string name="settings_notifications_subscription_error_dialog_title">Sorry, something went wrong</string>
strings.xml:982:    <string name="settings_notifications_summary_manage_in_app_subscriptions">Choose which notifications you want to receive</string>
```

### data_copy — 8 strings

```
strings.xml:93:    <string name="authtoolkit_connect_third_party_text">"To connect %1$s to your BBC account, we'll share a unique ID with them, but we will not share personal information."</string>
strings.xml:94:    <string name="authtoolkit_connect_third_party_title">Connect %1$s to your BBC account</string>
strings.xml:98:    <string name="authtoolkit_could_not_connect_third_party">Could not connect to %1$s</string>
strings.xml:356:    <string name="error_content_unavailable_unsupported_location_message">This content is not currently available in your location</string>
strings.xml:542:    <string name="key_third_party_libraries">third_party_libraries</string>
strings.xml:918:    <string name="settings_account_detail">Update your BBC account information, like location and personal details</string>
strings.xml:958:    <string name="settings_licenses">Third party libraries</string>
strings.xml:1201:    <string name="weather_in_location_text">in %s</string>
```

