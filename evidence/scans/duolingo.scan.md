# Pattern scan: work/duolingo/jadx

## Code categories (library packages excluded)

### installed_apps — 80 hits in 58 files

- `defpackage/pu60.java` (14)
- `com/google/android/gms/common/GooglePlayServicesUtilLight.java` (4)
- `com/bytedance/sdk/openadsdk/core/uc/uc.java` (2)
- `defpackage/tla0.java` (2)
- `defpackage/y.java` (2)
- `com/google/android/gms/internal/ads/zzfdd.java` (2)
- `com/google/android/gms/internal/ads/zzinp.java` (2)
- `defpackage/fa3.java` (2)
- `zendesk/support/request/UtilsAttachment.java` (1)
- `zendesk/support/request/CellBindHelper.java` (1)
- `androidx/credentials/playservices/controllers/identityauth/beginsignin/BeginSignInControllerUtility.java` (1)
- `androidx/credentials/playservices/controllers/identityauth/createpublickeycredential/PublicKeyCredentialControllerUtility.java` (1)

```
zendesk/support/request/UtilsAttachment.java:70:        List<ResolveInfo> listQueryIntentActivities = packageManager.queryIntentActivities(intent, NativeProtocol.MESSAGE_GET_ACCESS_TOKEN_REQUEST);
zendesk/support/request/CellBindHelper.java:82:        if (context.getPackageManager().queryIntentActivities(intent, 0).size() > 0) {
androidx/credentials/playservices/controllers/identityauth/beginsignin/BeginSignInControllerUtility.java:35:            return r1.getPackageInfo("com.google.android.gms", 0).versionCode;
androidx/credentials/playservices/controllers/identityauth/createpublickeycredential/PublicKeyCredentialControllerUtility.java:145:            PackageInfo packageInfo = packageManager.getPackageInfo("com.google.android.gms", 0);
com/adjust/sdk/DeviceInfo.java:203:            SigningInfo signingInfo = context.getPackageManager().getPackageInfo("com.facebook.katana", 134217728).signingInfo;
com/adjust/sdk/ActivityHandler.java:925:        int size = this.adjustConfig.context.getPackageManager().queryIntentActivities(intent, 0).size();
org/prebid/mobile/rendering/utils/helpers/ExternalViewerUtils.java:23:            return context.getPackageManager().queryIntentActivities(intent, NativeProtocol.MESSAGE_GET_ACCESS_TOKEN_REQUEST).size() > 0;
com/adjust/sdk/GooglePlayServicesClient.java:37:        context.getPackageManager().getPackageInfo("com.android.vending", 0);
com/ironsource/X4.java:215:        return context.getPackageManager().getInstalledApplications(0);
com/bytedance/sdk/openadsdk/utils/ok.java:461:        if (context == null || (listQueryIntentActivities = context.getPackageManager().queryIntentActivities(new Intent("android.intent.action.VIEW", Uri.parse("https://www.example.com")), 0)) == null) {
com/bytedance/sdk/openadsdk/utils/DeviceUtils.java:255:                PackageInfo packageInfo = context.getPackageManager().getPackageInfo("com.android.vending", 0);
com/bytedance/sdk/openadsdk/core/uc/uc.java:35:            List<ResolveInfo> listQueryIntentActivities = packageManager.queryIntentActivities(intent, 0);
```

### usage_stats — 5 hits in 2 files

- `defpackage/ww70.java` (3)
- `defpackage/pu60.java` (2)

```
defpackage/ww70.java:5:import android.app.usage.UsageStatsManager;
defpackage/ww70.java:65:                Object systemService = ((a090) obj).a.getSystemService((Class<Object>) UsageStatsManager.class);
defpackage/ww70.java:67:                    return (UsageStatsManager) systemService;
defpackage/pu60.java:4:import android.app.usage.UsageStatsManager;
defpackage/pu60.java:783:            numValueOf = Integer.valueOf(((UsageStatsManager) this.q.b.getValue()).getAppStandbyBucket());
```

### clipboard — 5 hits in 4 files

- `defpackage/a970.java` (2)
- `com/unity3d/player/UnityPlayer.java` (1)
- `defpackage/b870.java` (1)
- `defpackage/ejr.java` (1)

```
com/unity3d/player/UnityPlayer.java:666:        ClipData primaryClip = this.m_ClipboardManager.getPrimaryClip();
defpackage/b870.java:160:                    ClipData primaryClip = ((fs0) qk7Var2).a.j().getPrimaryClip();
defpackage/ejr.java:1731:        ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
defpackage/a970.java:595:            ClipData primaryClip = ((fs0) qk7Var).a.j().getPrimaryClip();
defpackage/a970.java:771:        if (yqs.y(qk7Var).hasPrimaryClip() && (primaryClipDescription = yqs.y(qk7Var).getPrimaryClipDescription()) != null && primaryClipDescription.hasMimeType("text/*")) {
```

### contacts — 25 hits in 4 files

- `defpackage/jg.java` (14)
- `defpackage/ep8.java` (5)
- `defpackage/fp8.java` (4)
- `defpackage/gy1.java` (2)

```
defpackage/gy1.java:5:import android.provider.ContactsContract;
defpackage/gy1.java:109:        ContactsContract.Data.CONTENT_URI.getClass();
defpackage/jg.java:5:import android.provider.ContactsContract;
defpackage/jg.java:357:                Uri uri = ContactsContract.CommonDataKinds.Email.CONTENT_URI;
defpackage/jg.java:362:                Uri uri2 = ContactsContract.CommonDataKinds.Phone.CONTENT_URI;
defpackage/jg.java:450:                    Uri uri3 = ContactsContract.Data.CONTENT_URI;
defpackage/jg.java:472:                    Uri uri4 = ContactsContract.Data.CONTENT_URI;
defpackage/jg.java:494:                    Uri uri5 = ContactsContract.Data.CONTENT_URI;
defpackage/jg.java:516:                    Uri uri6 = ContactsContract.Data.CONTENT_URI;
defpackage/jg.java:538:                    Uri uri7 = ContactsContract.Data.CONTENT_URI;
defpackage/jg.java:560:                    Uri uri8 = ContactsContract.Data.CONTENT_URI;
defpackage/jg.java:582:                    Uri uri9 = ContactsContract.Data.CONTENT_URI;
```

### call_log — 0 hits in 0 files


```
```

### sms — 49 hits in 21 files

- `com/google/android/gms/auth/api/phone/SmsRetrieverClient.java` (7)
- `com/google/android/gms/internal/p002authapiphone/zzab.java` (5)
- `defpackage/uy.java` (4)
- `com/google/android/gms/auth/api/phone/SmsRetriever.java` (4)
- `com/google/android/gms/internal/p002authapiphone/zzw.java` (3)
- `com/duolingo/signuplogin/y1.java` (3)
- `defpackage/rf90.java` (3)
- `defpackage/mh10.java` (2)
- `defpackage/ilv.java` (2)
- `com/google/android/gms/auth/api/phone/SmsRetrieverApi.java` (2)
- `com/google/android/gms/auth/api/phone/SmsRetrieverStatusCodes.java` (2)
- `defpackage/u530.java` (2)

```
defpackage/mh10.java:15:import com.google.android.gms.auth.api.phone.SmsRetriever;
defpackage/mh10.java:118:                    zvb0.y(context, vf90Var, new IntentFilter(SmsRetriever.SMS_RETRIEVED_ACTION), 2);
defpackage/ilv.java:30:import com.google.android.gms.auth.api.phone.SmsRetriever;
defpackage/ilv.java:196:                    String stringExtra = intent3 != null ? intent3.getStringExtra(SmsRetriever.EXTRA_SMS_MESSAGE) : null;
defpackage/uy.java:14:import com.google.android.gms.auth.api.phone.SmsRetriever;
defpackage/uy.java:15:import com.google.android.gms.auth.api.phone.SmsRetrieverClient;
defpackage/uy.java:19:    public static SmsRetrieverClient A(ComponentActivity componentActivity) {
defpackage/uy.java:20:        SmsRetrieverClient client = SmsRetriever.getClient((Activity) componentActivity);
com/google/android/gms/internal/p002authapiphone/zza.java:10:    private final String zzb = "com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService";
com/google/android/gms/internal/p002authapiphone/zzi.java:9:        super("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverResultCallback");
com/google/android/gms/internal/p002authapiphone/zzab.java:5:import com.google.android.gms.auth.api.phone.SmsRetrieverClient;
com/google/android/gms/internal/p002authapiphone/zzab.java:12:public final class zzab extends SmsRetrieverClient {
```

### location — 42 hits in 14 files

- `com/google/android/gms/location/FusedLocationProviderClient.java` (13)
- `com/google/android/gms/internal/location/zzz.java` (4)
- `com/google/android/gms/location/FusedLocationProviderApi.java` (4)
- `com/google/android/gms/location/LocationServices.java` (4)
- `com/google/android/gms/internal/location/zzaf.java` (3)
- `org/prebid/mobile/rendering/sdk/deviceData/managers/LastKnownLocationInfoManager.java` (2)
- `defpackage/wb1.java` (2)
- `com/google/android/gms/location/zzak.java` (2)
- `com/google/android/gms/location/GeofencingApi.java` (2)
- `com/google/android/gms/location/zzaj.java` (2)
- `com/amazon/device/ads/DtbGeoLocation.java` (1)
- `com/google/android/gms/location/GeofencingRequest.java` (1)

```
org/prebid/mobile/rendering/sdk/deviceData/managers/LastKnownLocationInfoManager.java:118:                    lastKnownLocation = locationManager.getLastKnownLocation("gps");
org/prebid/mobile/rendering/sdk/deviceData/managers/LastKnownLocationInfoManager.java:119:                    lastKnownLocation2 = this.locManager.getLastKnownLocation("network");
com/amazon/device/ads/DtbGeoLocation.java:73:            return locationManager.getLastKnownLocation(str);
com/google/android/gms/internal/location/zzz.java:62:    public final PendingResult<Status> requestLocationUpdates(GoogleApiClient googleApiClient, LocationRequest locationRequest, LocationListener locationListener) {
com/google/android/gms/internal/location/zzz.java:88:    public final PendingResult<Status> requestLocationUpdates(GoogleApiClient googleApiClient, LocationRequest locationRequest, LocationCallback locationCallback, Looper looper) {
com/google/android/gms/internal/location/zzz.java:93:    public final PendingResult<Status> requestLocationUpdates(GoogleApiClient googleApiClient, LocationRequest locationRequest, PendingIntent pendingIntent) {
com/google/android/gms/internal/location/zzz.java:98:    public final PendingResult<Status> requestLocationUpdates(GoogleApiClient googleApiClient, LocationRequest locationRequest, LocationListener locationListener, Looper looper) {
com/google/android/gms/internal/location/zzaf.java:16:    public final PendingResult<Status> addGeofences(GoogleApiClient googleApiClient, List<Geofence> list, PendingIntent pendingIntent) {
com/google/android/gms/internal/location/zzaf.java:18:        builder.addGeofences(list);
com/google/android/gms/internal/location/zzaf.java:38:    public final PendingResult<Status> addGeofences(GoogleApiClient googleApiClient, GeofencingRequest geofencingRequest, PendingIntent pendingIntent) {
defpackage/wb1.java:65:                        Location lastKnownLocation2 = locationManager.isProviderEnabled("network") ? locationManager.getLastKnownLocation("network") : null;
defpackage/wb1.java:73:                                lastKnownLocation = locationManager.getLastKnownLocation("gps");
```

### wifi_bt_scan — 0 hits in 0 files


```
```

### device_ids — 57 hits in 33 files

- `com/adjust/sdk/PackageBuilder.java` (13)
- `com/google/android/gms/measurement/internal/zzaw.java` (3)
- `defpackage/fvb.java` (3)
- `androidx/core/widget/NestedScrollView.java` (3)
- `com/bytedance/sdk/openadsdk/core/mtv/jg.java` (2)
- `com/bytedance/sdk/openadsdk/core/phb/phb.java` (2)
- `com/bytedance/sdk/openadsdk/core/phb/dd.java` (2)
- `com/facebook/internal/AttributionIdentifiers.java` (2)
- `androidx/compose/ui/platform/AndroidComposeView.java` (2)
- `defpackage/j6.java` (2)
- `com/google/androidgamesdk/GameActivity.java` (1)
- `com/google/android/gms/ads/internal/util/client/zzf.java` (1)

```
com/google/androidgamesdk/GameActivity.java:365:        return onTouchEventNative(this.mNativeHandle, motionEvent, motionEvent.getPointerCount(), motionEvent.getHistorySize(), motionEvent.getDeviceId(), motionEvent.getSource(), motionEvent.getAction(), motionEvent.getEventTime(), motionEvent.getDown
com/google/android/gms/measurement/internal/zzaw.java:41:    private static final String[] zzd = {"app_version", "ALTER TABLE apps ADD COLUMN app_version TEXT;", "app_store", "ALTER TABLE apps ADD COLUMN app_store TEXT;", "gmp_version", "ALTER TABLE apps ADD COLUMN gmp_version INTEGER;", "dev_cert_h
com/google/android/gms/measurement/internal/zzaw.java:2692:                cursorQuery = zze().query("apps", new String[]{"app_instance_id", "gmp_app_id", "resettable_device_id_hash", "last_bundle_index", "last_bundle_start_timestamp", "last_bundle_end_timestamp", "app_version", "app_store", "gmp_ve
com/google/android/gms/measurement/internal/zzaw.java:2841:        contentValues.put("android_id", (Long) 0L);
com/google/android/gms/ads/internal/util/client/zzf.java:108:        String string = contentResolver == null ? null : Settings.Secure.getString(contentResolver, "android_id");
com/google/android/gms/internal/ads/zztu.java:101:            iZzai = zzai(zztnVar.zzb().getDeviceId());
com/apm/insight/nativecrash/b.java:243:            return this.b.getDeviceId();
com/apm/insight/ICommonParams.java:10:    String getDeviceId();
com/apm/insight/i/a.java:24:                            string = Settings.Secure.getString(context.getContentResolver(), "android_id");
com/apm/insight/runtime/g.java:46:            public final String getDeviceId() {
com/apm/insight/d.java:130:            public final String getDeviceId() {
com/google/android/gms/internal/ads/zztg.java:195:                if (context3 == null || context3.getDeviceId() != i2) {
```

### gsf_id — 2 hits in 1 files

- `com/google/android/gms/internal/auth/zzcb.java` (2)

```
com/google/android/gms/internal/auth/zzcb.java:15:    public static final Uri zza = Uri.parse("content://com.google.android.gsf.gservices");
com/google/android/gms/internal/auth/zzcb.java:16:    public static final Uri zzb = Uri.parse("content://com.google.android.gsf.gservices/prefix");
```

### advertising_id — 157 hits in 48 files

- `com/google/android/gms/ads/identifier/AdvertisingIdClient.java` (16)
- `com/ironsource/C2590u1.java` (11)
- `com/unity3d/ads/core/domain/attribution/AndroidAttribution.java` (9)
- `com/unity3d/services/ads/measurements/MeasurementsService.java` (7)
- `com/unity3d/services/ads/topics/TopicsService.java` (5)
- `com/google/android/gms/measurement/internal/zznn.java` (5)
- `com/ironsource/X4.java` (4)
- `com/amazon/device/ads/DtbGooglePlayServicesAdapter.java` (4)
- `com/google/android/gms/measurement/internal/zzhh.java` (4)
- `com/google/android/gms/internal/ads/zzfds.java` (4)
- `com/google/android/gms/internal/pal/zzcs.java` (4)
- `com/google/android/gms/internal/pal/zzdu.java` (4)

```
org/prebid/mobile/rendering/utils/helpers/AdvertisingIdManager.java:8:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
org/prebid/mobile/rendering/utils/helpers/AdvertisingIdManager.java:117:                        AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(context);
com/adjust/sdk/Reflection.java:37:        return invokeStaticMethod("com.google.android.gms.ads.identifier.AdvertisingIdClient", "getAdvertisingIdInfo", new Class[]{Context.class}, context);
com/ironsource/C2590u1.java:3:import android.adservices.measurement.MeasurementManager;
com/ironsource/C2590u1.java:43:        final /* synthetic */ MeasurementManager c;
com/ironsource/C2590u1.java:48:        public c(MeasurementManager measurementManager, Uri uri, MotionEvent motionEvent, dv8<? super c> dv8Var) {
com/ironsource/C2590u1.java:73:                MeasurementManager measurementManager = this.c;
com/ironsource/C2590u1.java:97:        final /* synthetic */ MeasurementManager c;
com/ironsource/C2590u1.java:101:        public d(MeasurementManager measurementManager, Uri uri, dv8<? super d> dv8Var) {
com/ironsource/C2590u1.java:125:                MeasurementManager measurementManager = this.c;
com/ironsource/C2590u1.java:144:        MeasurementManager measurementManagerA = C2433l0.a(context);
com/ironsource/C2590u1.java:284:    private final a a(InterfaceC2624w1.a aVar, MeasurementManager measurementManager) {
```

### install_referrer — 70 hits in 15 files

- `com/android/installreferrer/api/b.java` (17)
- `com/adjust/sdk/InstallReferrer.java` (12)
- `com/google/android/gms/internal/ads/zzasg.java` (11)
- `com/facebook/internal/InstallReferrerUtil.java` (4)
- `com/facebook/appevents/AppEventsLoggerImpl.java` (4)
- `com/google/android/gms/internal/ads/zzasj.java` (4)
- `com/android/installreferrer/api/InstallReferrerClient.java` (3)
- `defpackage/p8h.java` (3)
- `defpackage/ffd.java` (3)
- `com/android/installreferrer/api/a.java` (2)
- `com/google/android/gms/internal/ads/zzasf.java` (2)
- `defpackage/hri.java` (2)

```
com/android/installreferrer/api/a.java:31:        InstallReferrerCommons.logVerbose("InstallReferrerClient", "Install Referrer service connected.");
com/android/installreferrer/api/a.java:47:        InstallReferrerCommons.logWarn("InstallReferrerClient", "Install Referrer service disconnected.");
com/android/installreferrer/api/ReferrerDetails.java:32:    public String getInstallReferrer() {
com/android/installreferrer/api/InstallReferrerClientImpl$ClientState.java:8:public @interface InstallReferrerClientImpl$ClientState {
com/android/installreferrer/api/InstallReferrerClient.java:9:public abstract class InstallReferrerClient {
com/android/installreferrer/api/InstallReferrerClient.java:18:        public InstallReferrerClient build() {
com/android/installreferrer/api/InstallReferrerClient.java:45:    public abstract ReferrerDetails getInstallReferrer();
com/android/installreferrer/api/b.java:19:public final class b extends InstallReferrerClient {
com/android/installreferrer/api/b.java:29:    @Override // com.android.installreferrer.api.InstallReferrerClient
com/android/installreferrer/api/b.java:33:            InstallReferrerCommons.logVerbose("InstallReferrerClient", "Unbinding from service.");
com/android/installreferrer/api/b.java:40:    @Override // com.android.installreferrer.api.InstallReferrerClient
com/android/installreferrer/api/b.java:41:    public final ReferrerDetails getInstallReferrer() throws RemoteException {
```

### sensors — 0 hits in 0 files


```
```

### accounts — 3 hits in 3 files

- `com/google/android/gms/auth/zzl.java` (1)
- `com/duolingo/core/networking/ManagerDuoJwt.java` (1)
- `defpackage/aw9.java` (1)

```
com/google/android/gms/auth/zzl.java:99:        AccountManager.get(context).invalidateAuthToken("com.google", str);
com/duolingo/core/networking/ManagerDuoJwt.java:79:            Account[] accountsByType = this.accountManager.getAccountsByType(account.type);
defpackage/aw9.java:679:                AccountManager accountManager = AccountManager.get(context4);
```

### battery_state — 4 hits in 2 files

- `com/facebook/battery/metrics/devicebattery/DeviceBatteryMetricsCollector.java` (3)
- `com/google/android/gms/internal/ads/zzewx.java` (1)

```
com/google/android/gms/internal/ads/zzewx.java:55:            zIsCharging = batteryManager != null ? batteryManager.isCharging() : zze(zzd());
com/facebook/battery/metrics/devicebattery/DeviceBatteryMetricsCollector.java:21:    boolean mIsCurrentlyCharging = isCharging(getBatteryIntent());
com/facebook/battery/metrics/devicebattery/DeviceBatteryMetricsCollector.java:71:            SystemMetricsLogger.wtf(TAG, "Exception registering receiver for ACTION_BATTERY_CHANGED");
com/facebook/battery/metrics/devicebattery/DeviceBatteryMetricsCollector.java:91:    private static boolean isCharging(Intent intent) {
```

### screen_capture_detect — 29 hits in 11 files

- `defpackage/luz.java` (6)
- `com/duolingo/core/share/ShareSheetVia.java` (6)
- `com/duolingo/session/SessionActivity.java` (5)
- `com/duolingo/core/persistence/file/ExternalCacheDir.java` (3)
- `defpackage/ir10.java` (2)
- `com/duolingo/data/debug/settings/DebugCategory.java` (2)
- `defpackage/b3b.java` (1)
- `defpackage/khz.java` (1)
- `defpackage/ggz.java` (1)
- `defpackage/dkz.java` (1)
- `defpackage/r0o.java` (1)

```
defpackage/b3b.java:808:            iArr[DebugCategory.RESET_SCREENSHOT_SHARE_STATE.ordinal()] = 200;
defpackage/ir10.java:147:                            ShareSheetVia shareSheetVia = ShareSheetVia.SESSION_SCREENSHOT;
defpackage/ir10.java:204:                    ShareSheetVia shareSheetVia2 = ShareSheetVia.SESSION_SCREENSHOT;
defpackage/luz.java:50:                Activity.ScreenCaptureCallback screenCaptureCallback = new Activity.ScreenCaptureCallback() { // from class: kuz
defpackage/luz.java:51:                    @Override // android.app.Activity.ScreenCaptureCallback
defpackage/luz.java:66:                activity.registerScreenCaptureCallback(activity.getMainExecutor(), screenCaptureCallback);
defpackage/luz.java:76:        Activity.ScreenCaptureCallback screenCaptureCallback;
defpackage/luz.java:79:        if (!nuzVar.b.a(34) || (screenCaptureCallback = (Activity.ScreenCaptureCallback) nuzVar.h.remove(activity)) == null) {
defpackage/luz.java:82:        activity.unregisterScreenCaptureCallback(screenCaptureCallback);
defpackage/khz.java:104:                    prz przVarA = t69Var.a(scoreIncreaseSessionEndParams.d, scoreIncreaseSessionEndParams.f.a, ShareSheetVia.SCORE_SESSION_END_SCREENSHOT, hhzVar.l, whzVar.q.getValue() == ScoreIncreaseSessionEndVariant.MILESTONE, new Integer(hhzVar.c));
defpackage/ggz.java:81:                prz przVarC = t69Var.c(scoreInProgressSessionEndParams.c, scoreInProgressSessionEndParams.e, qgzVar, ShareSheetVia.SCORE_SESSION_END_SCREENSHOT);
com/duolingo/core/share/ShareSheetVia.java:48:    public static final ShareSheetVia SCORE_SESSION_END_SCREENSHOT;
```

### audio_capture — 227 hits in 32 files

- `com/duolingo/data/speech/recognizer/engine/e.java` (36)
- `com/duolingo/data/speech/recognizer/engine/c.java` (26)
- `com/duolingo/data/speech/recognizer/engine/AudioPipelineSpeechRecognizerEngine$Phase.java` (24)
- `com/duolingo/data/speech/recognizer/engine/DefaultSpeechRecognizerEngine$Phase.java` (21)
- `com/duolingo/data/speech/recognizer/engine/b.java` (17)
- `com/duolingo/data/speech/recognizer/engine/a.java` (12)
- `com/duolingo/data/speech/recognizer/engine/SpeechRecognizerEngine$EndOfSpeechBehavior.java` (11)
- `com/duolingo/data/speech/recognizer/engine/SpeechRecognizerEngine$LanguageModel.java` (11)
- `com/duolingo/data/speech/recognizer/engine/SpeechRecognizerEngine$Implementation.java` (11)
- `defpackage/hx20.java` (9)
- `com/duolingo/data/speech/recognizer/engine/d.java` (8)
- `defpackage/pw30.java` (8)

```
com/duolingo/data/speech/recognizer/engine/a.java:10:        int[] iArr = new int[AudioPipelineSpeechRecognizerEngine$Phase.values().length];
com/duolingo/data/speech/recognizer/engine/a.java:12:            iArr[AudioPipelineSpeechRecognizerEngine$Phase.LISTENING.ordinal()] = 1;
com/duolingo/data/speech/recognizer/engine/a.java:16:            iArr[AudioPipelineSpeechRecognizerEngine$Phase.STARTING.ordinal()] = 2;
com/duolingo/data/speech/recognizer/engine/a.java:20:            iArr[AudioPipelineSpeechRecognizerEngine$Phase.PROCESSING.ordinal()] = 3;
com/duolingo/data/speech/recognizer/engine/a.java:24:            iArr[AudioPipelineSpeechRecognizerEngine$Phase.IDLE.ordinal()] = 4;
com/duolingo/data/speech/recognizer/engine/a.java:28:            iArr[AudioPipelineSpeechRecognizerEngine$Phase.DESTROYED.ordinal()] = 5;
com/duolingo/data/speech/recognizer/engine/a.java:32:        int[] iArr2 = new int[SpeechRecognizerEngine$LanguageModel.values().length];
com/duolingo/data/speech/recognizer/engine/a.java:34:            iArr2[SpeechRecognizerEngine$LanguageModel.FREE_FORM.ordinal()] = 1;
com/duolingo/data/speech/recognizer/engine/a.java:38:            iArr2[SpeechRecognizerEngine$LanguageModel.WEB_SEARCH.ordinal()] = 2;
com/duolingo/data/speech/recognizer/engine/a.java:42:        int[] iArr3 = new int[SpeechRecognizerEngine$EndOfSpeechBehavior.values().length];
com/duolingo/data/speech/recognizer/engine/a.java:44:            iArr3[SpeechRecognizerEngine$EndOfSpeechBehavior.CONTINUE.ordinal()] = 1;
com/duolingo/data/speech/recognizer/engine/a.java:48:            iArr3[SpeechRecognizerEngine$EndOfSpeechBehavior.AUTO_STOP.ordinal()] = 2;
```

### accessibility — 147 hits in 48 files

- `defpackage/dt0.java` (10)
- `defpackage/mon.java` (10)
- `app/rive/semantics/AndroidAccessibilityStateProvider.java` (7)
- `com/pgl/ssdk/u.java` (7)
- `com/unity3d/player/P.java` (5)
- `defpackage/aac.java` (5)
- `defpackage/tqo.java` (5)
- `defpackage/z23.java` (5)
- `defpackage/l7e.java` (5)
- `androidx/recyclerview/widget/RecyclerView.java` (4)
- `androidx/compose/ui/platform/AndroidComposeView.java` (4)
- `defpackage/ecd.java` (4)

```
androidx/recyclerview/widget/RecyclerView.java:31:import android.view.accessibility.AccessibilityManager;
androidx/recyclerview/widget/RecyclerView.java:128:    private final AccessibilityManager mAccessibilityManager;
androidx/recyclerview/widget/RecyclerView.java:318:        this.mAccessibilityManager = (AccessibilityManager) getContext().getSystemService("accessibility");
androidx/recyclerview/widget/RecyclerView.java:2638:        AccessibilityManager accessibilityManager = this.mAccessibilityManager;
androidx/compose/ui/platform/AndroidComposeView.java:26:import android.view.accessibility.AccessibilityManager;
androidx/compose/ui/platform/AndroidComposeView.java:2032:            AccessibilityManager accessibilityManager = dt0Var.d;
androidx/compose/ui/platform/AndroidComposeView.java:2033:            if (accessibilityManager.isEnabled() && accessibilityManager.isTouchExplorationEnabled()) {
androidx/compose/ui/platform/AndroidComposeView.java:2355:    public p6 getAccessibilityManager() {
android/view/accessibility/AccessibilityManager$AccessibilityServicesStateChangeListener.java:4:public /* synthetic */ interface AccessibilityManager$AccessibilityServicesStateChangeListener {
com/moloco/sdk/internal/services/bidtoken/providers/b.java:5:import android.view.accessibility.AccessibilityManager;
com/moloco/sdk/internal/services/bidtoken/providers/b.java:55:            Boolean boolValueOf2 = Boolean.valueOf(((AccessibilityManager) systemService2).isEnabled() && Settings.Secure.getInt(context.getContentResolver(), "accessibility_large_pointer_icon", 0) == 1);
com/moloco/sdk/internal/services/bidtoken/providers/b.java:66:            return new a(boolValueOf, boolValueOf2, boolValueOf3, Float.valueOf(((AccessibilityManager) systemService3).isEnabled() ? context2.getResources().getConfiguration().fontScale : 1.0f));
```

### root_emulator — 1000 hits in 140 files

- `com/unity3d/ads/core/domain/exposure/CommonAdViewerExposedFunctionsKt.java` (333)
- `com/unity3d/services/core/api/DeviceInfo.java` (67)
- `com/unity3d/ads/core/domain/exposure/CommonAdViewerExposedFunctionsKt$getAdContext$1.java` (26)
- `com/unity3d/services/ads/api/AdUnit.java` (24)
- `com/unity3d/services/core/api/Cache.java` (21)
- `com/unity3d/services/ads/api/VideoPlayer.java` (14)
- `com/unity3d/services/core/api/Sdk.java` (14)
- `com/unity3d/services/core/api/Storage.java` (14)
- `com/unity3d/services/core/api/Preferences.java` (13)
- `com/duolingo/R.java` (13)
- `com/unity3d/ads/core/domain/HandleInvocationsFromAdViewer.java` (12)
- `com/unity3d/ads/adplayer/WebViewAdPlayer.java` (12)

```
io/sentry/android/core/internal/util/n.java:35:        this.d = new String[]{"/sbin/su", "/data/local/xbin/su", "/system/bin/su", "/system/xbin/su", "/data/local/bin/su", "/system/app/Superuser.apk", "/system/sd/xbin/su", "/system/bin/failsafe/su", "/data/local/su", "/su/bin/su", "/su/bin", "/system
com/unity3d/services/ads/api/VideoPlayer.java:10:import com.unity3d.services.core.webview.bridge.WebViewExposed;
com/unity3d/services/ads/api/VideoPlayer.java:17:    @WebViewExposed
com/unity3d/services/ads/api/VideoPlayer.java:26:    @WebViewExposed
com/unity3d/services/ads/api/VideoPlayer.java:39:    @WebViewExposed
com/unity3d/services/ads/api/VideoPlayer.java:50:    @WebViewExposed
com/unity3d/services/ads/api/VideoPlayer.java:59:    @WebViewExposed
com/unity3d/services/ads/api/VideoPlayer.java:77:    @WebViewExposed
com/unity3d/services/ads/api/VideoPlayer.java:95:    @WebViewExposed
com/unity3d/services/ads/api/VideoPlayer.java:113:    @WebViewExposed
com/unity3d/services/ads/api/VideoPlayer.java:131:    @WebViewExposed
com/unity3d/services/ads/api/VideoPlayer.java:141:    @WebViewExposed
```

### js_bridge — 44 hits in 31 files

- `com/unity3d/ads/adplayer/AndroidWebViewContainer.java` (7)
- `defpackage/u49.java` (3)
- `com/bytedance/sdk/component/mtv/rw.java` (2)
- `com/bytedance/sdk/openadsdk/vv/ckp.java` (2)
- `com/moloco/sdk/xenoss/sdkdevkit/android/adrenderer/internal/templates/ad/a.java` (2)
- `com/duolingo/web/WebViewActivity.java` (2)
- `com/ironsource/sdk/controller/v.java` (2)
- `org/prebid/mobile/rendering/views/webview/WebViewInterstitial.java` (1)
- `org/prebid/mobile/rendering/views/webview/WebViewBanner.java` (1)
- `org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java` (1)
- `com/bytedance/sdk/component/mtv/dd.java` (1)
- `com/bytedance/sdk/component/uc/jg.java` (1)

```
org/prebid/mobile/rendering/views/webview/WebViewInterstitial.java:35:        addJavascriptInterface(interstitialJSInterface, "jsBridge");
org/prebid/mobile/rendering/views/webview/WebViewBanner.java:37:        addJavascriptInterface(bannerJSInterface, "jsBridge");
org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java:43:        public void addJavascriptInterface(Object obj, String str, List<String> list) {
com/bytedance/sdk/component/mtv/rw.java:45:    public void addJavascriptInterface(Object obj, String str) {
com/bytedance/sdk/component/mtv/rw.java:50:        super.addJavascriptInterface(obj, str);
com/bytedance/sdk/component/mtv/dd.java:1002:            this.whk.addJavascriptInterface(obj, str);
com/bytedance/sdk/component/uc/jg.java:28:            this.mtv.addJavascriptInterface(this, this.ac);
com/bytedance/sdk/component/adexpress/rw/rw.java:313:        webView.addJavascriptInterface(vvVar, str);
com/bytedance/sdk/openadsdk/vv/ckp.java:181:            webView2.addJavascriptInterface(new uc(iArr), "JS_LANDING_PAGE_LOG_OBJ");
com/bytedance/sdk/openadsdk/vv/ckp.java:183:            jg.uc("LandingPageLog", "addJavascriptInterface exception", e);
com/moloco/sdk/xenoss/sdkdevkit/android/adrenderer/internal/templates/ad/a.java:44:        eVar.addJavascriptInterface(new com.moloco.sdk.xenoss.sdkdevkit.android.adrenderer.internal.templates.renderer.a(dVar), "AndroidTemplateBridge");
com/moloco/sdk/xenoss/sdkdevkit/android/adrenderer/internal/templates/ad/a.java:47:        eVar.addJavascriptInterface((com.moloco.sdk.xenoss.sdkdevkit.android.adrenderer.internal.templates.creative.mraid.a) l4c0Var.f, "AndroidMraid");
```

### boot_persist — 11 hits in 6 files

- `com/duolingo/feature/widget/WidgetUpdateOrigin.java` (3)
- `com/duolingo/feature/appicon/AppIconHelper$Origin.java` (3)
- `defpackage/qk1.java` (2)
- `defpackage/uki.java` (1)
- `defpackage/sez.java` (1)
- `defpackage/yx40.java` (1)

```
defpackage/qk1.java:161:                                if (action.equals("android.intent.action.BOOT_COMPLETED")) {
defpackage/qk1.java:162:                                    AppIconHelper$Origin appIconHelper$Origin6 = AppIconHelper$Origin.BOOT_COMPLETED;
defpackage/uki.java:126:                        if (iHashCode == 1737074039 && action.equals("android.intent.action.MY_PACKAGE_REPLACED")) {
defpackage/sez.java:185:                        if (!str.equals("android.intent.action.MY_PACKAGE_REPLACED")) {
com/duolingo/feature/widget/WidgetUpdateOrigin.java:20:    public static final WidgetUpdateOrigin WORKER_BOOT_COMPLETED;
com/duolingo/feature/widget/WidgetUpdateOrigin.java:49:        WidgetUpdateOrigin widgetUpdateOrigin10 = new WidgetUpdateOrigin("WORKER_BOOT_COMPLETED", 9, "worker_boot_completed");
com/duolingo/feature/widget/WidgetUpdateOrigin.java:50:        WORKER_BOOT_COMPLETED = widgetUpdateOrigin10;
com/duolingo/feature/appicon/AppIconHelper$Origin.java:15:    public static final AppIconHelper$Origin BOOT_COMPLETED;
com/duolingo/feature/appicon/AppIconHelper$Origin.java:35:        AppIconHelper$Origin appIconHelper$Origin4 = new AppIconHelper$Origin("BOOT_COMPLETED", 3, "boot_completed");
com/duolingo/feature/appicon/AppIconHelper$Origin.java:36:        BOOT_COMPLETED = appIconHelper$Origin4;
defpackage/yx40.java:193:            alarmManager.setAlarmClock(alarmClockInfo, pendingIntentB);
```

### full_screen_intent — 3 hits in 3 files

- `com/moloco/sdk/acm/services/a.java` (1)
- `defpackage/jy40.java` (1)
- `defpackage/eil.java` (1)

```
com/moloco/sdk/acm/services/a.java:33:            if (context.getPackageManager().checkPermission("android.permission.USE_FULL_SCREEN_INTENT", context.getPackageName()) == 0) {
defpackage/jy40.java:160:        Intent intent = new Intent("android.settings.MANAGE_APP_USE_FULL_SCREEN_INTENT", uri);
defpackage/eil.java:130:        builder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.ledARGB, notification.ledOn [... omitted en
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 132 hits in 78 files

- `com/duolingo/debug/DebugActivity.java` (12)
- `com/duolingo/profile/completion/ProfileFullNameFragment.java` (10)
- `com/duolingo/ai/roleplay/chat/RoleplayChatFragment.java` (7)
- `com/duolingo/signuplogin/SignupStepFragment.java` (6)
- `com/duolingo/settings/PasswordChangeFragment.java` (3)
- `zendesk/support/request/ViewMessageComposer.java` (2)
- `zendesk/support/request/ComponentInputForm.java` (2)
- `com/unity3d/player/AbstractC2864w.java` (2)
- `com/bytedance/sdk/openadsdk/phb/zki.java` (2)
- `com/google/android/material/button/MaterialButton.java` (2)
- `defpackage/r530.java` (2)
- `com/duolingo/core/design/juicy/ui/JuicyButton.java` (2)

```
zendesk/messaging/ui/InputBox.java:89:        this.inputTextField.addTextChangedListener(new bd70() { // from class: zendesk.messaging.ui.InputBox.4
zendesk/support/request/ViewMessageComposer.java:230:        this.inputTextField.addTextChangedListener(this);
zendesk/support/request/ViewMessageComposer.java:390:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
zendesk/support/request/ComponentInputForm.java:48:                editText.addTextChangedListener(new EditTextTextWatcher(componentInputForm));
zendesk/support/request/ComponentInputForm.java:61:        public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
com/unity3d/player/AbstractC2864w.java:77:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
com/unity3d/player/AbstractC2864w.java:135:        this.c.addTextChangedListener(this);
com/bytedance/sdk/openadsdk/phb/zki.java:259:        this.phb.addTextChangedListener(new TextWatcher() { // from class: com.bytedance.sdk.openadsdk.phb.zki.3
com/bytedance/sdk/openadsdk/phb/zki.java:269:            public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
com/google/android/material/textfield/TextInputLayout.java:488:        this.d.addTextChangedListener(new e2(this, 17));
com/google/android/material/button/MaterialButton.java:445:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
com/google/android/material/button/MaterialButton.java:446:        super.onTextChanged(charSequence, i, i2, i3);
```

### webview_tracking — 3 hits in 3 files

- `com/facebook/ads/redexgen/core/AbstractC1271Ze.java` (1)
- `com/google/android/gms/ads/internal/overlay/zzm.java` (1)
- `defpackage/jt20.java` (1)

```
com/facebook/ads/redexgen/core/AbstractC1271Ze.java:73:            CookieManager.getInstance().setAcceptThirdPartyCookies(this, true);
com/google/android/gms/ads/internal/overlay/zzm.java:774:            CookieManager.getInstance().setAcceptThirdPartyCookies(this.zzd.zzD(), r2);
defpackage/jt20.java:322:        cookieManager.setAcceptThirdPartyCookies(webView, true);
```

### streaks — 23548 hits in 2552 files

- `com/duolingo/R.java` (1671)
- `com/duolingo/sessionend/streak/StreakExtendedViewModel.java` (460)
- `defpackage/ov7.java` (367)
- `com/duolingo/streak/StreakIncreasedHeaderRedesignView.java` (331)
- `com/duolingo/feature/widget/MediumStreakWidgetAsset.java` (251)
- `com/duolingo/feature/widget/StreakWidgetResources.java` (242)
- `defpackage/s190.java` (228)
- `com/duolingo/data/user/i.java` (179)
- `defpackage/j850.java` (177)
- `defpackage/ha10.java` (164)
- `defpackage/i310.java` (138)
- `defpackage/e350.java` (136)

```
com/moloco/sdk/internal/publisher/e0.java:2384:                    x8nVar = new x8n(R.string.friend_streaks, "", p120Var.m);
com/moloco/sdk/internal/publisher/e0.java:2692:                                mknVarN.add(LessonExperienceItem.FRIENDS_STREAK);
com/duolingo/ads/BackendInterstitialAdDecisionRequest.java:138:            cw9.y(sb, this.d, this.c, ", streak=", ", accountAgeInDays=");
com/duolingo/ads/b.java:29:        yzuVar.j("streak", false);
com/duolingo/core/ads/AdOrigin.java:32:    public static final AdOrigin SHARE_STREAK;
com/duolingo/core/ads/AdOrigin.java:69:        AdOrigin adOrigin13 = new AdOrigin("SHARE_STREAK", 12, "share_streak");
com/duolingo/core/ads/AdOrigin.java:70:        SHARE_STREAK = adOrigin13;
com/duolingo/core/subscription/models/SubscriptionFeatures.java:32:    public static final SubscriptionFeatures STREAK_REPAIR;
com/duolingo/core/subscription/models/SubscriptionFeatures.java:55:        SubscriptionFeatures subscriptionFeatures9 = new SubscriptionFeatures("STREAK_REPAIR", 8);
com/duolingo/core/subscription/models/SubscriptionFeatures.java:56:        STREAK_REPAIR = subscriptionFeatures9;
com/duolingo/core/routes/annotation/RouteDescriptor.java:61:    public static final RouteDescriptor streakState;
com/duolingo/core/routes/annotation/RouteDescriptor.java:86:        RouteDescriptor routeDescriptor6 = new RouteDescriptor("streakState", 5);
```

### reengagement — 4531 hits in 1131 files

- `com/ironsource/adqualitysdk/sdk/i/db.java` (120)
- `com/duolingo/R.java` (84)
- `com/facebook/ads/redexgen/core/C0O.java` (54)
- `com/duolingo/home/path/PathViewModel.java` (53)
- `defpackage/rr0.java` (49)
- `com/duolingo/feature/resurrection/ResurrectedLoginRewardType.java` (47)
- `com/duolingo/debug/ResurrectionDebugActivity.java` (39)
- `com/duolingo/goals/resurrection/ResurrectedLoginRewardTracker$Target.java` (38)
- `defpackage/eyl.java` (35)
- `defpackage/usw.java` (35)
- `com/duolingo/core/shop/Inventory$PowerUp.java` (30)
- `defpackage/pr0.java` (30)

```
okhttp3/internal/concurrent/TaskLoggerKt.java:34:    public static final <T> T logElapsed(Logger logger, Task task, TaskQueue taskQueue, Function0 function0) {
io/sentry/g.java:2136:                        case "elapsed_since_start_ns":
io/sentry/profilemeasurements/b.java:48:        qVar.e("elapsed_since_start_ns");
com/iab/omid/library/amazon/adsession/media/PlayerState.java:9:    COLLAPSED("collapsed"),
io/sentry/android/core/internal/time/a.java:12:        return SystemClock.elapsedRealtimeNanos();
io/sentry/android/core/l.java:20:        this.a = SystemClock.elapsedRealtimeNanos();
io/sentry/android/core/l.java:21:        this.b = Process.getElapsedCpuTime() * 1000000;
io/sentry/android/core/l.java:27:            long jElapsedRealtimeNanos = SystemClock.elapsedRealtimeNanos();
io/sentry/android/core/l.java:28:            long j = jElapsedRealtimeNanos - this.a;
io/sentry/android/core/l.java:29:            this.a = jElapsedRealtimeNanos;
io/sentry/android/core/l.java:30:            long elapsedCpuTime = Process.getElapsedCpuTime() * 1000000;
io/sentry/android/core/l.java:31:            long j2 = elapsedCpuTime - this.b;
```

### notif_permission_nag — 0 hits in 0 files


```
```

### cancellation_retention — 98 hits in 19 files

- `com/duolingo/plus/management/PlusCancelSurveyActivity.java` (25)
- `com/duolingo/plus/management/Hilt_PlusCancelSurveyActivity.java` (12)
- `com/duolingo/R.java` (10)
- `defpackage/s2v.java` (8)
- `defpackage/z2v.java` (8)
- `defpackage/y2v.java` (4)
- `defpackage/m180.java` (4)
- `com/duolingo/plus/management/Hilt_PlusCancelSurveyFragment.java` (3)
- `defpackage/beo.java` (3)
- `defpackage/czu.java` (3)
- `defpackage/jeu.java` (3)
- `com/duolingo/plus/management/PlusCancelReason.java` (2)

```
com/duolingo/plus/management/PlusCancelSurveyActivity.java:12:import com.duolingo.plus.management.PlusCancelSurveyActivity;
com/duolingo/plus/management/PlusCancelSurveyActivity.java:30:public final class PlusCancelSurveyActivity extends Hilt_PlusCancelSurveyActivity {
com/duolingo/plus/management/PlusCancelSurveyActivity.java:39:        View viewInflate = getLayoutInflater().inflate(R.layout.activity_plus_cancel_survey, (ViewGroup) null, false);
com/duolingo/plus/management/PlusCancelSurveyActivity.java:43:            i2 = R.id.cancelSurveyBackground;
com/duolingo/plus/management/PlusCancelSurveyActivity.java:44:            View viewC = fk50.c(R.id.cancelSurveyBackground, viewInflate);
com/duolingo/plus/management/PlusCancelSurveyActivity.java:46:                i2 = R.id.cancelSurveyContainer;
com/duolingo/plus/management/PlusCancelSurveyActivity.java:47:                FrameLayout frameLayout = (FrameLayout) fk50.c(R.id.cancelSurveyContainer, viewInflate);
com/duolingo/plus/management/PlusCancelSurveyActivity.java:49:                    i2 = R.id.cancelSurveyContinueButton;
com/duolingo/plus/management/PlusCancelSurveyActivity.java:50:                    JuicyButton juicyButton = (JuicyButton) fk50.c(R.id.cancelSurveyContinueButton, viewInflate);
com/duolingo/plus/management/PlusCancelSurveyActivity.java:67:                                        int i5 = PlusCancelSurveyActivity.q;
com/duolingo/plus/management/PlusCancelSurveyActivity.java:73:                                        int i6 = PlusCancelSurveyActivity.q;
com/duolingo/plus/management/PlusCancelSurveyActivity.java:78:                                        int i7 = PlusCancelSurveyActivity.q;
```

### urgency_countdown — 850 hits in 214 files

- `com/bytedance/sdk/openadsdk/component/reward/top/TopLayoutDislike2.java` (44)
- `org/prebid/mobile/rendering/views/interstitial/InterstitialVideo.java` (35)
- `com/ironsource/sdk/controller/v.java` (28)
- `com/duolingo/R.java` (26)
- `defpackage/df20.java` (20)
- `defpackage/oq60.java` (19)
- `com/duolingo/feature/shardcollections/fab/ShardCollectionsFabUiState$CountdownStyle.java` (18)
- `com/ironsource/sdk/controller/e.java` (17)
- `com/bytedance/sdk/openadsdk/component/reward/vv.java` (13)
- `defpackage/bg20.java` (12)
- `com/google/android/gms/internal/pal/zzff.java` (11)
- `com/ironsource/environment/thread/IronSourceThreadManager.java` (10)

```
okhttp3/internal/concurrent/TaskQueue.java:9:import java.util.concurrent.CountDownLatch;
okhttp3/internal/concurrent/TaskQueue.java:27:        private final CountDownLatch latch;
okhttp3/internal/concurrent/TaskQueue.java:31:            this.latch = new CountDownLatch(1);
okhttp3/internal/concurrent/TaskQueue.java:34:        public final CountDownLatch getLatch() {
okhttp3/internal/concurrent/TaskQueue.java:40:            this.latch.countDown();
okhttp3/internal/concurrent/TaskQueue.java:151:    public final CountDownLatch idleLatch() {
okhttp3/internal/concurrent/TaskQueue.java:154:                return new CountDownLatch(0);
okhttp3/internal/publicsuffix/BasePublicSuffixList.java:10:import java.util.concurrent.CountDownLatch;
okhttp3/internal/publicsuffix/BasePublicSuffixList.java:18:    private final CountDownLatch readCompleteLatch = new CountDownLatch(1);
okhttp3/internal/publicsuffix/BasePublicSuffixList.java:37:            this.readCompleteLatch.countDown();
io/sentry/d0.java:3:import java.util.concurrent.CountDownLatch;
io/sentry/d0.java:10:    public final CountDownLatch c = new CountDownLatch(1);
```

### infinite_autoplay — 284 hits in 90 files

- `app/rive/runtime/kotlin/RiveAnimationView.java` (31)
- `com/google/ads/interactivemedia/v3/impl/data/AutoValue_GsonAdsRequest.java` (16)
- `app/rive/runtime/kotlin/controllers/RiveFileController.java` (15)
- `com/google/ads/interactivemedia/v3/impl/AdsRequestImpl$AutoPlayState.java` (14)
- `com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java` (13)
- `com/facebook/ads/internal/settings/AdInternalSettings.java` (10)
- `com/facebook/ads/AdSettings.java` (8)
- `com/facebook/ads/redexgen/core/EnumC1160Uu.java` (8)
- `org/prebid/mobile/api/rendering/VideoView.java` (8)
- `com/facebook/ads/NativeAdViewAttributes.java` (6)
- `com/tude/adTypes/AditudePlaybackMethod.java` (6)
- `com/facebook/ads/redexgen/core/RH.java` (6)

```
com/iab/omid/library/amazon/adsession/media/VastProperties.java:40:            jSONObject.put("autoPlay", this.c);
com/iab/omid/library/amazon/adsession/media/VastProperties.java:57:    public boolean isAutoPlay() {
com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java:11:    private final boolean autoPlayAdBreaks;
com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java:23:        private boolean autoPlayAdBreaks;
com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java:38:                return new AutoValue_ImaSdkSettingsData(this.supportsMultipleVideoDisplayChannels, this.ppid, this.playerType, this.playerVersion, this.numRedirects, this.autoPlayAdBreaks, this.debugMode, this.sessionI
com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java:48:                sb.append(" autoPlayAdBreaks");
com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java:58:        public ImaSdkSettingsData.Builder setAutoPlayAdBreaks(boolean z) {
com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java:59:            this.autoPlayAdBreaks = z;
com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java:128:        this.autoPlayAdBreaks = z2;
com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java:136:    public boolean autoPlayAdBreaks() {
com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java:137:        return this.autoPlayAdBreaks;
com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java:157:            if (this.supportsMultipleVideoDisplayChannels == imaSdkSettingsData.supportsMultipleVideoDisplayChannels() && ((str = this.ppid) != null ? str.equals(imaSdkSettingsData.ppid()) : imaSdkSettingsData.ppid() 
```

### badges — 24 hits in 13 files

- `me/leolin/shortcutbadger/impl/DefaultBadger.java` (3)
- `com/google/protobuf/EnumValue.java` (3)
- `com/google/protobuf/Field.java` (3)
- `defpackage/bz20.java` (3)
- `com/google/protobuf/EnumValueKt.java` (2)
- `com/google/protobuf/FieldKt.java` (2)
- `defpackage/eil.java` (2)
- `me/leolin/shortcutbadger/impl/SonyHomeBadger.java` (1)
- `app/rive/ViewModelInstance.java` (1)
- `defpackage/hqs.java` (1)
- `defpackage/yvb0.java` (1)
- `defpackage/xq0.java` (1)

```
me/leolin/shortcutbadger/impl/SonyHomeBadger.java:40:        contentValues.put("badge_count", Integer.valueOf(i));
me/leolin/shortcutbadger/impl/DefaultBadger.java:22:        intent.putExtra("badge_count", i);
me/leolin/shortcutbadger/impl/DefaultBadger.java:23:        intent.putExtra("badge_count_package_name", componentName.getPackageName());
me/leolin/shortcutbadger/impl/DefaultBadger.java:24:        intent.putExtra("badge_count_class_name", componentName.getClassName());
app/rive/ViewModelInstance.java:726:    public final void setNumber(String str, float f) {
defpackage/hqs.java:26:        bundle.putInt("app_badge_count", i);
com/google/protobuf/EnumValue.java:107:    public void setNumber(int i) {
com/google/protobuf/EnumValue.java:279:        public Builder setNumber(int i) {
com/google/protobuf/EnumValue.java:281:            ((EnumValue) this.instance).setNumber(i);
com/google/protobuf/EnumValueKt.java:93:        public final void setNumber(int i) {
com/google/protobuf/EnumValueKt.java:94:            this._builder.setNumber(i);
com/google/protobuf/FieldKt.java:195:        public final void setNumber(int i) {
```

### minors_age — 75 hits in 36 files

- `com/google/android/gms/common/PackageSignatureVerifier.java` (12)
- `com/google/android/gms/common/PackageVerificationResult.java` (7)
- `com/google/android/gms/ads/RequestConfiguration.java` (5)
- `com/google/android/gms/common/zzac.java` (4)
- `com/duolingo/R.java` (4)
- `com/google/android/gms/internal/pal/zzgk.java` (3)
- `com/google/android/gms/internal/ads/zzbix.java` (3)
- `com/duolingo/splash/LaunchCheckViewModel.java` (3)
- `defpackage/xkc0.java` (3)
- `com/google/ads/mediation/ironsource/IronSourceMediationAdapter.java` (2)
- `com/google/android/gms/ads/internal/client/zzeu.java` (2)
- `defpackage/ds80.java` (2)

```
com/google/ads/mediation/ironsource/IronSourceMediationAdapter.java:132:        if (requestConfiguration.getTagForChildDirectedTreatment() == 1 || requestConfiguration.getTagForUnderAgeOfConsent() == 1) {
com/google/ads/mediation/ironsource/IronSourceMediationAdapter.java:134:        } else if (requestConfiguration.getTagForChildDirectedTreatment() == 0 || requestConfiguration.getTagForUnderAgeOfConsent() == 0) {
com/google/ads/mediation/moloco/MolocoMediationAdapter.java:93:        if (MobileAds.getRequestConfiguration().getTagForChildDirectedTreatment() != 1 && MobileAds.getRequestConfiguration().getTagForUnderAgeOfConsent() != 1) {
com/google/android/gms/ads/internal/client/zzq.java:35:        return new zzm(8, -1L, bundleZzd, -1, listUnmodifiableList, zZzh, Math.max(zzehVar.zzj(), requestConfigurationZzp.getTagForChildDirectedTreatment()), false, strZzf, null, null, strZza, zzehVar.zzi(), zzehVar.zzk(), Collections.unmodifiab
com/google/android/gms/ads/internal/client/zzeu.java:179:                        if (this.zzn.getTagForChildDirectedTreatment() != -1 || this.zzn.getTagForUnderAgeOfConsent() != -1) {
com/google/android/gms/ads/internal/client/zzeu.java:565:                if (requestConfiguration2.getTagForChildDirectedTreatment() != requestConfiguration.getTagForChildDirectedTreatment() || requestConfiguration2.getTagForUnderAgeOfConsent() != requestConfiguration.getTagForUnderAgeOfConsent()) {
com/google/android/gms/ads/internal/client/zzfr.java:17:        this.zzb = requestConfiguration.getTagForUnderAgeOfConsent();
com/google/android/gms/ads/RequestConfiguration.java:92:        public Builder setTagForUnderAgeOfConsent(int i) {
com/google/android/gms/ads/RequestConfiguration.java:98:            sb.append("Invalid value passed to setTagForUnderAgeOfConsent: ");
com/google/android/gms/ads/RequestConfiguration.java:144:    public @interface TagForUnderAgeOfConsent {
com/google/android/gms/ads/RequestConfiguration.java:176:    public int getTagForUnderAgeOfConsent() {
com/google/android/gms/ads/RequestConfiguration.java:188:        builder.setTagForUnderAgeOfConsent(this.zzd);
```

### screen_time — 234 hits in 83 files

- `com/duolingo/feature/yearinreview/report/YearInReviewTimeSpentLearningUiConverter$TslPageType.java` (19)
- `com/duolingo/core/tracking/timespent/CentralTimeSpentTracker$Priority.java` (16)
- `defpackage/ks4.java` (15)
- `com/adjust/sdk/PackageBuilder.java` (14)
- `com/duolingo/feature/yearinreview/report/a.java` (11)
- `com/adjust/sdk/ActivityState.java` (10)
- `defpackage/h80.java` (7)
- `com/duolingo/R.java` (6)
- `com/duolingo/goals/dailyquests/DailyQuestType.java` (6)
- `defpackage/u7l.java` (5)
- `com/duolingo/data/yearinreview/report/YearInReviewPageType$TimeSpentLearning.java` (5)
- `defpackage/is4.java` (5)

```
com/google/android/gms/ads/identifier/AdvertisingIdClient.java:286:        mapT.put("time_spent", Long.toString(j));
com/vungle/ads/fpd/SessionContext.java:162:    public final SessionContext setTimeSpent(int i) {
com/adjust/sdk/ActivityHandler.java:1146:        activityState.sessionLength += j;
com/adjust/sdk/ActivityHandler.java:1625:        activityState.sessionLength += j2;
com/adjust/sdk/ActivityHandler.java:1626:        activityState.timeSpent += j2;
com/adjust/sdk/j.java:27:        this.d = activityState.timeSpent;
com/adjust/sdk/j.java:28:        this.e = activityState.sessionLength;
com/adjust/sdk/PackageBuilder.java:228:        addDuration(map, "session_length", this.activityStateCopy.e);
com/adjust/sdk/PackageBuilder.java:230:        addDuration(map, "time_spent", this.activityStateCopy.d);
com/adjust/sdk/PackageBuilder.java:377:        addDuration(map, "session_length", this.activityStateCopy.e);
com/adjust/sdk/PackageBuilder.java:380:        addDuration(map, "time_spent", this.activityStateCopy.d);
com/adjust/sdk/PackageBuilder.java:622:        addDuration(map, "session_length", this.activityStateCopy.e);
```

