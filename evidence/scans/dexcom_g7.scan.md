# Pattern scan: work/dexcom_g7/jadx

## Code categories (library packages excluded)

### installed_apps — 0 hits in 0 files


```
```

### usage_stats — 2 hits in 1 files

- `androidx/core/content/ContextCompat.java` (2)

```
androidx/core/content/ContextCompat.java:16:import android.app.usage.UsageStatsManager;
androidx/core/content/ContextCompat.java:472:            map.put(UsageStatsManager.class, new String(iArr2, 0, i3));
```

### clipboard — 2 hits in 2 files

- `androidx/appcompat/widget/AppCompatReceiveContentHelper.java` (1)
- `androidx/compose/ui/platform/AndroidClipboardManager.java` (1)

```
androidx/appcompat/widget/AppCompatReceiveContentHelper.java:165:                    ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
androidx/compose/ui/platform/AndroidClipboardManager.java:60:                ClipData primaryClip = this.clipboardManager.getPrimaryClip();
```

### contacts — 4 hits in 1 files

- `ig/C1537.java` (4)

```
ig/C1537.java:6:import android.provider.ContactsContract;
ig/C1537.java:195:                        return ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uri2, true);
ig/C1537.java:201:                Uri uriLookupContact = ContactsContract.Contacts.lookupContact(contentResolver, uri2);
ig/C1537.java:203:                    return ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uriLookupContact, true);
```

### call_log — 0 hits in 0 files


```
```

### sms — 17 hits in 4 files

- `com/google/android/gms/internal/p001authapiphone/zzj.java` (5)
- `com/google/android/gms/auth/api/phone/SmsRetriever.java` (5)
- `com/google/android/gms/auth/api/phone/SmsRetrieverClient.java` (5)
- `com/google/android/gms/auth/api/phone/SmsRetrieverApi.java` (2)

```
com/google/android/gms/internal/p001authapiphone/zzj.java:6:import com.google.android.gms.auth.api.phone.SmsRetrieverClient;
com/google/android/gms/internal/p001authapiphone/zzj.java:11:public final class zzj extends SmsRetrieverClient {
com/google/android/gms/internal/p001authapiphone/zzj.java:31:    @Override // com.google.android.gms.auth.api.phone.SmsRetrieverClient, com.google.android.gms.auth.api.phone.SmsRetrieverApi
com/google/android/gms/internal/p001authapiphone/zzj.java:32:    public final Task<Void> startSmsRetriever() {
com/google/android/gms/internal/p001authapiphone/zzj.java:36:    @Override // com.google.android.gms.auth.api.phone.SmsRetrieverClient, com.google.android.gms.common.api.GoogleApi, com.google.android.gms.common.api.HasApiKey
com/google/android/gms/auth/api/phone/SmsRetrieverApi.java:6:public interface SmsRetrieverApi {
com/google/android/gms/auth/api/phone/SmsRetrieverApi.java:7:    Task<Void> startSmsRetriever();
com/google/android/gms/auth/api/phone/SmsRetriever.java:17:public final class SmsRetriever {
com/google/android/gms/auth/api/phone/SmsRetriever.java:77:    public static SmsRetrieverClient getClient(@NonNull Activity activity) {
com/google/android/gms/auth/api/phone/SmsRetriever.java:78:        return (SmsRetrieverClient) m36020(854483, activity);
com/google/android/gms/auth/api/phone/SmsRetriever.java:81:    public static SmsRetrieverClient getClient(@NonNull Context context) {
com/google/android/gms/auth/api/phone/SmsRetriever.java:82:        return (SmsRetrieverClient) m36020(427244, context);
```

### location — 66 hits in 19 files

- `androidx/core/location/LocationManagerCompat.java` (14)
- `com/google/android/gms/location/FusedLocationProviderClient.java` (8)
- `com/google/android/gms/location/LocationServices.java` (6)
- `androidx/appcompat/app/TwilightManager.java` (5)
- `com/dexcom/dexcomone/utils/CountryOfResidenceService.java` (4)
- `com/google/android/gms/internal/location/zzq.java` (4)
- `com/google/android/gms/internal/location/zzaf.java` (4)
- `com/google/android/gms/location/FusedLocationProviderApi.java` (4)
- `com/google/android/gms/location/zzn.java` (3)
- `com/google/android/gms/location/zzo.java` (3)
- `com/google/android/gms/location/GeofencingClient.java` (2)
- `com/google/android/gms/location/GeofencingApi.java` (2)

```
androidx/appcompat/app/TwilightManager.java:60:    private Location getLastKnownLocation() {
androidx/appcompat/app/TwilightManager.java:66:    private Location getLastKnownLocationForProvider(String str) {
androidx/appcompat/app/TwilightManager.java:95:                    Location lastKnownLocation = getLastKnownLocation();
androidx/appcompat/app/TwilightManager.java:142:                    lastKnownLocationForProvider = getLastKnownLocationForProvider(new String(iArr2, 0, i6));
androidx/appcompat/app/TwilightManager.java:181:                    lastKnownLocationForProvider2 = getLastKnownLocationForProvider(new String(iArr4, 0, i9));
androidx/core/location/LocationManagerCompat.java:283:        public static void getCurrentLocation(LocationManager locationManager, @NonNull String str, @Nullable CancellationSignal cancellationSignal, @NonNull Executor executor, @NonNull Consumer<Location> consumer) throws IllegalAccessException, 
androidx/core/location/LocationManagerCompat.java:316:                    locationManager.getCurrentLocation(str, cancellationSignal2, executor, new java.util.function.Consumer() { // from class: androidx.core.location.g
androidx/core/location/LocationManagerCompat.java:392:        public static void requestLocationUpdates(LocationManager locationManager, @NonNull String str, @NonNull LocationRequest locationRequest, @NonNull Executor executor, @NonNull LocationListener locationListener) {
androidx/core/location/LocationManagerCompat.java:393:            locationManager.requestLocationUpdates(str, locationRequest, executor, locationListener);
androidx/core/location/LocationManagerCompat.java:1601:    public static void getCurrentLocation(@NonNull LocationManager locationManager, @NonNull String str, @Nullable CancellationSignal cancellationSignal, @NonNull Executor executor, @NonNull Consumer<Location> consumer) throws IllegalAccessExcep
androidx/core/location/LocationManagerCompat.java:1819:    public static void requestLocationUpdates(@NonNull LocationManager locationManager, @NonNull String str, @NonNull LocationRequestCompat locationRequestCompat, @NonNull LocationListenerCompat locationListenerCompat, @NonNull Looper looper) th
androidx/core/location/LocationManagerCompat.java:1825:    public static void requestLocationUpdates(@NonNull LocationManager locationManager, @NonNull String str, @NonNull LocationRequestCompat locationRequestCompat, @NonNull Executor executor, @NonNull LocationListenerCompat locationListenerCompat
```

### wifi_bt_scan — 20 hits in 9 files

- `com/dexcom/coresdk/transmitterG7/G7TxController.java` (4)
- `com/dexcom/coresdk/blecommunication/Scanner$$ExternalSyntheticApiModelOutline0.java` (4)
- `ig/C6570.java` (2)
- `com/dexcom/coresdk/blecommunication/Scanner$$ExternalSyntheticApiModelOutline1.java` (2)
- `com/dexcom/coresdk/blecommunication/Scanner$$ExternalSyntheticApiModelOutline2.java` (2)
- `com/dexcom/coresdk/transmitter/G6TxController.java` (2)
- `ig/C5539.java` (2)
- `com/dexcom/coresdk/blecommunication/BleManager.java` (1)
- `ig/C3482.java` (1)

```
ig/C6570.java:111:                int iStartScan = this.f48133.f42576.getBluetoothLeScanner().startScan(this.f48131.m50637(c12285Arr), this.f48131.m50638(c6411), pendingIntent);
ig/C6570.java:154:                    this.f48133.f42576.getBluetoothLeScanner().stopScan(pendingIntent2);
com/dexcom/coresdk/transmitterG7/G7TxController.java:1415:                ((G7TxController) objArr[0]).startScan((String) objArr[1]);
com/dexcom/coresdk/transmitterG7/G7TxController.java:2296:                            g7TxController.bleManager.startScan((String) objArr[0]);
com/dexcom/coresdk/transmitterG7/G7TxController.java:2332:                g7TxController.startScan(null);
com/dexcom/coresdk/transmitterG7/G7TxController.java:3266:                            g7TxController.bleManager.startScan(null);
com/dexcom/coresdk/blecommunication/Scanner$$ExternalSyntheticApiModelOutline1.java:3:import android.bluetooth.le.BluetoothLeScanner;
com/dexcom/coresdk/blecommunication/Scanner$$ExternalSyntheticApiModelOutline1.java:17:        ((BluetoothLeScanner) objArr[0]).startScan((List<ScanFilter>) objArr[1], (ScanSettings) objArr[2], (ScanCallback) objArr[3]);
com/dexcom/coresdk/blecommunication/Scanner$$ExternalSyntheticApiModelOutline2.java:3:import android.bluetooth.le.BluetoothLeScanner;
com/dexcom/coresdk/blecommunication/Scanner$$ExternalSyntheticApiModelOutline2.java:14:        ((BluetoothLeScanner) objArr[0]).stopScan((ScanCallback) objArr[1]);
com/dexcom/coresdk/blecommunication/BleManager.java:1671:                        this.f491.startScan(arrayList, BleManager$$ExternalSyntheticApiModelOutline5.m(builder));
com/dexcom/coresdk/blecommunication/Scanner$$ExternalSyntheticApiModelOutline0.java:4:import android.bluetooth.le.BluetoothLeScanner;
```

### device_ids — 41 hits in 27 files

- `androidx/core/telephony/TelephonyManagerCompat.java` (6)
- `com/dexcom/coresdk/cgmkit/pendataservice/PenDataService.java` (4)
- `org/spongycastle/x509/AttributeCertificateHolder.java` (2)
- `org/spongycastle/cert/AttributeCertificateHolder.java` (2)
- `com/dexcom/coresdk/cgmkit/systemservice/eventsdataservice/DisplayableEvent.java` (2)
- `com/dexcom/coresdk/cgmkit/persistence/daos/PenDoseDao_Impl.java` (2)
- `com/dexcom/coresdk/cgmkit/persistence/repositories/PenDoseRepository.java` (2)
- `androidx/compose/ui/platform/AndroidComposeView.java` (2)
- `org/spongycastle/tsp/TimeStampToken.java` (1)
- `com/dexcom/coresdk/cgmkit/pendataservice/models/DeviceInfo.java` (1)
- `com/dexcom/coresdk/cgmkit/pendataservice/models/RecallResponse.java` (1)
- `com/dexcom/coresdk/cgmkit/pendataservice/models/PenDeviceSettingsRequest.java` (1)

```
org/spongycastle/tsp/TimeStampToken.java:318:                        if (!this.certID.getIssuerSerial().getSerial().equals(issuerAndSerialNumber.getSerialNumber())) {
com/dexcom/coresdk/cgmkit/pendataservice/PenDataService.java:978:                String deviceId = penDose.getDeviceId();
com/dexcom/coresdk/cgmkit/pendataservice/PenDataService.java:1029:                    str = penDose.getDeviceManufacturer().name() + penDose.getActionType().name() + penDose.getDeviceId() + penDose.getMedicationType().name();
com/dexcom/coresdk/cgmkit/pendataservice/PenDataService.java:1034:                        String deviceId2 = penDose.getDeviceId();
com/dexcom/coresdk/cgmkit/pendataservice/PenDataService.java:1054:                        String deviceId3 = penDose.getDeviceId();
com/dexcom/coresdk/cgmkit/pendataservice/models/DeviceInfo.java:50:    public final String getDeviceId() {
com/dexcom/coresdk/cgmkit/pendataservice/models/RecallResponse.java:99:    public final String getDeviceId() {
com/dexcom/coresdk/cgmkit/pendataservice/models/PenDeviceSettingsRequest.java:54:    public final String getDeviceId() {
com/dexcom/coresdk/cgmkit/pendataservice/models/PenDose.java:1811:    public final String getDeviceId() {
com/dexcom/coresdk/cgmkit/pendataservice/util/PenPrimingAlgorithm.java:93:            } else if (!Intrinsics.areEqual(penDose.getDeviceId(), penDose2.getDeviceId()) || !Intrinsics.areEqual(penDose.getMedication(), penDose2.getMedication()) || !Intrinsics.areEqual(penDose.getMedicationLong(), penDose
com/dexcom/coresdk/cgmkit/cloudservices/bulkdata/BulkDataManagerKt.java:233:                String deviceId = penDose.getDeviceId();
org/spongycastle/x509/AttributeCertificateIssuer.java:138:                        } else if (v2Form.getBaseCertificateID().getSerial().getValue().equals(x509Certificate.getSerialNumber()) && matchesDN(x509Certificate.getIssuerX500Principal(), v2Form.getBaseCertificateID().getIssuer())) {
```

### gsf_id — 0 hits in 0 files


```
```

### advertising_id — 18 hits in 4 files

- `com/google/android/gms/ads/identifier/AdvertisingIdClient.java` (9)
- `com/google/android/gms/measurement/internal/zzfb.java` (4)
- `com/google/android/gms/measurement/internal/zzjg.java` (4)
- `com/google/android/gms/ads/identifier/zza.java` (1)

```
com/google/android/gms/measurement/internal/zzfb.java:8:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
com/google/android/gms/measurement/internal/zzfb.java:331:                AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);
com/google/android/gms/measurement/internal/zzfb.java:333:                    AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.zzs.zzax());
com/google/android/gms/measurement/internal/zzfb.java:367:                AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);
com/google/android/gms/measurement/internal/zzjg.java:5:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
com/google/android/gms/measurement/internal/zzjg.java:173:                AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);
com/google/android/gms/measurement/internal/zzjg.java:175:                    AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.zzs.zzax());
com/google/android/gms/measurement/internal/zzjg.java:188:                AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);
com/google/android/gms/ads/identifier/zza.java:25:    public zza(AdvertisingIdClient advertisingIdClient, Map map) {
com/google/android/gms/ads/identifier/AdvertisingIdClient.java:58:public class AdvertisingIdClient {
com/google/android/gms/ads/identifier/AdvertisingIdClient.java:141:        public WeakReference<AdvertisingIdClient> zzm;
com/google/android/gms/ads/identifier/AdvertisingIdClient.java:146:        public zza(AdvertisingIdClient advertisingIdClient, long j) {
```

### install_referrer — 0 hits in 0 files


```
```

### sensors — 2 hits in 2 files

- `androidx/health/connect/client/records/SleepStageRecord.java` (1)
- `androidx/health/connect/client/records/SleepSessionRecord.java` (1)

```
androidx/health/connect/client/records/SleepStageRecord.java:55:    public static final int STAGE_TYPE_LIGHT = 4;
androidx/health/connect/client/records/SleepSessionRecord.java:69:    public static final int STAGE_TYPE_LIGHT = 4;
```

### accounts — 5 hits in 3 files

- `com/google/android/gms/measurement/internal/zzam.java` (3)
- `com/android/volley/toolbox/AndroidAuthenticator.java` (1)
- `com/google/android/gms/auth/zzd.java` (1)

```
com/android/volley/toolbox/AndroidAuthenticator.java:46:        this(AccountManager.get(context), account, str, z);
com/google/android/gms/measurement/internal/zzam.java:140:                            this.zzc = AccountManager.get(this.zzs.zzax());
com/google/android/gms/measurement/internal/zzam.java:163:                            Account[] result = accountManager.getAccountsByTypeAndFeatures(strM74819, new String[]{new String(iArr2, 0, i13)}, null, null).getResult();
com/google/android/gms/measurement/internal/zzam.java:179:                                Account[] result2 = accountManager2.getAccountsByTypeAndFeatures(strM74819, new String[]{new String(iArr3, 0, i17)}, null, null).getResult();
com/google/android/gms/auth/zzd.java:401:                AccountManager accountManager = AccountManager.get(context6);
```

### battery_state — 3 hits in 2 files

- `com/dexcom/coresdk/cgmkit/systemservice/CgmEngine.java` (2)
- `com/dexcom/coresdk/cgmkit/osservices/devicebattery/models/DeviceBatteryStatus.java` (1)

```
com/dexcom/coresdk/cgmkit/systemservice/CgmEngine.java:1440:                                                            if (deviceBatteryStatusCalculateBatteryStatus.isCharging()) {
com/dexcom/coresdk/cgmkit/systemservice/CgmEngine.java:1449:                                                        if (deviceBatteryStatusCalculateBatteryStatus.isCharging()) {
com/dexcom/coresdk/cgmkit/osservices/devicebattery/models/DeviceBatteryStatus.java:228:    public final boolean isCharging() {
```

### screen_capture_detect — 0 hits in 0 files


```
```

### audio_capture — 7 hits in 2 files

- `com/dexcom/phoenixuikit/uikit/SpeechToTextParser.java` (6)
- `androidx/camera/core/VideoCapture.java` (1)

```
androidx/camera/core/VideoCapture.java:1242:                audioRecord = new AudioRecord(audioRecordSource, this.mAudioSampleRate, i, s, minBufferSize * 2);
com/dexcom/phoenixuikit/uikit/SpeechToTextParser.java:7:import android.speech.SpeechRecognizer;
com/dexcom/phoenixuikit/uikit/SpeechToTextParser.java:49:    public final SpeechRecognizer speechRecognizer;
com/dexcom/phoenixuikit/uikit/SpeechToTextParser.java:63:        SpeechRecognizer speechRecognizerCreateSpeechRecognizer = SpeechRecognizer.createSpeechRecognizer(context);
com/dexcom/phoenixuikit/uikit/SpeechToTextParser.java:74:        Intrinsics.checkNotNullExpressionValue(speechRecognizerCreateSpeechRecognizer, new String(iArr, 0, s));
com/dexcom/phoenixuikit/uikit/SpeechToTextParser.java:75:        this.speechRecognizer = speechRecognizerCreateSpeechRecognizer;
com/dexcom/phoenixuikit/uikit/SpeechToTextParser.java:103:                if (!SpeechRecognizer.isRecognitionAvailable(this.context)) {
```

### accessibility — 202 hits in 30 files

- `androidx/core/view/accessibility/AccessibilityManagerCompat.java` (28)
- `androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java` (28)
- `com/google/android/material/search/SearchBar.java` (16)
- `com/google/android/material/textfield/DropdownMenuEndIconDelegate.java` (12)
- `com/google/android/material/textfield/MaterialAutoCompleteTextView.java` (9)
- `com/google/android/material/textfield/EndCompoundLayout.java` (9)
- `androidx/compose/material3/Listener.java` (9)
- `com/google/android/material/bottomsheet/BottomSheetDragHandleView.java` (8)
- `androidx/compose/ui/platform/CompositionLocalsKt.java` (8)
- `androidx/compose/material/SnackbarHostKt.java` (6)
- `androidx/compose/ui/platform/AndroidComposeView.java` (6)
- `androidx/compose/ui/platform/AndroidAccessibilityManager.java` (6)

```
com/google/android/material/snackbar/BaseTransientBottomBar.java:30:import android.view.accessibility.AccessibilityManager;
com/google/android/material/snackbar/BaseTransientBottomBar.java:96:    public final AccessibilityManager accessibilityManager;
com/google/android/material/snackbar/BaseTransientBottomBar.java:1006:        this.accessibilityManager = (AccessibilityManager) context.getSystemService(new String(iArr2, 0, i4));
com/google/android/material/snackbar/BaseTransientBottomBar.java:1500:                AccessibilityManager accessibilityManager = this.accessibilityManager;
com/google/android/material/snackbar/BaseTransientBottomBar.java:1502:                if (accessibilityManager != null && ((enabledAccessibilityServiceList = accessibilityManager.getEnabledAccessibilityServiceList(1)) == null || !enabledAccessibilityServiceList.isEmpty())) {
com/google/android/material/snackbar/Snackbar.java:14:import android.view.accessibility.AccessibilityManager;
com/google/android/material/snackbar/Snackbar.java:40:    public final AccessibilityManager accessibilityManager;
com/google/android/material/snackbar/Snackbar.java:218:        this.accessibilityManager = (AccessibilityManager) context2.getSystemService(new String(iArr, 0, s2));
com/google/android/material/textfield/MaterialAutoCompleteTextView.java:15:import android.view.accessibility.AccessibilityManager;
com/google/android/material/textfield/MaterialAutoCompleteTextView.java:47:    public final AccessibilityManager accessibilityManager;
com/google/android/material/textfield/MaterialAutoCompleteTextView.java:188:        this.accessibilityManager = (AccessibilityManager) context2.getSystemService(new String(iArr, 0, s3));
com/google/android/material/textfield/MaterialAutoCompleteTextView.java:258:    private boolean isTouchExplorationEnabled() {
```

### root_emulator — 329 hits in 41 files

- `androidx/compose/material3/ExposedDropdownMenu_androidKt.java` (49)
- `androidx/compose/material/ExposedDropdownMenu_androidKt.java` (37)
- `androidx/compose/material/internal/ExposedDropdownMenuPopup_androidKt.java` (27)
- `androidx/compose/material3/internal/ExposedDropdownMenuPopup_androidKt.java` (24)
- `androidx/compose/material/ExposedDropdownMenuBoxScope.java` (21)
- `com/dexcom/g7/R.java` (17)
- `androidx/compose/material3/ExposedDropdownMenuBoxScope.java` (15)
- `com/dexcom/phoenixuikit/uikit/R.java` (14)
- `com/google/android/material/R.java` (14)
- `androidx/compose/material/ExposedDropdownMenuDefaults.java` (14)
- `com/qualtrics/R.java` (8)
- `com/google/firebase/crashlytics/internal/model/AutoValue_StaticSessionData_OsData.java` (7)

```
com/qualtrics/R.java:1470:        public static final int mtrl_exposed_dropdown_menu_popup_elevation = 0x7f070303;
com/qualtrics/R.java:1471:        public static final int mtrl_exposed_dropdown_menu_popup_vertical_offset = 0x7f070304;
com/qualtrics/R.java:1472:        public static final int mtrl_exposed_dropdown_menu_popup_vertical_padding = 0x7f070305;
com/qualtrics/R.java:2326:        public static final int exposed_dropdown_menu_content_description = 0x7f140322;
com/qualtrics/R.java:3093:        public static final int Widget_MaterialComponents_TextInputLayout_FilledBox_Dense_ExposedDropdownMenu = 0x7f150527;
com/qualtrics/R.java:3094:        public static final int Widget_MaterialComponents_TextInputLayout_FilledBox_ExposedDropdownMenu = 0x7f150528;
com/qualtrics/R.java:3097:        public static final int Widget_MaterialComponents_TextInputLayout_OutlinedBox_Dense_ExposedDropdownMenu = 0x7f15052b;
com/qualtrics/R.java:3098:        public static final int Widget_MaterialComponents_TextInputLayout_OutlinedBox_ExposedDropdownMenu = 0x7f15052c;
com/dexcom/coresdk/cgmkit/cloudservices/settingssyncmanager/models/SimpleAlertSchedule.java:8:@Metadata(d1 = {"\u0000,\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0010\t\n\u0002\b\t\n\u0002\u0010\u000e\n\u0002\b
com/dexcom/coresdk/cgmkit/cloudservices/settingssyncmanager/models/SimpleAlertSchedule.java:24:    @SerializedName("fridayEnabled")
com/dexcom/coresdk/cgmkit/cloudservices/settingssyncmanager/models/SimpleAlertSchedule.java:25:    public final boolean fridayEnabled;
com/dexcom/coresdk/cgmkit/cloudservices/settingssyncmanager/models/SimpleAlertSchedule.java:67:                z = this.fridayEnabled;
```

### js_bridge — 2 hits in 2 files

- `com/dexcom/phoenix/ui/legal/WebLegalActivity.java` (1)
- `com/qualtrics/digital/QualtricsSurveyFragment.java` (1)

```
com/dexcom/phoenix/ui/legal/WebLegalActivity.java:333:                webView.addJavascriptInterface(webLegalResponseChecker, C7891.m67646("??Q;FC\u0016B7D@93", sM64320, (short) ((iM643203 | (-12984)) & ((~iM643203) | (~(-12984))))));
com/qualtrics/digital/QualtricsSurveyFragment.java:506:                webView3.addJavascriptInterface(webViewInterface, new String(iArr5, 0, s14));
```

### boot_persist — 15 hits in 8 files

- `androidx/core/app/AlarmManagerCompat.java` (8)
- `com/dexcom/coresdk/cgmkit/utils/AlarmManagerEventFactory$buildEvent$1$$ExternalSyntheticApiModelOutline1.java` (1)
- `com/dexcom/phoenix/system/heartbeat/HeartbeatProvider.java` (1)
- `com/dexcom/phoenix/system/AlertAlarmProvider.java` (1)
- `com/dexcom/phoenix/ui/screens/settings/alerts/schedule/AlertProfileScheduleAlarmProvider.java` (1)
- `com/dexcom/phoenix/util/alerts/TimeChangeBroadcastReceiver.java` (1)
- `ig/C4194.java` (1)
- `ig/C0274.java` (1)

```
com/dexcom/coresdk/cgmkit/utils/AlarmManagerEventFactory$buildEvent$1$$ExternalSyntheticApiModelOutline1.java:14:        ((AlarmManager) objArr[0]).setExactAndAllowWhileIdle(((Integer) objArr[1]).intValue(), ((Long) objArr[2]).longValue(), (PendingIntent) objArr[3]);
androidx/core/app/AlarmManagerCompat.java:40:        public static void setAlarmClock(AlarmManager alarmManager, Object obj, PendingIntent pendingIntent) {
androidx/core/app/AlarmManagerCompat.java:50:                    ((AlarmManager) objArr[0]).setAlarmClock((AlarmManager.AlarmClockInfo) objArr[1], (PendingIntent) objArr[2]);
androidx/core/app/AlarmManagerCompat.java:66:        public static void setExactAndAllowWhileIdle(AlarmManager alarmManager, int i, long j, PendingIntent pendingIntent) {
androidx/core/app/AlarmManagerCompat.java:77:                    ((AlarmManager) objArr[0]).setExactAndAllowWhileIdle(((Integer) objArr[1]).intValue(), ((Long) objArr[2]).longValue(), (PendingIntent) objArr[3]);
androidx/core/app/AlarmManagerCompat.java:86:    public static void setAlarmClock(@NonNull AlarmManager alarmManager, long j, @NonNull PendingIntent pendingIntent, @NonNull PendingIntent pendingIntent2) {
androidx/core/app/AlarmManagerCompat.java:98:    public static void setExactAndAllowWhileIdle(@NonNull AlarmManager alarmManager, int i, long j, @NonNull PendingIntent pendingIntent) {
androidx/core/app/AlarmManagerCompat.java:109:                Api21Impl.setAlarmClock(alarmManager, Api21Impl.createAlarmClockInfo(jLongValue, pendingIntent), (PendingIntent) objArr[3]);
androidx/core/app/AlarmManagerCompat.java:118:                Api23Impl.setExactAndAllowWhileIdle((AlarmManager) objArr[0], ((Integer) objArr[1]).intValue(), ((Long) objArr[2]).longValue(), (PendingIntent) objArr[3]);
com/dexcom/phoenix/system/heartbeat/HeartbeatProvider.java:159:                    alarmManager.setExactAndAllowWhileIdle(0, time, broadcast2);
com/dexcom/phoenix/system/AlertAlarmProvider.java:68:                    alarmManager.setExactAndAllowWhileIdle(0, date.getTime(), broadcast);
com/dexcom/phoenix/ui/screens/settings/alerts/schedule/AlertProfileScheduleAlarmProvider.java:325:                    alarmManager.setExactAndAllowWhileIdle(0, jLongValue, pendingIntent);
```

### full_screen_intent — 3 hits in 2 files

- `androidx/core/app/NotificationCompat.java` (2)
- `androidx/core/app/NotificationCompatBuilder.java` (1)

```
androidx/core/app/NotificationCompatBuilder.java:490:        deleteIntent.setFullScreenIntent(pendingIntent, (i3 + 128) - (i3 | 128) != 0).setNumber(builder.mNumber).setProgress(builder.mProgressMax, builder.mProgress, builder.mProgressIndeterminate);
androidx/core/app/NotificationCompat.java:2626:            Builder shortcutId = setContentTitle(NotificationCompat.getContentTitle(notification)).setContentText(NotificationCompat.getContentText(notification)).setContentInfo(NotificationCompat.getContentInfo(notification)).setSubText(NotificationCom
androidx/core/app/NotificationCompat.java:3671:        public Builder setFullScreenIntent(@Nullable PendingIntent pendingIntent, boolean z) {
```

### health_connect — 416 hits in 34 files

- `androidx/health/connect/client/impl/HealthConnectClientUpsideDownImpl.java` (82)
- `androidx/health/connect/client/impl/HealthConnectClientImpl.java` (51)
- `androidx/health/connect/client/impl/platform/records/RecordConvertersKt.java` (50)
- `com/dexcom/coresdk/cgmkit/health/HealthDataService.java` (36)
- `androidx/health/connect/client/HealthConnectClient.java` (27)
- `androidx/health/connect/client/impl/converters/records/RecordToProtoConvertersKt.java` (13)
- `androidx/health/connect/client/impl/HealthConnectClientUpsideDownImpl$readRecords$response$1.java` (12)
- `androidx/health/connect/client/impl/platform/records/RequestConvertersKt.java` (12)
- `androidx/health/connect/client/impl/converters/request/ReadDataRangeRequestToProtoKt.java` (11)
- `androidx/health/connect/client/impl/HealthConnectClientUpsideDownImpl$readRecord$response$1.java` (8)
- `androidx/health/connect/client/impl/converters/records/ProtoToRecordConvertersKt.java` (7)
- `androidx/health/connect/client/impl/HealthConnectClientUpsideDownImpl$insertRecords$response$1.java` (7)

```
com/dexcom/coresdk/cgmkit/eventlogger/EventLogger$readRecordsFromTime$2.java:26:@DebugMetadata(c = "com.dexcom.coresdk.cgmkit.eventlogger.EventLogger$readRecordsFromTime$2", f = "EventLogger.kt", i = {}, l = {C7206.f52853, 132}, m = "invokeSuspend", n = {}, s = {})
com/dexcom/coresdk/cgmkit/eventlogger/EventLogger$readRecordsFromTime$2.java:28:public final class EventLogger$readRecordsFromTime$2 extends SuspendLambda implements Function2<CoroutineScope, Continuation<? super List<? extends EventLog>>, Object> {
com/dexcom/coresdk/cgmkit/eventlogger/EventLogger$readRecordsFromTime$2.java:43:    public EventLogger$readRecordsFromTime$2(EventLogger eventLogger, long j, long j2, Continuation<? super EventLogger$readRecordsFromTime$2> continuation) {
com/dexcom/coresdk/cgmkit/eventlogger/EventLogger$readRecordsFromTime$2.java:54:            return ((EventLogger$readRecordsFromTime$2) create((CoroutineScope) objArr[0], (Continuation) objArr[1])).invokeSuspend(Unit.INSTANCE);
com/dexcom/coresdk/cgmkit/eventlogger/EventLogger$readRecordsFromTime$2.java:61:            return new EventLogger$readRecordsFromTime$2(this.f1563, this.f1562, this.f1561, (Continuation) objArr[1]);
com/dexcom/coresdk/cgmkit/eventlogger/EventLogger.java:53:@Metadata(d1 = {"\u0000d\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b
com/dexcom/coresdk/cgmkit/eventlogger/EventLogger.java:593:                    return BuildersKt.withContext(eventLogger.dispatcher, new EventLogger$readRecordsFromTime$2(eventLogger, ((Long) objArr[0]).longValue(), System.currentTimeMillis(), null), (Continuation) objArr[1]);
com/dexcom/coresdk/cgmkit/eventlogger/EventLogger.java:818:    public final Object readRecordsFromTime$phoenixsdk_production(long j, @NotNull Continuation<? super List<? extends EventLog>> continuation) {
ig/C2514.java:3:import androidx.health.connect.client.HealthConnectClient;
ig/C2514.java:9:public final class C2514 extends Lambda implements Function0<HealthConnectClient> {
ig/C2514.java:25:                return HealthConnectClient.Companion.getOrCreate$default(HealthConnectClient.Companion, this.f20578.f78301, null, 2, null);
ig/C2514.java:31:    /* JADX WARN: Type inference failed for: r0v3, types: [androidx.health.connect.client.HealthConnectClient, java.lang.Object] */
```

### keystroke_text_capture — 76 hits in 32 files

- `androidx/core/widget/TextViewKt.java` (20)
- `androidx/databinding/adapters/TextViewBindingAdapter.java` (10)
- `androidx/appcompat/widget/SearchView.java` (4)
- `androidx/emoji2/text/SpannableBuilder.java` (3)
- `com/dexcom/phoenix/ui/screens/events/editevent/insulin/InsulinEventEditFragment.java` (2)
- `com/dexcom/phoenix/ui/screens/events/editevent/glucose/BloodGlucoseEditFragment.java` (2)
- `com/dexcom/phoenix/ui/screens/events/addevent/logmeal/LogMealFragment.java` (2)
- `com/google/android/material/textfield/TextInputLayout.java` (2)
- `com/google/android/material/button/MaterialButton.java` (2)
- `com/google/android/material/datepicker/RangeDateSelector.java` (2)
- `com/google/android/material/search/SearchView.java` (2)
- `com/google/android/material/timepicker/ChipTextInputComboView.java` (2)

```
ig/C11933.java:311:    public void onTextChanged(@Nullable("") CharSequence charSequence, int i, int i2, int i3) {
ig/C2687.java:97:    public void onTextChanged(@Nullable("") CharSequence charSequence, int i, int i2, int i3) {
ig/C3911.java:85:    public void onTextChanged(@Nullable("") CharSequence charSequence, int i, int i2, int i3) {
ig/C1211.java:73:    public void onTextChanged(@Nullable("") CharSequence charSequence, int i, int i2, int i3) {
ig/C10567.java:86:    public void onTextChanged(@Nullable("") CharSequence charSequence, int i, int i2, int i3) {
com/dexcom/phoenix/ui/screens/insulinpen/editdevicename/G7PensEditDeviceNameFragment.java:255:                editText3.addTextChangedListener(new C8617(booleanRef2, this));
ig/C6930.java:63:    public void onTextChanged(@Nullable("") CharSequence charSequence, int i, int i2, int i3) {
com/dexcom/phoenix/ui/screens/settings/alerts/profile/AddNewProfileDialog.java:261:                                editText.addTextChangedListener(new C6930(addNewProfileDialog));
com/dexcom/phoenix/ui/screens/events/editevent/insulin/InsulinEventEditFragment.java:818:                textInputEditText.addTextChangedListener(new C1211(this));
com/dexcom/phoenix/ui/screens/events/editevent/insulin/InsulinEventEditFragment.java:1149:                editTextWithSuffix.addTextChangedListener(new C2687(this, editTextWithSuffix));
com/dexcom/phoenix/ui/screens/events/editevent/glucose/BloodGlucoseEditFragment.java:511:                        editTextWithSuffix.addTextChangedListener(new C3911(this));
com/dexcom/phoenix/ui/screens/events/editevent/glucose/BloodGlucoseEditFragment.java:607:                editTextWithSuffix.addTextChangedListener(new C3911(this));
```

### webview_tracking — 3 hits in 3 files

- `ig/C7675.java` (1)
- `com/dexcom/phoenix/ui/screens/DexcomWebViewFragment.java` (1)
- `com/dexcom/phoenix/ui/legal/WebLegalActivity.java` (1)

```
ig/C7675.java:36:                CookieManager.getInstance().setAcceptThirdPartyCookies(webView, true);
com/dexcom/phoenix/ui/screens/DexcomWebViewFragment.java:312:                CookieManager.getInstance().setAcceptThirdPartyCookies(webView2, true);
com/dexcom/phoenix/ui/legal/WebLegalActivity.java:328:                CookieManager.getInstance().setAcceptThirdPartyCookies(webView, true);
```

### streaks — 0 hits in 0 files


```
```

### reengagement — 949 hits in 223 files

- `com/google/android/material/internal/CollapsingTextHelper.java` (132)
- `com/google/android/material/bottomsheet/BottomSheetBehavior.java` (43)
- `androidx/compose/material3/ExitUntilCollapsedScrollBehavior$nestedScrollConnection$1.java` (40)
- `com/google/android/material/textfield/TextInputLayout.java` (33)
- `com/google/android/material/appbar/CollapsingToolbarLayout.java` (27)
- `com/dexcom/phoenixuikit/uikit/R.java` (22)
- `com/google/android/material/R.java` (21)
- `com/qualtrics/R.java` (20)
- `androidx/core/location/LocationCompat.java` (18)
- `com/dexcom/g7/R.java` (16)
- `androidx/compose/foundation/text2/input/internal/selection/TextFieldSelectionState.java` (16)
- `com/dexcom/coresdk/alertsstatemachine/alerts/Alert.java` (15)

```
okhttp3/internal/concurrent/TaskLoggerKt.java:55:    public static final <T> T logElapsed(@NotNull("") Task task, @NotNull("") TaskQueue taskQueue, @NotNull("") Function0<? extends T> function0) {
androidx/databinding/adapters/TableLayoutBindingAdapter.java:104:                    if (z != tableLayout.isColumnCollapsed(i6)) {
androidx/databinding/adapters/TableLayoutBindingAdapter.java:105:                        tableLayout.setColumnCollapsed(i6, z);
kotlinx/coroutines/scheduling/CoroutineScheduler.java:149:                iArr[WorkerState.DORMANT.ordinal()] = 4;
kotlinx/coroutines/scheduling/CoroutineScheduler.java:229:            this.state = WorkerState.DORMANT;
kotlinx/coroutines/scheduling/CoroutineScheduler.java:399:                    this.state = WorkerState.DORMANT;
kotlinx/coroutines/scheduling/CoroutineScheduler.java:684:        public static final WorkerState DORMANT;
kotlinx/coroutines/scheduling/CoroutineScheduler.java:735:            DORMANT = new WorkerState(new String(iArr2, 0, s2), 3);
kotlinx/coroutines/scheduling/CoroutineScheduler.java:758:                    return new WorkerState[]{CPU_ACQUIRED, BLOCKING, PARKING, DORMANT, TERMINATED};
androidx/core/location/LocationManagerCompat.java:1873:                if (lastKnownLocation != null && SystemClock.elapsedRealtime() - LocationCompat.getElapsedRealtimeMillis(lastKnownLocation) < 10000) {
androidx/core/location/LocationCompat.java:68:        public static long getElapsedRealtimeNanos(Location location) {
androidx/core/location/LocationCompat.java:76:                    return Long.valueOf(((Location) objArr[0]).getElapsedRealtimeNanos());
```

### notif_permission_nag — 0 hits in 0 files


```
```

### cancellation_retention — 3 hits in 1 files

- `androidx/camera/view/PreviewStreamStateObserver.java` (3)

```
androidx/camera/view/PreviewStreamStateObserver.java:78:    private void cancelFlow() {
androidx/camera/view/PreviewStreamStateObserver.java:107:                cancelFlow();
androidx/camera/view/PreviewStreamStateObserver.java:117:                    cancelFlow();
```

### urgency_countdown — 489 hits in 88 files

- `com/dexcom/phoenix/ui/uiutils/WarmupStateChecker.java` (27)
- `com/dexcom/phoenix/ui/screens/glucose/AlertSettingsThresholdViewModel.java` (24)
- `com/dexcom/phoenix/ui/screens/settings/alerts/AlertsSettingsScreenViewModel.java` (20)
- `ig/AbstractC1423.java` (18)
- `com/dexcom/phoenix/ui/screens/settings/alerts/quietmodes/QuietModesBannerViewModel.java` (18)
- `com/dexcom/cgmfoundation/systemstate/txsessionstate/ExpirationStatus.java` (14)
- `com/google/common/util/concurrent/ClosingFuture.java` (14)
- `com/google/firebase/crashlytics/internal/common/Utils.java` (13)
- `com/google/firebase/installations/local/AutoValue_PersistedInstallationEntry.java` (13)
- `com/dexcom/phoenix/ui/screens/glucose/GlucoseScreenStateViewModel.java` (12)
- `ig/C11747.java` (11)
- `okhttp3/internal/concurrent/TaskQueue.java` (9)

```
okhttp3/internal/concurrent/TaskQueue.java:27:import java.util.concurrent.CountDownLatch;
okhttp3/internal/concurrent/TaskQueue.java:63:        public final CountDownLatch latch;
okhttp3/internal/concurrent/TaskQueue.java:93:            this.latch = new CountDownLatch(1);
okhttp3/internal/concurrent/TaskQueue.java:101:                    this.latch.countDown();
okhttp3/internal/concurrent/TaskQueue.java:113:        public final CountDownLatch getLatch() {
okhttp3/internal/concurrent/TaskQueue.java:114:            return (CountDownLatch) m85354(116529, new Object[0]);
okhttp3/internal/concurrent/TaskQueue.java:500:                        return new CountDownLatch(0);
okhttp3/internal/concurrent/TaskQueue.java:830:    public final CountDownLatch idleLatch() {
okhttp3/internal/concurrent/TaskQueue.java:831:        return (CountDownLatch) m85352(58271, new Object[0]);
okhttp3/internal/publicsuffix/PublicSuffixDatabase.java:34:import java.util.concurrent.CountDownLatch;
okhttp3/internal/publicsuffix/PublicSuffixDatabase.java:66:    public final CountDownLatch readCompleteLatch = new CountDownLatch(1);
okhttp3/internal/publicsuffix/PublicSuffixDatabase.java:468:                this.readCompleteLatch.countDown();
```

### infinite_autoplay — 8 hits in 5 files

- `com/google/zxing/pdf417/decoder/DecodedBitStreamParser.java` (2)
- `ig/C11983.java` (2)
- `ig/C1405.java` (2)
- `okhttp3/internal/HostnamesKt.java` (1)
- `ig/C9488.java` (1)

```
okhttp3/internal/HostnamesKt.java:35:        jadx.core.utils.exceptions.JadxOverflowException: LoopRegionVisitor.assignOnlyInLoop endless recursion
com/google/zxing/pdf417/decoder/DecodedBitStreamParser.java:261:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
com/google/zxing/pdf417/decoder/DecodedBitStreamParser.java:265:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
ig/C9488.java:362:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
ig/C11983.java:94:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
ig/C11983.java:101:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
ig/C1405.java:726:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
ig/C1405.java:739:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
```

### badges — 23 hits in 11 files

- `androidx/core/app/NotificationCompatBuilder.java` (4)
- `androidx/core/app/NotificationCompat.java` (3)
- `androidx/health/platform/client/proto/EnumValue.java` (3)
- `androidx/health/platform/client/proto/Field.java` (3)
- `com/dexcom/phoenix/ui/MainActivity.java` (2)
- `com/google/android/material/badge/BadgeState.java` (2)
- `com/google/android/material/badge/BadgeDrawable.java` (2)
- `com/qualtrics/digital/Properties.java` (1)
- `com/dexcom/g7/R.java` (1)
- `ig/C8234.java` (1)
- `com/google/firebase/messaging/CommonNotificationBuilder.java` (1)

```
com/qualtrics/digital/Properties.java:660:    public void setNumber(String str, double d) {
com/dexcom/g7/R.java:6740:        public static final int id_g7pens_settings_data_consents_badge_count = 0x7f0a083b;
com/dexcom/phoenix/ui/MainActivity.java:1697:                orCreateBadge.setNumber(iIntValue);
com/dexcom/phoenix/ui/MainActivity.java:1768:                orCreateBadge2.setNumber(num.intValue());
com/google/android/material/badge/BadgeState.java:997:                setNumber(-1);
com/google/android/material/badge/BadgeState.java:1451:    public void setNumber(int i) {
com/google/android/material/badge/BadgeDrawable.java:607:                this.state.setNumber(iMax);
com/google/android/material/badge/BadgeDrawable.java:1337:    public void setNumber(int i) {
ig/C8234.java:94:        sparseIntArray.put(R.id.id_g7pens_settings_data_consents_badge_count, 24);
com/google/firebase/messaging/CommonNotificationBuilder.java:389:                    builder.setNumber(notificationCount.intValue());
androidx/core/app/NotificationCompatBuilder.java:339:        public static Notification.Builder setBadgeIconType(Notification.Builder builder, int i) {
androidx/core/app/NotificationCompatBuilder.java:374:                    return ((Notification.Builder) objArr[0]).setBadgeIconType(((Integer) objArr[1]).intValue());
```

### minors_age — 26 hits in 3 files

- `com/google/android/gms/common/PackageSignatureVerifier.java` (13)
- `com/google/android/gms/common/PackageVerificationResult.java` (8)
- `com/google/android/gms/common/zzac.java` (5)

```
com/google/android/gms/common/PackageSignatureVerifier.java:53:                        return PackageVerificationResult.zza(str, zzxVarZzc.zzb, zzxVarZzc.zzc);
com/google/android/gms/common/PackageSignatureVerifier.java:55:                    this.zzb = new zzac(strConcat, PackageVerificationResult.zzd(str, zzxVarZzc.zzd));
com/google/android/gms/common/PackageSignatureVerifier.java:62:                    PackageVerificationResult packageVerificationResultQueryPackageSignatureVerified = queryPackageSignatureVerified(context2, str2);
com/google/android/gms/common/PackageSignatureVerifier.java:63:                    packageVerificationResultQueryPackageSignatureVerified.zzb();
com/google/android/gms/common/PackageSignatureVerifier.java:64:                    return packageVerificationResultQueryPackageSignatureVerified;
com/google/android/gms/common/PackageSignatureVerifier.java:66:                    PackageVerificationResult packageVerificationResultQueryPackageSignatureVerified2 = queryPackageSignatureVerified(context2, str2);
com/google/android/gms/common/PackageSignatureVerifier.java:67:                    if (!packageVerificationResultQueryPackageSignatureVerified2.zzc()) {
com/google/android/gms/common/PackageSignatureVerifier.java:68:                        return packageVerificationResultQueryPackageSignatureVerified2;
com/google/android/gms/common/PackageSignatureVerifier.java:103:                    return packageVerificationResultQueryPackageSignatureVerified2;
com/google/android/gms/common/PackageSignatureVerifier.java:130:    public PackageVerificationResult queryPackageSignatureVerified(@NonNull Context context, @NonNull String str) {
com/google/android/gms/common/PackageSignatureVerifier.java:131:        return (PackageVerificationResult) m36204(38841, context, str);
com/google/android/gms/common/PackageSignatureVerifier.java:137:    public PackageVerificationResult queryPackageSignatureVerifiedWithRetry(@NonNull Context context, @NonNull String str) {
```

### screen_time — 2664 hits in 244 files

- `com/dexcom/phoenix/system/NotificationUtil.java` (230)
- `com/dexcom/g7/R.java` (116)
- `com/dexcom/phoenix/ui/screens/settings/alerts/AlertsSettingsScreenViewModel.java` (115)
- `com/dexcom/coresdk/cgmkit/persistence/quietmodes/QuietModesDAO_Impl.java` (91)
- `com/dexcom/coresdk/cgmkit/persistence/quietmodes/QuietModesRepository.java` (87)
- `com/dexcom/phoenix/ui/screens/glucose/AlertSettingsThresholdViewModel.java` (79)
- `com/dexcom/phoenix/ui/screens/settings/alerts/quietmodes/QuietModesBannerViewModel.java` (76)
- `com/dexcom/phoenix/ui/uiutils/ResourceProvider.java` (55)
- `ig/C12097.java` (42)
- `com/dexcom/dexcomone/persistence/quietmodes/QuietModesDisabler.java` (39)
- `com/dexcom/coresdk/cgmkit/persistence/quietmodes/QuietModesSetting.java` (36)
- `com/dexcom/coresdk/cgmkit/persistence/quietmodes/QuietModesSettings.java` (36)

```
androidx/databinding/library/baseAdapters/BR.java:27:    public static final int hasQuietModesInfoDisplayed = 22;
androidx/databinding/library/baseAdapters/BR.java:41:    public static final int onQuietModeSilenceChange = 36;
androidx/databinding/library/baseAdapters/BR.java:42:    public static final int onQuietModeTouch = 37;
androidx/databinding/library/baseAdapters/BR.java:43:    public static final int onQuietModeVibrateChange = 38;
androidx/databinding/library/baseAdapters/BR.java:45:    public static final int quietModeEnabled = 40;
androidx/databinding/library/baseAdapters/BR.java:46:    public static final int quietModeNotificationsEnabled = 41;
androidx/databinding/library/baseAdapters/BR.java:47:    public static final int quietModeSilenceEnabled = 42;
androidx/databinding/library/baseAdapters/BR.java:48:    public static final int quietModeVibrateEnabled = 43;
com/dexcom/coresdk/cgmkit/cgmorchestrator/CgmCore.java:698:                                    cgmKitRoomDatabaseCreate$phoenixsdk_production$default.getQuietModesRepository$phoenixsdk_production().setPersistenceEventListener(this.f573);
com/qualtrics/digital/resolvers/TimeSpentInAppResolver.java:17:public class TimeSpentInAppResolver {
com/qualtrics/digital/resolvers/TimeSpentInAppResolver.java:85:    public boolean evaluateTimeSpentInApp(String str, String str2) {
com/qualtrics/digital/ComparatorNode.java:7:import com.qualtrics.digital.resolvers.TimeSpentInAppResolver;
```

