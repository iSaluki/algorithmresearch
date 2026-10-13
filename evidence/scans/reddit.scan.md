# Pattern scan: work/reddit/jadx

## Code categories (library packages excluded)

### installed_apps — 27 hits in 22 files

- `defpackage/i7p0.java` (3)
- `com/google/android/gms/common/c.java` (3)
- `com/reddit/webembed/util/b.java` (2)
- `defpackage/ezo0.java` (1)
- `defpackage/dtp0.java` (1)
- `defpackage/ecq0.java` (1)
- `defpackage/wwp0.java` (1)
- `defpackage/jip0.java` (1)
- `defpackage/mcf0.java` (1)
- `defpackage/b2i0.java` (1)
- `defpackage/fsp0.java` (1)
- `defpackage/fxp0.java` (1)

```
defpackage/ezo0.java:28:                    if (yyo0.b(context.getPackageManager().getPackageInfo("com.android.vending", 64).signatures)) {
defpackage/dtp0.java:27:            installedPackages = this.a.getPackageManager().getInstalledPackages(0);
defpackage/ecq0.java:34:                Signature[] signatureArr = context.getPackageManager().getPackageInfo("com.android.vending", 64).signatures;
defpackage/wwp0.java:26:                Signature[] signatureArr = context.getPackageManager().getPackageInfo("com.android.vending", 64).signatures;
defpackage/jip0.java:30:                Signature[] signatureArr = context.getPackageManager().getPackageInfo("com.android.vending", 64).signatures;
defpackage/mcf0.java:55:            Iterator<ResolveInfo> it = context.getPackageManager().queryIntentActivities(intent, 65536).iterator();
defpackage/i7p0.java:69:                    context.getPackageManager().getPackageInfo("com.google.android.engage.verifyapp", 0);
defpackage/i7p0.java:88:                i2 = context.getPackageManager().getPackageInfo("com.android.vending", 0).versionCode;
defpackage/i7p0.java:94:                i4 = context.getPackageManager().getPackageInfo("com.android.vending", 0).versionCode;
defpackage/b2i0.java:131:            packageInfo = context.getPackageManager().getPackageInfo("com.android.vending", 64);
defpackage/fsp0.java:19:                    if (dcq0.a(context.getPackageManager().getPackageInfo("com.android.vending", 64).signatures)) {
defpackage/fxp0.java:375:                            List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(new Intent("android.intent.action.VIEW", Uri.parse(strOptString)), 0);
```

### usage_stats — 2 hits in 1 files

- `defpackage/z090.java` (2)

```
defpackage/z090.java:3:import android.app.usage.UsageStatsManager;
defpackage/z090.java:18:        int appStandbyBucket = ((UsageStatsManager) this.a.getSystemService("usagestats")).getAppStandbyBucket();
```

### clipboard — 3 hits in 3 files

- `androidx/compose/foundation/text/input/internal/selection/c.java` (1)
- `defpackage/g33.java` (1)
- `defpackage/ke2.java` (1)

```
androidx/compose/foundation/text/input/internal/selection/c.java:411:        boolean zHasPrimaryClip = ke2Var.a.a().hasPrimaryClip();
defpackage/g33.java:230:        ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
defpackage/ke2.java:16:        ClipData primaryClip = this.a.a().getPrimaryClip();
```

### contacts — 4 hits in 1 files

- `defpackage/gfg0.java` (4)

```
defpackage/gfg0.java:6:import android.provider.ContactsContract;
defpackage/gfg0.java:46:            Uri uriLookupContact = ContactsContract.Contacts.lookupContact(contentResolver, uri);
defpackage/gfg0.java:50:            inputStreamOpenContactPhotoInputStream = ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uriLookupContact, true);
defpackage/gfg0.java:52:            inputStreamOpenContactPhotoInputStream = ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uri, true);
```

### call_log — 0 hits in 0 files


```
```

### sms — 4 hits in 4 files

- `defpackage/eap0.java` (1)
- `defpackage/qqp0.java` (1)
- `defpackage/qbn0.java` (1)
- `defpackage/h5f0.java` (1)

```
defpackage/eap0.java:9:        String[] strArr = {"SmsRetrieverHelper"};
defpackage/qqp0.java:24:                attachInterface(this, "com.google.android.gms.auth.api.phone.internal.ISmsRetrieverResultCallback");
defpackage/qbn0.java:328:        parcelObtain.writeInterfaceToken("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService");
defpackage/h5f0.java:99:            return Telephony.Sms.getDefaultSmsPackage(this.a);
```

### location — 0 hits in 0 files


```
```

### wifi_bt_scan — 1 hits in 1 files

- `org/chromium/net/AndroidNetworkLibrary.java` (1)

```
org/chromium/net/AndroidNetworkLibrary.java:154:        return (wifiInfoB == null || (ssid = wifiInfoB.getSSID()) == null || ssid.equals("<unknown ssid>")) ? "" : ssid;
```

### device_ids — 29 hits in 18 files

- `androidx/core/widget/NestedScrollView.java` (3)
- `defpackage/khp0.java` (3)
- `defpackage/z5g.java` (3)
- `com/appsflyer/internal/AFg1oSDK.java` (2)
- `androidx/compose/ui/platform/c.java` (2)
- `com/reddit/data/common/client/platform/Platform.java` (2)
- `defpackage/ft70.java` (2)
- `defpackage/r000.java` (2)
- `com/google/android/recaptcha/internal/zzcx.java` (1)
- `com/appsflyer/internal/AFg1tSDK.java` (1)
- `com/appsflyer/share/deeplink/DeepLink.java` (1)
- `defpackage/a5f.java` (1)

```
com/google/android/recaptcha/internal/zzcx.java:43:        Cursor cursorQuery = this.zza.a.query(Uri.parse("content://com.google.android.gsf.gservices"), null, null, new String[]{"android_id"}, null);
com/appsflyer/internal/AFg1tSDK.java:235:                        if (map.remove("android_id") != null) {
com/appsflyer/internal/AFg1oSDK.java:178:            String string = Settings.Secure.getString(this.AFLogger.getContentResolver(), "android_id");
com/appsflyer/internal/AFg1oSDK.java:1542:            map.put("android_id", strD);
com/appsflyer/share/deeplink/DeepLink.java:35:        setKeySet.removeAll(Arrays.asList("install_time", "pid", "c", "af_prt", "af_mp", "clickid", "af_siteid", "af_sub_siteid", "af_click_lookback", "af_viewthrough_lookback", "af_keywords", "af_cost_model", "af_cost_currency", "af_cost_value", "af_r",
androidx/core/widget/NestedScrollView.java:1313:            getScrollFeedbackProvider().a.onScrollProgress(motionEvent.getDeviceId(), motionEvent.getSource(), i2, scrollY2);
androidx/core/widget/NestedScrollView.java:1327:                    getScrollFeedbackProvider().a.onScrollLimit(motionEvent.getDeviceId(), motionEvent.getSource(), i2, false);
androidx/core/widget/NestedScrollView.java:1354:                getScrollFeedbackProvider().a.onScrollLimit(motionEvent.getDeviceId(), motionEvent.getSource(), i2, true);
androidx/compose/ui/platform/c.java:945:        MotionEvent motionEventObtain = MotionEvent.obtain(motionEvent.getDownTime() == motionEvent.getEventTime() ? j : motionEvent.getDownTime(), j, i, pointerCount, pointerPropertiesArr, pointerCoordsArr, motionEvent.getMetaState(), z ? 0 : motionEvent.getB
androidx/compose/ui/platform/c.java:1563:            motionEvent.getDeviceId();
defpackage/a5f.java:111:        if (Build.VERSION.SDK_INT >= 34 && context != null && (deviceId = context.getDeviceId()) != 0 && deviceId != -1) {
com/reddit/data/common/client/platform/Platform.java:76:        this.deviceId_ = getDefaultInstance().getDeviceId();
```

### gsf_id — 1 hits in 1 files

- `com/google/android/recaptcha/internal/zzcx.java` (1)

```
com/google/android/recaptcha/internal/zzcx.java:43:        Cursor cursorQuery = this.zza.a.query(Uri.parse("content://com.google.android.gsf.gservices"), null, null, new String[]{"android_id"}, null);
```

### advertising_id — 107 hits in 21 files

- `androidx/privacysandbox/ads/adservices/measurement/MeasurementManagerImplCommon.java` (15)
- `com/google/android/gms/ads/identifier/AdvertisingIdClient.java` (12)
- `androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl.java` (9)
- `androidx/privacysandbox/ads/adservices/measurement/MeasurementManagerImplCommon$registerSource$4.java` (6)
- `androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$registerSourceAsync$2.java` (6)
- `androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$registerTriggerAsync$1.java` (6)
- `androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$registerWebSourceAsync$1.java` (6)
- `androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$registerWebTriggerAsync$1.java` (6)
- `androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$deleteRegistrationsAsync$1.java` (6)
- `androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$registerSourceAsync$1.java` (6)
- `androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures$Api33Ext5JavaImpl$getMeasurementApiStatusAsync$1.java` (6)
- `defpackage/a3u.java` (4)

```
com/reddit/ads/impl/device/GoogleDeviceAdIdProvider$fetchDeviceAdId$2.java:4:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
com/reddit/ads/impl/device/GoogleDeviceAdIdProvider$fetchDeviceAdId$2.java:60:            AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.this$0.a);
com/reddit/ads/impl/operator/b.java:7:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
com/reddit/ads/impl/operator/b.java:60:            AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(context);
com/appsflyer/internal/AFe1iSDK.java:8:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
com/appsflyer/internal/AFe1iSDK.java:454:            AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(p0);
com/google/android/gms/measurement/internal/b.java:14:import androidx.privacysandbox.ads.adservices.java.measurement.MeasurementManagerFutures$Api33Ext5JavaImpl;
com/google/android/gms/measurement/internal/b.java:386:        MeasurementManagerFutures$Api33Ext5JavaImpl measurementManagerFutures$Api33Ext5JavaImpl = caq0Var.i;
com/google/android/gms/ads/identifier/zza.java:11:    public zza(AdvertisingIdClient advertisingIdClient, Map map) {
com/google/android/gms/ads/identifier/AdvertisingIdClient.java:27:public class AdvertisingIdClient {
com/google/android/gms/ads/identifier/AdvertisingIdClient.java:29:    private static volatile AdvertisingIdClient zzh;
com/google/android/gms/ads/identifier/AdvertisingIdClient.java:62:    public AdvertisingIdClient(Context context, long j, boolean z, boolean z2) {
```

### install_referrer — 36 hits in 6 files

- `com/android/installreferrer/api/b.java` (17)
- `com/appsflyer/internal/AFi1gSDK.java` (12)
- `com/android/installreferrer/api/InstallReferrerClient.java` (3)
- `com/android/installreferrer/api/a.java` (2)
- `com/android/installreferrer/api/ReferrerDetails.java` (1)
- `com/android/installreferrer/api/InstallReferrerClientImpl$ClientState.java` (1)

```
com/android/installreferrer/api/a.java:32:        InstallReferrerCommons.logVerbose("InstallReferrerClient", "Install Referrer service connected.");
com/android/installreferrer/api/a.java:48:        InstallReferrerCommons.logWarn("InstallReferrerClient", "Install Referrer service disconnected.");
com/android/installreferrer/api/ReferrerDetails.java:33:    public String getInstallReferrer() {
com/android/installreferrer/api/InstallReferrerClientImpl$ClientState.java:9:public @interface InstallReferrerClientImpl$ClientState {
com/android/installreferrer/api/InstallReferrerClient.java:10:public abstract class InstallReferrerClient {
com/android/installreferrer/api/InstallReferrerClient.java:21:        public InstallReferrerClient build() {
com/android/installreferrer/api/InstallReferrerClient.java:49:    public abstract ReferrerDetails getInstallReferrer();
com/android/installreferrer/api/b.java:19:public final class b extends InstallReferrerClient {
com/android/installreferrer/api/b.java:29:    @Override // com.android.installreferrer.api.InstallReferrerClient
com/android/installreferrer/api/b.java:33:            InstallReferrerCommons.logVerbose("InstallReferrerClient", "Unbinding from service.");
com/android/installreferrer/api/b.java:40:    @Override // com.android.installreferrer.api.InstallReferrerClient
com/android/installreferrer/api/b.java:41:    public final ReferrerDetails getInstallReferrer() throws RemoteException {
```

### sensors — 0 hits in 0 files


```
```

### accounts — 19 hits in 15 files

- `defpackage/pp70.java` (3)
- `defpackage/jp70.java` (2)
- `org/chromium/net/HttpNegotiateAuthenticator.java` (2)
- `com/reddit/domain/model/GetAccountsByTokenResponse.java` (1)
- `defpackage/xy80.java` (1)
- `com/reddit/session/diagnostics/c.java` (1)
- `com/reddit/session/ui/external/ExternalAuthActivity.java` (1)
- `com/reddit/data/repository/e.java` (1)
- `com/reddit/auth/login/domain/usecase/x.java` (1)
- `com/reddit/auth/login/data/local/c.java` (1)
- `com/reddit/auth/login/data/local/b.java` (1)
- `com/reddit/auth/login/model/sso/SsoAccountResponse.java` (1)

```
com/reddit/domain/model/GetAccountsByTokenResponse.java:46:    public final List<GetAccountsByTokenAccount> getAccounts() {
defpackage/jp70.java:47:            AccountManager accountManager = AccountManager.get(this.a.getApplicationContext());
defpackage/jp70.java:49:            Account[] accountsByType = accountManager.getAccountsByType("com.reddit.account");
defpackage/xy80.java:42:                        AccountManager.get(applicationContext).addAccountExplicitly(account2, null, null);
com/reddit/session/diagnostics/c.java:85:                zliVar = new yyh0(Integer.valueOf(accountManager.getAccountsByType("com.reddit.account").length));
com/reddit/session/ui/external/ExternalAuthActivity.java:101:                            AccountManager accountManager = AccountManager.get(applicationContext.getApplicationContext());
com/reddit/data/repository/e.java:210:        if (getAccountsByTokenResponse == null || (accounts = getAccountsByTokenResponse.getAccounts()) == null) {
com/reddit/auth/login/domain/usecase/x.java:545:                List<SsoAccount> accounts = accountResponse.getAccounts();
com/reddit/auth/login/data/local/c.java:313:                Account[] accountsByType = accountManager.getAccountsByType("com.reddit.account");
com/reddit/auth/login/data/local/b.java:225:                Account[] accountsByType = accountManager.getAccountsByType("com.reddit.account");
com/reddit/auth/login/model/sso/SsoAccountResponse.java:28:    public final List getAccounts() {
defpackage/pp70.java:38:            zAddAccountExplicitly = AccountManager.get(applicationContext).addAccountExplicitly(new Account("Reddit for Android", "com.reddit.account"), null, null);
```

### battery_state — 0 hits in 0 files


```
```

### screen_capture_detect — 35 hits in 17 files

- `com/reddit/type/UxTargetingExperience.java` (4)
- `com/reddit/sharing/screenshot/c.java` (3)
- `com/reddit/domain/model/experience/UxExperience.java` (3)
- `com/reddit/devvit/ui/events/v1alpha/WebView$WebViewInternalEventMessage.java` (3)
- `com/reddit/devvit/ui/effects/v1alpha/EffectOuterClass$EffectType.java` (3)
- `com/reddit/devvit/ui/effects/web_view/v1alpha/PostMessage$WebViewInternalMessage.java` (3)
- `com/reddit/screen/util/PermissionUtil$Permission.java` (3)
- `defpackage/kvd0.java` (2)
- `defpackage/px80.java` (2)
- `defpackage/y5n0.java` (2)
- `com/reddit/sharing/screenshot/RedditScreenshotTriggerSharingListener$showBannerInContainerView$1$banner$1$2$1$1.java` (1)
- `com/reddit/sharing/screenshot/RedditScreenshotTriggerSharingListener$ScreenshotBanner$2$1$1.java` (1)

```
com/reddit/sharing/screenshot/RedditScreenshotTriggerSharingListener$showBannerInContainerView$1$banner$1$2$1$1.java:54:            UxExperience uxExperience = UxExperience.SCREENSHOT_SHARING_BANNER;
com/reddit/sharing/screenshot/RedditScreenshotTriggerSharingListener$ScreenshotBanner$2$1$1.java:54:            UxExperience uxExperience = UxExperience.SCREENSHOT_SHARING_BANNER;
com/reddit/sharing/screenshot/RedditScreenshotTriggerSharingListener$showBannerInContainerView$1$banner$1$1$1$1.java:54:            UxExperience uxExperience = UxExperience.SCREENSHOT_SHARING_BANNER;
com/reddit/sharing/screenshot/ScreenshotShareSheetExperience.java:16:    public static final ScreenshotShareSheetExperience UX1 = new ScreenshotShareSheetExperience("UX1", 0, "SCREENSHOT_SHARE_SHEET_UX1");
com/reddit/sharing/screenshot/RedditScreenshotTriggerSharingListener$ScreenshotBanner$3$1$1.java:54:            UxExperience uxExperience = UxExperience.SCREENSHOT_SHARING_BANNER;
com/reddit/sharing/screenshot/c.java:147:                if (((c6n0) it.next()).b() == UxExperience.SCREENSHOT_SHARING_BANNER) {
com/reddit/sharing/screenshot/c.java:223:            c.a(new px80(baseScreen, new Activity.ScreenCaptureCallback() { // from class: nx80
com/reddit/sharing/screenshot/c.java:224:                @Override // android.app.Activity.ScreenCaptureCallback
com/reddit/type/UxTargetingExperience.java:14:@Metadata(d1 = {"\u0000\u0010\n\u0002\u0018\u0002\n\u0002\u0010\u0010\n\u0002\u0010\u000e\n\u0002\bK\b\u0086\u0081\u0002\u0018\u0000 \t2\b\u0012\u0004\u0012\u00020\u00000\u0001:\u0001\nB\u0011\b\u0002\u0012\u0006\u0010\u0003\u001a\u00020\u0002¢\u0006\u00
com/reddit/type/UxTargetingExperience.java:39:    public static final UxTargetingExperience SCREENSHOT_SHARING_BANNER = new UxTargetingExperience("SCREENSHOT_SHARING_BANNER", 15, "SCREENSHOT_SHARING_BANNER");
com/reddit/type/UxTargetingExperience.java:92:        return new UxTargetingExperience[]{REONBOARDING_IN_FEED, REONBOARDING_BOTTOM_SHEET, VIRAL_COMMUNITY_XPROMO, ANNOUNCEMENT_IN_FEED, LIVE_CHAT_VIDEO_EDU, LIVE_CHAT_REACTION_EDU, BLOCKING_XPROMO, BYPASSABLE_XPROMO, AUTH, LOGGED_IN_ONBOARDING, NEW_USE
com/reddit/type/UxTargetingExperience.java:100:        Arrays.asList("REONBOARDING_IN_FEED", "REONBOARDING_BOTTOM_SHEET", "VIRAL_COMMUNITY_XPROMO", "ANNOUNCEMENT_IN_FEED", "LIVE_CHAT_VIDEO_EDU", "LIVE_CHAT_REACTION_EDU", "BLOCKING_XPROMO", "BYPASSABLE_XPROMO", "AUTH", "LOGGED_IN_ONBOARDING", "NEW_US
```

### audio_capture — 0 hits in 0 files


```
```

### accessibility — 105 hits in 27 files

- `defpackage/l8.java` (12)
- `androidx/compose/ui/platform/e.java` (10)
- `defpackage/vgq0.java` (8)
- `com/reddit/accessibility/RedditScreenReaderStateProvider$isScreenReaderOnFlow$1.java` (7)
- `com/reddit/eventkit/logger/dataproviders/events/a.java` (7)
- `androidx/compose/ui/platform/c.java` (5)
- `defpackage/tfi.java` (5)
- `defpackage/o8.java` (5)
- `androidx/recyclerview/widget/RecyclerView.java` (4)
- `com/wdullaer/materialdatetimepicker/time/RadialPickerLayout.java` (4)
- `com/reddit/accessibility/h.java` (3)
- `defpackage/eqg.java` (3)

```
androidx/recyclerview/widget/RecyclerView.java:30:import android.view.accessibility.AccessibilityManager;
androidx/recyclerview/widget/RecyclerView.java:182:    public final AccessibilityManager u0;
androidx/recyclerview/widget/RecyclerView.java:314:        this.u0 = (AccessibilityManager) getContext().getSystemService("accessibility");
androidx/recyclerview/widget/RecyclerView.java:887:        AccessibilityManager accessibilityManager;
com/wdullaer/materialdatetimepicker/time/TimePickerDialog.java:950:            radialPickerLayout3.r = radialPickerLayout3.t0.isTouchExplorationEnabled() || z5;
com/wdullaer/materialdatetimepicker/time/RadialPickerLayout.java:14:import android.view.accessibility.AccessibilityManager;
com/wdullaer/materialdatetimepicker/time/RadialPickerLayout.java:52:    public final AccessibilityManager t0;
com/wdullaer/materialdatetimepicker/time/RadialPickerLayout.java:108:                this.t0 = (AccessibilityManager) context.getSystemService("accessibility");
com/wdullaer/materialdatetimepicker/time/RadialPickerLayout.java:488:            int iA4 = a(x, y, this.t0.isTouchExplorationEnabled(), boolArr);
androidx/compose/ui/platform/e.java:18:import android.view.accessibility.AccessibilityManager;
androidx/compose/ui/platform/e.java:102:public final class e extends q7 implements View.OnAttachStateChangeListener, AccessibilityManager.AccessibilityStateChangeListener, AccessibilityManager.TouchExplorationStateChangeListener {
androidx/compose/ui/platform/e.java:114:    public final AccessibilityManager i;
```

### root_emulator — 67 hits in 18 files

- `com/reddit/frontpage/R.java` (13)
- `com/appsflyer/R.java` (8)
- `com/google/firebase/crashlytics/internal/model/AutoValue_StaticSessionData_OsData.java` (8)
- `com/google/firebase/crashlytics/internal/model/AutoValue_StaticSessionData_DeviceData.java` (8)
- `com/google/firebase/crashlytics/internal/common/CommonUtils.java` (7)
- `com/appsflyer/internal/AFf1iSDK.java` (4)
- `defpackage/eqg.java` (4)
- `com/reddit/postdetail/refactor/events/handlers/PostDetailPersistentGalleryIndicatorsVisibleEventHandler.java` (3)
- `com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java` (2)
- `com/google/firebase/crashlytics/internal/model/StaticSessionData.java` (2)
- `defpackage/q5f.java` (1)
- `com/reddit/domain/model/listing/ContentRemovalMessage.java` (1)

```
defpackage/q5f.java:643:                    String strN2 = xyo0.N(vjkVar14, R.string.search_exposed_exposure);
com/appsflyer/internal/AFf1iSDK.java:43:            put("aq", "ro.kernel.qemu");
com/appsflyer/internal/AFf1iSDK.java:88:                    if (stackTraceElement.toString().contains("de.robv.android.xposed") && i2 <= 2) {
com/appsflyer/internal/AFf1iSDK.java:114:            if (d(sb2.toString(), "frida")) {
com/appsflyer/internal/AFf1iSDK.java:118:            AFLogger.INSTANCE.e(LogTag.ANTI_FRAUD, "frida detection error", e, false, false);
com/appsflyer/R.java:1266:        public static final int mtrl_exposed_dropdown_menu_popup_elevation = 0x7f07021d;
com/appsflyer/R.java:1267:        public static final int mtrl_exposed_dropdown_menu_popup_vertical_offset = 0x7f07021e;
com/appsflyer/R.java:1268:        public static final int mtrl_exposed_dropdown_menu_popup_vertical_padding = 0x7f07021f;
com/appsflyer/R.java:1990:        public static final int exposed_dropdown_menu_content_description = 0x7f130e6f;
com/appsflyer/R.java:2702:        public static final int Widget_MaterialComponents_TextInputLayout_FilledBox_Dense_ExposedDropdownMenu = 0x7f140355;
com/appsflyer/R.java:2703:        public static final int Widget_MaterialComponents_TextInputLayout_FilledBox_ExposedDropdownMenu = 0x7f140356;
com/appsflyer/R.java:2706:        public static final int Widget_MaterialComponents_TextInputLayout_OutlinedBox_Dense_ExposedDropdownMenu = 0x7f140359;
```

### js_bridge — 3 hits in 3 files

- `com/reddit/devplatform/features/customposts/webview/d.java` (1)
- `org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java` (1)
- `defpackage/tr70.java` (1)

```
com/reddit/devplatform/features/customposts/webview/d.java:281:        addJavascriptInterface(this.j0, "__DEVVIT__");
org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java:46:        public void addJavascriptInterface(Object obj, String str, List<String> list) {
defpackage/tr70.java:28:        webView.addJavascriptInterface(on1Var, "AdsWebViewDownloadHandler");
```

### boot_persist — 0 hits in 0 files


```
```

### full_screen_intent — 1 hits in 1 files

- `defpackage/d4z.java` (1)

```
defpackage/d4z.java:101:        builder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.ledARGB, notification.ledOn [... omitted en
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 41 hits in 33 files

- `defpackage/wv8.java` (3)
- `defpackage/i23.java` (2)
- `defpackage/czf0.java` (2)
- `com/google/android/material/button/MaterialButton.java` (2)
- `com/reddit/notification/impl/inbox/ComposeMessageScreen.java` (2)
- `androidx/appcompat/widget/AppCompatTextView.java` (2)
- `com/reddit/screen/composewidgets/KeyboardExtensionsScreen.java` (2)
- `defpackage/iti0.java` (1)
- `defpackage/er5.java` (1)
- `defpackage/q7b.java` (1)
- `defpackage/dzf0.java` (1)
- `defpackage/gn00.java` (1)

```
defpackage/iti0.java:70:            editText.addTextChangedListener(new ich(2, this, strG));
defpackage/er5.java:93:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
defpackage/q7b.java:33:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
defpackage/dzf0.java:47:            ((czf0) arrayList.get(i)).onTextChanged(this, 0, length(), length());
defpackage/wv8.java:36:                editText.addTextChangedListener(er5Var);
defpackage/wv8.java:78:                autoCompleteTextViewD.addTextChangedListener(er5Var2);
defpackage/wv8.java:92:                editText2.addTextChangedListener(er5Var3);
defpackage/gn00.java:115:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
defpackage/blh.java:45:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) throws Throwable {
defpackage/qdh.java:43:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
defpackage/wta0.java:1864:                    editText.addTextChangedListener(new hti0(textView, view, iA));
defpackage/nch.java:103:            getEditText().addTextChangedListener(new q7b(communityNameEditText, 1));
```

### webview_tracking — 1 hits in 1 files

- `defpackage/xs8.java` (1)

```
defpackage/xs8.java:87:                CookieManager.getInstance().setAcceptThirdPartyCookies(redditWebView, true);
```

### streaks — 257 hits in 67 files

- `com/reddit/achievements/navbar/StreakPopupsViewModel.java` (35)
- `com/reddit/achievements/navbar/c.java` (18)
- `com/reddit/type/StreakExtendedNotificationPresentation.java` (17)
- `com/reddit/frontpage/R.java` (16)
- `com/reddit/achievements/navbar/b.java` (15)
- `com/reddit/subredditexperience/common/CommunityGuidance.java` (10)
- `com/reddit/achievements/navbar/StreakPopupsViewModel$handleProgressToastEvents$achievementEvent$2$2.java` (9)
- `com/reddit/achievements/navbar/StreakPopupsViewModel$handleToastEvent$1$1.java` (9)
- `com/reddit/achievements/navbar/StreakPopupsViewModel$viewState$2$1.java` (7)
- `com/reddit/streaks/domain/RedditStreaksStartupInstaller$install$2.java` (6)
- `com/reddit/streaks/RedditStreakPopupsKt$StreakPopups$1$1.java` (6)
- `com/reddit/achievements/navbar/a.java` (6)

```
com/reddit/streaks/domain/a.java:1:package com.reddit.streaks.domain;
com/reddit/streaks/domain/a.java:33:        Object objG0 = d6c.g0(this.c.e(), new RedditStreaksStartupInstaller$install$2(this, null), urcVar);
com/reddit/streaks/domain/RedditStreaksStartupInstaller$install$2.java:1:package com.reddit.streaks.domain;
com/reddit/streaks/domain/RedditStreaksStartupInstaller$install$2.java:18:@d0f(c = "com.reddit.streaks.domain.RedditStreaksStartupInstaller$install$2", f = "RedditStreaksStartupInstaller.kt", l = {27, 31, 35}, m = "invokeSuspend", v = 2)
com/reddit/streaks/domain/RedditStreaksStartupInstaller$install$2.java:21:final class RedditStreaksStartupInstaller$install$2 extends SuspendLambda implements Function2<n5d, urc<? super Unit>, Object> {
com/reddit/streaks/domain/RedditStreaksStartupInstaller$install$2.java:27:    public RedditStreaksStartupInstaller$install$2(a aVar, urc<? super RedditStreaksStartupInstaller$install$2> urcVar) {
com/reddit/streaks/domain/RedditStreaksStartupInstaller$install$2.java:34:        return new RedditStreaksStartupInstaller$install$2(this.this$0, urcVar);
com/reddit/streaks/domain/RedditStreaksStartupInstaller$install$2.java:39:        return ((RedditStreaksStartupInstaller$install$2) create(n5dVar, urcVar)).invokeSuspend(Unit.a);
com/reddit/streaks/RedditStreakPopupsKt$StreakPopups$1$1.java:1:package com.reddit.streaks;
com/reddit/streaks/RedditStreakPopupsKt$StreakPopups$1$1.java:3:import com.reddit.achievements.navbar.StreakPopupsViewModel;
com/reddit/streaks/RedditStreakPopupsKt$StreakPopups$1$1.java:13:final /* synthetic */ class RedditStreakPopupsKt$StreakPopups$1$1 extends FunctionReferenceImpl implements Function1<d160, Unit> {
com/reddit/streaks/RedditStreakPopupsKt$StreakPopups$1$1.java:14:    public RedditStreakPopupsKt$StreakPopups$1$1(Object obj) {
```

### reengagement — 1779 hits in 390 files

- `com/reddit/devvit/reddit/CommentOuterClass$Comment.java` (53)
- `com/reddit/devvit/plugin/redditapi/common/CommonMsg$RedditObject.java` (53)
- `com/reddit/data/model/v1/Comment.java` (44)
- `com/reddit/domain/model/Comment.java` (40)
- `com/reddit/data/events/chat_view/approve/collapsed_message/ChatViewApproveCollapsedMessage.java` (37)
- `com/reddit/data/events/chat_view/report/collapsed_message/ChatViewReportCollapsedMessage.java` (37)
- `com/reddit/screens/drawer/community/c.java` (32)
- `com/reddit/devplatform/data/repository/a.java` (29)
- `com/reddit/frontpage/R.java` (28)
- `com/reddit/type/CommentCollapsedReason.java` (27)
- `com/reddit/auth/login/domain/usecase/p.java` (24)
- `com/reddit/contribution/kickstarting/ui/ContributionKickstartingBannerV2ViewModel.java` (21)

```
okhttp3/internal/concurrent/TaskLoggerKt.java:13:@Metadata(d1 = {"\u0000*\n\u0000\n\u0002\u0010\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\b\b\n\u0002\u0010\t\n\u0000\u001a.\u0010\u0000\u001a\u00020\u0001*
okhttp3/internal/concurrent/TaskLoggerKt.java:47:    public static final <T> T logElapsed(Logger logger, Task task, TaskQueue taskQueue, Function0<? extends T> function0) {
androidx/appcompat/widget/k.java:33:            ((wju) ((f49) callback)).a.onActionViewCollapsed();
androidx/appcompat/widget/Toolbar.java:66:    private CharSequence mCollapseDescription;
androidx/appcompat/widget/Toolbar.java:172:        this.mCollapseDescription = typedArray2.getText(3);
androidx/appcompat/widget/Toolbar.java:520:            this.mCollapseButtonView.setContentDescription(this.mCollapseDescription);
kotlinx/coroutines/scheduling/CoroutineScheduler$WorkerState.java:10:@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0010\u0010\n\u0002\u0018\u0002\n\u0002\b\b\b\u0086\u0081\u0002\u0018\u00002\b\u0012\u0004\u0012\u00020\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0003\u0010\u0004j\u0002\b\u0005j\u0002\b\
kotlinx/coroutines/scheduling/CoroutineScheduler$WorkerState.java:18:    public static final CoroutineScheduler$WorkerState DORMANT = new CoroutineScheduler$WorkerState("DORMANT", 3);
kotlinx/coroutines/scheduling/CoroutineScheduler$WorkerState.java:22:        return new CoroutineScheduler$WorkerState[]{CPU_ACQUIRED, BLOCKING, PARKING, DORMANT, TERMINATED};
androidx/media3/exoplayer/a.java:429:                xh10Var4.t = SystemClock.elapsedRealtime();
androidx/media3/exoplayer/a.java:455:                        if (SystemClock.elapsedRealtime() - y8fVar.l < 1000) {
androidx/media3/exoplayer/a.java:461:                    y8fVar.l = SystemClock.elapsedRealtime();
```

### notif_permission_nag — 142 hits in 13 files

- `com/reddit/notification/impl/reenablement/a.java` (112)
- `com/reddit/notification/analytics/Noun.java` (4)
- `com/reddit/notification/domain/model/NotificationEnablementState.java` (4)
- `com/reddit/sharing/analytics/ShareAnalytics$Noun.java` (3)
- `com/reddit/frontpage/R.java` (3)
- `com/reddit/notification/impl/reenablement/RedditNotificationReEnablementDelegate$handlePrePrompt$1.java` (3)
- `com/reddit/notification/impl/reenablement/RedditNotificationReEnablementDelegate$handlePrePromptAsync$1.java` (3)
- `com/reddit/notification/impl/reenablement/RedditNotificationReEnablementDelegate$handleRePromptAsync$1.java` (3)
- `com/reddit/notification/impl/reenablement/NotificationReEnablementViewModel.java` (2)
- `defpackage/vl80.java` (2)
- `com/reddit/sharing/actions/ActionSheet.java` (1)
- `defpackage/xz80.java` (1)

```
com/reddit/sharing/analytics/ShareAnalytics$Noun.java:10:@Metadata(d1 = {"\u0000\u0012\n\u0000\n\u0002\u0010\u0010\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\b\u0010\b\u0086\u0081\u0002\u0018\u00002\b\u0012\u0004\u0012\u00020\u00020\u0001B\u0011\b\u0002\u0012\u0006\u0010\u0004\u001a\u00020\u000
com/reddit/sharing/analytics/ShareAnalytics$Noun.java:17:    public static final ShareAnalytics$Noun SharePrompt = new ShareAnalytics$Noun("SharePrompt", 1, "share_prompt");
com/reddit/sharing/analytics/ShareAnalytics$Noun.java:27:        return new ShareAnalytics$Noun[]{ScreenshotPrompt, SharePrompt, Share, OverflowCommentShare, Download, Save, Overflow, AwardOverflowMenu, EndShare};
com/reddit/sharing/actions/ActionSheet.java:136:            si6.B(", showOnlyShareSheet=", ", hideUsernameSharePrompt=", sb, this.e, this.g);
com/reddit/notification/analytics/Noun.java:10:@Metadata(d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0010\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0015\b\u0086\u0081\u0002\u0018\u00002\b\u0012\u0004\u0012\u00020\u00000\u0001B\u0011\b\u0002\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u
com/reddit/notification/analytics/Noun.java:26:    public static final Noun PRE_PROMPT_PERMISSIONS = new Noun("PRE_PROMPT_PERMISSIONS", 10, "preprompt_permissions");
com/reddit/notification/analytics/Noun.java:27:    public static final Noun RE_PROMPT_PERMISSIONS = new Noun("RE_PROMPT_PERMISSIONS", 11, "reprompt_permissions");
com/reddit/notification/analytics/Noun.java:34:        return new Noun[]{INBOX_NOTIFICATION, INBOX_GROUPED_NOTIFICATION, INBOX_GROUPED_OVERFLOW, INBOX_OVERFLOW_SETTINGS, EMPTY_STATE_CTA, INBOX_OVERFLOW_SETTINGS_OPTION, INBOX_NOTIFICATION_OVERFLOW, MARK_ALL_AS_READ, INBOX, RE_ENABLE_NOTIFICATIONS, PR
com/reddit/notification/domain/model/NotificationEnablementState.java:12:@Metadata(d1 = {"\u0000\u0010\n\u0002\u0018\u0002\n\u0002\u0010\u0010\n\u0002\u0010\u000e\n\u0002\b\u000e\b\u0086\u0081\u0002\u0018\u0000 \t2\b\u0012\u0004\u0012\u00020\u00000\u0001:\u0001\nB\u0011\b\u0002\u0012\u0006\u0010\u00
com/reddit/notification/domain/model/NotificationEnablementState.java:19:    public static final NotificationEnablementState ShouldShowPrePrompt = new NotificationEnablementState("ShouldShowPrePrompt", 0, "pre_prompt");
com/reddit/notification/domain/model/NotificationEnablementState.java:20:    public static final NotificationEnablementState ShouldShowRePrompt = new NotificationEnablementState("ShouldShowRePrompt", 1, "re_prompt");
com/reddit/notification/domain/model/NotificationEnablementState.java:26:        return new NotificationEnablementState[]{ShouldShowPrePrompt, ShouldShowRePrompt, NotificationsEnabled, ShouldShowReEnablementPrompt, NotGranted};
```

### cancellation_retention — 0 hits in 0 files


```
```

### urgency_countdown — 192 hits in 54 files

- `com/reddit/experiments/data/local/inmemory/b.java` (12)
- `com/reddit/auth/core/accesstoken/remote/RedditAccessTokenResponseDto.java` (11)
- `com/reddit/auth/login/model/AccessTokenSuccess.java` (11)
- `okhttp3/internal/concurrent/TaskQueue.java` (9)
- `com/appsflyer/internal/AFe1iSDK.java` (9)
- `com/google/firebase/crashlytics/internal/common/Utils.java` (9)
- `com/reddit/ads/impl/reminder/composables/ReminderAdSharedComposablesKt$ReminderAdLiveTimeRemainingLabel$1$1.java` (8)
- `com/reddit/marketplace/awards/features/dynamicentrypoint/composables/EntryPointIconKt$GlowingAnimatedView$1$1.java` (8)
- `com/reddit/marketplace/awards/features/dynamicentrypoint/composables/RedditAwardDynamicEntryPointKt$GlowingAwardEntryPoint$1$1.java` (8)
- `com/google/firebase/crashlytics/internal/analytics/BlockingAnalyticsEventLogger.java` (6)
- `com/google/firebase/crashlytics/internal/send/ReportQueue.java` (6)
- `com/reddit/auth/core/accesstoken/remote/RedditAccessTokenResponseDtoJsonAdapter.java` (6)

```
okhttp3/internal/concurrent/TaskQueue.java:8:import java.util.concurrent.CountDownLatch;
okhttp3/internal/concurrent/TaskQueue.java:20:@Metadata(d1 = {"\u0000V\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010!\n\u0002\b\u0006\n\u0002\u0010 
okhttp3/internal/concurrent/TaskQueue.java:31:    @Metadata(d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\t\n\u0000\b\u0002\u0018\u00002\u00020\u0001B\u0007¢\u0006\u0004\b\u0002\u0010\u0003J\b\u0010\b\u001a\u00020\tH\u00
okhttp3/internal/concurrent/TaskQueue.java:34:        private final CountDownLatch latch;
okhttp3/internal/concurrent/TaskQueue.java:38:            this.latch = new CountDownLatch(1);
okhttp3/internal/concurrent/TaskQueue.java:41:        public final CountDownLatch getLatch() {
okhttp3/internal/concurrent/TaskQueue.java:47:            this.latch.countDown();
okhttp3/internal/concurrent/TaskQueue.java:155:    public final CountDownLatch idleLatch() {
okhttp3/internal/concurrent/TaskQueue.java:158:                return new CountDownLatch(0);
okhttp3/internal/publicsuffix/BasePublicSuffixList.java:7:import java.util.concurrent.CountDownLatch;
okhttp3/internal/publicsuffix/BasePublicSuffixList.java:14:@Metadata(d1 = {"\u0000D\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0
okhttp3/internal/publicsuffix/BasePublicSuffixList.java:20:    private final CountDownLatch readCompleteLatch = new CountDownLatch(1);
```

### infinite_autoplay — 783 hits in 113 files

- `com/reddit/datasaver/settings/c.java` (138)
- `defpackage/g87.java` (38)
- `com/reddit/data/events/videoplayer/view/autoplay/VideoplayerViewAutoplay.java` (37)
- `com/reddit/devvit/reddit/UserOuterClass$User.java` (27)
- `defpackage/zun0.java` (22)
- `com/reddit/mediacomponent/api/props/MediaAutoplay.java` (17)
- `com/reddit/accessibility/AutoplayVideoPreviewsOption.java` (16)
- `com/reddit/domain/media/model/VideoAutoPlaySettingsFlag.java` (16)
- `com/reddit/exokit/api/ui/params/AutoplayType.java` (16)
- `com/reddit/ui/compose/ds/CarouselAutoplayIndicatorPlacement.java` (15)
- `com/reddit/ui/compose/ds/AutoplayIndicatorAppearance.java` (15)
- `com/reddit/ui/compose/ds/e.java` (15)

```
com/reddit/videoplayer/player/ui/VideoMetadata.java:169:        hvq.t(this.g, this.e, ", positionInFeed=", ", autoplayRank=", sb);
com/reddit/videoplayer/player/ui/VideoMetadata.java:170:        q4.y(sb, this.i, ", autoplaySubRank=", this.r, ", thumbnailUrl=");
com/reddit/mediacomponent/api/props/MediaAutoplay.java:10:@Metadata(d1 = {"\u0000\f\n\u0002\u0018\u0002\n\u0002\u0010\u0010\n\u0002\b\u0007\b\u0086\u0081\u0002\u0018\u00002\b\u0012\u0004\u0012\u00020\u00000\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u0003j\u0002\b\u0004j\u0002\b\u0005j\u0002\b\u000
com/reddit/mediacomponent/api/props/MediaAutoplay.java:12:public final class MediaAutoplay {
com/reddit/mediacomponent/api/props/MediaAutoplay.java:14:    private static final /* synthetic */ MediaAutoplay[] $VALUES;
com/reddit/mediacomponent/api/props/MediaAutoplay.java:15:    public static final MediaAutoplay APP_SETTINGS = new MediaAutoplay("APP_SETTINGS", 0);
com/reddit/mediacomponent/api/props/MediaAutoplay.java:16:    public static final MediaAutoplay ALWAYS = new MediaAutoplay("ALWAYS", 1);
com/reddit/mediacomponent/api/props/MediaAutoplay.java:17:    public static final MediaAutoplay NEVER = new MediaAutoplay("NEVER", 2);
com/reddit/mediacomponent/api/props/MediaAutoplay.java:18:    public static final MediaAutoplay BLURRED = new MediaAutoplay("BLURRED", 3);
com/reddit/mediacomponent/api/props/MediaAutoplay.java:20:    private static final /* synthetic */ MediaAutoplay[] $values() {
com/reddit/mediacomponent/api/props/MediaAutoplay.java:21:        return new MediaAutoplay[]{APP_SETTINGS, ALWAYS, NEVER, BLURRED};
com/reddit/mediacomponent/api/props/MediaAutoplay.java:25:        MediaAutoplay[] mediaAutoplayArr$values = $values();
```

### badges — 19 hits in 12 files

- `com/reddit/frontpage/R.java` (4)
- `me/leolin/shortcutbadger/impl/DefaultBadger.java` (3)
- `defpackage/d4z.java` (2)
- `defpackage/ml4.java` (2)
- `defpackage/lyo0.java` (1)
- `com/google/protobuf/EnumValue.java` (1)
- `defpackage/i90.java` (1)
- `com/google/protobuf/Field.java` (1)
- `me/leolin/shortcutbadger/impl/SonyHomeBadger.java` (1)
- `com/reddit/devvit/ui/effects/web_view/v1alpha/Context$NativeClientVersion.java` (1)
- `defpackage/zgz.java` (1)
- `defpackage/gxo0.java` (1)

```
defpackage/lyo0.java:23:        bundle.putInt("app_badge_count", i);
com/google/protobuf/EnumValue.java:114:    public void setNumber(int i) {
defpackage/i90.java:50:                dui0.b(str, dep.j0(fax.a, "user_card_mod_log_badge_count"), ((g89) vjkVar.j(e290.f)).n.b(), 0L, null, null, null, 0L, null, 0, 0L, 0, false, 0, 0, null, null, vjkVar, 48, 0, 262136);
com/google/protobuf/Field.java:208:    public void setNumber(int i) {
me/leolin/shortcutbadger/impl/SonyHomeBadger.java:40:        contentValues.put("badge_count", Integer.valueOf(i));
me/leolin/shortcutbadger/impl/DefaultBadger.java:23:        intent.putExtra("badge_count", i);
me/leolin/shortcutbadger/impl/DefaultBadger.java:24:        intent.putExtra("badge_count_package_name", componentName.getPackageName());
me/leolin/shortcutbadger/impl/DefaultBadger.java:25:        intent.putExtra("badge_count_class_name", componentName.getClassName());
defpackage/d4z.java:101:        builder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.ledARGB, notification.ledOn [... omitted en
defpackage/d4z.java:252:        ((Notification.Builder) xtdVar.b).setBadgeIconType(0);
com/reddit/frontpage/R.java:5288:        public static final int tab_badge_count = 0x7f0b048f;
com/reddit/frontpage/R.java:7698:        public static final int automations_a11y_badge_count = 0x7f1304fc;
```

### minors_age — 3810 hits in 370 files

- `com/reddit/agegating/impl/domain/v2/b.java` (520)
- `defpackage/y9.java` (292)
- `defpackage/vw1.java` (104)
- `defpackage/z9.java` (81)
- `com/reddit/agegating/data/AccountAgeGateSnapshotDiagnosticSourceJsonAdapter.java` (67)
- `defpackage/xw1.java` (51)
- `com/reddit/data/events/age_gate/flow/snapshot_operation/AgeGateFlowSnapshotOperation.java` (43)
- `com/reddit/data/events/age_gate/flow/resolver_evaluation/AgeGateFlowResolverEvaluation.java` (40)
- `com/reddit/data/events/age_gate/flow/checkpoint/AgeGateFlowCheckpoint.java` (40)
- `com/reddit/agegating/impl/age/b.java` (39)
- `com/reddit/agegating/data/AccountAgeGateSnapshotDiagnosticEvent.java` (37)
- `com/reddit/data/events/age_verification/verify/complete/AgeVerificationVerifyComplete.java` (37)

```
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:1:package wrappers.com.reddit.data.events.age_gate.flow.snapshot_operation;
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:3:import com.reddit.data.events.age_gate.flow.snapshot_operation.AgeGateFlowSnapshotOperation;
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:13:@Metadata(d1 = {"\u0000\u0014\n\u0002\u0018\u0002\n\u0002\u0010\u0010\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\b\u0086\u0081\u0002\u0018\u00002\b\u0012\u0004\u0012\u00020\u00000\u0001B\u0007\b\u000
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:22:    public static final SnapshotSourceKind SNAPSHOT_SOURCE_KIND_AGE_GATE_INFO = new SnapshotSourceKind("SNAPSHOT_SOURCE_KIND_AGE_GATE_INFO", 4);
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:25:        return new SnapshotSourceKind[]{SNAPSHOT_SOURCE_KIND_UNSPECIFIED, SNAPSHOT_SOURCE_KIND_ACTIVE_ACCOUNT, SNAPSHOT_SOURCE_KIND_ACCOUNT_PREFERENCES, SNAPSHOT_SOURCE_KIND_ACCOUNT_AGE_INFO, SNAPSHOT_SOURCE_
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:49:    public final AgeGateFlowSnapshotOperation.SnapshotSourceKind toJavaEnum() {
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:52:            return AgeGateFlowSnapshotOperation.SnapshotSourceKind.SNAPSHOT_SOURCE_KIND_UNSPECIFIED;
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:55:            return AgeGateFlowSnapshotOperation.SnapshotSourceKind.SNAPSHOT_SOURCE_KIND_ACTIVE_ACCOUNT;
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:58:            return AgeGateFlowSnapshotOperation.SnapshotSourceKind.SNAPSHOT_SOURCE_KIND_ACCOUNT_PREFERENCES;
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:61:            return AgeGateFlowSnapshotOperation.SnapshotSourceKind.SNAPSHOT_SOURCE_KIND_ACCOUNT_AGE_INFO;
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotSourceKind.java:64:            return AgeGateFlowSnapshotOperation.SnapshotSourceKind.SNAPSHOT_SOURCE_KIND_AGE_GATE_INFO;
wrappers/com/reddit/data/events/age_gate/flow/snapshot_operation/SnapshotTrigger.java:1:package wrappers.com.reddit.data.events.age_gate.flow.snapshot_operation;
```

### screen_time — 89 hits in 16 files

- `com/reddit/mmp/b.java` (35)
- `com/reddit/mmp/data/d.java` (16)
- `com/reddit/corexdata/common/ArticleLink.java` (10)
- `com/reddit/mmp/RedditMmpTimeSpentInAppHandler$onUserLeave$2.java` (7)
- `com/reddit/mmp/MmpEvent.java` (3)
- `com/reddit/mmp/data/RedditMmpUserActionRepository$addTimeSpentInApp$1.java` (3)
- `com/reddit/mmp/RedditMmpTimeSpentInAppHandler$onUserLeave$1.java` (3)
- `com/reddit/mmp/RedditMmpTimeSpentInAppHandler$onUserVisit$1.java` (3)
- `defpackage/ie8.java` (2)
- `defpackage/xj3.java` (1)
- `defpackage/vij.java` (1)
- `com/google/android/gms/ads/identifier/AdvertisingIdClient.java` (1)

```
defpackage/xj3.java:16:        ((ArticleLink) this.instance).setTimeSpentMillis(j);
defpackage/vij.java:37:            iArr[MmpEvent.TIME_SPENT_IN_APP.ordinal()] = 7;
com/google/android/gms/ads/identifier/AdvertisingIdClient.java:320:        map.put("time_spent", Long.toString(j));
defpackage/ie8.java:19:            return Intrinsics.areEqual("chat_session_length", "chat_session_length") && Intrinsics.areEqual(this.a, ((ie8) obj).a);
defpackage/ie8.java:29:        return af1.l("Timer(type=chat_session_length, millis=", this.a, ")");
com/reddit/data/events/chat_view/leave/screen/b.java:17:        ((ChatViewLeaveScreen.Timer) this.instance).setType("chat_session_length");
defpackage/ou70.java:37:            iArr[MmpEvent.TIME_SPENT_IN_APP.ordinal()] = 7;
com/reddit/corexdata/common/ArticleLink.java:24:    public static final int TIME_SPENT_MILLIS_FIELD_NUMBER = 3;
com/reddit/corexdata/common/ArticleLink.java:29:    private long timeSpentMillis_;
com/reddit/corexdata/common/ArticleLink.java:51:    private void clearTimeSpentMillis() {
com/reddit/corexdata/common/ArticleLink.java:53:        this.timeSpentMillis_ = 0L;
com/reddit/corexdata/common/ArticleLink.java:93:    public void setTimeSpentMillis(long j) {
```

