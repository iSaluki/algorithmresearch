# Pattern scan: work/bbcnews_ww/jdex

## Code categories (library packages excluded)

### installed_apps — 51 hits in 38 files

- `classes4:uk/co/bbc/authtoolkit/capability/CustomTabPackageProvider.java` (4)
- `classes8:com/google/android/gms/common/GooglePlayServicesUtilLight.java` (4)
- `classes6:cl/json/social/ShareIntent.java` (3)
- `classes4:uk/co/bbc/authtoolkit/capability/AppLinkVerifier.java` (2)
- `classes5:androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java` (2)
- `classes8:com/google/android/gms/internal/ads/zzimy.java` (2)
- `classes8:com/google/android/gms/internal/ads/zzfcj.java` (2)
- `classes8:com/google/android/gms/internal/ads/zzbzm.java` (2)
- `classes:androidx/appcompat/widget/ActivityChooserModel.java` (1)
- `classes:androidx/compose/foundation/text/contextmenu/ProcessTextApi23Impl.java` (1)
- `classes:androidx/browser/browseractions/BrowserActionsIntent.java` (1)
- `classes:androidx/browser/trusted/TrustedWebActivityServiceConnectionPool.java` (1)

```
classes:androidx/appcompat/widget/ActivityChooserModel.java:266:        List<ResolveInfo> listQueryIntentActivities = this.mContext.getPackageManager().queryIntentActivities(this.mIntent, 0);
classes:androidx/compose/foundation/text/contextmenu/ProcessTextApi23Impl.java:52:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(INSTANCE.createProcessTextIntent(), 0);
classes:androidx/browser/browseractions/BrowserActionsIntent.java:178:        return context.getPackageManager().queryIntentActivities(new Intent(ACTION_BROWSER_ACTIONS_OPEN, Uri.parse(TEST_URL)), 131072);
classes:androidx/browser/trusted/TrustedWebActivityServiceConnectionPool.java:110:        Iterator<ResolveInfo> it = context.getPackageManager().queryIntentActivities(intent, 65536).iterator();
classes10:com/sourcepoint/cmplibrary/util/WebViewUtilsKt.java:53:        List<ResolveInfo> listQueryIntentActivities = packageManager.queryIntentActivities(intent, 131072);
classes4:org/prebid/mobile/rendering/utils/helpers/ExternalViewerUtils.java:41:            return context.getPackageManager().queryIntentActivities(intent, 65536).size() > 0;
classes4:uk/co/bbc/authtoolkit/accountlinking/alexa/ImplementationVerifyAlexaCheck.java:36:            PackageInfo packageInfo = this.context.getPackageManager().getPackageInfo("com.amazon.dee.app", 0);
classes4:uk/co/bbc/authtoolkit/capability/AppLinkVerifier.java:73:        List<ResolveInfo> listQueryIntentActivities = this.context.getPackageManager().queryIntentActivities(intent, 65536);
classes4:uk/co/bbc/authtoolkit/capability/AppLinkVerifier.java:74:        Intrinsics.checkNotNullExpressionValue(listQueryIntentActivities, "queryIntentActivities(...)");
classes4:uk/co/bbc/authtoolkit/capability/CustomTabPackageProvider.java:56:        List<ResolveInfo> listQueryIntentActivities = this.pm.queryIntentActivities(this.activityIntent, 65536);
classes4:uk/co/bbc/authtoolkit/capability/CustomTabPackageProvider.java:57:        Intrinsics.checkNotNullExpressionValue(listQueryIntentActivities, "queryIntentActivities(...)");
classes4:uk/co/bbc/authtoolkit/capability/CustomTabPackageProvider.java:69:        List<ResolveInfo> listQueryIntentActivities = this.pm.queryIntentActivities(this.activityIntent, 131072);
```

### usage_stats — 0 hits in 0 files


```
```

### clipboard — 10 hits in 5 files

- `classes10:com/reactnativecommunity/clipboard/ClipboardModule.java` (5)
- `classes5:androidx/compose/ui/platform/AndroidClipboardManager.java` (2)
- `classes:androidx/appcompat/widget/AppCompatReceiveContentHelper.java` (1)
- `classes:androidx/compose/foundation/text/input/internal/selection/ClipboardPasteState.java` (1)
- `classes7:com/facebook/react/modules/clipboard/ClipboardModule.java` (1)

```
classes:androidx/appcompat/widget/AppCompatReceiveContentHelper.java:30:        ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
classes:androidx/compose/foundation/text/input/internal/selection/ClipboardPasteState.java:39:        boolean zHasPrimaryClip = this.clipboard.getNativeClipboard().hasPrimaryClip();
classes10:com/reactnativecommunity/clipboard/ClipboardModule.java:71:            ClipData primaryClip = getClipboardService().getPrimaryClip();
classes10:com/reactnativecommunity/clipboard/ClipboardModule.java:121:            ClipData primaryClip = getClipboardService().getPrimaryClip();
classes10:com/reactnativecommunity/clipboard/ClipboardModule.java:166:        if (!clipboardService.hasPrimaryClip()) {
classes10:com/reactnativecommunity/clipboard/ClipboardModule.java:174:        ClipData primaryClip = clipboardService.getPrimaryClip();
classes10:com/reactnativecommunity/clipboard/ClipboardModule.java:257:            clipboardService.addPrimaryClipChangedListener(onPrimaryClipChangedListener);
classes5:androidx/compose/ui/platform/AndroidClipboardManager.java:37:        ClipData primaryClip = this.clipboardManager.getPrimaryClip();
classes5:androidx/compose/ui/platform/AndroidClipboardManager.java:56:        ClipData primaryClip = this.clipboardManager.getPrimaryClip();
classes7:com/facebook/react/modules/clipboard/ClipboardModule.java:36:            ClipData primaryClip = getClipboardService().getPrimaryClip();
```

### contacts — 7 hits in 3 files

- `classes7:com/bumptech/glide/load/data/StreamLocalUriFetcher.java` (3)
- `classes7:com/facebook/imagepipeline/producers/LocalContentUriFetchProducer.java` (2)
- `classes7:com/facebook/common/util/UriUtil.java` (2)

```
classes7:com/bumptech/glide/load/data/StreamLocalUriFetcher.java:7:import android.provider.ContactsContract;
classes7:com/bumptech/glide/load/data/StreamLocalUriFetcher.java:65:        Uri uriLookupContact = ContactsContract.Contacts.lookupContact(contentResolver, uri);
classes7:com/bumptech/glide/load/data/StreamLocalUriFetcher.java:73:        return ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uri, true);
classes7:com/facebook/imagepipeline/producers/LocalContentUriFetchProducer.java:7:import android.provider.ContactsContract;
classes7:com/facebook/imagepipeline/producers/LocalContentUriFetchProducer.java:65:                    InputStream inputStreamOpenContactPhotoInputStream = ContactsContract.Contacts.openContactPhotoInputStream(this.contentResolver, sourceUri);
classes7:com/facebook/common/util/UriUtil.java:7:import android.provider.ContactsContract;
classes7:com/facebook/common/util/UriUtil.java:25:    private static final Uri LOCAL_CONTACT_IMAGE_URI = Uri.withAppendedPath((Uri) Assertions.assumeNotNull(ContactsContract.AUTHORITY_URI), "display_photo");
```

### call_log — 0 hits in 0 files


```
```

### sms — 27 hits in 10 files

- `classes8:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java` (7)
- `classes8:com/google/android/gms/internal/p001authapiphone/zzab.java` (5)
- `classes8:com/google/android/gms/auth/api/phone/SmsRetriever.java` (4)
- `classes8:com/google/android/gms/internal/p001authapiphone/zzw.java` (3)
- `classes8:com/google/android/gms/auth/api/phone/SmsRetrieverApi.java` (2)
- `classes8:com/google/android/gms/auth/api/phone/SmsRetrieverStatusCodes.java` (2)
- `classes6:cl/json/social/SMSShare.java` (1)
- `classes8:com/google/android/gms/internal/p001authapiphone/zza.java` (1)
- `classes8:com/google/android/gms/internal/p001authapiphone/zzi.java` (1)
- `classes8:com/google/android/gms/internal/p001authapiphone/zzh.java` (1)

```
classes6:cl/json/social/SMSShare.java:32:        return Telephony.Sms.getDefaultSmsPackage(this.reactContext);
classes8:com/google/android/gms/auth/api/phone/SmsRetrieverApi.java:7:public interface SmsRetrieverApi {
classes8:com/google/android/gms/auth/api/phone/SmsRetrieverApi.java:8:    Task<Void> startSmsRetriever();
classes8:com/google/android/gms/auth/api/phone/SmsRetriever.java:9:public final class SmsRetriever {
classes8:com/google/android/gms/auth/api/phone/SmsRetriever.java:17:    private SmsRetriever() {
classes8:com/google/android/gms/auth/api/phone/SmsRetriever.java:20:    public static SmsRetrieverClient getClient(Activity activity) {
classes8:com/google/android/gms/auth/api/phone/SmsRetriever.java:24:    public static SmsRetrieverClient getClient(Context context) {
classes8:com/google/android/gms/auth/api/phone/SmsRetrieverStatusCodes.java:7:public final class SmsRetrieverStatusCodes extends CommonStatusCodes {
classes8:com/google/android/gms/auth/api/phone/SmsRetrieverStatusCodes.java:12:    private SmsRetrieverStatusCodes() {
classes8:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java:11:public abstract class SmsRetrieverClient extends GoogleApi<Api.ApiOptions.NoOptions> implements SmsRetrieverApi {
classes8:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java:21:        zzc = new Api("SmsRetriever.API", zzaVar, clientKey);
classes8:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java:24:    public SmsRetrieverClient(Activity activity) {
```

### location — 73 hits in 17 files

- `classes5:androidx/core/location/LocationManagerCompat.java` (19)
- `classes9:com/google/android/gms/location/FusedLocationProviderClient.java` (18)
- `classes:androidx/appcompat/app/TwilightManager.java` (6)
- `classes7:com/google/android/gms/internal/location/zzz.java` (4)
- `classes9:com/google/android/gms/location/FusedLocationProviderApi.java` (4)
- `classes9:com/google/android/gms/location/LocationServices.java` (4)
- `classes7:com/google/android/gms/internal/location/zzaf.java` (3)
- `classes11:dotmetrics/analytics/DotmetricsSession.java` (2)
- `classes4:org/prebid/mobile/rendering/sdk/deviceData/managers/LastKnownLocationInfoManager.java` (2)
- `classes9:com/google/android/gms/location/zzak.java` (2)
- `classes9:com/google/android/gms/location/GeofencingApi.java` (2)
- `classes9:com/google/android/gms/location/zzaj.java` (2)

```
classes:androidx/appcompat/app/TwilightManager.java:43:        Location lastKnownLocation = getLastKnownLocation();
classes:androidx/appcompat/app/TwilightManager.java:53:    private Location getLastKnownLocation() {
classes:androidx/appcompat/app/TwilightManager.java:54:        Location lastKnownLocationForProvider = PermissionChecker.checkSelfPermission(this.mContext, "android.permission.ACCESS_COARSE_LOCATION") == 0 ? getLastKnownLocationForProvider("network") : null;
classes:androidx/appcompat/app/TwilightManager.java:55:        Location lastKnownLocationForProvider2 = PermissionChecker.checkSelfPermission(this.mContext, "android.permission.ACCESS_FINE_LOCATION") == 0 ? getLastKnownLocationForProvider("gps") : null;
classes:androidx/appcompat/app/TwilightManager.java:59:    private Location getLastKnownLocationForProvider(String str) {
classes:androidx/appcompat/app/TwilightManager.java:62:                return this.mLocationManager.getLastKnownLocation(str);
classes10:com/urbanairship/google/PlayServicesUtils.java:40:            Class.forName("com.google.android.gms.location.FusedLocationProviderClient");
classes11:dotmetrics/analytics/DotmetricsSession.java:1733:                            lastKnownLocation = locationManager.getLastKnownLocation("gps");
classes11:dotmetrics/analytics/DotmetricsSession.java:1744:                    Location lastKnownLocation2 = context.getPackageManager().checkPermission("android.permission.ACCESS_COARSE_LOCATION", context.getPackageName()) == 0 ? locationManager.getLastKnownLocation("network") : null;
classes4:org/prebid/mobile/rendering/sdk/deviceData/managers/LastKnownLocationInfoManager.java:35:                    lastKnownLocation = locationManager.getLastKnownLocation("gps");
classes4:org/prebid/mobile/rendering/sdk/deviceData/managers/LastKnownLocationInfoManager.java:36:                    lastKnownLocation2 = this.locManager.getLastKnownLocation("network");
classes5:androidx/core/location/LocationManagerCompat.java:64:    public static void getCurrentLocation(LocationManager locationManager, String str, CancellationSignal cancellationSignal, Executor executor, Consumer<Location> consumer) {
```

### wifi_bt_scan — 2 hits in 1 files

- `classes10:com/reactnativecommunity/netinfo/ConnectivityReceiver.java` (2)

```
classes10:com/reactnativecommunity/netinfo/ConnectivityReceiver.java:182:                        String ssid = connectionInfo.getSSID();
classes10:com/reactnativecommunity/netinfo/ConnectivityReceiver.java:189:                        String bssid = connectionInfo.getBSSID();
```

### device_ids — 117 hits in 56 files

- `classes11:de/spring/mobile/SpringStreamsBase.java` (6)
- `classes5:androidx/core/telephony/TelephonyManagerCompat.java` (6)
- `classes6:com/amazonaws/services/cognitosync/model/UpdateRecordsRequest.java` (6)
- `classes6:com/amazonaws/services/cognitosync/model/RegisterDeviceResult.java` (6)
- `classes6:com/amazonaws/services/cognitosync/model/UnsubscribeFromDatasetRequest.java` (6)
- `classes6:com/amazonaws/services/cognitosync/model/SubscribeToDatasetRequest.java` (6)
- `classes4:uk/co/bbc/echo/identity/UserPromiseHelper.java` (5)
- `classes10:com/mobile/fedid/FedIdManager.java` (4)
- `classes4:uk/co/bbc/echo/EchoClient.java` (4)
- `classes4:uk/co/bbc/federated_id_client_android/FederatedIDHelpers.java` (3)
- `classes4:uk/co/bbc/echo/device/DefaultDeviceDataProvider.java` (3)
- `classes5:androidx/core/widget/NestedScrollView.java` (3)

```
classes:androidx/appcompat/app/WindowDecorActionBar.java:1279:        menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
classes:androidx/appcompat/app/ToolbarActionBar.java:437:        menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
classes:androidx/appcompat/app/AppCompatDelegateImpl.java:1480:            panelFeatureState.qwertyMode = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;
classes10:com/learnium/RNDeviceInfo/RNDeviceModule.java:726:                return Build.getSerial();
classes10:com/learnium/RNDeviceInfo/RNDeviceModule.java:882:        return Settings.Secure.getString(getReactApplicationContext().getContentResolver(), "android_id");
classes10:com/mobile/piano/PianoComposer.java:228:        return (echo == null || (deviceId = echo.getDeviceId()) == null) ? SessionIdProviderImpl.UNSET_SESSION_ID : deviceId;
classes10:com/mobile/fedid/FedIdManager.java:116:            String deviceId = federatedIDHelpers2 != null ? federatedIDHelpers2.getDeviceId() : null;
classes10:com/mobile/fedid/FedIdManager.java:132:    public String getDeviceId() {
classes10:com/mobile/fedid/FedIdManager.java:135:            return federatedIDHelpers.getDeviceId();
classes10:com/mobile/fedid/FedIdManager.java:147:        String deviceId = federatedIDHelpers != null ? federatedIDHelpers.getDeviceId() : null;
classes10:com/mobile/NativeFedIdManagerSpec.java:29:    public abstract String getDeviceId();
classes10:com/swmansion/gesturehandler/core/GestureHandler.java:707:                    MotionEvent motionEventObtain = MotionEvent.obtain(downTime, eventTime, i3, i4, pointerPropertiesArr, pointerCoordsArr2, event.getMetaState(), event.getButtonState(), event.getXPrecision(), event.getYPrecision(),
```

### gsf_id — 4 hits in 2 files

- `classes7:com/google/android/gms/internal/measurement/zzjg.java` (2)
- `classes8:com/google/android/gms/internal/auth/zzcb.java` (2)

```
classes7:com/google/android/gms/internal/measurement/zzjg.java:9:    public static final Uri zza = Uri.parse("content://com.google.android.gsf.gservices");
classes7:com/google/android/gms/internal/measurement/zzjg.java:10:    public static final Uri zzb = Uri.parse("content://com.google.android.gsf.gservices/prefix");
classes8:com/google/android/gms/internal/auth/zzcb.java:16:    public static final Uri zza = Uri.parse("content://com.google.android.gsf.gservices");
classes8:com/google/android/gms/internal/auth/zzcb.java:17:    public static final Uri zzb = Uri.parse("content://com.google.android.gsf.gservices/prefix");
```

### advertising_id — 415 hits in 62 files

- `classes6:androidx/privacysandbox/ads/adservices/measurement/MeasurementManagerImplCommon.java` (36)
- `classes6:androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures.java` (30)
- `classes6:androidx/privacysandbox/ads/adservices/java/adid/AdIdManagerFutures.java` (18)
- `classes6:androidx/privacysandbox/ads/adservices/java/topics/TopicsManagerFutures.java` (18)
- `classes6:androidx/privacysandbox/ads/adservices/topics/TopicsManager.java` (16)
- `classes8:com/google/android/gms/ads/identifier/AdvertisingIdClient.java` (16)
- `classes6:androidx/privacysandbox/ads/adservices/adid/AdIdManagerImplCommon.java` (15)
- `classes6:androidx/privacysandbox/ads/adservices/topics/TopicsManagerImplCommon.java` (15)
- `classes6:androidx/privacysandbox/ads/adservices/measurement/MeasurementManager.java` (12)
- `classes6:androidx/privacysandbox/ads/adservices/adid/AdIdManager.java` (11)
- `classes6:androidx/transition/Transition$Impl26$$ExternalSyntheticApiModelOutline0.java` (8)
- `classes6:androidx/privacysandbox/ads/adservices/measurement/MeasurementManagerImplCommon$registerSource$4$1$1.java` (8)

```
classes10:com/mobile/gaid/GAIDModule.java:8:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
classes10:com/mobile/gaid/GAIDModule.java:87:                AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.$context);
classes10:com/mobile/gaid/GAIDModule.java:88:                Intrinsics.checkNotNullExpressionValue(advertisingIdInfo, "getAdvertisingIdInfo(...)");
classes10:com/urbanairship/google/PlayServicesUtils.java:58:            Class.forName("com.google.android.gms.ads.identifier.AdvertisingIdClient");
classes11:dotmetrics/analytics/DatapointHelper.java:99:            Object objInvoke = Class.forName("com.google.android.gms.ads.identifier.AdvertisingIdClient").getMethod("getAdvertisingIdInfo", Context.class).invoke(null, context);
classes11:dotmetrics/analytics/DatapointHelper.java:100:            Class<?> cls = Class.forName("com.google.android.gms.ads.identifier.AdvertisingIdClient$Info");
classes11:de/spring/mobile/SpringStreamsBase.java:727:            Class<?> cls = Class.forName("com.google.android.gms.ads.identifier.AdvertisingIdClient");
classes11:de/spring/mobile/SpringStreamsBase.java:731:            Object objInvoke = cls.getMethod("getAdvertisingIdInfo", Context.class).invoke(null, context);
classes11:io/piano/android/analytics/idproviders/GoogleAdvertisingIdProvider.java:4:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
classes11:io/piano/android/analytics/idproviders/GoogleAdvertisingIdProvider.java:48:            AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.context);
classes11:io/piano/android/analytics/idproviders/HuaweiAdvertisingIDIdProvider.java:4:import com.huawei.hms.ads.identifier.AdvertisingIdClient;
classes11:io/piano/android/analytics/idproviders/HuaweiAdvertisingIDIdProvider.java:48:            AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.context);
```

### install_referrer — 74 hits in 10 files

- `classes10:com/learnium/RNDeviceInfo/RNInstallReferrerClient.java` (18)
- `classes7:com/android/installreferrer/api/InstallReferrerClientImpl.java` (14)
- `classes7:com/appsflyer/internal/AFi1aSDK.java` (13)
- `classes8:com/google/android/gms/internal/ads/zzars.java` (11)
- `classes10:com/learnium/RNDeviceInfo/RNDeviceModule.java` (5)
- `classes7:com/android/installreferrer/api/InstallReferrerClient.java` (4)
- `classes8:com/google/android/gms/internal/ads/zzarv.java` (4)
- `classes7:com/appsflyer/internal/AFj1oSDK.java` (2)
- `classes8:com/google/android/gms/internal/ads/zzarr.java` (2)
- `classes7:com/android/installreferrer/api/ReferrerDetails.java` (1)

```
classes10:com/learnium/RNDeviceInfo/RNDeviceModule.java:71:    private RNInstallReferrerClient installReferrerClient;
classes10:com/learnium/RNDeviceInfo/RNDeviceModule.java:92:        this.installReferrerClient = new RNInstallReferrerClient(reactApplicationContext.getBaseContext());
classes10:com/learnium/RNDeviceInfo/RNDeviceModule.java:637:    public String getInstallReferrerSync() {
classes10:com/learnium/RNDeviceInfo/RNDeviceModule.java:642:    public void getInstallReferrer(Promise promise) {
classes10:com/learnium/RNDeviceInfo/RNDeviceModule.java:643:        promise.resolve(getInstallReferrerSync());
classes10:com/learnium/RNDeviceInfo/RNInstallReferrerClient.java:16:public class RNInstallReferrerClient {
classes10:com/learnium/RNDeviceInfo/RNInstallReferrerClient.java:17:    private static Class<?> InstallReferrerClientClazz = null;
classes10:com/learnium/RNDeviceInfo/RNInstallReferrerClient.java:31:            InstallReferrerClientClazz = Class.forName("com.android.installreferrer.api.InstallReferrerClient");
classes10:com/learnium/RNDeviceInfo/RNInstallReferrerClient.java:35:            System.err.println("RNInstallReferrerClient exception. 'installreferrer' APIs are unavailable.");
classes10:com/learnium/RNDeviceInfo/RNInstallReferrerClient.java:39:    RNInstallReferrerClient(final Context context) {
classes10:com/learnium/RNDeviceInfo/RNInstallReferrerClient.java:44:        if (InstallReferrerClientClazz == null || InstallReferrerStateListenerClazz == null || ReferrerDetailsClazz == null) {
classes10:com/learnium/RNDeviceInfo/RNInstallReferrerClient.java:47:        executorServiceNewSingleThreadExecutor.execute(new Runnable() { // from class: com.learnium.RNDeviceInfo.RNInstallReferrerClient$$ExternalSyntheticLambda0
```

### sensors — 0 hits in 0 files


```
```

### accounts — 1 hits in 1 files

- `classes8:com/google/android/gms/auth/zzl.java` (1)

```
classes8:com/google/android/gms/auth/zzl.java:97:        AccountManager.get(context).invalidateAuthToken("com.google", str);
```

### battery_state — 1 hits in 1 files

- `classes8:com/google/android/gms/internal/ads/zzewd.java` (1)

```
classes8:com/google/android/gms/internal/ads/zzewd.java:58:            zIsCharging = batteryManager != null ? batteryManager.isCharging() : zze(zzd());
```

### screen_capture_detect — 5 hits in 1 files

- `classes7:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java` (5)

```
classes7:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:44:    private static final int SCREENSHOT_OUTPUT_SIZE_HINT = 65536;
classes7:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:45:    private static final int SCREENSHOT_QUALITY = 80;
classes7:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:46:    private static final float SCREENSHOT_SCALE_FACTOR = 1.0f;
classes7:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:420:            bitmapCreateScaledBitmap = Bitmap.createScaledBitmap(bitmap, (int) ((width / f) * SCREENSHOT_SCALE_FACTOR), (int) ((height / f) * SCREENSHOT_SCALE_FACTOR), true);
classes7:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:426:                    bitmapCreateScaledBitmap.compress(compressFormat, SCREENSHOT_QUALITY, byteArrayOutputStream2);
```

### audio_capture — 0 hits in 0 files


```
```

### accessibility — 352 hits in 60 files

- `classes7:com/facebook/react/modules/accessibilityinfo/AccessibilityInfoModule.java` (24)
- `classes5:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java` (23)
- `classes5:androidx/core/view/accessibility/AccessibilityManagerCompat.java` (20)
- `classes:androidx/compose/material3/internal/Listener.java` (14)
- `classes10:com/urbanairship/android/layout/environment/State.java` (14)
- `classes5:androidx/compose/ui/platform/AndroidAccessibilityManager.java` (11)
- `classes10:com/urbanairship/android/layout/model/PagerModel.java` (10)
- `classes10:com/urbanairship/android/layout/view/PagerView.java` (10)
- `classes11:com/urbanairship/messagecenter/ui/widget/MessageRecyclerView.java` (10)
- `classes9:com/google/android/material/textfield/MaterialAutoCompleteTextView.java` (9)
- `classes9:com/google/android/material/textfield/DropdownMenuEndIconDelegate.java` (9)
- `classes10:com/sourcepoint/cmplibrary/SpConsentLibMobileCore.java` (8)

```
classes:androidx/appcompat/widget/TooltipCompatHandler.java:9:import android.view.accessibility.AccessibilityManager;
classes:androidx/appcompat/widget/TooltipCompatHandler.java:91:        AccessibilityManager accessibilityManager = (AccessibilityManager) this.mAnchor.getContext().getSystemService("accessibility");
classes:androidx/appcompat/widget/TooltipCompatHandler.java:92:        if (accessibilityManager.isEnabled() && accessibilityManager.isTouchExplorationEnabled()) {
classes:androidx/compose/material3/internal/AccessibilityServiceStateProvider_androidKt.java:4:import android.view.accessibility.AccessibilityManager;
classes:androidx/compose/material3/internal/AccessibilityServiceStateProvider_androidKt.java:63:        Intrinsics.checkNotNull(systemService, "null cannot be cast to non-null type android.view.accessibility.AccessibilityManager");
classes:androidx/compose/material3/internal/AccessibilityServiceStateProvider_androidKt.java:64:        final AccessibilityManager accessibilityManager = (AccessibilityManager) systemService;
classes:androidx/compose/material3/internal/AccessibilityServiceStateProvider_androidKt.java:121:    public static final Unit rememberAccessibilityServiceState$lambda$2$lambda$1(Listener listener, AccessibilityManager accessibilityManager, Lifecycle.Event event) {
classes:androidx/compose/material3/internal/AccessibilityServiceStateProvider_androidKt.java:129:    public static final Unit rememberAccessibilityServiceState$lambda$4$lambda$3(Listener listener, AccessibilityManager accessibilityManager) {
classes:androidx/compose/material3/SnackbarHostKt.java:30:import androidx.compose.ui.platform.AccessibilityManager;
classes:androidx/compose/material3/SnackbarHostKt.java:47:@Metadata(d1 = {"\u0000Z\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\t\n\u0002\u0018\u0002\n\u0000\n\u00
classes:androidx/compose/material3/SnackbarHostKt.java:127:            ProvidableCompositionLocal localAccessibilityManager = CompositionLocalsKt.getLocalAccessibilityManager();
classes:androidx/compose/material3/SnackbarHostKt.java:129:            Object objConsume = composerStartRestartGroup.consume(localAccessibilityManager);
```

### root_emulator — 930 hits in 125 files

- `classes:androidx/compose/material3/ExposedDropdownMenuBoxScope.java` (72)
- `classes:androidx/compose/material3/ExposedDropdownMenuKt.java` (67)
- `classes:androidx/compose/material/ExposedDropdownMenu_androidKt.java` (61)
- `classes:androidx/compose/material/internal/ExposedDropdownMenuPopup_androidKt.java` (49)
- `classes:androidx/compose/material/ExposedDropdownMenuBoxScope.java` (36)
- `classes:androidx/compose/material3/ExposedDropdownMenuDefaults.java` (30)
- `classes:androidx/compose/material/ExposedDropdownMenuDefaults.java` (28)
- `classes:androidx/compose/material3/ExposedDropdownMenuKt$ExposedDropdownMenuBox$scope$1$1.java` (27)
- `classes:androidx/compose/material/DefaultTextFieldForExposedDropdownMenusColors.java` (25)
- `classes:androidx/compose/material3/ExposedDropdownMenu_androidKt.java` (23)
- `classes:androidx/compose/material/internal/ExposedDropdownMenuPopup_androidKt$ExposedDropdownMenuPopup$popupLayout$1$1$1.java` (20)
- `classes10:com/sourcepoint/cmplibrary/model/exposed/PreferencesConsentInternal.java` (18)

```
classes:androidx/compose/material3/internal/Strings.java:66:    @Metadata(d1 = {"\u0000\u0015\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0003\b\u0093\u0001\b\u0086\u0003\u0018\u00002\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u0003R\u0012\u0010\u0004\u001a
classes:androidx/compose/material3/internal/Strings.java:80:        /* renamed from: getExposedDropdownMenu-8iCLdWM, reason: not valid java name */
classes:androidx/compose/material3/internal/Strings.java:81:        public final int m4463getExposedDropdownMenu8iCLdWM() {
classes:androidx/compose/material3/ExposedDropdownMenuDefaults.java:25:/* compiled from: ExposedDropdownMenu.kt */
classes:androidx/compose/material3/ExposedDropdownMenuDefaults.java:26:@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\
classes:androidx/compose/material3/ExposedDropdownMenuDefaults.java:28:public final class ExposedDropdownMenuDefaults {
classes:androidx/compose/material3/ExposedDropdownMenuDefaults.java:30:    public static final ExposedDropdownMenuDefaults INSTANCE = new ExposedDropdownMenuDefaults();
classes:androidx/compose/material3/ExposedDropdownMenuDefaults.java:31:    private static final PaddingValues ItemContentPadding = PaddingKt.m1022PaddingValuesYgX7TsA(ExposedDropdownMenuKt.ExposedDropdownMenuItemHorizontalPadding, Dp.constructor-impl(0));
classes:androidx/compose/material3/ExposedDropdownMenuDefaults.java:34:    public static final Unit TrailingIcon$lambda$0(ExposedDropdownMenuDefaults exposedDropdownMenuDefaults, boolean z, Modifier modifier, int i, int i2, Composer composer, int i3) {
classes:androidx/compose/material3/ExposedDropdownMenuDefaults.java:35:        exposedDropdownMenuDefaults.TrailingIcon(z, modifier, composer, RecomposeScopeImplKt.updateChangedFlags(i | 1), i2);
classes:androidx/compose/material3/ExposedDropdownMenuDefaults.java:40:    public static final Unit TrailingIcon$lambda$1(ExposedDropdownMenuDefaults exposedDropdownMenuDefaults, boolean z, int i, Composer composer, int i2) {
classes:androidx/compose/material3/ExposedDropdownMenuDefaults.java:41:        exposedDropdownMenuDefaults.TrailingIcon(z, composer, RecomposeScopeImplKt.updateChangedFlags(i | 1));
```

### js_bridge — 12 hits in 11 files

- `classes11:expo/modules/webview/DomWebView.java` (2)
- `classes10:com/reactnativecommunity/webview/RNCWebView.java` (1)
- `classes10:com/urbanairship/android/layout/view/MediaView.java` (1)
- `classes10:com/sourcepoint/cmplibrary/mobile_core/SPConsentWebView.java` (1)
- `classes11:expo/modules/logbox/ExpoLogBoxWebViewWrapper.java` (1)
- `classes11:io/piano/android/composer/showtemplate/ShowTemplateController.java` (1)
- `classes12:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java` (1)
- `classes4:org/prebid/mobile/rendering/views/webview/WebViewInterstitial.java` (1)
- `classes4:org/prebid/mobile/rendering/views/webview/WebViewBanner.java` (1)
- `classes8:com/google/android/gms/ads/nonagon/signalgeneration/zzap.java` (1)
- `classes8:com/google/android/gms/internal/ads/zzcll.java` (1)

```
classes10:com/reactnativecommunity/webview/RNCWebView.java:231:            addJavascriptInterface(rNCWebViewBridge, JAVASCRIPT_INTERFACE);
classes10:com/urbanairship/android/layout/view/MediaView.java:679:        touchAwareWebView.addJavascriptInterface(touchAwareWebView.getJavascriptInterface(), "VideoListenerInterface");
classes10:com/sourcepoint/cmplibrary/mobile_core/SPConsentWebView.java:164:        addJavascriptInterface(this, "JSReceiver");
classes11:expo/modules/webview/DomWebView.java:350:        webView.addJavascriptInterface(this.rncWebViewBridge, "ReactNativeWebView");
classes11:expo/modules/webview/DomWebView.java:351:        webView.addJavascriptInterface(new DomWebViewBridge(this), "ExpoDomWebViewBridge");
classes11:expo/modules/logbox/ExpoLogBoxWebViewWrapper.java:65:        webView.addJavascriptInterface(new Object() { // from class: expo.modules.logbox.ExpoLogBoxWebViewWrapper$webView$1$1
classes11:io/piano/android/composer/showtemplate/ShowTemplateController.java:203:            webView.addJavascriptInterface(composerJs, ShowTemplateController.JAVASCRIPT_INTERFACE);
classes12:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java:39:        public void addJavascriptInterface(Object obj, String str, List<String> list) {
classes4:org/prebid/mobile/rendering/views/webview/WebViewInterstitial.java:35:        addJavascriptInterface(interstitialJSInterface, "jsBridge");
classes4:org/prebid/mobile/rendering/views/webview/WebViewBanner.java:45:        addJavascriptInterface(bannerJSInterface, "jsBridge");
classes8:com/google/android/gms/ads/nonagon/signalgeneration/zzap.java:619:            webView.addJavascriptInterface(new TaggingLibraryJsInterface(webView, this.zzh, this.zzp, this.zzq, this.zzi, this.zzJ, zzaVar, zzeVar), "gmaSdk");
classes8:com/google/android/gms/internal/ads/zzcll.java:155:        addJavascriptInterface(new zzclt(this, new zzcls() { // from class: com.google.android.gms.internal.ads.zzclr
```

### boot_persist — 6 hits in 2 files

- `classes5:androidx/core/app/AlarmManagerCompat.java` (4)
- `classes10:com/transistorsoft/tsbackgroundfetch/BGTask.java` (2)

```
classes10:com/transistorsoft/tsbackgroundfetch/BGTask.java:195:                    alarmManager.setExactAndAllowWhileIdle(0, jCurrentTimeMillis, alarmPI);
classes10:com/transistorsoft/tsbackgroundfetch/BGTask.java:202:            alarmManager.setExactAndAllowWhileIdle(0, jCurrentTimeMillis, alarmPI);
classes5:androidx/core/app/AlarmManagerCompat.java:10:    public static void setAlarmClock(AlarmManager alarmManager, long j, PendingIntent pendingIntent, PendingIntent pendingIntent2) {
classes5:androidx/core/app/AlarmManagerCompat.java:11:        alarmManager.setAlarmClock(new AlarmManager.AlarmClockInfo(j, pendingIntent), pendingIntent2);
classes5:androidx/core/app/AlarmManagerCompat.java:24:    public static void setExactAndAllowWhileIdle(AlarmManager alarmManager, int i, long j, PendingIntent pendingIntent) {
classes5:androidx/core/app/AlarmManagerCompat.java:25:        alarmManager.setExactAndAllowWhileIdle(i, j, pendingIntent);
```

### full_screen_intent — 4 hits in 3 files

- `classes5:androidx/core/app/NotificationCompat.java` (2)
- `classes5:androidx/core/app/NotificationCompatBuilder.java` (1)
- `classes5:androidx/core/app/NotificationManagerCompat.java` (1)

```
classes5:androidx/core/app/NotificationCompatBuilder.java:41:        this.mBuilder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, builder.mTickerView).setVibrate(notification.vibrate).setLight
classes5:androidx/core/app/NotificationManagerCompat.java:378:            return this.mContext.checkSelfPermission("android.permission.USE_FULL_SCREEN_INTENT") == 0;
classes5:androidx/core/app/NotificationCompat.java:265:            setContentTitle(NotificationCompat.getContentTitle(notification)).setContentText(NotificationCompat.getContentText(notification)).setContentInfo(NotificationCompat.getContentInfo(notification)).setSubText(NotificationCompat.getSubTex
classes5:androidx/core/app/NotificationCompat.java:492:        public Builder setFullScreenIntent(PendingIntent pendingIntent, boolean z) {
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 75 hits in 25 files

- `classes5:androidx/core/widget/TextViewKt.java` (21)
- `classes5:androidx/core/widget/TextViewKt$addTextChangedListener$textWatcher$1.java` (7)
- `classes7:com/facebook/react/views/textinput/ReactEditText.java` (7)
- `classes:androidx/appcompat/widget/SearchView.java` (4)
- `classes5:androidx/emoji2/text/SpannableBuilder.java` (3)
- `classes:androidx/appcompat/widget/AppCompatButton.java` (2)
- `classes:androidx/appcompat/widget/AppCompatTextView.java` (2)
- `classes10:com/urbanairship/android/layout/util/ViewExtensionsKt$onEditing$1.java` (2)
- `classes10:com/urbanairship/android/layout/util/ViewExtensionsKt$textChanges$1.java` (2)
- `classes11:com/urbanairship/preferencecenter/widget/ContactChannelDialogInputView.java` (2)
- `classes4:uk/co/bbc/authtoolkit/profiles/view/CreateProfileFragment.java` (2)
- `classes7:com/facebook/react/views/textinput/ReactTextInputTextWatcher.java` (2)

```
classes:androidx/appcompat/widget/AppCompatButton.java:150:    protected void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:androidx/appcompat/widget/AppCompatButton.java:151:        super.onTextChanged(charSequence, i, i2, i3);
classes:androidx/appcompat/widget/AppCompatTextView.java:207:    protected void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:androidx/appcompat/widget/AppCompatTextView.java:208:        super.onTextChanged(charSequence, i, i2, i3);
classes:androidx/appcompat/widget/SearchView.java:232:            public void onTextChanged(CharSequence charSequence, int i2, int i3, int i4) {
classes:androidx/appcompat/widget/SearchView.java:233:                SearchView.this.onTextChanged(charSequence);
classes:androidx/appcompat/widget/SearchView.java:273:        searchAutoComplete.addTextChangedListener(this.mTextWatcher);
classes:androidx/appcompat/widget/SearchView.java:725:    void onTextChanged(CharSequence charSequence) {
classes10:com/urbanairship/android/layout/util/ViewExtensionsKt$onEditing$1.java:90:                public void onTextChanged(CharSequence s, int start, int before, int count) {
classes10:com/urbanairship/android/layout/util/ViewExtensionsKt$onEditing$1.java:105:            this.$this_onEditing.addTextChangedListener((TextWatcher) r1);
classes10:com/urbanairship/android/layout/util/ViewExtensionsKt$textChanges$1.java:62:                public void onTextChanged(CharSequence s, int start, int before, int count) {
classes10:com/urbanairship/android/layout/util/ViewExtensionsKt$textChanges$1.java:72:            this.$this_textChanges.addTextChangedListener((TextWatcher) r7);
```

### webview_tracking — 9 hits in 6 files

- `classes10:com/reactnativecommunity/webview/RNCWebViewManagerImpl.java` (3)
- `classes10:com/reactnativecommunity/webview/RNCWebViewManager.java` (2)
- `classes7:com/facebook/react/viewmanagers/RNCWebViewManagerInterface.java` (1)
- `classes7:com/facebook/react/viewmanagers/RNCWebViewManagerDelegate.java` (1)
- `classes7:com/google/ads/interactivemedia/v3/impl/zzcn.java` (1)
- `classes8:com/google/android/gms/ads/internal/overlay/zzm.java` (1)

```
classes10:com/reactnativecommunity/webview/RNCWebViewManager.java:352:    public void setThirdPartyCookiesEnabled(RNCWebViewWrapper rNCWebViewWrapper, boolean z) {
classes10:com/reactnativecommunity/webview/RNCWebViewManager.java:353:        this.mRNCWebViewManagerImpl.setThirdPartyCookiesEnabled(rNCWebViewWrapper, z);
classes10:com/reactnativecommunity/webview/RNCWebViewManagerImpl.java:48:@Metadata(d1 = {"\u0000\\\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\t\n\u0002\u0018\u0002\n
classes10:com/reactnativecommunity/webview/RNCWebViewManagerImpl.java:855:    public final void setThirdPartyCookiesEnabled(RNCWebViewWrapper viewWrapper, boolean enabled) {
classes10:com/reactnativecommunity/webview/RNCWebViewManagerImpl.java:857:        CookieManager.getInstance().setAcceptThirdPartyCookies(viewWrapper.getWebView(), enabled);
classes7:com/facebook/react/viewmanagers/RNCWebViewManagerInterface.java:176:    void setThirdPartyCookiesEnabled(T t, boolean z);
classes7:com/facebook/react/viewmanagers/RNCWebViewManagerDelegate.java:703:                ((RNCWebViewManagerInterface) this.mViewManager).setThirdPartyCookiesEnabled(t, obj != null ? ((Boolean) obj).booleanValue() : true);
classes7:com/google/ads/interactivemedia/v3/impl/zzcn.java:215:        cookieManager.setAcceptThirdPartyCookies(webView, true);
classes8:com/google/android/gms/ads/internal/overlay/zzm.java:808:            CookieManager.getInstance().setAcceptThirdPartyCookies(this.zzd.zzD(), r2);
```

### streaks — 0 hits in 0 files


```
```

### reengagement — 2280 hits in 427 files

- `classes9:com/google/android/material/internal/CollapsingTextHelper.java` (172)
- `classes9:com/google/android/material/appbar/CollapsingToolbarLayout.java` (62)
- `classes:androidx/compose/material3/AppBarKt.java` (53)
- `classes9:com/google/android/material/bottomsheet/BottomSheetBehavior.java` (44)
- `classes8:com/google/android/gms/internal/ads/zzckt.java` (38)
- `classes9:com/google/android/material/textfield/TextInputLayout.java` (36)
- `classes4:uk/co/bbc/authtoolkitlibrary/R.java` (33)
- `classes4:uk/co/bbc/authtoolkitnativeauthui/R.java` (33)
- `classes9:com/google/android/material/R.java` (32)
- `classes10:com/margelo/nitro/iap/Variant_NullType_WinBackOfferInputIOS.java` (31)
- `classes:androidx/compose/material3/ExitUntilCollapsedScrollBehavior$nestedScrollConnection$1.java` (28)
- `classes9:com/google/android/material/navigationrail/NavigationRailView.java` (27)

```
classes:com/google/firebase/StartupTime.java:7:    public abstract long getElapsedRealtime();
classes:com/google/firebase/StartupTime.java:18:        return create(System.currentTimeMillis(), SystemClock.elapsedRealtime(), SystemClock.uptimeMillis());
classes:com/google/firebase/AutoValue_StartupTime.java:5:    private final long elapsedRealtime;
classes:com/google/firebase/AutoValue_StartupTime.java:11:        this.elapsedRealtime = j2;
classes:com/google/firebase/AutoValue_StartupTime.java:21:    public long getElapsedRealtime() {
classes:com/google/firebase/AutoValue_StartupTime.java:22:        return this.elapsedRealtime;
classes:com/google/firebase/AutoValue_StartupTime.java:31:        return "StartupTime{epochMillis=" + this.epochMillis + ", elapsedRealtime=" + this.elapsedRealtime + ", uptimeMillis=" + this.uptimeMillis + "}";
classes:com/google/firebase/AutoValue_StartupTime.java:40:            if (this.epochMillis == startupTime.getEpochMillis() && this.elapsedRealtime == startupTime.getElapsedRealtime() && this.uptimeMillis == startupTime.getUptimeMillis()) {
classes:com/google/firebase/AutoValue_StartupTime.java:49:        long j2 = this.elapsedRealtime;
classes:android/support/v4/media/session/MediaSessionCompat.java:428:        long jElapsedRealtime = SystemClock.elapsedRealtime();
classes:android/support/v4/media/session/MediaSessionCompat.java:429:        long playbackSpeed = ((long) (playbackStateCompat.getPlaybackSpeed() * (jElapsedRealtime - r0))) + playbackStateCompat.getPosition();
classes:android/support/v4/media/session/MediaSessionCompat.java:433:        return new PlaybackStateCompat.Builder(playbackStateCompat).setState(playbackStateCompat.getState(), (j < 0 || playbackSpeed <= j) ? playbackSpeed < 0 ? 0L : playbackSpeed : j, playbackStateCompat.getPlaybackSpeed(), jElaps
```

### notif_permission_nag — 0 hits in 0 files


```
```

### cancellation_retention — 108 hits in 5 files

- `classes10:com/margelo/nitro/iap/Variant_NullType_WinBackOfferInputIOS.java` (31)
- `classes11:dev/hyo/openiap/RequestSubscriptionIosProps.java` (25)
- `classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java` (22)
- `classes10:com/margelo/nitro/iap/WinBackOfferInputIOS.java` (17)
- `classes11:dev/hyo/openiap/WinBackOfferInputIOS.java` (13)

```
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:12:@Metadata(d1 = {"\u0000P\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:26:    private final Variant_NullType_WinBackOfferInputIOS winBackOffer;
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:29:    public static /* synthetic */ NitroRequestPurchaseIos copy$default(NitroRequestPurchaseIos nitroRequestPurchaseIos, String str, Variant_NullType_Boolean variant_NullType_Boolean, Variant_NullType_String variant_NullType_String, Vari
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:58:            variant_NullType_WinBackOfferInputIOS = nitroRequestPurchaseIos.winBackOffer;
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:61:        Variant_NullType_WinBackOfferInputIOS variant_NullType_WinBackOfferInputIOS2 = variant_NullType_WinBackOfferInputIOS;
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:66:        return nitroRequestPurchaseIos.copy(str, variant_NullType_Boolean, variant_NullType_String, variant_NullType_Double, variant_NullType_Map_String__String_2, variant_NullType_String5, subscriptionBillingPlanTypeIOS2, variant_NullT
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:70:    private static final NitroRequestPurchaseIos fromCpp(String str, Variant_NullType_Boolean variant_NullType_Boolean, Variant_NullType_String variant_NullType_String, Variant_NullType_Double variant_NullType_Double, Variant_NullType_M
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:71:        return INSTANCE.fromCpp(str, variant_NullType_Boolean, variant_NullType_String, variant_NullType_Double, variant_NullType_Map_String__String_, variant_NullType_String2, subscriptionBillingPlanTypeIOS, variant_NullType_String3, v
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:80:    public final Variant_NullType_WinBackOfferInputIOS getWinBackOffer() {
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:81:        return this.winBackOffer;
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:124:    public final NitroRequestPurchaseIos copy(String sku, Variant_NullType_Boolean andDangerouslyFinishTransactionAutomatically, Variant_NullType_String appAccountToken, Variant_NullType_Double quantity, Variant_NullType_Map_String__St
classes10:com/margelo/nitro/iap/NitroRequestPurchaseIos.java:126:        return new NitroRequestPurchaseIos(sku, andDangerouslyFinishTransactionAutomatically, appAccountToken, quantity, withOffer, advancedCommerceData, billingPlanType, compactJWS, promotionalOfferJWS, winBackOffer);
```

### urgency_countdown — 508 hits in 94 files

- `classes4:org/prebid/mobile/rendering/views/interstitial/InterstitialVideo.java` (35)
- `classes4:rx/Completable.java` (21)
- `classes4:uk/co/bbc/authtoolkit/federatedFlow/FederatedAuthTokens.java` (15)
- `classes11:io/piano/android/api/anon/model/OAuthToken.java` (14)
- `classes4:uk/co/bbc/authtoolkit/profiles/network/AdminTokensDto.java` (14)
- `classes4:rx/observables/BlockingObservable.java` (13)
- `classes9:com/google/firebase/installations/local/AutoValue_PersistedInstallationEntry.java` (13)
- `classes6:com/amazonaws/mobileconnectors/s3/transfermanager/TransferManager.java` (12)
- `classes4:uk/co/bbc/authtoolkit/AuthHTTPClient.java` (11)
- `classes9:com/google/common/util/concurrent/ClosingFuture.java` (11)
- `classes12:okhttp3/internal/concurrent/TaskQueue.java` (9)
- `classes4:rx/internal/operators/BlockingOperatorToFuture.java` (9)

```
classes10:com/urbanairship/channel/ChannelAuthApiClient.java:61:        return new AuthToken(str, jsonMapRequireMap.require("token").requireString(), j + jsonMapRequireMap.require("expires_in").getLong(0L));
classes10:com/urbanairship/contacts/ContactApiClient.java:1538:            JsonValue jsonValue15 = jsonMap.get("token_expires_in");
classes10:com/urbanairship/contacts/ContactApiClient.java:1540:                throw new JsonException("Missing required field: 'token_expires_in'");
classes10:com/urbanairship/contacts/ContactApiClient.java:1583:                    throw new JsonException("Invalid type 'Long' for field 'token_expires_in'");
classes11:io/reactivex/internal/subscribers/BlockingLastSubscriber.java:12:        countDown();
classes11:io/reactivex/observers/TestObserver.java:151:            this.done.countDown();
classes11:io/reactivex/observers/TestObserver.java:168:            this.done.countDown();
classes11:io/reactivex/observers/BaseTestConsumer.java:18:import java.util.concurrent.CountDownLatch;
classes11:io/reactivex/observers/BaseTestConsumer.java:32:    protected final CountDownLatch done = new CountDownLatch(1);
classes11:io/reactivex/internal/util/BlockingIgnoringReceiver.java:5:import java.util.concurrent.CountDownLatch;
classes11:io/reactivex/internal/util/BlockingIgnoringReceiver.java:8:public final class BlockingIgnoringReceiver extends CountDownLatch implements Consumer<Throwable>, Action {
classes11:io/reactivex/internal/util/BlockingIgnoringReceiver.java:18:        countDown();
```

### infinite_autoplay — 222 hits in 52 files

- `classes7:com/google/ads/interactivemedia/v3/impl/data/AutoValue_GsonAdsRequest.java` (15)
- `classes7:com/google/ads/interactivemedia/v3/impl/data/AutoValue_ImaSdkSettingsData.java` (13)
- `classes10:com/urbanairship/android/layout/view/MediaView.java` (10)
- `classes6:com/airbnb/lottie/LottieAnimationView.java` (10)
- `classes10:com/mobile/video/VideoView.java` (9)
- `classes11:expo/modules/image/ExpoImageViewWrapper.java` (9)
- `classes7:com/facebook/drawee/controller/AbstractDraweeControllerBuilder.java` (9)
- `classes12:org/prebid/mobile/api/rendering/VideoView.java` (8)
- `classes4:uk/co/bbc/smpan/media/PlayRequest.java` (8)
- `classes7:com/github/penfeizhou/animation/FrameAnimationDrawable.java` (8)
- `classes10:com/urbanairship/android/layout/property/Video.java` (7)
- `classes4:uk/co/bbc/smpan/PlayerController.java` (7)

```
classes10:com/iab/omid/library/prebidorg/adsession/media/VastProperties.java:39:            jSONObject.put("autoPlay", this.c);
classes10:com/iab/omid/library/prebidorg/adsession/media/VastProperties.java:56:    public boolean isAutoPlay() {
classes10:com/mobile/video/VideoView.java:73:@Metadata(d1 = {"\u0000à\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\
classes10:com/mobile/video/VideoView.java:86:    private boolean autoPlay;
classes10:com/mobile/video/VideoView.java:117:    private boolean shouldAutoPlayAfterLoad;
classes10:com/mobile/video/VideoView.java:373:            if (!videoView.shouldAutoPlayAfterLoad) {
classes10:com/mobile/video/VideoView.java:399:            videoView.shouldAutoPlayAfterLoad = false;
classes10:com/mobile/video/VideoView.java:728:        this.shouldAutoPlayAfterLoad = z;
classes10:com/mobile/video/VideoView.java:799:            playRequestBuilderForVpid.withAutoplay(true);
classes10:com/mobile/video/VideoView.java:1203:        Log.d(str, "onHostResume: " + str2 + " isLoading: " + z + " adsCompleted: " + z + " autoPlay: " + this.autoPlay);
classes10:com/mobile/video/VideoView.java:1205:        boolean z2 = this.autoPlay || Intrinsics.areEqual(this.configuration, "vertical");
classes10:com/mobile/audio/AudioManagerModule.java:515:            PlayRequest playRequestBuild = new AODUnmediatedMP3PlayRequestBuilder(this.reactContext, str, str2, (DefaultConstructorMarker) null).forUri(stringOrDefault$default2, aVStatisticsProviderCreate).withAutoplay(this.pendingPlay).with(Med
```

### badges — 38 hits in 13 files

- `classes5:androidx/datastore/preferences/protobuf/DescriptorProtos.java` (9)
- `classes5:androidx/core/app/NotificationCompatBuilder.java` (4)
- `classes5:androidx/core/app/NotificationCompat.java` (3)
- `classes5:androidx/datastore/preferences/protobuf/EnumValue.java` (3)
- `classes5:androidx/datastore/preferences/protobuf/Field.java` (3)
- `classes9:com/google/crypto/tink/shaded/protobuf/EnumValue.java` (3)
- `classes9:com/google/crypto/tink/shaded/protobuf/Field.java` (3)
- `classes6:androidx/media3/ui/PlayerNotificationManager.java` (2)
- `classes8:com/google/android/exoplayer2/ui/PlayerNotificationManager.java` (2)
- `classes9:com/google/android/material/badge/BadgeState.java` (2)
- `classes9:com/google/android/material/badge/BadgeDrawable.java` (2)
- `classes10:com/swmansion/rnscreens/gamma/tabs/appearance/TabsAppearanceApplicator.java` (1)

```
classes10:com/swmansion/rnscreens/gamma/tabs/appearance/TabsAppearanceApplicator.java:201:            orCreateBadge.setNumber(intOrNull.intValue());
classes5:androidx/core/app/NotificationCompatBuilder.java:41:        this.mBuilder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, builder.mTickerView).setVibrate(notification.vibrate).setLight
classes5:androidx/core/app/NotificationCompatBuilder.java:111:            Api26Impl.setBadgeIconType(this.mBuilder, builder.mBadgeIcon);
classes5:androidx/core/app/NotificationCompatBuilder.java:318:        static Notification.Builder setBadgeIconType(Notification.Builder builder, int i) {
classes5:androidx/core/app/NotificationCompatBuilder.java:319:            return builder.setBadgeIconType(i);
classes5:androidx/core/app/NotificationCompat.java:265:            setContentTitle(NotificationCompat.getContentTitle(notification)).setContentText(NotificationCompat.getContentText(notification)).setContentInfo(NotificationCompat.getContentInfo(notification)).setSubText(NotificationCompat.getSubTex
classes5:androidx/core/app/NotificationCompat.java:447:        public Builder setNumber(int i) {
classes5:androidx/core/app/NotificationCompat.java:817:        public Builder setBadgeIconType(int i) {
classes5:androidx/datastore/preferences/protobuf/EnumValue.java:59:    public void setNumber(int value) {
classes5:androidx/datastore/preferences/protobuf/EnumValue.java:235:        public Builder setNumber(int value) {
classes5:androidx/datastore/preferences/protobuf/EnumValue.java:237:            ((EnumValue) this.instance).setNumber(value);
classes5:androidx/datastore/preferences/protobuf/Field.java:303:    public void setNumber(int value) {
```

### minors_age — 125 hits in 33 files

- `classes4:uk/co/bbc/authtoolkit/idctaConfig/IdctaFederatedEndpoints.java` (15)
- `classes4:uk/co/bbc/iDAuth/V5AuthConfig.java` (13)
- `classes4:uk/co/bbc/authtoolkitnativeauthui/NativeSignInDependencies.java` (13)
- `classes8:com/google/android/gms/common/PackageSignatureVerifier.java` (12)
- `classes8:com/google/android/gms/common/PackageVerificationResult.java` (7)
- `classes4:uk/co/bbc/authtoolkit/idctaConfig/AndroidIdctaConfigStore.java` (6)
- `classes10:com/mobile/auth/BBCAuthConfig.java` (5)
- `classes4:uk/co/bbc/authtoolkitnativeauthui/NativeSignInViewModel.java` (5)
- `classes8:com/google/android/gms/ads/RequestConfiguration.java` (5)
- `classes8:com/google/android/gms/common/zzac.java` (4)
- `classes11:io/invertase/googlemobileads/ReactNativeGoogleMobileAdsModule.java` (3)
- `classes4:uk/co/bbc/authtoolkit/federatedFlow/FederatedURLBuilder.java` (3)

```
classes10:com/mobile/auth/BBCAuthConfig.java:9:@Metadata(d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0002\b\f\u0018\u00002\u00020\u0001B?\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u0012\u0006\u0010\u0004\u001a\u00020
classes10:com/mobile/auth/BBCAuthConfig.java:14:    private final boolean hideUnder13Registration;
classes10:com/mobile/auth/BBCAuthConfig.java:32:        this.hideUnder13Registration = z2;
classes10:com/mobile/auth/BBCAuthConfig.java:60:    public boolean getHideUnder13Registration() {
classes10:com/mobile/auth/BBCAuthConfig.java:61:        return this.hideUnder13Registration;
classes11:io/invertase/googlemobileads/ReactNativeGoogleMobileAdsConsentModule.java:104:            if (readableMap.hasKey("tagForUnderAgeOfConsent")) {
classes11:io/invertase/googlemobileads/ReactNativeGoogleMobileAdsConsentModule.java:105:                builder.setTagForUnderAgeOfConsent(readableMap.getBoolean("tagForUnderAgeOfConsent"));
classes11:io/invertase/googlemobileads/ReactNativeGoogleMobileAdsModule.java:87:        if (requestConfiguration.hasKey("tagForUnderAgeOfConsent")) {
classes11:io/invertase/googlemobileads/ReactNativeGoogleMobileAdsModule.java:88:            builder.setTagForUnderAgeOfConsent(requestConfiguration.getBoolean("tagForUnderAgeOfConsent") ? 1 : 0);
classes11:io/invertase/googlemobileads/ReactNativeGoogleMobileAdsModule.java:90:            builder.setTagForUnderAgeOfConsent(-1);
classes4:uk/co/bbc/iDAuth/V5AuthConfig.java:9:@Metadata(d1 = {"\u0000(\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0002\b\u0015\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\b\u0087\b\u0018\u00002\u00020\u0001BC\u0012\u0006
classes4:uk/co/bbc/iDAuth/V5AuthConfig.java:15:    private final boolean hideUnder13Registration;
```

### screen_time — 29 hits in 6 files

- `classes10:com/permutive/android/config/api/model/SdkConfiguration.java` (14)
- `classes11:com/urbanairship/messagecenter/MessageAnalytics.java` (7)
- `classes10:com/permutive/android/config/api/model/GeneratedJsonAdapter.java` (4)
- `classes11:dotmetrics/analytics/JsonObjects.java` (2)
- `classes10:com/permutive/android/event/SessionIdProviderImpl.java` (1)
- `classes8:com/google/android/gms/ads/identifier/AdvertisingIdClient.java` (1)

```
classes10:com/permutive/android/event/SessionIdProviderImpl.java:239:        return Long.valueOf(sdkConfiguration.getSessionLengthInSeconds() * 1000);
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:17:@Metadata(d1 = {"\u0000T\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010$\n\u0002\u0010 \n\u0002\b\u0003\n\u0002\u0010\t\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0012\n\u0002\u0010\u
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:49:    private final int sessionLengthInSeconds;
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:107:        int i42 = (i18 & 2048) != 0 ? sdkConfiguration.sessionLengthInSeconds : i6;
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:229:    public final int getSessionLengthInSeconds() {
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:230:        return this.sessionLengthInSeconds;
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:391:    public final SdkConfiguration copy(@Json(name = "organization_id") String organisationId, @Json(name = "disable_os") Map<String, ? extends List<String>> disableOs, @Json(name = "disable_app") Map<String, ? extends List<St
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:403:        return new SdkConfiguration(organisationId, disableOs, disableApp, disableSdk, javaScriptRetrievalInSeconds, syncEventsWaitInSeconds, eventsCacheSizeLimit, errorQuotaLimit, eventsBatchSizeLimit, errorQuotaPeriodInSeco
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:414:        return Intrinsics.areEqual(this.organisationId, sdkConfiguration.organisationId) && Intrinsics.areEqual(this.disableOs, sdkConfiguration.disableOs) && Intrinsics.areEqual(this.disableApp, sdkConfiguration.disableApp) 
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:418:        return (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((this.organisationId.hashCode() * 31) + this.disableOs.hashCode()) * 31) + this.disableApp.hashCode()) * 31) + this.disableSdk.hashCode()) *
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:422:        return "SdkConfiguration(organisationId=" + this.organisationId + ", disableOs=" + this.disableOs + ", disableApp=" + this.disableApp + ", disableSdk=" + this.disableSdk + ", javaScriptRetrievalInSeconds=" + this.java
classes10:com/permutive/android/config/api/model/SdkConfiguration.java:426:    public SdkConfiguration(@Json(name = "organization_id") String str, @Json(name = "disable_os") Map<String, ? extends List<String>> map, @Json(name = "disable_app") Map<String, ? extends List<String>> map2, @Json(name = "d
```

## UI string categories (default locale)

### loss_aversion_copy — 0 strings

```
```

### urgency_copy — 0 strings

```
```

### confirmshaming_copy — 3 strings

```
strings.xml:112:    <string name="authtoolkit_not_now_button">Not Now</string>
strings.xml:525:    <string name="offline_opt_in_decline">No thanks</string>
strings.xml:706:    <string name="ua_rate_app_action_default_rate_negative_button">No Thanks</string>
```

### social_pressure_copy — 2 strings

```
strings.xml:218:    <string name="com.google.firebase.crashlytics.mapping_file_id">00000000000000000000000000000000</string>
strings.xml:315:    <string name="firebase_database_url">https://api-project-1062059617256.firebaseio.com</string>
```

### guilt_copy — 2 strings

```
strings.xml:124:    <string name="authtoolkit_profile_picker_heading">Welcome back...</string>
strings.xml:618:    <string name="ua_emoji_sad">😞</string>
```

### subscription_copy — 4 strings

```
strings.xml:333:    <string name="m3_exceed_max_badge_text_suffix">%1$s%2$s</string>
strings.xml:457:    <string name="mtrl_exceed_max_badge_number_content_description">More than %1$d new notifications</string>
strings.xml:458:    <string name="mtrl_exceed_max_badge_number_suffix">%1$d%2$s</string>
strings.xml:702:    <string name="ua_preference_center_subscription_item_description">%1$s. %2$s. %3$s.</string>
```

### data_copy — 12 strings

```
strings.xml:71:    <string name="authtoolkit_connect_third_party_text">"To connect %1$s to your BBC account, we'll share a unique ID with them, but we will not share personal information."</string>
strings.xml:72:    <string name="authtoolkit_connect_third_party_title">Connect %1$s to your BBC account</string>
strings.xml:76:    <string name="authtoolkit_could_not_connect_third_party">Could not connect to %1$s</string>
strings.xml:168:    <string name="catalyst_change_bundle_location">Change Bundle Location</string>
strings.xml:169:    <string name="catalyst_change_bundle_location_apply">Apply Changes</string>
strings.xml:170:    <string name="catalyst_change_bundle_location_cancel">Cancel</string>
strings.xml:171:    <string name="catalyst_change_bundle_location_input_hint">127.0.0.1:8081</string>
strings.xml:172:    <string name="catalyst_change_bundle_location_input_label">Provide a custom bundler address and port:</string>
strings.xml:173:    <string name="catalyst_change_bundle_location_instructions">"You can connect either via USB (localhost - default) or Wifi. If you connect via USB and running with a physical device, make sure you:
strings.xml:175: 2. Set the bundle location to `localhost:8081`
strings.xml:523:    <string name="offline_notification_title_with_advertiser">You are back online! Continue learning about %s</string>
strings.xml:526:    <string name="offline_opt_in_message">"We'll send you a notification with a link to the advertiser site."</string>
```

