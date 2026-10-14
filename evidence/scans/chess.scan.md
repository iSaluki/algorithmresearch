# Pattern scan: work/chess/jdex

## Code categories (library packages excluded)

### installed_apps — 42 hits in 33 files

- `classes2:com/inmobi/media/AbstractC0483o5.java` (4)
- `classes10:com/google/android/gms/common/GooglePlayServicesUtilLight.java` (3)
- `classes10:com/facebook/internal/Utility.java` (2)
- `classes11:com/google/android/gms/internal/ads/zzinp.java` (2)
- `classes7:com/chess/net/model/MembershipActivity.java` (2)
- `classes9:android/content/pm/PackageManager.java` (2)
- `classes:androidx/credentials/playservices/controllers/BeginSignIn/BeginSignInControllerUtility.java` (1)
- `classes:androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java` (1)
- `classes:android/view/inputmethod/eob.java` (1)
- `classes:android/view/inputmethod/xn9.java` (1)
- `classes10:com/facebook/internal/Validate.java` (1)
- `classes10:com/facebook/login/NativeAppLoginMethodHandler.java` (1)

```
classes:androidx/credentials/playservices/controllers/BeginSignIn/BeginSignInControllerUtility.java:44:            return r3.getPackageInfo("com.google.android.gms", 0).versionCode;
classes:androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:133:            PackageInfo packageInfo = packageManager.getPackageInfo("com.google.android.gms", 0);
classes:android/view/inputmethod/eob.java:100:            Iterator<ResolveInfo> it = packageManager.queryIntentActivities(intent, 128).iterator();
classes:android/view/inputmethod/xn9.java:64:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(a.c(), 0);
classes10:com/facebook/internal/Validate.java:114:            listQueryIntentActivities = packageManager.queryIntentActivities(intent, 64);
classes10:com/facebook/internal/Utility.java:681:            List<ResolveInfo> listQueryIntentActivities = packageManager.queryIntentActivities(intent, NativeProtocol.MESSAGE_GET_ACCESS_TOKEN_REQUEST);
classes10:com/facebook/internal/Utility.java:682:            Intrinsics.checkNotNullExpressionValue(listQueryIntentActivities, "packageManager.queryIntentActivities(intent, PackageManager.MATCH_DEFAULT_ONLY)");
classes10:com/facebook/login/NativeAppLoginMethodHandler.java:47:        Intrinsics.checkNotNullExpressionValue(FacebookSdk.getApplicationContext().getPackageManager().queryIntentActivities(intent, NativeProtocol.MESSAGE_GET_ACCESS_TOKEN_REQUEST), "FacebookSdk.getApplicationContext()\n            .p
classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:220:                    context.getPackageManager().getPackageInfo("com.android.vending", 0);
classes10:com/google/android/gms/common/GooglePlayServicesUtilLight.java:82:            return context.getPackageManager().getPackageInfo("com.google.android.gms", 0).versionCode;
classes10:com/google/android/gms/common/GooglePlayServicesUtilLight.java:239:                packageInfo = packageManager.getPackageInfo("com.android.vending", 134225984);
classes10:com/google/android/gms/common/GooglePlayServicesUtilLight.java:247:            PackageInfo packageInfo2 = packageManager.getPackageInfo("com.google.android.gms", 134217792);
```

### usage_stats — 0 hits in 0 files


```
```

### clipboard — 3 hits in 3 files

- `classes:androidx/appcompat/widget/t.java` (1)
- `classes:android/view/inputmethod/aj.java` (1)
- `classes10:com/facebook/react/modules/clipboard/ClipboardModule.java` (1)

```
classes:androidx/appcompat/widget/t.java:66:        ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
classes:android/view/inputmethod/aj.java:43:        ClipData primaryClip = c().getPrimaryClip();
classes10:com/facebook/react/modules/clipboard/ClipboardModule.java:35:            ClipData primaryClip = getClipboardService().getPrimaryClip();
```

### contacts — 30 hits in 12 files

- `classes2:androidx/fragment/app/ry1.java` (5)
- `classes2:com/squareup/picasso/ContactsPhotoRequestHandler.java` (4)
- `classes5:com/google/android/y9c.java` (3)
- `classes10:com/facebook/imagepipeline/producers/LocalContentUriFetchProducer.java` (2)
- `classes2:androidx/fragment/app/ob.java` (2)
- `classes2:androidx/fragment/app/y89.java` (2)
- `classes2:androidx/fragment/app/gea.java` (2)
- `classes2:androidx/fragment/app/xi5.java` (2)
- `classes2:androidx/fragment/app/c1c.java` (2)
- `classes2:androidx/fragment/app/po3.java` (2)
- `classes6:com/google/android/connect/invite/contacts/repository/ContactsRepositoryImpl$getContactNameByLookupKey$2.java` (2)
- `classes7:com/facebook/common/util/UriUtil.java` (2)

```
classes10:com/facebook/imagepipeline/producers/LocalContentUriFetchProducer.java:7:import android.provider.ContactsContract;
classes10:com/facebook/imagepipeline/producers/LocalContentUriFetchProducer.java:88:                InputStream inputStreamOpenContactPhotoInputStream = ContactsContract.Contacts.openContactPhotoInputStream(this.contentResolver, sourceUri);
classes2:com/squareup/picasso/ContactsPhotoRequestHandler.java:7:import android.provider.ContactsContract;
classes2:com/squareup/picasso/ContactsPhotoRequestHandler.java:51:        uriLookupContact = ContactsContract.Contacts.lookupContact(contentResolver, uriLookupContact);
classes2:com/squareup/picasso/ContactsPhotoRequestHandler.java:55:        return ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uriLookupContact, true);
classes2:com/squareup/picasso/ContactsPhotoRequestHandler.java:61:        return "content".equals(uri.getScheme()) && ContactsContract.Contacts.CONTENT_URI.getHost().equals(uri.getHost()) && matcher.match(request.uri) != -1;
classes2:androidx/fragment/app/ob.java:4:import android.provider.ContactsContract;
classes2:androidx/fragment/app/ob.java:24:        return context.getString(ContactsContract.CommonDataKinds.StructuredPostal.getTypeLabelResource(i));
classes2:androidx/fragment/app/y89.java:4:import android.provider.ContactsContract;
classes2:androidx/fragment/app/y89.java:26:        return context.getString(ContactsContract.CommonDataKinds.Phone.getTypeLabelResource(i));
classes2:androidx/fragment/app/gea.java:4:import android.provider.ContactsContract;
classes2:androidx/fragment/app/gea.java:24:        return context.getString(ContactsContract.CommonDataKinds.Relation.getTypeLabelResource(i));
```

### call_log — 0 hits in 0 files


```
```

### sms — 21 hits in 10 files

- `classes9:com/chess/utils/android/phonenumbers/SmsCodeAutofillImpl$codes$1.java` (4)
- `classes10:com/google/android/gms/auth/api/phone/SmsRetriever.java` (3)
- `classes10:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java` (3)
- `classes11:com/google/android/gms/internal/p001authapiphone/zzah.java` (3)
- `classes10:com/google/android/gms/auth/api/phone/SmsRetrieverStatusCodes.java` (2)
- `classes11:com/google/android/gms/internal/p001authapiphone/zzam.java` (2)
- `classes10:com/google/android/gms/auth/api/phone/SmsRetrieverApi.java` (1)
- `classes11:com/google/android/gms/internal/p001authapiphone/zzl.java` (1)
- `classes11:com/google/android/gms/internal/p001authapiphone/zzk.java` (1)
- `classes9:com/chess/utils/android/misc/g0.java` (1)

```
classes10:com/google/android/gms/auth/api/phone/SmsRetrieverApi.java:4:public interface SmsRetrieverApi {
classes10:com/google/android/gms/auth/api/phone/SmsRetriever.java:7:public final class SmsRetriever {
classes10:com/google/android/gms/auth/api/phone/SmsRetriever.java:8:    private SmsRetriever() {
classes10:com/google/android/gms/auth/api/phone/SmsRetriever.java:11:    public static SmsRetrieverClient a(Context context) {
classes10:com/google/android/gms/auth/api/phone/SmsRetrieverStatusCodes.java:6:public final class SmsRetrieverStatusCodes extends CommonStatusCodes {
classes10:com/google/android/gms/auth/api/phone/SmsRetrieverStatusCodes.java:7:    private SmsRetrieverStatusCodes() {
classes10:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java:9:public abstract class SmsRetrieverClient extends GoogleApi<Api.ApiOptions.NoOptions> implements SmsRetrieverApi {
classes10:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java:13:    public SmsRetrieverClient(Context context) {
classes10:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java:14:        super(context, (Api<Api.ApiOptions.NoOptions>) new Api("SmsRetriever.API", m, l), Api.ApiOptions.j2, GoogleApi.Settings.c);
classes11:com/google/android/gms/internal/p001authapiphone/zzl.java:10:        super("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverResultCallback");
classes11:com/google/android/gms/internal/p001authapiphone/zzam.java:5:import com.google.android.gms.auth.api.phone.SmsRetrieverClient;
classes11:com/google/android/gms/internal/p001authapiphone/zzam.java:13:public final class zzam extends SmsRetrieverClient {
```

### location — 14 hits in 6 files

- `classes2:com/inmobi/media/C0774zb.java` (6)
- `classes11:com/google/android/gms/location/FusedLocationProviderClient.java` (2)
- `classes11:com/google/android/gms/location/LocationServices.java` (2)
- `classes3:org/prebid/mobile/rendering/sdk/deviceData/managers/LastKnownLocationInfoManager.java` (2)
- `classes:androidx/appcompat/app/k.java` (1)
- `classes5:com/amazon/device/ads/DtbGeoLocation.java` (1)

```
classes:androidx/appcompat/app/k.java:46:                return this.b.getLastKnownLocation(str);
classes11:com/google/android/gms/location/FusedLocationProviderClient.java:9:public class FusedLocationProviderClient extends GoogleApi<Api.ApiOptions.NoOptions> {
classes11:com/google/android/gms/location/FusedLocationProviderClient.java:10:    public FusedLocationProviderClient(Context context) {
classes11:com/google/android/gms/location/LocationServices.java:37:    public static FusedLocationProviderClient a(Context context) {
classes11:com/google/android/gms/location/LocationServices.java:38:        return new FusedLocationProviderClient(context);
classes2:com/inmobi/media/C0774zb.java:13:import com.google.android.gms.location.FusedLocationProviderClient;
classes2:com/inmobi/media/C0774zb.java:55:            FusedLocationProviderClient fusedLocationProviderClientA = LocationServices.a(context);
classes2:com/inmobi/media/C0774zb.java:56:            Intrinsics.checkNotNullExpressionValue(fusedLocationProviderClientA, "getFusedLocationProviderClient(...)");
classes2:com/inmobi/media/C0774zb.java:89:            oda.b(FusedLocationProviderClient.class).t();
classes2:com/inmobi/media/C0774zb.java:338:                lastKnownLocation = locationManager2.getLastKnownLocation(bestProvider);
classes2:com/inmobi/media/C0774zb.java:361:                                    lastKnownLocation2 = locationManager.getLastKnownLocation(str);
classes3:org/prebid/mobile/rendering/sdk/deviceData/managers/LastKnownLocationInfoManager.java:117:                    lastKnownLocation = locationManager.getLastKnownLocation("gps");
```

### wifi_bt_scan — 1 hits in 1 files

- `classes6:com/google/android/connectedboards/settings/ConnectedBoardsSettingsViewModel.java` (1)

```
classes6:com/google/android/connectedboards/settings/ConnectedBoardsSettingsViewModel.java:542:            connectedBoardsScanningState = bluetoothAdapterC.startDiscovery() ? ConnectedBoardsScanningState.d : ConnectedBoardsScanningState.a;
```

### device_ids — 42 hits in 32 files

- `classes:androidx/core/widget/NestedScrollView.java` (3)
- `classes:android/view/inputmethod/da3.java` (3)
- `classes11:com/google/android/gms/measurement/internal/l.java` (3)
- `classes:androidx/compose/ui/platform/AndroidComposeView.java` (2)
- `classes10:com/facebook/internal/AttributionIdentifiers.java` (2)
- `classes5:com/appsflyer/internal/AFg1nSDK.java` (2)
- `classes5:com/appsflyer/internal/AFb1hSDK.java` (2)
- `classes:androidx/appcompat/app/l.java` (1)
- `classes:androidx/appcompat/app/e.java` (1)
- `classes:androidx/appcompat/app/i.java` (1)
- `classes10:com/google/android/gms/ads/internal/util/client/zzf.java` (1)
- `classes10:com/facebook/react/devsupport/DevServerHelper.java` (1)

```
classes:androidx/core/widget/NestedScrollView.java:1529:            getScrollFeedbackProvider().c(motionEvent.getDeviceId(), motionEvent.getSource(), i2, scrollY2);
classes:androidx/core/widget/NestedScrollView.java:1541:                    getScrollFeedbackProvider().b(motionEvent.getDeviceId(), motionEvent.getSource(), i2, true);
classes:androidx/core/widget/NestedScrollView.java:1550:                getScrollFeedbackProvider().b(motionEvent.getDeviceId(), motionEvent.getSource(), i2, false);
classes:androidx/appcompat/app/l.java:590:        menuE.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
classes:androidx/appcompat/app/e.java:1127:            boolean z2 = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;
classes:androidx/appcompat/app/i.java:205:        menuX.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
classes:androidx/compose/ui/platform/AndroidComposeView.java:1440:        return getFocusOwner().u(new RotaryScrollEvent(t7e.h(viewConfiguration, getContext()) * f2, f2 * t7e.e(viewConfiguration, getContext()), event.getEventTime(), event.getDeviceId()), new Function0<Boolean>() { // from class: and
classes:androidx/compose/ui/platform/AndroidComposeView.java:1837:        MotionEvent motionEventObtain = MotionEvent.obtain(motionEvent.getDownTime() == motionEvent.getEventTime() ? eventTime : motionEvent.getDownTime(), eventTime, action, pointerCount, pointerPropertiesArr, pointerCoordsArr, motio
classes:android/view/inputmethod/da3.java:46:        iArr[0] = t7e.g(context, viewConfiguration, motionEvent.getDeviceId(), i, motionEvent.getSource());
classes:android/view/inputmethod/da3.java:47:        iArr[1] = t7e.f(context, viewConfiguration, motionEvent.getDeviceId(), i, motionEvent.getSource());
classes:android/view/inputmethod/da3.java:52:        int deviceId = motionEvent.getDeviceId();
classes10:com/facebook/internal/AttributionIdentifiers.java:93:                Utility.logd("android_id", e);
```

### gsf_id — 4 hits in 2 files

- `classes11:com/google/android/gms/internal/measurement/zzjg.java` (2)
- `classes11:com/google/android/gms/internal/auth/zzcb.java` (2)

```
classes11:com/google/android/gms/internal/measurement/zzjg.java:8:    public static final Uri a = Uri.parse("content://com.google.android.gsf.gservices");
classes11:com/google/android/gms/internal/measurement/zzjg.java:9:    public static final Uri b = Uri.parse("content://com.google.android.gsf.gservices/prefix");
classes11:com/google/android/gms/internal/auth/zzcb.java:10:    public static final Uri a = Uri.parse("content://com.google.android.gsf.gservices");
classes11:com/google/android/gms/internal/auth/zzcb.java:11:    public static final Uri b = Uri.parse("content://com.google.android.gsf.gservices/prefix");
```

### advertising_id — 300 hits in 52 files

- `classes4:androidx/privacysandbox/ads/adservices/measurement/MeasurementManagerImplCommon.java` (29)
- `classes4:androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures.java` (24)
- `classes4:androidx/privacysandbox/ads/adservices/java/topics/TopicsManagerFutures.java` (16)
- `classes4:androidx/privacysandbox/ads/adservices/topics/TopicsManagerImplCommon.java` (14)
- `classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java` (13)
- `classes4:androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$registerSourceAsync$2.java` (8)
- `classes4:androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$registerTriggerAsync$1.java` (8)
- `classes4:androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$registerWebSourceAsync$1.java` (8)
- `classes4:androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$registerWebTriggerAsync$1.java` (8)
- `classes4:androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$deleteRegistrationsAsync$1.java` (8)
- `classes4:androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$registerSourceAsync$1.java` (8)
- `classes4:androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$getMeasurementApiStatusAsync$1.java` (8)

```
classes10:com/facebook/internal/AttributionIdentifiers.java:75:                if (!isGooglePlayServicesAvailable(context) || (methodQuietly = Utility.getMethodQuietly("com.google.android.gms.ads.identifier.AdvertisingIdClient", "getAdvertisingIdInfo", (Class<?>[]) new Class[]{Context.class})) == nu
classes10:com/google/android/gms/ads/internal/util/zzc.java:4:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
classes10:com/google/android/gms/ads/internal/util/zzc.java:21:            isAdIdFakeForDebugLogging = AdvertisingIdClient.getIsAdIdFakeForDebugLogging(this.zza);
classes10:com/google/android/gms/ads/identifier/zza.java:10:    zza(AdvertisingIdClient advertisingIdClient, Map map) {
classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:21:public class AdvertisingIdClient {
classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:60:    public AdvertisingIdClient(Context context) {
classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:64:    public static Info getAdvertisingIdInfo(Context context) throws GooglePlayServicesRepairableException, IllegalStateException, GooglePlayServicesNotAvailableException, IOException {
classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:65:        AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, true, false);
classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:78:        AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, false, false);
classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:88:                                throw new IOException("AdvertisingIdClient is not connected.");
classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:94:                                throw new IOException("AdvertisingIdClient cannot reconnect.");
classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:97:                            throw new IOException("AdvertisingIdClient cannot reconnect.", e);
```

### install_referrer — 6744 hits in 2284 files

- `classes5:chesscom/puzzles/v1/PuzzlePathAward.java` (27)
- `classes5:com/android/installreferrer/api/InstallReferrerClientImpl.java` (24)
- `classes6:com/google/android/attribution/InstallReferrerProviderImpl.java` (23)
- `classes5:com/chess/entities/j0.java` (22)
- `classes5:chesscom/path/v1/PathAward.java` (22)
- `classes6:com/google/android/attribution/InstallReferrerProviderImpl$getInstallReferrer$2$2$1.java` (16)
- `classes7:com/chess/features/installreferrer/GooglePlayInstallReferrerHandler.java` (15)
- `classes5:com/chess/achievements/Award.java` (14)
- `classes5:com/chess/entities/AdvStatsViewModel.java` (14)
- `classes5:chesscom/settings/v1/SettingMetadata.java` (14)
- `classes5:com/chess/entities/k0.java` (13)
- `classes5:chesscom/settings/v1/SettingValue.java` (13)

```
classes10:com/facebook/internal/InstallReferrerUtil.java:4:import com.android.installreferrer.api.InstallReferrerClient;
classes10:com/facebook/internal/InstallReferrerUtil.java:32:        final InstallReferrerClient installReferrerClientBuild = InstallReferrerClient.newBuilder(FacebookSdk.getApplicationContext()).build();
classes10:com/facebook/internal/InstallReferrerUtil.java:45:                                ReferrerDetails installReferrer = installReferrerClientBuild.getInstallReferrer();
classes10:com/facebook/internal/InstallReferrerUtil.java:47:                                String installReferrer2 = installReferrer.getInstallReferrer();
classes11:com/google/android/gms/internal/ads/zzasg.java:42:            zzasj.zza("InstallReferrerClient", "Service connection is valid. No need to re-initialize.");
classes11:com/google/android/gms/internal/ads/zzasg.java:48:            zzasj.zzb("InstallReferrerClient", "Client is already in the process of connecting to the service.");
classes11:com/google/android/gms/internal/ads/zzasg.java:53:            zzasj.zzb("InstallReferrerClient", "Client was already closed and can't be reused. Please create another instance.");
classes11:com/google/android/gms/internal/ads/zzasg.java:57:        zzasj.zza("InstallReferrerClient", "Starting install referrer service setup.");
classes11:com/google/android/gms/internal/ads/zzasg.java:64:            zzasj.zza("InstallReferrerClient", "Install Referrer service unavailable on device.");
classes11:com/google/android/gms/internal/ads/zzasg.java:78:                            zzasj.zza("InstallReferrerClient", "Service was bonded successfully.");
classes11:com/google/android/gms/internal/ads/zzasg.java:81:                        zzasj.zzb("InstallReferrerClient", "Connection to service is blocked.");
classes11:com/google/android/gms/internal/ads/zzasg.java:86:                        zzasj.zzb("InstallReferrerClient", "No permission to connect to service.");
```

### sensors — 5 hits in 1 files

- `classes4:chesscom/explanation_engine/v1/AnalysisType.java` (5)

```
classes4:chesscom/explanation_engine/v1/AnalysisType.java:18:@kotlin.Metadata(d1 = {"\u0000\u0017\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0010\n\u0000\n\u0002\u0010\b\n\u0003\b\u00ad\u0002\b\u0086\u0081\u0002\u0018\u0000 °\u00022\u00020\u00012\b\u0012\u0004\u0012\u00020\u00000\u0002:\
classes4:chesscom/explanation_engine/v1/AnalysisType.java:230:    public static final AnalysisType ANALYSIS_TYPE_PRESSURES_PINNED_PIECE;
classes4:chesscom/explanation_engine/v1/AnalysisType.java:836:                    return AnalysisType.ANALYSIS_TYPE_PRESSURES_PINNED_PIECE;
classes4:chesscom/explanation_engine/v1/AnalysisType.java:947:        return new AnalysisType[]{ANALYSIS_TYPE_UNSPECIFIED, ANALYSIS_TYPE_STALEMATE, ANALYSIS_TYPE_FIFTY_MOVE, ANALYSIS_TYPE_REPETITION, ANALYSIS_TYPE_INSUFFICIENT, ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE, ANALYSIS_TYPE_DIRECT_SACRIFICE_E
classes4:chesscom/explanation_engine/v1/AnalysisType.java:1195:        ANALYSIS_TYPE_PRESSURES_PINNED_PIECE = new AnalysisType("ANALYSIS_TYPE_PRESSURES_PINNED_PIECE", 243, 248);
```

### accounts — 0 hits in 0 files


```
```

### battery_state — 1 hits in 1 files

- `classes11:com/google/android/gms/internal/ads/zzewx.java` (1)

```
classes11:com/google/android/gms/internal/ads/zzewx.java:55:            zIsCharging = batteryManager != null ? batteryManager.isCharging() : zze(zzd());
```

### screen_capture_detect — 16 hits in 7 files

- `classes10:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java` (5)
- `classes9:com/chess/utils/android/basefragment/g0.java` (5)
- `classes9:com/chess/utils/android/basefragment/d0.java` (2)
- `classes:android/app/Activity$ScreenCaptureCallback.java` (1)
- `classes10:com/google/ads/mediation/inmobi/InMobiNetworkValues.java` (1)
- `classes5:com/chess/MainApplication.java` (1)
- `classes6:com/google/android/FeatureFlag.java` (1)

```
classes:android/app/Activity$ScreenCaptureCallback.java:4:public /* synthetic */ interface Activity$ScreenCaptureCallback {
classes10:com/google/ads/mediation/inmobi/InMobiNetworkValues.java:44:    public static final String SCREENSHOTS = "screenshots";
classes10:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:42:    private static final int SCREENSHOT_OUTPUT_SIZE_HINT = 65536;
classes10:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:43:    private static final int SCREENSHOT_QUALITY = 80;
classes10:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:44:    private static final float SCREENSHOT_SCALE_FACTOR = 1.0f;
classes10:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:353:            bitmapCreateScaledBitmap = Bitmap.createScaledBitmap(bitmap, (int) ((width / f) * SCREENSHOT_SCALE_FACTOR), (int) ((height / f) * SCREENSHOT_SCALE_FACTOR), true);
classes10:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:358:                    bitmapCreateScaledBitmap.compress(compressFormat, SCREENSHOT_QUALITY, byteArrayOutputStream);
classes5:com/chess/MainApplication.java:86:@Metadata(d1 = {"\u0000¤\u0003\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\b\u000e\n\u0002\u0018\u0002\n\
classes6:com/google/android/FeatureFlag.java:345:        P = new FeatureFlag("USER_SELECTIVE_ACTIVITY_SCREENSHOT", 39, false, "screenshot_selective_activity", C0591g.a ? bool : null);
classes9:com/chess/utils/android/basefragment/d0.java:7:    public static /* bridge */ /* synthetic */ Activity.ScreenCaptureCallback a(Object obj) {
classes9:com/chess/utils/android/basefragment/d0.java:8:        return (Activity.ScreenCaptureCallback) obj;
classes9:com/chess/utils/android/basefragment/g0.java:15:@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0002\b\u0007\n\u0002\u0018\u0002\n\
```

### audio_capture — 0 hits in 0 files


```
```

### accessibility — 263 hits in 53 files

- `classes10:com/facebook/react/modules/accessibilityinfo/AccessibilityInfoModule.java` (24)
- `classes:android/view/inputmethod/u47.java` (21)
- `classes2:com/onetrust/otpublishers/headless/accessibility/d.java` (16)
- `classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java` (10)
- `classes11:com/google/android/material/textfield/p.java` (9)
- `classes2:com/onetrust/otpublishers/headless/cmp/ui/tv/fragments/ViewOnKeyListenerC0792h.java` (9)
- `classes10:com/facebook/react/views/view/ReactViewGroup.java` (8)
- `classes11:com/google/android/material/behavior/HideBottomViewOnScrollBehavior.java` (8)
- `classes11:com/google/android/material/behavior/HideViewOnScrollBehavior.java` (8)
- `classes2:com/onetrust/otpublishers/headless/cmp/ui/tv/fragments/H.java` (8)
- `classes2:com/onetrust/otpublishers/headless/cmp/ui/tv/fragments/a0.java` (8)
- `classes11:com/google/android/material/textfield/v.java` (7)

```
classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:21:import android.view.accessibility.AccessibilityManager;
classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:121:@Metadata(d1 = {"\u0000\u0098\u0003\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0002\b\u0002\
classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:123:public final class AndroidComposeViewAccessibilityDelegateCompat extends a6 implements View.OnAttachStateChangeListener, AccessibilityManager.AccessibilityStateChangeListener, AccessibilityManager.TouchExplor
classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:185:    private final AccessibilityManager accessibilityManager;
classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:437:        Intrinsics.h(systemService, "null cannot be cast to non-null type android.view.accessibility.AccessibilityManager");
classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:438:        this.accessibilityManager = (AccessibilityManager) systemService;
classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:619:        List<AccessibilityServiceInfo> enabledAccessibilityServiceList = this.accessibilityManager.getEnabledAccessibilityServiceList(-1);
classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:1029:        return this.accessibilityManager.isEnabled() && this.accessibilityManager.isTouchExplorationEnabled();
classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:3274:    @Override // android.view.accessibility.AccessibilityManager.AccessibilityStateChangeListener
classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:3279:    @Override // android.view.accessibility.AccessibilityManager.TouchExplorationStateChangeListener
classes:androidx/compose/ui/platform/ComposeViewContext.java:484:    public final lh getAccessibilityManager() {
classes:androidx/compose/ui/platform/AndroidComposeView.java:212:@Metadata(d1 = {"\u0000¼\u0007\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0
```

### root_emulator — 51 hits in 17 files

- `classes:com/google/android/ExposedDropdownMenuKt.java` (25)
- `classes2:io/intercom/android/sdk/views/compose/ListAttributeCollectorKt.java` (5)
- `classes:com/google/android/i0.java` (4)
- `classes:com/google/android/g0.java` (2)
- `classes5:com/amazon/device/ads/SDKUtilities.java` (2)
- `classes9:com/facebook/appevents/internal/AppEventUtility.java` (2)
- `classes:android/view/inputmethod/c49.java` (1)
- `classes10:com/google/firebase/crashlytics/internal/common/CommonUtils.java` (1)
- `classes10:com/google/android/da0.java` (1)
- `classes10:com/google/android/ea0.java` (1)
- `classes11:com/google/android/material/textfield/p.java` (1)
- `classes11:com/google/android/gms/measurement/internal/ha.java` (1)

```
classes:com/google/android/ExposedDropdownMenuKt.java:20:import com.google.android.ExposedDropdownMenuKt;
classes:com/google/android/ExposedDropdownMenuKt.java:39:@Metadata(d1 = {"\u0000~\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\
classes:com/google/android/ExposedDropdownMenuKt.java:41:public final class ExposedDropdownMenuKt {
classes:com/google/android/ExposedDropdownMenuKt.java:44:    @Metadata(d1 = {"\u0000\u001b\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\r*\u0001\u0000\b\n\u0018\u00002\u00020\u0001J#\u0010\u0007\u001a\u00020\u0002*\u00020\u00022\u0006\u001
classes:com/google/android/ExposedDropdownMenuKt.java:75:            int iG = android.view.inputmethod.nx1.g(kx1Var.getValue(), ExposedDropdownMenuKt.p(q48Var));
classes:com/google/android/ExposedDropdownMenuKt.java:76:            int iF = android.view.inputmethod.nx1.f(kx1Var.getValue(), ExposedDropdownMenuKt.r(q48Var2));
classes:com/google/android/ExposedDropdownMenuKt.java:84:                    return ExposedDropdownMenuKt.a.r(oVarR0, (o.a) obj);
classes:com/google/android/ExposedDropdownMenuKt.java:97:            if (ExposedDropdownMenuKt.E(str, ((f0) o58Var.getValue()).getName())) {
classes:com/google/android/ExposedDropdownMenuKt.java:116:                    return ExposedDropdownMenuKt.a.q(z, q48Var, q48Var2, (j) obj, (dj7) obj2, (kx1) obj3);
classes:com/google/android/ExposedDropdownMenuKt.java:138:                    return ExposedDropdownMenuKt.a.s(str, o58Var);
classes:com/google/android/ExposedDropdownMenuKt.java:146:                bVarA = ExposedDropdownMenuKt.A(companion, z2, new Function0() { // from class: com.google.android.g14
classes:com/google/android/ExposedDropdownMenuKt.java:148:                        return ExposedDropdownMenuKt.a.t(o58Var2, str, function1, z2);
```

### js_bridge — 13 hits in 13 files

- `classes10:com/google/android/gms/ads/nonagon/signalgeneration/zzap.java` (1)
- `classes11:com/google/android/gms/internal/ads/zzcme.java` (1)
- `classes2:io/intercom/android/sdk/blocks/messengercard/MessengerCardWebViewPresenter.java` (1)
- `classes2:io/intercom/android/sdk/sheets/SheetWebViewPresenter.java` (1)
- `classes2:com/reactnativecommunity/webview/c.java` (1)
- `classes2:com/inmobi/media/GestureDetectorOnGestureListenerC0729xi.java` (1)
- `classes3:org/prebid/mobile/rendering/views/webview/WebViewInterstitial.java` (1)
- `classes3:org/prebid/mobile/rendering/views/webview/WebViewBanner.java` (1)
- `classes5:com/amazon/aps/ads/util/adview/ApsAdViewImpl.java` (1)
- `classes6:com/google/android/ui/SDUIDialogViewModel.java` (1)
- `classes9:com/confiant/android/sdk/Confiant.java` (1)
- `classes9:com/google/android/WebViewModel.java` (1)

```
classes10:com/google/android/gms/ads/nonagon/signalgeneration/zzap.java:609:            webView.addJavascriptInterface(new TaggingLibraryJsInterface(webView, this.zzh, this.zzp, this.zzq, this.zzi, this.zzJ, zzaVar, zzeVar), "gmaSdk");
classes11:com/google/android/gms/internal/ads/zzcme.java:150:        addJavascriptInterface(new zzcmm(this, new zzcml() { // from class: com.google.android.gms.internal.ads.zzcmk
classes2:io/intercom/android/sdk/blocks/messengercard/MessengerCardWebViewPresenter.java:66:        this.webView.addJavascriptInterface(new MessengerCardWebViewInterface(this.webView, this.loadingView, this.gson, this.primaryColor, this.metricTracker, this.conversationId, this.isHomeScreen, this.con
classes2:io/intercom/android/sdk/sheets/SheetWebViewPresenter.java:43:        this.webView.addJavascriptInterface(new SheetWebViewInterface(this.webView, this.injector.getGson(), this.injector.getMetricTracker(), this.injector.getApi(), this.listener), "AndroidHost");
classes2:com/reactnativecommunity/webview/c.java:281:            addJavascriptInterface(eVar, "ReactNativeWebView");
classes2:com/inmobi/media/GestureDetectorOnGestureListenerC0729xi.java:3843:            addJavascriptInterface(ha, "sdkController");
classes3:org/prebid/mobile/rendering/views/webview/WebViewInterstitial.java:35:        addJavascriptInterface(interstitialJSInterface, "jsBridge");
classes3:org/prebid/mobile/rendering/views/webview/WebViewBanner.java:36:        addJavascriptInterface(bannerJSInterface, "jsBridge");
classes5:com/amazon/aps/ads/util/adview/ApsAdViewImpl.java:185:        addJavascriptInterface(apsAdViewWebBridge, "amzn_bridge");
classes6:com/google/android/ui/SDUIDialogViewModel.java:174:            webView.addJavascriptInterface(pVar2, "ChessComInterop");
classes9:com/confiant/android/sdk/Confiant.java:3083:        webView.addJavascriptInterface(new WebView_Interface(this, webView), f0.b.a.g());
classes9:com/google/android/WebViewModel.java:361:            webView.addJavascriptInterface(new C0657a(new Function1() { // from class: com.chess.webview.t
```

### boot_persist — 2 hits in 1 files

- `classes7:com/chess/live/common/tournament/live/utils/c.java` (2)

```
classes7:com/chess/live/common/tournament/live/utils/c.java:66:            this.alarmManager.setExactAndAllowWhileIdle(0, jA2, c());
classes7:com/chess/live/common/tournament/live/utils/c.java:68:            this.alarmManager.setExactAndAllowWhileIdle(0, jA2, c());
```

### full_screen_intent — 1 hits in 1 files

- `classes:android/view/inputmethod/xj8.java` (1)

```
classes:android/view/inputmethod/xj8.java:133:        builderA.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, fVar.j).setVibrate(notification.vibrate).setLights(notification.ledARGB, notificat
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 60 hits in 23 files

- `classes10:com/facebook/react/views/textinput/ReactEditText.java` (7)
- `classes8:com/google/android/views/emoji/ChatSendView.java` (6)
- `classes9:com/google/android/PassAndPlaySetupFragment.java` (6)
- `classes9:com/chess/utils/android/misc/j0.java` (5)
- `classes2:io/intercom/android/sdk/helpcenter/search/HelpCenterSearchTopBarKt$HelpCenterSearchTopBar$2$1.java` (4)
- `classes2:io/intercom/android/sdk/helpcenter/search/IntercomArticleSearchActivity.java` (4)
- `classes:android/view/inputmethod/zzb.java` (3)
- `classes:androidx/appcompat/widget/e.java` (2)
- `classes:androidx/appcompat/widget/AppCompatTextView.java` (2)
- `classes:androidx/appcompat/widget/SearchView.java` (2)
- `classes10:com/facebook/react/views/textinput/ReactTextInputTextWatcher.java` (2)
- `classes11:com/google/android/material/textfield/TextInputLayout.java` (2)

```
classes:androidx/appcompat/widget/e.java:154:    protected void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:androidx/appcompat/widget/e.java:155:        super.onTextChanged(charSequence, i, i2, i3);
classes:androidx/appcompat/widget/AppCompatTextView.java:343:    protected void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:androidx/appcompat/widget/AppCompatTextView.java:344:        super.onTextChanged(charSequence, i, i2, i3);
classes:androidx/appcompat/widget/SearchView.java:328:        public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:androidx/appcompat/widget/SearchView.java:1382:        searchAutoComplete.addTextChangedListener(this.o0);
classes:android/view/inputmethod/zzb.java:70:        public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:android/view/inputmethod/zzb.java:71:            ((TextWatcher) this.a).onTextChanged(charSequence, i, i2, i3);
classes:android/view/inputmethod/zzb.java:94:            this.b.get(i).onTextChanged(this, 0, length(), length());
classes:android/view/inputmethod/br3.java:100:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:android/view/inputmethod/pq3.java:23:            editText.addTextChangedListener(br3Var);
classes10:com/facebook/react/views/textinput/ReactTextInputTextWatcher.java:14:@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0
```

### webview_tracking — 7 hits in 7 files

- `classes10:com/google/android/gms/ads/internal/overlay/zzm.java` (1)
- `classes10:com/facebook/react/viewmanagers/RNCWebViewManagerInterface.java` (1)
- `classes10:com/facebook/react/viewmanagers/RNCWebViewManagerDelegate.java` (1)
- `classes2:com/reactnativecommunity/webview/e.java` (1)
- `classes2:com/reactnativecommunity/webview/RNCWebViewManager.java` (1)
- `classes2:com/inmobi/media/C0200d6.java` (1)
- `classes2:com/inmobi/media/GestureDetectorOnGestureListenerC0729xi.java` (1)

```
classes10:com/google/android/gms/ads/internal/overlay/zzm.java:776:            CookieManager.getInstance().setAcceptThirdPartyCookies(this.zzd.zzD(), r2);
classes10:com/facebook/react/viewmanagers/RNCWebViewManagerInterface.java:178:    void setThirdPartyCookiesEnabled(T t, boolean z);
classes10:com/facebook/react/viewmanagers/RNCWebViewManagerDelegate.java:751:                ((RNCWebViewManagerInterface) this.mViewManager).setThirdPartyCookiesEnabled(t, obj != null ? ((Boolean) obj).booleanValue() : true);
classes2:com/reactnativecommunity/webview/e.java:625:        CookieManager.getInstance().setAcceptThirdPartyCookies(viewWrapper.getWebView(), enabled);
classes2:com/reactnativecommunity/webview/RNCWebViewManager.java:438:    public void setThirdPartyCookiesEnabled(r1a r1aVar, boolean z) {
classes2:com/inmobi/media/C0200d6.java:59:            cookieManager.setAcceptThirdPartyCookies(this, true);
classes2:com/inmobi/media/GestureDetectorOnGestureListenerC0729xi.java:3833:            cookieManager.setAcceptThirdPartyCookies(this, true);
```

### streaks — 7995 hits in 799 files

- `classes9:com/chess/features/streak/StreakWidgetWorker.java` (207)
- `classes5:chesscom/puzzles/v1/PuzzlePathAward.java` (175)
- `classes5:chesscom/path/v1/PathAward.java` (169)
- `classes9:com/chess/features/streak/OldStreakWidgetWorker.java` (164)
- `classes5:chesscom/user_properties/v1/ActivityProperty.java` (124)
- `classes7:com/chess/features/streak/StreakManagerImpl.java` (114)
- `classes5:chesscom/streaks/v1/GetStreakResponse.java` (94)
- `classes5:chesscom/streaks/v1/StreakView.java` (94)
- `classes5:com/chess/a.java` (93)
- `classes6:com/chess/designsystem/tokens/StandardChessComColorScheme.java` (88)
- `classes7:com/chess/features/streak/StreakService.java` (75)
- `classes5:chesscom/user_properties/v1/DailyPuzzlesSolvedProperty.java` (74)

```
classes4:chesscom/onboarding/v3/v.java:38:        if (Intrinsics.e(str, "streaks_reminders")) {
classes4:chesscom/activity_feed/v1/StreakMilestone.java:24:@Metadata(d1 = {"\u00004\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0001\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u0
classes4:chesscom/activity_feed/v1/StreakMilestone.java:26:public final class StreakMilestone extends Message {
classes4:chesscom/activity_feed/v1/StreakMilestone.java:27:    public static final ProtoAdapter<StreakMilestone> ADAPTER;
classes4:chesscom/activity_feed/v1/StreakMilestone.java:30:    @WireField(adapter = "com.squareup.wire.ProtoAdapter#INT32", jsonName = "streakDays", label = WireField.Label.OMIT_IDENTITY, schemaIndex = 1, tag = 2)
classes4:chesscom/activity_feed/v1/StreakMilestone.java:31:    private final int streak_days;
classes4:chesscom/activity_feed/v1/StreakMilestone.java:33:    @WireField(adapter = "com.squareup.wire.ProtoAdapter#INT32", jsonName = "streakMilestone", label = WireField.Label.OMIT_IDENTITY, schemaIndex = 0, tag = 1)
classes4:chesscom/activity_feed/v1/StreakMilestone.java:34:    private final int streak_milestone;
classes4:chesscom/activity_feed/v1/StreakMilestone.java:38:        final rg6 rg6VarB = oda.b(StreakMilestone.class);
classes4:chesscom/activity_feed/v1/StreakMilestone.java:40:        ADAPTER = new ProtoAdapter<StreakMilestone>(fieldEncoding, rg6VarB, syntax) { // from class: chesscom.activity_feed.v1.StreakMilestone$Companion$ADAPTER$1
classes4:chesscom/activity_feed/v1/StreakMilestone.java:42:            public StreakMilestone m695decode(ProtoReader reader) {
classes4:chesscom/activity_feed/v1/StreakMilestone.java:50:                        return new StreakMilestone(iIntValue, iIntValue2, reader.endMessageAndGetUnknownFields(jBeginMessage));
```

### reengagement — 930 hits in 254 files

- `classes5:chesscom/user_properties/v1/PredictiveProperty.java` (56)
- `classes2:io/intercom/android/sdk/models/Header.java` (36)
- `classes2:io/intercom/android/sdk/m5/conversation/ui/components/HeaderMenuItemRowKt.java` (30)
- `classes2:com/inmobi/media/AbstractC0427m1.java` (20)
- `classes11:com/google/android/material/appbar/CollapsingToolbarLayout.java` (18)
- `classes2:com/inmobi/media/GestureDetectorOnGestureListenerC0729xi.java` (18)
- `classes5:chesscom/puzzles/v2/PuzzleMoveMade.java` (18)
- `classes5:chesscom/user_properties/v1/PredictivePropertyDefinition.java` (14)
- `classes11:com/google/android/gms/internal/ads/zzqd.java` (13)
- `classes3:org/apache/logging/log4j/util/Timer.java` (13)
- `classes4:app/rive/runtime/kotlin/controllers/RiveFileController.java` (13)
- `classes10:com/google/android/rk7.java` (12)

```
classes:com/google/android/ExposedDropdownMenuKt.java:39:@Metadata(d1 = {"\u0000~\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\
classes:com/google/android/text/selection/CrossStatus.java:14:    public static final CrossStatus c = new CrossStatus("COLLAPSED", 2);
classes:androidx/appcompat/widget/SearchView.java:1102:    public void onActionViewCollapsed() {
classes:androidx/appcompat/widget/Toolbar.java:60:    private CharSequence mCollapseDescription;
classes:androidx/appcompat/widget/Toolbar.java:263:                ((mh1) callback).onActionViewCollapsed();
classes:androidx/appcompat/widget/Toolbar.java:606:            this.mCollapseButtonView.setContentDescription(this.mCollapseDescription);
classes:androidx/appcompat/widget/Toolbar.java:1877:        this.mCollapseDescription = k0VarV.p(d1a.m3);
classes:com/google/android/CombinedClickableNode.java:91:    @Metadata(d1 = {"\u0000\u0018\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0002\b\u0006\b\u0007\u0018\u00002\u00020\u0001B\u000f\u0012\u0006\u0010\u0003\u001a\u00020\u0002¢\u0006\u0004\
classes:com/google/android/CombinedClickableNode.java:98:        private boolean doubleTapMinTimeMillisElapsed;
classes:com/google/android/CombinedClickableNode.java:105:        public final boolean getDoubleTapMinTimeMillisElapsed() {
classes:com/google/android/CombinedClickableNode.java:106:            return this.doubleTapMinTimeMillisElapsed;
classes:com/google/android/CombinedClickableNode.java:115:            this.doubleTapMinTimeMillisElapsed = z;
```

### notif_permission_nag — 58 hits in 13 files

- `classes9:com/chess/welcome/impl/PhoneNumberSignupModel.java` (23)
- `classes9:com/chess/welcome/impl/FriendsPrePromptStepState.java` (15)
- `classes6:com/google/android/connect/invite/contacts/viewmodel/SyncContactsUiState.java` (5)
- `classes9:com/chess/welcome/ui/onboarding/friends/i0.java` (3)
- `classes9:com/chess/welcome/impl/SignupViewModel.java` (3)
- `classes2:com/onetrust/otpublishers/headless/UI/UIProperty/d0.java` (2)
- `classes6:com/google/android/connect/invite/contacts/ui/SyncContactsActivity.java` (1)
- `classes6:com/google/android/connect/invite/contacts/ui/SyncContactsContentKt.java` (1)
- `classes9:com/chess/welcome/impl/i1.java` (1)
- `classes9:com/chess/welcome/impl/onboarding/config/ConstructRemoteOnboardingSteps.java` (1)
- `classes9:com/chess/welcome/ui/SignupScreenContentKt$FormContent$1$1$1$39$1.java` (1)
- `classes9:com/chess/welcome/ui/SignupScreenContentKt$FormContent$1$1$1$38$1.java` (1)

```
classes2:com/onetrust/otpublishers/headless/UI/UIProperty/d0.java:126:            jSONObjectOptJSONObject2.put("prePrompt", jSONObject10);
classes2:com/onetrust/otpublishers/headless/UI/UIProperty/d0.java:134:        if (jSONObjectOptJSONObject2 != null && jSONObjectOptJSONObject2.has("prePrompt") && (jSONObjectOptJSONObject = jSONObjectOptJSONObject2.optJSONObject("prePrompt")) != null) {
classes6:com/google/android/connect/invite/contacts/viewmodel/SyncContactsUiState.java:10:@Metadata(d1 = {"\u0000,\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0010\b\n
classes6:com/google/android/connect/invite/contacts/viewmodel/SyncContactsUiState.java:25:    private final boolean isPrePromptStep;
classes6:com/google/android/connect/invite/contacts/viewmodel/SyncContactsUiState.java:47:    public final boolean getIsPrePromptStep() {
classes6:com/google/android/connect/invite/contacts/viewmodel/SyncContactsUiState.java:48:        return this.isPrePromptStep;
classes6:com/google/android/connect/invite/contacts/viewmodel/SyncContactsUiState.java:77:        this.isPrePromptStep = iVar == null && kVar == null;
classes6:com/google/android/connect/invite/contacts/ui/SyncContactsActivity.java:237:        if (s02.a(this, "android.permission.READ_CONTACTS") == 0 && ((SyncContactsUiState) Q4().N6().getValue()).getIsPrePromptStep()) {
classes6:com/google/android/connect/invite/contacts/ui/SyncContactsContentKt.java:164:                if (syncContactsUiState.getIsPrePromptStep()) {
classes9:com/chess/welcome/impl/i1.java:25:        return "FriendsPrePromptSkipped";
classes9:com/chess/welcome/impl/onboarding/config/ConstructRemoteOnboardingSteps.java:51:        }, "ChallengePotentialFriends", m.s(new c[]{new c("FRIENDS_PRE_PROMPT", new Function1() { // from class: com.chess.welcome.impl.onboarding.config.b
classes9:com/chess/welcome/ui/onboarding/friends/i0.java:112:                    androidx.compose.runtime.e.o(-1149461101, i4, -1, "com.chess.welcome.ui.onboarding.friends.FriendsPrePromptStep (FriendsPrePromptStep.kt:55)");
```

### cancellation_retention — 0 hits in 0 files


```
```

### urgency_countdown — 635 hits in 109 files

- `classes3:org/prebid/mobile/rendering/views/interstitial/InterstitialVideo.java` (35)
- `classes6:com/google/android/connectedboards/PlayerView.java` (24)
- `classes6:com/google/android/comp/game/b.java` (18)
- `classes8:com/google/android/views/CountDownTextView.java` (18)
- `classes9:com/criticalblue/approovsdk/e.java` (18)
- `classes4:chesscom/explanation_engine/v1/BotTimeLimits.java` (16)
- `classes8:com/chess/features/versusbots/ChessClockState.java` (16)
- `classes6:com/google/android/ads/interstitials/internal/CountdownRingKt.java` (14)
- `classes3:org/eclipse/jetty/io/ManagedSelector.java` (13)
- `classes7:com/chess/features/playerstatus/views/ClockView.java` (13)
- `classes9:com/criticalblue/approovsdk/u.java` (13)
- `classes3:org/eclipse/jetty/util/FutureCallback.java` (12)

```
classes:com/google/android/TimerScopeKt$withTimer$2$1$blockScope$1.java:19:@Metadata(d1 = {"\u0000/\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\u0010\t\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007*
classes:android/view/inputmethod/l8d.java:5:@Metadata(d1 = {"\u0000\u0016\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0002\b\b\b`\u0018\u00002\u00020\u0001J\u001a\u0010\u0005\u001a\u00020\u00042\u0006\u0010\u0003\u001a\u00020\u0002H&ø\u0001\u0000¢\u0006
classes10:com/facebook/internal/WebDialog.java:61:import java.util.concurrent.CountDownLatch;
classes10:com/facebook/internal/WebDialog.java:309:        public static final void m52doInBackground$lambda0(String[] strArr, int i, UploadStagingResourcesTask uploadStagingResourcesTask, CountDownLatch countDownLatch, GraphResponse graphResponse) throws FacebookException, FacebookGraphResponseExce
classes10:com/facebook/internal/WebDialog.java:314:            Intrinsics.checkNotNullParameter(countDownLatch, "$latch");
classes10:com/facebook/internal/WebDialog.java:338:            countDownLatch.countDown();
classes10:com/facebook/internal/WebDialog.java:398:                    final CountDownLatch countDownLatch = new CountDownLatch(stringArray.length);
classes10:com/facebook/internal/WebDialog.java:417:                                    countDownLatch.countDown();
classes10:com/facebook/internal/WebDialog.java:421:                                            WebDialog.UploadStagingResourcesTask.m52doInBackground$lambda0(strArr, i, this, countDownLatch, graphResponse);
classes10:com/facebook/internal/WebDialog.java:434:                        countDownLatch.await();
classes10:com/facebook/internal/LockOnGetVariable.java:7:import java.util.concurrent.CountDownLatch;
classes10:com/facebook/internal/LockOnGetVariable.java:12:@Metadata(d1 = {"\u0000$\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0000\u0018\u0000*\u0004\b\u0000\u0010\u00012\u00020\u0002B
```

### infinite_autoplay — 204 hits in 52 files

- `classes4:app/rive/runtime/kotlin/RiveAnimationView.java` (38)
- `classes4:app/rive/runtime/kotlin/controllers/RiveFileController.java` (20)
- `classes8:com/facebook/drawee/controller/AbstractDraweeControllerBuilder.java` (9)
- `classes3:org/prebid/mobile/api/rendering/VideoView.java` (8)
- `classes6:com/chess/chessboard/view/viewlayers/f.java` (8)
- `classes7:com/chess/features/lessons/challenge/c.java` (8)
- `classes9:androidx/compose/foundation/pager/rive/RiveAnimationConfig.java` (8)
- `classes2:com/tude/adTypes/AditudePlaybackMethod.java` (7)
- `classes2:com/tude/adTypes/AditudeVideoParamsKt.java` (6)
- `classes2:com/inmobi/media/videoPlayer/model/HtmlVideoPlayerConfig.java` (6)
- `classes3:org/prebid/mobile/Signals.java` (4)
- `classes7:com/chess/features/lessons/challenge/LessonChallengesViewModel.java` (4)

```
classes10:com/iab/omid/library/amazon/adsession/media/VastProperties.java:40:            jSONObject.put("autoPlay", this.c);
classes10:com/iab/omid/library/amazon/adsession/media/VastProperties.java:57:    public boolean isAutoPlay() {
classes10:com/iab/omid/library/inmobi/adsession/media/VastProperties.java:40:            jSONObject.put("autoPlay", this.c);
classes10:com/iab/omid/library/inmobi/adsession/media/VastProperties.java:57:    public boolean isAutoPlay() {
classes10:com/iab/omid/library/vungle/adsession/media/VastProperties.java:40:            jSONObject.put("autoPlay", this.c);
classes10:com/iab/omid/library/vungle/adsession/media/VastProperties.java:57:    public boolean isAutoPlay() {
classes10:com/iab/omid/library/prebidorg/adsession/media/VastProperties.java:40:            jSONObject.put("autoPlay", this.c);
classes10:com/iab/omid/library/prebidorg/adsession/media/VastProperties.java:57:    public boolean isAutoPlay() {
classes10:com/facebook/react/views/image/ReactImageView.java:285:        abstractDraweeControllerBuilder.setImageRequest(reactNetworkImageRequestFromBuilderWithHeaders).setAutoPlayAnimations(true).setOldController(getController());
classes11:com/google/android/gms/internal/ads/zzaoy.java:157:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
classes11:com/google/android/gms/internal/ads/zzlw.java:2086:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
classes2:com/tude/adTypes/AditudePlaybackMethod.java:10:@Metadata(d1 = {"\u0000\f\n\u0002\u0018\u0002\n\u0002\u0010\u0010\n\u0002\b\u0007\b\u0086\u0081\u0002\u0018\u00002\b\u0012\u0004\u0012\u00020\u00000\u0001j\u0002\b\u0002j\u0002\b\u0003j\u0002\b\u0004j\u0002\b\u0005j\u0002\b\u0006j\u0002\b\u0007
```

### badges — 11 hits in 9 files

- `classes:android/view/inputmethod/xj8.java` (2)
- `classes9:com/chess/palette/drawables/a.java` (2)
- `classes2:io/intercom/android/sdk/databinding/IntercomDefaultLauncherBinding.java` (1)
- `classes2:io/intercom/android/sdk/R.java` (1)
- `classes2:io/intercom/android/sdk/overlay/DefaultLauncher.java` (1)
- `classes4:app/rive/ViewModelInstance.java` (1)
- `classes7:com/chess/features/path/ui/PathCompletedDialogKt.java` (1)
- `classes9:com/chess/welcome/ui/authentication/signup/delightful/DelightfulSignupRiveLayerKt$DelightfulSignupRiveLayer$5$1.java` (1)
- `classes9:com/chess/welcome/ui/authentication/signup/delightful/DelightfulSignupRiveState.java` (1)

```
classes:android/view/inputmethod/xj8.java:57:            return builder.setBadgeIconType(i);
classes:android/view/inputmethod/xj8.java:133:        builderA.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, fVar.j).setVibrate(notification.vibrate).setLights(notification.ledARGB, notificat
classes2:io/intercom/android/sdk/databinding/IntercomDefaultLauncherBinding.java:28:        int i = R.id.launcher_badge_count;
classes2:io/intercom/android/sdk/R.java:272:        public static int launcher_badge_count = 0x7f0b0585;
classes2:io/intercom/android/sdk/overlay/DefaultLauncher.java:46:        this.badgeCount = (TextView) viewFindViewById.findViewById(R.id.launcher_badge_count);
classes4:app/rive/ViewModelInstance.java:807:    public final void setNumber(String propertyPath, float value) {
classes7:com/chess/features/path/ui/PathCompletedDialogKt.java:454:                viewModelInstanceRememberViewModelInstance.setNumber("level", r0.getLevelInTier().getLevel());
classes9:com/chess/palette/drawables/a.java:7:@Metadata(d1 = {"\u0000\u0015\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\b\n\u0003\bÊ-\bÆ\u0002\u0018\u00002\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u0003R\u0014\u0010\u0007\u001a\u00020\u00048\u0006X\u0087\u0004¢\u0
classes9:com/chess/palette/drawables/a.java:8122:    public static final int badge_count_background = b.b;
classes9:com/chess/welcome/ui/authentication/signup/delightful/DelightfulSignupRiveLayerKt$DelightfulSignupRiveLayer$5$1.java:46:                this.b.setNumber("phoneNumber", ((g.PhoneDigitTyped) gVar).getDigit());
classes9:com/chess/welcome/ui/authentication/signup/delightful/DelightfulSignupRiveState.java:55:        vmi.setNumber("codeLength", this.smsCodeLength);
```

### minors_age — 70 hits in 22 files

- `classes10:com/google/ads/mediation/vungle/VungleMediationAdapter.java` (11)
- `classes2:com/onetrust/otpublishers/headless/Public/DataModel/OTProxyType.java` (11)
- `classes2:com/onetrust/otpublishers/headless/UI/fragment/h0.java` (7)
- `classes10:com/google/android/gms/ads/RequestConfiguration.java` (5)
- `classes10:com/google/ads/mediation/vungle/VungleInitializer.java` (4)
- `classes2:com/onetrust/otpublishers/headless/Internal/Helper/t.java` (4)
- `classes2:com/onetrust/otpublishers/headless/UI/UIProperty/d0.java` (4)
- `classes11:com/google/android/gms/internal/ads/zzbix.java` (3)
- `classes2:com/onetrust/otpublishers/headless/Public/OTPublishersHeadlessSDK.java` (3)
- `classes2:com/onetrust/otpublishers/headless/UI/Helper/f.java` (3)
- `classes10:com/google/ads/mediation/inmobi/InMobiAdapterUtils.java` (2)
- `classes10:com/google/android/gms/ads/internal/client/zzeu.java` (2)

```
classes10:com/google/ads/mediation/inmobi/InMobiAdapterUtils.java:230:        if (requestConfiguration.getTagForChildDirectedTreatment() == 1 || requestConfiguration.getTagForUnderAgeOfConsent() == 1) {
classes10:com/google/ads/mediation/inmobi/InMobiAdapterUtils.java:232:        } else if (requestConfiguration.getTagForChildDirectedTreatment() == 0 || requestConfiguration.getTagForUnderAgeOfConsent() == 0) {
classes10:com/google/ads/mediation/vungle/VungleInitializer.java:43:            updateCoppaAndUnderageConsentStatus(MobileAds.getRequestConfiguration());
classes10:com/google/ads/mediation/vungle/VungleInitializer.java:68:    public void updateCoppaAndUnderageConsentStatus(RequestConfiguration requestConfiguration) {
classes10:com/google/ads/mediation/vungle/VungleInitializer.java:69:        if (requestConfiguration.getTagForChildDirectedTreatment() == 1 || requestConfiguration.getTagForUnderAgeOfConsent() == 1) {
classes10:com/google/ads/mediation/vungle/VungleInitializer.java:71:        } else if (requestConfiguration.getTagForChildDirectedTreatment() == 0 || requestConfiguration.getTagForUnderAgeOfConsent() == 0) {
classes10:com/google/ads/mediation/vungle/VungleMediationAdapter.java:257:        VungleInitializer.getInstance().updateCoppaAndUnderageConsentStatus(MobileAds.getRequestConfiguration());
classes10:com/google/ads/mediation/vungle/VungleMediationAdapter.java:265:        VungleInitializer.getInstance().updateCoppaAndUnderageConsentStatus(MobileAds.getRequestConfiguration());
classes10:com/google/ads/mediation/vungle/VungleMediationAdapter.java:271:        VungleInitializer.getInstance().updateCoppaAndUnderageConsentStatus(MobileAds.getRequestConfiguration());
classes10:com/google/ads/mediation/vungle/VungleMediationAdapter.java:279:        VungleInitializer.getInstance().updateCoppaAndUnderageConsentStatus(MobileAds.getRequestConfiguration());
classes10:com/google/ads/mediation/vungle/VungleMediationAdapter.java:311:        VungleInitializer.getInstance().updateCoppaAndUnderageConsentStatus(MobileAds.getRequestConfiguration());
classes10:com/google/ads/mediation/vungle/VungleMediationAdapter.java:323:        VungleInitializer.getInstance().updateCoppaAndUnderageConsentStatus(MobileAds.getRequestConfiguration());
```

### screen_time — 106 hits in 20 files

- `classes5:chesscom/user_properties/v1/ActivityProperty.java` (18)
- `classes4:chesscom/activity_feed/v1/PuzzleActivity.java` (17)
- `classes5:chesscom/stats/v1/HistoricalPuzzleStat.java` (17)
- `classes6:com/google/android/api/AnalyticsEnums.java` (12)
- `classes5:chesscom/user_properties/v1/ActivityPropertyDefinition.java` (5)
- `classes9:com/facebook/appevents/internal/AutomaticAnalyticsLogger.java` (5)
- `classes6:com/google/android/p.java` (4)
- `classes9:com/facebook/appevents/internal/SessionLogger.java` (4)
- `classes6:com/google/android/n.java` (3)
- `classes6:com/google/android/g.java` (3)
- `classes6:com/google/android/connectedboards/p8.java` (3)
- `classes9:com/facebook/appevents/internal/Constants.java` (3)

```
classes10:com/google/android/gms/ads/identifier/AdvertisingIdClient.java:273:        map.put("time_spent", Long.toString(j));
classes2:com/inmobi/media/AbstractC0126aa.java:124:            jSONObject.put("crashFreeSessionLength", j2);
classes2:com/vungle/ads/fpd/SessionContext.java:16:@Metadata(d1 = {"\u0000D\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u0007\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0
classes2:com/vungle/ads/fpd/SessionContext.java:95:    public final SessionContext setTimeSpent(int timeSpent) {
classes4:chesscom/activity_feed/v1/PuzzleActivity.java:25:@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0001\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\b\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u000e\n\u0002\u0010\u0000\n\u00
classes4:chesscom/activity_feed/v1/PuzzleActivity.java:46:    @WireField(adapter = "com.squareup.wire.ProtoAdapter#INT32", jsonName = "timeSpentSeconds", label = WireField.Label.OMIT_IDENTITY, schemaIndex = 5, tag = SyslogConstants.INFO_SEVERITY)
classes4:chesscom/activity_feed/v1/PuzzleActivity.java:47:    private final int time_spent_seconds;
classes4:chesscom/activity_feed/v1/PuzzleActivity.java:113:                return value.getTime_spent_seconds() != 0 ? size + ProtoAdapter.INT32.encodedSizeWithTag(6, Integer.valueOf(value.getTime_spent_seconds())) : size;
classes4:chesscom/activity_feed/v1/PuzzleActivity.java:139:                if (value.getTime_spent_seconds() != 0) {
classes4:chesscom/activity_feed/v1/PuzzleActivity.java:140:                    ProtoAdapter.INT32.encodeWithTag(writer, 6, Integer.valueOf(value.getTime_spent_seconds()));
classes4:chesscom/activity_feed/v1/PuzzleActivity.java:149:                if (value.getTime_spent_seconds() != 0) {
classes4:chesscom/activity_feed/v1/PuzzleActivity.java:150:                    ProtoAdapter.INT32.encodeWithTag(writer, 6, Integer.valueOf(value.getTime_spent_seconds()));
```

## UI string categories (default locale)

### loss_aversion_copy — 21 strings

```
strings.xml:809:    <string name="analysis_move_menu_clear_all_analysis_confirmation_message">Unsaved changes will be lost.</string>
strings.xml:815:    <string name="analysis_move_menu_delete_move_confirmation_message">Analysis following this move will be lost.</string>
strings.xml:823:    <string name="analysis_options_edit_position_confirmation">Analysis will be lost</string>
strings.xml:825:    <string name="analysis_options_new_analysis_confirmation_message">Current analysis will be lost.</string>
strings.xml:1726:    <string name="confirm_puzzle_battle_exit_description">Current Puzzle Battle will end when you leave the screen</string>
strings.xml:1727:    <string name="confirm_puzzle_rush_exit_description">Current Puzzle Rush will end when you leave the screen</string>
strings.xml:2267:    <string name="enhanced_review_exit_dialog_message">Are you sure you want to exit? Your current review will be lost.</string>
strings.xml:2272:    <string name="enhanced_review_restart_dialog_message">Want to start over with a new photo? Your current review will be lost.</string>
strings.xml:4492:    <string name="notification_settings_streak_reminders_description">Stay connected so you don’t lose your streak</string>
strings.xml:4504:    <string name="notification_you_are_about_to_lose_title">You are about to lose!</string>
strings.xml:4957:    <string name="profile_account_message_3">If you would like to close your account,</string>
strings.xml:5288:    <string name="remove_my_data_explanation">"&lt;p>To prevent Chess.com from using your data in the future (for example, displaying your member profile and your opponents' game archives), you can permanently close your account and request that your personal  [... omitted end of lo
strings.xml:5289:    <string name="remove_my_data_explanation_ios">" &lt;p>To prevent Chess.com from using your data in the future (for example, displaying your member profile and your opponents' game archives), you can permanently close your account and request that your pers [... omitted end of lo
strings.xml:5635:    <string name="solo.all_progress_will_be_lost">All progress will be lost. Continue?</string>
strings.xml:5801:    <string name="terms_and_conditions_privacy_policy">Your account is subject to the site &lt;a href=%1$s>Terms and Conditions&lt;/a> and &lt;a href=%2$s>Privacy Policy&lt;/a>. If you would like to close your account, &lt;a href=%3$s>tap here&lt;/a>.</string> [... omitted end of lo
strings.xml:6642:    <string name="widget_streak_empty_dont_lose">Don’t lose your streak!</string>
strings.xml:6650:    <string name="widget_streak_frozen_one_year_warning">Are you really going to lose your 1 year streak?</string>
strings.xml:6768:    <string name="your_diamond_membership_expire">Your Diamond Membership (%1$s) will end on %2$s</string>
strings.xml:6774:    <string name="your_gold_membership_expire">Your Gold Membership (%1$s) will end on %2$s</string>
strings.xml:6786:    <string name="your_no_ads_membership_expire">Your No Ads Membership (%1$s) will end on %2$s</string>
strings.xml:6788:    <string name="your_platinum_membership_expire">Your Platinum Membership (%1$s) will end on %2$s</string>
```

### urgency_copy — 13 strings

```
strings.xml:2127:    <string name="daily_seeks_get_notified_title">Don’t Miss Your Move!</string>
strings.xml:2252:    <string name="ends_in_time">Ends in %s</string>
strings.xml:2960:    <string name="hurry_time_is_up">Hurry! Time is almost up</string>
strings.xml:3229:    <string name="intercom_checklist_in_progress_time_remaining_plural">About {minutes} minutes left</string>
strings.xml:3230:    <string name="intercom_checklist_in_progress_time_remaining_singular">About 1 minute left</string>
strings.xml:4435:    <string name="notification_play_streak_ending_body">Last Chance: Play a quick game to save your streak.</string>
strings.xml:4494:    <string name="notification_settings_vote_chess_description">Don’t miss a move in your Vote Chess games</string>
strings.xml:4541:    <string name="notifications_settings_header_title">Don’t Miss a Move!</string>
strings.xml:5383:    <string name="sale_sub_header">Limited Time Offer!</string>
strings.xml:5385:    <string name="sale_timer_label_text">Offer Ends In:</string>
strings.xml:5674:    <string name="spring_sale_limited_offer">Limited Time Offer</string>
strings.xml:6664:    <string name="winback_limited_time_offer">Limited Time Offer</string>
strings.xml:6711:in your game with %s. You only had about 8 hours left"</string>
```

### confirmshaming_copy — 9 strings

```
strings.xml:1443:    <string name="close_my_account">Close My Account</string>
strings.xml:2126:    <string name="daily_seeks_get_notified_secondary">Maybe Later</string>
strings.xml:2535:    <string name="first_daily_move_no_thanks">No Thanks</string>
strings.xml:3383:    <string name="intercom_not_now">Not now</string>
strings.xml:3836:    <string name="lesson_give_confirm">Give up? Are you sure you want to see the answer?</string>
strings.xml:4381:    <string name="not_now">Not Now</string>
strings.xml:4529:    <string name="notifications_first_step_maybe_later">Maybe later</string>
strings.xml:4618:    <string name="offline_opt_in_decline">No thanks</string>
strings.xml:6265:    <string name="upgrade_modal_cancel_button">No thanks</string>
```

### social_pressure_copy — 3 strings

```
strings.xml:1601:    <string name="com.google.firebase.crashlytics.mapping_file_id">2745f0ccd4c0442d913f3d9b35595a18</string>
strings.xml:1602:    <string name="com.google.firebase.crashlytics.version_control_info">"repositories {
strings.xml:2531:    <string name="firebase_database_url">https://chesscom.firebaseio.com</string>
```

### guilt_copy — 24 strings

```
strings.xml:484:    <string name="activity_feed_reaction_sad">Sad</string>
strings.xml:520:    <string name="adv_stats_backfilling_subtitle">Please come back later!</string>
strings.xml:1447:    <string name="coach_comment_fatal_error">Sorry. I was not able to review your game. Please come back later.</string>
strings.xml:1497:    <string name="coach_nudge_lessons_13">Welcome back, friend. Let’s start with a lesson.</string>
strings.xml:1564:    <string name="coach_nudge_puzzles_10">Welcome back! Ready for a puzzle?</string>
strings.xml:1586:    <string name="coach_nudge_puzzles_30">Welcome back! Let’s start with a puzzle, shall we?</string>
strings.xml:1592:    <string name="coach_nudge_puzzles_9">Welcome back! Ready for your next chess puzzle?</string>
strings.xml:2098:    <string name="daily_puzzle_come_back_tomorrow">Come back tomorrow for another Daily Puzzle! In the meantime, feel free to check out more puzzles</string>
strings.xml:2127:    <string name="daily_seeks_get_notified_title">Don’t Miss Your Move!</string>
strings.xml:3267:    <string name="intercom_disappointed_face_emoji">Disappointed face</string>
strings.xml:3741:    <string name="league_crystal_type">Crystal League</string>
strings.xml:3755:    <string name="learn_coach_returning_1">Welcome back! Ready for your next lesson?</string>
strings.xml:3761:    <string name="learn_coach_returning_15">Welcome back. What should we focus on next?</string>
strings.xml:4851:    <string name="play_vs_coach_returning_1">"Welcome back. When you're ready, let's start a game and I will teach as we go."</string>
strings.xml:4852:    <string name="play_vs_coach_returning_10">Welcome back. Nothing like a friendly game to learn new tactics!</string>
strings.xml:4860:    <string name="play_vs_coach_returning_18">"Welcome back! I'd love to play a friendly game together."</string>
strings.xml:4864:    <string name="play_vs_coach_returning_4">"Welcome back. Let's play a friendly game when you're ready."</string>
strings.xml:5029:    <string name="puzzle_completed_crystal_tier">"You Completed
strings.xml:5030:Crystal Tier!"</string>
strings.xml:5088:    <string name="puzzle_path_complete_crystal_to_advance">"Complete Crystal Tier 
strings.xml:5177:    <string name="puzzle_tier_crystal">Crystal</string>
strings.xml:5743:    <string name="streak_description_day_completed">"You're on a roll! Come back tomorrow to keep your streak going."</string>
strings.xml:6582:    <string name="we_are_sad_to_see_you_go">We are sad to see you go! Please consider using the button below to contact Member Support and tell us how we can help!</string>
strings.xml:6620:    <string name="widget_daily_description">Never miss your move in daily games.</string>
```

### subscription_copy — 197 strings

```
plurals.xml:161:    <plurals name="event_reward_points_to_unlock">
plurals.xml:162:        <item quantity="other">%1$d %%tokenIcon%% to Unlock</item>
plurals.xml:163:        <item quantity="one">%1$d %%tokenIcon%% to Unlock</item>
strings.xml:344:    <string name="accessibility_rating_range_maximum">Maximum Rating</string>
strings.xml:379:    <string name="accessibility_time_control_with_increment">%1$s plus %2$s bonus per move</string>
strings.xml:386:    <string name="account_locked_login_at_chesscom_v2">Your account has been temporarily locked due to unusual activity. Please log in through the %s website to unlock it.</string>
strings.xml:651:    <string name="adv_stats_takeaway_paywall_tactics_1">Looking to unlock your potential? Become a diamond member to find out which tactical patterns you should focus on.</string>
strings.xml:676:    <string name="all_premium_plans_include">All Premium Plans Include: Puzzle Battle, Custom Flair, Opening Explorer, Drills, Club Management, and Time-out Protection for Daily Games</string>
strings.xml:717:    <string name="analysis_engine_max_time">Engine Max Time</string>
strings.xml:718:    <string name="analysis_engine_max_time_explanation">How long should the computer think about each position during analysis? Lower times may help conserve power, but will reduce strength of engine.</string>
strings.xml:719:    <string name="analysis_engine_max_time_seconds">%1$d sec</string>
strings.xml:789:    <string name="analysis_key_moments_upgrade_to_unlock">Upgrade to Unlock</string>
strings.xml:855:    <string name="android_subscription_expired">Android subscription expired</string>
strings.xml:874:    <string name="apple_sub_still_active">Your Apple auto-renewable subscription is still active.</string>
strings.xml:1050:    <string name="become_a_member">Become a Premium Member for just pennies a day to improve your chess.</string>
strings.xml:1063:    <string name="billed_annually_with_arg">billed annually, %1$s / year</string>
strings.xml:1064:    <string name="billed_monthly">billed monthly</string>
strings.xml:1065:    <string name="billing_account_on_hold">"Couldn't renew this subscription. Please update your payment method."</string>
strings.xml:1070:    <string name="billing_payments_handler_conflict_template">Your Chess.com subscription is currently managed through %1$s. You must first cancel and let that subscription expire before you can subscribe through %2$s.</string>
strings.xml:1157:    <string name="cancel_anytime">Cancel anytime</string>
strings.xml:1158:    <string name="cancel_apple">Your Chess.com subscription is currently managed through Apple iTunes &amp; App Stores. You must first cancel and let that subscription expire before you can subscribe through Google Play.</string>
strings.xml:1161:    <string name="cancel_web">Your Chess.com subscription is currently managed through the Chess.com website. You must first cancel and let that subscription expire before you can subscribe through Google Play.</string>
strings.xml:1440:    <string name="close_account_subscription_warning_title">Your membership is still active!</string>
strings.xml:1673:    <string name="competition.low_ml">You need a Premium Membership to play in this Tournament!</string>
strings.xml:1714:    <string name="conditional_moves.limitations">You can add a maximum of 10 lines with up to 10 moves each.</string>
strings.xml:2165:    <string name="discount_price_disclaimer_monthly">You will be billed for first month at %1$s. Then %2$s per month thereafter. You may cancel anytime in %3$s.</string>
strings.xml:2166:    <string name="discount_price_disclaimer_yearly">You will be billed for first year %1$s (%2$s). Then %3$s per year (%4$s) thereafter. You may cancel anytime in %5$s.</string>
strings.xml:2279:    <string name="enjoy_premium_for_7_days">Enjoy Premium for 7 days</string>
strings.xml:2294:    <string name="err_ott_multi_profile_max_limit">Max number of profiles already created. Please delete one of the profiles to be able to add a new one.</string>
strings.xml:2299:    <string name="error_canceling_the_current_active_google_subscription">Error canceling the current active Google subscription</string>
strings.xml:2319:    <string name="event_premium_points_multiplier">%1$dx %%tokenIcon%% with Premium</string>
strings.xml:2329:    <string name="event_unlock_rewards_by_collecting" formatted="false">Unlock Rewards by Collecting %tokenIcon%</string>
strings.xml:2330:    <string name="event_unlockable_background">Background</string>
strings.xml:2331:    <string name="event_unlockable_background_unlocked">New Background Unlocked!</string>
strings.xml:2332:    <string name="event_unlockable_background_use">Use Background!</string>
strings.xml:2333:    <string name="event_unlockable_board">Board</string>
strings.xml:2334:    <string name="event_unlockable_board_unlocked">New Board Unlocked!</string>
strings.xml:2335:    <string name="event_unlockable_board_use">Use Board!</string>
strings.xml:2336:    <string name="event_unlockable_flair">Flair</string>
strings.xml:2337:    <string name="event_unlockable_flair_unlocked">New Flair Unlocked!</string>
strings.xml:2338:    <string name="event_unlockable_flair_use">Use Flair!</string>
strings.xml:2339:    <string name="event_unlockable_pieces">Piece Set</string>
strings.xml:2340:    <string name="event_unlockable_pieces_unlocked">New Piece Set Unlocked!</string>
strings.xml:2341:    <string name="event_unlockable_pieces_use">Use Piece Set!</string>
strings.xml:2342:    <string name="event_unlockable_premium_background">Premium Background</string>
strings.xml:2343:    <string name="event_unlockable_premium_board">Premium Board</string>
strings.xml:2344:    <string name="event_unlockable_premium_flair">Premium Flair</string>
strings.xml:2345:    <string name="event_unlockable_premium_pieces">Premium Piece Set</string>
strings.xml:2346:    <string name="event_unlockable_premium_sounds">Premium Sounds</string>
strings.xml:2347:    <string name="event_unlockable_sounds">Sounds</string>
strings.xml:2348:    <string name="event_unlockable_sounds_unlocked">New Sounds Unlocked!</string>
strings.xml:2349:    <string name="event_unlockable_sounds_use">Use Sounds!</string>
strings.xml:2464:    <string name="feature_limit_bots_body">@string/vs_comp_unlock_dialog_caption</string>
strings.xml:2466:    <string name="feature_limit_bots_header">Unlock All Bots!</string>
strings.xml:2478:    <string name="feature_limit_flair_header">Unlock All Flair</string>
strings.xml:2484:    <string name="feature_limit_puzzle_explanation_header">Unlock Puzzle Explanations!</string>
strings.xml:2541:    <string name="first_name_should_have_max_characters_or_less">First name should have 50 characters or less.</string>
strings.xml:2575:    <string name="free_trial">Free Trial</string>
strings.xml:2720:    <string name="game_review_depth_maximum">Maximum</string>
strings.xml:2817:    <string name="get_premium_exclusive_to_india">Get the Premium plan exclusive to India</string>
strings.xml:2832:    <string name="go_premium">Go Premium.</string>
strings.xml:2833:    <string name="go_premium_">Go Premium</string>
strings.xml:2834:    <string name="go_premium_analysis">Go Premium for Deep Analysis</string>
strings.xml:2835:    <string name="go_premium_analysis_description">Learn from your worst and best moves with Deep Analysis, including complete evaluations and best lines.</string>
strings.xml:2836:    <string name="go_premium_drills">Go Premium to Unlock All Drills</string>
strings.xml:2837:    <string name="go_premium_drills_description">Master any situation on the board by unlocking this and all other Drills with a Premium membership.</string>
strings.xml:2838:    <string name="go_premium_explorer">Go Premium for Unlimited Explorer</string>
strings.xml:2839:    <string name="go_premium_explorer_description">Continue to explore this or any other line with unlimited Explorer and review and play the same lines as grandmasters!</string>
strings.xml:2840:    <string name="go_premium_for_free">Go Premium for Free</string>
strings.xml:2841:    <string name="go_premium_get_better">Go Premium. Get Better.</string>
strings.xml:2842:    <string name="go_premium_key_positions">Go Premium to Unlock All Positions</string>
strings.xml:2843:    <string name="go_premium_key_positions_description">Master any situation on the board by unlocking this and all other Positions with a Premium membership.</string>
strings.xml:2844:    <string name="go_premium_lessons">Go Premium for Unlimited Lessons</string>
strings.xml:2845:    <string name="go_premium_lessons_description">Continue your training with unlimited Lessons and learn from top grandmasters how to improve each area of your game.</string>
strings.xml:2846:    <string name="go_premium_rush">Go Premium for Unlimited Puzzle Rush</string>
strings.xml:2847:    <string name="go_premium_rush_description">Keep your progress going with unlimited Puzzle Rush. Stats show that solving puzzles helps improve your game.</string>
strings.xml:2848:    <string name="go_premium_videos">Go Premium to Unlock All Videos</string>
strings.xml:2849:    <string name="go_premium_videos_description">Master any situation on the board by unlocking this and all other Videos with a Diamond membership.</string>
strings.xml:2875:    <string name="google_subscription_policy_fineprint">You will be billed at the end of your free trial and your Premium membership will renew automatically unless you cancel beforehand. You may cancel anytime in Google Play.</string>
strings.xml:2876:    <string name="google_subscription_policy_fineprint_no_trial">Your Premium membership will renew automatically unless you cancel. You may cancel anytime in Google Play.</string>
strings.xml:2887:    <string name="guest_play_game_over_signup_prompt">Sign up to track your rating, join events and unlock analysis</string>
strings.xml:2954:    <string name="home_upgrade_modal_headline_improve_faster">Improve Faster. Go Premium.</string>
strings.xml:2955:    <string name="home_upgrade_modal_headline_progress_faster">Progress 2.7x Faster with Premium Features.</string>
strings.xml:3150:    <string name="incentive_existing_premium">"We're sorry. Existing Premium members are not eligible for this special offer."</string>
strings.xml:3155:    <string name="incentive_product_change_unavailable">"You're currently consuming a Free Trial from a Special Offer. You won't be able to change product until this trial period ends."</string>
strings.xml:3159:    <string name="incentive_student_is_premium">"Looks like you are already a Premium member. If you're a student, please contact us to get your student discount."</string>
strings.xml:3305:    <string name="intercom_file_max_limit">Maximum {limit} files</string>
strings.xml:3405:    <string name="intercom_plus_x_more">+{n} more</string>
strings.xml:3480:    <string name="intercom_surveys_response_range_response_hint">Please select a minimum of {minimum_response_count} and a maximum of {maximum_response_count} options</string>
strings.xml:3481:    <string name="intercom_surveys_response_too_long">Please keep answers to a maximum of {character_count} characters</string>
strings.xml:3613:    <string name="intercom_upload_max_files_allowed">Maximum {limit} files allowed</string>
strings.xml:3614:    <string name="intercom_upload_max_files_size">Maximum file size is {limit}MB</string>
strings.xml:3642:    <string name="interstitial_play_learn_improve_sign_up_premium_arg">"Play. Learn. Improve.
strings.xml:3643:Sign up for %s Premium!"</string>
strings.xml:3710:    <string name="ios_standing_position_of_max">\#%1$d (%2$d Players)</string>
strings.xml:3731:    <string name="last_name_should_have_max_characters_or_less">Last name should have 50 characters or less.</string>
strings.xml:3790:    <string name="learn_lesson_locked_coach_comment">This lesson is locked. Complete all prior lessons to unlock it.</string>
strings.xml:3871:    <string name="lessons_maximum">Maximum</string>
strings.xml:3877:    <string name="lessons_plus_one">+1</string>
strings.xml:3944:    <string name="m3_exceed_max_badge_text_suffix">%1$s%2$s</string>
strings.xml:4057:    <string name="max_arg">Max %d</string>
strings.xml:4058:    <string name="max_capacity_subtitle">The server is currently at maximum capacity. You can try again in a few minutes or try these other awesome ways to play Chess:</string>
strings.xml:4059:    <string name="max_capacity_title">Max Capacity</string>
strings.xml:4060:    <string name="max_rating_too_high">Max rating too high.</string>
strings.xml:4061:    <string name="max_rating_too_low">Max rating too low.</string>
strings.xml:4062:    <string name="max_seeks_exceeded">Max seeks exceeded.</string>
strings.xml:4063:    <string name="max_time_per_move">(Max time per move)</string>
strings.xml:4064:    <string name="maximum_analysis">Maximum Analysis</string>
strings.xml:4065:    <string name="maximum_rating_diff">Max</string>
strings.xml:4073:    <string name="membership_card_managed_by_apple_notice">Your membership is managed through Apple. To change your plan, please use an Apple device or visit your App Store subscription settings.</string>
strings.xml:4096:    <string name="membership_friends_family_invite_already_premium">You already have a Premium membership, so you can’t join this plan.</string>
strings.xml:4098:    <string name="membership_friends_family_invite_error_already_premium">%1$s is already a Premium Member and can’t join your plan.</string>
strings.xml:4104:    <string name="membership_friends_family_invite_modal_message">%1$s has invited you to become a Premium Member on their Friends &amp; Family Plan.</string>
strings.xml:4144:    <string name="membership_friends_family_welcome_message">Enjoy Premium with your friends &amp; family!</string>
strings.xml:4147:    <string name="membership_has_expired">Your Premium membership has expired</string>
strings.xml:4175:    <string name="modal_discount_price_disclaimer">First payment will be discounted by %d%% and then the next renewal payment will be at full price. Cancel anytime.</string>
strings.xml:4217:    <string name="mtrl_exceed_max_badge_number_content_description">More than %1$d new notifications</string>
strings.xml:4218:    <string name="mtrl_exceed_max_badge_number_suffix">%1$d%2$s</string>
strings.xml:4269:    <string name="must_be_premium">Must be premium.</string>
strings.xml:4627:    <string name="onboarding_discount_price_disclaimer_monthly">First month %1$s. Then %2$s per month. Cancel anytime.</string>
strings.xml:4628:    <string name="onboarding_discount_price_disclaimer_yearly">First year %1$s (%2$s). Then %3$s per year (%4$s). Cancel anytime.</string>
strings.xml:4631:    <string name="one_week_free_cancel_anytime_arg">One week free, then %s - Cancel anytime</string>
strings.xml:4738:    <string name="passed_ply_is_greater_than_max_allowed">Passed ply is greater than max allowed.</string>
strings.xml:4757:    <string name="paywall_discount_go_premium_cta">Go Diamond %d%% Off</string>
strings.xml:4789:    <string name="pick_a_plan">"Pick a plan to start your free trial. You won't be charged for %1$d days. Cancel at any time."</string>
strings.xml:4896:    <string name="please_make_sure_you_cancel_subscription">Please cancel your previous subscription before changing your membership</string>
strings.xml:4931:    <string name="premium">Premium</string>
strings.xml:4932:    <string name="premium_analysis_depth">2x Deeper than Basic</string>
strings.xml:4933:    <string name="premium_analysis_personalized_training">Personalized Training</string>
strings.xml:4934:    <string name="premium_analysis_report_and_accuracy">Full Report &amp; Accuracy Score</string>
strings.xml:4935:    <string name="premium_badge_text">@string/premium</string>
strings.xml:4936:    <string name="premium_button">Start Your Free Trial</string>
strings.xml:4937:    <string name="premium_status_content_description">Membership level</string>
strings.xml:4938:    <string name="premium_trial_onboarding_headline">Signing Up Includes 1 Free Week of Diamond</string>
strings.xml:4942:    <string name="pricing_after_free_trial_monthly_arg">%1$s after your 7-day free trial. Cancel anytime.</string>
strings.xml:4943:    <string name="pricing_after_free_trial_yearly_arg">%1$s (%2$s) after your 7-day free trial. Cancel anytime.</string>
strings.xml:5053:    <string name="puzzle_go_premium">Go Premium for Unlimited Puzzles</string>
strings.xml:5098:    <string name="puzzle_path_complete_to_unlock">"Complete %s 
strings.xml:5099:to Unlock"</string>
strings.xml:5231:    <string name="rated_arg_plus">Rated %d+</string>
strings.xml:5381:    <string name="sale_main_header">Get %d%% Off Premium</string>
strings.xml:5591:    <string name="signing_up_includes_one_week_of_premium">"Signing Up Includes
strings.xml:5592:1 FREE Week of Premium"</string>
strings.xml:5610:    <string name="skills_first_point_coach_speech">You earned a skill point! Skill points are rewarded for good moves played in your games. Level up to unlock more skills!</string>
strings.xml:5619:    <string name="skills_new_skill_unlocked">New Skill Unlocked</string>
strings.xml:5620:    <string name="skills_new_skills_unlocked">New Skills Unlocked</string>
strings.xml:5673:    <string name="spring_sale_discount_long">Get 50% Off Premium</string>
strings.xml:5680:    <string name="standing_position_of_max">\#%1$d (%2$d Players)</string>
strings.xml:5687:    <string name="start_free_trial">Start Free Trial</string>
strings.xml:5758:    <string name="subscriptions">Subscriptions</string>
strings.xml:5971:    <string name="title_activity_video_interstitial_go_premium">VideoInterstitialGoPremiumActivity</string>
strings.xml:6050:    <string name="tournament_title_3_2_premium_blitz">3|2 Premium Blitz</string>
strings.xml:6055:    <string name="tournament_title_5_5_premium_blitz">5|5 Premium Blitz</string>
strings.xml:6143:    <string name="trial_premium_free">Try Premium free. As little as $5/month after.</string>
strings.xml:6144:    <string name="trial_premium_free_7_days">Try Premium free for 7 days. As low as %1$s/month after.</string>
strings.xml:6145:    <string name="trial_premium_free_month">Get 1 Month of Premium for Free</string>
strings.xml:6146:    <string name="trial_premium_free_week">Get 1 Week of Premium for Free</string>
strings.xml:6154:    <string name="try_premium">Try Premium</string>
strings.xml:6202:    <string name="unlimited_max_analysis">Unlimited Maximum Analysis</string>
strings.xml:6212:    <string name="unlock_all_bots">Unlock All Bots</string>
strings.xml:6213:    <string name="unlock_all_bots_description">Over 130 different personalities to choose from.</string>
strings.xml:6214:    <string name="unlock_all_drills">Unlock All Drills</string>
strings.xml:6215:    <string name="unlock_all_lessons">Unlock All Lessons</string>
strings.xml:6216:    <string name="unlock_all_of_premium_description">Including unlimited Game Review, Puzzles, Lessons, Bots, and more.</string>
strings.xml:6217:    <string name="unlock_all_of_premium_title">Unlock All of Premium</string>
strings.xml:6218:    <string name="unlock_all_positions">Unlock All Positions</string>
strings.xml:6219:    <string name="unlock_all_tactics">Unlock All Tactics</string>
strings.xml:6220:    <string name="unlock_all_videos">Unlock All Videos</string>
strings.xml:6221:    <string name="unlock_everything_to_improve">Unlock everything to improve!</string>
strings.xml:6222:    <string name="unlock_full_access">Unlock Full Access</string>
strings.xml:6223:    <string name="unlock_opening_explorer">Unlock Opening Explorer</string>
strings.xml:6224:    <string name="unlock_your_potential">Unlock your Potential</string>
strings.xml:6269:    <string name="upgrade_no_ads_disclaimer_android">Your No Ads Plan will renew automatically unless you cancel. You may cancel anytime in Google Play.</string>
strings.xml:6270:    <string name="upgrade_no_ads_disclaimer_ios">Your No Ads Plan will renew automatically unless you cancel. You may cancel anytime in the App Store.</string>
strings.xml:6293:    <string name="upgrade_sign_up_to_keep_unlock_lessons">Sign up to unlock Lessons.</string>
strings.xml:6296:    <string name="upgrade_subtitle_try_premium_for_free">Try Premium for Free</string>
strings.xml:6299:    <string name="upgrade_title_drills">Upgrade Now to Unlock All Drills</string>
strings.xml:6303:    <string name="upgrade_title_key_positions">Upgrade Now to Unlock All Key Positions</string>
strings.xml:6309:    <string name="upgrade_to_premium">Upgrade to Premium</string>
strings.xml:6313:    <string name="upgrade_unlock_all_bots">Unlock All Bots</string>
strings.xml:6314:    <string name="upgrade_unlock_all_daily_puzzles">Unlock All Daily Puzzles</string>
strings.xml:6315:    <string name="upgrade_unlock_puzzle_explanations">Unlock Puzzle Explanations</string>
strings.xml:6316:    <string name="upgrade_unlock_puzzles_lessons_more">Unlock Puzzles, Lessons, and more!</string>
strings.xml:6317:    <string name="upgrade_unlock_with_premium">Unlock with Premium</string>
strings.xml:6396:    <string name="username_should_have_max_characters_or_less">Username should have 25 characters or less.</string>
strings.xml:6482:    <string name="vs_comp_bot_strength_max">Maximum</string>
strings.xml:6483:    <string name="vs_comp_bot_strength_super_gm">Super Grandmaster</string>
strings.xml:6539:    <string name="vs_comp_unlock_dialog_caption">Play vs various skills and styles</string>
strings.xml:6540:    <string name="vs_comp_unlock_dialog_title">Want Unlimited Computer Bots?</string>
strings.xml:6541:    <string name="vs_comp_unlock_with_free_trial">Unlock with Free Trial</string>
strings.xml:6575:    <string name="watch_rewarded_video_game_review">Or Watch a Video to Unlock this Game Review</string>
strings.xml:6576:    <string name="watch_rewarded_video_lesson">Or Watch a Video to Unlock this Lesson</string>
strings.xml:6577:    <string name="watch_rewarded_video_rated_puzzles">Or Watch a Video to Unlock Another 3 Puzzles</string>
strings.xml:6606:    <string name="welcome_to_premium">Welcome to Premium</string>
strings.xml:6607:    <string name="welcome_to_premium_button">Enjoy Now</string>
strings.xml:6665:    <string name="winback_restart_premium_and_get">Restart Premium and Get</string>
strings.xml:6739:    <string name="you_have_reached_the_maximum_number_of_pending_friend_requests">You have reached the maximum number of pending friend requests.</string>
```

### data_copy — 74 strings

```
plurals.xml:413:    <plurals name="x_contacts_found">
plurals.xml:414:        <item quantity="other">%d Contacts Found</item>
plurals.xml:415:        <item quantity="zero">%d Contacts Found</item>
plurals.xml:417:        <item quantity="two">%d Contacts Found</item>
plurals.xml:418:        <item quantity="few">%d Contacts Found</item>
plurals.xml:419:        <item quantity="many">%d Contacts Found</item>
strings.xml:73:    <string name="access_blocked_at_location">Access to Chess.com is blocked at your location.</string>
strings.xml:512:    <string name="add_friends_through">Add friends through phone contacts, social, or username.</string>
strings.xml:650:    <string name="adv_stats_takeaway_paywall_strategy_2">Want more tips? Diamond members get Advanced Stats for a personalized look at how to improve their strategy.</string>
strings.xml:673:    <string name="all_contacts">All Contacts</string>
strings.xml:685:    <string name="allow_friends_to_find_you_via_contacts">Allow friends to find you via phone contacts</string>
strings.xml:739:    <string name="analysis_game_details_location">Location</string>
strings.xml:1146:    <string name="can_not_access_contacts">Cannot access Contacts</string>
strings.xml:1211:    <string name="catalyst_change_bundle_location">Change Bundle Location</string>
strings.xml:1212:    <string name="catalyst_change_bundle_location_apply">Apply Changes</string>
strings.xml:1213:    <string name="catalyst_change_bundle_location_cancel">Cancel</string>
strings.xml:1214:    <string name="catalyst_change_bundle_location_input_hint">127.0.0.1:8081</string>
strings.xml:1215:    <string name="catalyst_change_bundle_location_input_label">Provide a custom bundler address and port:</string>
strings.xml:1216:    <string name="catalyst_change_bundle_location_instructions">"You can connect either via USB (localhost - default) or Wifi. If you connect via USB and running with a physical device, make sure you:
strings.xml:1218: 2. Set the bundle location to `localhost:8081`
strings.xml:1309:    <string name="challenge_from_your_contacts">From Contacts</string>
strings.xml:1730:    <string name="connect_to_facebook_to_find_friends">Connect to Facebook to find friends.</string>
strings.xml:1732:    <string name="connect_with_friends_modal_body">"Sync your contacts with your phone number to see who's on %1$s."</string>
strings.xml:1772:    <string name="contacts">Contacts</string>
strings.xml:1773:    <string name="contacts_friends_title">"None of your contacts friends play on %1$s.
strings.xml:1775:    <string name="contacts_permission_description_clear_cta">For more on how your information is used to improve your experience, please read our &lt;a href=https://www.chess.com/legal/privacy>Privacy Policy&lt;/a>.</string>
strings.xml:2227:    <string name="edit_profile_location_field">@string/location</string>
strings.xml:2292:    <string name="err_ott_geoloc_callback_failure">failed to fetch Geolocation data</string>
strings.xml:2509:    <string name="find_contacts">Find Contacts</string>
strings.xml:2511:    <string name="find_friends">Find friends already using Chess.com</string>
strings.xml:2512:    <string name="find_friends_already_on_chesscom">Or, find friends already on Chess.com:</string>
strings.xml:2514:    <string name="find_friends_on_chesscom">Find Friends on %s</string>
strings.xml:2515:    <string name="find_friends_short">Find friends</string>
strings.xml:2516:    <string name="find_friends_short_">Find Friends</string>
strings.xml:2517:    <string name="find_friends_social">Find friends through social.</string>
strings.xml:2519:    <string name="find_friends_tap_allow">Tap Allow to sync your contacts and find people you know on %s</string>
strings.xml:2592:    <string name="friends_contacts_permission">Allow access to Contacts to invite your friends to play.</string>
strings.xml:2722:    <string name="game_review_eval_bar_location_left">Left</string>
strings.xml:2723:    <string name="game_review_eval_bar_location_setting">Eval Bar Location</string>
strings.xml:2724:    <string name="game_review_eval_bar_location_top">Top</string>
strings.xml:2813:    <string name="get_location_permission_confirm">Please provide a location permission for a better experience</string>
strings.xml:2880:    <string name="grant_access_to_contacts">Please grant access to \"Chess\" via iOS Settings > Privacy > Contacts.</string>
strings.xml:3017:    <string name="ic_contacts">o</string>
strings.xml:3142:    <string name="improve_your_game_with_personalized_advice">Improve your game with personalized advice</string>
strings.xml:3175:    <string name="intercom_access_background_location_message">Go to your device’s settings to enable the app to use your location in the background</string>
strings.xml:3176:    <string name="intercom_access_background_location_title">Allow access to your location all the time</string>
strings.xml:3408:    <string name="intercom_profile_location">{time} in {location}</string>
strings.xml:3701:    <string name="invite_from_contacts">Invite from Contacts</string>
strings.xml:3703:    <string name="invite_more_contacts">Invite More Contacts</string>
strings.xml:3925:    <string name="location">Location</string>
strings.xml:4342:    <string name="no_ads_found_for_location">No ads were found for your location</string>
strings.xml:4346:    <string name="no_contacts_found">No Contacts Found</string>
strings.xml:4401:    <string name="notification_contact_match_tooltip">A person from my phone contacts has joined %1$s.</string>
strings.xml:4464:    <string name="notification_settings_contact_signups">Contacts Signups</string>
strings.xml:4465:    <string name="notification_settings_contact_signups_description">Get notified when one of your contacts create an account</string>
strings.xml:4616:    <string name="offline_notification_title_with_advertiser">You are back online! Continue learning about %s</string>
strings.xml:4619:    <string name="offline_opt_in_message">"We'll send you a notification with a link to the advertiser site."</string>
strings.xml:4721:    <string name="otvc_disclaimer_body">"We don't recognize this device or location. This one-time verification helps to protect your account."</string>
strings.xml:4933:    <string name="premium_analysis_personalized_training">Personalized Training</string>
strings.xml:5051:    <string name="puzzle_difficulty_setting_description">All Difficulty options are personalized to your skill level.</string>
strings.xml:5398:    <string name="search_contacts">Search Contacts</string>
strings.xml:5399:    <string name="search_contacts_allow">Allow</string>
strings.xml:5400:    <string name="search_contacts_confirm">I accept, Search Contacts</string>
strings.xml:5401:    <string name="search_contacts_disclaimer">These contacts are already %s players</string>
strings.xml:5402:    <string name="search_contacts_no_thanks">@string/first_daily_move_no_thanks</string>
strings.xml:5403:    <string name="search_contacts_permission_explanation">In order to search your contacts, Chess.com will need to access your personal information. We ONLY use this information to search your contacts and do not share this with 3rd parties. Please see our com [... omitted end of lo
strings.xml:5404:    <string name="search_contacts_privacy_loading_failed">Failed to load Privacy Policy, tap here to read in an external browser.</string>
strings.xml:5405:    <string name="search_contacts_view_policy">View Policy</string>
strings.xml:5629:    <string name="social_setting_allow_friend_find_via_contacts">Allow friends to find you via contacts</string>
strings.xml:5954:    <string name="title_activity_search_contacts">SearchContactsActivity</string>
strings.xml:6583:    <string name="we_could_not_find_your_contacts">"We couldn't find any of your contacts on Chess.com. Invite some friends below."</string>
strings.xml:6585:    <string name="we_didnt_find_contacts">We didn’t find any contacts on %s</string>
strings.xml:6766:    <string name="your_contacts">Your Contacts</string>
strings.xml:6767:    <string name="your_contacts_will_be_used_by_chess_com_privacy_policy">Your contacts will be used by %s to improve your experience by allowing you to connect with your friends. For more information, please read our &lt;a href=https://www.chess.com/legal/pri [... omitted end of lo
```

