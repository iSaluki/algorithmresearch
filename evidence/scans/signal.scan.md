# Pattern scan: work/signal/jdex

## Code categories (library packages excluded)

### installed_apps — 12 hits in 10 files

- `classes:com/google/android/gms/internal/p000authapi/zbag.java` (2)
- `classes:com/google/android/gms/common/GooglePlayServicesUtil.java` (2)
- `classes:okhttp3/internal/http2/Huffman$Node.java` (1)
- `classes:androidx/core/widget/TextViewCompat$OreoCallback.java` (1)
- `classes:androidx/core/os/BuildCompat.java` (1)
- `classes:androidx/compose/material3/ChipKt$$ExternalSyntheticLambda1.java` (1)
- `classes:androidx/sharetarget/ShareTargetXmlParser.java` (1)
- `classes:androidx/credentials/playservices/controllers/identityauth/beginsignin/CredentialProviderBeginSignInController.java` (1)
- `classes2:me/leolin/shortcutbadger/ShortcutBadger.java` (1)
- `classes2:ezvcard/util/GeoUri.java` (1)

```
classes:okhttp3/internal/http2/Huffman$Node.java:267:                packageInfo = Wrappers.packageManager((Context) this.children).context.getPackageManager().getPackageInfo("com.google.android.gms", 0);
classes:com/google/android/gms/internal/p000authapi/zbag.java:191:            PackageInfo packageInfo = revocationBoundService.getPackageManager().getPackageInfo("com.google.android.gms", 64);
classes:com/google/android/gms/internal/p000authapi/zbag.java:202:                                PackageInfo packageInfo2 = Wrappers.packageManager(context).context.getPackageManager().getPackageInfo("com.google.android.gms", Build.VERSION.SDK_INT >= 28 ? 134217792 : 64);
classes:androidx/core/widget/TextViewCompat$OreoCallback.java:79:                for (ResolveInfo resolveInfo : packageManager.queryIntentActivities(new Intent().setAction("android.intent.action.PROCESS_TEXT").setType("text/plain"), 0)) {
classes:androidx/core/os/BuildCompat.java:164:                Iterator<ResolveInfo> it = packageManager.queryIntentActivities(intent, 128).iterator();
classes:com/google/android/gms/common/GooglePlayServicesUtil.java:88:                packageInfo = packageManager.getPackageInfo("com.android.vending", Build.VERSION.SDK_INT >= 28 ? 134225984 : 8256);
classes:com/google/android/gms/common/GooglePlayServicesUtil.java:96:            PackageInfo packageInfo2 = packageManager.getPackageInfo("com.google.android.gms", Build.VERSION.SDK_INT >= 28 ? 134217792 : 64);
classes:androidx/compose/material3/ChipKt$$ExternalSyntheticLambda1.java:112:                List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(new Intent().setAction("android.intent.action.PROCESS_TEXT").setType("text/plain"), 0);
classes:androidx/sharetarget/ShareTargetXmlParser.java:114:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(intent, 128);
classes:androidx/credentials/playservices/controllers/identityauth/beginsignin/CredentialProviderBeginSignInController.java:396:        int i = packageManager.getPackageInfo("com.google.android.gms", 0).versionCode;
classes2:me/leolin/shortcutbadger/ShortcutBadger.java:110:        Iterator<ResolveInfo> it = context.getPackageManager().queryIntentActivities(intent, 65536).iterator();
classes2:ezvcard/util/GeoUri.java:1204:                    if (metadata.gmsVersionCode == 0 && (packageInfo = metadata.getPackageInfo("com.google.android.gms")) != null) {
```

### usage_stats — 11 hits in 4 files

- `classes5:org/thoughtcrime/securesms/util/BatterySnapshotTracker.java` (3)
- `classes5:org/thoughtcrime/securesms/logsubmit/LogSectionBattery.java` (3)
- `classes5:org/thoughtcrime/securesms/logsubmit/LogSectionPower.java` (3)
- `classes5:org/thoughtcrime/securesms/util/BucketInfo.java` (2)

```
classes5:org/thoughtcrime/securesms/util/BucketInfo.java:4:import android.app.usage.UsageStatsManager;
classes5:org/thoughtcrime/securesms/util/BucketInfo.java:28:    public static BucketInfo getInfo(UsageStatsManager usageStatsManager, long j) {
classes5:org/thoughtcrime/securesms/util/BatterySnapshotTracker.java:3:import android.app.usage.UsageStatsManager;
classes5:org/thoughtcrime/securesms/util/BatterySnapshotTracker.java:168:            Object systemService2 = context.getSystemService("usagestats");
classes5:org/thoughtcrime/securesms/util/BatterySnapshotTracker.java:169:            UsageStatsManager usageStatsManager = systemService2 instanceof UsageStatsManager ? (UsageStatsManager) systemService2 : null;
classes5:org/thoughtcrime/securesms/logsubmit/LogSectionBattery.java:3:import android.app.usage.UsageStatsManager;
classes5:org/thoughtcrime/securesms/logsubmit/LogSectionBattery.java:90:            Object systemService2 = context.getSystemService("usagestats");
classes5:org/thoughtcrime/securesms/logsubmit/LogSectionBattery.java:91:            UsageStatsManager usageStatsManager = systemService2 instanceof UsageStatsManager ? (UsageStatsManager) systemService2 : null;
classes5:org/thoughtcrime/securesms/logsubmit/LogSectionPower.java:3:import android.app.usage.UsageStatsManager;
classes5:org/thoughtcrime/securesms/logsubmit/LogSectionPower.java:12:        UsageStatsManager usageStatsManager = (UsageStatsManager) context.getSystemService("usagestats");
classes5:org/thoughtcrime/securesms/logsubmit/LogSectionPower.java:14:            return "UsageStatsManager not available";
```

### clipboard — 9 hits in 6 files

- `classes:androidx/compose/foundation/text/input/internal/selection/TextFieldSelectionState.java` (2)
- `classes3:org/thoughtcrime/securesms/verify/VerifyDisplayRepository.java` (2)
- `classes3:org/thoughtcrime/securesms/components/emoji/EmojiEditText.java` (2)
- `classes:androidx/appcompat/widget/AppCompatEditText.java` (1)
- `classes:androidx/compose/foundation/text/selection/TextFieldSelectionManager$paste$1.java` (1)
- `classes3:org/thoughtcrime/securesms/components/ComposeText.java` (1)

```
classes:androidx/appcompat/widget/AppCompatEditText.java:239:        ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
classes:androidx/compose/foundation/text/selection/TextFieldSelectionManager$paste$1.java:137:                        ClipData primaryClip = ((AndroidClipboardImpl) clipboard).androidClipboardManager.getClipboardManager().getPrimaryClip();
classes:androidx/compose/foundation/text/input/internal/selection/TextFieldSelectionState.java:834:            ClipData primaryClip = ((AndroidClipboardImpl) clipboard).androidClipboardManager.getClipboardManager().getPrimaryClip();
classes:androidx/compose/foundation/text/input/internal/selection/TextFieldSelectionState.java:1022:        if (TestTagKt.getNativeClipboardManager(clipboard).hasPrimaryClip() && (primaryClipDescription = TestTagKt.getNativeClipboardManager(clipboard).getPrimaryClipDescription()) != null && primaryC
classes3:org/thoughtcrime/securesms/verify/VerifyDisplayRepository.java:54:        if (!clipboardManager.hasPrimaryClip() || clipboardManager.getPrimaryClip().getItemCount() <= 0) {
classes3:org/thoughtcrime/securesms/verify/VerifyDisplayRepository.java:57:        return clipboardManager.getPrimaryClip().getItemAt(0).getText().toString();
classes3:org/thoughtcrime/securesms/components/emoji/EmojiEditText.java:101:            ClipData primaryClip = ((ClipboardManager) getContext().getSystemService("clipboard")).getPrimaryClip();
classes3:org/thoughtcrime/securesms/components/emoji/EmojiEditText.java:107:            CharSequence textFromClipData = getTextFromClipData(((ClipboardManager) getContext().getSystemService("clipboard")).getPrimaryClip());
classes3:org/thoughtcrime/securesms/components/ComposeText.java:464:            ClipData primaryClip = ((ClipboardManager) getContext().getSystemService("clipboard")).getPrimaryClip();
```

### contacts — 69 hits in 21 files

- `classes4:org/signal/contacts/SystemContactsRepository.java` (15)
- `classes4:org/thoughtcrime/securesms/contactshare/ContactCardReader.java` (7)
- `classes4:org/thoughtcrime/securesms/conversation/v2/AddToContactsContract.java` (5)
- `classes4:com/bumptech/glide/load/data/StreamLocalUriFetcher.java` (4)
- `classes4:org/thoughtcrime/securesms/contacts/ContactIdentityManagerICS.java` (4)
- `classes4:org/thoughtcrime/securesms/conversation/v2/ConversationFragment.java` (4)
- `classes4:org/thoughtcrime/securesms/profiles/SystemProfileUtil$1.java` (2)
- `classes4:org/thoughtcrime/securesms/mms/AttachmentManager.java` (2)
- `classes4:org/thoughtcrime/securesms/conversation/v2/ConversationActivityResultContracts.java` (2)
- `classes4:org/thoughtcrime/securesms/contacts/index/ContactIndexBuilder.java` (2)
- `classes4:org/thoughtcrime/securesms/contacts/sync/CdsPermanentErrorBottomSheet.java` (2)
- `classes4:org/thoughtcrime/securesms/contacts/sync/CdsTemporaryErrorBottomSheet.java` (2)

```
classes4:com/bumptech/glide/load/data/StreamLocalUriFetcher.java:7:import android.provider.ContactsContract;
classes4:com/bumptech/glide/load/data/StreamLocalUriFetcher.java:49:            Uri uriLookupContact = ContactsContract.Contacts.lookupContact(contentResolver, uri);
classes4:com/bumptech/glide/load/data/StreamLocalUriFetcher.java:53:            inputStreamOpenContactPhotoInputStream = ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uriLookupContact, true);
classes4:com/bumptech/glide/load/data/StreamLocalUriFetcher.java:55:            inputStreamOpenContactPhotoInputStream = ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uri, true);
classes4:org/thoughtcrime/securesms/profiles/SystemProfileUtil$1.java:7:import android.provider.ContactsContract;
classes4:org/thoughtcrime/securesms/profiles/SystemProfileUtil$1.java:32:            Cursor cursorQuery = this.val$context.getContentResolver().query(ContactsContract.Profile.CONTENT_URI, null, null, null, null);
classes4:org/signal/contacts/SystemContactsRepository.java:11:import android.provider.ContactsContract;
classes4:org/signal/contacts/SystemContactsRepository.java:179:                    Uri lookupUri = ContactsContract.Contacts.getLookupUri(cursor.getLong(cursor.getColumnIndexOrThrow("_id")), strRequireNonNullString);
classes4:org/signal/contacts/SystemContactsRepository.java:635:        Uri uriBuild = ContactsContract.Data.CONTENT_URI.buildUpon().appendQueryParameter("caller_is_syncadapter", "true").build();
classes4:org/signal/contacts/SystemContactsRepository.java:636:        ContentProviderOperation.Builder builderWithValue = ContentProviderOperation.newInsert(ContactsContract.RawContacts.CONTENT_URI).withValue("account_name", contactLinkConfiguration.account.name).withValue("account_type", contactLi
classes4:org/signal/contacts/SystemContactsRepository.java:654:        ContentProviderOperation contentProviderOperationBuild7 = ContentProviderOperation.newUpdate(ContactsContract.AggregationExceptions.CONTENT_URI).withValue("raw_contact_id1", Long.valueOf(systemContactInfo.siblingRawContactId)).wi
classes4:org/signal/contacts/SystemContactsRepository.java:660:        Uri uriBuild = ContactsContract.Data.CONTENT_URI.buildUpon().appendQueryParameter("caller_is_syncadapter", "true").build();
```

### call_log — 0 hits in 0 files


```
```

### sms — 37 hits in 13 files

- `classes5:org/thoughtcrime/securesms/registration/data/RegistrationRepository.java` (7)
- `classes3:org/thoughtcrime/securesms/registration/sms/SmsRetrieverReceiver.java` (5)
- `classes3:org/thoughtcrime/securesms/components/settings/app/changenumber/ChangeNumberViewModel.java` (4)
- `classes:org/thoughtcrime/securesms/registration/data/RegistrationRepository$registerSmsListener$started$1.java` (3)
- `classes:org/signal/registration/RegistrationRepository$hasKnownPin$2.java` (3)
- `classes:com/google/android/gms/internal/p001authapiphone/zzab.java` (3)
- `classes:com/google/android/gms/internal/p001authapiphone/zzw.java` (3)
- `classes5:org/whispersystems/signalservice/api/registration/RegistrationApi.java` (3)
- `classes:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java` (2)
- `classes:com/google/android/gms/internal/p001authapiphone/zzz.java` (1)
- `classes2:kotlin/time/Duration.java` (1)
- `classes2:org/signal/network/api/RegistrationApiV2.java` (1)

```
classes:org/thoughtcrime/securesms/registration/data/RegistrationRepository$registerSmsListener$started$1.java:4:import com.google.android.gms.auth.api.phone.SmsRetrieverClient;
classes:org/thoughtcrime/securesms/registration/data/RegistrationRepository$registerSmsListener$started$1.java:49:                zzw zzwVarStartSmsRetriever = new zzab(this.$context, null, SmsRetrieverClient.zzc, Api$ApiOptions.NO_OPTIONS, GoogleApi.Settings.DEFAULT_SETTINGS).startSmsRetriever();
classes:org/thoughtcrime/securesms/registration/data/RegistrationRepository$registerSmsListener$started$1.java:51:                Object objAwait = ByteStreamsKt.await(zzwVarStartSmsRetriever, this);
classes:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java:10:public abstract class SmsRetrieverClient extends GoogleApi {
classes:com/google/android/gms/auth/api/phone/SmsRetrieverClient.java:11:    public static final zzdl zzc = new zzdl("SmsRetriever.API", new zaa(1), new Api$ClientKey());
classes:org/signal/registration/RegistrationRepository$hasKnownPin$2.java:3:import com.google.android.gms.auth.api.phone.SmsRetrieverClient;
classes:org/signal/registration/RegistrationRepository$hasKnownPin$2.java:238:                        zzw zzwVarStartSmsRetriever = new zzab(registrationRepository.context, null, SmsRetrieverClient.zzc, Api$ApiOptions.NO_OPTIONS, GoogleApi.Settings.DEFAULT_SETTINGS).startSmsRetriever();
classes:org/signal/registration/RegistrationRepository$hasKnownPin$2.java:240:                        if (ByteStreamsKt.await(zzwVarStartSmsRetriever, this) == unit2) {
classes:com/google/android/gms/internal/p001authapiphone/zzab.java:3:import com.google.android.gms.auth.api.phone.SmsRetrieverClient;
classes:com/google/android/gms/internal/p001authapiphone/zzab.java:12:public final class zzab extends SmsRetrieverClient {
classes:com/google/android/gms/internal/p001authapiphone/zzab.java:13:    public final zzw startSmsRetriever() {
classes:com/google/android/gms/internal/p001authapiphone/zzw.java:16:        IInterface iInterfaceQueryLocalInterface = iBinder.queryLocalInterface("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService");
```

### location — 16 hits in 12 files

- `classes:com/fasterxml/jackson/core/exc/StreamReadException.java` (2)
- `classes:com/fasterxml/jackson/core/util/JsonParserDelegate.java` (2)
- `classes:com/fasterxml/jackson/databind/util/TokenBuffer.java` (2)
- `classes:androidx/appcompat/app/AppCompatDelegateImpl.java` (2)
- `classes:com/fasterxml/jackson/core/JsonParser.java` (1)
- `classes:com/fasterxml/jackson/core/json/UTF8StreamJsonParser.java` (1)
- `classes:com/fasterxml/jackson/core/json/ReaderBasedJsonParser.java` (1)
- `classes:com/fasterxml/jackson/databind/deser/AbstractDeserializer.java` (1)
- `classes:com/fasterxml/jackson/databind/deser/BeanDeserializerBase.java` (1)
- `classes:com/fasterxml/jackson/databind/exc/UnrecognizedPropertyException.java` (1)
- `classes:com/fasterxml/jackson/databind/exc/IgnoredPropertyException.java` (1)
- `classes4:org/thoughtcrime/securesms/maps/LocationRetriever.java` (1)

```
classes:com/fasterxml/jackson/core/exc/StreamReadException.java:12:        super(str, jsonParser == null ? null : jsonParser.getCurrentLocation());
classes:com/fasterxml/jackson/core/exc/StreamReadException.java:27:        super(str, jsonParser == null ? null : jsonParser.getCurrentLocation(), th);
classes:com/fasterxml/jackson/core/JsonParser.java:123:    public abstract JsonLocation getCurrentLocation();
classes:com/fasterxml/jackson/core/util/JsonParserDelegate.java:70:    public JsonLocation getCurrentLocation() {
classes:com/fasterxml/jackson/core/util/JsonParserDelegate.java:71:        return this.delegate.getCurrentLocation();
classes:com/fasterxml/jackson/core/json/UTF8StreamJsonParser.java:2245:    public JsonLocation getCurrentLocation() {
classes:com/fasterxml/jackson/core/json/ReaderBasedJsonParser.java:1724:    public JsonLocation getCurrentLocation() {
classes:com/fasterxml/jackson/databind/deser/AbstractDeserializer.java:74:        throw new UnresolvedForwardReference(jsonParser, Animation.CC.m("Could not resolve Object Id [", objectReference, "] -- unresolved forward-reference?"), jsonParser.getCurrentLocation(), readableObjectIdFindObjectId);
classes:com/fasterxml/jackson/databind/deser/BeanDeserializerBase.java:488:        throw new UnresolvedForwardReference(jsonParser, "Could not resolve Object Id [" + objectReference + "] (for " + this._beanType + ").", jsonParser.getCurrentLocation(), readableObjectIdFindObjectId);
classes:com/fasterxml/jackson/databind/exc/UnrecognizedPropertyException.java:17:        UnrecognizedPropertyException unrecognizedPropertyException = new UnrecognizedPropertyException(jsonParser, TooltipState.CC.m("Unrecognized field \"", str, "\" (class ", cls.getName(), "), not marked as ignorabl
classes:com/fasterxml/jackson/databind/util/TokenBuffer.java:303:        public JsonLocation getCurrentLocation() {
classes:com/fasterxml/jackson/databind/util/TokenBuffer.java:460:            return getCurrentLocation();
```

### wifi_bt_scan — 1 hits in 1 files

- `classes5:org/webrtc/NetworkMonitorAutoDetect.java` (1)

```
classes5:org/webrtc/NetworkMonitorAutoDetect.java:441:            return (intentRegisterReceiver == null || (wifiInfo = (WifiInfo) intentRegisterReceiver.getParcelableExtra("wifiInfo")) == null || (ssid = wifiInfo.getSSID()) == null) ? "" : ssid;
```

### device_ids — 207 hits in 94 files

- `classes3:org/thoughtcrime/securesms/components/settings/app/subscription/InAppPaymentsRepository.java` (7)
- `classes4:org/thoughtcrime/securesms/jobs/InAppPaymentAuthCheckJob.java` (6)
- `classes4:org/thoughtcrime/securesms/jobs/InAppPaymentKeepAliveJob.java` (6)
- `classes5:org/whispersystems/signalservice/api/keys/KeysApi.java` (6)
- `classes3:org/thoughtcrime/securesms/components/settings/app/subscription/RecurringInAppPaymentRepository.java` (5)
- `classes4:org/thoughtcrime/securesms/jobs/InAppPaymentRecurringContextJob.java` (5)
- `classes4:org/thoughtcrime/securesms/database/SessionTable.java` (5)
- `classes2:org/signal/libsignal/protocol/SignalProtocolAddress.java` (4)
- `classes3:org/thoughtcrime/securesms/components/webrtc/WebRtcAudioOutputBottomSheetKt.java` (4)
- `classes4:org/thoughtcrime/securesms/linkdevice/LinkDeviceViewModel.java` (4)
- `classes4:org/thoughtcrime/securesms/linkdevice/LinkDeviceSettingsState.java` (4)
- `classes4:org/thoughtcrime/securesms/dependencies/ApplicationDependencyProvider.java` (4)

```
classes:com/android/billingclient/api/zzdn.java:54:        this.zza = Build.VERSION.SDK_INT >= 34 && PlayerView.Api34.getDeviceId(context) != 0;
classes:androidx/core/widget/NestedScrollView.java:1429:            getScrollFeedbackProvider().mImpl.onScrollProgress(motionEvent.getDeviceId(), motionEvent.getSource(), i2, scrollY2);
classes:androidx/core/widget/NestedScrollView.java:1443:                    getScrollFeedbackProvider().mImpl.onScrollLimit(motionEvent.getDeviceId(), motionEvent.getSource(), i2, false);
classes:androidx/core/widget/NestedScrollView.java:1470:                getScrollFeedbackProvider().mImpl.onScrollLimit(motionEvent.getDeviceId(), motionEvent.getSource(), i2, true);
classes:androidx/core/view/ViewKt.java:180:            transformScopeImpl.isVeilMutated$delegate = LifecycleCameraRepositories.getInstance$camera_lifecycle(Build.VERSION.SDK_INT >= 34 ? context.getDeviceId() : 0);
classes:androidx/core/view/DifferentialMotionFlingController.java:57:        int deviceId = motionEvent.getDeviceId();
classes:androidx/core/view/DifferentialMotionFlingController.java:67:            int deviceId2 = motionEvent.getDeviceId();
classes:androidx/core/view/DifferentialMotionFlingController.java:91:            int deviceId3 = motionEvent.getDeviceId();
classes:androidx/navigation/internal/NavControllerImpl$$ExternalSyntheticLambda8.java:298:                builder.linkedDeviceData = new LinkedDeviceData(((RegistrationApiV2.LinkDeviceResponse) success.getResult()).getDeviceId(), "Android", (ByteString) networkController$LinkDeviceProvisioningMessag
classes:androidx/camera/core/impl/utils/ContextUtil.java:22:        String str = String.format("%d-%d-%s", Integer.valueOf(iHashCode), Integer.valueOf(i >= 34 ? context.getDeviceId() : 0), i >= 30 ? BuildCompat.Api30Impl.getAttributionTag(context) : null);
classes:androidx/camera/core/impl/utils/ContextUtil.java:39:                    applicationContext = PlayerView.Api34.createDeviceContext(applicationContext, context.getDeviceId());
classes:androidx/media3/exoplayer/audio/DefaultAudioSink.java:230:        if (Build.VERSION.SDK_INT >= 34 && context != null && (deviceId = context.getDeviceId()) != 0 && deviceId != -1) {
```

### gsf_id — 0 hits in 0 files


```
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

### accounts — 3 hits in 2 files

- `classes4:org/signal/contacts/SystemContactsRepository.java` (2)
- `classes5:org/thoughtcrime/securesms/profiles/SystemProfileUtil.java` (1)

```
classes4:org/signal/contacts/SystemContactsRepository.java:743:        AccountManager accountManager = AccountManager.get(context);
classes4:org/signal/contacts/SystemContactsRepository.java:745:        Account[] accountsByType = accountManager.getAccountsByType(BuildConfig.APPLICATION_ID);
classes5:org/thoughtcrime/securesms/profiles/SystemProfileUtil.java:51:                for (Account account : AccountManager.get(context).getAccountsByType("com.google")) {
```

### battery_state — 12 hits in 8 files

- `classes4:org/thoughtcrime/securesms/jobmanager/impl/ChargingAndBatteryIsNotLowConstraintObserver.java` (4)
- `classes4:org/signal/core/util/DeviceProperties.java` (2)
- `classes4:org/thoughtcrime/securesms/ApplicationContext.java` (1)
- `classes4:org/thoughtcrime/securesms/jobmanager/impl/ChargingConstraint.java` (1)
- `classes4:org/thoughtcrime/securesms/jobmanager/impl/BatteryNotLowConstraint.java` (1)
- `classes4:org/thoughtcrime/securesms/logsubmit/LogSectionSystemInfo.java` (1)
- `classes5:org/thoughtcrime/securesms/logsubmit/LogSectionBattery.java` (1)
- `classes5:org/thoughtcrime/securesms/util/BatterySnapshotTracker.java` (1)

```
classes4:org/thoughtcrime/securesms/ApplicationContext.java:724:        Log.i(str, "App is now visible. Battery: " + DeviceProperties.getBatteryLevel(this) + "% (charging: " + DeviceProperties.isCharging(this) + ")");
classes4:org/thoughtcrime/securesms/jobmanager/impl/ChargingConstraint.java:40:        return ChargingAndBatteryIsNotLowConstraintObserver.isCharging();
classes4:org/thoughtcrime/securesms/jobmanager/impl/BatteryNotLowConstraint.java:63:            return ChargingAndBatteryIsNotLowConstraintObserver.isCharging() || ChargingAndBatteryIsNotLowConstraintObserver.isBatteryNotLow();
classes4:org/thoughtcrime/securesms/jobmanager/impl/ChargingAndBatteryIsNotLowConstraintObserver.java:36:    public static boolean isCharging(Intent intent) {
classes4:org/thoughtcrime/securesms/jobmanager/impl/ChargingAndBatteryIsNotLowConstraintObserver.java:42:        charging = isCharging(this.application.registerReceiver(new BroadcastReceiver(this) { // from class: org.thoughtcrime.securesms.jobmanager.impl.ChargingAndBatteryIsNotLowConstraintObserve
classes4:org/thoughtcrime/securesms/jobmanager/impl/ChargingAndBatteryIsNotLowConstraintObserver.java:47:                ChargingAndBatteryIsNotLowConstraintObserver.charging = ChargingAndBatteryIsNotLowConstraintObserver.isCharging(intent);
classes4:org/thoughtcrime/securesms/jobmanager/impl/ChargingAndBatteryIsNotLowConstraintObserver.java:57:    public static boolean isCharging() {
classes4:org/thoughtcrime/securesms/logsubmit/LogSectionSystemInfo.java:240:        boolean zIsCharging = DeviceProperties.isCharging(context);
classes4:org/signal/core/util/DeviceProperties.java:46:    public static boolean isCharging(Context context) {
classes4:org/signal/core/util/DeviceProperties.java:48:        return batteryManager != null && batteryManager.isCharging();
classes5:org/thoughtcrime/securesms/logsubmit/LogSectionBattery.java:76:        sb.append(DeviceProperties.isCharging(context));
classes5:org/thoughtcrime/securesms/util/BatterySnapshotTracker.java:161:        boolean zIsCharging = DeviceProperties.isCharging(context);
```

### screen_capture_detect — 2 hits in 1 files

- `classes4:org/thoughtcrime/securesms/migrations/LegacyMigrationJob.java` (2)

```
classes4:org/thoughtcrime/securesms/migrations/LegacyMigrationJob.java:53:    private static final int SCREENSHOTS = 300;
classes4:org/thoughtcrime/securesms/migrations/LegacyMigrationJob.java:149:        if (lastSeenVersion < SCREENSHOTS) {
```

### audio_capture — 2 hits in 2 files

- `classes5:org/thoughtcrime/securesms/audio/AudioCodec.java` (1)
- `classes5:org/webrtc/audio/WebRtcAudioRecord.java` (1)

```
classes5:org/thoughtcrime/securesms/audio/AudioCodec.java:66:        return new AudioRecord(1, SAMPLE_RATE, 16, 2, i * 10);
classes5:org/webrtc/audio/WebRtcAudioRecord.java:194:        return new AudioRecord(i, i2, i3, i4, i5);
```

### accessibility — 122 hits in 30 files

- `classes:androidx/compose/material3/internal/Listener.java` (10)
- `classes:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java` (10)
- `classes2:com/google/android/material/snackbar/BaseTransientBottomBar.java` (7)
- `classes2:com/google/android/material/textfield/EndCompoundLayout.java` (7)
- `classes:com/bumptech/glide/request/target/ViewTarget.java` (6)
- `classes:androidx/lifecycle/BlockRunner$maybeRun$1.java` (6)
- `classes:androidx/core/view/accessibility/AccessibilityManagerCompat$TouchExplorationStateChangeListenerWrapper.java` (6)
- `classes:com/google/android/material/textfield/MaterialAutoCompleteTextView.java` (6)
- `classes:androidx/customview/widget/ExploreByTouchHelper.java` (5)
- `classes:androidx/compose/ui/platform/ComposeViewContext.java` (5)
- `classes2:com/google/android/material/snackbar/Snackbar.java` (5)
- `classes2:com/google/android/material/textfield/DropdownMenuEndIconDelegate.java` (5)

```
classes:android/view/accessibility/AccessibilityManager$AccessibilityServicesStateChangeListener.java:4:public /* synthetic */ interface AccessibilityManager$AccessibilityServicesStateChangeListener {
classes:kotlin/text/Regex$$ExternalSyntheticLambda0.java:5:import android.view.accessibility.AccessibilityManager;
classes:kotlin/text/Regex$$ExternalSyntheticLambda0.java:221:                ((Listener) this.f$0).unregister((AccessibilityManager) this.f$1);
classes:com/bumptech/glide/request/target/ViewTarget.java:12:import android.view.accessibility.AccessibilityManager;
classes:com/bumptech/glide/request/target/ViewTarget.java:22:import androidx.core.view.accessibility.AccessibilityManagerCompat$TouchExplorationStateChangeListenerWrapper;
classes:com/bumptech/glide/request/target/ViewTarget.java:357:                    AccessibilityManager accessibilityManager = endCompoundLayout.accessibilityManager;
classes:com/bumptech/glide/request/target/ViewTarget.java:361:                            accessibilityManager.addTouchExplorationStateChangeListener(new AccessibilityManagerCompat$TouchExplorationStateChangeListenerWrapper(endCompoundLayout.touchExplorationStateChangeListener));
classes:com/bumptech/glide/request/target/ViewTarget.java:371:            AccessibilityManager accessibilityManager;
classes:com/bumptech/glide/request/target/ViewTarget.java:449:                    accessibilityManager.removeTouchExplorationStateChangeListener(new AccessibilityManagerCompat$TouchExplorationStateChangeListenerWrapper(exoPlayerImplInternal$$ExternalSyntheticLambda2));
classes:androidx/recyclerview/widget/RecyclerView.java:37:import android.view.accessibility.AccessibilityManager;
classes:androidx/recyclerview/widget/RecyclerView.java:133:    private final AccessibilityManager mAccessibilityManager;
classes:androidx/recyclerview/widget/RecyclerView.java:2367:        this.mAccessibilityManager = (AccessibilityManager) getContext().getSystemService("accessibility");
```

### root_emulator — 262 hits in 73 files

- `classes2:org/conscrypt/OpenSSLAeadCipher.java` (26)
- `classes2:org/signal/appsettings/account/AccountSettingsScreenKt.java` (14)
- `classes:androidx/compose/material3/ExposedDropdownMenuBoxScope.java` (13)
- `classes3:org/thoughtcrime/securesms/components/settings/app/internal/donor/InternalDonationErrorValuesKt.java` (13)
- `classes:androidx/compose/material3/CardKt.java` (12)
- `classes:androidx/compose/material3/ExposedDropdownMenuAnchorElement.java` (9)
- `classes:androidx/compose/ui/window/AndroidPopup_androidKt$Popup$lambda$3$0$$inlined$onDispose$1.java` (7)
- `classes3:org/thoughtcrime/securesms/backup/v2/local/ArchiveFileSystem.java` (7)
- `classes3:org/signal/appsettings/account/AccountSettingsScreenKt$$ExternalSyntheticLambda4.java` (7)
- `classes3:org/thoughtcrime/securesms/components/settings/app/internal/InternalPendingOneTimeDonationConfigurationFragmentKt.java` (7)
- `classes4:org/thoughtcrime/securesms/help/HelpScreenKt.java` (7)
- `classes:androidx/compose/foundation/text/BasicTextKt.java` (6)

```
classes:org/signal/core/ui/compose/Dialogs$$ExternalSyntheticLambda13.java:21:import androidx.compose.material3.ExposedDropdownMenuKt$;
classes:org/signal/core/ui/compose/Dialogs$$ExternalSyntheticLambda13.java:360:                        objRememberedValue6 = new ExposedDropdownMenuKt$.ExternalSyntheticLambda3(function1, (byte) 16);
classes:org/signal/core/ui/compose/Rows$$ExternalSyntheticLambda22.java:4:import androidx.compose.material3.ExposedDropdownMenuAnchorType;
classes:org/signal/core/ui/compose/Rows$$ExternalSyntheticLambda22.java:82:                ((ExposedDropdownMenuAnchorType) mutableState.getValue()).getClass();
classes:org/signal/core/ui/compose/Rows$$ExternalSyntheticLambda22.java:83:                mutableState.setValue(new ExposedDropdownMenuAnchorType());
classes:androidx/core/util/PatternsCompat.java:14:        Pattern patternCompile2 = Pattern.compile("(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucff
classes:androidx/compose/foundation/contextmenu/ContextMenuUiKt.java:20:import androidx.compose.material3.ExposedDropdownMenuKt$;
classes:androidx/compose/foundation/contextmenu/ContextMenuUiKt.java:182:                objRememberedValue = new ExposedDropdownMenuKt$.ExternalSyntheticLambda2(z, function0, (byte) 1);
classes:androidx/compose/foundation/AndroidEdgeEffectOverscrollEffect.java:7:import androidx.compose.material3.ExposedDropdownMenuKt$expandable$1;
classes:androidx/compose/foundation/AndroidEdgeEffectOverscrollEffect.java:51:        ExposedDropdownMenuKt$expandable$1 exposedDropdownMenuKt$expandable$1 = new ExposedDropdownMenuKt$expandable$1(this, (byte) 1);
classes:androidx/compose/foundation/AndroidEdgeEffectOverscrollEffect.java:53:        SuspendingPointerInputModifierNodeImpl suspendingPointerInputModifierNodeImpl = new SuspendingPointerInputModifierNodeImpl(null, null, null, exposedDropdownMenuKt$expandable$1);
classes:org/signal/registration/screens/RegistrationScaffold.java:11:import androidx.compose.material3.ExposedDropdownMenuKt$;
```

### js_bridge — 0 hits in 0 files


```
```

### boot_persist — 9 hits in 6 files

- `classes5:org/thoughtcrime/securesms/service/TimedEventManager.java` (4)
- `classes3:org/thoughtcrime/securesms/util/PowerManagerCompat.java` (1)
- `classes5:org/thoughtcrime/securesms/service/PersistentConnectionBootListener.java` (1)
- `classes5:org/thoughtcrime/securesms/service/PersistentAlarmManagerListener.java` (1)
- `classes5:org/thoughtcrime/securesms/messageprocessingalarm/RoutineMessageFetchReceiver.java` (1)
- `classes5:org/thoughtcrime/securesms/util/AlarmSleepTimer.java` (1)

```
classes3:org/thoughtcrime/securesms/util/PowerManagerCompat.java:12:        return new Intent("android.settings.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS", Uri.parse("package:" + context.getPackageName()));
classes5:org/thoughtcrime/securesms/service/TimedEventManager.java:81:                        Log.d(TAG, "[trySetExactAlarm] Using setExactAndAllowWhileIdle(), API: " + i);
classes5:org/thoughtcrime/securesms/service/TimedEventManager.java:82:                        alarmManager.setExactAndAllowWhileIdle(0, j, broadcast);
classes5:org/thoughtcrime/securesms/service/TimedEventManager.java:89:            Log.d(TAG, "[trySetExactAlarm] Using setAlarmClock(), API: " + i);
classes5:org/thoughtcrime/securesms/service/TimedEventManager.java:90:            alarmManager.setAlarmClock(new AlarmManager.AlarmClockInfo(j, pendingIntent), broadcast);
classes5:org/thoughtcrime/securesms/service/PersistentConnectionBootListener.java:15:        if (intent == null || !"android.intent.action.BOOT_COMPLETED".equals(intent.getAction())) {
classes5:org/thoughtcrime/securesms/service/PersistentAlarmManagerListener.java:39:                alarmManager.setExactAndAllowWhileIdle(0, j, pendingIntent);
classes5:org/thoughtcrime/securesms/messageprocessingalarm/RoutineMessageFetchReceiver.java:62:        if ("android.intent.action.BOOT_COMPLETED".equals(intent.getAction())) {
classes5:org/thoughtcrime/securesms/util/AlarmSleepTimer.java:86:            alarmManager.setExactAndAllowWhileIdle(2, SystemClock.elapsedRealtime() + j, broadcast);
```

### full_screen_intent — 3 hits in 3 files

- `classes:androidx/core/app/NotificationManagerCompat.java` (1)
- `classes:androidx/media3/common/util/GlProgram.java` (1)
- `classes3:org/thoughtcrime/securesms/notifications/TurnOnNotificationsBottomSheet.java` (1)

```
classes:androidx/core/app/NotificationManagerCompat.java:355:        return i < 34 ? this.mContext.checkSelfPermission("android.permission.USE_FULL_SCREEN_INTENT") == 0 : Api34Impl.canUseFullScreenIntent(this.mNotificationManager);
classes:androidx/media3/common/util/GlProgram.java:166:        builder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.ledARGB, not
classes3:org/thoughtcrime/securesms/notifications/TurnOnNotificationsBottomSheet.java:124:            turnOnNotificationsBottomSheet.setArguments(ArraysKt___ArraysKt.bundleOf(new Pair[]{new Pair(TurnOnNotificationsBottomSheet.ARG_TITLE, Integer.valueOf(R.string.GrantFullScreenIntentPermission_bottom
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 154 hits in 65 files

- `classes3:org/thoughtcrime/securesms/components/settings/app/subscription/donate/card/CreditCardFragment.java` (8)
- `classes2:com/google/android/material/timepicker/TimePickerTextInputPresenter.java` (6)
- `classes3:org/thoughtcrime/securesms/components/settings/models/TextInput.java` (5)
- `classes4:org/thoughtcrime/securesms/contactshare/SimpleTextWatcher.java` (5)
- `classes4:org/thoughtcrime/securesms/conversation/v2/ConversationFragment.java` (5)
- `classes:androidx/appcompat/widget/SearchView.java` (4)
- `classes3:org/thoughtcrime/securesms/stories/settings/create/CreateStoryNameFieldItem.java` (4)
- `classes3:org/thoughtcrime/securesms/components/settings/app/subscription/boost/Boost.java` (4)
- `classes4:org/thoughtcrime/securesms/mediasend/v2/review/AddMessageDialogFragment.java` (4)
- `classes4:org/thoughtcrime/securesms/mediasend/v2/text/TextStoryPostLinkEntryFragment.java` (4)
- `classes4:org/thoughtcrime/securesms/mediasend/v2/text/TextStoryPostTextEntryFragment.java` (4)
- `classes5:org/thoughtcrime/securesms/profiles/manage/UsernameEditFragment.java` (4)

```
classes:org/thoughtcrime/securesms/backup/PassphraseAsYouTypeFormatter.java:61:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:androidx/camera/video/Recorder.java:4323:            editText.addTextChangedListener(emojiTextWatcher);
classes:androidx/appcompat/widget/AppCompatButton.java:177:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:androidx/appcompat/widget/AppCompatButton.java:178:        super.onTextChanged(charSequence, i, i2, i3);
classes:androidx/appcompat/widget/AppCompatTextView.java:326:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:androidx/appcompat/widget/AppCompatTextView.java:327:        super.onTextChanged(charSequence, i, i2, i3);
classes:androidx/appcompat/widget/SearchView.java:370:            public final void onTextChanged(CharSequence charSequence, int i2, int i3, int i4) {
classes:androidx/appcompat/widget/SearchView.java:371:                searchView.onTextChanged(charSequence);
classes:androidx/appcompat/widget/SearchView.java:421:        searchAutoComplete.addTextChangedListener(this.mTextWatcher);
classes:androidx/appcompat/widget/SearchView.java:923:    public void onTextChanged(CharSequence charSequence) {
classes:androidx/emoji2/viewsintegration/EmojiTextWatcher.java:100:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:androidx/emoji2/text/SpannableBuilder.java:80:        public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
```

### webview_tracking — 0 hits in 0 files


```
```

### streaks — 0 hits in 0 files


```
```

### reengagement — 1386 hits in 232 files

- `classes2:com/google/android/material/internal/CollapsingTextHelper.java` (100)
- `classes4:org/thoughtcrime/securesms/database/MessageTable.java` (85)
- `classes:androidx/camera/camera2/pipe/compat/AndroidCameraDevice.java` (52)
- `classes2:com/google/android/material/textfield/TextInputLayout.java` (46)
- `classes4:org/thoughtcrime/securesms/jobs/BackfillCollapsedMessageJob.java` (41)
- `classes4:org/thoughtcrime/securesms/database/CollapsedState.java` (35)
- `classes4:org/thoughtcrime/securesms/conversation/ConversationUpdateItem.java` (34)
- `classes4:org/thoughtcrime/securesms/jobs/protos/BackfillCollapsedMessageJobData.java` (29)
- `classes2:com/google/android/material/appbar/CollapsingToolbarLayout.java` (27)
- `classes2:com/google/android/material/bottomsheet/BottomSheetBehavior.java` (27)
- `classes4:org/thoughtcrime/securesms/conversation/ConversationMessage.java` (24)
- `classes:androidx/camera/camera2/pipe/compat/AndroidCameraCaptureSession.java` (22)

```
classes:androidx/loader/content/AsyncTaskLoader.java:118:            printWriter.print(DateUtils.formatElapsedTime(this.mUpdateThrottle / 1000));
classes:androidx/loader/content/AsyncTaskLoader.java:123:                str2 = "-" + DateUtils.formatElapsedTime((SystemClock.uptimeMillis() - this.mLastLoadCompleteTime) / 1000);
classes:androidx/lifecycle/BlockRunner$cancel$1.java:842:                    if (!TextRange.m922getCollapsedimpl(textFieldSelectionManager.getValue$foundation().selection) && textFieldSelectionManager.getEditable() && !(textFieldSelectionManager.visualTransformation instanceof PasswordVisualTransfor
classes:com/bumptech/glide/request/SingleRequest.java:100:                this.startTime = SystemClock.elapsedRealtimeNanos();
classes:com/bumptech/glide/request/SingleRequest.java:141:                    logV("finished run method in " + LogTime.getElapsedMillis(this.startTime));
classes:com/bumptech/glide/request/SingleRequest.java:412:            Log.d("Glide", "Finished loading " + obj.getClass().getSimpleName() + " from " + dataSource + " for " + this.model + " with size [" + this.width + "x" + this.height + "] in " + LogTime.getElapsedMillis(this.startTime) + " ms");
classes:com/bumptech/glide/request/SingleRequest.java:459:                        logV("Got onSizeReady in " + LogTime.getElapsedMillis(this.startTime));
classes:com/bumptech/glide/request/SingleRequest.java:472:                        logV("finished setup for calling load in " + LogTime.getElapsedMillis(this.startTime));
classes:com/bumptech/glide/request/SingleRequest.java:487:                                        logV("finished onSizeReady in " + LogTime.getElapsedMillis(this.startTime));
classes:com/bumptech/glide/util/LogTime.java:11:    public static double getElapsedMillis(long j) {
classes:com/bumptech/glide/util/LogTime.java:12:        return (SystemClock.elapsedRealtimeNanos() - j) * MILLIS_MULTIPLIER;
classes:com/bumptech/glide/load/data/HttpUrlFetcher.java:83:        long jElapsedRealtimeNanos = SystemClock.elapsedRealtimeNanos();
```

### notif_permission_nag — 2 hits in 2 files

- `classes3:org/thoughtcrime/securesms/components/RatingManager.java` (1)
- `classes5:org/thoughtcrime/securesms/payments/preferences/PaymentsHomeFragment.java` (1)

```
classes3:org/thoughtcrime/securesms/components/RatingManager.java:16:    private static final int DAYS_UNTIL_REPROMPT_THRESHOLD = 4;
classes5:org/thoughtcrime/securesms/payments/preferences/PaymentsHomeFragment.java:63:    private static final int DAYS_UNTIL_REPROMPT_PAYMENT_LOCK = 30;
```

### cancellation_retention — 0 hits in 0 files


```
```

### urgency_countdown — 909 hits in 193 files

- `classes4:org/thoughtcrime/securesms/database/MessageTable.java` (54)
- `classes4:org/thoughtcrime/securesms/mms/OutgoingMessage.java` (44)
- `classes4:org/thoughtcrime/securesms/dependencies/NetworkDependenciesModule.java` (30)
- `classes4:org/thoughtcrime/securesms/messages/SyncMessageProcessor.java` (27)
- `classes4:org/thoughtcrime/securesms/database/ThreadTable.java` (22)
- `classes2:org/signal/core/ui/compose/QrCodeKt.java` (20)
- `classes3:org/thoughtcrime/securesms/components/registration/ActionCountDownButton.java` (16)
- `classes5:org/webrtc/EglRenderer.java` (16)
- `classes4:org/thoughtcrime/securesms/messagedetails/MessageHeaderViewHolder.java` (15)
- `classes4:org/thoughtcrime/securesms/jobmanager/JobManager.java` (15)
- `classes4:org/thoughtcrime/securesms/conversation/v2/data/DeletedMessageTombstoneCache.java` (15)
- `classes4:org/thoughtcrime/securesms/database/model/ThreadRecord.java` (14)

```
classes:org/thoughtcrime/securesms/components/location/SignalMapView$$ExternalSyntheticLambda2.java:64:import java.util.concurrent.CountDownLatch;
classes:org/thoughtcrime/securesms/components/location/SignalMapView$$ExternalSyntheticLambda2.java:291:        CountDownLatch countDownLatch = new CountDownLatch(1);
classes:org/thoughtcrime/securesms/components/location/SignalMapView$$ExternalSyntheticLambda2.java:293:        Base64.runOnMain(new MediaSessionStub$$ExternalSyntheticLambda3((Object) webView, (Object) intRef, (Object) objectRef, (Object) countDownLatch, (byte) 11));
classes:org/thoughtcrime/securesms/components/location/SignalMapView$$ExternalSyntheticLambda2.java:294:        countDownLatch.await();
classes:org/signal/core/util/crypto/KeyStoreHelper.java:16:import java.util.concurrent.CountDownLatch;
classes:org/signal/core/util/crypto/KeyStoreHelper.java:96:        CountDownLatch countDownLatch = new CountDownLatch(1);
classes:org/signal/core/util/crypto/KeyStoreHelper.java:98:        executor.execute(new ScannerView21$$ExternalSyntheticLambda1((Object) bArr, (Object) atomicReference, (Object) countDownLatch, (byte) 16));
classes:org/signal/core/util/crypto/KeyStoreHelper.java:100:            countDownLatch.await();
classes:org/signal/core/util/crypto/KeyStoreHelper.java:109:        CountDownLatch countDownLatch = new CountDownLatch(1);
classes:org/signal/core/util/crypto/KeyStoreHelper.java:111:        executor.execute(new ScannerView21$$ExternalSyntheticLambda1((Object) sealedData, (Object) atomicReference, (Object) countDownLatch, (byte) 15));
classes:org/signal/core/util/crypto/KeyStoreHelper.java:113:            countDownLatch.await();
classes:org/signal/qr/ScannerView21$$ExternalSyntheticLambda1.java:72:import java.util.concurrent.CountDownLatch;
```

### infinite_autoplay — 17 hits in 9 files

- `classes:com/airbnb/lottie/LottieAnimationView.java` (7)
- `classes2:org/signal/archive/proto/Group$Companion$ADAPTER$1.java` (2)
- `classes4:org/thoughtcrime/securesms/conversation/ConversationItem.java` (2)
- `classes:io/grpc/okhttp/OutboundFlowController.java` (1)
- `classes4:org/thoughtcrime/securesms/mediapreview/MediaPreviewFragment.java` (1)
- `classes4:org/thoughtcrime/securesms/mediapreview/MediaPreviewPageFragment.java` (1)
- `classes4:org/thoughtcrime/securesms/mediapreview/VideoMediaPreviewPageFragment.java` (1)
- `classes4:org/thoughtcrime/securesms/giph/mp4/GiphyMp4PlaybackPolicy.java` (1)
- `classes4:org/thoughtcrime/securesms/mms/VideoSlide.java` (1)

```
classes:io/grpc/okhttp/OutboundFlowController.java:228:        jadx.core.utils.exceptions.JadxOverflowException: LoopRegionVisitor.assignOnlyInLoop endless recursion
classes:com/airbnb/lottie/LottieAnimationView.java:52:    private boolean autoPlay;
classes:com/airbnb/lottie/LottieAnimationView.java:227:        this.autoPlay = false;
classes:com/airbnb/lottie/LottieAnimationView.java:256:            this.autoPlay = true;
classes:com/airbnb/lottie/LottieAnimationView.java:345:        this.autoPlay = false;
classes:com/airbnb/lottie/LottieAnimationView.java:569:        if (isInEditMode() || !this.autoPlay) {
classes:com/airbnb/lottie/LottieAnimationView.java:635:        this.autoPlay = false;
classes:com/airbnb/lottie/LottieAnimationView.java:771:        if (this.autoPlay) {
classes2:org/signal/archive/proto/Group$Companion$ADAPTER$1.java:24:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
classes2:org/signal/archive/proto/Group$Companion$ADAPTER$1.java:28:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
classes4:org/thoughtcrime/securesms/mediapreview/MediaPreviewFragment.java:610:            currentFragment.autoPlayIfNeeded();
classes4:org/thoughtcrime/securesms/mediapreview/MediaPreviewPageFragment.java:87:    public void autoPlayIfNeeded() {
```

### badges — 42 hits in 16 files

- `classes2:me/leolin/shortcutbadger/ShortcutBadger.java` (15)
- `classes2:me/leolin/shortcutbadger/impl/AsusHomeBadger.java` (3)
- `classes2:me/leolin/shortcutbadger/impl/LGHomeBadger.java` (3)
- `classes2:me/leolin/shortcutbadger/impl/DefaultBadger.java` (3)
- `classes3:org/thoughtcrime/securesms/notifications/v2/DefaultMessageNotifier.java` (3)
- `classes:androidx/core/app/RemoteInput.java` (2)
- `classes:androidx/media3/common/util/GlProgram.java` (2)
- `classes3:org/thoughtcrime/securesms/notifications/v2/NotificationBuilder.java` (2)
- `classes3:org/thoughtcrime/securesms/notifications/v2/NotificationFactory.java` (2)
- `classes2:me/leolin/shortcutbadger/impl/ZTEHomeBadger.java` (1)
- `classes2:me/leolin/shortcutbadger/impl/SonyHomeBadger.java` (1)
- `classes2:me/leolin/shortcutbadger/impl/OPPOHomeBader.java` (1)

```
classes:androidx/core/app/RemoteInput.java:29:        public static void setBadgeIconType(Notification.Builder builder) {
classes:androidx/core/app/RemoteInput.java:30:            builder.setBadgeIconType(0);
classes:androidx/media3/common/util/GlProgram.java:166:        builder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.ledARGB, not
classes:androidx/media3/common/util/GlProgram.java:358:            RemoteInput.Api26Impl.setBadgeIconType((Notification.Builder) this.uniforms);
classes2:me/leolin/shortcutbadger/impl/ZTEHomeBadger.java:18:        bundle.putInt("app_badge_count", i);
classes2:me/leolin/shortcutbadger/impl/AsusHomeBadger.java:16:    private static final String INTENT_EXTRA_ACTIVITY_NAME = "badge_count_class_name";
classes2:me/leolin/shortcutbadger/impl/AsusHomeBadger.java:17:    private static final String INTENT_EXTRA_BADGE_COUNT = "badge_count";
classes2:me/leolin/shortcutbadger/impl/AsusHomeBadger.java:18:    private static final String INTENT_EXTRA_PACKAGENAME = "badge_count_package_name";
classes2:me/leolin/shortcutbadger/impl/SonyHomeBadger.java:24:    private static final String PROVIDER_COLUMNS_BADGE_COUNT = "badge_count";
classes2:me/leolin/shortcutbadger/impl/LGHomeBadger.java:17:    private static final String INTENT_EXTRA_ACTIVITY_NAME = "badge_count_class_name";
classes2:me/leolin/shortcutbadger/impl/LGHomeBadger.java:18:    private static final String INTENT_EXTRA_BADGE_COUNT = "badge_count";
classes2:me/leolin/shortcutbadger/impl/LGHomeBadger.java:19:    private static final String INTENT_EXTRA_PACKAGENAME = "badge_count_package_name";
```

### minors_age — 0 hits in 0 files


```
```

### screen_time — 0 hits in 0 files


```
```

## UI string categories (default locale)

### loss_aversion_copy — 13 strings

```
plurals.xml:588:        <item quantity="other">"You have %1$d attempts remaining. If you run out of attempts, you can create a new PIN. You can register and use your account but you'll lose some saved settings like your profile information."</item>
plurals.xml:589:        <item quantity="one">"You have %1$d attempt remaining. If you run out of attempts, you can create a new PIN. You can register and use your account but you'll lose some saved settings like your profile information."</item>
strings.xml:1261:    <string name="CreateFoldersFragment__you_will_lose_changes">"You'll lose the changes you've made to this folder."</string>
strings.xml:1481:    <string name="DeviceTransferProgress__all_transfer_progress_will_be_lost">All transfer progress will be lost.</string>
strings.xml:1537:    <string name="DeviceTransfer__all_transfer_progress_will_be_lost">All transfer progress will be lost.</string>
strings.xml:1728:    <string name="EndGroupDialog__this_will_end_the_group_permanently">This will end the group permanently. Are you sure you want to proceed?</string>
strings.xml:2420:    <string name="MediaReviewImagePageFragment__youll_lose_any_changes">"You'll lose any changes you've made to this photo."</string>
strings.xml:2445:    <string name="MediaSendDialogs__youll_lose_any_changes">"You'll lose any changes you've made to this photo."</string>
strings.xml:2548:    <string name="MessageBackupsKeyRecordScreen__signal_will_not">Signal will not be able to help you restore your backup if you lose your key. Store it somewhere safe and secure, and do not share it with others.</string>
strings.xml:3286:    <string name="PinCreationScreen__pins_can_help">PINs can help you restore your account if you lose your phone.</string>
strings.xml:3309:    <string name="PinEntryScreen__skip_pin_entry_message">"If you can't remember your PIN, you can create a new one. You can register and use your account but you'll lose some saved settings like your profile information."</string>
strings.xml:3317:    <string name="PinRestoreEntryFragment_if_you_cant_remember_your_pin">If you can’t remember your PIN, you can create a new one. You can register and use your account but you’ll lose some saved settings like your profile information.</string>
strings.xml:3325:If you can’t remember your PIN, you can create a new one. You can register and use your account but you’ll lose some saved settings like your profile information."</string>
```

### urgency_copy — 5 strings

```
plurals.xml:628:        <item quantity="other">Your backup includes all of your text messages and your last %1$d days of media. The size will change as new media is received and old media expires.</item>
plurals.xml:629:        <item quantity="one">Your backup includes all of your text messages and your last %1$d day of media. The size will change as new media is received and old media expires.</item>
strings.xml:3334:    <string name="PinnedMessage__disappearing_message_body">Disappearing messages will be unpinned when their timer expires and the message is removed from the chat.</string>
strings.xml:3644:    <string name="RemoteBackupsSettingsFragment__expires_on_s">Expires on %1$s</string>
strings.xml:4287:    <string name="Subscription__expires_s">Expires %1$s</string>
```

### confirmshaming_copy — 39 strings

```
strings.xml:71:    <string name="AddAProfilePhotoMegaphone__not_now">Not now</string>
strings.xml:153:    <string name="AllowNotificationsScreen__not_now">Not now</string>
strings.xml:271:    <string name="BackupAlertBottomSheet__not_now">Not now</string>
strings.xml:318:    <string name="BackupMediaUpsell__not_now">Not now</string>
strings.xml:322:    <string name="BackupMessagesUpsell__not_now">Not now</string>
strings.xml:331:    <string name="BackupSchedulePermissionMegaphone__not_now">Not now</string>
strings.xml:375:    <string name="BackupStorageUpsell__not_now">Not now</string>
strings.xml:381:    <string name="BackupUpsellBottomSheet__no_thanks">No thanks</string>
strings.xml:491:    <string name="BubbleOptOutTooltip__not_now">Not now</string>
strings.xml:687:    <string name="CensorshipCircumventionMegaphone_no_thanks">No thanks</string>
strings.xml:906:    <string name="ConnectWithUsernamesDialogFragment__not_now">Not now</string>
strings.xml:937:    <string name="ContactSelectionListFragment__no_thanks">No thanks</string>
strings.xml:1065:    <string name="ConversationFragment_not_now">Not now</string>
strings.xml:1389:    <string name="DebugLogsPromptDialogFragment__no_thanks">No thanks</string>
strings.xml:1466:    <string name="DeviceSpecificNotificationBottomSheet__no_thanks">No thanks</string>
strings.xml:1565:    <string name="DonationErrorBottomSheet__not_now">Not now</string>
strings.xml:1760:    <string name="ExpiredBadgeBottomSheetDialogFragment__not_now">Not now</string>
strings.xml:1767:    <string name="ExpiredGiftSheetConfiguration__not_now">Not now</string>
strings.xml:1861:    <string name="GrantFullScreenIntentPermission_megaphone_not_now">Not now</string>
strings.xml:1870:    <string name="GrantPermissionsFragment__not_now">Not now</string>
strings.xml:1986:    <string name="GroupsV1MigrationSuggestionsReminder_no_thanks">No thanks</string>
strings.xml:2357:    <string name="MediaNoLongerAvailableSheet__not_now">Not now</string>
strings.xml:2494:    <string name="MessageBackupsEducationScreen__not_now">Not now</string>
strings.xml:2838:    <string name="MonthlyDonationCanceled__not_now_button">Not now</string>
strings.xml:2923:    <string name="NewWaysToConnectDialogFragment__not_now">Not now</string>
strings.xml:3003:    <string name="NotificationsMegaphone_not_now">Not now</string>
strings.xml:3149:    <string name="PaymentsHomeFragment__not_now">Not Now</string>
strings.xml:3215:    <string name="PaymentsSecuritySetupFragment__not_now">Not now</string>
strings.xml:3258:    <string name="Permissions_not_now">Not now</string>
strings.xml:3424:    <string name="PromptBatterySaverBottomSheet__no_thanks">No thanks</string>
strings.xml:3466:    <string name="RatingManager_no_thanks">No thanks</string>
strings.xml:3717:    <string name="RemoteRestoreScreen__not_now">Not now</string>
strings.xml:3873:    <string name="SelectContactScreen__no_thanks">No thanks</string>
strings.xml:3887:    <string name="SelfVerificationFailureSheet__no_thanks">No thanks</string>
strings.xml:4259:    <string name="SubscribeFragment__not_now">Not now</string>
strings.xml:4439:    <string name="TurnOnSignalBackups__not_now">Not now</string>
strings.xml:4584:    <string name="VerifyBackupKey__not_now">Not now</string>
strings.xml:4612:    <string name="ViewReceivedGiftSheet__not_now">Not now</string>
strings.xml:4654:    <string name="WebRtcCallActivity__not_now">Not now</string>
```

### social_pressure_copy — 4 strings

```
strings.xml:3186:    <string name="PaymentsRecoveryPhraseFragment__do_not_screenshot_or_send_by_email">Do not screenshot or send by email.</string>
strings.xml:3396:    <string name="PrivacySettingsFragment__block_screenshots_in_the_recents_list_and_inside_the_app">Block screenshots in the recents list and inside the app</string>
strings.xml:4224:    <string name="StoryViewsFragment__enable_view_receipts_to_see_whos_viewed_your_story">"Enable view receipts to see who's viewed your stories."</string>
strings.xml:5051:    <string name="firebase_database_url">https://api-project-312334754206.firebaseio.com</string>
```

### guilt_copy — 51 strings

```
strings.xml:94:    <string name="AddGroupDetailsFragment__youve_selected_a_contact_that_doesnt_support_signal_groups_mms_removal">"You've selected a contact that doesn't support Signal groups, this group will be MMS. Custom MMS group names and photos will only be visible to  [... omitted end of long
strings.xml:393:    <string name="BackupsPreferenceFragment__backups_are_encrypted_with_a_passphrase">Backups are encrypted with a passphrase and stored on your device.</string>
strings.xml:409:    <string name="BackupsSettingsFragment__automatic_backups_get_started_on_your_phone">"Automatic backups with Signal's secure end-to-end encrypted storage service. Get started on your phone."</string>
strings.xml:411:    <string name="BackupsSettingsFragment_automatic_backups_with_signals">"Automatic backups with Signal's secure end-to-end encrypted storage service."</string>
strings.xml:419:    <string name="BadDecryptLearnMoreDialog_couldnt_be_delivered_group">"A message, sticker, reaction, or read receipt couldn't be delivered to you from %s."</string>
strings.xml:420:    <string name="BadDecryptLearnMoreDialog_couldnt_be_delivered_individual">"A message, sticker, reaction, or read receipt couldn't be delivered to you from %s. They may have tried sending it to you directly, or in a group."</string>
strings.xml:421:    <string name="BadDecryptLearnMoreDialog_delivery_issue">Delivery Issue</string>
strings.xml:934:    <string name="ContactSelectionListFragment__allow_access_to_your_contacts_encrypted">Allow access to your contacts. Your contacts are encrypted and not visible to the Signal service.</string>
strings.xml:1268:    <string name="CreateKbsPinFragment__pins_can_help_you_restore_your_account">PINs can help you restore your account and keep your info encrypted with Signal.</string>
strings.xml:1310:    <string name="CreateProfileActivity_signal_profiles_are_end_to_end_encrypted">Your profile and changes to it will be visible to people you message, contacts, and groups.</string>
strings.xml:1415:    <string name="DecryptionFailedDialog_chat_session_refreshed">Chat session refreshed</string>
strings.xml:1416:    <string name="DecryptionFailedDialog_signal_uses_end_to_end_encryption">"Signal uses end-to-end encryption and it may need to refresh your chat session sometimes. This doesn't affect your chat's security, but you may have missed a message from this contact [... omitted end of lo
strings.xml:1540:    <string name="DeviceTransfer__keep_both_devices_near_each_other">Keep both devices near each other. Do not turn off the devices and keep Signal open. Transfers are end-to-end encrypted.</string>
strings.xml:1632:    <string name="EditAboutFragment_encrypted">Encrypted</string>
strings.xml:1717:    <string name="EncryptionVerifiedSheet__body_no_longer_unavailable">Signal can not automatically verify the encryption for this chat. This could be because %1$s changed their phone number or their phone number privacy settings. Verify end-to-end encryption  [... omitted end of lo
strings.xml:1718:    <string name="EncryptionVerifiedSheet__body_success">For people you’re connected to by phone number, Signal can automatically confirm whether the connection is secure using a process called key transparency. For added security, verify end-to-end encryption [... omitted end of lo
strings.xml:1719:    <string name="EncryptionVerifiedSheet__body_unavailable">Signal can only automatically verify the encryption in chats where you’re connected to someone via a phone number. If the chat was started with a username or a group in common, verify end-to-end encr [... omitted end of lo
strings.xml:1720:    <string name="EncryptionVerifiedSheet__title_no_longer_unavailable">Auto-verification is not available for this chat</string>
strings.xml:1721:    <string name="EncryptionVerifiedSheet__title_success">Encryption was auto-verified for this chat</string>
strings.xml:1722:    <string name="EncryptionVerifiedSheet__title_unavailable">Auto-verification not available for this chat</string>
strings.xml:1823:    <string name="GifQuickSearchOption__sad">Sad</string>
strings.xml:1866:    <string name="GrantPermissionsFragment__find_people_you_know">Find people you know. Your contacts are encrypted and not visible to the Signal service.</string>
strings.xml:2080:    <string name="KbsMegaphone__pins_keep_information_thats_stored_with_signal_encrytped">PINs keep information that’s stored with Signal encrypted.</string>
strings.xml:2093:    <string name="KbsSplashFragment__pins_keep_information_stored_with_signal_encrypted">"PINs keep information stored with Signal encrypted so only you can access it. Your profile, settings, and contacts will restore when you reinstall. You won't need your PI [... omitted end of lo
strings.xml:2152:    <string name="LinkDeviceFragment__messages_and_chat_info_are_protected">%1$s Messages and chat info are protected by end-to-end encryption on all devices</string>
strings.xml:2342:    <string name="MediaKeyboard__sad">Sad</string>
strings.xml:2490:    <string name="MessageBackupsEducationScreen__backup_your_messages_and_media">"Back up your messages and media using Signal's secure, end-to-end encrypted storage service. Never lose a message when you get a new phone or reinstall Signal."</string>
strings.xml:2493:    <string name="MessageBackupsEducationScreen__end_to_end_encrypted">End-to-end Encrypted</string>
strings.xml:2561:    <string name="MessageBackupsTypeSelectionScreen__all_backups_are_end_to_end_encrypted">All backups are end-to-end encrypted. Signal is a non-profit—paying for backups helps support our mission.</string>
strings.xml:2826:    <string name="MessageSyncScreen__messages_and_chat_info_are_protected_by_e2ee">Messages and chat info are protected by end-to-end encryption, including the syncing process.</string>
strings.xml:2937:    <string name="NicknameActivity__nicknames_amp_notes">Nicknames &amp; notes are stored with Signal and end-to-end encrypted. They are only visible to you.</string>
strings.xml:3056:    <string name="OnDeviceBackupsImprovementsScreen__all_backups_remain_end_to_end_encrypted">All backups remain end-to-end encrypted</string>
strings.xml:3094:    <string name="PaymentsAddMoneyFragment__add_funds">Add funds</string>
strings.xml:3095:    <string name="PaymentsAddMoneyFragment__copied_to_clipboard">Copied to clipboard</string>
strings.xml:3096:    <string name="PaymentsAddMoneyFragment__copy">Copy</string>
strings.xml:3097:    <string name="PaymentsAddMoneyFragment__learn_more__information">https://support.signal.org/hc/articles/360057625692#payments_transfer_from_exchange</string>
strings.xml:3098:    <string name="PaymentsAddMoneyFragment__to_add_funds">To add funds, send MobileCoin to your wallet address. Start a transaction from your account on an exchange that supports MobileCoin, then scan the QR code or copy your wallet address.</string>
strings.xml:3099:    <string name="PaymentsAddMoneyFragment__your_wallet_address">Your Wallet Address</string>
strings.xml:3808:    <string name="SafetyTips_detail_tip4_message">"If someone you don't know messages about cryptocurrency (like Bitcoin) or a financial opportunity, be careful—it's likely spam."</string>
strings.xml:3809:    <string name="SafetyTips_detail_tip4_title">Crypto or money scams</string>
strings.xml:3867:    <string name="SelectContactScreen__allow_access_to_your_contacts">Allow access to your contacts. Your contacts are encrypted and not visible to the Signal service.</string>
strings.xml:4020:    <string name="SignalLoginPaymentScreen__your_payment_is_still_processing">"Your payment is still processing. Come back and tap continue once it goes through, and you won't be charged again."</string>
strings.xml:4418:    <string name="TransferAccount_messages_e2e">Messages and chat info are protected by end-to-end encryption on all devices</string>
strings.xml:4581:    <string name="VerifyAutomaticallyEducationSheet__title">Signal can now auto-verify encryption</string>
strings.xml:4791:    <string name="backup_enable_dialog__backups_will_be_saved_to_external_storage_and_encrypted_with_the_passphrase_below_you_must_have_this_passphrase_in_order_to_restore_a_backup">Backups will be saved to external storage and encrypted with the passphrase be [... omitted end of lo
strings.xml:5375:    <string name="preferences__pins_keep_information_stored_with_signal_encrypted_so_only_you_can_access_it">PINs keep information stored with Signal encrypted so only you can access it. Your profile, settings, and contacts will restore when you reinstall. You [... omitted end of lo
strings.xml:5431:    <string name="preferences_automatic_key_verification_body">When enabled, Signal will attempt to automatically verify the encryption of 1:1 chats.</string>
strings.xml:5571:    <string name="verify_display_fragment__encryption_unavailable">Auto-verification unavailable</string>
strings.xml:5572:    <string name="verify_display_fragment__encryption_verified">Encryption verified</string>
strings.xml:5577:    <string name="verify_display_fragment__pnp_verify_safety_numbers_explanation_with_s">To verify end-to-end encryption with %1$s, compare the numbers above with their device. You can also scan the code on their device.</string>
strings.xml:5581:    <string name="verify_display_fragment__verifying">Verifying encryption…</string>
```

### subscription_copy — 97 strings

```
plurals.xml:35:    <plurals name="CallInfoView__plus_d_people">
plurals.xml:443:    <plurals name="MessageBackupsTypeSelectionScreen__text_plus_d_days_of_media">
plurals.xml:579:    <plurals name="PendingParticipantsView__plus_d_requests">
plurals.xml:639:    <plurals name="RemoteBackupsSettingsFragment__your_subscription_on_this_device_is_valid">
plurals.xml:640:        <item quantity="other">Your subscription on this device is valid for the next %1$d days. Renew to continue using Signal Secure Backups</item>
plurals.xml:641:        <item quantity="one">Your subscription on this device is valid for the next %1$d day. Renew to continue using Signal Secure Backups</item>
strings.xml:50:    <string name="AccountSettingsFragment__unlock_to_confirm_its_you">"Unlock to confirm it's you"</string>
strings.xml:51:    <string name="AccountSettingsFragment__unlock_to_remove_two_factor_method">Unlock to remove two-factor method</string>
strings.xml:52:    <string name="AccountSettingsFragment__unlock_to_view_signal_login">Unlock to view Signal Login</string>
strings.xml:126:    <string name="AddUsernameScreen__enter_a_maximum_of_d_digits">Invalid username, enter a maximum of %1$d digits.</string>
strings.xml:150:    <string name="AlbumThumbnailView_plus">+%d</string>
strings.xml:174:    <string name="AppSettingsFragment__couldnt_redeem_your_backups_subscription">"Couldn't redeem your backups subscription"</string>
strings.xml:176:    <string name="AppSettingsFragment__renew_your_signal_backups_subscription">Renew your Signal Secure Backups subscription</string>
strings.xml:188:    <string name="ApplicationPreferencesActivity_this_will_permanently_unlock_signal_and_message_notifications">This will permanently unlock Signal and message notifications.</string>
strings.xml:256:    <string name="BackupAlertBottomSheet__check_to_make_sure_your_payment_method">Check to make sure your payment method is up to date. Tap Manage subscription and under Payment methods tap Update.</string>
strings.xml:259:    <string name="BackupAlertBottomSheet__couldnt_redeem_your_backups_subscription">"Couldn't redeem your backups subscription"</string>
strings.xml:266:    <string name="BackupAlertBottomSheet__have_too_many_devices_using_the_same_subscription">Have too many devices using the same subscription.</string>
strings.xml:270:    <string name="BackupAlertBottomSheet__manage_subscription">Manage subscription</string>
strings.xml:279:    <string name="BackupAlertBottomSheet__too_many_devices_have_tried">Too many devices have tried to redeem your subscription this month. You may have:</string>
strings.xml:282:    <string name="BackupAlertBottomSheet__you_have_s_of_media_thats_not_on_this_device">"You have %1$s of media that's not on this device. The media and attachments stored in your backup will be permanently deleted without a paid subscription."</string>
strings.xml:284:    <string name="BackupAlertBottomSheet__your_backups_subscription_expired">Your backups subscription expired</string>
strings.xml:285:    <string name="BackupAlertBottomSheet__your_backups_subscription_failed_to_renew">Your backups subscription failed to renew</string>
strings.xml:286:    <string name="BackupAlertBottomSheet__your_backups_subscription_has_expired">Your backups subscription has expired</string>
strings.xml:287:    <string name="BackupAlertBottomSheet__your_subscription_couldnt_be_renewed">"Your subscription couldn't be renewed with your payment method. To continue backing up media you need an active subscription."</string>
strings.xml:379:    <string name="BackupUpsellBottomSheet__body">Paid Signal Secure Backup plans save all media you send and receive, up to a maximum of 100GB. Never lose a photo or video when you get a new phone or reinstall Signal.</string>
strings.xml:410:    <string name="BackupsSettingsFragment__subscription_canceled">Subscription canceled</string>
strings.xml:413:    <string name="BackupsSettingsFragment_renews_s">Renews %1$s</string>
strings.xml:414:    <string name="BackupsSettingsFragment_s_month_renews_s">%1$s/month, renews %2$s</string>
strings.xml:416:    <string name="BackupsSettingsFragment_subscription_not_found_on_this_device">Subscription not found on this device.</string>
strings.xml:823:    <string name="ChatsSettingsFragment__unlock_to_export_chat_history">Unlock to export chat history</string>
strings.xml:940:    <string name="ContactSelectionListFragment_maximum_group_size_reached">Maximum group size reached</string>
strings.xml:943:    <string name="ContactSelectionListFragment_signal_groups_can_have_a_maximum_of_s_members">Signal groups can have a maximum of %1$s members.</string>
strings.xml:1193:    <string name="ConversationTypingView__plus_d">+%1$d</string>
strings.xml:1421:    <string name="DeleteAccountFragment__canceling_your_subscription">Canceling your subscription…</string>
strings.xml:1551:    <string name="DonateToSignalFragment__bank_transfers_usually_take_1_business_day_to_process_monthly">Bank transfers can take 1 to 14 business days to process. Please wait until this payment completes before updating your subscription.</string>
strings.xml:1559:    <string name="DonateToSignalFragment__your_payment_is_still_being_processed_monthly">Your donation is still being processed. This can take a few minutes depending on your connection. Please wait until this payment completes before updating your subscriptio [... omitted end of lo
strings.xml:1591:    <string name="DonationsError__your_backups_subscription_couldnt_be_displayed">"Your backups subscription couldn't be displayed. Please contact support."</string>
strings.xml:1598:    <string name="DonationsErrors__failed_to_cancel_subscription">Failed to cancel subscription</string>
strings.xml:1602:    <string name="DonationsErrors__subscription_cancellation_requires_an_internet_connection">Subscription cancellation requires an internet connection.</string>
strings.xml:1616:    <string name="DownloadYourBackupTodayDialog__you_have_s_of_backup_data">"You have %1$s of backup data that's not on this device. Your media and attachments will be permanently deleted without a paid subscription."</string>
strings.xml:1848:    <string name="GooglePlayServicesAvailability__service_disabled_title">Paid subscriptions require Google Play</string>
strings.xml:2051:    <string name="ImageEditorToolbar__aspect_ratio_unlocked">Aspect ratio unlocked</string>
strings.xml:2098:    <string name="KeyCachingService_passphrase_cached">Signal is unlocked</string>
strings.xml:2127:    <string name="LinkAccountScreen__maximize_qr_code">Maximize QR Code</string>
strings.xml:2175:    <string name="LinkDeviceFragment__unlock_to_link">Unlock to link a device</string>
strings.xml:2266:    <string name="ManageDonationsFragment__subscription_faq">Donor FAQ</string>
strings.xml:2299:    <string name="ManageStorageSettingsFragment__storage_optimization_can_only_be_used">Storage optimization can only be used with the paid tier of Signal Secure Backups. Your backups subscription is still processing and not yet active. Please try again later. [... omitted end of lo
strings.xml:2575:    <string name="MessageBackupsTypeSelectionScreen__text_plus_all_your_media">Text + all your media</string>
strings.xml:2839:    <string name="MonthlyDonationCanceled__renew_button">Renew subscription</string>
strings.xml:2893:    <string name="MySupportPreference__checking_subscription">Checking subscription…</string>
strings.xml:2899:    <string name="MySupportPreference__renews_s">Renews %1$s</string>
strings.xml:3080:    <string name="PassphrasePromptActivity_unlock_signal">Unlock Signal</string>
strings.xml:3486:    <string name="ReactionsConversationView_plus">+%1$d</string>
strings.xml:3627:    <string name="RemoteBackupsSettingsFragment__backup_type_changed_and_subcription_deleted">Backup type changed and subscription cancelled</string>
strings.xml:3663:    <string name="RemoteBackupsSettingsFragment__renews_s">Renews %1$s</string>
strings.xml:3677:    <string name="RemoteBackupsSettingsFragment__subscription_cancelled">Subscription canceled</string>
strings.xml:3678:    <string name="RemoteBackupsSettingsFragment__subscription_inactive">Subscription inactive</string>
strings.xml:3683:    <string name="RemoteBackupsSettingsFragment__unlock_to_view_backup_key">Unlock to view recovery key</string>
strings.xml:3690:    <string name="RemoteBackupsSettingsFragment__you_can_manage_or_cancel_your_subscription_on_your_primary_device">You can manage or cancel your Signal Secure Backups subscription on your primary device.</string>
strings.xml:3691:    <string name="RemoteBackupsSettingsFragment__you_can_manage_or_renew_your_subscription_on_your_primary_device">You can manage or renew your Signal Secure Backups subscription on your primary device.</string>
strings.xml:3693:    <string name="RemoteBackupsSettingsFragment__you_can_manage_or_upgrade_your_subscription_on_your_primary_device">You can manage or upgrade your Signal Secure Backups subscription on your primary device.</string>
strings.xml:3694:    <string name="RemoteBackupsSettingsFragment__you_have_s_of_backup_data">"You have %1$s of backup data that's not on this device. Without a paid subscription media can't be offloaded."</string>
strings.xml:3700:    <string name="RemoteBackupsSettingsFragment__your_subscription_was_not_found">Your subscription was not found on this device. Renew to continue using Signal Secure Backups.</string>
strings.xml:3701:    <string name="RemoteBackupsSettingsFragment__your_subscription_will_be_canceled">"Your subscription will be canceled and you won't be charged again. Your backup will also be deleted and no new backups will be created. Any media stored in your backup will b [... omitted end of lo
strings.xml:3850:    <string name="ScreenLockSettingsFragment__your_android_device">Your Android device lock settings will be required to unlock Signal when you leave or switch apps. When locked, notification previews will not show message content.</string>
strings.xml:4256:    <string name="SubscribeFragment__cancel_subscription">Cancel Subscription</string>
strings.xml:4261:    <string name="SubscribeFragment__update_subscription">Update Subscription</string>
strings.xml:4262:    <string name="SubscribeFragment__update_subscription_question">Update subscription?</string>
strings.xml:4263:    <string name="SubscribeFragment__you_will_be_charged_the_full_amount_s_of">You will be charged the full amount (%1$s) of the new subscription price today. Your subscription will renew monthly.</string>
strings.xml:4265:    <string name="SubscribeFragment__your_subscription_has_been_cancelled">Your subscription has been cancelled.</string>
strings.xml:4277:    <string name="SubscriptionNotFoundBottomSheet__contact_support">Contact support</string>
strings.xml:4278:    <string name="SubscriptionNotFoundBottomSheet__got_it">Got it</string>
strings.xml:4279:    <string name="SubscriptionNotFoundBottomSheet__if_you_have_an_active_subscription_on">If you have an active subscription on your old phone consider canceling it before it renews.</string>
strings.xml:4280:    <string name="SubscriptionNotFoundBottomSheet__subscription_not_found">Subscription not found</string>
strings.xml:4281:    <string name="SubscriptionNotFoundBottomSheet__this_could_happen_if">This could happen if:</string>
strings.xml:4282:    <string name="SubscriptionNotFoundBottomSheet__you_transferred_from_an_iphone">You transferred from an iPhone.</string>
strings.xml:4283:    <string name="SubscriptionNotFoundBottomSheet__your_subscription_couldnt_be_restored">"Your subscription couldn't be restored."</string>
strings.xml:4284:    <string name="SubscriptionNotFoundBottomSheet__your_subscription_recently_expired">Your subscription recently expired.</string>
strings.xml:4285:    <string name="SubscriptionNotFoundBottomSheet__youre_signed_into_the_play_store_with_a_different_google_account">"You're signed into the Play Store with a different Google account."</string>
strings.xml:4286:    <string name="Subscription__contact_support">Contact Support</string>
strings.xml:4287:    <string name="Subscription__expires_s">Expires %1$s</string>
strings.xml:4288:    <string name="Subscription__get_a_s_badge">Get a %1$s badge</string>
strings.xml:4289:    <string name="Subscription__renews_s">Renews %1$s</string>
strings.xml:4290:    <string name="Subscription__s_per_month">%s/month</string>
strings.xml:4421:    <string name="TransferAccount_unlock_to_transfer">Unlock to transfer account</string>
strings.xml:4485:    <string name="UsernameEditFragment__invalid_username_enter_a_maximum_of_d_digits">Invalid username, enter a maximum of %1$d digits.</string>
strings.xml:4703:    <string name="WebRtcCallView__the_maximum_number_of_d_participants_has_been_Reached_for_this_call">The maximum number of %1$d participants has been reached for this call. Try again later.</string>
strings.xml:4775:    <string name="arrays__max">Max</string>
strings.xml:4795:    <string name="backup_subscription_management_url">https://play.google.com/store/account/subscriptions?sku=%1$s&amp;package=%2$s</string>
strings.xml:4976:    <string name="error_message_premium_account_required">Premium access required</string>
strings.xml:5081:    <string name="m3_exceed_max_badge_text_suffix">%1$s%2$s</string>
strings.xml:5225:    <string name="mtrl_exceed_max_badge_number_content_description">More than %1$d new notifications</string>
strings.xml:5226:    <string name="mtrl_exceed_max_badge_number_suffix">%1$d%2$s</string>
strings.xml:5509:    <string name="prompt_passphrase_activity__screen_lock_is_on">Screen lock is on and Signal is safely secured with your device lock settings. Unlock Signal the same way as you would normally unlock your phone, this could be with Face Unlock, Fingerprint Unlo [... omitted end of lo
strings.xml:5511:    <string name="prompt_passphrase_activity__unlock">Unlock</string>
strings.xml:5512:    <string name="prompt_passphrase_activity__unlock_signal">Unlock Signal</string>
strings.xml:5513:    <string name="prompt_passphrase_activity__use_your_android_device">Use your Android device lock settings to unlock Signal.</string>
```

### data_copy — 161 strings

```
plurals.xml:92:        <item quantity="other">Another attempt to process your contacts will be made within %1$d days.</item>
plurals.xml:93:        <item quantity="one">Another attempt to process your contacts will be made within %1$d day.</item>
plurals.xml:147:    <plurals name="ContactSearchItems__custom_story_d_viewers">
plurals.xml:151:    <plurals name="ContactSearchItems__group_d_members">
plurals.xml:155:    <plurals name="ContactSearchItems__group_story_d_viewers">
plurals.xml:159:    <plurals name="ContactSearchItems__my_story_s_dot_d_excluded">
plurals.xml:163:    <plurals name="ContactSearchItems__my_story_s_dot_d_viewers">
plurals.xml:167:    <plurals name="ContactSelectionListFragment_d_members">
plurals.xml:595:    <plurals name="PrivacySettingsFragment__d_contacts">
plurals.xml:596:        <item quantity="other">%1$d contacts or groups</item>
plurals.xml:656:        <item quantity="other">"If you're not sure who the request is from, review the contacts below and take action."</item>
plurals.xml:743:    <plurals name="UserNotificationMigrationJob_d_contacts_are_on_signal">
plurals.xml:744:        <item quantity="other">%d contacts are on Signal!</item>
strings.xml:9:    <string name="AboutSheet__s_is_in_your_system_contacts">%1$s is in your phone contacts</string>
strings.xml:103:    <string name="AddLinkDeviceFragment__this_device_will_see_your_groups_contacts">This device will be able to see your groups and contacts, access your chats, and send messages in your name.</string>
strings.xml:160:    <string name="AndroidManifest__select_contacts">Select contacts</string>
strings.xml:208:    <string name="AttachmentKeyboard_location">Location</string>
strings.xml:220:    <string name="AttachmentManager_signal_allow_access_location">Allow access to your location</string>
strings.xml:221:    <string name="AttachmentManager_signal_allow_signal_access_location">Allow Signal access to send your location.</string>
strings.xml:223:    <string name="AttachmentManager_signal_needs_location_access">Signal needs location access to send your location.</string>
strings.xml:225:    <string name="AttachmentManager_signal_requires_contacts_permission_in_order_to_attach_contact_information">Signal requires Contacts permission in order to attach contact information, but it has been permanently denied. Please continue to the app settings  [... omitted end of lon
strings.xml:226:    <string name="AttachmentManager_signal_requires_location_information_in_order_to_attach_a_location">Signal requires Location permission in order to attach a location, but it has been permanently denied. Please continue to the app settings menu, select \"Pe [... omitted end of lon
strings.xml:228:    <string name="AttachmentManager_signal_to_send_location">To send your location:</string>
strings.xml:309:    <string name="BackupDialog_to_enable_backups_choose_a_folder">To enable backups, choose a folder. Backups will be saved to this location.</string>
strings.xml:452:    <string name="BecomeASustainerFragment__signal_is_a_non_profit">Signal is a nonprofit with no advertisers or investors, supported only by people like you.</string>
strings.xml:506:    <string name="CallInfoView__before_joining_a_call">"Before joining a call you can only see the names of phone contacts, people you're in a group with, or people you've chatted with 1:1. You'll see all names and photos once you've joined the call."</string> [... omitted end of lon
strings.xml:650:    <string name="CameraContacts__menu_search">Search</string>
strings.xml:680:    <string name="CdsPermanentErrorBottomSheet_body">The number of contacts on your phone exceeds the limit Signal can process. To find contacts on Signal, consider removing contacts or accounts on your phone that are syncing a lot of contacts.</string>
strings.xml:681:    <string name="CdsPermanentErrorBottomSheet_contacts_button">Open contacts</string>
strings.xml:683:    <string name="CdsPermanentErrorBottomSheet_no_contacts_toast">No contacts app found</string>
strings.xml:684:    <string name="CdsPermanentErrorBottomSheet_title">"Your contacts can't be processed"</string>
strings.xml:685:    <string name="CdsTemporaryErrorBottomSheet_body2">To resolve this issue sooner, you can consider removing contacts or accounts on your phone that are syncing a lot of contacts.</string>
strings.xml:686:    <string name="CdsTemporaryErrorBottomSheet_title">Too many contacts have been processed</string>
strings.xml:922:    <string name="ContactSearchItems__delete_story">Delete story</string>
strings.xml:923:    <string name="ContactSearchItems__only_share_with">Only share with</string>
strings.xml:924:    <string name="ContactSearchItems__remove_story">Remove story</string>
strings.xml:925:    <string name="ContactSearchItems__story_settings">Story settings</string>
strings.xml:926:    <string name="ContactSearchItems__tap_to_choose_your_viewers">Tap to choose your viewers</string>
strings.xml:927:    <string name="ContactSearchMediator__delete">Delete</string>
strings.xml:928:    <string name="ContactSearchMediator__delete_story">Delete story?</string>
strings.xml:929:    <string name="ContactSearchMediator__delete_the_custom">Delete the custom story \"%1$s\"?</string>
strings.xml:930:    <string name="ContactSearchMediator__remove">Remove</string>
strings.xml:931:    <string name="ContactSearchMediator__remove_group_story">Remove group story?</string>
strings.xml:932:    <string name="ContactSearchMediator__this_will_remove">This will remove the story from this list. You will still be able to view stories from this group.</string>
strings.xml:933:    <string name="ContactSelectionListFragment__allow_access">Allow access</string>
strings.xml:934:    <string name="ContactSelectionListFragment__allow_access_to_your_contacts_encrypted">Allow access to your contacts. Your contacts are encrypted and not visible to the Signal service.</string>
strings.xml:935:    <string name="ContactSelectionListFragment__find_by_phone_number">Find by phone number</string>
strings.xml:936:    <string name="ContactSelectionListFragment__find_by_username">Find by username</string>
strings.xml:937:    <string name="ContactSelectionListFragment__no_thanks">No thanks</string>
strings.xml:938:    <string name="ContactSelectionListFragment_allow_access_contacts">Allow access to contacts</string>
strings.xml:939:    <string name="ContactSelectionListFragment_error_retrieving_contacts_check_your_network_connection">Error retrieving contacts, check your network connection</string>
strings.xml:940:    <string name="ContactSelectionListFragment_maximum_group_size_reached">Maximum group size reached</string>
strings.xml:941:    <string name="ContactSelectionListFragment_recommended_member_limit_reached">Recommended member limit reached</string>
strings.xml:942:    <string name="ContactSelectionListFragment_s_is_not_a_signal_user">%1$s is not a Signal user. Please check the username and try again.</string>
strings.xml:943:    <string name="ContactSelectionListFragment_signal_groups_can_have_a_maximum_of_s_members">Signal groups can have a maximum of %1$s members.</string>
strings.xml:944:    <string name="ContactSelectionListFragment_signal_groups_perform_best_with_s_members_or_fewer">Signal groups perform best with %1$s members or fewer. Adding more members will cause delays sending and receiving messages.</string>
strings.xml:945:    <string name="ContactSelectionListFragment_signal_requires_the_contacts_permission_in_order_to_display_your_contacts">Signal requires the Contacts permission in order to display your contacts, but it has been permanently denied. Please continue to the app  [... omitted end of lon
strings.xml:946:    <string name="ContactSelectionListFragment_to_find_people">To find people you know on Signal:</string>
strings.xml:947:    <string name="ContactSelectionListFragment_username_not_found">Username not found</string>
strings.xml:948:    <string name="ContactSelectionListFragment_you_do_not_need_to_add_yourself_to_the_group">You do not need to add yourself to the group</string>
strings.xml:949:    <string name="ContactShareEditActivity_invalid_contact">Selected contact was invalid</string>
strings.xml:950:    <string name="ContactShareEditActivity_type_home">Home</string>
strings.xml:951:    <string name="ContactShareEditActivity_type_missing">Other</string>
strings.xml:952:    <string name="ContactShareEditActivity_type_mobile">Mobile</string>
strings.xml:953:    <string name="ContactShareEditActivity_type_work">Work</string>
strings.xml:954:    <string name="ContactSupportDialog__submit_debug_log">Submit debug log?</string>
strings.xml:955:    <string name="ContactSupportDialog__submit_with_debug_log">Submit with debug log</string>
strings.xml:956:    <string name="ContactSupportDialog__submit_without_debug_log">Submit without debug log</string>
strings.xml:957:    <string name="ContactSupportDialog__your_debug_logs">Your debug logs will help us troubleshoot your issue faster. Submitting your logs is optional.</string>
strings.xml:958:    <string name="ContactSupportDialog_submit_debug_log">Submit debug log?</string>
strings.xml:959:    <string name="ContactSupportDialog_submit_with_debug">Submit with debug log</string>
strings.xml:960:    <string name="ContactSupportDialog_submit_without_debug">Submit without debug log</string>
strings.xml:961:    <string name="ContactSupportDialog_your_debug_logs">Your debug logs will help us troubleshoot your issue faster. Submitting your logs is optional.</string>
strings.xml:962:    <string name="ContactsCursorLoader__chat_types">Chat types</string>
strings.xml:963:    <string name="ContactsCursorLoader__chats">Chats</string>
strings.xml:964:    <string name="ContactsCursorLoader__messages">Messages</string>
strings.xml:965:    <string name="ContactsCursorLoader_contacts">Contacts</string>
strings.xml:966:    <string name="ContactsCursorLoader_group_members">Group members</string>
strings.xml:967:    <string name="ContactsCursorLoader_groups">Groups</string>
strings.xml:968:    <string name="ContactsCursorLoader_my_stories">My Stories</string>
strings.xml:969:    <string name="ContactsCursorLoader_new">New</string>
strings.xml:970:    <string name="ContactsCursorLoader_recent_chats">Recent chats</string>
strings.xml:971:    <string name="ContactsDatabase_message_s">Message %s</string>
strings.xml:972:    <string name="ContactsDatabase_signal_call_s">Signal Voice Call %s</string>
strings.xml:973:    <string name="ContactsDatabase_signal_video_call_s">Signal Video Call %s</string>
strings.xml:1031:    <string name="ConversationFragment__contacts_app_not_found">Contacts app not found.</string>
strings.xml:1159:    <string name="ConversationSettingsFragment__contacts_app_not_found">Contacts app not found</string>
strings.xml:1310:    <string name="CreateProfileActivity_signal_profiles_are_end_to_end_encrypted">Your profile and changes to it will be visible to people you message, contacts, and groups.</string>
strings.xml:1494:    <string name="DeviceTransferSetup__grant_location_permission">Grant location permission</string>
strings.xml:1497:    <string name="DeviceTransferSetup__location_permission">Location permission</string>
strings.xml:1498:    <string name="DeviceTransferSetup__location_permission_required">Signal needs the location permission to discover and connect with your old device.</string>
strings.xml:1499:    <string name="DeviceTransferSetup__location_services">Location services</string>
strings.xml:1500:    <string name="DeviceTransferSetup__location_services_required">Signal needs location services enabled to discover and connect with your old device.</string>
strings.xml:1515:    <string name="DeviceTransferSetup__troubleshooting_tips">"• Make sure location permissions are granted.
strings.xml:1521:    <string name="DeviceTransferSetup__turn_on_location_services">Turn on location services</string>
strings.xml:1621:    <string name="DraftDatabase_Draft_location_snippet">(location)</string>
strings.xml:1858:    <string name="GrantFullScreenIntentPermission_bottomsheet_subtitle">To receive call notifications from your contacts and groups:</string>
strings.xml:1860:    <string name="GrantFullScreenIntentPermission_megaphone_body">Never miss a call from your contacts and groups.</string>
strings.xml:1865:    <string name="GrantPermissionsFragment__contacts">Contacts</string>
strings.xml:1866:    <string name="GrantPermissionsFragment__find_people_you_know">Find people you know. Your contacts are encrypted and not visible to the Signal service.</string>
strings.xml:2093:    <string name="KbsSplashFragment__pins_keep_information_stored_with_signal_encrypted">"PINs keep information stored with Signal encrypted so only you can access it. Your profile, settings, and contacts will restore when you reinstall. You won't need your PI [... omitted end of lo
strings.xml:2275:    <string name="ManageGroupActivity_this_is_an_insecure_mms_group">This is an insecure MMS Group. To chat privately, invite your contacts to Signal.</string>
strings.xml:2477:    <string name="MemberSearchFragment__filter_contacts">Contacts</string>
strings.xml:2480:    <string name="MemberSearchFragment__search_contacts">Search contacts</string>
strings.xml:2524:    <string name="MessageBackupsKeyRecordScreen__creating_a_new_key_is_only_necessary">Creating a new key is only necessary if someone else knows your key. You will have to re-upload your backup, including media. If you are using \"Optimize Signal storage\" yo [... omitted end of lo
strings.xml:2930:    <string name="NewWaysToConnectDialogFragment__your_phone_number_is_no_longer_shared">"Your phone number is no longer shared with chats. If your number is saved to a friend's contacts, they will still see it."</string>
strings.xml:3002:    <string name="NotificationsMegaphone_never_miss_a_message">Never miss a message from your contacts and groups.</string>
strings.xml:3050:    <string name="OldDeviceTransferSetup__signal_needs_location_services_enabled_to_discover_and_connect_with_your_new_device">Signal needs location services enabled to discover and connect with your new Android device.</string>
strings.xml:3051:    <string name="OldDeviceTransferSetup__signal_needs_the_location_permission_to_discover_and_connect_with_your_new_device">Signal needs the location permission to discover and connect to your new Android device.</string>
strings.xml:3267:    <string name="PhoneNumberPrivacySettingsFragment_sharing_off_discovery_on_description">"Your phone number will not be visible to anyone unless they have it saved in their phone's contacts."</string>
strings.xml:3412:    <string name="ProfileCreateFragment__profiles_are_visible_to_contacts_and_people_you_message">Profiles are visible to people you message, contacts, and groups.</string>
strings.xml:3495:    <string name="RecipientBottomSheet_add_to_contacts">Add to contacts</string>
strings.xml:3506:    <string name="RecipientBottomSheet_unable_to_open_contacts">"Can't find an app able to open contacts."</string>
strings.xml:3745:    <string name="ResetRecoveryKeyBottomSheet__if_backups_are_enabled_you_will_have_to_re_upload">If backups are enabled you will have to re-upload your backup, including media. If you are using \"Optimize Signal storage\" you will have to download offloaded m [... omitted end of lo
strings.xml:3771:    <string name="ReviewCard__s_is_in_your_system_contacts">%1$s is in your phone contacts</string>
strings.xml:3784:    <string name="SafetyNumberBucketRowItem__contacts">Contacts</string>
strings.xml:3865:    <string name="SelectContactScreen__allow_access">Allow access</string>
strings.xml:3866:    <string name="SelectContactScreen__allow_access_to_contacts">Allow access to contacts</string>
strings.xml:3867:    <string name="SelectContactScreen__allow_access_to_your_contacts">Allow access to your contacts. Your contacts are encrypted and not visible to the Signal service.</string>
strings.xml:3868:    <string name="SelectContactScreen__clear_search">Clear search</string>
strings.xml:3869:    <string name="SelectContactScreen__couldnt_open_contact">"Couldn't open that contact"</string>
strings.xml:3870:    <string name="SelectContactScreen__find_people_you_know_on_signal">Find people you know on Signal</string>
strings.xml:3871:    <string name="SelectContactScreen__in_your_contacts">In your contacts</string>
strings.xml:3872:    <string name="SelectContactScreen__learn_more">Learn more</string>
strings.xml:3873:    <string name="SelectContactScreen__no_thanks">No thanks</string>
strings.xml:3874:    <string name="SelectContactScreen__open_phone_contacts">Open phone contacts</string>
strings.xml:3875:    <string name="SelectContactScreen__search">Search</string>
strings.xml:3876:    <string name="SelectContactScreen__select_contact">Select contact</string>
strings.xml:3877:    <string name="SelectContactScreen__to_find_people_you_know_on_signal">To find people you know on Signal:</string>
strings.xml:3878:    <string name="SelectContactScreen__to_see_your_phone_contacts_here">To see your phone contacts here, allow access in your device settings. %1$s</string>
strings.xml:3907:    <string name="ShareActivity__could_not_get_share_data_from_intent">Could not get share data from intent.</string>
strings.xml:3910:    <string name="ShareContactScreen__change_photo">Change photo</string>
strings.xml:3911:    <string name="ShareContactScreen__company">Company</string>
strings.xml:3912:    <string name="ShareContactScreen__done">Done</string>
strings.xml:3913:    <string name="ShareContactScreen__edit_name">Edit name</string>
strings.xml:3914:    <string name="ShareContactScreen__nickname">Nickname</string>
strings.xml:3915:    <string name="ShareContactScreen__notes">Notes</string>
strings.xml:3916:    <string name="ShareContactScreen__select_a_photo_to_share">Select a photo to share</string>
strings.xml:3917:    <string name="ShareContactScreen__send">Send</string>
strings.xml:3918:    <string name="ShareContactScreen__share_contact">Share contact</string>
strings.xml:3930:    <string name="SharedContactDetailsScreen__add_to_phone_contacts">Add to phone contacts</string>
strings.xml:3935:    <string name="SharedContactDetailsScreen__couldnt_open_contacts">"Couldn't open Contacts"</string>
strings.xml:3943:    <string name="SharedContactView_add_to_contacts">Add to Contacts</string>
strings.xml:3953:    <string name="SignalConnectionsBottomSheet__having_them_in_your_system_contacts">Having them in your phone contacts</string>
strings.xml:4030:    <string name="SignalLoginViewDetailsScreen__cant_save_pdf_to_the_selected_location">"Can't save PDF to the selected location."</string>
strings.xml:4051:    <string name="SingleContactSelectionActivity_contact_photo">Contact Photo</string>
strings.xml:4413:    <string name="TransferAccount_body">Your account will be transferred to a new device. This device will be able to see your groups and contacts, access your chats, and send messages in your name. %1$s</string>
strings.xml:4578:    <string name="VerifyAutomaticallyEducationSheet__body">For contacts you’re connected to by phone number, Signal can automatically confirm whether the connection is secure using a process called key transparency. For added security, you can still verify con [... omitted end of lo
strings.xml:4604:    <string name="ViewBadgeBottomSheetDialogFragment__s_supports_signal_with_a_donation">%1$s supports Signal with a donation. Signal is a nonprofit with no advertisers or investors, supported only by people like you.</string>
strings.xml:4605:    <string name="ViewBadgeBottomSheetDialogFragment__s_supports_signal_with_a_monthly">%1$s supports Signal with a monthly donation. Signal is a nonprofit with no advertisers or investors, supported only by people like you.</string>
strings.xml:4853:    <string name="contact_selection_activity__allow_access_to_contacts">Allow access to your contacts</string>
strings.xml:4859:    <string name="contact_selection_activity__refresh_contacts">Refresh contacts</string>
strings.xml:4860:    <string name="contact_selection_group_activity__finding_contacts">Loading contacts…</string>
strings.xml:4861:    <string name="contact_selection_group_activity__no_contacts">No contacts.</string>
strings.xml:4887:    <string name="conversation_add_to_contacts__menu_add_to_contacts">Add to contacts</string>
strings.xml:5375:    <string name="preferences__pins_keep_information_stored_with_signal_encrypted_so_only_you_can_access_it">PINs keep information stored with Signal encrypted so only you can access it. Your profile, settings, and contacts will restore when you reinstall. You [... omitted end of lo
strings.xml:5383:    <string name="preferences__request_keyboard_to_disable">Request keyboard to disable personalized learning.</string>
strings.xml:5446:    <string name="preferences_communication__censorship_circumvention_if_enabled_signal_will_attempt_to_circumvent_censorship">If enabled, Signal will attempt to circumvent censorship. Do not enable this feature unless you are in a location where Signal is cen [... omitted end of lo
strings.xml:5450:    <string name="preferences_communication__sealed_sender_allow_from_anyone_description">Enable sealed sender for incoming messages from non-contacts and people with whom you have not shared your profile.</string>
strings.xml:5519:    <string name="reminder_cds_permanent_error_body">"Signal's private contact discovery can't process your phone's contacts."</string>
strings.xml:5521:    <string name="reminder_cds_warning_body">"Signal's private contact discovery temporarily can't process your phone's contacts."</string>
```

