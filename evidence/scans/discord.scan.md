# Pattern scan: work/discord/jdex

## Code categories (library packages excluded)

### installed_apps — 24 hits in 19 files

- `classes:v1/h.java` (2)
- `classes:com/discord/browser_manager/BrowserManager.java` (2)
- `classes3:ve/l.java` (2)
- `classes3:ye/f.java` (2)
- `classes3:qh/f.java` (2)
- `classes:a5/g.java` (1)
- `classes:z0/d.java` (1)
- `classes:u1/d.java` (1)
- `classes:com/android/installreferrer/api/b.java` (1)
- `classes:com/appsflyer/internal/AFb1qSDK.java` (1)
- `classes:androidx/core/widget/g.java` (1)
- `classes:com/appsflyer/internal/AFa1uSDK.java` (1)

```
classes:v1/h.java:171:                PackageInfo packageInfo = packageManager.getPackageInfo("com.google.android.gms", 0);
classes:v1/h.java:175:                jQ = packageManager.getPackageInfo("com.google.android.gms", 0).versionCode;
classes:a5/g.java:114:                packageInfo = jf.c.a((Context) this.f157i).a.getPackageManager().getPackageInfo("com.google.android.gms", 0);
classes:z0/d.java:104:            Iterator<ResolveInfo> it = packageManager.queryIntentActivities(intent, 128).iterator();
classes:u1/d.java:275:        long j = packageManager.getPackageInfo("com.google.android.gms", 0).versionCode;
classes:com/android/installreferrer/api/b.java:98:                if (context.getPackageManager().getPackageInfo("com.android.vending", 128).versionCode >= 80837300) {
classes:com/appsflyer/internal/AFb1qSDK.java:100:        context.getPackageManager().getPackageInfo("com.android.vending", 0);
classes:androidx/core/widget/g.java:88:                for (ResolveInfo resolveInfo : packageManager.queryIntentActivities(new Intent().setAction("android.intent.action.PROCESS_TEXT").setType("text/plain"), 0)) {
classes:com/appsflyer/internal/AFa1uSDK.java:3373:            context.getPackageManager().getPackageInfo("com.google.android.gms", 0);
classes:f3/d.java:115:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(intent, 128);
classes:com/discord/browser_manager/BrowserManager.java:105:            List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(intentAddFlags, 0);
classes:com/discord/browser_manager/BrowserManager.java:106:            Intrinsics.checkNotNullExpressionValue(listQueryIntentActivities, "queryIntentActivities(...)");
```

### usage_stats — 0 hits in 0 files


```
```

### clipboard — 7 hits in 3 files

- `classes3:com/reactnativecommunity/clipboard/ClipboardModule.java` (5)
- `classes:androidx/appcompat/widget/AppCompatEditText.java` (1)
- `classes3:com/facebook/react/modules/clipboard/ClipboardModule.java` (1)

```
classes:androidx/appcompat/widget/AppCompatEditText.java:226:        ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
classes3:com/reactnativecommunity/clipboard/ClipboardModule.java:58:        if (!clipboardService.hasPrimaryClip()) {
classes3:com/reactnativecommunity/clipboard/ClipboardModule.java:66:        ClipData primaryClip = clipboardService.getPrimaryClip();
classes3:com/reactnativecommunity/clipboard/ClipboardModule.java:145:            ClipData primaryClip = getClipboardService().getPrimaryClip();
classes3:com/reactnativecommunity/clipboard/ClipboardModule.java:180:            ClipData primaryClip = getClipboardService().getPrimaryClip();
classes3:com/reactnativecommunity/clipboard/ClipboardModule.java:231:            clipboardService.addPrimaryClipChangedListener(aVar);
classes3:com/facebook/react/modules/clipboard/ClipboardModule.java:41:            ClipData primaryClip = getClipboardService().getPrimaryClip();
```

### contacts — 8 hits in 3 files

- `classes:com/discord/contact_sync/ContactSyncProvider.java` (4)
- `classes3:w8/a.java` (2)
- `classes3:com/facebook/imagepipeline/producers/j0.java` (2)

```
classes:com/discord/contact_sync/ContactSyncProvider.java:10:import android.provider.ContactsContract;
classes:com/discord/contact_sync/ContactSyncProvider.java:65:        Cursor cursorQuery = context.getContentResolver().query(ContactsContract.Data.CONTENT_URI, null, e.k("mimetype = ? AND contact_id = ", contactId), new String[]{"vnd.android.cursor.item/name"}, null);
classes:com/discord/contact_sync/ContactSyncProvider.java:94:        Cursor cursorQuery = context.getContentResolver().query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI, new String[]{"_id", "data4", "display_name", "photo_file_id", "contact_id"}, null, null, null);
classes:com/discord/contact_sync/ContactSyncProvider.java:120:        Cursor cursorQuery = context.getContentResolver().query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI, new String[]{"_id", "photo_thumb_uri"}, "_id = ?", new String[]{deviceContactId}, null);
classes3:w8/a.java:6:import android.provider.ContactsContract;
classes3:w8/a.java:12:    public static final Uri a = Uri.withAppendedPath(ContactsContract.AUTHORITY_URI, "display_photo");
classes3:com/facebook/imagepipeline/producers/j0.java:7:import android.provider.ContactsContract;
classes3:com/facebook/imagepipeline/producers/j0.java:100:                        InputStream inputStreamOpenContactPhotoInputStream = ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, sourceUri);
```

### call_log — 0 hits in 0 files


```
```

### sms — 13 hits in 7 files

- `classes:com/discord/phone_verification/SmsAutofillManagerModule.java` (3)
- `classes3:wf/e.java` (3)
- `classes:com/discord/intents/IntentsModule.java` (2)
- `classes:com/discord/phone_verification/SmsAutofillManager.java` (2)
- `classes:a3/j.java` (1)
- `classes3:l8/a.java` (1)
- `classes3:te/a.java` (1)

```
classes:a3/j.java:27:        attachInterface(this, "com.google.android.gms.auth.api.phone.internal.ISmsRetrieverResultCallback");
classes:com/discord/intents/IntentsModule.java:120:        String defaultSmsPackage = Telephony.Sms.getDefaultSmsPackage(this.reactContext);
classes:com/discord/intents/IntentsModule.java:176:        String defaultSmsPackage = Telephony.Sms.getDefaultSmsPackage(this.reactContext);
classes:com/discord/phone_verification/SmsAutofillManagerModule.java:16:@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0002\b\u0006
classes:com/discord/phone_verification/SmsAutofillManagerModule.java:65:    public final void startSmsRetriever() {
classes:com/discord/phone_verification/SmsAutofillManagerModule.java:66:        this.smsAutofillManager.startSmsRetriever();
classes:com/discord/phone_verification/SmsAutofillManager.java:17:@Metadata(d1 = {"\u0000&\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010\u0002\n\u0002\b\b\n\u0002\u0018\u0002\n\u0002\b\u0003\b\u0000\u0018\u00002\u00020\u0001
classes:com/discord/phone_verification/SmsAutofillManager.java:38:    public final void startSmsRetriever() {
classes3:l8/a.java:253:        parcelObtain.writeInterfaceToken("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService");
classes3:te/a.java:10:    public static final e k = new e("SmsRetriever.API", new m1(7), new d());
classes3:wf/e.java:18:        IInterface iInterfaceQueryLocalInterface = iBinder.queryLocalInterface("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService");
classes3:wf/e.java:29:        return "com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService";
```

### location — 2 hits in 1 files

- `classes:i/v.java` (2)

```
classes:i/v.java:68:                        Location lastKnownLocation2 = locationManager.isProviderEnabled("network") ? locationManager.getLastKnownLocation("network") : null;
classes:i/v.java:76:                                lastKnownLocation = locationManager.getLastKnownLocation("gps");
```

### wifi_bt_scan — 3 hits in 2 files

- `classes3:ll/b.java` (2)
- `classes4:org/webrtc/NetworkMonitorAutoDetect.java` (1)

```
classes3:ll/b.java:158:                        String ssid = connectionInfo.getSSID();
classes3:ll/b.java:165:                        String bssid = connectionInfo.getBSSID();
classes4:org/webrtc/NetworkMonitorAutoDetect.java:670:            return (intentRegisterReceiver == null || (wifiInfo = (WifiInfo) intentRegisterReceiver.getParcelableExtra("wifiInfo")) == null || (ssid = wifiInfo.getSSID()) == null) ? "" : ssid;
```

### device_ids — 20 hits in 14 files

- `classes:com/appsflyer/internal/AFg1qSDK.java` (3)
- `classes:androidx/core/widget/NestedScrollView.java` (3)
- `classes:androidx/core/view/DifferentialMotionFlingController.java` (3)
- `classes:i/j0.java` (1)
- `classes:i/e0.java` (1)
- `classes:com/appsflyer/internal/AFa1uSDK.java` (1)
- `classes:com/appsflyer/internal/AFd1nSDK.java` (1)
- `classes:com/appsflyer/deeplink/DeepLink.java` (1)
- `classes:androidx/appcompat/app/a.java` (1)
- `classes:com/discord/audio/DiscordAudioManager2.java` (1)
- `classes:com/discord/audio/AndroidAudioDevice.java` (1)
- `classes3:jm/f.java` (1)

```
classes:i/j0.java:186:        jVar.setQwertyMode(KeyCharacterMap.load(keyEvent.getDeviceId()).getKeyboardType() != 1);
classes:i/e0.java:135:        menuT.setQwertyMode(KeyCharacterMap.load(keyEvent.getDeviceId()).getKeyboardType() != 1);
classes:com/appsflyer/internal/AFa1uSDK.java:2929:                            if (map.remove("android_id") != null) {
classes:com/appsflyer/internal/AFg1qSDK.java:395:                map.put("android_id", revenue);
classes:com/appsflyer/internal/AFg1qSDK.java:399:                map.put("android_id", revenue);
classes:com/appsflyer/internal/AFg1qSDK.java:912:            String string = Settings.Secure.getString(aFg1qSDK.getMediationNetwork.getContentResolver(), "android_id");
classes:com/appsflyer/internal/AFd1nSDK.java:457:                    this.getMediationNetwork.put("android_id", str3);
classes:androidx/core/widget/NestedScrollView.java:1425:            getScrollFeedbackProvider().a.onScrollProgress(motionEvent.getDeviceId(), motionEvent.getSource(), i6, scrollY2);
classes:androidx/core/widget/NestedScrollView.java:1437:                    getScrollFeedbackProvider().a.onScrollLimit(motionEvent.getDeviceId(), motionEvent.getSource(), i6, true);
classes:androidx/core/widget/NestedScrollView.java:1446:                getScrollFeedbackProvider().a.onScrollLimit(motionEvent.getDeviceId(), motionEvent.getSource(), i6, false);
classes:androidx/core/view/DifferentialMotionFlingController.java:66:        int deviceId = motionEvent.getDeviceId();
classes:androidx/core/view/DifferentialMotionFlingController.java:76:            int deviceId2 = motionEvent.getDeviceId();
```

### gsf_id — 0 hits in 0 files


```
```

### advertising_id — 31 hits in 7 files

- `classes3:pe/a.java` (13)
- `classes:com/discord/ads/AdsModule.java` (7)
- `classes3:ah/a.java` (4)
- `classes:com/appsflyer/internal/AFe1aSDK.java` (2)
- `classes:com/appsflyer/internal/AFe1fSDK.java` (2)
- `classes3:com/google/android/gms/ads/identifier/AdvertisingIdClient$Info.java` (2)
- `classes:a1/k.java` (1)

```
classes:a1/k.java:115:                AdsModule.getAdvertisingIdInfoAsync$lambda$1$lambda$0((SettableFuture) obj2, (AdsModule) obj);
classes:com/appsflyer/internal/AFe1aSDK.java:3:import android.adservices.measurement.MeasurementManager;
classes:com/appsflyer/internal/AFe1aSDK.java:127:        MeasurementManager measurementManagerC;
classes:com/appsflyer/internal/AFe1fSDK.java:8:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
classes:com/appsflyer/internal/AFe1fSDK.java:329:            AdvertisingIdClient.Info infoA = pe.a.a(p02);
classes:com/discord/ads/AdsModule.java:11:import com.google.android.gms.ads.identifier.AdvertisingIdClient;
classes:com/discord/ads/AdsModule.java:28:@Metadata(d1 = {"\u00006\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u00
classes:com/discord/ads/AdsModule.java:56:    private final ListenableFuture getAdvertisingIdInfoAsync() {
classes:com/discord/ads/AdsModule.java:64:    public static final void getAdvertisingIdInfoAsync$lambda$1$lambda$0(SettableFuture settableFuture, AdsModule adsModule) {
classes:com/discord/ads/AdsModule.java:66:            AdvertisingIdClient.Info infoA = a.a(adsModule.getReactApplicationContext());
classes:com/discord/ads/AdsModule.java:89:        ListenableFuture advertisingIdInfoAsync = getAdvertisingIdInfoAsync();
classes:com/discord/ads/AdsModule.java:104:            public void onSuccess(AdvertisingIdClient.Info adInfo) {
```

### install_referrer — 52 hits in 9 files

- `classes:com/android/installreferrer/api/b.java` (17)
- `classes:com/appsflyer/internal/AFi1bSDK.java` (12)
- `classes:com/discord/analytics/InstallReferrerModule.java` (10)
- `classes:com/discord/analytics/InstallReferrerModuleKt.java` (4)
- `classes:com/android/installreferrer/api/InstallReferrerClient.java` (3)
- `classes:com/android/installreferrer/api/a.java` (2)
- `classes:com/appsflyer/internal/AFj1mSDK.java` (2)
- `classes:com/android/installreferrer/api/ReferrerDetails.java` (1)
- `classes:com/android/installreferrer/api/InstallReferrerClientImpl$ClientState.java` (1)

```
classes:com/android/installreferrer/api/a.java:29:        InstallReferrerCommons.logVerbose("InstallReferrerClient", "Install Referrer service connected.");
classes:com/android/installreferrer/api/a.java:45:        InstallReferrerCommons.logWarn("InstallReferrerClient", "Install Referrer service disconnected.");
classes:com/android/installreferrer/api/ReferrerDetails.java:32:    public String getInstallReferrer() {
classes:com/android/installreferrer/api/InstallReferrerClientImpl$ClientState.java:8:public @interface InstallReferrerClientImpl$ClientState {
classes:com/android/installreferrer/api/InstallReferrerClient.java:8:public abstract class InstallReferrerClient {
classes:com/android/installreferrer/api/InstallReferrerClient.java:17:        public InstallReferrerClient build() {
classes:com/android/installreferrer/api/InstallReferrerClient.java:42:    public abstract ReferrerDetails getInstallReferrer();
classes:com/android/installreferrer/api/b.java:16:public final class b extends InstallReferrerClient {
classes:com/android/installreferrer/api/b.java:32:    @Override // com.android.installreferrer.api.InstallReferrerClient
classes:com/android/installreferrer/api/b.java:36:            InstallReferrerCommons.logVerbose("InstallReferrerClient", "Unbinding from service.");
classes:com/android/installreferrer/api/b.java:43:    @Override // com.android.installreferrer.api.InstallReferrerClient
classes:com/android/installreferrer/api/b.java:44:    public final ReferrerDetails getInstallReferrer() throws RemoteException {
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

### screen_capture_detect — 7 hits in 2 files

- `classes3:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java` (6)
- `classes3:io/sentry/react/RNSentryModuleImpl.java` (1)

```
classes3:io/sentry/react/RNSentryModuleImpl.java:110:    private static final int SCREENSHOT_TIMEOUT_SECONDS = 2;
classes3:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:38:    private static final int SCREENSHOT_OUTPUT_SIZE_HINT = 65536;
classes3:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:39:    private static final int SCREENSHOT_QUALITY = 80;
classes3:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:40:    private static final float SCREENSHOT_SCALE_FACTOR = 1.0f;
classes3:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:372:            bitmapCreateScaledBitmap = Bitmap.createScaledBitmap(bitmap, (int) ((width / f) * SCREENSHOT_SCALE_FACTOR), (int) ((height / f) * SCREENSHOT_SCALE_FACTOR), true);
classes3:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:375:                ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(SCREENSHOT_OUTPUT_SIZE_HINT);
classes3:com/facebook/react/devsupport/inspector/FrameTimingsObserver.java:377:                    bitmapCreateScaledBitmap.compress(compressFormat, SCREENSHOT_QUALITY, byteArrayOutputStream);
```

### audio_capture — 1 hits in 1 files

- `classes4:org/webrtc/audio/WebRtcAudioRecord.java` (1)

```
classes4:org/webrtc/audio/WebRtcAudioRecord.java:147:        return new AudioRecord(i, i2, i3, i4, i5);
```

### accessibility — 134 hits in 26 files

- `classes3:com/facebook/react/modules/accessibilityinfo/AccessibilityInfoModule.java` (24)
- `classes:com/discord/device/DeviceAccessibilityModule.java` (8)
- `classes3:oh/k.java` (8)
- `classes3:com/facebook/react/views/view/ReactViewGroup.java` (8)
- `classes3:sg/f.java` (7)
- `classes3:oh/n.java` (7)
- `classes3:oh/t.java` (6)
- `classes3:el/i.java` (6)
- `classes3:com/google/android/material/behavior/HideBottomViewOnScrollBehavior.java` (6)
- `classes3:com/google/android/material/behavior/HideViewOnScrollBehavior.java` (6)
- `classes:androidx/customview/widget/a.java` (5)
- `classes:androidx/recyclerview/widget/RecyclerView.java` (4)

```
classes:androidx/recyclerview/widget/RecyclerView.java:36:import android.view.accessibility.AccessibilityManager;
classes:androidx/recyclerview/widget/RecyclerView.java:102:    private final AccessibilityManager mAccessibilityManager;
classes:androidx/recyclerview/widget/RecyclerView.java:5404:        AccessibilityManager accessibilityManager = this.mAccessibilityManager;
classes:androidx/recyclerview/widget/RecyclerView.java:7494:        this.mAccessibilityManager = (AccessibilityManager) getContext().getSystemService("accessibility");
classes:androidx/core/view/s0.java:15:import android.view.accessibility.AccessibilityManager;
classes:androidx/core/view/s0.java:197:        AccessibilityManager accessibilityManager = (AccessibilityManager) view.getContext().getSystemService("accessibility");
classes:androidx/appcompat/widget/a4.java:17:import android.view.accessibility.AccessibilityManager;
classes:androidx/appcompat/widget/a4.java:300:            AccessibilityManager accessibilityManager = (AccessibilityManager) view2.getContext().getSystemService("accessibility");
classes:androidx/appcompat/widget/a4.java:301:            if (!accessibilityManager.isEnabled() || !accessibilityManager.isTouchExplorationEnabled()) {
classes:androidx/customview/widget/a.java:10:import android.view.accessibility.AccessibilityManager;
classes:androidx/customview/widget/a.java:37:    private final AccessibilityManager mManager;
classes:androidx/customview/widget/a.java:52:        this.mManager = (AccessibilityManager) view.getContext().getSystemService("accessibility");
```

### root_emulator — 27 hits in 6 files

- `classes:com/appsflyer/R.java` (14)
- `classes:com/discord/chrome_custom_tabs/TrackedCustomTab.java` (6)
- `classes:com/appsflyer/internal/AFf1kSDK.java` (4)
- `classes:com/discord/chrome_custom_tabs/CustomTabHostActivity.java` (1)
- `classes3:oh/k.java` (1)
- `classes3:io/sentry/android/core/internal/util/i.java` (1)

```
classes:com/appsflyer/internal/AFf1kSDK.java:43:            put("aq", "ro.kernel.qemu");
classes:com/appsflyer/internal/AFf1kSDK.java:85:                    if (stackTraceElement.toString().contains("de.robv.android.xposed") && i6 <= 2) {
classes:com/appsflyer/internal/AFf1kSDK.java:111:            if (AFAdRevenueData(sb2.toString(), "frida")) {
classes:com/appsflyer/internal/AFf1kSDK.java:118:            AFLogger.afErrorLogForExcManagerOnly("frida detection error", e9);
classes:com/appsflyer/R.java:1095:        public static int textInputFilledExposedDropdownMenuStyle = 0x7f0405b7;
classes:com/appsflyer/R.java:1099:        public static int textInputOutlinedExposedDropdownMenuStyle = 0x7f0405bb;
classes:com/appsflyer/R.java:2404:        public static int mtrl_exposed_dropdown_menu_popup_elevation = 0x7f0703d9;
classes:com/appsflyer/R.java:2405:        public static int mtrl_exposed_dropdown_menu_popup_vertical_offset = 0x7f0703da;
classes:com/appsflyer/R.java:2406:        public static int mtrl_exposed_dropdown_menu_popup_vertical_padding = 0x7f0703db;
classes:com/appsflyer/R.java:3396:        public static int exposed_dropdown_menu_content_description = 0x7f1300b5;
classes:com/appsflyer/R.java:4467:        public static int Widget_Material3_TextInputLayout_FilledBox_Dense_ExposedDropdownMenu = 0x7f140492;
classes:com/appsflyer/R.java:4468:        public static int Widget_Material3_TextInputLayout_FilledBox_ExposedDropdownMenu = 0x7f140493;
```

### js_bridge — 1 hits in 1 files

- `classes3:com/reactnativecommunity/webview/j.java` (1)

```
classes3:com/reactnativecommunity/webview/j.java:158:        addJavascriptInterface(iVar, "ReactNativeWebView");
```

### boot_persist — 0 hits in 0 files


```
```

### full_screen_intent — 1 hits in 1 files

- `classes3:ad/d0.java` (1)

```
classes3:ad/d0.java:433:        ((Notification.Builder) this.i).setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.led [... omitted en
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 50 hits in 23 files

- `classes:com/discord/mobile_voice_overlay/views/OverlayVoiceSelectorBubbleDialog.java` (12)
- `classes3:com/facebook/react/views/textinput/ReactEditText.java` (7)
- `classes:com/discord/chat/input/views/ChatInputRootView.java` (3)
- `classes:k2/v.java` (2)
- `classes:androidx/appcompat/widget/AppCompatTextView.java` (2)
- `classes:androidx/appcompat/widget/s.java` (2)
- `classes:com/discord/chat/input/plugins/DeleteNodeOnBackspaceTextWatcher.java` (2)
- `classes:com/discord/chat/input/views/DCDChatInput.java` (2)
- `classes3:com/facebook/react/views/textinput/ReactTextInputTextWatcher.java` (2)
- `classes3:com/google/android/material/button/MaterialButton.java` (2)
- `classes3:com/facebook/drawee/span/SimpleDraweeSpanTextView.java` (2)
- `classes:k2/w.java` (1)

```
classes:k2/v.java:74:    public final void onTextChanged(CharSequence charSequence, int i5, int i6, int i8) {
classes:k2/v.java:75:        ((TextWatcher) this.f4043d).onTextChanged(charSequence, i5, i6, i8);
classes:k2/w.java:50:            ((v) arrayList.get(i5)).onTextChanged(this, 0, length(), length());
classes:m2/i.java:50:    public final void onTextChanged(CharSequence charSequence, int i5, int i6, int i8) throws Throwable {
classes:com/discord/mobile_voice_overlay/views/OverlayVoiceSelectorBubbleDialog.java:37:@Metadata(d1 = {"\u0000l\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0002\b\u0005\n\u0002
classes:com/discord/mobile_voice_overlay/views/OverlayVoiceSelectorBubbleDialog.java:53:    private Function1<? super String, Unit> onTextChanged;
classes:com/discord/mobile_voice_overlay/views/OverlayVoiceSelectorBubbleDialog.java:68:        this.onTextChanged = new com.discord.chat.presentation.textutils.c(29);
classes:com/discord/mobile_voice_overlay/views/OverlayVoiceSelectorBubbleDialog.java:118:    public static final Unit onTextChanged$lambda$1(String str) {
classes:com/discord/mobile_voice_overlay/views/OverlayVoiceSelectorBubbleDialog.java:127:        editText.addTextChangedListener(new TextWatcher() { // from class: com.discord.mobile_voice_overlay.views.OverlayVoiceSelectorBubbleDialog$onViewBound$$inlined$doOnTextChanged$1
classes:com/discord/mobile_voice_overlay/views/OverlayVoiceSelectorBubbleDialog.java:137:            public void onTextChanged(CharSequence text, int start, int before, int count) {
classes:com/discord/mobile_voice_overlay/views/OverlayVoiceSelectorBubbleDialog.java:139:                Function1<String, Unit> onTextChanged = this.this$0.getOnTextChanged();
classes:com/discord/mobile_voice_overlay/views/OverlayVoiceSelectorBubbleDialog.java:143:                onTextChanged.invoke(string);
```

### webview_tracking — 4 hits in 1 files

- `classes3:com/reactnativecommunity/webview/RNCWebViewManager.java` (4)

```
classes3:com/reactnativecommunity/webview/RNCWebViewManager.java:509:    private static /* synthetic */ void lambda$setThirdPartyCookiesEnabled$14(boolean z, j jVar) {
classes3:com/reactnativecommunity/webview/RNCWebViewManager.java:510:        CookieManager.getInstance().setAcceptThirdPartyCookies(jVar, z);
classes3:com/reactnativecommunity/webview/RNCWebViewManager.java:1116:    public void setThirdPartyCookiesEnabled(c cVar, boolean z) {
classes3:com/reactnativecommunity/webview/RNCWebViewManager.java:1119:            lambda$setThirdPartyCookiesEnabled$14(z, jVar);
```

### streaks — 0 hits in 0 files


```
```

### reengagement — 469 hits in 121 files

- `classes:com/discord/misc/utilities/time/TimeElapsed.java` (22)
- `classes:com/appsflyer/R.java` (20)
- `classes3:ic/x.java` (18)
- `classes3:ng/k.java` (18)
- `classes:com/discord/lifecycle/ActivityResumedTracker.java` (17)
- `classes3:le/i.java` (15)
- `classes:app/rive/runtime/kotlin/controllers/RiveFileController.java` (13)
- `classes3:cd/s.java` (13)
- `classes3:td/b.java` (13)
- `classes:com/discord/lifecycle/ForegroundServiceStartGuard.java` (12)
- `classes3:io/sentry/android/core/s.java` (10)
- `classes4:org/webrtc/ThreadUtils.java` (10)

```
classes:u4/c.java:331:            ((com.google.android.gms.net.b) this.f5370d).b.set(SystemClock.elapsedRealtime());
classes:a5/h0.java:121:        long jElapsedRealtime = SystemClock.elapsedRealtime();
classes:a5/h0.java:122:        long j5 = j + jElapsedRealtime;
classes:a5/h0.java:123:        if (j5 < jElapsedRealtime) {
classes:a5/h0.java:126:            while (!this.f175e && jElapsedRealtime < j5) {
classes:a5/h0.java:127:                wait(j5 - jElapsedRealtime);
classes:a5/h0.java:129:                jElapsedRealtime = SystemClock.elapsedRealtime();
classes:n/n.java:21:    public final void onActionViewCollapsed() {
classes:n/n.java:22:        this.f4471d.onActionViewCollapsed();
classes:m/a.java:5:    void onActionViewCollapsed();
classes:c5/g.java:39:        SystemClock.elapsedRealtime();
classes:c5/g.java:67:                SystemClock.elapsedRealtime();
```

### notif_permission_nag — 151 hits in 14 files

- `classes:com/discord/chat/presentation/message/view/ForumPostActionBarView.java` (28)
- `classes:com/discord/chat/bridge/forums/ForumPostActions.java` (27)
- `classes:com/discord/chat/bridge/forums/PostSharePrompt.java` (21)
- `classes:com/discord/chat/reactevents/TapDismissMediaPostSharePromptData.java` (16)
- `classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java` (12)
- `classes:com/discord/chat/bridge/forums/PostSharePrompt$$serializer.java` (11)
- `classes:com/discord/chat/reactevents/TapDismissMediaPostSharePromptData$$serializer.java` (10)
- `classes:com/discord/chat/bridge/forums/ForumPostActions$$serializer.java` (8)
- `classes:com/discord/chat/presentation/events/ChatEventHandler.java` (6)
- `classes:com/discord/chat/reactevents/ChatViewEventHandler.java` (4)
- `classes:com/discord/chat/presentation/message/viewholder/ForumPostActionBarViewHolder.java` (4)
- `classes:com/discord/chat/presentation/events/CreateChatReactEventsKt.java` (2)

```
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:54:    public final DCDButton sharePromptCloseButton;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:57:    public final ConstraintLayout sharePromptContainer;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:60:    public final DCDButton sharePromptCopyLinkButton;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:63:    public final SimpleDraweeView sharePromptIcon;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:66:    public final SimpleDraweeSpanTextView sharePromptSubtitle;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:69:    public final TextView sharePromptTitle;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:88:        this.sharePromptCloseButton = dCDButton4;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:89:        this.sharePromptContainer = constraintLayout;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:90:        this.sharePromptCopyLinkButton = dCDButton5;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:91:        this.sharePromptIcon = simpleDraweeView;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:92:        this.sharePromptSubtitle = simpleDraweeSpanTextView;
classes:com/discord/chat/databinding/ForumPostActionBarViewBinding.java:93:        this.sharePromptTitle = textView;
```

### cancellation_retention — 0 hits in 0 files


```
```

### urgency_countdown — 238 hits in 60 files

- `classes4:org/webrtc/EglRenderer.java` (16)
- `classes:com/appsflyer/internal/AFe1aSDK.java` (9)
- `classes:com/appsflyer/internal/AFe1fSDK.java` (9)
- `classes3:y8/c.java` (9)
- `classes:app/rive/HardwareRenderBuffer.java` (8)
- `classes3:jf/a.java` (8)
- `classes4:org/webrtc/ThreadUtils.java` (8)
- `classes3:com/facebook/react/ReactPackageTurboModuleManagerDelegate.java` (7)
- `classes:app/rive/core/CommandQueue.java` (6)
- `classes:com/discord/MainApplication.java` (6)
- `classes:com/discord/image/core/FrescoModuleDiscord.java` (6)
- `classes:com/discord/media/engine/video/egl_renderer/EglRenderer.java` (6)

```
classes:a5/k0.java:31:import java.util.concurrent.CountDownLatch;
classes:a5/k0.java:709:        ((CountDownLatch) lVar.d).await();
classes:a5/k0.java:730:        if (((CountDownLatch) lVar.d).await(j, timeUnit)) {
classes:a5/s.java:32:import java.util.concurrent.CountDownLatch;
classes:a5/s.java:295:                lVarC.b(xe.g.e, new qa.t(12, (CountDownLatch) this.f222v));
classes:a1/k.java:52:import java.util.concurrent.CountDownLatch;
classes:a1/k.java:145:                EglRenderer.release$lambda$15$lambda$13((EglRenderer) obj2, (CountDownLatch) obj);
classes:a3/h.java:424:                    cVar2.w.countDown();
classes:app/rive/core/CommandQueue.java:27:import java.util.concurrent.CountDownLatch;
classes:app/rive/core/CommandQueue.java:58:@Metadata(d1 = {"\u0000È\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u0002\n\u0002\b\u0005\n\u0002\u0010\t\n\u0002\b\u000
classes:app/rive/core/CommandQueue.java:120:    private final CountDownLatch shutdownComplete;
classes:app/rive/core/CommandQueue.java:523:                commandQueue.shutdownComplete.countDown();
```

### infinite_autoplay — 258 hits in 43 files

- `classes:app/rive/runtime/kotlin/RiveAnimationView.java` (38)
- `classes:app/rive/runtime/kotlin/controllers/RiveFileController.java` (20)
- `classes:com/discord/chat/bridge/Message.java` (18)
- `classes:com/discord/media_player/MediaSource.java` (14)
- `classes:com/discord/chat/presentation/message/view/EmbedView.java` (14)
- `classes:com/discord/chat/presentation/message/view/botuikit/ComponentContext.java` (14)
- `classes:com/discord/chat/presentation/message/messagepart/polls/PollAnswerAccessory.java` (13)
- `classes:com/discord/chat/presentation/message/messagepart/MediaMosaicAttachmentMessageAccessory.java` (13)
- `classes:com/discord/chat/presentation/message/messagepart/EmbedMessageAccessory.java` (13)
- `classes3:com/margelo/nitro/rive/HybridRiveView.java` (10)
- `classes:com/discord/chat/presentation/message/view/MediaImageView.java` (7)
- `classes:com/discord/chat/presentation/message/view/mosaic_recycler/AttachmentMediaMosaicAdapter.java` (6)

```
classes:com/airbnb/android/react/lottie/LottieAnimationViewManager.java:36:@Metadata(d1 = {"\u0000\u0084\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010$\n\u0002\u0010\u000e\n\u0002\u0010\u0000\n\
classes:com/airbnb/android/react/lottie/LottieAnimationViewManager.java:213:    @ReactProp(name = "autoPlay")
classes:com/airbnb/android/react/lottie/LottieAnimationViewManager.java:214:    public void setAutoPlay(@NotNull h view, boolean autoPlay) {
classes:com/airbnb/android/react/lottie/LottieAnimationViewManager.java:218:        orCreatePropertyManager.f4077q = Boolean.valueOf(autoPlay);
classes:app/rive/runtime/kotlin/RiveAnimationView.java:73:@Metadata(d1 = {"\u0000\u009a\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u000
classes:app/rive/runtime/kotlin/RiveAnimationView.java:89:    private final boolean defaultAutoplay;
classes:app/rive/runtime/kotlin/RiveAnimationView.java:110:    @Metadata(d1 = {"\u0000Z\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000e\n\u0002\b\b\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0
classes:app/rive/runtime/kotlin/RiveAnimationView.java:119:        private Boolean autoplay;
classes:app/rive/runtime/kotlin/RiveAnimationView.java:170:        /* renamed from: getAutoplay$kotlin_release, reason: from getter */
classes:app/rive/runtime/kotlin/RiveAnimationView.java:171:        public final Boolean getAutoplay() {
classes:app/rive/runtime/kotlin/RiveAnimationView.java:172:            return this.autoplay;
classes:app/rive/runtime/kotlin/RiveAnimationView.java:286:        public final Builder setAutoplay(boolean value) {
```

### badges — 3 hits in 3 files

- `classes:x0/k.java` (1)
- `classes:app/rive/ViewModelInstance.java` (1)
- `classes3:ad/d0.java` (1)

```
classes:x0/k.java:25:        builder.setBadgeIconType(i5);
classes:app/rive/ViewModelInstance.java:842:    public final void setNumber(@NotNull String propertyPath, float value) {
classes3:ad/d0.java:433:        ((Notification.Builder) this.i).setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.led [... omitted en
```

### minors_age — 7 hits in 3 files

- `classes:com/discord/R.java` (4)
- `classes:com/discord/age_assurance/PlayAgeSignalsModuleKt.java` (2)
- `classes3:qh/b.java` (1)

```
classes:com/discord/age_assurance/PlayAgeSignalsModuleKt.java:78:                if (str.equals("under_13")) {
classes:com/discord/age_assurance/PlayAgeSignalsModuleKt.java:130:                if (str.equals("under_13_declined")) {
classes:com/discord/R.java:1126:        public static int modules_age_gate_native_images_check = 0x7f0805ac;
classes:com/discord/R.java:1127:        public static int modules_age_gate_native_images_nsfw_gate = 0x7f0805ad;
classes:com/discord/R.java:1128:        public static int modules_age_gate_native_images_nsfw_gate_lock = 0x7f0805ae;
classes:com/discord/R.java:1129:        public static int modules_age_gate_native_images_nsfw_gate_unavailable = 0x7f0805af;
classes3:qh/b.java:7:    public static final Intent a = new Intent("com.google.android.finsky.ageverification.BIND").setPackage("com.android.vending");
```

### screen_time — 1 hits in 1 files

- `classes3:pe/a.java` (1)

```
classes3:pe/a.java:68:            map.put("time_spent", Long.toString(j));
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
strings.xml:205:    <string name="firebase_database_url">https://adept-ethos-91518.firebaseio.com</string>
```

### guilt_copy — 0 strings

```
```

### subscription_copy — 3 strings

```
strings.xml:226:    <string name="m3_exceed_max_badge_text_suffix">%1$s%2$s</string>
strings.xml:286:    <string name="mtrl_exceed_max_badge_number_content_description">More than %1$d new notifications</string>
strings.xml:287:    <string name="mtrl_exceed_max_badge_number_suffix">%1$d%2$s</string>
```

### data_copy — 7 strings

```
strings.xml:51:    <string name="catalyst_change_bundle_location">Change Bundle Location</string>
strings.xml:52:    <string name="catalyst_change_bundle_location_apply">Apply Changes</string>
strings.xml:53:    <string name="catalyst_change_bundle_location_cancel">Cancel</string>
strings.xml:54:    <string name="catalyst_change_bundle_location_input_hint">127.0.0.1:8081</string>
strings.xml:55:    <string name="catalyst_change_bundle_location_input_label">Provide a custom bundler address and port:</string>
strings.xml:56:    <string name="catalyst_change_bundle_location_instructions">"You can connect either via USB (localhost - default) or Wifi. If you connect via USB and running with a physical device, make sure you:
strings.xml:58: 2. Set the bundle location to `localhost:8081`
```

