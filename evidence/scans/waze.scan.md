# Pattern scan: work/waze/jdex

## Code categories (library packages excluded)

### installed_apps — 28 hits in 21 files

- `classes4:com/waze/camera/b.java` (4)
- `classes4:com/google/android/play/core/c/a.java` (2)
- `classes4:com/google/android/gms/common/ag.java` (2)
- `classes6:com/waze/ad/b.java` (2)
- `classes6:com/waze/ac/a/i.java` (2)
- `classes:androidx/compose/foundation/text/contextmenu/ProcessTextApi23Impl.java` (1)
- `classes2:androidx/browser/browseractions/BrowserActionsIntent.java` (1)
- `classes2:androidx/browser/trusted/TrustedWebActivityServiceConnectionPool.java` (1)
- `classes3:androidx/core/widget/TextViewCompat.java` (1)
- `classes3:androidx/core/content/PackageManagerCompat.java` (1)
- `classes3:androidx/core/content/pm/ShortcutXmlParser.java` (1)
- `classes3:androidx/core/content/pm/ShortcutManagerCompat.java` (1)

```
classes:androidx/compose/foundation/text/contextmenu/ProcessTextApi23Impl.java:50:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(INSTANCE.createProcessTextIntent(), 0);
classes2:androidx/browser/browseractions/BrowserActionsIntent.java:69:        return context.getPackageManager().queryIntentActivities(new Intent(ACTION_BROWSER_ACTIONS_OPEN, Uri.parse(TEST_URL)), 131072);
classes2:androidx/browser/trusted/TrustedWebActivityServiceConnectionPool.java:73:            Iterator<ResolveInfo> it = context.getPackageManager().queryIntentActivities(intent, 131072).iterator();
classes3:androidx/core/widget/TextViewCompat.java:152:                for (ResolveInfo resolveInfo : packageManager.queryIntentActivities(createProcessTextIntent(), 0)) {
classes3:androidx/core/content/PackageManagerCompat.java:49:        Iterator<ResolveInfo> it = packageManager.queryIntentActivities(new Intent(ACTION_PERMISSION_REVOCATION_SETTINGS).setData(Uri.fromParts("package", "com.example", null)), 0).iterator();
classes3:androidx/core/content/pm/ShortcutXmlParser.java:62:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(intent, 128);
classes3:androidx/core/content/pm/ShortcutManagerCompat.java:235:            Iterator<ResolveInfo> it = packageManager.queryIntentActivities(intent, 128).iterator();
classes3:androidx/credentials/playservices/controllers/identityauth/beginsignin/BeginSignInControllerUtility.java:36:            return r1.getPackageInfo("com.google.android.gms", 0).versionCode;
classes3:androidx/credentials/playservices/controllers/identityauth/createpublickeycredential/PublicKeyCredentialControllerUtility.java:148:            PackageInfo packageInfo = packageManager.getPackageInfo("com.google.android.gms", 0);
classes4:com/a/a/a/a.java:65:                        if (context.getPackageManager().getPackageInfo("com.android.vending", TsExtractor.TS_STREAM_TYPE_DC2_H262).versionCode >= 80837300) {
classes4:com/waze/camera/b.java:196:            List listQueryIntentActivities = packageManager.queryIntentActivities(intentO, PackageManager.ResolveInfoFlags.of(131072L));
classes4:com/waze/camera/b.java:197:            x.e(listQueryIntentActivities, "queryIntentActivities(...)");
```

### usage_stats — 0 hits in 0 files


```
```

### clipboard — 4 hits in 3 files

- `classes:androidx/compose/ui/platform/AndroidClipboardManager.java` (2)
- `classes:androidx/compose/foundation/text/input/internal/selection/ClipboardPasteState.java` (1)
- `classes2:android/support/v7/widget/ah.java` (1)

```
classes:androidx/compose/foundation/text/input/internal/selection/ClipboardPasteState.java:31:        boolean zHasPrimaryClip = AndroidClipboard_androidKt.getNativeClipboardManager(this.clipboard).hasPrimaryClip();
classes:androidx/compose/ui/platform/AndroidClipboardManager.java:34:        ClipData primaryClip = getClipboardManager().getPrimaryClip();
classes:androidx/compose/ui/platform/AndroidClipboardManager.java:48:        ClipData primaryClip = getClipboardManager().getPrimaryClip();
classes2:android/support/v7/widget/ah.java:230:            ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
```

### contacts — 7 hits in 3 files

- `classes4:com/bumptech/glide/load/data/u.java` (3)
- `classes5:com/waze/menus/p.java` (2)
- `classes7:com/airbnb/lottie/b/s.java` (2)

```
classes4:com/bumptech/glide/load/data/u.java:7:import android.provider.ContactsContract;
classes4:com/bumptech/glide/load/data/u.java:35:        return ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uri, true);
classes4:com/bumptech/glide/load/data/u.java:52:            Uri uriLookupContact = ContactsContract.Contacts.lookupContact(contentResolver, uri);
classes5:com/waze/menus/p.java:4:import android.provider.ContactsContract;
classes5:com/waze/menus/p.java:193:                        Cursor cursorQuery = lv.a().getContentResolver().query(ContactsContract.Data.CONTENT_URI, null, "display_name LIKE ? AND mimetype = ?", new String[]{"%" + str + '%', "vnd.android.cursor.item/postal-address_v2"}, null);
classes7:com/airbnb/lottie/b/s.java:8:import android.provider.ContactsContract;
classes7:com/airbnb/lottie/b/s.java:91:                Cursor cursorH = this.a.h(ContactsContract.Data.CONTENT_URI, new String[]{"data1", "data4", "data7", "data9", "data4", "data8", "data10", "data2"}, "_id = " + ContentUris.parseId(uri) + " AND ContactsContract.Data.MIMETYPE = 'vnd.android.cursor 
```

### call_log — 0 hits in 0 files


```
```

### sms — 0 hits in 0 files


```
```

### location — 43 hits in 18 files

- `classes3:androidx/core/location/LocationManagerCompat.java` (19)
- `classes7:com/waze/tide/s.java` (3)
- `classes4:com/fasterxml/jackson/core/filter/FilteringParserDelegate.java` (2)
- `classes4:com/fasterxml/jackson/core/JsonParser.java` (2)
- `classes4:com/fasterxml/jackson/core/util/JsonParserDelegate.java` (2)
- `classes6:com/waze/ch/a/a.java` (2)
- `classes7:com/waze/sharedrive/data/o.java` (2)
- `classes2:androidx/car/app/AppManager.java` (1)
- `classes2:android/support/v7/app/au.java` (1)
- `classes4:com/fasterxml/jackson/core/base/ParserBase.java` (1)
- `classes4:com/fasterxml/jackson/core/json/JsonParserBase.java` (1)
- `classes4:com/fasterxml/jackson/databind/util/TokenBuffer.java` (1)

```
classes2:androidx/car/app/AppManager.java:300:        ((LocationManager) this.mCarContext.getSystemService("location")).requestLocationUpdates("fused", 1000L, 1.0f, (LocationListener) this.mLocationListener, this.mLocationUpdateHandlerThread.getLooper());
classes2:android/support/v7/app/au.java:40:                return locationManager.getLastKnownLocation(str);
classes3:androidx/core/location/LocationManagerCompat.java:74:        static void getCurrentLocation(LocationManager locationManager, String str, CancellationSignal cancellationSignal, Executor executor, final Consumer<Location> consumer) {
classes3:androidx/core/location/LocationManagerCompat.java:76:            locationManager.getCurrentLocation(str, cancellationSignal, executor, new java.util.function.Consumer() { // from class: androidx.core.location.LocationManagerCompat$Api30Impl$$ExternalSyntheticLambda0
classes3:androidx/core/location/LocationManagerCompat.java:112:                        Method declaredMethod = LocationManager.class.getDeclaredMethod("requestLocationUpdates", cls, Executor.class, LocationListener.class);
classes3:androidx/core/location/LocationManagerCompat.java:141:        static void requestLocationUpdates(LocationManager locationManager, String str, LocationRequest locationRequest, Executor executor, LocationListener locationListener) {
classes3:androidx/core/location/LocationManagerCompat.java:142:            locationManager.requestLocationUpdates(str, locationRequest, executor, locationListener);
classes3:androidx/core/location/LocationManagerCompat.java:510:    public static void getCurrentLocation(LocationManager locationManager, String str, CancellationSignal cancellationSignal, Executor executor, final androidx.core.util.Consumer<Location> consumer) {
classes3:androidx/core/location/LocationManagerCompat.java:512:            Api30Impl.getCurrentLocation(locationManager, str, cancellationSignal, executor, consumer);
classes3:androidx/core/location/LocationManagerCompat.java:518:        final Location lastKnownLocation = locationManager.getLastKnownLocation(str);
classes3:androidx/core/location/LocationManagerCompat.java:529:        locationManager.requestLocationUpdates(str, 0L, 0.0f, cancellableLocationListener, Looper.getMainLooper());
classes3:androidx/core/location/LocationManagerCompat.java:662:    public static void requestLocationUpdates(LocationManager locationManager, String str, LocationRequestCompat locationRequestCompat, Executor executor, LocationListenerCompat locationListenerCompat) {
```

### wifi_bt_scan — 5 hits in 1 files

- `classes5:com/waze/beacons/f.java` (5)

```
classes5:com/waze/beacons/f.java:5:import android.bluetooth.le.BluetoothLeScanner;
classes5:com/waze/beacons/f.java:62:        BluetoothLeScanner bluetoothLeScanner = bluetoothAdapter.getBluetoothLeScanner();
classes5:com/waze/beacons/f.java:71:                    bluetoothLeScanner.startScan(h.a.i.d(scanFilterBuild), scanSettingsBuild, this.f);
classes5:com/waze/beacons/f.java:74:                    bluetoothLeScanner.startScan((List<ScanFilter>) null, scanSettingsBuild, this.f);
classes5:com/waze/beacons/f.java:87:            BluetoothLeScanner bluetoothLeScanner = bluetoothAdapter != null ? bluetoothAdapter.getBluetoothLeScanner() : null;
```

### device_ids — 46 hits in 22 files

- `classes2:androidx/camera/core/impl/utils/ContextUtil.java` (6)
- `classes2:android/support/v7/widget/RecyclerView.java` (6)
- `classes3:androidx/core/telephony/TelephonyManagerCompat.java` (4)
- `classes:androidx/compose/ui/platform/AndroidComposeView.java` (3)
- `classes3:androidx/core/widget/NestedScrollView.java` (3)
- `classes3:androidx/core/view/DifferentialMotionFlingController.java` (3)
- `classes2:androidx/camera/core/impl/CameraValidatorImpl.java` (2)
- `classes2:android/support/v7/app/an.java` (2)
- `classes5:com/google/aa/a/a/a/a/cb.java` (2)
- `classes5:com/google/aa/a/a/a/a/bu.java` (2)
- `classes5:com/google/aa/a/a/a/a/ai.java` (2)
- `classes2:androidx/camera/lifecycle/LifecycleCameraRepository.java` (1)

```
classes:androidx/compose/ui/platform/AndroidComposeView.java:958:        return getFocusOwner().dispatchRotaryEvent(new RotaryScrollEvent(ViewConfigurationCompat.getScaledVerticalScrollFactor(viewConfiguration, getContext()) * f, f * ViewConfigurationCompat.getScaledHorizontalScrollFactor(viewConfig
classes:androidx/compose/ui/platform/AndroidComposeView.java:977:            focusTraversalThreshold = Api37_1Impl.getFocusTraversalThreshold(viewConfiguration, motionEvent.getDeviceId(), 26, 4194304);
classes:androidx/compose/ui/platform/AndroidComposeView.java:1493:        MotionEvent motionEventObtain = (!ComposeUiFlags.isTrackpadPanHoverFixEnabled || Build.VERSION.SDK_INT < 34) ? MotionEvent.obtain(downTime, j, i, pointerCount, pointerPropertiesArr, pointerCoordsArr, motionEvent.getMetaState()
classes2:androidx/camera/lifecycle/LifecycleCameraRepository.java:271:    int getDeviceId() {
classes2:androidx/camera/lifecycle/LifecycleCameraProviderImpl.java:884:            this.lifecycleCameraRepository = LifecycleCameraRepositories.getInstance$camera_lifecycle(ContextUtil.getDeviceId(context));
classes2:androidx/camera/core/impl/utils/ContextUtil.java:47:        static int getDeviceId(Context context) {
classes2:androidx/camera/core/impl/utils/ContextUtil.java:48:            return context.getDeviceId();
classes2:androidx/camera/core/impl/utils/ContextUtil.java:65:        return String.format("%d-%d-%s", Integer.valueOf(context.getApplicationContext().hashCode()), Integer.valueOf(getDeviceId(context)), Build.VERSION.SDK_INT >= 30 ? Api30Impl.getAttributionTag(context) : null);
classes2:androidx/camera/core/impl/utils/ContextUtil.java:86:    public static int getDeviceId(Context context) {
classes2:androidx/camera/core/impl/utils/ContextUtil.java:88:            return Api34Impl.getDeviceId(context);
classes2:androidx/camera/core/impl/utils/ContextUtil.java:102:                applicationContext = Api34Impl.createDeviceContext(applicationContext, Api34Impl.getDeviceId(context));
classes2:androidx/camera/core/impl/CameraValidatorImpl.java:36:        public final int getDeviceId(Context context) {
```

### gsf_id — 0 hits in 0 files


```
```

### advertising_id — 39 hits in 6 files

- `classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java` (28)
- `classes4:com/google/android/gms/ads/identifier/AdvertisingIdListenerService.java` (3)
- `classes5:com/waze/c.java` (3)
- `classes4:com/google/android/gms/ads/identifier/AdvertisingIdTelemetryLogger.java` (2)
- `classes5:com/waze/lu.java` (2)
- `classes4:com/google/android/gms/ads/identifier/AdvertisingIdClientConstants.java` (1)

```
classes4:com/google/android/gms/ads/identifier/AdvertisingIdListenerService.java:8:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
classes4:com/google/android/gms/ads/identifier/AdvertisingIdListenerService.java:55:                        this.this$1.this$0.onAdvertisingIdInfoChanged(new AdvertisingIdClient.Info(bundle2.getString(AdvertisingIdListenerService.AD_ID_BUNDLE_KEY), bundle2.getBoolean(AdvertisingIdListenerService.LAT
classes4:com/google/android/gms/ads/identifier/AdvertisingIdListenerService.java:74:    public abstract void onAdvertisingIdInfoChanged(AdvertisingIdClient.Info info);
classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:26:public class AdvertisingIdClient {
classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:37:    private static final String TAG = "AdvertisingIdClient";
classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:39:    private static volatile AdvertisingIdClient sharedClient;
classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:52:        private WeakReference<AdvertisingIdClient> client;
classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:56:        public AutoDisconnectTask(AdvertisingIdClient advertisingIdClient, long j2) {
classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:66:            AdvertisingIdClient advertisingIdClient = this.client.get();
classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:118:    public AdvertisingIdClient(Context context, long j2, boolean z, boolean z2) {
classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:127:    public static AdvertisingIdClient getAdvertisingIdClient(Context context) {
classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:128:        AdvertisingIdClient advertisingIdClient = sharedClient;
```

### install_referrer — 4 hits in 1 files

- `classes2:android/support/v7/widget/ek.java` (4)

```
classes2:android/support/v7/widget/ek.java:20:        if (Log.isLoggable("InstallReferrerClient", 2)) {
classes2:android/support/v7/widget/ek.java:21:            Log.v("InstallReferrerClient", str);
classes2:android/support/v7/widget/ek.java:26:        if (Log.isLoggable("InstallReferrerClient", 5)) {
classes2:android/support/v7/widget/ek.java:27:            Log.w("InstallReferrerClient", str);
```

### sensors — 6 hits in 3 files

- `classes5:com/google/k/a/a/b/bl.java` (2)
- `classes5:com/google/k/a/a/b/bs.java` (2)
- `classes5:com/waze/AlerterController$Alerter$Subtype.java` (2)

```
classes5:com/google/k/a/a/b/bl.java:281:    TYPE_LIGHTHOUSE(3950),
classes5:com/google/k/a/a/b/bl.java:1067:                                                            return TYPE_LIGHTHOUSE;
classes5:com/google/k/a/a/b/bs.java:32:    TYPE_LIGHT_RAIL_TRACK(4661),
classes5:com/google/k/a/a/b/bs.java:761:                    return TYPE_LIGHT_RAIL_TRACK;
classes5:com/waze/AlerterController$Alerter$Subtype.java:78:    public static final AlerterController$Alerter$Subtype JAM_TYPE_LIGHT_TRAFFIC = new AlerterController$Alerter$Subtype("JAM_TYPE_LIGHT_TRAFFIC", 66, AlerterController$Alerter$Type.TRAFFIC_JAM, 3);
classes5:com/waze/AlerterController$Alerter$Subtype.java:110:        return new AlerterController$Alerter$Subtype[]{UNSPECIFIED, HAZARD_TYPE_ON_ROAD, HAZARD_TYPE_ON_SHOULDER, HAZARD_TYPE_WEATHER, HAZARD_TYPE_ON_ROAD_OBJECT, HAZARD_TYPE_ON_ROAD_POT_HOLE, HAZARD_TYPE_ON_ROAD_ROAD_KILL, HAZARD_TYPE_ON_
```

### accounts — 0 hits in 0 files


```
```

### battery_state — 0 hits in 0 files


```
```

### screen_capture_detect — 28 hits in 3 files

- `classes4:com/google/android/apps/a/a/a/a/b.java` (26)
- `classes2:androidx/camera/view/SurfaceViewImplementation.java` (1)
- `classes4:com/google/android/apps/a/a/a/a/f.java` (1)

```
classes2:androidx/camera/view/SurfaceViewImplementation.java:32:    private static final int SCREENSHOT_TIMEOUT_MILLIS = 100;
classes4:com/google/android/apps/a/a/a/a/f.java:24:    public static final int SCREENSHOT_URL_FIELD_NUMBER = 3;
classes4:com/google/android/apps/a/a/a/a/b.java:2051:    OPA_CHAT_PERFORMER_SCREENSHOT_SHARE(1215),
classes4:com/google/android/apps/a/a/a/a/b.java:2052:    OPA_CHAT_PERFORMER_SCREENSHOT_SHARE_FALLBACK(3083),
classes4:com/google/android/apps/a/a/a/a/b.java:2061:    OPA_CHAT_PERFORMER_SCREENSHOT_FAILED(1223),
classes4:com/google/android/apps/a/a/a/a/b.java:2382:    SHARE_SCREENSHOT_STARTED(1975),
classes4:com/google/android/apps/a/a/a/a/b.java:2383:    SHARE_SCREENSHOT_URI_SAVED(1976),
classes4:com/google/android/apps/a/a/a/a/b.java:2384:    SHARE_SCREENSHOT_SUCCESSFUL(1977),
classes4:com/google/android/apps/a/a/a/a/b.java:2385:    SHARE_SCREENSHOT_FAILED(1978),
classes4:com/google/android/apps/a/a/a/a/b.java:2386:    SHARE_SCREENSHOT_CANCELLED(1979),
classes4:com/google/android/apps/a/a/a/a/b.java:2691:    ASSIST_DATA_PROCESSOR_SCREENSHOT_TIMEOUT(3488),
classes4:com/google/android/apps/a/a/a/a/b.java:2739:    ASSISTANT_AVS_SCREENSHOT_SUCCEEDED(3736),
```

### audio_capture — 113 hits in 23 files

- `classes5:com/waze/car_lib/x.java` (42)
- `classes6:com/waze/google_assistant/aw.java` (17)
- `classes7:com/waze/google_assistant/SpeechRecognizerActivity.java` (11)
- `classes7:com/waze/speech/w.java` (9)
- `classes7:com/waze/mywaze/f.java` (3)
- `classes6:com/google/android/material/datepicker/ad.java` (2)
- `classes6:com/waze/ifs/ui/e.java` (2)
- `classes6:com/waze/app_nav/hub/c/h.java` (2)
- `classes7:com/waze/reports/dh.java` (2)
- `classes7:com/waze/car_lib/o/ab.java` (2)
- `classes7:com/waze/menus/SideMenuSearchBar.java` (2)
- `classes7:com/waze/MainActivity.java` (2)

```
classes5:com/waze/h/c/b/p.java:53:        return new o(new AudioRecord(i2, aVar.c().a(), 16, iC, i3), i3, aVar, aVar2, this.a);
classes5:com/waze/car_lib/ag.java:30:        h.g.b.x.f(gVar, "googleSpeechRecognizerApi");
classes5:com/waze/car_lib/x.java:1964:                        com.waze.shared_infra.i.e eVarD = com.waze.shared_infra.i.a.d("GoogleSpeechRecognizerApi");
classes5:com/waze/car_lib/x.java:1975:                        com.waze.shared_infra.i.e eVarD2 = com.waze.shared_infra.i.a.d("CarSpeechRecognizerService");
classes5:com/waze/car_lib/x.java:2142:                        com.waze.shared_infra.i.e eVarD = com.waze.shared_infra.i.a.d("GoogleSpeechRecognizerApi");
classes5:com/waze/car_lib/x.java:2153:                        com.waze.shared_infra.i.e eVarD2 = com.waze.shared_infra.i.a.d("CarSpeechRecognizerService");
classes5:com/waze/car_lib/x.java:16016:                        com.waze.shared_infra.i.e eVarD = com.waze.shared_infra.i.a.d("GoogleSpeechRecognizerApi");
classes5:com/waze/car_lib/x.java:16027:                        com.waze.shared_infra.i.e eVarD2 = com.waze.shared_infra.i.a.d("CarSpeechRecognizerService");
classes5:com/waze/car_lib/x.java:16197:                        com.waze.shared_infra.i.e eVarD = com.waze.shared_infra.i.a.d("GoogleSpeechRecognizerApi");
classes5:com/waze/car_lib/x.java:16208:                        com.waze.shared_infra.i.e eVarD2 = com.waze.shared_infra.i.a.d("CarSpeechRecognizerService");
classes5:com/waze/car_lib/x.java:18914:                        com.waze.shared_infra.i.e eVarD = com.waze.shared_infra.i.a.d("GoogleSpeechRecognizerApi");
classes5:com/waze/car_lib/x.java:18925:                        com.waze.shared_infra.i.e eVarD2 = com.waze.shared_infra.i.a.d("CarSpeechRecognizerService");
```

### accessibility — 216 hits in 42 files

- `classes:androidx/compose/ui/platform/ComposeViewContext.java` (23)
- `classes3:androidx/core/view/accessibility/AccessibilityManagerCompat.java` (20)
- `classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java` (18)
- `classes3:androidx/compose/material3/internal/Listener.java` (12)
- `classes4:com/google/android/material/textfield/u.java` (9)
- `classes:androidx/compose/ui/platform/CompositionLocalsKt.java` (7)
- `classes:androidx/compose/ui/platform/AndroidAccessibilityManager.java` (7)
- `classes4:com/google/android/material/behavior/HideBottomViewOnScrollBehavior.java` (7)
- `classes4:com/google/android/material/behavior/HideViewOnScrollBehavior.java` (7)
- `classes4:com/google/android/material/textfield/ab.java` (7)
- `classes4:com/google/android/material/textfield/ai.java` (6)
- `classes3:androidx/customview/widget/ExploreByTouchHelper.java` (5)

```
classes:androidx/compose/material/SnackbarHostKt$SnackbarHost$1$1.java:3:import androidx.compose.ui.platform.AccessibilityManager;
classes:androidx/compose/material/SnackbarHostKt$SnackbarHost$1$1.java:16:    final /* synthetic */ AccessibilityManager $accessibilityManager;
classes:androidx/compose/material/SnackbarHostKt$SnackbarHost$1$1.java:22:    SnackbarHostKt$SnackbarHost$1$1(SnackbarData snackbarData, AccessibilityManager accessibilityManager, e<? super SnackbarHostKt$SnackbarHost$1$1> eVar) {
classes:androidx/compose/ui/platform/CompositionLocalsKt.java:41:    private static final ProvidableCompositionLocal<AccessibilityManager> LocalAccessibilityManager;
classes:androidx/compose/ui/platform/CompositionLocalsKt.java:104:        LocalAccessibilityManager = ComposeUiFlags.isMinimalistLocalsEnabled ? CompositionLocalKt.staticCompositionLocalWithComputedDefaultOf(new l<CompositionLocalAccessorScope, AccessibilityManager>() { // from class: androidx.compo
classes:androidx/compose/ui/platform/CompositionLocalsKt.java:105:            public final AccessibilityManager invoke(CompositionLocalAccessorScope compositionLocalAccessorScope) {
classes:androidx/compose/ui/platform/CompositionLocalsKt.java:106:                return ((Owner) compositionLocalAccessorScope.getCurrentValue(CompositionLocalsKt.getLocalOwner())).getAccessibilityManager();
classes:androidx/compose/ui/platform/CompositionLocalsKt.java:307:                providedValueArr[0] = LocalAccessibilityManager.provides(owner.getAccessibilityManager());
classes:androidx/compose/ui/platform/CompositionLocalsKt.java:520:    public static final ProvidableCompositionLocal<AccessibilityManager> getLocalAccessibilityManager() {
classes:androidx/compose/ui/platform/CompositionLocalsKt.java:521:        return LocalAccessibilityManager;
classes:androidx/compose/ui/node/Owner.java:21:import androidx.compose.ui.platform.AccessibilityManager;
classes:androidx/compose/ui/node/Owner.java:90:    AccessibilityManager getAccessibilityManager();
```

### root_emulator — 410 hits in 43 files

- `classes2:androidx/compose/material3/ExposedDropdownMenuKt.java` (79)
- `classes2:androidx/compose/material/internal/ExposedDropdownMenuPopup_androidKt.java` (55)
- `classes:androidx/compose/material/ExposedDropdownMenu_androidKt.java` (45)
- `classes2:androidx/compose/material3/ExposedDropdownMenuKt$ExposedDropdownMenuBox$scope$1$1.java` (26)
- `classes:androidx/compose/material/ExposedDropdownMenuDefaults.java` (21)
- `classes:androidx/compose/material/ExposedDropdownMenuBoxScope.java` (20)
- `classes2:androidx/compose/material3/ExposedDropdownMenuBoxScope.java` (18)
- `classes2:androidx/compose/material3/ExposedDropdownMenu_androidKt.java` (15)
- `classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java` (14)
- `classes2:androidx/compose/material3/ExposedDropdownMenuDefaults.java` (10)
- `classes5:com/waze/R.java` (10)
- `classes4:com/fasterxml/jackson/core/filter/FilteringParserDelegate.java` (9)

```
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:17:final class DefaultTextFieldForExposedDropdownMenusColors implements TextFieldColors {
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:41:    private DefaultTextFieldForExposedDropdownMenusColors(long j, long j2, long j3, long j4, long j5, long j6, long j7, long j8, long j9, long j10, long j11, long j12, long j13, long j14, long j15, long j16, long
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:82:            ComposerKt.traceEventStart(-28962788, i, -1, "androidx.compose.material.DefaultTextFieldForExposedDropdownMenusColors.backgroundColor (ExposedDropdownMenu.kt:567)");
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:96:            ComposerKt.traceEventStart(-930693132, i, -1, "androidx.compose.material.DefaultTextFieldForExposedDropdownMenusColors.cursorColor (ExposedDropdownMenu.kt:600)");
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:113:        DefaultTextFieldForExposedDropdownMenusColors defaultTextFieldForExposedDropdownMenusColors = (DefaultTextFieldForExposedDropdownMenusColors) obj;
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:114:        return Color.m3769equalsimpl0(this.textColor, defaultTextFieldForExposedDropdownMenusColors.textColor) && Color.m3769equalsimpl0(this.disabledTextColor, defaultTextFieldForExposedDropdownMenusColors.disa
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:147:            ComposerKt.traceEventStart(476110356, i, -1, "androidx.compose.material.DefaultTextFieldForExposedDropdownMenusColors.indicatorColor (ExposedDropdownMenu.kt:549)");
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:172:            ComposerKt.traceEventStart(-1749156593, i, -1, "androidx.compose.material.DefaultTextFieldForExposedDropdownMenusColors.labelColor (ExposedDropdownMenu.kt:581)");
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:186:            ComposerKt.traceEventStart(-776179197, i, -1, "androidx.compose.material.DefaultTextFieldForExposedDropdownMenusColors.leadingIconColor (ExposedDropdownMenu.kt:504)");
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:200:            ComposerKt.traceEventStart(1742462291, i, -1, "androidx.compose.material.DefaultTextFieldForExposedDropdownMenusColors.placeholderColor (ExposedDropdownMenu.kt:572)");
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:214:            ComposerKt.traceEventStart(394526077, i, -1, "androidx.compose.material.DefaultTextFieldForExposedDropdownMenusColors.textColor (ExposedDropdownMenu.kt:595)");
classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java:228:            ComposerKt.traceEventStart(79259602, i, -1, "androidx.compose.material.DefaultTextFieldForExposedDropdownMenusColors.trailingIconColor (ExposedDropdownMenu.kt:531)");
```

### js_bridge — 5 hits in 4 files

- `classes7:com/waze/sharedui/web/WazeWebView.java` (2)
- `classes4:androidx/webkit/RestrictionAllowlist.java` (1)
- `classes6:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface$Config.java` (1)
- `classes7:com/waze/settings/q.java` (1)

```
classes4:androidx/webkit/RestrictionAllowlist.java:39:            config.addJavascriptInterface(obj, str, this.mOriginPatterns);
classes6:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface$Config.java:32:    public void addJavascriptInterface(Object obj, String str, List<String> list) {
classes7:com/waze/sharedui/web/WazeWebView.java:180:            this.c.addJavascriptInterface(this.b, "androidSystemInterface");
classes7:com/waze/sharedui/web/WazeWebView.java:184:                cVar2.addJavascriptInterface(this.a, "androidInterface");
classes7:com/waze/settings/q.java:24:        ((WazeWebView) this.a).c.addJavascriptInterface(obj, str);
```

### boot_persist — 4 hits in 1 files

- `classes3:androidx/core/app/AlarmManagerCompat.java` (4)

```
classes3:androidx/core/app/AlarmManagerCompat.java:32:    public static void setAlarmClock(AlarmManager alarmManager, long j, PendingIntent pendingIntent, PendingIntent pendingIntent2) {
classes3:androidx/core/app/AlarmManagerCompat.java:33:        alarmManager.setAlarmClock(new AlarmManager.AlarmClockInfo(j, pendingIntent), pendingIntent2);
classes3:androidx/core/app/AlarmManagerCompat.java:46:    public static void setExactAndAllowWhileIdle(AlarmManager alarmManager, int i, long j, PendingIntent pendingIntent) {
classes3:androidx/core/app/AlarmManagerCompat.java:47:        alarmManager.setExactAndAllowWhileIdle(i, j, pendingIntent);
```

### full_screen_intent — 4 hits in 3 files

- `classes3:androidx/core/app/NotificationCompat.java` (2)
- `classes3:androidx/core/app/NotificationCompatBuilder.java` (1)
- `classes3:androidx/core/app/NotificationManagerCompat.java` (1)

```
classes3:androidx/core/app/NotificationCompatBuilder.java:174:        builderCreateBuilder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, builder.mTickerView).setVibrate(notification.vibrate).
classes3:androidx/core/app/NotificationManagerCompat.java:483:        return Build.VERSION.SDK_INT < 34 ? this.mContext.checkSelfPermission("android.permission.USE_FULL_SCREEN_INTENT") == 0 : Api34Impl.canUseFullScreenIntent(this.mNotificationManager);
classes3:androidx/core/app/NotificationCompat.java:1683:            Builder defaults = number.setContentIntent(notification.contentIntent).setDeleteIntent(notification.deleteIntent).setFullScreenIntent(notification.fullScreenIntent, NotificationCompat.getHighPriority(notification)).setSound(notifica
classes3:androidx/core/app/NotificationCompat.java:2055:        public Builder setFullScreenIntent(PendingIntent pendingIntent, boolean z) {
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 82 hits in 45 files

- `classes3:androidx/core/widget/TextViewKt.java` (22)
- `classes3:androidx/core/widget/TextViewKt$addTextChangedListener$textWatcher$1.java` (6)
- `classes7:com/waze/reports/ax.java` (5)
- `classes3:androidx/emoji2/text/SpannableBuilder.java` (3)
- `classes2:android/support/v7/widget/y.java` (2)
- `classes4:com/google/android/material/button/MaterialButton.java` (2)
- `classes7:com/waze/reports/g.java` (2)
- `classes7:com/waze/reports/GasPriceReportActivity.java` (2)
- `classes7:com/waze/reports/bk.java` (2)
- `classes3:androidx/emoji2/viewsintegration/EmojiTextWatcher.java` (1)
- `classes3:androidx/emoji2/viewsintegration/EmojiEditTextHelper.java` (1)
- `classes4:com/google/android/material/internal/m.java` (1)

```
classes2:android/support/v7/widget/y.java:164:    protected void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes2:android/support/v7/widget/y.java:165:        super.onTextChanged(charSequence, i, i2, i3);
classes3:androidx/core/widget/TextViewKt.java:14:    public static final TextWatcher addTextChangedListener(TextView textView, r<? super CharSequence, ? super Integer, ? super Integer, ? super Integer, ab> rVar, r<? super CharSequence, ? super Integer, ? super Integer, ? super Integer, ab> rVar2, l<
classes3:androidx/core/widget/TextViewKt.java:17:        x.f(rVar2, "onTextChanged");
classes3:androidx/core/widget/TextViewKt.java:19:        TextViewKt$addTextChangedListener$textWatcher$1 textViewKt$addTextChangedListener$textWatcher$1 = new TextViewKt$addTextChangedListener$textWatcher$1(lVar, rVar, rVar2);
classes3:androidx/core/widget/TextViewKt.java:20:        textView.addTextChangedListener(textViewKt$addTextChangedListener$textWatcher$1);
classes3:androidx/core/widget/TextViewKt.java:21:        return textViewKt$addTextChangedListener$textWatcher$1;
classes3:androidx/core/widget/TextViewKt.java:24:    public static /* synthetic */ TextWatcher addTextChangedListener$default(TextView textView, r rVar, r rVar2, l lVar, int i, Object obj) {
classes3:androidx/core/widget/TextViewKt.java:26:            rVar = new r<CharSequence, Integer, Integer, Integer, ab>() { // from class: androidx.core.widget.TextViewKt.addTextChangedListener.1
classes3:androidx/core/widget/TextViewKt.java:39:            rVar2 = new r<CharSequence, Integer, Integer, Integer, ab>() { // from class: androidx.core.widget.TextViewKt.addTextChangedListener.2
classes3:androidx/core/widget/TextViewKt.java:52:            lVar = new l<Editable, ab>() { // from class: androidx.core.widget.TextViewKt.addTextChangedListener.3
classes3:androidx/core/widget/TextViewKt.java:63:        x.f(rVar2, "onTextChanged");
```

### webview_tracking — 0 hits in 0 files


```
```

### streaks — 0 hits in 0 files


```
```

### reengagement — 1061 hits in 241 files

- `classes2:androidx/compose/material3/ExitUntilCollapsedScrollBehavior$nestedScrollConnection$1.java` (39)
- `classes2:androidx/compose/material3/AppBarKt.java` (37)
- `classes5:com/waze/R.java` (32)
- `classes2:androidx/compose/material3/FloatingToolbarKt.java` (30)
- `classes3:androidx/core/app/NotificationCompat.java` (26)
- `classes:androidx/compose/foundation/text/input/internal/selection/TextFieldSelectionState.java` (22)
- `classes:androidx/compose/foundation/text/input/internal/selection/SelectionMovementDeletionContext.java` (21)
- `classes4:androidx/media3/exoplayer/util/SntpClient.java` (18)
- `classes6:com/waze/jni/protos/RtAlertsThumbsUpDataProto.java` (18)
- `classes:androidx/compose/foundation/text/selection/TextFieldSelectionManager.java` (17)
- `classes2:androidx/compose/material3/WideNavigationRailKt.java` (17)
- `classes3:androidx/core/location/LocationCompat.java` (17)

```
classes:androidx/compose/foundation/text/selection/SelectionAdjustmentKt.java:34:        if (SelectionLayoutKt.isCollapsed(selection, selectionLayout)) {
classes:androidx/compose/foundation/text/selection/SelectableInfo.java:46:        return i < i2 ? CrossStatus.NOT_CROSSED : i > i2 ? CrossStatus.CROSSED : CrossStatus.COLLAPSED;
classes:androidx/compose/foundation/text/selection/SelectionAdjustment.java:86:            if (selectionLayout.getCrossStatus() != CrossStatus.CROSSED && (selectionLayout.getCrossStatus() != CrossStatus.COLLAPSED || start.getOffset() <= end2.getOffset())) {
classes:androidx/compose/foundation/text/selection/MultiSelectionLayout.java:33:                iArr[CrossStatus.COLLAPSED.ordinal()] = 1;
classes:androidx/compose/foundation/CombinedClickableNode.java:71:        private boolean doubleTapMinTimeMillisElapsed;
classes:androidx/compose/foundation/CombinedClickableNode.java:78:        public final boolean getDoubleTapMinTimeMillisElapsed() {
classes:androidx/compose/foundation/CombinedClickableNode.java:79:            return this.doubleTapMinTimeMillisElapsed;
classes:androidx/compose/foundation/CombinedClickableNode.java:86:        public final void setDoubleTapMinTimeMillisElapsed(boolean z) {
classes:androidx/compose/foundation/CombinedClickableNode.java:87:            this.doubleTapMinTimeMillisElapsed = z;
classes:androidx/compose/foundation/CombinedClickableNode.java:576:                if (!doubleKeyClickState.getDoubleTapMinTimeMillisElapsed()) {
classes:androidx/compose/foundation/text/selection/BaseTextPreparedSelection.java:220:            if (TextRange.m5660getCollapsedimpl(this.selection)) {
classes:androidx/compose/foundation/text/selection/BaseTextPreparedSelection.java:238:            if (TextRange.m5660getCollapsedimpl(this.selection)) {
```

### notif_permission_nag — 16 hits in 2 files

- `classes8:i/b/l/hi.java` (10)
- `classes8:i/b/w/o.java` (6)

```
classes8:i/b/w/o.java:34:        ensurePromptsIsMutable();
classes8:i/b/w/o.java:41:        ensurePromptsIsMutable();
classes8:i/b/w/o.java:50:    private void ensurePromptsIsMutable() {
classes8:i/b/w/o.java:80:        ensurePromptsIsMutable();
classes8:i/b/w/o.java:87:        ensurePromptsIsMutable();
classes8:i/b/w/o.java:155:        ensurePromptsIsMutable();
classes8:i/b/l/hi.java:87:        ensurePromptIconsIsMutable();
classes8:i/b/l/hi.java:93:        ensurePromptIdsIsMutable();
classes8:i/b/l/hi.java:152:        ensurePromptIconsIsMutable();
classes8:i/b/l/hi.java:158:        ensurePromptIconsIsMutable();
classes8:i/b/l/hi.java:165:        ensurePromptIdsIsMutable();
classes8:i/b/l/hi.java:171:        ensurePromptIdsIsMutable();
```

### cancellation_retention — 3 hits in 1 files

- `classes2:androidx/camera/view/PreviewStreamStateObserver.java` (3)

```
classes2:androidx/camera/view/PreviewStreamStateObserver.java:45:    private void cancelFlow() {
classes2:androidx/camera/view/PreviewStreamStateObserver.java:99:        cancelFlow();
classes2:androidx/camera/view/PreviewStreamStateObserver.java:139:                cancelFlow();
```

### urgency_countdown — 150 hits in 34 files

- `classes3:androidx/core/app/NotificationCompat.java` (19)
- `classes7:e/a/f/x.java` (11)
- `classes2:androidx/camera/camera2/pipe/compat/CaptureSessionState.java` (10)
- `classes7:e/a/f/ac.java` (7)
- `classes2:androidx/camera/core/impl/utils/Threads.java` (6)
- `classes2:androidx/camera/core/impl/utils/futures/ChainingListenableFuture.java` (6)
- `classes2:androidx/camera/camera2/pipe/compat/AndroidCameraState.java` (6)
- `classes5:com/google/firebase/crashlytics/a/g/e.java` (6)
- `classes2:androidx/camera/camera2/pipe/compat/Camera2DeviceCloserImpl.java` (5)
- `classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java` (5)
- `classes4:com/google/android/gms/n/ad.java` (5)
- `classes5:com/google/firebase/crashlytics/a/c/ay.java` (5)

```
classes2:androidx/camera/core/impl/utils/Threads.java:6:import java.util.concurrent.CountDownLatch;
classes2:androidx/camera/core/impl/utils/Threads.java:37:    static /* synthetic */ void lambda$runOnMainSync$0(Runnable runnable, CountDownLatch countDownLatch) {
classes2:androidx/camera/core/impl/utils/Threads.java:41:            countDownLatch.countDown();
classes2:androidx/camera/core/impl/utils/Threads.java:58:        final CountDownLatch countDownLatch = new CountDownLatch(1);
classes2:androidx/camera/core/impl/utils/Threads.java:62:                Threads.lambda$runOnMainSync$0(runnable, countDownLatch);
classes2:androidx/camera/core/impl/utils/Threads.java:66:            if (countDownLatch.await(TIMEOUT_RUN_ON_MAIN_MS, TimeUnit.MILLISECONDS)) {
classes2:androidx/camera/core/impl/utils/futures/ChainingListenableFuture.java:9:import java.util.concurrent.CountDownLatch;
classes2:androidx/camera/core/impl/utils/futures/ChainingListenableFuture.java:22:    private final CountDownLatch mOutputCreated = new CountDownLatch(1);
classes2:androidx/camera/core/impl/utils/futures/ChainingListenableFuture.java:98:            CountDownLatch countDownLatch = this.mOutputCreated;
classes2:androidx/camera/core/impl/utils/futures/ChainingListenableFuture.java:100:            if (!countDownLatch.await(j, timeUnit)) {
classes2:androidx/camera/core/impl/utils/futures/ChainingListenableFuture.java:113:    /* JADX WARN: Type inference failed for: r4v3, types: [java.util.concurrent.CountDownLatch] */
classes2:androidx/camera/core/impl/utils/futures/ChainingListenableFuture.java:155:                    this.mOutputCreated.countDown();
```

### infinite_autoplay — 13 hits in 2 files

- `classes4:com/google/d/i/g.java` (10)
- `classes5:com/waze/R.java` (3)

```
classes4:com/google/d/i/g.java:36:    public static final int VIDEO_AUTOPLAY_ENABLED_FIELD_NUMBER = 17;
classes4:com/google/d/i/g.java:56:    private boolean videoAutoplayEnabled_;
classes4:com/google/d/i/g.java:171:    public void clearVideoAutoplayEnabled() {
classes4:com/google/d/i/g.java:173:        this.videoAutoplayEnabled_ = false;
classes4:com/google/d/i/g.java:305:    public void setVideoAutoplayEnabled(boolean z) {
classes4:com/google/d/i/g.java:307:        this.videoAutoplayEnabled_ = z;
classes4:com/google/d/i/g.java:319:            return newMessageInfo(DEFAULT_INSTANCE, "\u0001\u0013\u0000\u0001\u0001\u0013\u0013\u0000\u0000\u0000\u0001ဇ\u0000\u0002ဇ\u0001\u0003ဇ\u0002\u0004ဇ\u0003\u0005ဇ\u0004\u0006ဇ\u0005\u0007ဇ\u0006\bဇ\u0007\tဇ\b\nဇ\t\u000bဇ\n\fဇ\u000b\rဇ\f\u000eဇ\r\u000 [...
classes4:com/google/d/i/g.java:406:    public boolean getVideoAutoplayEnabled() {
classes4:com/google/d/i/g.java:407:        return this.videoAutoplayEnabled_;
classes4:com/google/d/i/g.java:482:    public boolean hasVideoAutoplayEnabled() {
classes5:com/waze/R.java:973:        public static final int lottie_autoPlay = 0x7f0403b4;
classes5:com/waze/R.java:9949:        public static final int LottieAnimationView_lottie_autoPlay = 0x00000001;
```

### badges — 28 hits in 11 files

- `classes3:androidx/datastore/preferences/protobuf/DescriptorProtos.java` (9)
- `classes3:androidx/core/app/NotificationCompatBuilder.java` (4)
- `classes3:androidx/core/app/NotificationCompat.java` (3)
- `classes3:androidx/datastore/preferences/protobuf/EnumValue.java` (3)
- `classes3:androidx/datastore/preferences/protobuf/Field.java` (3)
- `classes3:com/google/firebase/messaging/c.java` (1)
- `classes5:com/google/p/a/a/b.java` (1)
- `classes5:com/google/k/a/a/b/jj.java` (1)
- `classes5:com/google/v/ar.java` (1)
- `classes5:com/google/k/a/a/b/dy.java` (1)
- `classes5:com/google/k/a/a/b/r.java` (1)

```
classes3:com/google/firebase/messaging/c.java:177:            builder.setNumber(numC4.intValue());
classes3:androidx/core/app/NotificationCompatBuilder.java:67:        static Notification.Builder setBadgeIconType(Notification.Builder builder, int i) {
classes3:androidx/core/app/NotificationCompatBuilder.java:68:            return builder.setBadgeIconType(i);
classes3:androidx/core/app/NotificationCompatBuilder.java:174:        builderCreateBuilder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, builder.mTickerView).setVibrate(notification.vibrate).
classes3:androidx/core/app/NotificationCompatBuilder.java:248:        Api26Impl.setBadgeIconType(this.mBuilder, builder.mBadgeIcon);
classes3:androidx/core/app/NotificationCompat.java:1681:            Builder number = usesChronometer.setOngoing(NotificationCompat.getOngoing(notification)).setLocalOnly(NotificationCompat.getLocalOnly(notification)).setLargeIcon(notification.largeIcon).setBadgeIconType(NotificationCompat.getBadgeIc
classes3:androidx/core/app/NotificationCompat.java:1955:        public Builder setBadgeIconType(int i) {
classes3:androidx/core/app/NotificationCompat.java:2110:        public Builder setNumber(int i) {
classes3:androidx/datastore/preferences/protobuf/EnumValue.java:147:    public void setNumber(int i) {
classes3:androidx/datastore/preferences/protobuf/EnumValue.java:317:        public Builder setNumber(int i) {
classes3:androidx/datastore/preferences/protobuf/EnumValue.java:319:            ((EnumValue) this.instance).setNumber(i);
classes3:androidx/datastore/preferences/protobuf/DescriptorProtos.java:4111:            public void setNumber(int i) {
```

### minors_age — 2 hits in 2 files

- `classes3:androidx/core/content/PackageManagerCompat.java` (1)
- `classes6:com/waze/config/ConfigValues.java` (1)

```
classes3:androidx/core/content/PackageManagerCompat.java:52:            if (packageManager.checkPermission("android.permission.PACKAGE_VERIFICATION_AGENT", str2) == 0) {
classes6:com/waze/config/ConfigValues.java:74814:        return "https://storagegateway-row.waze.com/StorageGateway/upload_log";
```

### screen_time — 1 hits in 1 files

- `classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java` (1)

```
classes4:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:253:        map.put("time_spent", Long.toString(j2));
```

## UI string categories (default locale)

### loss_aversion_copy — 2 strings

```
strings.xml:637:    <string name="BEACONS_GO_TO_SETTINGS_FOR_PERMISSIONS_TITLE">Don’t lose your signal - turn on Bluetooth</string>
strings.xml:3172:    <string name="SHARE_DRIVE_LIVE_DRIVE_STOP_SHARING_CONFIRMATION_DIALOG_SUBTITLE">This will end your shared drive</string>
```

### urgency_copy — 0 strings

```
```

### confirmshaming_copy — 23 strings

```
strings.xml:382:    <string name="ALERTER_NO_THANKS">No thanks</string>
strings.xml:576:    <string name="AUDIO_SDK_DATA_SHARING_DECLINE">No thanks</string>
strings.xml:626:    <string name="BEACONS_BLUETOOTH_PERMISSIONS_RATIONALE_BUTTON2">No thanks</string>
strings.xml:635:    <string name="BEACONS_GO_TO_SETTINGS_FOR_PERMISSIONS_BUTTON2">No thanks</string>
strings.xml:639:    <string name="BEACONS_TURN_ON_BLUETOOTH_BUTTON2">No thanks</string>
strings.xml:897:    <string name="CONVERSATIONAL_REPORTING_ACTIVATION_DIALOG_CTA_CANCEL">Not now</string>
strings.xml:901:    <string name="CONVERSATIONAL_REPORTING_ACTIVATION_DIALOG_SECONDARY_CTA_NO_PERMISSION">Not now</string>
strings.xml:1156:    <string name="DECLINE">No thanks</string>
strings.xml:1502:    <string name="FUTURE_DRIVES_LOCATION_PERMISSION_DIALOG_NO_TEXT">No thanks</string>
strings.xml:1597:    <string name="GOOGLE_ASSISTANT_BOTTOM_SHEET_INTRO_CANCEL_BUTTON">Not now</string>
strings.xml:1600:    <string name="GOOGLE_ASSISTANT_BOTTOM_SHEET_ONBOARDING_ALTERNATIVE_CANCEL_BUTTON">No thanks</string>
strings.xml:1647:    <string name="GOOGLE_ASSISTANT_ONBOARDING_CANCEL_BUTTON_DEFAULT">Not now</string>
strings.xml:1648:    <string name="GOOGLE_ASSISTANT_ONBOARDING_CANCEL_BUTTON_MIC_OPT_IN_FLOW">No thanks</string>
strings.xml:1825:    <string name="INSIGHT_FEEDBACK_GOTO_SETTINGS_NO_BUTTON">No thanks</string>
strings.xml:2334:    <string name="NOT_NOW">Not now</string>
strings.xml:2348:    <string name="NO_THANKS">No thanks</string>
strings.xml:2426:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_CANCEL_BUTTON_TITLE">Not now</string>
strings.xml:2428:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_ANDROID_CANCEL_BUTTON_TITLE">No thanks</string>
strings.xml:2541:    <string name="PRIVACY_CONCENT_BUMP_BG_LOCATION_BUTTON_NO_THANKS">No thanks</string>
strings.xml:2543:    <string name="PRIVACY_CONCENT_BUMP_BG_LOCATION_CONFIRM_BUTTON_DONT_ALLOW">No thanks</string>
strings.xml:2971:    <string name="SEARCH_MATE_MIC_PERMISSION_DIALOG_NOT_NOW">Not now</string>
strings.xml:3134:    <string name="SHARE_DRIVE_JOIN_PREVIEW_CARPLAY_NO_THANKS_BUTTON">No thanks</string>
strings.xml:3509:    <string name="TRANSPORTATION_CUSTOMIZATION_POPUP_NO_BUTTON">No thanks</string>
```

### social_pressure_copy — 4 strings

```
strings.xml:2197:    <string name="MY_PROFILE_GUEST_MOOD_SEEN">Your mood is seen by other Wazers when you drive</string>
strings.xml:4040:    <string name="com.google.firebase.crashlytics.mapping_file_id">686ffacbed574c47ab5bc6e15392b429</string>
strings.xml:4148:    <string name="firebase_database_url">https://api-project-1005457359603.firebaseio.com</string>
strings.xml:4160:    <string name="google_storage_bucket">api-project-1005457359603.firebasestorage.app</string>
```

### guilt_copy — 3 strings

```
strings.xml:601:    <string name="AUTH_FLOW_COMPLETE_MSG">Welcome back!</string>
strings.xml:2004:    <string name="LOGIN_MAIN_TITLE">Welcome back, Wazer!</string>
strings.xml:4091:    <string name="contentDescription_generalSettingsAdSettingsLabel">generalSettingsAdSettingsLabel</string>
```

### subscription_copy — 21 strings

```
strings.xml:526:    <string name="ALT_ROUTE_LABEL_HOV_REQUIRES_SUBSCRIPTION">Requires a pass</string>
strings.xml:568:    <string name="AUDIO_SDK_APPLE_MUSIC_NO_SUBSCRIPTION_DIALOG_BUTTON_TITLE">Open Apple Music</string>
strings.xml:569:    <string name="AUDIO_SDK_APPLE_MUSIC_NO_SUBSCRIPTION_DIALOG_SUBTITLE">To listen to Apple Music in Waze, link your Apple Music account. Active subscription required.</string>
strings.xml:570:    <string name="AUDIO_SDK_APPLE_MUSIC_NO_SUBSCRIPTION_DIALOG_TITLE">Connect Apple Music</string>
strings.xml:599:    <string name="AUDIO_SDK_SUBSCRIPTION_DIALOG_CANCEL_BUTTON_TITLE">Cancel</string>
strings.xml:910:    <string name="CONVERSATIONAL_REPORTING_CANCEL_MAX_MESSAGES_BUTTON">Paused. Tap to resume.</string>
strings.xml:1081:    <string name="CUSTOM_PROMPTS_X_SECONDS_MAX">%d seconds max</string>
strings.xml:1298:    <string name="ECO_REGULATIONS_LOWER_SPEED_ITINERARY_MESSAGE_PD_PS_PD" formatted="false">Driving %d %s max on highways adds %d min &amp; saves CO₂</string>
strings.xml:1982:    <string name="LOCK_SCREEN_NAVIGATION_ALERT_CLICK_MESSAGE">Unlock your phone to view</string>
strings.xml:1983:    <string name="LOCK_SCREEN_NAVIGATION_BANNER_CLICK_MESSAGE">Unlock your phone to view</string>
strings.xml:1984:    <string name="LOCK_SCREEN_NAVIGATION_DETAILS_POPUP_BLOCKED_MESSAGE">Unlock your phone to view</string>
strings.xml:1985:    <string name="LOCK_SCREEN_NAVIGATION_DIRECTIONS_ETA_EXPAND_MESSAGE">Unlock your phone to view</string>
strings.xml:1987:    <string name="LOCK_SCREEN_NAVIGATION_GA_CLICK_MESSAGE">Unlock your phone to view</string>
strings.xml:1988:    <string name="LOCK_SCREEN_NAVIGATION_MUSIC_BUTTON_CLICK_MESSAGE">Unlock your phone to view</string>
strings.xml:1989:    <string name="LOCK_SCREEN_NAVIGATION_SETTINGS_BLOCKED_MESSAGE">Unlock your phone to view</string>
strings.xml:2118:    <string name="MAX_PD_CHARACTERS">Max. %d Characters</string>
strings.xml:2359:    <string name="OGOTTA_DRIVE_PDP_PS_TO_ACCESS_OTHER_MOODSU" formatted="false">(You need to drive %d+ %s to unlock other moods)</string>
strings.xml:3942:    <string name="YOUSRE_A_BABY_WAZER_NOW_H_BUT_NOT_FOR_LONGE_DRIVE_PD_PS_TO_UNLOCK_MOODS___" formatted="false">Drive at least %d %s to unlock more moods</string>
strings.xml:4176:    <string name="m3_exceed_max_badge_text_suffix">%1$s%2$s</string>
strings.xml:4319:    <string name="mtrl_exceed_max_badge_number_content_description">More than %1$d new notifications</string>
strings.xml:4320:    <string name="mtrl_exceed_max_badge_number_suffix">%1$d%2$s</string>
```

### data_copy — 392 strings

```
strings.xml:9:    <string name="AADC_REQUEST_AGE_SCREEN_BODY">"To make sure your data is used according to legal requirements and Google policy, you need to enter your age. Your age won't be shown publicly or used for advertising purposes."</string>
strings.xml:20:For example: GPS locations and past routes, as well as any addresses, voice recordings, and other info you choose to share with Waze.
strings.xml:23:To provide you with personalized experiences of our services, including ads presented to you; maintain &amp; improve our services, and more.
strings.xml:57:    <string name="AAOS_ADDRESS_PREVIEW_LOCATION_TITLE">Location</string>
strings.xml:121:    <string name="AAOS_PERMISSION_DENIED_SCREEN_MESSAGE">Waze needs your location to work</string>
strings.xml:123:    <string name="AAOS_PRIVACY_SETTINGS_DELETE_RECENT_DESTINATION_MESSAGE">"Remove this location from your car?
strings.xml:124:If you’ve driven to this location, it’s also saved in your navigation history (and be deleted from your phone)"</string>
strings.xml:140:    <string name="AAOS_PRIVACY_SETTINGS_PERSONALIZED_ADS_OFF_MESSAGE">"Turn on personalized ads?
strings.xml:142:See ads based on info you’ve added to your Waze account and data from trusted ad partners. To learn more, visit our Privacy Policy."</string>
strings.xml:143:    <string name="AAOS_PRIVACY_SETTINGS_PERSONALIZED_ADS_ON_MESSAGE">"Turn off personalized ads?
strings.xml:146:    <string name="AAOS_PRIVACY_SETTINGS_PERSONALIZED_ADS_TITLE">Personalized ads</string>
strings.xml:147:    <string name="AAOS_PRIVACY_SETTINGS_RECENT_DESTINATION_EMPTY_MESSAGE">No recent locations</string>
strings.xml:148:    <string name="AAOS_PRIVACY_SETTINGS_RECENT_DESTINATION_MESSAGE">"Recent locations
strings.xml:149:View or remove recent locations from Waze in this car"</string>
strings.xml:152:    <string name="AAOS_PRIVACY_SETTINGS_TRIP_SUGGESTIONS_DESCRIPTION">Get trip suggestions based on your daily commute, saved places, and recent locations</string>
strings.xml:155:Get trip suggestions based on your daily commute, saved places, and recent locations"</string>
strings.xml:158:Stop getting trip suggestions based on your daily commute, saved places, and recent locations"</string>
strings.xml:182:    <string name="AAOS_REQUEST_PERMISSION_SCREEN_MESSAGE">To use all of Waze’s many useful features, Waze needs to access your location</string>
strings.xml:216:    <string name="AAOS_SEARCH_ND4C_CONTENT">Search results are based on distance, location, and more. Prices, opening hours, and other info is collected from different sources, like user contributions and third parties, and may not be accurate or updated in re [... omitted end of lon
strings.xml:269:    <string name="AAP_GPS_DISABLED_MESSAGE">When it’s safe, open Waze on your phone to give location permission</string>
strings.xml:270:    <string name="AAP_GPS_DISABLED_TITLE">Location disabled</string>
strings.xml:356:    <string name="ADS_SETTINGS_GENERAL_SETTING_ITEM">Ads personalization</string>
strings.xml:357:    <string name="ADS_SETTINGS_PROFILE_TARGETING_DESCRIPTION">"Ads are based on info you've added to your Waze account and data from trusted ad partners. When this is turned off, you'll still see ads, but they may be less useful to you. To learn more, visit ou [... omitted end of lon
strings.xml:358:    <string name="ADS_SETTINGS_PROFILE_TARGETING_DESCRIPTION_IOS">"Personalized ads are based on info you've added to your Waze account and your app activity. When this is turned off, you'll still see ads, but they may be less useful to you. To learn more, vis [... omitted end of lon
strings.xml:359:    <string name="ADS_SETTINGS_PROFILE_TARGETING_ITEM">Personalize your ads</string>
strings.xml:360:    <string name="ADS_SETTINGS_TITLE">Ads personalization</string>
strings.xml:605:    <string name="AUTOCOMPLETE_CURRENT_LOCATION">Your location</string>
strings.xml:607:    <string name="AUTOCOMPLETE_OPEN_CATEGORY_SEARCH">See locations</string>
strings.xml:608:    <string name="AUTOCOMPLETE_SELECT_ON_MAP">Current location</string>
strings.xml:667:    <string name="CALENDAR_CONFIRM_BLOCK_ADDRESS_BODY">"Meetings with this location won't show on your navigation list and you will not get reminders for them"</string>
strings.xml:668:    <string name="CALENDAR_CONFIRM_BLOCK_ADDRESS_OK">Ignore location</string>
strings.xml:718:    <string name="CANST_FIND_A_ROAD_NEAR_DESTINATION_POINT_">Destination not found. Review the location and try again.</string>
strings.xml:749:    <string name="CARPLAY_LOCATION_PERMISSION_OVERVIEW_SHORT">When safe, turn on Location Services on your phone</string>
strings.xml:750:    <string name="CARPLAY_LOCATION_PERMISSION_REQUIRES_PHONE">Open Waze on your phone to provide access to your location</string>
strings.xml:813:    <string name="CARPOOL_LOCATION_PICKER_EDIT_BUTTON">Edit route</string>
strings.xml:814:    <string name="CARPOOL_LOCATION_PICKER_LOCATING">Locating...</string>
strings.xml:815:    <string name="CARPOOL_LOCATION_PICKER_UNKNOWN_ADDRESS">Can’t find address. Adjust pin.</string>
strings.xml:890:    <string name="CONSENT_BUMP_MAIN_TEXT">"&lt;style type=\"text/css\">body{font-family: sans-serif;color: #717171;padding-left: 16px;padding-right: 16px;font-size: 15px;line-height: 1.2;}a{color: #717171;}h1{font-size: 26px;font-weight: bold;color: #4C4C4C;te [... omitted end of lon
strings.xml:892:    <string name="CONSENT_BUMP_MOBILE_BODY_HTML">"&lt;!--copy-id=TOS_TESTING-->&lt;style type=\"text/css\">body{font-family: sans-serif;color: #717171;padding-left: 16px;padding-right: 16px;font-size: 15px;line-height: 1.2;}a{color: #717171;}h1{font-size: 26px [... omitted end of lon
strings.xml:895:    <string name="CONTACTS_PERMISSION_OVERVIEW">Before you continue, allow Waze access to your Contacts in your device settings.</string>
strings.xml:1050:    <string name="CRISIS_RESPONSE_LOAD_FAILED_MESSAGE">Failed to load location</string>
strings.xml:1139:    <string name="DANGEROUS_ADDRESS_SAVE1">"This location is in a high risk area or prohibited to Israelis by law.
strings.xml:1143:    <string name="DANGEROUS_ADDRESS_SAVE_BUTTON">Confirm location</string>
strings.xml:1162:    <string name="DEFAULT_PERMISSION_HEADER">Waze needs your precise location to give you turn-by-turn directions and reminders to leave.</string>
strings.xml:1173:    <string name="DESTINATION_CELL_CONTACTS_TITLE">Drive to friends and family</string>
strings.xml:1174:    <string name="DESTINATION_CELL_COTACTS_SUBTITLE">Search contacts</string>
strings.xml:1177:    <string name="DESTINATION_CELL_UNKNOWN_LOCATION">Unknown location</string>
strings.xml:1184:    <string name="DESTINATION_MENU_CALENDAR_EVENT_CHANGE_LOCATION">Change location</string>
strings.xml:1219:    <string name="DESTINATION_MENU_SEND_LOCATION">Send location</string>
strings.xml:1310:    <string name="EMAIL_BODY2">Click the link below to share your location with me.</string>
strings.xml:1313:    <string name="EMAIL_SUBJECT">I want to drive to you, send me your location.</string>
strings.xml:1317:    <string name="ENABLE_CONTACTS_SEARCH">Enable contacts search</string>
strings.xml:1446:    <string name="EV_VENUE_PLUG_AVAILABILITY_POPUP_BODY">Plug details are collected from different sources, such as third parties and user contributions, and may not be accurate or updated in real-time.</string>
strings.xml:1484:    <string name="FUTURE_DRIVES_ERROR_NO_CURRENT_LOCATION">Your current location is unavailable. Choose an address as your starting point.</string>
strings.xml:1497:    <string name="FUTURE_DRIVES_LIST_NOTIFY_ME_DESCRIPTION">"For better accuracy, choose \"Always on\" in your device's location settings"</string>
strings.xml:1502:    <string name="FUTURE_DRIVES_LOCATION_PERMISSION_DIALOG_NO_TEXT">No thanks</string>
strings.xml:1503:    <string name="FUTURE_DRIVES_LOCATION_PERMISSION_DIALOG_TEXT">Go to Settings and then</string>
strings.xml:1504:    <string name="FUTURE_DRIVES_LOCATION_PERMISSION_DIALOG_TITLE">Wait a sec...</string>
strings.xml:1505:    <string name="FUTURE_DRIVES_LOCATION_PERMISSION_DIALOG_YES_TEXT">Settings</string>
strings.xml:1509:    <string name="FUTURE_DRIVES_PLAN_CURRENT_LOCATION">Your location</string>
strings.xml:1523:    <string name="FUTURE_DRIVES_TIME_TO_LEAVE_FOOTER_CELL_TEXT">"For better accuracy, choose \"Always on\" in your device's location settings"</string>
strings.xml:1524:    <string name="FUTURE_DRIVES_TIME_TO_LEAVE_FOOTER_CELL_TEXT_NOTIFICATIONS_OFF">"For better accuracy, choose \"Always on\" in your device's location settings"</string>
strings.xml:1550:    <string name="GDPR_CONSENT_MAIN_HTML">"&lt;h1>Data and privacy&lt;/h1>&lt;When you use our service an account is created for you and your information is processed as described in our &lt;a href='https://www.waze.com/en/legal/privacy/?back_only=T'>Privacy P [... omitted end of lo
strings.xml:1581:    <string name="GOOGLE_ADS_AD_PIN_IN_CAR_MANAGE_PREFERENCES">This ad is based on your approximate location</string>
strings.xml:1582:    <string name="GOOGLE_ADS_AD_PIN_IN_CAR_MANAGE_PREFERENCES_DESCRIPTION">To report this advertiser, visit adstransparency.google.com when you can do so safely</string>
strings.xml:1782:    <string name="HTML_MAKE_SURE_LOCATION_AND_WAZE_SWITCHED_ON">Make sure both &lt;b>Location Services&lt;/b> and &lt;b>Waze&lt;/b> are switched on</string>
strings.xml:1785:    <string name="HTML_SELECT_CONTACTS">Next, select &lt;b>Contacts&lt;/b></string>
strings.xml:1786:    <string name="HTML_SELECT_LOCATION">Next, select &lt;b>Location Services&lt;/b></string>
strings.xml:1882:    <string name="LOCATION">Location</string>
strings.xml:1883:    <string name="LOCATION_FAILED">"Can't find your location. Make sure your phone's location settings are on and you're connected to the internet."</string>
strings.xml:1884:    <string name="LOCATION_PERMISSION_ENABLE_LOCATION_ACCESS">Tap Always or While using</string>
strings.xml:1885:    <string name="LOCATION_PERMISSION_ENABLE_PRECISE_LOCATION">Turn on Precise location</string>
strings.xml:1886:    <string name="LOCATION_PERMISSION_OVERVIEW">Go to Settings and then</string>
strings.xml:1887:    <string name="LOCATION_PERMISSION_SELECT_LOCATION">Select Location</string>
strings.xml:1888:    <string name="LOCATION_PREVIEW_24_HOURS">24 hrs</string>
strings.xml:1889:    <string name="LOCATION_PREVIEW_ABOUT">About</string>
strings.xml:1890:    <string name="LOCATION_PREVIEW_ABOUT_THIS_AD_BADGE">Sponsored</string>
strings.xml:1891:    <string name="LOCATION_PREVIEW_ABOUT_TITLE">About us</string>
strings.xml:1892:    <string name="LOCATION_PREVIEW_AD">Ad</string>
strings.xml:1893:    <string name="LOCATION_PREVIEW_ADD_A_STOP_BUTTON">Add stop</string>
strings.xml:1894:    <string name="LOCATION_PREVIEW_ADD_PHOTO">Add photo</string>
strings.xml:1895:    <string name="LOCATION_PREVIEW_CALENDAR_CHANGE_ACTION">Change location</string>
strings.xml:1896:    <string name="LOCATION_PREVIEW_CALENDAR_REMOVE_ACTION">Remove event</string>
strings.xml:1897:    <string name="LOCATION_PREVIEW_CALENDAR_SETTINGS_ACTION">Calendar settings</string>
strings.xml:1898:    <string name="LOCATION_PREVIEW_CALL_BUTTON">Call</string>
strings.xml:1899:    <string name="LOCATION_PREVIEW_CLOSED">Closed</string>
strings.xml:1900:    <string name="LOCATION_PREVIEW_CLOSED_TODAY">Closed</string>
strings.xml:1901:    <string name="LOCATION_PREVIEW_CLOSES_AT">Closes %s</string>
strings.xml:1902:    <string name="LOCATION_PREVIEW_CLOSES_AT_PS">Closes %s</string>
strings.xml:1903:    <string name="LOCATION_PREVIEW_CLOSES_SOON">Closes soon</string>
strings.xml:1904:    <string name="LOCATION_PREVIEW_CLOSES_SOON_AT">Closes soon - %s</string>
strings.xml:1905:    <string name="LOCATION_PREVIEW_CREATED_BY_PS">Created by %s</string>
strings.xml:1906:    <string name="LOCATION_PREVIEW_EDIT_BUTTON">Edit</string>
strings.xml:1907:    <string name="LOCATION_PREVIEW_FAVORITE_POPUP_TITLE">Give it a name</string>
strings.xml:1908:    <string name="LOCATION_PREVIEW_GAS_PRICES_TITLE">Gas prices</string>
strings.xml:1909:    <string name="LOCATION_PREVIEW_GAS_PRICES_TITLE_PS">Gas prices (%s)</string>
strings.xml:1910:    <string name="LOCATION_PREVIEW_GO_BUTTON">Go</string>
strings.xml:1911:    <string name="LOCATION_PREVIEW_GO_LATER_BUTTON">Go later</string>
strings.xml:1912:    <string name="LOCATION_PREVIEW_HOME_SET_BUTTON">Set home</string>
strings.xml:1913:    <string name="LOCATION_PREVIEW_HOME_SET_GO_BUTTON">Set home and go</string>
strings.xml:1914:    <string name="LOCATION_PREVIEW_IMAGES">Photos</string>
strings.xml:1915:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_MENU_INAPPROPRIATE">Inappropriate</string>
strings.xml:1916:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_MENU_LOW_QUALITY">Low quality</string>
strings.xml:1917:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_MENU_TITLE">"What's wrong with this photo?"</string>
strings.xml:1918:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_MENU_UNRELATED">Irrelevant</string>
strings.xml:1919:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_VENUE_CLOSED_MOVED">Closed or moved</string>
strings.xml:1920:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_VENUE_DUPLICATE">Duplicate</string>
strings.xml:1921:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_VENUE_INAPPROPRIATE">Inappropriate</string>
strings.xml:1922:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_VENUE_RESIDENTIAL">Residential place</string>
strings.xml:1923:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_VENUE_SUBTITLE">Sharing publicly - used across Google services</string>
strings.xml:1924:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_VENUE_TITLE">"What's wrong with this place?"</string>
strings.xml:1925:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_VENUE_WRONG_DETAILS">Wrong details</string>
strings.xml:1926:    <string name="LOCATION_PREVIEW_IMAGE_REPORT_VENUE_WRONG_PLACE">"Doesn't match search results"</string>
strings.xml:1927:    <string name="LOCATION_PREVIEW_IN_1_HOUR">in 1 hr</string>
strings.xml:1928:    <string name="LOCATION_PREVIEW_IN_MINUTES_PS">in %d min</string>
strings.xml:1929:    <string name="LOCATION_PREVIEW_MISSING_ADDRESS">Missing address</string>
strings.xml:1930:    <string name="LOCATION_PREVIEW_MORE_BUTTON">More</string>
strings.xml:1931:    <string name="LOCATION_PREVIEW_NEW_DRIVE_BUTTON">New drive</string>
strings.xml:1932:    <string name="LOCATION_PREVIEW_NOW_CLOSED">Closed</string>
strings.xml:1933:    <string name="LOCATION_PREVIEW_NOW_OPEN">Open now</string>
strings.xml:1934:    <string name="LOCATION_PREVIEW_ON_SITE_PARKING">Onsite parking available</string>
strings.xml:1935:    <string name="LOCATION_PREVIEW_OPENING_HOURS_TITLE">Opening hours</string>
strings.xml:1936:    <string name="LOCATION_PREVIEW_OPENS_AT">Opens %s</string>
strings.xml:1937:    <string name="LOCATION_PREVIEW_OPENS_AT_PS">Opens at %s</string>
strings.xml:1938:    <string name="LOCATION_PREVIEW_OPENS_SOON">Opens soon</string>
strings.xml:1939:    <string name="LOCATION_PREVIEW_OPENS_SOON_AT">Opens soon - %s</string>
strings.xml:1940:    <string name="LOCATION_PREVIEW_OPENS_TOMORROW">Opens tomorrow</string>
strings.xml:1941:    <string name="LOCATION_PREVIEW_OPEN_24H">Open 24 hours</string>
strings.xml:1942:    <string name="LOCATION_PREVIEW_PARKING_BOOK">Book parking</string>
strings.xml:1943:    <string name="LOCATION_PREVIEW_PARKING_ETA_PS">Arrive at %s</string>
strings.xml:1944:    <string name="LOCATION_PREVIEW_PARKING_LEGAL_POPUP_BODY">Parking rates are provided by third parties and updated regularly. However, sometimes rates may not be accurate or updated in real-time.</string>
strings.xml:1945:    <string name="LOCATION_PREVIEW_PARKING_LEGAL_POPUP_TITLE">Parking rates</string>
strings.xml:1946:    <string name="LOCATION_PREVIEW_PARKING_MORE">See more parking</string>
strings.xml:1947:    <string name="LOCATION_PREVIEW_PARKING_NO_RESULTS">NO PARKING LOTS FOUND</string>
strings.xml:1948:    <string name="LOCATION_PREVIEW_PARKING_POPULAR">Most popular parking lot</string>
strings.xml:1949:    <string name="LOCATION_PREVIEW_PARKING_RATES">Parking rates</string>
strings.xml:1950:    <string name="LOCATION_PREVIEW_PARKING_TITLE">Nearby parking</string>
strings.xml:1951:    <string name="LOCATION_PREVIEW_PARKING_VIEW">View</string>
strings.xml:1952:    <string name="LOCATION_PREVIEW_PARKING_WALKING_MINUTES_PD">%d min</string>
strings.xml:1953:    <string name="LOCATION_PREVIEW_PARKING_WALK_AND_VENUE_PD_PS" formatted="false">%d min walk from %s</string>
strings.xml:1954:    <string name="LOCATION_PREVIEW_PARKING_WALK_PD_PS" formatted="false">%d min walk to %s</string>
strings.xml:1955:    <string name="LOCATION_PREVIEW_PARK_HERE_BUTTON">Park here</string>
strings.xml:1956:    <string name="LOCATION_PREVIEW_PERMANENTLY_CLOSED">Permanently closed</string>
strings.xml:1957:    <string name="LOCATION_PREVIEW_REMOVE_EVENT_BUTTON">Remove event</string>
strings.xml:1958:    <string name="LOCATION_PREVIEW_REMOVE_FAVORITE_CONFIRMATION_BODY">This address will be cleared from your saved places</string>
strings.xml:1959:    <string name="LOCATION_PREVIEW_REMOVE_FAVORITE_CONFIRMATION_NEGATIVE">Cancel</string>
strings.xml:1960:    <string name="LOCATION_PREVIEW_REMOVE_FAVORITE_CONFIRMATION_POSITIVE">Remove</string>
strings.xml:1961:    <string name="LOCATION_PREVIEW_REMOVE_FAVORITE_CONFIRMATION_TITLE_PS">Remove %s?</string>
strings.xml:1962:    <string name="LOCATION_PREVIEW_REMOVE_FROM_HISTORY_ACTION">Remove from history</string>
strings.xml:1963:    <string name="LOCATION_PREVIEW_REPORT_A_PROBLEM_ACTION">Report a problem</string>
strings.xml:1964:    <string name="LOCATION_PREVIEW_SAVE_BUTTON">Save</string>
strings.xml:1965:    <string name="LOCATION_PREVIEW_SERVICES_TITLE">Onsite services</string>
strings.xml:1966:    <string name="LOCATION_PREVIEW_SET_ADDRESS_BUTTON">Set address</string>
strings.xml:1967:    <string name="LOCATION_PREVIEW_SET_AS_START_POINT_ACTION">Set as start point</string>
strings.xml:1968:    <string name="LOCATION_PREVIEW_SHARE_BUTTON">Share</string>
strings.xml:1969:    <string name="LOCATION_PREVIEW_SHOW_ON_MAP_ACTION">Show on map</string>
strings.xml:1970:    <string name="LOCATION_PREVIEW_TEMPORARILY_CLOSED">Temporarily closed</string>
strings.xml:1971:    <string name="LOCATION_PREVIEW_UNNAMED_ROAD">Unnamed road</string>
strings.xml:1972:    <string name="LOCATION_PREVIEW_UNSAVE_BUTTON">Saved</string>
strings.xml:1973:    <string name="LOCATION_PREVIEW_UPDATED_BY_PS">Last updated by %s</string>
strings.xml:1974:    <string name="LOCATION_PREVIEW_VIEW_ROUTES_BUTTON">View routes</string>
strings.xml:1975:    <string name="LOCATION_PREVIEW_WEBSITE_BUTTON">Website</string>
strings.xml:1976:    <string name="LOCATION_PREVIEW_WORK_SET_BUTTON">Set work</string>
strings.xml:1977:    <string name="LOCATION_PREVIEW_WORK_SET_GO_BUTTON">Set work and go</string>
strings.xml:1978:    <string name="LOCATION_SAVED">Location saved</string>
strings.xml:1979:    <string name="LOCATION_SAVED_WILL_NOTIFY">Saved</string>
strings.xml:2039:    <string name="MAIN_MENU_ALLOW_CONTACTS_LINE1">Search contacts</string>
strings.xml:2040:    <string name="MAIN_MENU_ALLOW_CONTACTS_LINE2">Drive to friends &amp; family</string>
strings.xml:2081:    <string name="MAP_POPUP_MENU_PREVIEW">Preview location</string>
strings.xml:2083:    <string name="MAP_POPUP_MY_LOCATION_SEND_LOCATION_BUTTON">Share location</string>
strings.xml:2084:    <string name="MAP_POPUP_MY_LOCATION_TITLE">You are here</string>
strings.xml:2087:    <string name="MAP_POPUP_PARKED_MENU_EDIT">Edit location</string>
strings.xml:2090:    <string name="MAP_POPUP_PARKED_SEND_LOCATION_BUTTON">Share location</string>
strings.xml:2168:    <string name="MOVE_THE_MAP_TO_ADJUST_PIN_LOCATION">Adjust the pin to show the exact location on the map, including side of street.</string>
strings.xml:2169:    <string name="MOVE_THE_MAP_TO_ADJUST_PIN_LOCATION_NON_RESIDENTIAL">Move the pin to mark the exact location on the map</string>
strings.xml:2170:    <string name="MOVE_THE_MAP_TO_ADJUST_PIN_LOCATION_RESIDENTIAL">Move the pin to mark the exact location on the map, including the correct side of the street</string>
strings.xml:2211:    <string name="NAME_THIS_FAVORITE_LOCATION">Make it memorable</string>
strings.xml:2228:    <string name="NAVIGATION_SETTINGS_PERSONALIZED_ETA">Personalize your ETA</string>
strings.xml:2229:    <string name="NAVIGATION_SETTINGS_PERSONALIZED_ETA_DESCRIPTION_HTML">"Allow Waze to use past drives to calculate your estimated arrival time. &lt;a href='https://support.google.com/waze/answer/10058853'>Learn more&lt;/a>"</string>
strings.xml:2241:    <string name="NAVLIST_OPTIONS_CHANGE_LOCATION">Change location</string>
strings.xml:2251:    <string name="NAVLIST_OPTIONS_SEND_LOCATION">Share location</string>
strings.xml:2252:    <string name="NAVLIST_OPTIONS_SET_LOCATION">Save</string>
strings.xml:2267:    <string name="NAV_CONNECT_CONSENT_HTML_PS_PS_PS_PS_PS_PS" formatted="false">"Your real-time location, distance, and arrival time will be shared with %s to help improve service and driver performance.&lt;br>&lt;ul>&lt;li>&lt;b>%s trips only:&lt;/b> Data is  [... omitted end of lo
strings.xml:2269:    <string name="NAV_CONNECT_CONSENT_WITH_ISV_HTML_PS_PS_PS_PS_PS_PS_PS_PS_PS" formatted="false">"Your real-time location, distance, and arrival time will be shared with %s and %s to help improve service and driver performance.&lt;br>&lt;ul>&lt;li>&lt;b>%s tr [... omitted end of lo
strings.xml:2279:    <string name="ND4C_CONSENT_MAIN_HTML_PS">"&lt;h1>Terms of Service&lt;/h1>&lt;p>Waze is a social navigation app that uses information provided by our users and partners to give you the optimal route.&lt;/p> &lt;p>To use Waze, you need to agree to the &lt;a  [... omitted end of lo
strings.xml:2295:    <string name="NEARING_PARKING_NO_GPS_TEXT">No GPS connection. Waze will mark your parking spot at a nearby location.</string>
strings.xml:2303:    <string name="NEW_LOCATION_PERMISSION_BUTTON">Continue</string>
strings.xml:2304:    <string name="NEW_LOCATION_PERMISSION_BUTTON_SETTINGS">Settings</string>
strings.xml:2305:    <string name="NEW_LOCATION_PERMISSION_LOCATION_DENIED_EXPLANATION_HTML">&lt;p>Waze needs your precise location to give you turn-by-turn directions and other useful features. &lt;a href=\"https://www.waze.com/legal/privacy\">See privacy policy&lt;/a>&lt;/p> [... omitted end of lo
strings.xml:2306:    <string name="NEW_LOCATION_PERMISSION_LOCATION_DENIED_LOW_OS_VERSION_EXPLANATION_HTML">&lt;p>Waze needs your precise location to give you turn-by-turn directions and other useful features. &lt;a href=\"https://www.waze.com/legal/privacy\">See privacy polic [... omitted end of lo
strings.xml:2307:    <string name="NEW_LOCATION_PERMISSION_LOCATION_DENIED_LOW_OS_VERSION_TITLE">"Waze can't work without knowing your precise location"</string>
strings.xml:2308:    <string name="NEW_LOCATION_PERMISSION_LOCATION_DENIED_TITLE">"Waze can't work without knowing your precise location"</string>
strings.xml:2309:    <string name="NEW_LOCATION_PERMISSION_NO_GPS_EXPLANATION_HTML">&lt;p>Device location must be turned on for navigation services to work&lt;/p></string>
strings.xml:2310:    <string name="NEW_LOCATION_PERMISSION_NO_GPS_TITLE">To use Waze, turn on device location</string>
strings.xml:2311:    <string name="NEW_LOCATION_PERMISSION_NO_LOCATION_EXPLANATION_HTML">&lt;p>Waze needs your precise location to give you turn-by-turn directions and other useful features. &lt;a href=\"https://www.waze.com/legal/privacy\">See privacy policy&lt;/a>&lt;/p>&lt; [... omitted end of lo
strings.xml:2312:    <string name="NEW_LOCATION_PERMISSION_NO_LOCATION_LOW_OS_VERSION_EXPLANATION_HTML">&lt;p>Waze needs your precise location to give you turn-by-turn directions and other useful features. &lt;a href=\"https://www.waze.com/legal/privacy\">See privacy policy&lt [... omitted end of lo
strings.xml:2313:    <string name="NEW_LOCATION_PERMISSION_NO_LOCATION_TITLE">Give Waze access to your precise location</string>
strings.xml:2314:    <string name="NEW_LOCATION_PERMISSION_NO_LOCATION_TITLE_LOW_OS_VERSION">Give Waze access to your precise location</string>
strings.xml:2315:    <string name="NEW_LOCATION_PERMISSION_NO_PRECISE_LOCATION_EXPLANATION_HTML">&lt;p>Waze needs your precise location to give you turn-by-turn directions and other useful features. &lt;a href=\"https://www.waze.com/legal/privacy\">See privacy policy&lt;/a>&lt [... omitted end of lo
strings.xml:2339:    <string name="NO_GPS_CONNECTION__MAKE_SURE_YOU_ARE_OUTDOORS__CURRENTLY_SHOWING_APPROXIMATE_LOCATION">"No GPS reception. Make sure you're outdoors."</string>
strings.xml:2341:    <string name="NO_GPS__SHOWING_APPROXIMATE_LOCATION">No GPS - showing your approximate location</string>
strings.xml:2371:    <string name="ONBOARDING_OPTMIZATION_PRIVACY_ADS_CONSENT_TEXT_IOS">"Waze uses info you've added to your account and your app activity to show you personalized ads that are more useful to you. To learn more about how ads work, visit our Privacy Policy."</st [... omitted end of lo
strings.xml:2401:    <string name="PARKED_EDIT_TEXT">Adjust your parking location by moving the map.</string>
strings.xml:2402:    <string name="PARKED_EDIT_TITLE">Parking location</string>
strings.xml:2405:    <string name="PARKED_REMOVED">Location removed</string>
strings.xml:2409:    <string name="PARKED_REMOVE_CONFIRM_WRONG_LOCATION">Wrong location</string>
strings.xml:2412:    <string name="PARKED_UPDATED">Location updated</string>
strings.xml:2428:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_ANDROID_CANCEL_BUTTON_TITLE">No thanks</string>
strings.xml:2429:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_ANDROID_FROM_PLANNED_DRIVE_TEXT">Waze wants to use your location to remind you to leave on time, update you about traffic, and more – even when not using the app</string>
strings.xml:2430:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_ANDROID_FROM_PLANNED_DRIVE_TITLE">Wait a second...</string>
strings.xml:2431:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_ANDROID_FROM_SYNC_CALENDAR_TEXT">Know exactly when to leave, avoid traffic, and more by letting your location run in the background</string>
strings.xml:2432:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_ANDROID_FROM_SYNC_CALENDAR_TITLE">Get the best time to leave</string>
strings.xml:2433:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_ANDROID_GRANT_BUTTON_TITLE">Settings</string>
strings.xml:2434:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_ANDROID_LINK_TITLE">Learn how Waze uses your location</string>
strings.xml:2435:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_FROM_PLANNED_DRIVES_LIST_TEXT">Go to Settings and then</string>
strings.xml:2436:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_FROM_PLANNED_DRIVES_LIST_TITLE">Get the best time to leave</string>
strings.xml:2437:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_FROM_PLANNED_DRIVE_TEXT">Waze wants to use your location to remind you to leave on time, update you about traffic, and more – even when not using the app</string>
strings.xml:2438:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_FROM_PLANNED_DRIVE_TITLE">Wait a second...</string>
strings.xml:2439:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_FROM_SYNC_CALENDAR_TEXT">Go to Settings and then</string>
strings.xml:2440:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_FROM_SYNC_CALENDAR_TITLE">Arrive on time to your events</string>
strings.xml:2441:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_INSTRUCTIONS">Go to ‘Location’ and choose ‘Always’</string>
strings.xml:2442:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_LINK_DEFAULT_BROWSER_TITLE">Your Location</string>
strings.xml:2443:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_LINK_TITLE">Learn how Waze uses your location</string>
strings.xml:2444:    <string name="PERMISSIONS_INSTRUCTIONS_POPUP_LOCATION_LINK_URL">https://www.waze.com/ios_location</string>
strings.xml:2456:    <string name="PERSONALIZED_NAVIGATION_DESCRIPTION_HTML">"&lt;a href='https://support.google.com/waze/answer/16696199'>How personalized navigation works&lt;/a>"</string>
strings.xml:2457:    <string name="PERSONALIZED_NAVIGATION_FOOTER">[How personalized navigation works](https://support.google.com/waze/answer/16696199)</string>
strings.xml:2458:    <string name="PERSONALIZED_NAVIGATION_PERSONALIZED_ROUTES_AND_GUIDANCE_DESCRIPTION">Waze uses your past drives to personalize your routes and spoken directions</string>
strings.xml:2459:    <string name="PERSONALIZED_NAVIGATION_PERSONALIZED_ROUTES_DESCRIPTION">Waze will show routes based on your past drives and route selection</string>
strings.xml:2460:    <string name="PERSONALIZED_NAVIGATION_PERSONALIZED_ROUTES_TITLE">Get personalized routes</string>
strings.xml:2461:    <string name="PERSONALIZED_NAVIGATION_PETA_DESCRIPTION">Waze will calculate your arrival time based on your past drives</string>
strings.xml:2462:    <string name="PERSONALIZED_NAVIGATION_PETA_TITLE">Get personalized ETAs</string>
strings.xml:2463:    <string name="PERSONALIZED_NAVIGATION_TITLE">Personalized navigation</string>
strings.xml:2464:    <string name="PERSONALIZED_SETTINGS_ADS_PERSONALIZATION_DESCRIPTION">"Personalized ads are based on info you've added to your Waze account and your app activity"</string>
strings.xml:2465:    <string name="PERSONALIZED_SETTINGS_ADS_PERSONALIZATION_TITLE">Ads personalization</string>
strings.xml:2466:    <string name="PERSONALIZED_SETTINGS_PERSONALIZED_NAVIGATION_TITLE">Personalized navigation</string>
strings.xml:2467:    <string name="PERSONALIZED_SETTINGS_TITLE">Personalization</string>
strings.xml:2468:    <string name="PERSONALIZED_SETTINGS_TRIP_SUGGESTIONS_TITLE">Trip suggestions</string>
strings.xml:2477:    <string name="PICK_UP_TITLE_SEND">Send location request</string>
strings.xml:2481:    <string name="PLACE_ADD_LOCATION_ERROR">"There's an issue with the place's location. Review the house number and map pin."</string>
strings.xml:2482:    <string name="PLACE_CANNOT_ADD_CATEGORY_BODY">Parking lots are a single category place. To set this location as a parking lot, create a new place.</string>
strings.xml:2485:    <string name="PLACE_CONFIRM_LOCATION">Tap to confirm location</string>
strings.xml:2522:    <string name="PRIVACY_ADS_CONSENT_NOT_PERSONALIZED_BUTTON">Not personalized</string>
strings.xml:2523:    <string name="PRIVACY_ADS_CONSENT_NOT_PERSONALIZED_BUTTON_IOS">Not personalized</string>
strings.xml:2524:    <string name="PRIVACY_ADS_CONSENT_ONBOARDING_NOT_PERSONALIZED_BUTTON">Not personalized</string>
strings.xml:2525:    <string name="PRIVACY_ADS_CONSENT_ONBOARDING_PERSONALIZED_BUTTON">Personalized</string>
strings.xml:2526:    <string name="PRIVACY_ADS_CONSENT_ONBOARDING_TEXT">"Waze uses info you've added to your account and data from trusted ad partners to show you more relevant ads. To learn more about how ads work visit our Privacy Policy."</string>
strings.xml:2527:    <string name="PRIVACY_ADS_CONSENT_ONBOARDING_TITLE">Personalized ads?</string>
strings.xml:2528:    <string name="PRIVACY_ADS_CONSENT_PERSONALIZED_BUTTON">Personalized</string>
strings.xml:2529:    <string name="PRIVACY_ADS_CONSENT_PERSONALIZED_BUTTON_IOS">Personalized</string>
strings.xml:2531:    <string name="PRIVACY_ADS_CONSENT_TEXT">"Waze uses info you've added to your account and data from trusted ad partners to show you more relevant ads. To learn more about how ads work visit our Privacy Policy"</string>
strings.xml:2532:    <string name="PRIVACY_ADS_CONSENT_TEXT_IOS">"Waze uses info you've added to your account and your app activity to show you personalized ads that are more useful to you"</string>
strings.xml:2533:    <string name="PRIVACY_ADS_CONSENT_TITLE">Personalized ads?</string>
strings.xml:2534:    <string name="PRIVACY_ADS_CONSENT_TITLE_IOS">Personalized ads?</string>
strings.xml:2535:    <string name="PRIVACY_ANDROID_Q_LOCATION_POPUP_NO_TEXT">Allow all the time</string>
strings.xml:2536:    <string name="PRIVACY_ANDROID_Q_LOCATION_POPUP_TEXT">"With the upgrade to Android Q, location settings are now controlled on your phone, not in Waze. 
strings.xml:2538:    <string name="PRIVACY_ANDROID_Q_LOCATION_POPUP_TITLE">Your location permissions have changed</string>
strings.xml:2539:    <string name="PRIVACY_ANDROID_Q_LOCATION_POPUP_YES_TEXT">Settings</string>
strings.xml:2540:    <string name="PRIVACY_CONCENT_BUMP_BG_LOCATION_BUTTON_ALLOW">Allow access</string>
strings.xml:2541:    <string name="PRIVACY_CONCENT_BUMP_BG_LOCATION_BUTTON_NO_THANKS">No thanks</string>
strings.xml:2542:    <string name="PRIVACY_CONCENT_BUMP_BG_LOCATION_CONFIRM_BUTTON_ALLOW">Allow access</string>
strings.xml:2543:    <string name="PRIVACY_CONCENT_BUMP_BG_LOCATION_CONFIRM_BUTTON_DONT_ALLOW">No thanks</string>
strings.xml:2544:    <string name="PRIVACY_CONCENT_BUMP_BG_LOCATION_CONFIRM_TEXT">Using real-time traffic data, Waze can tell you when to leave for calendar events. To get these alerts and more, let Waze access your location even when not using the app.</string>
strings.xml:2545:    <string name="PRIVACY_CONCENT_BUMP_BG_LOCATION_CONFIRM_TITLE">Are you sure?</string>
strings.xml:2546:    <string name="PRIVACY_CONCENT_BUMP_BG_LOCATION_TEXT">Waze can tell you about bad traffic, remind you when to leave for planned drives, help with parking and more, when you allow Waze to use your location even while not using the app</string>
strings.xml:2547:    <string name="PRIVACY_CONCENT_BUMP_BG_LOCATION_TITLE">Get even more out of Waze</string>
strings.xml:2553:    <string name="PRIVACY_SETTINGS_ACTIVITY_RECENT_DESTINATIONS_DESCRIPTION">View or remove recent locations from the Waze menu</string>
strings.xml:2554:    <string name="PRIVACY_SETTINGS_ACTIVITY_RECENT_DESTINATIONS_TITLE">Recent locations</string>
strings.xml:2556:    <string name="PRIVACY_SETTINGS_ANDROID_LOCATION_DISCLAIMER">Waze can check your location even when you’re not using the app to get reminders for planned drives, updates about bad traffic, parking assistance, and more</string>
strings.xml:2557:    <string name="PRIVACY_SETTINGS_ANDROID_LOCATION_TITLE">Location</string>
strings.xml:2558:    <string name="PRIVACY_SETTINGS_ANDROID_LOCATION_USE">Always on</string>
strings.xml:2566:    <string name="PRIVACY_SETTINGS_TARGETED_ADS_DESCRIPTION">"Personalized ads are based on info you've added to your Waze account and your app activity. When this is turned off, you'll still see ads, but they may be less useful to you. To learn more, visit ou [... omitted end of lo
strings.xml:2567:    <string name="PRIVACY_SETTINGS_TARGETED_ADS_TITLE">Ads personalization</string>
strings.xml:2640:    <string name="REMOVE_DESTINATION_MESSAGE">If you’ve driven to this location, it’s also saved in your navigation history.</string>
strings.xml:2642:    <string name="REMOVE_DESTINATION_TITLE">Remove location from your phone?</string>
strings.xml:2824:    <string name="REPORT_SOS_LOCATION_COMMENT">Having car trouble? Easily request roadside help. Your fellow Wazers will see your request and location on the map.</string>
strings.xml:2825:    <string name="REPORT_SOS_LOCATION_COMMENT_SENT">Your request and location are currently visible on the map</string>
strings.xml:2826:    <string name="REPORT_SOS_LOCATION_POPUP">Your request is now live</string>
strings.xml:2837:    <string name="REQUEST_CONTACTS_BODY">This will allow you to find addresses saved in your phone contacts when searching in Waze</string>
strings.xml:2838:    <string name="REQUEST_CONTACTS_CANCEL">Cancel</string>
strings.xml:2839:    <string name="REQUEST_CONTACTS_DONE">Done</string>
strings.xml:2840:    <string name="REQUEST_CONTACTS_LEARN_MORE">Learn more</string>
strings.xml:2841:    <string name="REQUEST_CONTACTS_NEXT">Next</string>
strings.xml:2842:    <string name="REQUEST_CONTACTS_TITLE">Allow access to your Contacts</string>
strings.xml:2846:    <string name="RESIDENTIAL_PLACE_CONFIRM_DIALOG_BODY">Residential places show photos &amp; location only. To add a business or other public place, go back.</string>
strings.xml:2943:    <string name="SEARCH_BY_VOICE_AUTO_FOOTER">Search for locations by speaking the language of the country you’re in.</string>
strings.xml:2950:    <string name="SEARCH_LEGAL_POPUP_BODY">Search results are based on distance, location, and more. Prices, opening hours, and other info is collected from different sources, like user contributions and third parties, and may not be accurate or updated in rea [... omitted end of lo
strings.xml:2983:    <string name="SEARCH_RESULTS_ERROR_LABEL">There was a problem showing locations</string>
strings.xml:3029:    <string name="SEND_CURRENT_LOCATION_DISPLAY_TEXT_PS">"I'm at %s.
strings.xml:3030:Open to view location."</string>
strings.xml:3031:    <string name="SEND_CURRENT_LOCATION_EMAIL_BODY_PS_PS_PS" formatted="false">"I'm at %s.
strings.xml:3035:    <string name="SEND_CURRENT_LOCATION_EMAIL_SUBJECT">I sent you my location using Waze. Tap to view</string>
strings.xml:3036:    <string name="SEND_CURRENT_LOCATION_SMS_PS_PS" formatted="false">"I'm at %s, drive here using Waze: %s"</string>
strings.xml:3041:    <string name="SEND_LOCATION">Send Location</string>
strings.xml:3042:    <string name="SEND_LOCATION_ASSISTANCE_EMAIL_BODY_PS_PS" formatted="false">"I need help. I'm at this location: %s
strings.xml:3043: Use Waze to drive to this location: %s"</string>
strings.xml:3044:    <string name="SEND_LOCATION_ASSISTANCE_EMAIL_SUBJECT">"I need help - here's my location"</string>
strings.xml:3045:    <string name="SEND_LOCATION_DISPLAY_TEXT_PS">"Here's the location - %s
strings.xml:3046:Open to view location."</string>
strings.xml:3047:    <string name="SEND_LOCATION_EMAIL_BODY_NAMED_PS_PS">Use Waze to drive to &lt;ADDRESS>: &lt;LINK></string>
strings.xml:3048:    <string name="SEND_LOCATION_EMAIL_SUBJECT">"I've sent you a location using Waze. Open to view location"</string>
strings.xml:3049:    <string name="SEND_LOCATION_SHEET_APP_BTN_COPY">Copy link</string>
strings.xml:3050:    <string name="SEND_LOCATION_SHEET_APP_BTN_EMAIL">Email</string>
strings.xml:3051:    <string name="SEND_LOCATION_SHEET_APP_BTN_MESSAGE">Messages</string>
strings.xml:3052:    <string name="SEND_LOCATION_SHEET_APP_BTN_WHATSAPP">WhatsApp</string>
strings.xml:3053:    <string name="SEND_LOCATION_SHEET_CANCEL">Cancel</string>
strings.xml:3054:    <string name="SEND_LOCATION_SHEET_MORE_OPTIONS">More options</string>
strings.xml:3055:    <string name="SEND_LOCATION_SHEET_SUBTITLE_DRIVE">Anyone with the link can see your drive on the map and share it. You can stop sharing at any time.</string>
strings.xml:3056:    <string name="SEND_LOCATION_SHEET_SUBTITLE_LOCATION">Anyone with the link can see the location and also share it</string>
strings.xml:3057:    <string name="SEND_LOCATION_SHEET_TITLE_DRIVE">Share your drive</string>
strings.xml:3058:    <string name="SEND_LOCATION_SHEET_TITLE_LOCATION">Send location</string>
strings.xml:3059:    <string name="SEND_LOCATION_SMS_PS_PS" formatted="false">"I've sent you a location: %s, drive there using Waze: %s"</string>
strings.xml:3060:    <string name="SEND_LOCATION_TITLE">Send location</string>
strings.xml:3061:    <string name="SEND_LOCATION_TITLE_ETA">Share drive</string>
strings.xml:3063:    <string name="SEND_PARKED_LOCATION_DISPLAY_TEXT_PS">"This is where I've parked: %s 
strings.xml:3065:    <string name="SEND_PARKED_LOCATION_EMAIL_BODY_PS_PS_PS" formatted="false">"This is where I've parked: %s 
strings.xml:3069:    <string name="SEND_PARKED_LOCATION_EMAIL_SUBJECT">"I've sent you my parking location. See it in Waze"</string>
strings.xml:3070:    <string name="SEND_PARKED_LOCATION_SMS_PS_PS" formatted="false">"This is where I've parked: %s 
strings.xml:3133:    <string name="SHARE_DRIVE_JOIN_PREVIEW_CARPLAY_LOCATION_SHARE_DISCLAIMER_TITLE">"You'll share real-time location"</string>
strings.xml:3138:    <string name="SHARE_DRIVE_JOIN_PREVIEW_LOCATION_SHARE_DISCLAIMER_DETAILS">The driver, and anyone with the link, will see your location, name, and photo on the map. Stop sharing at any time.</string>
strings.xml:3139:    <string name="SHARE_DRIVE_JOIN_PREVIEW_LOCATION_SHARE_DISCLAIMER_TITLE">Share your real-time location</string>
strings.xml:3163:    <string name="SHARE_DRIVE_LIVE_DRIVE_PARTICIPANT_STATUS_CURRENT_USER_VIEWING">Turn on to share location</string>
strings.xml:3164:    <string name="SHARE_DRIVE_LIVE_DRIVE_PARTICIPANT_STATUS_CURRENT_USER_VIEWING_SHARING_LOCATION">Sharing location</string>
strings.xml:3167:    <string name="SHARE_DRIVE_LIVE_DRIVE_PARTICIPANT_STATUS_VIEWING_SHARING_LOCATION">Viewing, sharing location</string>
strings.xml:3223:    <string name="SHARE_YOUR_DRIVE_WITH_FRIENDS_AND">friends &amp; contacts you share a drive with will see your real-time movements on the map and receive updates on your ETA.</string>
strings.xml:3279:    <string name="SORRY__THERESS_NO_GPS_RECEPTION_IN_THIS_LOCATION__MAKE_SURE_YOU_ARE_OUTDOORS">"No GPS reception. Make sure you're outdoors."</string>
strings.xml:3287:    <string name="SOS_LIST_SEND_LOCAITON">Send your location</string>
strings.xml:3383:    <string name="START_STATE_SETTINGS_ALLOW_TRIP_FORECASTS_DESCRIPTION">"Get trip suggestions based on your daily commute, saved places, and recent locations. &lt;a href='https://support.google.com/waze/answer/9747181'>More info&lt;/a>"</string>
strings.xml:3390:    <string name="STATE_STATE_PREDICTION_CARD_INCAR_TITLE_NEW_DRIVE_UNKNOWN_DESTINATION">Driving to unnamed location?</string>
strings.xml:3391:    <string name="STATE_STATE_PREDICTION_CARD_INCAR_TITLE_RESUME_DRIVE_UNKNOWN_DESTINATION">Driving to unnamed location?</string>
strings.xml:3406:    <string name="STOP_POINT_QUESTION_REPLACE_LABEL">You can only add 1 stop to a route. Start a new drive to drive to another location.</string>
strings.xml:3491:    <string name="TO_LOCATION_PS">to %s</string>
strings.xml:3544:    <string name="TRIP_OVERVIEW_CURRENT_LOCATION">Your location</string>
strings.xml:3572:    <string name="TRIP_OVERVIEW_ERROR_CANT_FIND_ROUTE_MESSAGE">It looks like there’s no way to drive there. Try a nearby location.</string>
strings.xml:3588:    <string name="TRIP_OVERVIEW_NO_ORIGIN">Your location</string>
strings.xml:3589:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_DEFAULT_1">Personalizing routes…</string>
strings.xml:3590:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_DEFAULT_2">Finding best for you…</string>
strings.xml:3591:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_DEFAULT_3">Matching preferences…</string>
strings.xml:3592:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_DEFAULT_4">Tailoring for your drive…</string>
strings.xml:3593:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_DEFAULT_5">Matching your habits…</string>
strings.xml:3594:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_DEFAULT_6">Scanning live traffic…</string>
strings.xml:3595:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_ENDPOINT_2W_1">Updating ride routes…</string>
strings.xml:3596:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_ENDPOINT_2W_2">Checking road conditions…</string>
strings.xml:3597:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_ENDPOINT_2W_3">Finding moto-friendly routes…</string>
strings.xml:3598:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_ENDPOINT_DEFAULT_1">Personalizing new route…</string>
strings.xml:3599:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_ENDPOINT_DEFAULT_2">Tailoring updated drive…</string>
strings.xml:3600:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_ENDPOINT_DEFAULT_3">Matching driving style…</string>
strings.xml:3601:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_ENDPOINT_NEW_USER_1">Analyzing new routes…</string>
strings.xml:3602:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_ENDPOINT_NEW_USER_2">Checking live traffic…</string>
strings.xml:3603:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_ENDPOINT_NEW_USER_3">Optimizing new route…</string>
strings.xml:3604:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_NEW_USER_1">Scanning local roads…</string>
strings.xml:3605:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_NEW_USER_2">Checking live traffic…</string>
strings.xml:3606:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_NEW_USER_3">Finding optimal routes…</string>
strings.xml:3607:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_NEW_USER_4">Analyzing traffic flow…</string>
strings.xml:3608:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_2W_1">Updating vehicle type…</string>
strings.xml:3609:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_2W_2">Checking rider rules…</string>
strings.xml:3610:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_2W_3">Adapting routes for riders…</string>
strings.xml:3611:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_2W_4">Finding moto-friendly routes…</string>
strings.xml:3612:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_PREFERENCES_1">Applying preferences…</string>
strings.xml:3613:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_PREFERENCES_2">Updating your route…</string>
strings.xml:3614:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_PREFERENCES_3">Updating customized route…</string>
strings.xml:3615:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_PRIVATE_1">Updating vehicle type…</string>
strings.xml:3616:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_PRIVATE_2">Optimizing your route…</string>
strings.xml:3617:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_PRIVATE_3">Tailoring for your vehicle…</string>
strings.xml:3618:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_RECALCULATE_PRIVATE_4">Analyzing road rules…</string>
strings.xml:3619:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_TWO_WHEELER_1">Optimizing for riders…</string>
strings.xml:3620:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_TWO_WHEELER_2">Finding moto-friendly routes…</string>
strings.xml:3621:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_TWO_WHEELER_3">Bypassing traffic hotspots…</string>
strings.xml:3622:    <string name="TRIP_OVERVIEW_PERSONALIZATION_LOADER_MESSAGE_TWO_WHEELER_4">Tailoring your ride route…</string>
strings.xml:3712:    <string name="UNABLE_TO_PROVIDE_ROUTE_TO_DESTINATION__TAKING_YOU_TO_NEAREST_LOCATION_">Unable to provide route to destination. Taking you to nearest location.</string>
strings.xml:3726:    <string name="USE_MY_LOCATION_ALWAYS">Always</string>
strings.xml:3727:    <string name="USE_MY_LOCATION_WHILE_IN_USE">While using the app</string>
strings.xml:3748:    <string name="VENUE_FRESHNESS_POPUP_CONFIRM_BUTTON">View location</string>
strings.xml:3749:    <string name="VENUE_FRESHNESS_POPUP_CONFIRM_BUTTON_AA">View location</string>
strings.xml:3750:    <string name="VENUE_FRESHNESS_POPUP_CONFIRM_BUTTON_CARPLAY">View location</string>
strings.xml:3751:    <string name="VENUE_FRESHNESS_POPUP_MESSAGE_NO_ADDRESS_AA_PS">%s has moved to a new location</string>
strings.xml:3752:    <string name="VENUE_FRESHNESS_POPUP_MESSAGE_NO_ADDRESS_CARPLAY_PS">%s has moved to a new location</string>
strings.xml:3753:    <string name="VENUE_FRESHNESS_POPUP_MESSAGE_NO_ADDRESS_PS">%s has moved to a new location</string>
strings.xml:3761:    <string name="VERIFY_CALENDAR_AUTOCOMPLETE_TITLE">Find location</string>
strings.xml:3765:    <string name="VERIFY_CALENDAR_SET_LOCATION">Set address</string>
strings.xml:3800:    <string name="VOICE_COMMANDS_GOOGLE_ASSISTANT_ENABLE_PERSONALIZED_DESCRIPTION">Google</string>
strings.xml:3801:    <string name="VOICE_COMMANDS_GOOGLE_ASSISTANT_ENABLE_PERSONALIZED_REASON">Get a personalized experience when you connect Waze to your Google Assistant</string>
strings.xml:3802:    <string name="VOICE_COMMANDS_GOOGLE_ASSISTANT_ENABLE_PERSONALIZED_TITLE">Personalized Google Assistant</string>
strings.xml:3816:    <string name="VOICE_COMMANDS_GOOGLE_ASSISTANT_SETTINGS_SIGN_OUT_BUMP_BODY">"You will no longer get personalized results from Google Assistant in Waze.
strings.xml:3819:    <string name="VOICE_COMMANDS_GOOGLE_ASSISTANT_SETTINGS_SIGN_OUT_BUMP_BODY_HTML">&lt;p>You will no longer get personalized results from Google Assistant.&lt;/p>&lt;p>However, your Google Account is still connected to Waze. Go to your &lt;a href=\"%s\">Googl [... omitted end of lo
strings.xml:3909:    <string name="WELCOME_LOCATION_DOWNLOADING_LANGUAGE">Updating the map...</string>
strings.xml:3910:    <string name="WELCOME_LOCATION_MESSAGE">Scanning traffic around you</string>
strings.xml:3922:    <string name="WE_COULDNT_RETRIEVE_YOUR_LOCATION">"Can't find your location. Make sure your phone's location settings are on and you're connected to the internet."</string>
strings.xml:3967:    <string name="Z_SPEED_SENT_LOCATION_TEXT" formatted="false">%s sent %s</string>
strings.xml:3968:    <string name="Z_SPEED_SENT_LOCATION_TITLE">SENT LOCATION</string>
strings.xml:4071:    <string name="contentDescription_addressItemChangeLocation">addressItemChangeLocation</string>
strings.xml:4083:    <string name="contentDescription_addressItemSendLocation">addressItemSendLocation</string>
strings.xml:4085:    <string name="contentDescription_addressItemSetLocation">addressItemSetLocation</string>
```

