# Pattern scan: work/snapchat/jadx

## Code categories (library packages excluded)

### installed_apps — 52 hits in 42 files

- `defpackage/AbstractC56418zyn.java` (4)
- `com/google/android/gms/common/a.java` (3)
- `com/google/ar/core/SessionCreateJniHelper.java` (2)
- `defpackage/Ton.java` (2)
- `defpackage/C2471Dv6.java` (2)
- `defpackage/OYm.java` (2)
- `defpackage/C17243aS1.java` (2)
- `androidx/credentials/playservices/CredentialProviderPlayServicesImpl.java` (1)
- `com/amazon/identity/auth/device/AndroidManifest.java` (1)
- `com/google/ar/core/m.java` (1)
- `org/chromium/base/BuildInfo.java` (1)
- `defpackage/C36582n2n.java` (1)

```
androidx/credentials/playservices/CredentialProviderPlayServicesImpl.java:315:                long j = context.getPackageManager().getPackageInfo("com.google.android.gms", 0).versionCode;
com/amazon/identity/auth/device/AndroidManifest.java:21:        return !context.getPackageManager().queryIntentActivities(intent, 65536).isEmpty();
com/google/ar/core/SessionCreateJniHelper.java:21:            PackageInfo packageInfo = context.getPackageManager().getPackageInfo("com.google.ar.core", 64);
com/google/ar/core/SessionCreateJniHelper.java:38:            return context.getPackageManager().getPackageInfo("com.google.ar.core", 0).versionCode;
com/google/ar/core/m.java:44:            PackageInfo packageInfo = context.getPackageManager().getPackageInfo("com.google.ar.core", 4);
org/chromium/base/BuildInfo.java:53:                packageInfo = packageManager.getPackageInfo("com.google.android.gms", 0);
com/google/android/gms/common/a.java:37:            return context.getPackageManager().getPackageInfo("com.google.android.gms", 0).versionCode;
com/google/android/gms/common/a.java:147:                packageInfo = packageManager.getPackageInfo("com.android.vending", Build.VERSION.SDK_INT >= 28 ? 134225984 : 8256);
com/google/android/gms/common/a.java:155:            PackageInfo packageInfo2 = packageManager.getPackageInfo("com.google.android.gms", Build.VERSION.SDK_INT >= 28 ? 134217792 : 64);
defpackage/Ton.java:30:                    Signature[] signatureArr = context.getPackageManager().getPackageInfo("com.android.vending", 64).signatures;
defpackage/Ton.java:86:            return ((long) this.b.getPackageManager().getPackageInfo("com.android.vending", 0).versionCode) >= 85222500;
defpackage/C36582n2n.java:31:                Signature[] signatureArr = context.getPackageManager().getPackageInfo("com.android.vending", 64).signatures;
```

### usage_stats — 0 hits in 0 files


```
```

### clipboard — 5 hits in 5 files

- `com/snap/identity/api/sharedui/VerificationCodeEditTextView.java` (1)
- `com/snap/messaging/chat/features/input/InputBarEditText.java` (1)
- `com/snap/content/comments/core/ui/tray/tab/live/inputbar/CommentsInputEditText.java` (1)
- `defpackage/L33.java` (1)
- `defpackage/C13901Vx3.java` (1)

```
com/snap/identity/api/sharedui/VerificationCodeEditTextView.java:160:        if (clipboardManager != null && (primaryClip = clipboardManager.getPrimaryClip()) != null) {
com/snap/messaging/chat/features/input/InputBarEditText.java:81:            if (clipboardManager != null && (primaryClip = clipboardManager.getPrimaryClip()) != null && (cVcN = n(primaryClip.getDescription())) != CVc.UNRECOGNIZED_VALUE && primaryClip.getItemCount() > 0) {
com/snap/content/comments/core/ui/tray/tab/live/inputbar/CommentsInputEditText.java:29:                ClipData primaryClip = clipboardManager != null ? clipboardManager.getPrimaryClip() : null;
defpackage/L33.java:260:                ClipData primaryClip = c13901Vx3.c().getPrimaryClip();
defpackage/C13901Vx3.java:44:        if (z && c().hasPrimaryClip()) {
```

### contacts — 29 hits in 13 files

- `defpackage/IBk.java` (4)
- `defpackage/CallableC34303lZ3.java` (3)
- `defpackage/SE0.java` (3)
- `defpackage/C37901nu7.java` (2)
- `defpackage/U0m.java` (2)
- `defpackage/C25763g00.java` (2)
- `defpackage/C6456Kd7.java` (2)
- `defpackage/FB6.java` (2)
- `defpackage/C12253Th4.java` (2)
- `defpackage/C0111Ac0.java` (2)
- `defpackage/C23634ec7.java` (2)
- `defpackage/C43861rn5.java` (2)

```
defpackage/IBk.java:6:import android.provider.ContactsContract;
defpackage/IBk.java:49:            Uri uriLookupContact = ContactsContract.Contacts.lookupContact(contentResolver, uri);
defpackage/IBk.java:53:            inputStreamOpenContactPhotoInputStream = ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uriLookupContact, true);
defpackage/IBk.java:55:            inputStreamOpenContactPhotoInputStream = ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uri, true);
defpackage/CallableC34303lZ3.java:5:import android.provider.ContactsContract;
defpackage/CallableC34303lZ3.java:137:                    inputStreamOpenContactPhotoInputStream = ContactsContract.Contacts.openContactPhotoInputStream((ContentResolver) c0432Ap3.b, ContactsContract.Profile.CONTENT_URI, true);
defpackage/CallableC34303lZ3.java:155:                Cursor cursorQuery = c12884Uh4.a.getContentResolver().query(ContactsContract.Contacts.CONTENT_URI, new String[]{"_id"}, null, null, null);
defpackage/SE0.java:6:import android.provider.ContactsContract;
defpackage/SE0.java:21:        return ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI).withValueBackReference("raw_contact_id", 0);
defpackage/SE0.java:42:        Cursor cursorF = f(this, ContactsContract.Data.CONTENT_URI, "raw_contact_id = ?", new String[]{str}, 2);
defpackage/C1293Byh.java:183:        c49687vaj.c(null, "CREATE TABLE IF NOT EXISTS Contact(\n    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\n    friendRowId INTEGER,\n    displayName TEXT,\n    -- Formatted number suitable for UI\n    phone TEXT NOT NULL,\n    -- Last modified timest [... omitt
defpackage/C37901nu7.java:6:import android.provider.ContactsContract;
```

### call_log — 0 hits in 0 files


```
```

### sms — 12 hits in 9 files

- `defpackage/C17096aLn.java` (3)
- `defpackage/C19737c4i.java` (2)
- `com/snap/ms/authapiphone/gms/GoogleSmsRetrieverV2.java` (1)
- `defpackage/C51842wzl.java` (1)
- `defpackage/PJc.java` (1)
- `defpackage/IMc.java` (1)
- `defpackage/GLn.java` (1)
- `defpackage/C4759Hl8.java` (1)
- `defpackage/C50852wLc.java` (1)

```
com/snap/ms/authapiphone/gms/GoogleSmsRetrieverV2.java:15:public final class GoogleSmsRetrieverV2 extends BroadcastReceiver {
defpackage/C19737c4i.java:153:                intent2.setPackage(Telephony.Sms.getDefaultSmsPackage(context));
defpackage/C19737c4i.java:194:                intent.setPackage(Telephony.Sms.getDefaultSmsPackage(context));
defpackage/C51842wzl.java:175:        ((LB6) gCh).a(new BB0(c33400kyd, "GoogleSmsRetrieverRegistry"));
defpackage/PJc.java:487:                String defaultSmsPackage = Telephony.Sms.getDefaultSmsPackage(context);
defpackage/IMc.java:40:        parcelObtain.writeInterfaceToken("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService");
defpackage/GLn.java:19:        attachInterface(this, "com.google.android.gms.auth.api.phone.internal.ISmsRetrieverResultCallback");
defpackage/C4759Hl8.java:15:    public static final TQm q = new TQm("SmsRetriever.API", new C22976eBa(11), new C44922sTm());
defpackage/C50852wLc.java:46:        parcelObtain.writeInterfaceToken("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService");
defpackage/C17096aLn.java:20:        IInterface iInterfaceQueryLocalInterface = iBinder.queryLocalInterface("com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService");
defpackage/C17096aLn.java:31:        return "com.google.android.gms.auth.api.phone.internal.ISmsRetrieverApiService";
defpackage/C17096aLn.java:36:        return "com.google.android.gms.auth.api.phone.service.SmsRetrieverApiService.START";
```

### location — 15 hits in 12 files

- `com/looksery/sdk/DefaultDeviceLocationTracker.java` (2)
- `defpackage/C12046Syj.java` (2)
- `defpackage/FAl.java` (2)
- `com/snap/ad_web_browser/AutofillLocationProvider.java` (1)
- `defpackage/Y00.java` (1)
- `defpackage/C19955cDb.java` (1)
- `defpackage/KX3.java` (1)
- `defpackage/RunnableC16573a10.java` (1)
- `defpackage/C52493xQ0.java` (1)
- `defpackage/C13879Vw5.java` (1)
- `defpackage/InterfaceC49168vFb.java` (1)
- `defpackage/C33248ksb.java` (1)

```
com/snap/ad_web_browser/AutofillLocationProvider.java:14:    Promise<GeoPoint> getCurrentLocation();
defpackage/Y00.java:84:                ((UZk) this.c).d(((LocationManager) ((C42996rE) this.b).b).getLastKnownLocation((String) this.t));
com/looksery/sdk/DefaultDeviceLocationTracker.java:86:                            this.mLocation = this.mLocationManager.getLastKnownLocation(str);
com/looksery/sdk/DefaultDeviceLocationTracker.java:89:                            this.mLocationManager.requestLocationUpdates(str, locationTrackingParameters.getLocationUpdateIntervalMillis(), locationTrackingParameters.getDistanceFilterMeters(), this, this.mHandler.getLooper());
defpackage/C12046Syj.java:672:            Location lastKnownLocation = locationManager.getLastKnownLocation("gps");
defpackage/C12046Syj.java:674:                lastKnownLocation = locationManager.getLastKnownLocation("network");
defpackage/C19955cDb.java:24:    public final Maybe getCurrentLocation() {
defpackage/KX3.java:21:    public final Promise getCurrentLocation() {
defpackage/FAl.java:33:            lastKnownLocation = this.b.isProviderEnabled("network") ? this.b.getLastKnownLocation("network") : null;
defpackage/FAl.java:38:                    lastKnownLocation2 = this.b.getLastKnownLocation("gps");
defpackage/RunnableC16573a10.java:38:                ((LocationManager) c42996rE.b).requestLocationUpdates((String) this.c, j, c25761g.I, (Z00) this.I, (Looper) this.X);
defpackage/C52493xQ0.java:21:    public Promise<GeoPoint> getCurrentLocation() {
```

### wifi_bt_scan — 20 hits in 11 files

- `defpackage/PTf.java` (4)
- `defpackage/C10150Pyj.java` (3)
- `defpackage/C4186Gnj.java` (2)
- `defpackage/C15825Yw6.java` (2)
- `defpackage/C51541wnj.java` (2)
- `defpackage/ZWm.java` (2)
- `org/chromium/net/a.java` (1)
- `org/chromium/net/AndroidNetworkLibrary.java` (1)
- `defpackage/C7237Lj9.java` (1)
- `defpackage/E1b.java` (1)
- `defpackage/C35618mQ.java` (1)

```
org/chromium/net/a.java:47:                    return connectionInfo.getSSID();
org/chromium/net/AndroidNetworkLibrary.java:174:        return (wifiInfoA == null || (ssid = wifiInfoA.getSSID()) == null || ssid.equals("<unknown ssid>")) ? BuildConfig.APPLIVERY_SECRET : ssid;
defpackage/PTf.java:5:import android.bluetooth.le.BluetoothLeScanner;
defpackage/PTf.java:105:        BluetoothLeScanner bluetoothLeScanner = null;
defpackage/PTf.java:229:                            bluetoothLeScanner = bluetoothAdapter.getBluetoothLeScanner();
defpackage/PTf.java:232:                            bluetoothLeScanner.startScan(c51541wnj.q, new ScanSettings.Builder().setScanMode(c51541wnj.e.a).build(), c51541wnj.r);
defpackage/C7237Lj9.java:470:        String ssid = (!z || (wifiManager = (WifiManager) ((C29629iW5) this.I).a.getValue()) == null || (connectionInfo = wifiManager.getConnectionInfo()) == null) ? null : connectionInfo.getSSID();
defpackage/C4186Gnj.java:71:                            zStartDiscovery = bluetoothAdapter.startDiscovery();
defpackage/C4186Gnj.java:290:                                    zStartDiscovery = bluetoothAdapter.startDiscovery();
defpackage/E1b.java:39:                        f1b2.i = connectionInfo.getBSSID();
defpackage/C10150Pyj.java:294:                                    if (connectionInfo.getSSID().equals(c12046Syj.Q0)) {
defpackage/C10150Pyj.java:319:                                if (connectionInfo2.getNetworkId() == c12046Syj.P0 && connectionInfo2.getSSID().equals(c12046Syj.Q0)) {
```

### device_ids — 24 hits in 13 files

- `androidx/core/widget/NestedScrollView.java` (6)
- `com/snap/identity/loginsignup/ui/LoginSignupActivity.java` (4)
- `defpackage/C50121vs7.java` (3)
- `defpackage/ViewTreeObserverOnGlobalLayoutListenerC52708xZ.java` (2)
- `com/amazon/identity/auth/device/utils/MAPUtils.java` (1)
- `androidx/appcompat/app/f.java` (1)
- `com/snapchat/client/notifications/AckConfig.java` (1)
- `com/snapchat/client/notifications/TokenRegistrarParameters.java` (1)
- `defpackage/BOm.java` (1)
- `defpackage/ViewOnTouchListenerC12276Ti2.java` (1)
- `defpackage/M53.java` (1)
- `defpackage/C4115Gkl.java` (1)

```
com/amazon/identity/auth/device/utils/MAPUtils.java:101:    public static String getDeviceId() {
androidx/core/widget/NestedScrollView.java:641:            int deviceId = motionEvent.getDeviceId();
androidx/core/widget/NestedScrollView.java:650:                int deviceId2 = motionEvent.getDeviceId();
androidx/core/widget/NestedScrollView.java:672:                int deviceId3 = motionEvent.getDeviceId();
androidx/core/widget/NestedScrollView.java:1542:            ((OGh) this.o0.b).e(motionEvent.getDeviceId(), motionEvent.getSource(), i2, scrollY2);
androidx/core/widget/NestedScrollView.java:1558:                    ((OGh) this.o0.b).b(motionEvent.getDeviceId(), motionEvent.getSource(), i2, false);
androidx/core/widget/NestedScrollView.java:1586:                ((OGh) this.o0.b).b(motionEvent.getDeviceId(), motionEvent.getSource(), i2, true);
androidx/appcompat/app/f.java:1196:                c52047x80.h.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
com/snap/identity/loginsignup/ui/LoginSignupActivity.java:228:            c48832v20.X = motionEvent.getDeviceId();
com/snap/identity/loginsignup/ui/LoginSignupActivity.java:245:            int deviceId = motionEvent.getDeviceId();
com/snap/identity/loginsignup/ui/LoginSignupActivity.java:299:        if (motionEvent.getDeviceId() == 0) {
com/snap/identity/loginsignup/ui/LoginSignupActivity.java:378:        int deviceId = keyEvent.getDeviceId();
```

### gsf_id — 0 hits in 0 files


```
```

### advertising_id — 16 hits in 8 files

- `defpackage/TI.java` (4)
- `defpackage/OA9.java` (4)
- `defpackage/N7n.java` (2)
- `defpackage/NA9.java` (2)
- `com/snap/ms/gms/AdvertisingIdClientInfoFetcherApiService.java` (1)
- `defpackage/AbstractC17022aJ.java` (1)
- `defpackage/C22491ds1.java` (1)
- `defpackage/VI.java` (1)

```
com/snap/ms/gms/AdvertisingIdClientInfoFetcherApiService.java:12:public class AdvertisingIdClientInfoFetcherApiService extends Service {
defpackage/N7n.java:20:import com.snap.ms.gms.AdvertisingIdClientInfoFetcherApiService;
defpackage/N7n.java:111:        AdvertisingIdClientInfoFetcherApiService advertisingIdClientInfoFetcherApiService = (AdvertisingIdClientInfoFetcherApiService) this.b;
defpackage/AbstractC17022aJ.java:12:        Collections.singletonList("AdvertisingIdClientInfoFetcherApiService");
defpackage/NA9.java:23:import com.snap.ms.gms.AdvertisingIdClientInfoFetcherApiService;
defpackage/NA9.java:179:                Intent intent = new Intent(oa9.a, (Class<?>) AdvertisingIdClientInfoFetcherApiService.class);
defpackage/C22491ds1.java:33:        int iE = c34393lcj.e("BlizzardAdInfoFetchHelper.getCachedAdvertisingIdClientInfo");
defpackage/TI.java:60:            mapF.put("tag", "AdvertisingIdClient");
defpackage/TI.java:144:                            throw new IOException("AdvertisingIdClient is not connected.");
defpackage/TI.java:150:                            throw new IOException("AdvertisingIdClient cannot reconnect.");
defpackage/TI.java:153:                        throw new IOException("AdvertisingIdClient cannot reconnect.", e);
defpackage/VI.java:30:        StringBuilder sb = new StringBuilder("AdvertisingIdClientInfo(id=");
```

### install_referrer — 0 hits in 0 files


```
```

### sensors — 0 hits in 0 files


```
```

### accounts — 7 hits in 4 files

- `org/chromium/net/HttpNegotiateAuthenticator.java` (2)
- `defpackage/AbstractC56418zyn.java` (2)
- `defpackage/GA1.java` (2)
- `defpackage/C11585Sfi.java` (1)

```
org/chromium/net/HttpNegotiateAuthenticator.java:40:        c10690Qv.c = AccountManager.get(context);
org/chromium/net/HttpNegotiateAuthenticator.java:58:            ((AccountManager) c10690Qv.c).getAccountsByTypeAndFeatures(this.b, strArr, new C27308h0a(this, c10690Qv, i), new Handler(ThreadUtils.a().getLooper()));
defpackage/AbstractC56418zyn.java:115:            accountManager = AccountManager.get(context);
defpackage/AbstractC56418zyn.java:120:            return Boolean.valueOf(accountManager.getAccounts().length > 0);
defpackage/C11585Sfi.java:382:            AccountManager.get(snapResourcesContextWrapper).addAccountExplicitly(account, null, null);
defpackage/GA1.java:418:                AccountManager accountManager = AccountManager.get(applicationContext);
defpackage/GA1.java:419:                if (accountManager != null && (accounts = accountManager.getAccounts()) != null) {
```

### battery_state — 0 hits in 0 files


```
```

### screen_capture_detect — 221 hits in 122 files

- `com/snap/modules/share_upsell/UpsellType.java` (19)
- `defpackage/EnumC45220sg2.java` (12)
- `defpackage/EnumC45976tAa.java` (12)
- `defpackage/EnumC10442Qkf.java` (5)
- `com/snap/modules/foundation/ScreenCaptureType.java` (4)
- `com/snap/modules/commerce_blizzard_logging/CommerceActionType.java` (4)
- `com/snap/modules/media/MediaLibraryItemSubType.java` (4)
- `defpackage/EnumC8651Npd.java` (4)
- `com/snap/ad_format/AdTooltipSource.java` (4)
- `com/snap/ad_format/AdRequestAFECategory.java` (4)
- `defpackage/EnumC25132faj.java` (3)
- `defpackage/AbstractC10190Qac.java` (3)

```
defpackage/C18197b4d.java:281:                ((InterfaceC33797lE9) c24728fK1.t).h(EnumC29072i9d.SCREENSHOT, 1L);
defpackage/C18197b4d.java:298:                es5.a(UpsellType.class, UpsellType.SCREENSHOT_MEMORY);
defpackage/AbstractC9050Og.java:14:    public static /* bridge */ /* synthetic */ Activity.ScreenCaptureCallback b(Object obj) {
defpackage/AbstractC9050Og.java:15:        return (Activity.ScreenCaptureCallback) obj;
defpackage/EnumC23921enk.java:52:    SCREENSHOT(41),
defpackage/EnumC29072i9d.java:293:    SCREENSHOT,
defpackage/Q1d.java:908:        c55828zb4E76.c("ENABLE_MEMORIES_SCREENSHOTS_TAB");
defpackage/Q1d.java:909:        I3 = new Q1d("ENABLE_SCREENSHOTS_MEMORY_TAB", 183, c55828zb4E76);
defpackage/Q1l.java:30:        Q1l q1l6 = new Q1l("SCREENSHOT", 5);
defpackage/Q1l.java:32:        Q1l q1l7 = new Q1l("SCREENSHOT_PLUS", 6);
defpackage/C9464Owc.java:14:        super("MAP_SCREENSHOT_CAPTURE", EnumC8630Nog.BUSINESS, 1.0d, 1.0d, 1.0d);
defpackage/G6b.java:12:    FRIEND_MADE_SCREENSHOT(7),
```

### audio_capture — 3 hits in 3 files

- `org/webrtc/audio/WebRtcAudioRecord.java` (1)
- `org/webrtc_v141/audio/WebRtcAudioRecord.java` (1)
- `defpackage/ZCi.java` (1)

```
org/webrtc/audio/WebRtcAudioRecord.java:150:        return new AudioRecord(i, i2, i3, i4, i5);
org/webrtc_v141/audio/WebRtcAudioRecord.java:150:        return new AudioRecord(i, i2, i3, i4, i5);
defpackage/ZCi.java:24:        return new AudioRecord(5, this.a, this.b, this.c, this.t);
```

### accessibility — 64 hits in 18 files

- `defpackage/EZ.java` (10)
- `defpackage/AbstractC36756n9m.java` (7)
- `defpackage/AbstractC46393tR7.java` (5)
- `defpackage/AbstractC24328f41.java` (5)
- `defpackage/PEc.java` (5)
- `androidx/recyclerview/widget/RecyclerView.java` (4)
- `defpackage/C40820po7.java` (3)
- `defpackage/ViewTreeObserverOnGlobalLayoutListenerC52708xZ.java` (3)
- `defpackage/ViewOnLongClickListenerC26943gll.java` (3)
- `defpackage/RunnableC7693Mc6.java` (3)
- `defpackage/C19720c41.java` (3)
- `defpackage/WHi.java` (3)

```
androidx/recyclerview/widget/RecyclerView.java:27:import android.view.accessibility.AccessibilityManager;
androidx/recyclerview/widget/RecyclerView.java:108:    public final AccessibilityManager H0;
androidx/recyclerview/widget/RecyclerView.java:1527:        AccessibilityManager accessibilityManager;
androidx/recyclerview/widget/RecyclerView.java:3015:        this.H0 = (AccessibilityManager) getContext().getSystemService("accessibility");
defpackage/AbstractC46393tR7.java:8:import android.view.accessibility.AccessibilityManager;
defpackage/AbstractC46393tR7.java:19:    public final AccessibilityManager Z;
defpackage/AbstractC46393tR7.java:32:        this.Z = (AccessibilityManager) view.getContext().getSystemService("accessibility");
defpackage/AbstractC46393tR7.java:159:        AccessibilityManager accessibilityManager = this.Z;
defpackage/AbstractC46393tR7.java:160:        if (!accessibilityManager.isEnabled() || !accessibilityManager.isTouchExplorationEnabled()) {
defpackage/C40820po7.java:11:import android.view.accessibility.AccessibilityManager;
defpackage/C40820po7.java:33:    public AccessibilityManager n;
defpackage/C40820po7.java:117:        this.n = (AccessibilityManager) context.getSystemService("accessibility");
```

### root_emulator — 13 hits in 9 files

- `com/snapchat/android/R.java` (5)
- `defpackage/C40820po7.java` (1)
- `defpackage/AbstractC26881gj9.java` (1)
- `defpackage/C1293Byh.java` (1)
- `defpackage/C22518dt3.java` (1)
- `defpackage/C37345nXm.java` (1)
- `defpackage/C51753ww7.java` (1)
- `defpackage/C37751no7.java` (1)
- `defpackage/C36215mo7.java` (1)

```
defpackage/C40820po7.java:93:        textInputLayout.m(textInputLayout.getResources().getText(R.string.exposed_dropdown_menu_content_description));
defpackage/AbstractC26881gj9.java:11:    public static final List b = Arrays.asList("${sunday}", "${monday}", "${tuesday}", "${wednesday}", "${thursday}", "${friday}", "${saturday}");
com/snapchat/android/R.java:23306:        public static final int exposed_dropdown_menu_content_description = 0x7f1318ac;
com/snapchat/android/R.java:24003:        public static final int friday_essential = 0x7f131b68;
com/snapchat/android/R.java:35421:        public static final int venue_api_friday = 0x7f13480d;
com/snapchat/android/R.java:35422:        public static final int venue_api_friday_short = 0x7f13480e;
com/snapchat/android/R.java:35502:        public static final int venue_editor_friday = 0x7f13485e;
defpackage/C1293Byh.java:222:        c49687vaj.c(null, "CREATE TABLE IF NOT EXISTS MobStoryMetadata (\n    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\n    storyRowId INTEGER NOT NULL,\n    creatorFriendRowId INTEGER, -- row id of mob story creator in Friend table\n    creatorUserId T [... omitt
defpackage/C22518dt3.java:45:                    throw new RuntimeException("EditText needs to be an AutoCompleteTextView if an Exposed Dropdown Menu is being used.");
defpackage/C37345nXm.java:185:            String[] strArr = {"/system/app/Superuser.apk", "/sbin/su", "/system/bin/su", "/system/xbin/su", "/data/local/xbin/su", "/data/local/bin/su", "/system/sd/xbin/su", "/system/bin/failsafe/su", "/data/local/su", "/su/bin/su"};
defpackage/C51753ww7.java:43:            if (!str2.contains("google_sdk") && !str2.contains("Emulator") && !str2.contains("Android SDK built for x86") && ((!Build.BRAND.startsWith("generic") || !Build.DEVICE.startsWith("generic")) && !"google_sdk".equals(Build.PRODUCT) && System.getProper [... omitt
defpackage/C37751no7.java:38:            throw new RuntimeException("EditText needs to be an AutoCompleteTextView if an Exposed Dropdown Menu is being used.");
```

### js_bridge — 15 hits in 11 files

- `com/razorpay/B$$W$.java` (3)
- `defpackage/LBa.java` (2)
- `defpackage/C49980vmf.java` (2)
- `org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java` (1)
- `com/snap/ads/attachments/core/instantpage/ComposerStaticWebView.java` (1)
- `com/snap/web/core/lib/webview/b.java` (1)
- `defpackage/C49963vlm.java` (1)
- `defpackage/C45405snf.java` (1)
- `defpackage/C32450kLm.java` (1)
- `defpackage/C40450pZ9.java` (1)
- `defpackage/M.java` (1)

```
org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java:34:        public void addJavascriptInterface(Object obj, String str, List<String> list) {
com/snap/ads/attachments/core/instantpage/ComposerStaticWebView.java:56:            this.webView.addJavascriptInterface(new H34(this), (String) it.next());
com/razorpay/B$$W$.java:499:        this.b.addJavascriptInterface(c15436Yg3, "CheckoutBridge");
com/razorpay/B$$W$.java:510:        webView3.addJavascriptInterface(c44970sVm, "MagicBridge");
com/razorpay/B$$W$.java:511:        this.c.addJavascriptInterface(new C15436Yg3(this.I, 2), "CheckoutBridge");
com/snap/web/core/lib/webview/b.java:103:                webView2.addJavascriptInterface(new ValdiWebView$ValdiWebViewMessageHandler(this, str2), str2);
defpackage/LBa.java:171:                webView.addJavascriptInterface(c44828sQ0, "AutofillJsBridge");
defpackage/LBa.java:172:                webView.addJavascriptInterface(c44828sQ0, "AndroidBridge");
defpackage/C49963vlm.java:211:            webView.addJavascriptInterface(new C33085klm(this), "AndroidBridge");
defpackage/C45405snf.java:46:        addJavascriptInterface(new C43871rnf(interfaceC42337qnf), "ScPlayableAd");
defpackage/C32450kLm.java:24:            webViewC.addJavascriptInterface(interfaceC33985lLm, interfaceC33985lLm.g());
defpackage/C40450pZ9.java:123:        webView3.addJavascriptInterface(new C37380nZ9(i, this, webView3, function1), "RenderBridge");
```

### boot_persist — 0 hits in 0 files


```
```

### full_screen_intent — 3 hits in 2 files

- `defpackage/AbstractC39476ovn.java` (2)
- `defpackage/C46967toj.java` (1)

```
defpackage/AbstractC39476ovn.java:99:            boolean z = inCallService.checkPermission("android.permission.USE_FULL_SCREEN_INTENT", Process.myUid(), Process.myUid()) == 0;
defpackage/AbstractC39476ovn.java:116:                builderAddPerson.setFullScreenIntent(pendingIntentB, false);
defpackage/C46967toj.java:1704:        ((Notification.Builder) this.c).setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.led [... omi
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 111 hits in 91 files

- `defpackage/C22518dt3.java` (3)
- `defpackage/C33372kxa.java` (3)
- `com/google/android/material/button/MaterialButton.java` (2)
- `com/snap/component/input/SnapPhoneNumberInputView.java` (2)
- `defpackage/C10471Qlj.java` (2)
- `com/snap/overlayrender/caption/ui/CaptionEditTextView.java` (2)
- `com/snap/identity/loginsignup/ui/pages/login/LoginFragment.java` (2)
- `com/snap/identity/ui/settings/passwordchange/InAppPasswordChangeFragment.java` (2)
- `com/snap/identity/ui/shared/phonenumber/PhonePickerViewV2.java` (2)
- `androidx/appcompat/widget/AppCompatTextView.java` (2)
- `defpackage/C29034i80.java` (2)
- `defpackage/C35881mam.java` (2)

```
com/cardinalcommerce/a/setLeft.java:89:    public final void addTextChangedListener(TextWatcher textWatcher) {
com/google/android/material/textfield/TextInputLayout.java:725:        this.I.addTextChangedListener(new C38264o8k(2, this));
com/google/android/material/button/MaterialButton.java:320:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
com/google/android/material/button/MaterialButton.java:321:        super.onTextChanged(charSequence, i, i2, i3);
com/google/android/material/timepicker/ChipTextInputComboView.java:85:        editText.addTextChangedListener(new a(this));
com/snap/security/cos/OTPView.java:222:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
com/snap/security/cos/TwoFAView.java:151:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
defpackage/D83.java:37:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
com/snap/payments/lib/paymentcore/PaymentsCardExpiryEditText.java:19:        addTextChangedListener(new C17588ag4(2, this));
com/snap/payments/lib/paymentcore/PaymentsCVVEditText.java:23:        addTextChangedListener(new C17588ag4(1, this));
com/snap/payments/lib/paymentcore/PaymentsCardNumberEditText.java:25:        addTextChangedListener(new C17588ag4(3, this));
com/snap/payments/lib/views/FloatLabelLayout.java:67:            this.a.addTextChangedListener(new C24529fC2(7, this));
```

### webview_tracking — 3 hits in 3 files

- `defpackage/C39680p41.java` (1)
- `defpackage/AbstractC29406iMm.java` (1)
- `defpackage/M.java` (1)

```
defpackage/C39680p41.java:52:                CookieManager.getInstance().setAcceptThirdPartyCookies(this, true);
defpackage/AbstractC29406iMm.java:32:            CookieManager.getInstance().setAcceptThirdPartyCookies(operaWebView, true);
defpackage/M.java:343:        CookieManager.getInstance().setAcceptThirdPartyCookies(webView, true);
```

### streaks — 1990 hits in 637 files

- `com/snapchat/android/R.java` (159)
- `defpackage/C1293Byh.java` (75)
- `defpackage/AbstractC19417brn.java` (28)
- `defpackage/C50610wBk.java` (26)
- `com/snap/modules/streak_restore/StreakRestoreSource.java` (20)
- `defpackage/C54476yic.java` (19)
- `defpackage/C3322Fe8.java` (18)
- `com/snapchat/client/messaging/Conversation.java` (17)
- `com/snap/plus/FeatureCatalog.java` (16)
- `com/snap/modules/streak_restore/StreakRestorePromoType.java` (14)
- `snap/snap_maps_sdk/nano/SnapMapsSdk.java` (13)
- `com/snap/modules/snap_editor_metrics/SnapEditorAdditionalParams.java` (13)

```
snap/snap_maps_sdk/nano/SnapMapsSdk.java:4762:        private int streakCount_;
snap/snap_maps_sdk/nano/SnapMapsSdk.java:4910:            this.streakCount_ = 0;
snap/snap_maps_sdk/nano/SnapMapsSdk.java:4938:        public FriendInfo clearStreakCount() {
snap/snap_maps_sdk/nano/SnapMapsSdk.java:4939:            this.streakCount_ = 0;
snap/snap_maps_sdk/nano/SnapMapsSdk.java:4948:                iComputeSerializedSize += C53657yB3.i(1, this.streakCount_);
snap/snap_maps_sdk/nano/SnapMapsSdk.java:4975:        public int getStreakCount() {
snap/snap_maps_sdk/nano/SnapMapsSdk.java:4976:            return this.streakCount_;
snap/snap_maps_sdk/nano/SnapMapsSdk.java:4991:        public boolean hasStreakCount() {
snap/snap_maps_sdk/nano/SnapMapsSdk.java:5013:        public FriendInfo setStreakCount(int i) {
snap/snap_maps_sdk/nano/SnapMapsSdk.java:5014:            this.streakCount_ = i;
snap/snap_maps_sdk/nano/SnapMapsSdk.java:5022:                c53657yB3.K(1, this.streakCount_);
snap/snap_maps_sdk/nano/SnapMapsSdk.java:5050:                        this.streakCount_ = c50593wB3.s();
```

### reengagement — 2791 hits in 1027 files

- `defpackage/C6308Jx6.java` (42)
- `defpackage/J74.java` (30)
- `defpackage/C4162Gmj.java` (24)
- `defpackage/RunnableC50829wKe.java` (21)
- `defpackage/BG2.java` (20)
- `defpackage/YW.java` (19)
- `defpackage/AbstractC51158wY5.java` (18)
- `defpackage/C55666zUb.java` (17)
- `defpackage/GHc.java` (16)
- `com/snapchat/android/R.java` (14)
- `defpackage/C5062Hy0.java` (14)
- `defpackage/BG8.java` (14)

```
app/aifactory/base/view/player/preview/LoadingSpinnerView.java:35:            float fElapsedRealtime = (((int) (SystemClock.elapsedRealtime() - this.o0)) / 1000.0f) * 360.0f;
app/aifactory/base/view/player/preview/LoadingSpinnerView.java:36:            canvas.drawArc(this.a, fElapsedRealtime + 90.0f, 180.0f, false, paint);
app/aifactory/base/view/player/preview/LoadingSpinnerView.java:37:            canvas.drawArc(this.b, 90.0f - fElapsedRealtime, -180L, false, paint);
org/webrtc/ThreadUtils.java:114:        long jElapsedRealtime = SystemClock.elapsedRealtime();
org/webrtc/ThreadUtils.java:116:        long jElapsedRealtime2 = j;
org/webrtc/ThreadUtils.java:117:        while (jElapsedRealtime2 > 0) {
org/webrtc/ThreadUtils.java:119:                thread.join(jElapsedRealtime2);
org/webrtc/ThreadUtils.java:122:                jElapsedRealtime2 = j - (SystemClock.elapsedRealtime() - jElapsedRealtime);
org/webrtc/ThreadUtils.java:133:        long jElapsedRealtime = SystemClock.elapsedRealtime();
org/webrtc/ThreadUtils.java:135:        long jElapsedRealtime2 = j;
org/webrtc/ThreadUtils.java:139:                zAwait = countDownLatch.await(jElapsedRealtime2, TimeUnit.MILLISECONDS);
org/webrtc/ThreadUtils.java:142:                jElapsedRealtime2 = j - (SystemClock.elapsedRealtime() - jElapsedRealtime);
```

### notif_permission_nag — 120 hits in 45 files

- `com/snapchat/android/R.java` (15)
- `com/snap/identity/loginsignup/ui/pages/contactsync/ContactSyncPrepromptFragment.java` (10)
- `defpackage/C24607fF5.java` (9)
- `defpackage/AKi.java` (6)
- `defpackage/C4656Hh4.java` (5)
- `defpackage/AbstractC30441j2n.java` (5)
- `defpackage/EnumC23587eaa.java` (4)
- `defpackage/U8c.java` (4)
- `defpackage/EnumC48994v8c.java` (4)
- `defpackage/CX0.java` (4)
- `defpackage/C17709al1.java` (3)
- `defpackage/C31961k28.java` (3)

```
defpackage/C17709al1.java:27:        this.s0 = ((LB6) gCh).a(A40.n(c34334laa, c34334laa, "BitmojiCreationPrePromptPresenter"));
defpackage/C17709al1.java:39:            B21.v2(this, c25539fr2.h(A40.n(c34334laa, c34334laa, "BitmojiCreationPrePromptPresenter"), null, true), this);
defpackage/C17709al1.java:44:            B21.v2(this, DFn.e(c25654fvh, new BB0(c34334laa2, "BitmojiCreationPrePromptPresenter")), this);
com/snap/identity/loginsignup/ui/pages/contactsync/ContactSyncPrepromptFragment.java:20:public final class ContactSyncPrepromptFragment extends LoginSignupFragment implements InterfaceC5288Ih4 {
com/snap/identity/loginsignup/ui/pages/contactsync/ContactSyncPrepromptFragment.java:82:            snapFontTextView.setText(getResources().getText(R.string.contact_sync_pre_prompt_dialog_title_v2));
com/snap/identity/loginsignup/ui/pages/contactsync/ContactSyncPrepromptFragment.java:83:            snapFontTextView2.setText(getResources().getText(R.string.contact_sync_pre_prompt_dialog_description_v2));
com/snap/identity/loginsignup/ui/pages/contactsync/ContactSyncPrepromptFragment.java:85:            snapFontTextView.setText(getResources().getText(R.string.contact_sync_pre_prompt_dialog_title_v3));
com/snap/identity/loginsignup/ui/pages/contactsync/ContactSyncPrepromptFragment.java:86:            snapFontTextView2.setText(getResources().getText(R.string.contact_sync_pre_prompt_dialog_description_v3));
com/snap/identity/loginsignup/ui/pages/contactsync/ContactSyncPrepromptFragment.java:88:            snapFontTextView.setText(getResources().getText(R.string.contact_sync_pre_prompt_dialog_title));
com/snap/identity/loginsignup/ui/pages/contactsync/ContactSyncPrepromptFragment.java:89:            snapFontTextView2.setText(getResources().getText(R.string.contact_sync_pre_prompt_dialog_description));
com/snap/identity/loginsignup/ui/pages/contactsync/ContactSyncPrepromptFragment.java:91:            snapFontTextView.setText(getResources().getText(R.string.contact_sync_pre_prompt_dialog_title_v4));
com/snap/identity/loginsignup/ui/pages/contactsync/ContactSyncPrepromptFragment.java:92:            snapFontTextView2.setText(getResources().getText(R.string.contact_sync_pre_prompt_dialog_description_v4));
```

### cancellation_retention — 1 hits in 1 files

- `defpackage/EnumC54703yrg.java` (1)

```
defpackage/EnumC54703yrg.java:31:        EnumC54703yrg enumC54703yrg3 = new EnumC54703yrg("CANCEL_FLOW", 2);
```

### urgency_countdown — 1205 hits in 267 files

- `com/snapchat/android/R.java` (74)
- `com/snap/modules/SCCCountdownShared/CountdownActionType.java` (56)
- `com/snap/modules/SCCCountdownShared/CountdownPageSource.java` (26)
- `defpackage/RunnableC10302Qf.java` (25)
- `com/snap/modules/countdown_in_chat/CountdownStatusType.java` (24)
- `defpackage/C34129lRl.java` (23)
- `com/snap/modules/SCCCountdownShared/CountdownStatusType.java` (20)
- `defpackage/C56119zmm.java` (17)
- `defpackage/C43407rUi.java` (15)
- `defpackage/C16791a9i.java` (14)
- `com/snap/modules/countdown_in_profile/CountdownProfileCellView.java` (12)
- `com/snap/modules/countdown/CountdownDetailsComponent.java` (12)

```
okhttp3/internal/publicsuffix/PublicSuffixDatabase.java:22:import java.util.concurrent.CountDownLatch;
okhttp3/internal/publicsuffix/PublicSuffixDatabase.java:31:    public final CountDownLatch b = new CountDownLatch(1);
okhttp3/internal/publicsuffix/PublicSuffixDatabase.java:185:            this.b.countDown();
io/reactivex/rxjava3/internal/subscribers/BlockingFirstSubscriber.java:14:        countDown();
io/reactivex/rxjava3/internal/subscribers/BlockingFirstSubscriber.java:22:            countDown();
io/reactivex/rxjava3/internal/subscribers/BlockingBaseSubscriber.java:6:import java.util.concurrent.CountDownLatch;
io/reactivex/rxjava3/internal/subscribers/BlockingBaseSubscriber.java:9:public abstract class BlockingBaseSubscriber<T> extends CountDownLatch implements FlowableSubscriber<T> {
io/reactivex/rxjava3/internal/subscribers/BlockingBaseSubscriber.java:20:        countDown();
io/reactivex/rxjava3/internal/observers/BlockingFirstObserver.java:10:        countDown();
io/reactivex/rxjava3/internal/observers/BlockingFirstObserver.java:18:            countDown();
com/amazon/identity/auth/device/endpoint/AbstractJSONTokenResponse.java:22:    public static final String EXPIRES_IN = "expires_in";
com/amazon/identity/auth/device/endpoint/AbstractJSONTokenResponse.java:39:    public static final String TOKEN_EXPIRES_IN = "token_expires_in";
```

### infinite_autoplay — 242 hits in 127 files

- `defpackage/AKi.java` (8)
- `com/snap/ads/api/AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState.java` (6)
- `com/snap/opera/events/ViewerEvents$AutoAdvanceRequested.java` (6)
- `defpackage/EnumC45220sg2.java` (6)
- `defpackage/C32366kId.java` (5)
- `defpackage/SGe.java` (5)
- `defpackage/K6m.java` (5)
- `defpackage/UKd.java` (5)
- `defpackage/C12034Sy7.java` (5)
- `defpackage/EnumC23921enk.java` (4)
- `com/snap/ad_common_api/AdInventoryType.java` (4)
- `defpackage/C10422Qjk.java` (4)

```
defpackage/C33802lEe.java:316:        sb.append(", blockAutoAdvance=");
defpackage/EnumC37278nV3.java:52:        p0 = new EnumC37278nV3[]{enumC37278nV3, enumC37278nV32, enumC37278nV33, enumC37278nV34, enumC37278nV35, enumC37278nV36, enumC37278nV37, enumC37278nV38, new EnumC37278nV3("COMPLIANCE_OVERRIDE_BITMOJI", 8, C22870e74.i(fv3)), new EnumC37278nV3("COMPLIANCE [... o
com/snap/ads/api/AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState.java:8:public final class AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState extends JJ7 {
com/snap/ads/api/AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState.java:12:    public AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState(SGe sGe, boolean z) {
com/snap/ads/api/AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState.java:26:        if (!(obj instanceof AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState)) {
com/snap/ads/api/AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState.java:29:        AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState adOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState = (AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState) obj;
com/snap/ads/api/AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState.java:30:        return this.b == adOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState.b && AbstractC26072gCa.i(this.c, adOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState.c);
com/snap/ads/api/AdOperaViewerEvents$UpdateAdPlaybackAutoAdvanceState.java:38:        return "UpdateAdPlaybackAutoAdvanceState(isEnabled=" + this.b + ", pageModel=" + this.c + ")";
defpackage/C50936wP.java:135:            iOd.N0 = "AUTOPLAY";
defpackage/TO0.java:37:        StringBuilder sb = new StringBuilder("AutoPlayTileConfig(enabled=");
defpackage/AbstractC16583a1a.java:71:    public static void setPlaybackAutoAdvance(IAdPageActionHandlers iAdPageActionHandlers, boolean z) {
defpackage/EnumC23921enk.java:43:    AUTO_ADVANCE_ITEM(32),
```

### badges — 24 hits in 17 files

- `me/leolin/shortcutbadger/impl/DefaultBadger.java` (3)
- `defpackage/C44099rwi.java` (2)
- `defpackage/C36222moe.java` (2)
- `defpackage/C45331ske.java` (2)
- `defpackage/C2847Eke.java` (2)
- `defpackage/C56037zje.java` (2)
- `me/leolin/shortcutbadger/impl/SonyHomeBadger.java` (1)
- `com/snapchat/client/messaging/PhoneNumber.java` (1)
- `defpackage/C1017Bn4.java` (1)
- `defpackage/PU8.java` (1)
- `defpackage/C31132jUm.java` (1)
- `defpackage/C19128bg8.java` (1)

```
me/leolin/shortcutbadger/impl/SonyHomeBadger.java:39:        contentValues.put("badge_count", Integer.valueOf(i));
me/leolin/shortcutbadger/impl/DefaultBadger.java:23:        intent.putExtra("badge_count", i);
me/leolin/shortcutbadger/impl/DefaultBadger.java:24:        intent.putExtra("badge_count_package_name", componentName.getPackageName());
me/leolin/shortcutbadger/impl/DefaultBadger.java:25:        intent.putExtra("badge_count_class_name", componentName.getClassName());
com/snapchat/client/messaging/PhoneNumber.java:17:    public void setNumber(String str) {
defpackage/C1017Bn4.java:24:            bundle.putInt("app_badge_count", i);
defpackage/PU8.java:169:            ((HashMap) map).put("feed_badge_count", l18);
defpackage/C31132jUm.java:23:        bundle.putInt("app_badge_count", i);
defpackage/C44099rwi.java:37:        Long l = (Long) map.get("badge_count");
defpackage/C44099rwi.java:77:            ((HashMap) map).put("badge_count", l);
defpackage/C19128bg8.java:146:            ((HashMap) map).put("feed_badge_count", l4);
defpackage/USm.java:20:        bundle.putInt("app_badge_count", i);
```

### minors_age — 255 hits in 84 files

- `defpackage/RUe.java` (20)
- `com/snapchat/android/R.java` (19)
- `defpackage/C21680dL.java` (13)
- `com/snap/modules/map_under_age_location_permission_tray/MapUnderAgeLocationPermissionTrayFeature.java` (13)
- `com/snap/modules/map_under_age_location_permission_tray/MapUnderAgeLocationPermissionTrayView.java` (11)
- `defpackage/C39403ot0.java` (10)
- `defpackage/AK.java` (9)
- `defpackage/C24489fAc.java` (8)
- `defpackage/C27560hAc.java` (7)
- `defpackage/C22953eAc.java` (7)
- `defpackage/EnumC17317aV3.java` (6)
- `com/looksery/sdk/LSCoreManagerWrapper.java` (5)

```
defpackage/C43829rlm.java:75:        c49963vlm.K2().l("underage", enumC41587qJ);
com/looksery/sdk/LSCoreManagerWrapper.java:287:    private native int nativeGetMemoryUsageEstimation(long j, String str);
com/looksery/sdk/LSCoreManagerWrapper.java:893:    public int getMemoryUsageEstimation() {
com/looksery/sdk/LSCoreManagerWrapper.java:894:        return getMemoryUsageEstimationFor(null);
com/looksery/sdk/LSCoreManagerWrapper.java:897:    public int getMemoryUsageEstimationFor(String str) {
com/looksery/sdk/LSCoreManagerWrapper.java:898:        return nativeGetMemoryUsageEstimation(getNativeHandle(), str);
com/looksery/sdk/MemoryUsageEstimationListener.java:4:public interface MemoryUsageEstimationListener {
defpackage/FK.java:42:        Collections.singletonList("AgeVerificationFailureTakeoverPresenter");
defpackage/FK.java:44:        this.u0 = ((LB6) gCh).a(new BB0(bv3, "AgeVerificationFailureTakeoverPresenter"));
defpackage/FK.java:63:        zk.w0 = RUe.AGE_VERIFICATION_ENTRY;
defpackage/FK.java:115:        zk.w0 = RUe.AGE_VERIFICATION_DECLARED_AGE_INELIGIBLE;
defpackage/FK.java:120:        c40926psdQ0.d("page_type", "AGE_VERIFICATION_DECLARED_AGE_INELIGIBLE");
```

### screen_time — 73 hits in 40 files

- `com/snapchat/android/R.java` (16)
- `defpackage/C3161Exj.java` (4)
- `defpackage/C50088vr.java` (2)
- `defpackage/C24828fO3.java` (2)
- `defpackage/TD3.java` (2)
- `defpackage/I93.java` (2)
- `defpackage/C37908nue.java` (2)
- `defpackage/Q48.java` (2)
- `defpackage/XM3.java` (2)
- `defpackage/HD3.java` (2)
- `defpackage/PC3.java` (2)
- `defpackage/C8470Ni1.java` (2)

```
com/snapchat/android/R.java:23603:        public static final int family_center_time_spent_camera = 0x7f1319d5;
com/snapchat/android/R.java:23604:        public static final int family_center_time_spent_fri = 0x7f1319d6;
com/snapchat/android/R.java:23605:        public static final int family_center_time_spent_map = 0x7f1319d7;
com/snapchat/android/R.java:23606:        public static final int family_center_time_spent_messaging = 0x7f1319d8;
com/snapchat/android/R.java:23607:        public static final int family_center_time_spent_mon = 0x7f1319d9;
com/snapchat/android/R.java:23608:        public static final int family_center_time_spent_none = 0x7f1319da;
com/snapchat/android/R.java:23609:        public static final int family_center_time_spent_sat = 0x7f1319db;
com/snapchat/android/R.java:23610:        public static final int family_center_time_spent_section_subtitle = 0x7f1319dc;
com/snapchat/android/R.java:23611:        public static final int family_center_time_spent_section_title = 0x7f1319dd;
com/snapchat/android/R.java:23612:        public static final int family_center_time_spent_spotlight_stories = 0x7f1319de;
com/snapchat/android/R.java:23613:        public static final int family_center_time_spent_sun = 0x7f1319df;
com/snapchat/android/R.java:23614:        public static final int family_center_time_spent_thu = 0x7f1319e0;
```

