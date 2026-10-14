# Pattern scan: work/whatsapp/jdex

## Code categories (library packages excluded)

### installed_apps — 120 hits in 92 files

- `classes5:X/C434383r.java` (6)
- `classes:X/C0Ff.java` (5)
- `classes:X/C14960l9.java` (4)
- `classes:com/google/android/gms/common/GooglePlayServicesUtil.java` (3)
- `classes:X/C01j.java` (3)
- `classes7:X/D3I.java` (3)
- `classes:X/AbstractC27781Mv.java` (2)
- `classes:X/C15930ml.java` (2)
- `classes11:X/AbstractC1221MTe.java` (2)
- `classes11:X/C3544NUs.java` (2)
- `classes4:X/AnonymousClass534.java` (2)
- `classes4:X/C56Z.java` (2)

```
classes:com/google/android/gms/common/GooglePlayServicesUtil.java:95:                packageInfo = packageManager.getPackageInfo("com.android.vending", 8256);
classes:com/google/android/gms/common/GooglePlayServicesUtil.java:104:            PackageInfo packageInfo2 = packageManager.getPackageInfo("com.google.android.gms", 64);
classes:com/google/android/gms/common/GooglePlayServicesUtil.java:171:                    PackageInfo packageInfo = C237913f.A00(context).A00.getPackageManager().getPackageInfo("com.google.android.gms", 64);
classes:com/whatsapp/home/ui/HomeActivity.java:4465:                        Signature[] signatureArr = homeActivity.getPackageManager().getPackageInfo("com.android.vending", 64).signatures;
classes:X/C15320lj.java:26:            PackageInfo packageInfo = this.A00.getPackageInfo("com.facebook.appmanager", 192);
classes:X/C14960l9.java:139:                    PackageInfo packageInfo = packageManager2.getPackageInfo("com.facebook.system", 4288);
classes:X/C14960l9.java:209:                    PackageInfo packageInfo2 = this.A04.A00.getPackageInfo("com.LogiaGroup.LogiaDeck", 4232);
classes:X/C14960l9.java:380:                            PackageInfo packageInfo = packageManager2.getPackageInfo("com.facebook.services", 192);
classes:X/C14960l9.java:431:                ProviderInfo[] providerInfoArr = packageManager.getPackageInfo("com.facebook.appmanager", 8).providers;
classes:X/AbstractC12660hM.java:169:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(intent, 0);
classes:X/AbstractC27781Mv.java:8988:                    applicationA003.getPackageManager().getPackageInfo("com.android.vending", 0);
classes:X/AbstractC27781Mv.java:36283:                                    List<ResolveInfo> listQueryIntentActivities = packageManager.queryIntentActivities(intent, 0);
```

### usage_stats — 9 hits in 3 files

- `classes:X/C0AF.java` (5)
- `classes7:X/C4127CoG.java` (2)
- `classes7:X/C4476Cu0.java` (2)

```
classes:X/C0AF.java:11:import android.app.usage.UsageStatsManager;
classes:X/C0AF.java:45:    public UsageStatsManager A08;
classes:X/C0AF.java:118:    public UsageStatsManager A08() {
classes:X/C0AF.java:119:        UsageStatsManager usageStatsManager = this.A08;
classes:X/C0AF.java:123:        UsageStatsManager usageStatsManager2 = (UsageStatsManager) C00I.A00().getSystemService("usagestats");
classes7:X/C4127CoG.java:5:import android.app.usage.UsageStatsManager;
classes7:X/C4127CoG.java:670:            UsageStatsManager usageStatsManagerA08 = r6.A08();
classes7:X/C4476Cu0.java:7:import android.app.usage.UsageStatsManager;
classes7:X/C4476Cu0.java:252:        UsageStatsManager usageStatsManagerA08 = this.A00.A08();
```

### clipboard — 8 hits in 7 files

- `classes11:com/whatsapp/mentions/ui/MentionableEntry.java` (2)
- `classes:X/C11630fb.java` (1)
- `classes4:X/C5MV.java` (1)
- `classes7:com/whatsapp/calling/ui/dialer/DialerActivity.java` (1)
- `classes7:X/ActionModeCallbackC3324CaT.java` (1)
- `classes8:com/whatsapp/ui/coreui/components/PhoneNumberEntry.java` (1)
- `classes8:X/ActionModeCallbackC3310EwP.java` (1)

```
classes:X/C11630fb.java:77:        ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
classes11:com/whatsapp/mentions/ui/MentionableEntry.java:596:        if (i == 16908322 && 1wa.A0d(this.A03).A15(AbstractC1439Mak.A00) && this.A0H != null && (r0 = this.A04) != null && (clipboardManagerA09 = r0.A09()) != null && (primaryClip = clipboardManagerA09.getPrimaryClip()) != null && primaryC
classes11:com/whatsapp/mentions/ui/MentionableEntry.java:621:                ClipData primaryClip2 = clipboardManagerA092.getPrimaryClip();
classes4:X/C5MV.java:19:        ClipData primaryClip = ((C5MU) obj).A00.A00.getPrimaryClip();
classes7:com/whatsapp/calling/ui/dialer/DialerActivity.java:350:        if (clipboardManagerA09 == null || (primaryClip = clipboardManagerA09.getPrimaryClip()) == null || primaryClip.getItemCount() == 0 || (itemAt = primaryClip.getItemAt(0)) == null || (text = itemAt.getText()) == null || (string = 
classes7:X/ActionModeCallbackC3324CaT.java:130:            z = clipboardManagerA09.hasPrimaryClip();
classes8:com/whatsapp/ui/coreui/components/PhoneNumberEntry.java:124:        if ((i == 16908322 || i == 16908337) && (clipboardManagerA09 = r5.A09()) != null && (primaryClip = clipboardManagerA09.getPrimaryClip()) != null && primaryClip.getItemCount() != 0) {
classes8:X/ActionModeCallbackC3310EwP.java:37:            if (clipboardManagerA09 != null && (primaryClip = clipboardManagerA09.getPrimaryClip()) != null) {
```

### contacts — 167 hits in 37 files

- `classes:X/C21240wy.java` (43)
- `classes6:com/whatsapp/contact/ui/picker/PhoneContactsSelector.java` (12)
- `classes6:X/C00858So.java` (9)
- `classes6:X/C8aB.java` (8)
- `classes9:X/HQG.java` (7)
- `classes6:X/C31099x0.java` (6)
- `classes6:X/A39.java` (5)
- `classes:X/C07870Ye.java` (4)
- `classes:X/C21140wo.java` (4)
- `classes2:X/C1fK.java` (4)
- `classes6:X/C00668Rs.java` (4)
- `classes6:X/AXR.java` (4)

```
classes:X/C07870Ye.java:8:import android.provider.ContactsContract;
classes:X/C07870Ye.java:73:                Uri uri = ContactsContract.Data.CONTENT_URI;
classes:X/C07870Ye.java:78:                            c0agA0O.AKi(ContentUris.withAppendedId(ContactsContract.RawContacts.CONTENT_URI, jLongValue), null, null);
classes:X/C07870Ye.java:91:                                c0agA0O.AKi(ContentUris.withAppendedId(ContactsContract.RawContacts.CONTENT_URI, jLongValue), null, null);
classes:X/C21240wy.java:17:import android.provider.ContactsContract;
classes:X/C21240wy.java:880:                                                Uri uriBuild = ContactsContract.RawContacts.CONTENT_URI.buildUpon().appendQueryParameter("account_name", accountA05.name).appendQueryParameter("account_type", accountA05.type).appendQueryParameter("caller_is_sync [... omitte
classes:X/C21240wy.java:881:                                                Uri uriBuild2 = ContactsContract.Data.CONTENT_URI.buildUpon().appendQueryParameter("caller_is_syncadapter", "true").build();
classes:X/C21240wy.java:973:                                                Uri uriBuild3 = ContactsContract.RawContacts.CONTENT_URI.buildUpon().appendQueryParameter("account_name", accountA05.name).appendQueryParameter("account_type", accountA05.type).appendQueryParameter("caller_is_syn [... omitte
classes:X/C21240wy.java:974:                                                Uri uriBuild4 = ContactsContract.Data.CONTENT_URI.buildUpon().appendQueryParameter("caller_is_syncadapter", "true").build();
classes:X/C21240wy.java:1054:                                                Uri uriBuild5 = ContactsContract.Data.CONTENT_URI.buildUpon().build();
classes:X/C21240wy.java:1115:                                                    Uri.Builder builderBuildUpon = ContactsContract.Data.CONTENT_URI.buildUpon();
classes:X/C21240wy.java:1251:                                                                Uri uriBuild6 = ContactsContract.Data.CONTENT_URI.buildUpon().appendQueryParameter("caller_is_syncadapter", "true").build();
```

### call_log — 2 hits in 2 files

- `classes9:com/whatsapp/registration/app/verifyphone/VerifyPhoneNumber.java` (1)
- `classes9:X/RunnableC5299I7g.java` (1)

```
classes9:com/whatsapp/registration/app/verifyphone/VerifyPhoneNumber.java:4429:                                        Uri uri = CallLog.Calls.CONTENT_URI;
classes9:X/RunnableC5299I7g.java:252:                    if (r9 == null || (cursorCL3 = r9.CL3(6CS.A0G(CallLog.Calls.CONTENT_URI.buildUpon().appendQueryParameter("limit", String.valueOf(5))), (String[]) null, "date >? ", 1wf.A1b(System.currentTimeMillis() - flk.A01), "date DESC ")) == null) {
```

### sms — 29 hits in 19 files

- `classes9:com/whatsapp/registration/app/verifyphone/VerifyPhoneNumber.java` (4)
- `classes9:X/HVI.java` (4)
- `classes9:com/whatsapp/registration/app/VerifyTwoFactorAuth.java` (2)
- `classes9:com/whatsapp/registration/app/phonenumberentry/RegisterPhone.java` (2)
- `classes9:com/whatsapp/registration/app/phonenumberentry/ChangeNumber.java` (2)
- `classes9:X/HJS.java` (2)
- `classes11:X/C5096NyI.java` (1)
- `classes4:X/C56Z.java` (1)
- `classes4:X/C27054y3.java` (1)
- `classes4:X/RunnableC40605g3.java` (1)
- `classes8:X/C4102FMk.java` (1)
- `classes8:X/FRC.java` (1)

```
classes11:X/C5096NyI.java:35:            cursorQuery = uVar.A00.getContentResolver().query(Uri.parse("content://sms/inbox"), new String[]{"_id", "address", "body", "date"}, String.format("date > ?", new Object[0]), new String[]{1wf.A0n(this.A00 - 2000, "")}, "date DESC");
classes4:X/C56Z.java:90:        String defaultSmsPackage = Telephony.Sms.getDefaultSmsPackage(context);
classes4:X/C27054y3.java:75:        String defaultSmsPackage = Telephony.Sms.getDefaultSmsPackage(context);
classes4:X/RunnableC40605g3.java:401:                    String defaultSmsPackage = Telephony.Sms.getDefaultSmsPackage(context);
classes8:X/C4102FMk.java:123:                Log.i("SmsRetrieverUtils/maybeUseSmsRetriever/onsuccess");
classes8:X/FRC.java:1291:                String defaultSmsPackage = Telephony.Sms.getDefaultSmsPackage((Context) this.A01);
classes9:com/whatsapp/registration/app/VerifyTwoFactorAuth.java:938:            Log.i("VerifyTwoFactorAuth/proceedWithoutSmsRetriever/requesting RECEIVE_SMS permission");
classes9:com/whatsapp/registration/app/VerifyTwoFactorAuth.java:941:            Log.i("VerifyTwoFactorAuth/proceedWithoutSmsRetriever/NOT requesting RECEIVE_SMS permission");
classes9:com/whatsapp/registration/app/verifyphone/VerifyPhoneNumber.java:1863:            Log.i("VerifyPhoneNumber/maybeUseSmsRetriever/useSmsRetriever already set");
classes9:com/whatsapp/registration/app/verifyphone/VerifyPhoneNumber.java:1866:            Log.i("VerifyPhoneNumber/maybeUseSmsRetriever");
classes9:com/whatsapp/registration/app/verifyphone/VerifyPhoneNumber.java:2203:            Log.i("VerifyPhoneNumber/launchVerifyPhoneNumberFor2faFallback/sms/maybeUseSmsRetriever");
classes9:com/whatsapp/registration/app/verifyphone/VerifyPhoneNumber.java:4894:        Log.i("VerifyPhoneNumber/requestSmsCode/maybeUseSmsRetriever");
```

### location — 25 hits in 9 files

- `classes:X/AbstractC27781Mv.java` (13)
- `classes10:X/AbstractC4021KiU.java` (2)
- `classes9:X/RunnableC5302I7j.java` (2)
- `classes9:X/HYP.java` (2)
- `classes9:X/AbstractC2945HAi.java` (2)
- `classes10:androidx/car/app/AppManager$1.java` (1)
- `classes7:X/C93.java` (1)
- `classes8:com/whatsapp/eventsv2/ui/location/EventLocationView.java` (1)
- `classes9:X/C4052HiJ.java` (1)

```
classes:X/AbstractC27781Mv.java:10948:                                    Log.w("FusedLocationManager/getLastKnownLocation/client not connected", e);
classes:X/AbstractC27781Mv.java:10956:                                        return locationManager.getLastKnownLocation(str2);
classes:X/AbstractC27781Mv.java:10958:                                    StringBuilder sb2 = new StringBuilder("FusedLocationManager/getLastKnownLocation/do not have location permissions context:");
classes:X/AbstractC27781Mv.java:10965:                                        return locationManager.getLastKnownLocation(str2);
classes:X/AbstractC27781Mv.java:10967:                                    StringBuilder sb22 = new StringBuilder("FusedLocationManager/getLastKnownLocation/do not have location permissions context:");
classes:X/AbstractC27781Mv.java:10973:                            StringBuilder sb222 = new StringBuilder("FusedLocationManager/getLastKnownLocation/do not have location permissions context:");
classes:X/AbstractC27781Mv.java:11087:                                        Log.w("FusedLocationManager/requestLocationUpdates/unable to request location updates", e);
classes:X/AbstractC27781Mv.java:11096:                                        Log.w("FusedLocationManager/requestLocationUpdates/do not have fine location permission");
classes:X/AbstractC27781Mv.java:11098:                                        this.A0A.requestLocationUpdates("gps", j, f, locationListener, Looper.getMainLooper());
classes:X/AbstractC27781Mv.java:11101:                                    Log.e("FusedLocationManager/requestLocationUpdates", e2);
classes:X/AbstractC27781Mv.java:11107:                                        Log.w("FusedLocationManager/requestLocationUpdates/do not have coarse location permission");
classes:X/AbstractC27781Mv.java:11109:                                        this.A0A.requestLocationUpdates("network", j, f, locationListener, Looper.getMainLooper());
```

### wifi_bt_scan — 11 hits in 7 files

- `classes11:X/C0067Lbn.java` (2)
- `classes7:X/C93.java` (2)
- `classes9:X/C3922HgB.java` (2)
- `classes9:X/H5R.java` (2)
- `classes12:ca/psiphon/PsiphonTunnel.java` (1)
- `classes9:com/whatsapp/consumer/messaging/CaptivePortalActivity.java` (1)
- `classes9:com/whatsapp/migration/transfer/network/connection/WifiDirectScannerConnectionHandler.java` (1)

```
classes11:X/C0067Lbn.java:104:            String bssid = connectionInfo.getBSSID();
classes11:X/C0067Lbn.java:108:            String ssid = connectionInfo.getSSID();
classes12:ca/psiphon/PsiphonTunnel.java:906:            String bssid = connectionInfo.getBSSID();
classes7:X/C93.java:269:                bssid = ((WifiManager) this.A00.getSystemService("wifi")).getConnectionInfo().getBSSID();
classes7:X/C93.java:275:                ssid = ((WifiManager) this.A00.getSystemService("wifi")).getConnectionInfo().getSSID();
classes9:com/whatsapp/consumer/messaging/CaptivePortalActivity.java:52:            String ssid = connectionInfo.getSSID();
classes9:com/whatsapp/migration/transfer/network/connection/WifiDirectScannerConnectionHandler.java:327:        if (!00i.areEqual((wifiManagerA0F == null || (connectionInfo = wifiManagerA0F.getConnectionInfo()) == null || (ssid = connectionInfo.getSSID()) == null) ? null : 0CF.A0E(ssid, "\"", "", fa
classes9:X/C3922HgB.java:42:            String ssid = wifiInfo != null ? wifiInfo.getSSID() : null;
classes9:X/C3922HgB.java:48:            if (!zIsConnected || wifiInfo == null || wifiInfo.getSSID() == null || !00i.areEqual(wifiInfo.getSSID(), this.A00.SSID)) {
classes9:X/H5R.java:82:            String bssid = connectionInfo.getBSSID();
classes9:X/H5R.java:86:                if (!1wd.A1S(04O.A01(00I.A00(), "android.permission.ACCESS_FINE_LOCATION")) || (wifiManagerA0F = AmZ.A0f(r2).A0F()) == null || (scanResults = wifiManagerA0F.getScanResults()) == null) {
```

### device_ids — 33 hits in 20 files

- `classes10:X/KY6.java` (5)
- `classes7:X/C93.java` (5)
- `classes11:androidx/core/widget/NestedScrollView.java` (3)
- `classes:X/C00L.java` (2)
- `classes4:androidx/compose/ui/platform/AndroidComposeView.java` (2)
- `classes9:com/whatsapp/waffle/accountlinking/mex/MexUnpauseWithoutFoaNonceApi.java` (2)
- `classes:X/C0L2.java` (1)
- `classes:X/C11310f4.java` (1)
- `classes:X/C11300f3.java` (1)
- `classes10:com/meta/wearable/acdc/sdk/auth/ConstellationAuthentication.java` (1)
- `classes10:X/L4N.java` (1)
- `classes10:X/KK2.java` (1)

```
classes:X/C0L2.java:1062:                        c09970cn.A0A.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
classes:X/C11310f4.java:225:        menu.setQwertyMode(KeyCharacterMap.load(keyEvent.getDeviceId()).getKeyboardType() != 1);
classes:X/C00L.java:573:        return Settings.Secure.getString(((C0AJ) c0ag).A00, "android_id");
classes:X/C00L.java:587:            boolean z2 = motionEvent.getDeviceId() == 0;
classes:X/C11300f3.java:296:        c12850hfA02.setQwertyMode(KeyCharacterMap.load(keyEvent.getDeviceId()).getKeyboardType() != 1);
classes10:com/meta/wearable/acdc/sdk/auth/ConstellationAuthentication.java:117:        ByteBuffer byteBufferAllocateDirect = ByteBuffer.allocateDirect(generatedMessageLiteBuild.getSerializedSize());
classes10:X/KY6.java:57:                    if (map.containsKey("android_id")) {
classes10:X/KY6.java:58:                        Object obj3 = map.get("android_id");
classes10:X/KY6.java:68:                    String strA00 = KIQ.A00(contentResolver, "android_id");
classes10:X/KY6.java:79:                            map.put("android_id", lValueOf2);
classes10:X/KY6.java:80:                            KIQ.A01.remove("android_id");
classes10:X/L4N.java:27:        Cursor cursorQuery = this.zza.A00.query(Uri.parse("content://com.google.android.gsf.gservices"), null, null, new String[]{"android_id"}, null);
```

### gsf_id — 5 hits in 3 files

- `classes10:X/KIQ.java` (2)
- `classes10:X/K8E.java` (2)
- `classes10:X/L4N.java` (1)

```
classes10:X/KIQ.java:14:    public static final Uri A07 = Uri.parse("content://com.google.android.gsf.gservices");
classes10:X/KIQ.java:15:    public static final Uri A08 = Uri.parse("content://com.google.android.gsf.gservices/prefix");
classes10:X/L4N.java:27:        Cursor cursorQuery = this.zza.A00.query(Uri.parse("content://com.google.android.gsf.gservices"), null, null, new String[]{"android_id"}, null);
classes10:X/K8E.java:12:    public static final Uri A02 = Uri.parse("content://com.google.android.gsf.gservices");
classes10:X/K8E.java:13:    public static final Uri A03 = Uri.parse("content://com.google.android.gsf.gservices/prefix");
```

### advertising_id — 17 hits in 6 files

- `classes9:X/C3283HOe.java` (5)
- `classes:X/AbstractC09900cd.java` (3)
- `classes9:X/C5416IBw.java` (3)
- `classes9:com/whatsapp/gapenforcement/managers/AccuracyMeasurementManager.java` (2)
- `classes9:X/H6Q.java` (2)
- `classes9:X/C5465IDt.java` (2)

```
classes:X/AbstractC09900cd.java:3:import com.whatsapp.gapenforcement.managers.AccuracyMeasurementManager;
classes:X/AbstractC09900cd.java:52:    public static final AccuracyMeasurementManager A0A() {
classes:X/AbstractC09900cd.java:53:        return new AccuracyMeasurementManager();
classes9:com/whatsapp/gapenforcement/managers/AccuracyMeasurementManager.java:38:public final class AccuracyMeasurementManager {
classes9:com/whatsapp/gapenforcement/managers/AccuracyMeasurementManager.java:84:                1wd.A0a(r1).A0e("GapEnforcement/AccuracyMeasurementManager/measureAccuracy", "Cannot evaluate rules", false, "No view port state before MM");
classes9:X/C5416IBw.java:6:import com.whatsapp.gapenforcement.managers.AccuracyMeasurementManager;
classes9:X/C5416IBw.java:72:                        AccuracyMeasurementManager accuracyMeasurementManager = (AccuracyMeasurementManager) 058.A02(rulesManager2.A01);
classes9:X/C5416IBw.java:75:                        if (accuracyMeasurementManager.A00(r3, c5229I4o, hf2, ie2) == r4) {
classes9:X/H6Q.java:39:                            1wj.A1C("GoogleAdIdManager/getAdvertisingIdInfo failed: ", e.getMessage(), e);
classes9:X/H6Q.java:44:                    1wj.A1C("GoogleAdIdManager/getTosRegion failed, treating as EU: ", e2.getMessage(), e2);
classes9:X/C5465IDt.java:3:import com.whatsapp.gapenforcement.managers.AccuracyMeasurementManager;
classes9:X/C5465IDt.java:52:                return ((AccuracyMeasurementManager) this.A0A).A00(null, null, null, this);
```

### install_referrer — 10 hits in 5 files

- `classes9:X/AbstractC3154HIp.java` (4)
- `classes9:X/HW0.java` (2)
- `classes9:X/RunnableC5318I7z.java` (2)
- `classes9:X/H6P.java` (1)
- `classes9:X/H1W.java` (1)

```
classes9:X/HW0.java:170:                            8PI.A1B(th, "/", 000.A08("AppManagerInstallReferrerUtils/getInstallReferrerFromAppManager/softReport ", "OxygenInstallSDK_UNEXPECTED_THREAD_EXCEPTION"));
classes9:X/HW0.java:179:            1wf.A1I(e.getStackTrace(), " ", 000.A08("AppManagerInstallReferrerUtils/getInstallReferrerFromAppManager/onError ", e.getMessage()));
classes9:X/AbstractC3154HIp.java:9:        if (Log.isLoggable("InstallReferrerClient", 2)) {
classes9:X/AbstractC3154HIp.java:10:            Log.v("InstallReferrerClient", str);
classes9:X/AbstractC3154HIp.java:15:        if (Log.isLoggable("InstallReferrerClient", 5)) {
classes9:X/AbstractC3154HIp.java:16:            Log.w("InstallReferrerClient", str);
classes9:X/H6P.java:42:        1wf.A1O("AppManagerInstallReferrerUtils/getInstallReferrerFromAppManager/onError ", str);
classes9:X/H1W.java:19:                8PI.A1B(th, "/", 000.A08("AppManagerInstallReferrerUtils/getInstallReferrerFromAppManager/softReport ", str));
classes9:X/RunnableC5318I7z.java:469:                        8PI.A1B(e6, "/", 000.A08("AppManagerInstallReferrerUtils/getInstallReferrerFromAppManager/softReport ", "OxygenInstallSDK_UNEXPECTED_STATE_EXCEPTION"));
classes9:X/RunnableC5318I7z.java:479:                        8PI.A1B(th, "/", 000.A08("AppManagerInstallReferrerUtils/getInstallReferrerFromAppManager/softReport ", "OxygenInstallSDK_UNEXPECTED_THREAD_EXCEPTION"));
```

### sensors — 0 hits in 0 files


```
```

### accounts — 5 hits in 3 files

- `classes9:X/FeN.java` (2)
- `classes9:X/IHD.java` (2)
- `classes9:X/C1114GPw.java` (1)

```
classes9:X/C1114GPw.java:19:        Account[] accounts = ((FeN) ((InterfaceC5652INt) this.A00.A05.get())).A00.getAccounts();
classes9:X/FeN.java:15:        Account[] accountsByType = this.A00.getAccountsByType(str);
classes9:X/FeN.java:21:        AccountManager accountManager = AccountManager.get(00I.A00());
classes9:X/IHD.java:900:                                                        Account[] accounts = ((FeN) ((InterfaceC5652INt) 058.A02(c0219Foj.A0U))).A00.getAccounts();
classes9:X/IHD.java:945:                                    Account[] accounts2 = ((FeN) ((InterfaceC5652INt) 058.A02(c0219Foj.A0U))).A00.getAccounts();
```

### battery_state — 0 hits in 0 files


```
```

### screen_capture_detect — 28 hits in 16 files

- `classes:X/C0LO.java` (5)
- `classes8:X/C2011EYj.java` (3)
- `classes4:X/C5FN.java` (2)
- `classes6:com/whatsapp/profile/ui/ViewProfilePhoto.java` (2)
- `classes6:com/whatsapp/contact/ui/quickcontact/QuickContactActivity.java` (2)
- `classes6:com/whatsapp/chatinfo/ContactInfoActivity.java` (2)
- `classes9:com/whatsapp/status/playback/StatusPlaybackActivity.java` (2)
- `classes9:X/C3469HXc.java` (2)
- `classes10:X/C3492KVk.java` (1)
- `classes3:com/whatsapp/media/recentmediasuggestion/impl/MediaStoreRecentMediaProvider.java` (1)
- `classes4:X/AbstractC11724Xl.java` (1)
- `classes4:X/C4SS.java` (1)

```
classes:X/C0LO.java:1709:                return s == 6013 ? "IG_IAB_SCREENSHOT_STORY_SECOND_CARD_SCREENSHOT_LOAD" : "UNDEFINED_QPL_EVENT";
classes:X/C0LO.java:3086:                    return "IG4A_SCREENSHOT_CHECK_PATH_AND_REPORT";
classes:X/C0LO.java:3089:                    return "IG4A_SCREENSHOT_CONTENT_CHANGE";
classes:X/C0LO.java:3629:                return s == 1 ? "IG_BUG_REPORTER_MME_TAKE_SCREENSHOT_FAILURE" : "UNDEFINED_QPL_EVENT";
classes:X/C0LO.java:7041:                return s == 9565 ? "VR_DEVICE_CAPTURE_OCULUS_CAPTURE_SCREENSHOT" : "UNDEFINED_QPL_EVENT";
classes10:X/C3492KVk.java:124:                return "MEDIA_ACCURACY_SCREENSHOT_CAPTURER";
classes3:com/whatsapp/media/recentmediasuggestion/impl/MediaStoreRecentMediaProvider.java:88:        A08 = 06q.A05() ? Environment.DIRECTORY_SCREENSHOTS : "Screenshots";
classes4:X/AbstractC11724Xl.java:107:                return "WEARABLE_LAUNCHER_DISPLAY_HANDOFF_LATENCY_SCREENSHOT_IN_GALLERY";
classes4:X/C4SS.java:7:        return i != 1088 ? i != 3236 ? i != 3246 ? i != 3437 ? i != 3798 ? i != 4652 ? i != 10084 ? i != 10299 ? i != 10355 ? i != 10679 ? "UNDEFINED_QPL_EVENT" : "MSGR_PRIVACY_EXPERIENCES_IP_ADDRESS_PROTECTION_TOGGLE" : "MSGR_PRIVACY_EXPERIENCES_PRIVACY_CHECK [... omitted end
classes4:X/C4IS.java:39:                return "BUGREPORT_CAPTURE_SCREENSHOT";
classes4:X/C4Y3.java:59:                return "WEARABLE_SETTINGS_SETTINGS_SCREENSHOTS_PAGE_LOAD";
classes4:X/C5FN.java:10:public final class C5FN implements Activity.ScreenCaptureCallback {
```

### audio_capture — 221 hits in 53 files

- `classes7:X/DBd.java` (19)
- `classes7:X/C3707ChD.java` (17)
- `classes7:X/C4816Czv.java` (14)
- `classes7:com/whatsapp/calling/asr/OsSpeechRecognizer$downloadStatus$1.java` (13)
- `classes7:com/whatsapp/calling/asr/OsSpeechRecognizer$startRecognition$1.java` (12)
- `classes7:X/DC4.java` (10)
- `classes7:com/whatsapp/voicetranscription/engines/speechrecognizer/SpeechRecognizerLocaleSupportKt$queryRecognitionSupport$3$1.java` (9)
- `classes7:X/C3319CaO.java` (9)
- `classes7:X/C3320CaP.java` (8)
- `classes7:com/whatsapp/calling/asr/mlkit/MlKitSpeechRecognizer.java` (6)
- `classes7:com/whatsapp/conversation/composer/livedictation/OnDeviceLiveDictationEngine.java` (6)
- `classes7:X/D22.java` (6)

```
classes11:com/whatsapp/infra/media/audioRecording/AudioRecordFactory.java:16:        return new AudioRecord(i3, i, 16, 2, i2);
classes11:X/RunnableC4761Nsh.java:1508:                    AudioRecord audioRecord2 = new AudioRecord(5, 44100, 16, 2, c3249NHd2.A00);
classes11:X/C4854NuJ.java:18:            1we.A1Q(1Wh.A0P("voicetranscription/SpeechRecognizerTranscriptionEngine/callback watchdog triggered after ", this.A00), "ms; waiting for terminal callback");
classes12:X/QZC.java:144:                Log.e("SpeechRecognizer", "Failed to check SBG version code", e);
classes3:X/AnonymousClass352.java:62:        sbA0O.append(", isSpeechRecognizerMigrationCtaEnabled=");
classes3:X/AnonymousClass352.java:64:        sbA0O.append(", isSpeechRecognizerMigrationCtaAboveTranscript=");
classes7:com/whatsapp/speechrecognition/locale/SpeechRecognitionLocaleModelDownloader.java:24:import com.whatsapp.voicetranscription.engines.speechrecognizer.SpeechRecognizerLocaleSupport;
classes7:com/whatsapp/speechrecognition/locale/SpeechRecognitionLocaleModelDownloader.java:45:    public final Enum A00(0BQ r13, 07z r14, EnumC1580BkI enumC1580BkI, SpeechRecognizerLocaleSupport speechRecognizerLocaleSupport, 0ub r17, int i) {
classes7:com/whatsapp/calling/asr/OsSpeechRecognizer$downloadStatus$1.java:23:import android.speech.SpeechRecognizer;
classes7:com/whatsapp/calling/asr/OsSpeechRecognizer$downloadStatus$1.java:28:@DebugMetadata(c = "com.whatsapp.calling.asr.OsSpeechRecognizer$downloadStatus$1", f = "OsSpeechRecognizer.kt", i = {0, 0, 0, 0}, l = {213}, m = "invokeSuspend", n = {"$this$callbackFlow", "events", "supportRecognizerRef",
classes7:com/whatsapp/calling/asr/OsSpeechRecognizer$downloadStatus$1.java:30:public final class OsSpeechRecognizer$downloadStatus$1 extends 0uf implements 09c {
classes7:com/whatsapp/calling/asr/OsSpeechRecognizer$downloadStatus$1.java:39:    public OsSpeechRecognizer$downloadStatus$1(C3707ChD c3707ChD, 0ub r3) {
```

### accessibility — 210 hits in 55 files

- `classes4:androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java` (15)
- `classes4:androidx/compose/ui/platform/AndroidComposeView.java` (10)
- `classes11:com/whatsapp/calling/ui/views/SlideToAnswerView.java` (9)
- `classes11:com/google/android/material/textfield/MaterialAutoCompleteTextView.java` (9)
- `classes11:com/whatsapp/ui/wds/components/bottomsheet/WDSBottomSheetHandleView.java` (8)
- `classes:X/C11650fd.java` (6)
- `classes10:com/facebook/rendercore/text/RCTextView.java` (6)
- `classes10:com/facebook/litho/LithoView.java` (6)
- `classes11:X/LhR.java` (6)
- `classes:X/C0AF.java` (5)
- `classes10:X/AccessibilityManagerAccessibilityStateChangeListenerC3365KQc.java` (5)
- `classes10:X/IfC.java` (5)

```
classes:androidx/recyclerview/widget/RecyclerView.java:82:import android.view.accessibility.AccessibilityManager;
classes:androidx/recyclerview/widget/RecyclerView.java:163:    public final AccessibilityManager A0x;
classes:androidx/recyclerview/widget/RecyclerView.java:955:        this.A0x = (AccessibilityManager) getContext().getSystemService("accessibility");
classes:androidx/recyclerview/widget/RecyclerView.java:2372:        AccessibilityManager accessibilityManager;
classes:X/C0AF.java:31:import android.view.accessibility.AccessibilityManager;
classes:X/C0AF.java:59:    public AccessibilityManager A0M;
classes:X/C0AF.java:249:    public AccessibilityManager A0M() {
classes:X/C0AF.java:250:        AccessibilityManager accessibilityManager = this.A0M;
classes:X/C0AF.java:254:        AccessibilityManager accessibilityManager2 = (AccessibilityManager) C00I.A00().getSystemService("accessibility");
classes:X/C11650fd.java:6:import android.view.accessibility.AccessibilityManager;
classes:X/C11650fd.java:35:        AccessibilityManager accessibilityManagerA0M = c0af.A0M();
classes:X/C11650fd.java:232:        C000500i.A0D(systemService, "null cannot be cast to non-null type android.view.accessibility.AccessibilityManager");
```

### root_emulator — 14 hits in 11 files

- `classes:X/C00L.java` (2)
- `classes6:X/C10168xU.java` (2)
- `classes9:X/I51.java` (2)
- `classes:X/C0BR.java` (1)
- `classes11:X/BinderC0119Ldu.java` (1)
- `classes11:X/AbstractC2528Mto.java` (1)
- `classes12:X/AbstractC2026PVm.java` (1)
- `classes2:X/AbstractC04201od.java` (1)
- `classes7:X/C0027Aod.java` (1)
- `classes9:X/RunnableC5302I7j.java` (1)
- `classes9:X/C2863H6n.java` (1)

```
classes:X/C0BR.java:795:                C0BU.A00(this.A0U, "isRooted", sb);
classes:X/C00L.java:437:                    File file = new File("/system/bin/su");
classes:X/C00L.java:438:                    File file2 = new File("/system/xbin/su");
classes11:X/BinderC0119Ldu.java:252:            String[] strArr = {"/system/app/Superuser.apk", "/sbin/su", "/system/bin/su", "/system/xbin/su", "/data/local/xbin/su", "/data/local/bin/su", "/system/sd/xbin/su", "/system/bin/failsafe/su", "/data/local/su", "/su/bin/su"};
classes11:X/AbstractC2528Mto.java:47:            throw 3b6.A12("EditText needs to be an AutoCompleteTextView if an Exposed Dropdown Menu is being used.");
classes12:X/AbstractC2026PVm.java:22:        Pattern patternCompile3 = Pattern.compile(Fdu.A0e(patternCompile, "(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfff [.
classes2:X/AbstractC04201od.java:20:        Pattern patternCompile3 = Pattern.compile("(?:(?:(?:aaa|aarp|abb|abbott|abbvie|abc|able|abogado|abudhabi|academy|accenture|accountant|accountants|aco|actor|ads|adult|aeg|aero|aetna|afl|africa|agakhan|agency|aig|airbus|airforce|airtel|akdn|alibaba|alipa [..
classes6:X/C10168xU.java:21:        return "wam_username_exposed";
classes6:X/C10168xU.java:47:        sbA16.append("WamUsernameExposed {");
classes7:X/C0027Aod.java:84:        sbA08.append(" exposed=");
classes9:X/RunnableC5302I7j.java:742:                                                                Log.e("p2p/fpm/ImportHelper/processFpmManifestInfoExposed/failed to parse");
classes9:X/C2863H6n.java:13:        return (1wa.A03(r3).getBoolean("has_primary_been_exposed_to_sender_enabled", false) && 058.A00(this.A00).A12(13524)) ? EnumC1675Gi4.A03 : (1wa.A03(r3).getBoolean("has_primary_been_exposed_to_receiver_enabled", false) && 058.A00(this.A00).A12(13523)) ?  [... omitte
```

### js_bridge — 7 hits in 7 files

- `classes10:com/whatsapp/hatch/conversation/browser/HatchBrowserStreamActivity.java` (1)
- `classes10:X/IeK.java` (1)
- `classes10:X/JR4.java` (1)
- `classes10:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java` (1)
- `classes10:X/JR3.java` (1)
- `classes10:X/RunnableC4290Kng.java` (1)
- `classes10:X/LII.java` (1)

```
classes10:com/whatsapp/hatch/conversation/browser/HatchBrowserStreamActivity.java:356:            webView.addJavascriptInterface(new C2974K3q(browserSessionController, atomicInteger.get()), "AndroidVncBridge");
classes10:X/IeK.java:441:            ie3.addJavascriptInterface(value, "navigationPerformanceLoggerJavascriptInterface");
classes10:X/JR4.java:82:        webView.addJavascriptInterface(new C2660JvM(jr4), "YoutubeJsInterface");
classes10:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java:33:        public void addJavascriptInterface(Object obj, String str, List list) {
classes10:X/JR3.java:195:            webView.addJavascriptInterface(new C2659JvL(this), "TiktokJsInterface");
classes10:X/RunnableC4290Kng.java:122:                    keg.A01.addJavascriptInterface(c2666JvS, "iabjs_unified_bridge");
classes10:X/LII.java:48:            secureWebView.addJavascriptInterface(new C2662JvO(c0794IyM.A04), "AndroidBridge");
```

### boot_persist — 13 hits in 9 files

- `classes:X/C0AF.java` (4)
- `classes3:com/whatsapp/infra/systemreceivers/boot/BootReceiver.java` (2)
- `classes:X/AbstractC14720ki.java` (1)
- `classes:X/C15050lI.java` (1)
- `classes7:X/C0976BVb.java` (1)
- `classes9:com/whatsapp/infra/systemreceivers/appupdated/AppUpdatedReceiver.java` (1)
- `classes9:com/facebook/errorreporting/lacrima/detector/broadcast/InternalShutdownBootBroadcastReceiver.java` (1)
- `classes9:com/facebook/errorreporting/lacrima/detector/broadcast/SystemShutdownBootBroadcastReceiver.java` (1)
- `classes9:com/whatsapp/aura/main/LauncherIconUpdateReceiver.java` (1)

```
classes:X/AbstractC14720ki.java:8:    public static final Set A00 = AnonymousClass087.A0c(new String[]{"ACTION_DEFAULT_DATA_SUBSCRIPTION_CHANGED", "ACTION_DEFAULT_VOICE_SUBSCRIPTION_CHANGED", "ACTION_IDLE_MAINTENANCE_END", "ACTION_IDLE_MAINTENANCE_START", "ACTION_MANAGED_ROAMING_IND", "ACTION_ [... 
classes:X/C0AF.java:323:            public void setExactAndAllowWhileIdle(int i, long j, PendingIntent pendingIntent) {
classes:X/C0AF.java:327:                        this.A00.setExactAndAllowWhileIdle(i, (i2 * 10) + j, pendingIntent);
classes:X/C0AF.java:370:            public void setAlarmClock(AlarmManager.AlarmClockInfo alarmClockInfo, PendingIntent pendingIntent) {
classes:X/C0AF.java:371:                this.A00.setAlarmClock(alarmClockInfo, pendingIntent);
classes:X/C15050lI.java:42:        alarmManagerA04.setExactAndAllowWhileIdle(i, j, pendingIntent);
classes3:com/whatsapp/infra/systemreceivers/boot/BootReceiver.java:21:        if ("android.intent.action.BOOT_COMPLETED".equals(intent.getAction())) {
classes3:com/whatsapp/infra/systemreceivers/boot/BootReceiver.java:23:            if ("android.intent.action.BOOT_COMPLETED".equals(intent.getAction())) {
classes7:X/C0976BVb.java:44:                alarmManagerA04.setExactAndAllowWhileIdle(i, j, pendingIntent);
classes9:com/whatsapp/infra/systemreceivers/appupdated/AppUpdatedReceiver.java:18:        if (Amc.A1Q(intent, "android.intent.action.MY_PACKAGE_REPLACED")) {
classes9:com/facebook/errorreporting/lacrima/detector/broadcast/InternalShutdownBootBroadcastReceiver.java:17:        if (0e8.A00(action, "com.facebook.android.intent.action.BOOT_COMPLETED") || 0e8.A00(action, "com.instagram.android.intent.action.BOOT_COMPLETED")) {
classes9:com/facebook/errorreporting/lacrima/detector/broadcast/SystemShutdownBootBroadcastReceiver.java:16:        if (0e8.A00(intent.getAction(), "android.intent.action.BOOT_COMPLETED")) {
```

### full_screen_intent — 3 hits in 3 files

- `classes:X/C07790Xw.java` (1)
- `classes7:X/C3408Cbr.java` (1)
- `classes7:X/ViewOnClickListenerC3357Cb1.java` (1)

```
classes:X/C07790Xw.java:129:            return !AbstractC013306q.A05() || A02("android.permission.USE_FULL_SCREEN_INTENT") == 0;
classes7:X/C3408Cbr.java:44:        builderA00.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.ledARGB, notification.le [... omitte
classes7:X/ViewOnClickListenerC3357Cb1.java:371:                            Amb.A1K(new Intent("android.settings.MANAGE_APP_USE_FULL_SCREEN_INTENT", Uri.parse(000.A04("package:", callsHistoryFragment2.A19().getPackageName()))), callsHistoryFragment2, 1l2.A00().A0B());
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 326 hits in 211 files

- `classes8:com/whatsapp/payments/indiaupi/common/ui/IndiaUpiAddressFormActivity.java` (9)
- `classes4:X/C3tA.java` (7)
- `classes6:X/C9Mr.java` (5)
- `classes8:com/whatsapp/payments/brazilpay/ui/BrazilAddOrEditPixFragment.java` (4)
- `classes8:com/whatsapp/payments/indiaupi/ui/IndiaUpiDebitCardVerificationActivity.java` (4)
- `classes9:X/C3769Hdg.java` (4)
- `classes9:X/GYb.java` (4)
- `classes11:X/MHs.java` (3)
- `classes3:X/C2AD.java` (3)
- `classes3:X/C33P.java` (3)
- `classes4:X/C5GT.java` (3)
- `classes5:com/whatsapp/evolvedabout/ui/creation/AddTextStatusActivity.java` (3)

```
classes:com/whatsapp/emoji/search/EmojiSearchKeyboardContainer.java:199:                interceptingEditText.addTextChangedListener(new 6rK(viewFindViewById, this));
classes:X/C11400fE.java:485:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:X/C11400fE.java:486:        super.onTextChanged(charSequence, i, i2, i3);
classes10:com/whatsapp/questionreply/composer/ReplyComposerActivity.java:358:        wDSEditText.addTextChangedListener(new JQR(this, 2));
classes10:com/whatsapp/question/composer/MessageComposerBottomSheet.java:117:        wDSEditText.addTextChangedListener(new JQR(this, 0));
classes10:com/whatsapp/question/composer/QuestionComposerBottomSheet.java:155:        laG.addTextChangedListener(new JQR(this, 1));
classes10:com/whatsapp/ui/coreui/text/FinalBackspaceAwareEntry.java:97:        addTextChangedListener(new JQR(this, 3));
classes10:X/C3357KPu.java:145:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes10:X/C3356KPt.java:40:    public void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes10:X/C4569Ksr.java:1729:                                wDSTextInputEditText.addTextChangedListener(new C3356KPt(r7, k2u));
classes10:X/C3933Kgv.java:211:        editText.addTextChangedListener(c3357KPu);
classes10:X/JQK.java:35:                    textWatcher.onTextChanged(jqk, iMin, i, i);
```

### webview_tracking — 4 hits in 3 files

- `classes8:com/whatsapp/webview/ui/WebViewWrapperView.java` (2)
- `classes10:X/JR3.java` (1)
- `classes10:X/Ie3.java` (1)

```
classes10:X/JR3.java:189:            CookieManager.getInstance().setAcceptThirdPartyCookies(webView, false);
classes10:X/Ie3.java:142:        CookieManager.getInstance().setAcceptThirdPartyCookies(this, z);
classes8:com/whatsapp/webview/ui/WebViewWrapperView.java:103:            cookieManager.setAcceptThirdPartyCookies(secureWebView, z);
classes8:com/whatsapp/webview/ui/WebViewWrapperView.java:114:            jx4A02.A00().setAcceptThirdPartyCookies(secureWebView, ev9CKj.A09);
```

### streaks — 28 hits in 11 files

- `classes:com/whatsapp/fieldstats/events/WamCall.java` (11)
- `classes:com/whatsapp/integrityai/modeldownload/IntegrityAiModelDownloadCoordinator.java` (4)
- `classes11:X/C3123NAo.java` (4)
- `classes7:X/C3075CNn.java` (2)
- `classes10:X/K05.java` (1)
- `classes12:X/AbstractC2822PqR.java` (1)
- `classes12:X/PV3.java` (1)
- `classes4:X/AbstractC09304Od.java` (1)
- `classes4:X/C37155aI.java` (1)
- `classes4:X/C3dJ.java` (1)
- `classes9:com/whatsapp/settings/ui/SettingsContactsActivity.java` (1)

```
classes:com/whatsapp/fieldstats/events/WamCall.java:2154:    public Long transportOvershootLongestStreakS;
classes:com/whatsapp/fieldstats/events/WamCall.java:2160:    public Double transportOvershootStreakAvgS;
classes:com/whatsapp/fieldstats/events/WamCall.java:8923:        map.put(708, this.transportOvershootLongestStreakS);
classes:com/whatsapp/fieldstats/events/WamCall.java:8929:        map.put(709, this.transportOvershootStreakAvgS);
classes:com/whatsapp/fieldstats/events/WamCall.java:11903:        map.put("transport_overshoot_longest_streak_s", this.transportOvershootLongestStreakS);
classes:com/whatsapp/fieldstats/events/WamCall.java:11909:        Double d3 = this.transportOvershootStreakAvgS;
classes:com/whatsapp/fieldstats/events/WamCall.java:11911:            map.put("transport_overshoot_streak_avg_s", d3);
classes:com/whatsapp/fieldstats/events/WamCall.java:12650:        map.put("transportOvershootLongestStreakS", this.transportOvershootLongestStreakS);
classes:com/whatsapp/fieldstats/events/WamCall.java:12656:        map.put("transportOvershootStreakAvgS", this.transportOvershootStreakAvgS);
classes:com/whatsapp/fieldstats/events/WamCall.java:15592:        C0BU.A00(this.transportOvershootLongestStreakS, "transportOvershootLongestStreakS", sb);
classes:com/whatsapp/fieldstats/events/WamCall.java:15598:        C0BU.A00(this.transportOvershootStreakAvgS, "transportOvershootStreakAvgS", sb);
classes:com/whatsapp/integrityai/modeldownload/IntegrityAiModelDownloadCoordinator.java:804:                                long jA04 = C0H8.A04(((SharedPreferences) interfaceC000800m.getValue()).getLong("model_download_failure_streak", 0L), 0L, 10L);
```

### reengagement — 2108 hits in 674 files

- `classes12:X/C3483QFr.java` (81)
- `classes:X/C21240wy.java` (77)
- `classes:X/C02160Ah.java` (20)
- `classes12:X/C4410QsE.java` (18)
- `classes12:X/OYW.java` (18)
- `classes:X/C233311j.java` (15)
- `classes12:X/QGG.java` (15)
- `classes12:X/C4407QsB.java` (15)
- `classes:com/whatsapp/status/updates/ui/UpdatesFragment.java` (14)
- `classes11:X/NWZ.java` (14)
- `classes11:X/NK9.java` (14)
- `classes11:X/C5159Nzh.java` (14)

```
classes:com/whatsapp/calling/voipcalling/VoipNativeImpl.java:147:        long jElapsedRealtime = SystemClock.elapsedRealtime();
classes:com/whatsapp/calling/voipcalling/VoipNativeImpl.java:151:        long jElapsedRealtime2 = SystemClock.elapsedRealtime();
classes:com/whatsapp/calling/voipcalling/VoipNativeImpl.java:155:        c16610nw.A00 = Long.valueOf(jElapsedRealtime2 - jElapsedRealtime);
classes:com/whatsapp/conversationslist/ConversationsFragmentKt.java:854:        long jElapsedRealtime = SystemClock.elapsedRealtime();
classes:com/whatsapp/conversationslist/ConversationsFragmentKt.java:855:        long j = jElapsedRealtime - this.A0q;
classes:com/whatsapp/conversationslist/ConversationsFragmentKt.java:864:        this.A0q = jElapsedRealtime;
classes:com/whatsapp/wamsys/JniBridge.java:227:                    c16610nw.A00 = Long.valueOf(SystemClock.elapsedRealtime() - c3p.A00);
classes:com/whatsapp/wamsys/JniBridge.java:1343:                    if (((C13120i6) interfaceC001300t4.get()).A0V(new Hvv((C0BQ) c016407y2.A04.get(), (C0AK) c016407y2.A00.get(), c016407y2.A06, (C09O) c016407y2.A05.get(), (JniBridge) c016407y2.A01.get(), SystemClock.elapsedRealtime()), c13560io3.A01(
classes:com/whatsapp/status/updates/ui/UpdatesFragment.java:789:        long jElapsedRealtime = SystemClock.elapsedRealtime();
classes:com/whatsapp/status/updates/ui/UpdatesFragment.java:791:        if (c26861Hf.A03 && (C26861Hf.A00(c26861Hf, jElapsedRealtime) || !c26861Hf.A03)) {
classes:com/whatsapp/status/updates/ui/UpdatesFragment.java:799:            bundle.putLong("prepared_crosspost_upsell_deeplink_action_at_elapsed_ms", l.longValue());
classes:com/whatsapp/status/updates/ui/UpdatesFragment.java:1185:            long jElapsedRealtime = SystemClock.elapsedRealtime();
```

### notif_permission_nag — 1 hits in 1 files

- `classes7:X/C3309CaA.java` (1)

```
classes7:X/C3309CaA.java:113:        StringBuilder sbA08 = 000.A08("PrivacyDisclosurePrompt(name=", str);
```

### cancellation_retention — 4 hits in 4 files

- `classes4:X/C4VH.java` (1)
- `classes4:X/C4ZJ.java` (1)
- `classes4:X/AbstractC07904It.java` (1)
- `classes4:X/AbstractC09674Po.java` (1)

```
classes4:X/C4VH.java:7:        return i != 6963 ? i != 8329 ? i != 9564 ? "UNDEFINED_QPL_EVENT" : "SELLER_OFFERS_CANCEL_OFFER" : "SELLER_OFFERS_EDIT_OFFER" : "SELLER_OFFERS_CREATE_OFFER";
classes4:X/C4ZJ.java:7:        return i != 2533 ? i != 5634 ? i != 11412 ? i != 16074 ? "UNDEFINED_QPL_EVENT" : "WORKPLACE_SHIFT_COVER_SHIFT_COVER_REVIEW_REQUEST_FLOW" : "WORKPLACE_SHIFT_COVER_SHIFT_COVER_CANCEL_OFFER_COVER_FLOW" : "WORKPLACE_SHIFT_COVER_SHIFT_COVER_ATTACHMENT_DELET [... omitted end
classes4:X/AbstractC07904It.java:40:                return "CHECKOUT_PURCHASE_EXPERIENCES_SAVE_OFFER";
classes4:X/AbstractC09674Po.java:73:                        return "INSTAGRAM_SHOPPING_SAVE_OFFER";
```

### urgency_countdown — 1302 hits in 299 files

- `classes8:com/whatsapp/conversation/ui/conversationrow/businessmessaging/limitedtimeoffer/LimitedTimeOfferView.java` (31)
- `classes:X/C03110Fm.java` (20)
- `classes8:com/whatsapp/conversation/ui/conversationrow/businessmessaging/interactive/InteractiveMessageView.java` (19)
- `classes:X/C1BT.java` (18)
- `classes5:X/C24577Pv.java` (16)
- `classes11:X/C3639NYo.java` (14)
- `classes9:X/RunnableC5302I7j.java` (14)
- `classes9:X/C4644Hrz.java` (14)
- `classes9:com/whatsapp/registration/app/VerifyTwoFactorAuth.java` (12)
- `classes9:X/HT3.java` (12)
- `classes9:X/C3452HWg.java` (11)
- `classes9:X/I6M.java` (11)

```
classes:com/whatsapp/accountswitching/AccountSwitchingContentProvider.java:63:import java.util.concurrent.CountDownLatch;
classes:com/whatsapp/accountswitching/AccountSwitchingContentProvider.java:407:                                            CountDownLatch countDownLatch = new CountDownLatch(1);
classes:com/whatsapp/accountswitching/AccountSwitchingContentProvider.java:408:                                            c016007u.A00.postDelayed(new I51(countDownLatch, 23), 100L);
classes:com/whatsapp/accountswitching/AccountSwitchingContentProvider.java:411:                                                countDownLatch.await(timeUnit.toMillis(1L), timeUnit);
classes:com/whatsapp/backup/google/restart/RestartAppContentProvider.java:15:import java.util.concurrent.CountDownLatch;
classes:com/whatsapp/backup/google/restart/RestartAppContentProvider.java:39:                        CountDownLatch countDownLatch = new CountDownLatch(1);
classes:com/whatsapp/backup/google/restart/RestartAppContentProvider.java:40:                        Executors.newSingleThreadExecutor().execute(new I7d(countDownLatch, 1));
classes:com/whatsapp/backup/google/restart/RestartAppContentProvider.java:41:                        countDownLatch.await(120L, TimeUnit.SECONDS);
classes:com/whatsapp/backup/google/restart/RestartAppContentProvider.java:50:                    CountDownLatch countDownLatch2 = new CountDownLatch(1);
classes:com/whatsapp/backup/google/restart/RestartAppContentProvider.java:51:                    Executors.newSingleThreadExecutor().execute(new I7n(this, str2, countDownLatch2, 7));
classes:com/whatsapp/backup/google/restart/RestartAppContentProvider.java:52:                    countDownLatch2.await(120L, TimeUnit.SECONDS);
classes:com/whatsapp/backup/google/restart/RestartAppContentProvider.java:65:            CountDownLatch countDownLatch3 = new CountDownLatch(1);
```

### infinite_autoplay — 79 hits in 42 files

- `classes4:X/AbstractC08444Kv.java` (22)
- `classes8:X/C0700Dny.java` (5)
- `classes8:X/C4098FMg.java` (4)
- `classes8:X/F69.java` (3)
- `classes8:X/C0797Dpa.java` (3)
- `classes8:X/EZJ.java` (3)
- `classes:com/whatsapp/home/ui/HomeActivity.java` (2)
- `classes10:X/JR3.java` (2)
- `classes3:com/whatsapp/conversation/delegate/ConversationDelegateImplJava.java` (2)
- `classes:X/C0LO.java` (1)
- `classes10:X/JR4.java` (1)
- `classes10:X/C1148JJk.java` (1)

```
classes:com/whatsapp/home/ui/HomeActivity.java:1804:        ((C0II) this).A08.A0Z().A01().putBoolean("is_last_video_autoplay_mute", true).apply();
classes:com/whatsapp/home/ui/HomeActivity.java:4419:            String stringExtra = intent.getStringExtra("autoplay_status_single_contact_jid");
classes:X/C0LO.java:7861:                    return "MARKETPLACE_VIDEO_AUTOPLAY_TRIGGERED";
classes10:X/JR4.java:117:            jSONObjectA1T.put("start", i2).put("rel", 0).put("modestbranding", 0).put("iv_load_policy", 3).put("autohide", 1).put("autoplay", 1).put("cc_load_policy", 1).put("playsinline", 1).put("controls", 0);
classes10:X/JR3.java:198:                String strA05 = 000.A05("?autoplay=1&controls=0&progress_bar=0&play_button=0&volume_control=0&fullscreen_button=0&music_info=0&description=0&rel=0&native_context_menu=0", 000.A08("https://www.tiktok.com/player/v1/", strA04));
classes10:X/JR3.java:200:                webView.loadDataWithBaseURL("https://whatsapp.com", 000.A05("' allow='autoplay; fullscreen; encrypted-media' allowfullscreen></iframe><script>(function(){var f=document.getElementById('tt');function post(ev,d){try{TiktokJsInterface.postPlayerEv [... omitted e
classes10:X/C1148JJk.java:26:        return 1Wh.A0L(", key=", this.A00, 000.A08("EndlessReelsWidget(widgetData=", this.A01));
classes10:X/J0A.java:128:                                    5DT.A03("Bloks WebView media capture", "Enabled media autoplay (setMediaPlaybackRequiresUserGesture=false) for media capture session.");
classes10:X/KGj.java:231:                            if (strA0F7.equals("mks_endless_scroll")) {
classes11:X/C2748MxT.java:30:        StringBuilder sbA1N = 1wc.A1N("VideoPlayState(isAutoPlayAllowed=", z);
classes11:X/C2825Myl.java:45:        sbA0O.append(", autoplay=");
classes12:X/OG5.java:401:    public final boolean disable_preload_when_no_autoplay = false;
```

### badges — 29 hits in 15 files

- `classes12:com/google/protobuf/DescriptorProtos.java` (6)
- `classes7:X/CQF.java` (5)
- `classes:X/C1OB.java` (2)
- `classes12:com/google/protobuf/EnumValue.java` (2)
- `classes12:com/google/protobuf/Field.java` (2)
- `classes7:X/ArQ.java` (2)
- `classes7:X/D39.java` (2)
- `classes:X/C12470h3.java` (1)
- `classes10:X/C3918Kgg.java` (1)
- `classes10:X/C1192JMt.java` (1)
- `classes10:X/C4725KvZ.java` (1)
- `classes7:X/C3107CPe.java` (1)

```
classes:X/C12470h3.java:293:        editorEdit.putLong("badge_count", 0L);
classes:X/C1OB.java:40:        linkedHashMap.put("unread_badge_count", this.A02);
classes:X/C1OB.java:96:            List listSingletonList2 = Collections.singletonList("unread_badge_count");
classes10:X/C3918Kgg.java:32:        int iA01 = 1wg.A01(1wa.A03(this.A00.A01), "badge_count");
classes10:X/C1192JMt.java:30:                int iA0L = 3bA.A0L(KKO.A02("unfiltered_badge_count", jSONObject2));
classes10:X/C4725KvZ.java:77:        r2.A00("unfiltered_badge_count", false);
classes12:com/google/protobuf/EnumValue.java:104:        public Builder setNumber(int value) {
classes12:com/google/protobuf/EnumValue.java:227:    private void setNumber(int value) {
classes12:com/google/protobuf/DescriptorProtos.java:2667:            public Builder setNumber(int i) {
classes12:com/google/protobuf/DescriptorProtos.java:2668:                ((EnumValueDescriptorProto) 1wf.A0J(this)).setNumber(i);
classes12:com/google/protobuf/DescriptorProtos.java:2728:        public void setNumber(int i) {
classes12:com/google/protobuf/DescriptorProtos.java:3462:            public Builder setNumber(int i) {
```

### minors_age — 183 hits in 88 files

- `classes4:X/C45445op.java` (15)
- `classes4:com/whatsapp/managedaccount/product/SponsorOnboardingActivity.java` (12)
- `classes:X/AbstractC27781Mv.java` (10)
- `classes4:X/C41735hs.java` (6)
- `classes8:com/whatsapp/payments/brazilpay/ui/BrazilCopyPixBottomSheet.java` (6)
- `classes:X/HandlerC10940eS.java` (5)
- `classes4:com/whatsapp/ageverification/idv/AuthenticityActivity.java` (5)
- `classes4:X/C42345ir.java` (4)
- `classes4:X/C5Y7.java` (4)
- `classes8:X/C4112FMu.java` (4)
- `classes8:X/C3733F7x.java` (4)
- `classes4:com/whatsapp/managedaccount/deeplink/ManagedAccountSponsorOnboardingViewModel.java` (3)

```
classes:com/whatsapp/home/ui/HomeActivity.java:2554:                            StringBuilder sb9 = new StringBuilder("ManagedAccountSponsorOnboardingViewModel/requestAgeVerification: isSponsorAgeVerified=");
classes:X/C250718k.java:14:        ((SharedPreferences) this.A02.getValue()).edit().putBoolean("age_verification_status_fetched", true).apply();
classes:X/C250718k.java:102:        ((SharedPreferences) this.A02.getValue()).edit().putBoolean("app_store_age_underage_block", z).apply();
classes:X/C10850eI.java:235:                    C016608a.A00((C016608a) interfaceC001300t3.get()).putBoolean("underage_account_banned", false).apply();
classes:X/AbstractC27781Mv.java:24775:                                String str4 = iIntValue != 0 ? iIntValue != 1 ? iIntValue != 2 ? iIntValue != 3 ? iIntValue != 4 ? iIntValue != 7 ? UXLog.UNKNOWN : "cac_under13_block_remediable" : "cac_age_confirmation" : "cac_yob_confirmation" : "cac_monthday [
classes:X/AbstractC27781Mv.java:24817:                                        str2 = "cac_under13_blocked_remediatable_landing";
classes:X/AbstractC27781Mv.java:24844:                                        str2 = "cac_under13_blocked_remediatable_learn_more";
classes:X/AbstractC27781Mv.java:33843:                                } else if (str7.equals("age_verification_update") && this.A0O.A04() && this.A0C.A12(25237)) {
classes:X/AbstractC27781Mv.java:33845:                                    String str18 = "block_underage";
classes:X/AbstractC27781Mv.java:33846:                                    if ("block_underage".equals(strA0M11)) {
classes:X/AbstractC27781Mv.java:33847:                                        ((C00S) this.A08.get()).A04("com.whatsapp_br_payment_preferences").edit().putBoolean("pix_underage_restricted", true).apply();
classes:X/AbstractC27781Mv.java:33849:                                        str = "handleAgeVerificationUpdateBr/block_underage";
```

### screen_time — 146 hits in 56 files

- `classes:com/whatsapp/fieldstats/events/WamCall.java` (35)
- `classes:X/C05830Qf.java` (18)
- `classes12:X/POQ.java` (11)
- `classes9:X/HXY.java` (6)
- `classes7:com/whatsapp/calling/service/VoiceServiceEventCallback.java` (4)
- `classes8:com/whatsapp/payments/brazilpay/ui/BrazilCopyPixBottomSheet.java` (4)
- `classes8:com/whatsapp/inappsupport/ui/app/support/faq/SearchFAQActivity.java` (4)
- `classes:X/C0LO.java` (3)
- `classes4:X/AbstractC08864Ml.java` (3)
- `classes8:X/EW9.java` (3)
- `classes:X/C07240Vq.java` (2)
- `classes11:X/M8T.java` (2)

```
classes:com/whatsapp/fieldstats/events/WamCall.java:22:    public Long acceptedButNotConnectedTimeSpentMs;
classes:com/whatsapp/fieldstats/events/WamCall.java:72:    public Long androidTelecomTimeSpentBeforeReject;
classes:com/whatsapp/fieldstats/events/WamCall.java:2459:    public Long videoEncTimeSpentInNegative10Vp8Ms;
classes:com/whatsapp/fieldstats/events/WamCall.java:2460:    public Long videoEncTimeSpentInNegative12Vp8Ms;
classes:com/whatsapp/fieldstats/events/WamCall.java:2461:    public Long videoEncTimeSpentInNegative4Vp8Ms;
classes:com/whatsapp/fieldstats/events/WamCall.java:2462:    public Long videoEncTimeSpentInNegative6Vp8Ms;
classes:com/whatsapp/fieldstats/events/WamCall.java:2463:    public Long videoEncTimeSpentInNegative8Vp8Ms;
classes:com/whatsapp/fieldstats/events/WamCall.java:3177:        map.put("accepted_but_not_connected_time_spent_ms", this.acceptedButNotConnectedTimeSpentMs);
classes:com/whatsapp/fieldstats/events/WamCall.java:3230:        map.put("android_telecom_time_spent_before_reject", this.androidTelecomTimeSpentBeforeReject);
classes:com/whatsapp/fieldstats/events/WamCall.java:6780:        map.put(1015, this.acceptedButNotConnectedTimeSpentMs);
classes:com/whatsapp/fieldstats/events/WamCall.java:6830:        map.put(497, this.androidTelecomTimeSpentBeforeReject);
classes:com/whatsapp/fieldstats/events/WamCall.java:9228:        map.put(1019, this.videoEncTimeSpentInNegative10Vp8Ms);
```

## UI string categories (default locale)

### loss_aversion_copy — 29 strings

```
plurals.xml:170:        <item quantity="other">%1$d chats have a custom wallpaper or theme. This will be lost if overridden with list customizations.</item>
plurals.xml:171:        <item quantity="one">%1$d chat has a custom wallpaper or theme. This will be lost if overridden with list customizations.</item>
plurals.xml:3068:        <item quantity="other">Ongoing video call - Waiting for others… This call will end in %d minutes if no one joins.</item>
plurals.xml:3069:        <item quantity="one">Ongoing video call - Waiting for others… This call will end in %d minute if no one joins.</item>
plurals.xml:3120:        <item quantity="other">Ongoing voice chat - Waiting for others… This voice chat will end in %d minutes if no one joins.</item>
plurals.xml:3121:        <item quantity="one">Ongoing voice chat - Waiting for others… This voice chat will end in %d minute if no one joins.</item>
plurals.xml:3132:        <item quantity="other">Ongoing voice call - Waiting for others… This call will end in %d minutes if no one joins.</item>
plurals.xml:3133:        <item quantity="one">Ongoing voice call - Waiting for others… This call will end in %d minute if no one joins.</item>
strings.xml:344:    <string name="APKTOOL_DUMMYVAL_0x7f12015c">This payment won’t be completed and you’ll lose access to your existing payments information. If you restored your WhatsApp account, you can still access your payment history in your chats and Payments.</string> [... omitted end of long 
strings.xml:345:    <string name="APKTOOL_DUMMYVAL_0x7f12015d">You’ll lose access to your existing payments information and any payments in progress won’t be completed. If you restored your WhatsApp account, you can still access your payment history in your chats and Payments [... omitted end of lon
strings.xml:493:    <string name="APKTOOL_DUMMYVAL_0x7f1201ee">If you exit, you’ll lose any messages or other data that aren’t backed up for &lt;b>%s&lt;/b>.</string>
strings.xml:1477:    <string name="APKTOOL_DUMMYVAL_0x7f1205ce">Turn on cloud backups so you can restore your chats if you lose your device.</string>
strings.xml:1621:    <string name="APKTOOL_DUMMYVAL_0x7f12065e">"No new messages, photos, videos or other media will be backed up. If you lose your phone, you may have no way to access your chat history.
strings.xml:2581:    <string name="APKTOOL_DUMMYVAL_0x7f120a3c">Report issues like app freezes, crashes, or broken features.</string>
strings.xml:3440:    <string name="APKTOOL_DUMMYVAL_0x7f120d9e">"Your chats will no longer be backed up to the cloud, and you won't be able to restore them if you lose your device. Your existing backup is kept until you delete it."</string>
strings.xml:4972:    <string name="APKTOOL_DUMMYVAL_0x7f121390">"Repairing your chats. This won't take long…"</string>
strings.xml:4973:    <string name="APKTOOL_DUMMYVAL_0x7f121391">Repairing your chats</string>
strings.xml:5839:    <string name="APKTOOL_DUMMYVAL_0x7f1216f7">To protect your encrypted backups, you will need to create a password and use it when restoring your backups. Your encrypted backup cannot be restored if you lose your phone and forget the password.</string>
strings.xml:5846:    <string name="APKTOOL_DUMMYVAL_0x7f1216fe">Your backup will be safe, even if you lose your phone.</string>
strings.xml:5895:    <string name="APKTOOL_DUMMYVAL_0x7f121732">If you forget your password and lose your phone, WhatsApp cannot help you recover your backup.</string>
strings.xml:5907:    <string name="APKTOOL_DUMMYVAL_0x7f12173e">If you forget your key and lose your phone, WhatsApp cannot help you recover your backup.</string>
strings.xml:5912:    <string name="APKTOOL_DUMMYVAL_0x7f121743">Save your key. WhatsApp does not have a copy of it. If you forget your key and lose your phone, WhatsApp cannot help you recover your backup.</string>
strings.xml:11586:    <string name="APKTOOL_DUMMYVAL_0x7f122dbf">"You can still save contacts to your phone so you don't lose them."</string>
strings.xml:13930:    <string name="APKTOOL_DUMMYVAL_0x7f123707">&lt;b>%s&lt;/b> has been logged out of WhatsApp on this device. This might be because you registered it on another phone. If you remove the account from this device, you’ll lose any messages or other data that are [... omitted end of l
strings.xml:14764:    <string name="APKTOOL_DUMMYVAL_0x7f123a17">If you remove &lt;b>%s&lt;/b> from this device, you’ll lose any messages or other data that aren’t backed up.</string>
strings.xml:15899:    <string name="APKTOOL_DUMMYVAL_0x7f123e7c">Back up your chats and media safely to the cloud, in case you lose your phone. &lt;a href=\"%1$s\">Get started&lt;/a></string>
strings.xml:15932:    <string name="APKTOOL_DUMMYVAL_0x7f123e9e">"Back up your chats and media to the cloud so you don't lose them when you get a new Android phone."</string>
strings.xml:15957:    <string name="APKTOOL_DUMMYVAL_0x7f123eb7">"Your videos will no longer be backed up to cloud storage. If you lose your phone, you won't be able to get them back."</string>
strings.xml:20511:    <string name="APKTOOL_DUMMYVAL_0x7f125102">"If you stop now you'll lose any progress you've made."</string>
```

### urgency_copy — 82 strings

```
plurals.xml:1216:        <item quantity="other">Expires in %d days</item>
plurals.xml:1217:        <item quantity="one">Expires in %d day</item>
plurals.xml:1470:        <item quantity="other">%d minutes left</item>
plurals.xml:1471:        <item quantity="one">1 minute left</item>
plurals.xml:2020:        <item quantity="other">expires in %1$s</item>
plurals.xml:2021:        <item quantity="one">expires in %1$s</item>
plurals.xml:2116:        <item quantity="other">Ends in %1$d days</item>
plurals.xml:2117:        <item quantity="one">Ends in %1$d day</item>
plurals.xml:2120:        <item quantity="other">Ends in %1$dh</item>
plurals.xml:2121:        <item quantity="one">Ends in %1$dh</item>
plurals.xml:2228:        <item quantity="other">"Don't forget to join %1$s on WhatsApp! This invite expires in %2$d days. %3$s"</item>
plurals.xml:2229:        <item quantity="one">"Don't forget to join %1$s on WhatsApp! This invite expires in %2$d day. %3$s"</item>
plurals.xml:2236:        <item quantity="other">"Don't forget to join our community on WhatsApp! This invite expires in %1$d days. %2$s"</item>
plurals.xml:2237:        <item quantity="one">"Don't forget to join our community on WhatsApp! This invite expires in %1$d day. %2$s"</item>
plurals.xml:2240:        <item quantity="other">"Don't forget to join our community on WhatsApp, the world's most popular messaging app! This invite expires in %1$d days. %2$s"</item>
plurals.xml:2241:        <item quantity="one">"Don't forget to join our community on WhatsApp, the world's most popular messaging app! This invite expires in %1$d day. %2$s"</item>
plurals.xml:2248:        <item quantity="other">"Don't forget to join our group on WhatsApp! This invite expires in %1$d days. %2$s"</item>
plurals.xml:2249:        <item quantity="one">"Don't forget to join our group on WhatsApp! This invite expires in %1$d day. %2$s"</item>
plurals.xml:2252:        <item quantity="other">"Don't forget to join our group chat on WhatsApp, the world's most popular messaging app! This invite expires in %1$d days. %2$s"</item>
plurals.xml:2253:        <item quantity="one">"Don't forget to join our group chat on WhatsApp, the world's most popular messaging app! This invite expires in %1$d day. %2$s"</item>
plurals.xml:2364:        <item quantity="other">"You're invited to join a community on WhatsApp! It's the world's most popular messaging app. This invite expires in %1$d days. %2$s"</item>
plurals.xml:2365:        <item quantity="one">"You're invited to join a community on WhatsApp! It's the world's most popular messaging app. This invite expires in %1$d day. %2$s"</item>
plurals.xml:2372:        <item quantity="other">"You're invited to join a group chat on WhatsApp! It's the world's most popular messaging app. This invite expires in %1$d days. %2$s"</item>
plurals.xml:2373:        <item quantity="one">"You're invited to join a group chat on WhatsApp! It's the world's most popular messaging app. This invite expires in %1$d day. %2$s"</item>
plurals.xml:3016:        <item quantity="other">"Don't miss these updates"</item>
plurals.xml:3017:        <item quantity="one">"Don't miss this update"</item>
plurals.xml:3264:        <item quantity="other">Expires in %1$d hours</item>
plurals.xml:3265:        <item quantity="one">Expires in %1$d hour</item>
plurals.xml:3268:        <item quantity="other">Expires in %1$d minutes</item>
plurals.xml:3269:        <item quantity="one">Expires in %1$d minute</item>
strings.xml:1402:    <string name="APKTOOL_DUMMYVAL_0x7f120575">Expires %1$s</string>
strings.xml:3047:    <string name="APKTOOL_DUMMYVAL_0x7f120c0e">Chat with me on WhatsApp! You can download the app or chat as a guest. This invite expires soon. %1$s</string>
strings.xml:4999:    <string name="APKTOOL_DUMMYVAL_0x7f1213ac">"Chat with me on WhatsApp! Here's a link to join again - it expires soon. %s"</string>
strings.xml:6194:    <string name="APKTOOL_DUMMYVAL_0x7f12185d">%1$s (12+ hours left)</string>
strings.xml:6497:    <string name="APKTOOL_DUMMYVAL_0x7f121989">"Add the event to your calendar so you don't miss it."</string>
strings.xml:7757:    <string name="APKTOOL_DUMMYVAL_0x7f121e8a">Invite expires in %1$s</string>
strings.xml:8623:    <string name="APKTOOL_DUMMYVAL_0x7f122204">Let’s keep chatting on WhatsApp! Here’s a link to download the full app. This invite expires soon. %1$s</string>
strings.xml:8624:    <string name="APKTOOL_DUMMYVAL_0x7f122205">"Let's chat on WhatsApp! It's fast, simple, secure messaging and calling for free. This invite expires soon. %1$s"</string>
strings.xml:8625:    <string name="APKTOOL_DUMMYVAL_0x7f122206">Join me on WhatsApp! It lets us message privately and share photos, videos and more. This invite expires soon. %1$s</string>
strings.xml:8626:    <string name="APKTOOL_DUMMYVAL_0x7f122207">Chat with me on WhatsApp! It lets us message privately on iPhone, Android and more. This invite expires soon. %1$s</string>
strings.xml:8649:    <string name="APKTOOL_DUMMYVAL_0x7f12221e">Expires at %s</string>
strings.xml:8696:    <string name="APKTOOL_DUMMYVAL_0x7f122250">"Let's have a call on WhatsApp! It lets us make secure video and audio calls to any device. This invite expires soon. %1$s"</string>
strings.xml:8698:    <string name="APKTOOL_DUMMYVAL_0x7f122252">"Hey, let's hop on a group call! Here's a WhatsApp invite link — it expires soon. %1$s"</string>
strings.xml:8699:    <string name="APKTOOL_DUMMYVAL_0x7f122253">"Let's have a group call on WhatsApp! It's the world's most popular messaging app. This invite expires soon. %1$s"</string>
strings.xml:8700:    <string name="APKTOOL_DUMMYVAL_0x7f122254">"Let's have a group call on WhatsApp! It lets us make secure video and audio calls to any device. Invite expires soon. %1$s"</string>
strings.xml:8906:    <string name="APKTOOL_DUMMYVAL_0x7f122326">Ends in %1$s days</string>
strings.xml:8911:    <string name="APKTOOL_DUMMYVAL_0x7f12232b">Promotion ends in %1$s days</string>
strings.xml:11431:    <string name="APKTOOL_DUMMYVAL_0x7f122d23">This order expires on %1$s at %2$s.</string>
strings.xml:12700:    <string name="APKTOOL_DUMMYVAL_0x7f12323d">expires in less than 1 minute</string>
strings.xml:13444:    <string name="APKTOOL_DUMMYVAL_0x7f123521">Message may disappear before the pin expires.</string>
strings.xml:13885:    <string name="APKTOOL_DUMMYVAL_0x7f1236da">Ends in less than 1h</string>
strings.xml:14481:    <string name="APKTOOL_DUMMYVAL_0x7f12390e">"Don't miss the messages that matter."</string>
strings.xml:14657:    <string name="APKTOOL_DUMMYVAL_0x7f1239ac">"Don't forget to join our community %1$s on WhatsApp! This invite expires soon. %2$s"</string>
strings.xml:14660:    <string name="APKTOOL_DUMMYVAL_0x7f1239af">"Don't forget to join %1$s on WhatsApp! This invite expires soon. %2$s"</string>
strings.xml:14661:    <string name="APKTOOL_DUMMYVAL_0x7f1239b0">"Don't forget to join our group chat %1$s on WhatsApp! This invite expires soon. %2$s"</string>
strings.xml:14666:    <string name="APKTOOL_DUMMYVAL_0x7f1239b5">"Don't forget to join our community on WhatsApp! This invite expires soon. %1$s"</string>
strings.xml:14667:    <string name="APKTOOL_DUMMYVAL_0x7f1239b6">"Don't forget to join our community on WhatsApp! This invite expires soon. %1$s"</string>
strings.xml:14669:    <string name="APKTOOL_DUMMYVAL_0x7f1239b8">"Don't forget to join our community on WhatsApp, the world's most popular messaging app! This invite expires soon. %1$s"</string>
strings.xml:14670:    <string name="APKTOOL_DUMMYVAL_0x7f1239b9">"Don't forget to join our group on WhatsApp! This invite expires soon. %1$s"</string>
strings.xml:14671:    <string name="APKTOOL_DUMMYVAL_0x7f1239ba">"Don't forget to join our group chat on WhatsApp! This invite expires soon. %1$s"</string>
strings.xml:14673:    <string name="APKTOOL_DUMMYVAL_0x7f1239bc">"Don't forget to join our group chat on WhatsApp, the world's most popular messaging app! This invite expires soon. %1$s"</string>
strings.xml:15608:    <string name="APKTOOL_DUMMYVAL_0x7f123d56">Join community %1$s on WhatsApp! This invite expires soon. %2$s</string>
strings.xml:15609:    <string name="APKTOOL_DUMMYVAL_0x7f123d57">"Hey, join our community %1$s on WhatsApp! Here's an invite link — it expires soon. %2$s"</string>
strings.xml:15611:    <string name="APKTOOL_DUMMYVAL_0x7f123d59">Join community %1$s on WhatsApp! This invite expires in %2$d days. %3$s</string>
strings.xml:15640:    <string name="APKTOOL_DUMMYVAL_0x7f123d76">Join the group %1$s on WhatsApp! This invite expires soon. %2$s</string>
strings.xml:15641:    <string name="APKTOOL_DUMMYVAL_0x7f123d77">"Hey, join our group chat %1$s on WhatsApp! Here's an invite link — it expires soon. %2$s"</string>
strings.xml:15643:    <string name="APKTOOL_DUMMYVAL_0x7f123d79">Join the group %1$s on WhatsApp! This invite expires in %2$d days. %3$s</string>
strings.xml:15645:    <string name="APKTOOL_DUMMYVAL_0x7f123d7b">"You're invited to join a community on WhatsApp! This invite expires soon. %1$s"</string>
strings.xml:15646:    <string name="APKTOOL_DUMMYVAL_0x7f123d7c">"Hey, join our community on WhatsApp! Here's an invite link — it expires soon. %1$s"</string>
strings.xml:15648:    <string name="APKTOOL_DUMMYVAL_0x7f123d7e">"You're invited to join a community on WhatsApp! This invite expires in %1$d days. %2$s"</string>
strings.xml:15649:    <string name="APKTOOL_DUMMYVAL_0x7f123d7f">"You're invited to join a community on WhatsApp! It's the world's most popular messaging app. This invite expires soon. %1$s"</string>
strings.xml:15650:    <string name="APKTOOL_DUMMYVAL_0x7f123d80">"You're invited to join a group on WhatsApp! This invite expires soon. %1$s"</string>
strings.xml:15651:    <string name="APKTOOL_DUMMYVAL_0x7f123d81">"Hey, join our group chat on WhatsApp! Here's an invite link — it expires soon. %1$s"</string>
strings.xml:15653:    <string name="APKTOOL_DUMMYVAL_0x7f123d83">"You're invited to join a group on WhatsApp! This invite expires in %1$d days. %2$s"</string>
strings.xml:15654:    <string name="APKTOOL_DUMMYVAL_0x7f123d84">"You're invited to join a group chat on WhatsApp! It's the world's most popular messaging app. This invite expires soon. %1$s"</string>
strings.xml:18277:    <string name="APKTOOL_DUMMYVAL_0x7f124844">"%1$s's status expires soon."</string>
strings.xml:18432:    <string name="APKTOOL_DUMMYVAL_0x7f1248e0">Offer available for limited time. Promotional terms apply. &lt;a href=\"learn-more\">Learn more&lt;/a></string>
strings.xml:18433:    <string name="APKTOOL_DUMMYVAL_0x7f1248e1">Offer available for a limited time. &lt;a href=\"learn-more\">Learn more&lt;/a></string>
strings.xml:19487:    <string name="APKTOOL_DUMMYVAL_0x7f124d02">Voice chat ending soon</string>
strings.xml:20256:    <string name="APKTOOL_DUMMYVAL_0x7f125004">%1$s/month • Expires on %2$s</string>
strings.xml:21050:    <string name="APKTOOL_DUMMYVAL_0x7f125324">Expires in %1$dh %2$dm</string>
strings.xml:21051:    <string name="APKTOOL_DUMMYVAL_0x7f125325">Expires in under a minute</string>
```

### confirmshaming_copy — 4 strings

```
strings.xml:399:    <string name="APKTOOL_DUMMYVAL_0x7f120193">"If you didn't request this transfer, tap \"Not now.\" &lt;a href=\"%1$s\">Learn more about account safety&lt;/a>"</string>
strings.xml:17704:You can review and accept the WhatsApp update to chat with this business. Or view this message by tapping Not Now."</string>
strings.xml:19162:    <string name="APKTOOL_DUMMYVAL_0x7f124bb6">No thanks</string>
strings.xml:21520:    <string name="APKTOOL_DUMMYVAL_0x7f125517">Not now</string>
```

### social_pressure_copy — 49 strings

```
strings.xml:537:    <string name="APKTOOL_DUMMYVAL_0x7f12021a">"Share your role, title or how you're known in this group. Your tag can be seen by all group members and anyone who joins. &lt;a href=\"learn-more\">Learn more&lt;/a>"</string>
strings.xml:573:    <string name="APKTOOL_DUMMYVAL_0x7f12023e">Tap screenshot to edit or remove sensitive info</string>
strings.xml:1956:    <string name="APKTOOL_DUMMYVAL_0x7f1207b1">"Your location stays private. It can't be seen by businesses or WhatsApp. &lt;a href=learn-more>Learn more&lt;/a>"</string>
strings.xml:1957:    <string name="APKTOOL_DUMMYVAL_0x7f1207b2">"Your location stays private. It can't be seen by businesses or WhatsApp. &lt;a href=clear-search-location>Clear currently set location&lt;/a> or &lt;a href=learn-more>Learn more&lt;/a>"</string>
strings.xml:2558:    <string name="APKTOOL_DUMMYVAL_0x7f120a24">Include steps to reproduce, expected vs. actual behavior, and screenshots.</string>
strings.xml:2560:    <string name="APKTOOL_DUMMYVAL_0x7f120a26">Not bad! Add screenshots or recordings to help find root cause.</string>
strings.xml:2562:    <string name="APKTOOL_DUMMYVAL_0x7f120a28">Reports that lack detailed descriptions, screenshots, or recordings are more difficult to investigate.</string>
strings.xml:2565:    <string name="APKTOOL_DUMMYVAL_0x7f120a2b">Remove screenshot %1$d</string>
strings.xml:2566:    <string name="APKTOOL_DUMMYVAL_0x7f120a2c">Screenshot %1$d</string>
strings.xml:2568:    <string name="APKTOOL_DUMMYVAL_0x7f120a2e">Submit without failed screenshots?</string>
strings.xml:2569:    <string name="APKTOOL_DUMMYVAL_0x7f120a2f">Some screenshots are not added successfully. If you submit now, those screenshots will not be included.</string>
strings.xml:2571:    <string name="APKTOOL_DUMMYVAL_0x7f120a31">"Some screenshots couldn't be added. Tap to try again."</string>
strings.xml:2575:    <string name="APKTOOL_DUMMYVAL_0x7f120a36">Shaking your phone also adds a screenshot you can edit or remove.</string>
strings.xml:2582:    <string name="APKTOOL_DUMMYVAL_0x7f120a3d">Include details and screenshots to help us understand your feedback.</string>
strings.xml:4247:    <string name="APKTOOL_DUMMYVAL_0x7f1210c3">This business can see that you contacted them from find business. Your location stays private and is not seen by any businesses or WhatsApp.</string>
strings.xml:4701:    <string name="APKTOOL_DUMMYVAL_0x7f12127e">%s is typing…</string>
strings.xml:5261:    <string name="APKTOOL_DUMMYVAL_0x7f1214b6">Add screenshot</string>
strings.xml:5262:    <string name="APKTOOL_DUMMYVAL_0x7f1214b7">Add screenshot %1$d of %2$d</string>
strings.xml:5270:    <string name="APKTOOL_DUMMYVAL_0x7f1214bf">Remove screenshot %1$d</string>
strings.xml:5271:    <string name="APKTOOL_DUMMYVAL_0x7f1214c0">Screenshot %1$d</string>
strings.xml:5272:    <string name="APKTOOL_DUMMYVAL_0x7f1214c1">Add screenshots (optional)</string>
strings.xml:8992:    <string name="APKTOOL_DUMMYVAL_0x7f122377">Firefox (%s)</string>
strings.xml:9326:    <string name="APKTOOL_DUMMYVAL_0x7f1224c5">Screenshots (optional)</string>
strings.xml:9734:    <string name="APKTOOL_DUMMYVAL_0x7f122678">Seen by</string>
strings.xml:9735:    <string name="APKTOOL_DUMMYVAL_0x7f122679">Seen by</string>
strings.xml:10931:    <string name="APKTOOL_DUMMYVAL_0x7f122b2c">We have reviewed your report and determined this channel follows our &lt;a href=\"%s\">Channels Guidelines&lt;/a>.</string>
strings.xml:10944:    <string name="APKTOOL_DUMMYVAL_0x7f122b39">"We have reviewed your report and determined some updates on this channel don't follow our &lt;a href=\"%s\">Channels Guidelines&lt;/a>. WhatsApp requires all updates and channels to follow our Channels Guidelines [... omitted end of l
strings.xml:10957:    <string name="APKTOOL_DUMMYVAL_0x7f122b46">We have reviewed your report and determined this response follows our &lt;a href=\"%s\">Channels Guidelines&lt;/a>.</string>
strings.xml:10958:    <string name="APKTOOL_DUMMYVAL_0x7f122b47">We have reviewed your report and determined this response doesn’t follow our &lt;a href=\"%s\">Channels Guidelines&lt;/a>.</string>
strings.xml:10962:    <string name="APKTOOL_DUMMYVAL_0x7f122b4b">We have reviewed your report and determined this channel status follows our &lt;a href=\"%1$s\">Channels Guidelines&lt;/a>.</string>
strings.xml:10963:    <string name="APKTOOL_DUMMYVAL_0x7f122b4c">"We have reviewed your report and determined this channel status doesn't follow our &lt;a href=\"%1$s\">Channels Guidelines&lt;/a>. WhatsApp requires all updates and channels to follow our Channels Guidelines."</s [... omitted end of l
strings.xml:10967:    <string name="APKTOOL_DUMMYVAL_0x7f122b50">We have reviewed your report and determined this update follows our &lt;a href=\"%s\">Channels Guidelines&lt;/a>.</string>
strings.xml:10968:    <string name="APKTOOL_DUMMYVAL_0x7f122b51">"We have reviewed your report and determined this update doesn't follow our &lt;a href=\"%s\">Channels Guidelines&lt;/a>. WhatsApp requires all updates and channels to follow our Channels Guidelines."</string>
strings.xml:14263:    <string name="APKTOOL_DUMMYVAL_0x7f123830">Firefox</string>
strings.xml:14281:    <string name="APKTOOL_DUMMYVAL_0x7f123843">Include screenshots or recordings</string>
strings.xml:14327:    <string name="APKTOOL_DUMMYVAL_0x7f123871">Shaking your phone lets you report technical issues and captures a screenshot that you can edit or remove.</string>
strings.xml:14332:    <string name="APKTOOL_DUMMYVAL_0x7f123876">"Screenshot won't be added"</string>
strings.xml:14383:    <string name="APKTOOL_DUMMYVAL_0x7f1238ac">Recent activity on your account may not have followed the &lt;a href=\"%s\">WhatsApp Business Messaging Policy&lt;/a> on buying, selling, or promoting the exchange of firearms, ammunition, or weapons.</string>
strings.xml:15372:    <string name="APKTOOL_DUMMYVAL_0x7f123c6a">Screenshots</string>
strings.xml:15373:    <string name="APKTOOL_DUMMYVAL_0x7f123c6b">Screenshots or recordings (optional)</string>
strings.xml:17851:    <string name="APKTOOL_DUMMYVAL_0x7f124691">Only your answer will be shared with WhatsApp. The transcript is only seen by you and not shared.</string>
strings.xml:19369:    <string name="APKTOOL_DUMMYVAL_0x7f124c8e">For added privacy, the recipient can’t share, forward, copy, save, or take a screenshot of it.</string>
strings.xml:19374:    <string name="APKTOOL_DUMMYVAL_0x7f124c93">"Now when you send a view once message, the recipient can’t take a screenshot of it.
strings.xml:19378:    <string name="APKTOOL_DUMMYVAL_0x7f124c95">Also, you can’t share, forward, copy, save, or take a screenshot of it.</string>
strings.xml:19380:    <string name="APKTOOL_DUMMYVAL_0x7f124c97">For more privacy, your photo or video will disappear from the chat after the recipient opens it once. Remember, people can always take screenshots.</string>
strings.xml:19391:    <string name="APKTOOL_DUMMYVAL_0x7f124ca2">Also, you can’t share, forward, copy, save, or take a screenshot of it.</string>
strings.xml:19392:    <string name="APKTOOL_DUMMYVAL_0x7f124ca3">Also, you can’t share, forward, copy, save, or take a screenshot of it.</string>
strings.xml:20165:    <string name="APKTOOL_DUMMYVAL_0x7f124fa5">"We have reviewed your report and determined this ad doesn't follow our &lt;a href=\"learn-more\">Advertising Standards&lt;/a>."</string>
strings.xml:20166:    <string name="APKTOOL_DUMMYVAL_0x7f124fa6">We have reviewed your report and determined this ad follows our &lt;a href=\"learn-more\">Advertising Standards&lt;/a>.</string>
```

### guilt_copy — 250 strings

```
plurals.xml:190:        <item quantity="other">"Changing where your backup is stored doesn't change your encryption key. You'll use the same passkey, password or %1$d-digit key to restore."</item>
plurals.xml:191:        <item quantity="one">"Changing where your backup is stored doesn't change your encryption key. You'll use the same passkey, password or %1$d-digit key to restore."</item>
plurals.xml:698:        <item quantity="other">Use %1$d-digit encryption key instead</item>
plurals.xml:699:        <item quantity="one">Use %1$d-digit encryption key instead</item>
plurals.xml:702:        <item quantity="other">%d-digit encryption key</item>
plurals.xml:703:        <item quantity="one">%d-digit encryption key</item>
plurals.xml:710:        <item quantity="other">If you move to a new device, you can use your %d-digit encryption key to restore your chats.</item>
plurals.xml:711:        <item quantity="one">If you move to a new device, you can use your %d-digit encryption key to restore your chats.</item>
plurals.xml:714:        <item quantity="other">Your backup is protected with a %d-digit encryption-key</item>
plurals.xml:715:        <item quantity="one">Your backup is protected with a %d-digit encryption-key</item>
plurals.xml:722:        <item quantity="other">Did you save your full %d-digit encryption key?</item>
plurals.xml:723:        <item quantity="one">Did you save your full %d-digit encryption key?</item>
plurals.xml:742:        <item quantity="other">Your account is not associated with a password. Please enter your %d-digit encryption key instead.</item>
plurals.xml:743:        <item quantity="one">Your account is not associated with a password. Please enter your %d-digit encryption key instead.</item>
plurals.xml:746:        <item quantity="other">To restore your end-to-end encrypted backup, enter your %d-digit encryption key.</item>
plurals.xml:747:        <item quantity="one">To restore your end-to-end encrypted backup, enter your %d-digit encryption key.</item>
plurals.xml:750:        <item quantity="other">Use %d-digit encryption key instead</item>
plurals.xml:751:        <item quantity="one">Use %d-digit encryption key instead</item>
plurals.xml:754:        <item quantity="other">Enter the %d-digit key you use to protect your end-to-end encrypted backup.</item>
plurals.xml:755:        <item quantity="one">Enter the %d-digit key you use to protect your end-to-end encrypted backup.</item>
plurals.xml:758:        <item quantity="other">To begin, enter your %d-digit encryption key.</item>
plurals.xml:759:        <item quantity="one">To begin, enter your %d-digit encryption key.</item>
plurals.xml:762:        <item quantity="other">To turn off end-to-end encryption for your backup, enter your %d-digit encryption key.</item>
plurals.xml:763:        <item quantity="one">To turn off end-to-end encryption for your backup, enter your %d-digit encryption key.</item>
strings.xml:401:    <string name="APKTOOL_DUMMYVAL_0x7f120195">Transfer all your chats and media with the protection of end-to-end encryption. Just use your old phone to scan a QR code on this phone.</string>
strings.xml:433:    <string name="APKTOOL_DUMMYVAL_0x7f1201b2">Whether or not you turn on these restrictions, the messages and calls in this chat are protected with end-to-end encryption. The people in this chat are the only ones who can read, listen to, or choose to share th [... omitted end of lon
strings.xml:490:    <string name="APKTOOL_DUMMYVAL_0x7f1201eb">Your account details will be encrypted and stored securely. Update them anytime.</string>
strings.xml:509:    <string name="APKTOOL_DUMMYVAL_0x7f1201fe">Your CLABE will be encrypted and securely stored. Update it anytime.</string>
strings.xml:702:    <string name="APKTOOL_DUMMYVAL_0x7f1202b4">"Your personal messages, calls and statuses are &lt;a href=\"%1$s\">end-to-end encrypted&lt;/a> and can't be used to show you ads."</string>
strings.xml:1007:    <string name="APKTOOL_DUMMYVAL_0x7f1203e7">"Meta AI is an optional service from Meta that uses AI models to provide responses. Meta AI can only read messages people share with it. Meta can't read any other messages in your personal chats, as your personal  [... omitted end of lo
strings.xml:1008:    <string name="APKTOOL_DUMMYVAL_0x7f1203e8">"Meta AI is an optional service from Meta that uses AI models to provide responses. Meta AI can only read messages people share with it. Meta can't read any other messages in your personal chats, as your personal  [... omitted end of lo
strings.xml:1031:    <string name="APKTOOL_DUMMYVAL_0x7f1203fc">Other ways to verify encryption</string>
strings.xml:1457:    <string name="APKTOOL_DUMMYVAL_0x7f1205ba">Fix by confirming your end-to-end encryption method. &lt;a href=\"%1$s\">Fix now&lt;/a></string>
strings.xml:1466:    <string name="APKTOOL_DUMMYVAL_0x7f1205c3">Enter your encryption key to begin backup.</string>
strings.xml:1468:    <string name="APKTOOL_DUMMYVAL_0x7f1205c5">Enter your encryption password to begin backup.</string>
strings.xml:1481:    <string name="APKTOOL_DUMMYVAL_0x7f1205d2">Back up now, to protect your chats with your updated encryption method.</string>
strings.xml:1567:    <string name="APKTOOL_DUMMYVAL_0x7f120627">Encrypting your backup</string>
strings.xml:1617:    <string name="APKTOOL_DUMMYVAL_0x7f12065a">Your backup is still end-to-end encrypted</string>
strings.xml:1618:    <string name="APKTOOL_DUMMYVAL_0x7f12065b">"By continuing, you agree to WhatsApp's Storage &lt;a href=\"wa-storage-tos\">Terms of Service&lt;/a>. Your backup is &lt;a href=\"end-to-end-encrypted\">end-to-end encrypted&lt;/a> and subject to our &lt;a href=\ [... omitted end of lo
strings.xml:1619:    <string name="APKTOOL_DUMMYVAL_0x7f12065c">"By continuing, you agree to WhatsApp's Storage &lt;a href=\"wa-storage-tos\">Terms of Service&lt;/a>. Your backup is &lt;a href=\"end-to-end-encrypted\">end-to-end encrypted&lt;/a> and subject to our updated &lt; [... omitted end of lo
strings.xml:2275:    <string name="APKTOOL_DUMMYVAL_0x7f120903">"When you mention @Meta AI, the AI generates a response. Meta can't read or listen to the other messages and calls in this chat, because they are end-to-end encrypted."</string>
strings.xml:2276:    <string name="APKTOOL_DUMMYVAL_0x7f120904">"When you share with or mention @Meta AI, the AI generates a response. Meta can't read or listen to the other messages and calls in this chat, because they are end-to-end encrypted."</string>
strings.xml:2301:    <string name="APKTOOL_DUMMYVAL_0x7f12091e">"Only messages that mention or people share with @%s can be read by Meta. Meta can't read any other messages in this chat, as your personal messages remain end-to-end encrypted. 
strings.xml:2319:    <string name="APKTOOL_DUMMYVAL_0x7f12092e">"Meta may use your AI messages to improve AI quality. Personal messages are never sent to Meta, can't be read, and remain end-to-end encrypted."</string>
strings.xml:2320:    <string name="APKTOOL_DUMMYVAL_0x7f12092f">"Only the messages you send to AIs can be read by Meta. Meta can't read any other messages in your personal chats, as your personal messages remain end-to-end encrypted."</string>
strings.xml:2349:    <string name="APKTOOL_DUMMYVAL_0x7f12094d">By continuing, you acknowledge the privacy policies of &lt;a href=\"wa-privacy-policy\">WhatsApp Payments&lt;/a> and &lt;a href=\"fb-privacy-policy\">Meta&lt;/a> and accept the terms of &lt;a href=\"wa-tos\">Whats [... omitted end of lo
strings.xml:2350:    <string name="APKTOOL_DUMMYVAL_0x7f12094e">Your Pix key and name will be securely stored and encrypted.</string>
strings.xml:2597:End-to-end encryption keeps your personal calls between you and the people you choose. Not even WhatsApp can listen to them."</string>
strings.xml:2602:    <string name="APKTOOL_DUMMYVAL_0x7f120a4f">End-to-end encryption keeps your personal messages and calls between you and the people you choose. Not even WhatsApp can read or listen to them. This includes your:</string>
strings.xml:2603:    <string name="APKTOOL_DUMMYVAL_0x7f120a50">End-to-end encryption keeps your personal messages and calls between you and the people you choose. No one outside of the chat, not even WhatsApp, can read, listen to, or share them. This includes your:</string>
strings.xml:2606:    <string name="APKTOOL_DUMMYVAL_0x7f120a53">End-to-end encryption keeps your status updates and personal messages between you and the people you choose. Not even WhatsApp can see them. This includes your:</string>
strings.xml:3027:    <string name="APKTOOL_DUMMYVAL_0x7f120bfa">Your personal calls are &lt;a href=\"%s\">end-to-end encrypted&lt;/a></string>
strings.xml:3438:    <string name="APKTOOL_DUMMYVAL_0x7f120d9c">End-to-end encryption, cellular, include videos</string>
strings.xml:3448:    <string name="APKTOOL_DUMMYVAL_0x7f120da6">Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.</string>
strings.xml:3449:    <string name="APKTOOL_DUMMYVAL_0x7f120da7">Messages and calls are end-to-end encrypted. Only people in this chat can read, listen to, or share them. *Learn more*</string>
strings.xml:3523:    <string name="APKTOOL_DUMMYVAL_0x7f120df0">If you forgot your secret code, you can clear it. This will also unlock and clear messages, photos and videos in locked chats.</string>
strings.xml:4060:    <string name="APKTOOL_DUMMYVAL_0x7f121004">"This community is end-to-end encrypted. WhatsApp can't see or read messages from this community."</string>
strings.xml:4201:    <string name="APKTOOL_DUMMYVAL_0x7f121094">This message was secured with end-to-end encryption.</string>
strings.xml:4268:    <string name="APKTOOL_DUMMYVAL_0x7f1210d8">Encryption</string>
strings.xml:4334:    <string name="APKTOOL_DUMMYVAL_0x7f121118">Messages and calls are end-to-end encrypted. Tap to verify.</string>
strings.xml:4465:    <string name="APKTOOL_DUMMYVAL_0x7f1211a2">"We're experiencing technical difficulties. Please come back later."</string>
strings.xml:4476:    <string name="APKTOOL_DUMMYVAL_0x7f1211ad">By continuing, you allow WhatsApp Support to review technical information about your account to help answer your question. Messages from WhatsApp Support may be generated by AI using a secure technology from Meta. [... omitted end of lo
strings.xml:4704:    <string name="APKTOOL_DUMMYVAL_0x7f121281">Your personal messages are &lt;a href=\"%s\">end-to-end encrypted&lt;/a></string>
strings.xml:5068:    <string name="APKTOOL_DUMMYVAL_0x7f1213f3">You’ll be notified if your security code changes for a contact’s phone in an end-to-end encrypted chat.</string>
strings.xml:5251:    <string name="APKTOOL_DUMMYVAL_0x7f1214ac">Dismiss yourself as community admin?</string>
strings.xml:5252:    <string name="APKTOOL_DUMMYVAL_0x7f1214ad">"As the owner, you'll need to assign a new owner to dismiss yourself as an admin."</string>
strings.xml:5282:    <string name="APKTOOL_DUMMYVAL_0x7f1214cb">Some answers are generated by AI using a secure technology from Meta. WhatsApp uses your messages with WhatsApp Support to provide you with relevant answers. Your personal messages and calls remain end-to-end encr [... omitted end of lo
strings.xml:5502:    <string name="APKTOOL_DUMMYVAL_0x7f1215a1">Dismiss yourself as admin</string>
strings.xml:5503:    <string name="APKTOOL_DUMMYVAL_0x7f1215a2">"Couldn't dismiss yourself as admin. Please try again."</string>
strings.xml:5505:    <string name="APKTOOL_DUMMYVAL_0x7f1215a4">Dismiss yourself as channel admin?</string>
strings.xml:5839:    <string name="APKTOOL_DUMMYVAL_0x7f1216f7">To protect your encrypted backups, you will need to create a password and use it when restoring your backups. Your encrypted backup cannot be restored if you lose your phone and forget the password.</string>
strings.xml:5840:    <string name="APKTOOL_DUMMYVAL_0x7f1216f8">Secure your backup with end-to-end encryption</string>
strings.xml:5844:    <string name="APKTOOL_DUMMYVAL_0x7f1216fc">Turn on auto backup and end-to-end encryption. &lt;font color=#%1$s>Turn on&lt;/font></string>
strings.xml:5845:    <string name="APKTOOL_DUMMYVAL_0x7f1216fd">Encrypted backups are off</string>
strings.xml:5847:    <string name="APKTOOL_DUMMYVAL_0x7f1216ff">Secure your backup with a password or an encryption key.</string>
strings.xml:5848:    <string name="APKTOOL_DUMMYVAL_0x7f121700">Secure your backup with a passkey, password or an encryption key.</string>
strings.xml:5856:    <string name="APKTOOL_DUMMYVAL_0x7f121709">If you cancel now, your new end-to-end encrypted backup will be deleted.</string>
strings.xml:5861:    <string name="APKTOOL_DUMMYVAL_0x7f12170e">Your end-to-end encrypted backup will be replaced by a new backup that is not protected with end-to-end encryption. You can turn this setting back on at any time.</string>
strings.xml:5862:    <string name="APKTOOL_DUMMYVAL_0x7f12170f">Turn off end-to-end encryption for your backup?</string>
strings.xml:5864:    <string name="APKTOOL_DUMMYVAL_0x7f121711">Turn off end-to-end encryption for your backup?</string>
strings.xml:5871:    <string name="APKTOOL_DUMMYVAL_0x7f121718">"Your device doesn't support passkeys. Try a different option. &lt;a href=\"passkey-encrypted-backups-learn-more\">Learn more&lt;/a>"</string>
strings.xml:5872:    <string name="APKTOOL_DUMMYVAL_0x7f12171a">"Couldn't create passkey. Try again later, or choose a different option. &lt;a href=\"passkey-encrypted-backups-learn-more\">Learn more&lt;/a>"</string>
strings.xml:5873:    <string name="APKTOOL_DUMMYVAL_0x7f12171b">"Your password manager doesn't support passkey-encrypted backups. Try a different option. &lt;a href=\"passkey-encrypted-backups-learn-more\">Learn more&lt;/a>"</string>
strings.xml:5879:    <string name="APKTOOL_DUMMYVAL_0x7f121721">Your backup is no longer end-to-end encrypted</string>
strings.xml:5880:    <string name="APKTOOL_DUMMYVAL_0x7f121722">Your end-to-end encrypted backup will be replaced by a new backup that is not protected with end-to-end encryption.</string>
strings.xml:5883:    <string name="APKTOOL_DUMMYVAL_0x7f121726">The encryption process will complete in the background. It may take some time.</string>
strings.xml:5884:    <string name="APKTOOL_DUMMYVAL_0x7f121727">Create your end-to-end encrypted backup?</string>
strings.xml:5896:    <string name="APKTOOL_DUMMYVAL_0x7f121733">To protect your end-to-end encrypted backup, create a password. You will need this password to restore your backup.</string>
strings.xml:5903:    <string name="APKTOOL_DUMMYVAL_0x7f12173a">End-to-end encrypted backup is on</string>
strings.xml:5910:    <string name="APKTOOL_DUMMYVAL_0x7f121741">Instead of using a password, you can protect and restore your end-to-end encrypted backup with your encryption key:</string>
strings.xml:5911:    <string name="APKTOOL_DUMMYVAL_0x7f121742">Your encryption key</string>
strings.xml:5913:    <string name="APKTOOL_DUMMYVAL_0x7f121744">End-to-end encrypted</string>
strings.xml:5916:    <string name="APKTOOL_DUMMYVAL_0x7f121747">When you log back into your account, you must enter the password you created when you turned on end-to-end encrypted backup.</string>
strings.xml:5917:    <string name="APKTOOL_DUMMYVAL_0x7f121748">Incorrect encryption key. Try again.</string>
strings.xml:5923:    <string name="APKTOOL_DUMMYVAL_0x7f12174e">"WhatsApp can't find the passkey you used to encrypt your backup. Open your password manager and make sure your passkey is available, or try switching back to the password manager you used when creating your backu [... omitted end of lo
strings.xml:5924:    <string name="APKTOOL_DUMMYVAL_0x7f12174f">"WhatsApp can't find the passkey you used to encrypt your backup. Open %1$s and make sure your passkey is available. If you're using a different password manager, try switching back to %1$s to restore your backup. [... omitted end of lo
strings.xml:5930:    <string name="APKTOOL_DUMMYVAL_0x7f121755">"Your password manager doesn't support passkey-encrypted backups."</string>
strings.xml:5934:    <string name="APKTOOL_DUMMYVAL_0x7f121759">Your backup is end-to-end encrypted in your Google storage. No one, not even Google or WhatsApp, can access it.</string>
strings.xml:5935:    <string name="APKTOOL_DUMMYVAL_0x7f12175a">Your backup is end-to-end encrypted. No one, not even WhatsApp, can access it.</string>
strings.xml:5939:    <string name="APKTOOL_DUMMYVAL_0x7f12175e">You previously set up passkey-encrypted backups on your old phone. This lets you use your fingerprint, face or app lock to add protection to your chats.</string>
strings.xml:5940:    <string name="APKTOOL_DUMMYVAL_0x7f12175f">To continue encrypting your backup on this phone, use your passkey.</string>
strings.xml:5943:    <string name="APKTOOL_DUMMYVAL_0x7f121762">I lost my encryption key</string>
strings.xml:5945:    <string name="APKTOOL_DUMMYVAL_0x7f121764">Enter your encryption key</string>
strings.xml:5947:    <string name="APKTOOL_DUMMYVAL_0x7f121766">To restore your chats from encrypted backup on a new device, you will need your password or encryption key.</string>
strings.xml:5948:    <string name="APKTOOL_DUMMYVAL_0x7f121767">To restore your end-to-end encrypted backup, enter your password.</string>
strings.xml:5952:    <string name="APKTOOL_DUMMYVAL_0x7f12176b">"Your device doesn't support passkeys. Try a different option. &lt;a href=\"passkey-encrypted-backups-learn-more\">Learn more&lt;/a>"</string>
strings.xml:5953:    <string name="APKTOOL_DUMMYVAL_0x7f12176c">"Couldn't create backup. Try again later. &lt;a href=\"passkey-encrypted-backups-learn-more\">Learn more&lt;/a>"</string>
strings.xml:5954:    <string name="APKTOOL_DUMMYVAL_0x7f12176d">"Couldn't use passkey. Try again later, or choose a different option. &lt;a href=\"passkey-encrypted-backups-learn-more\">Learn more&lt;/a>"</string>
strings.xml:5955:    <string name="APKTOOL_DUMMYVAL_0x7f12176e">"WhatsApp can't find your passkey on this phone. Check your password manager, or replace your passkey with a new one. &lt;a href=\"passkey-encrypted-backups-learn-more\">Learn more&lt;/a>"</string>
strings.xml:5958:    <string name="APKTOOL_DUMMYVAL_0x7f121771">"Your password manager doesn't support passkey-encrypted backups. Try a different option. &lt;a href=\"passkey-encrypted-backups-learn-more\">Learn more&lt;/a>"</string>
strings.xml:5959:    <string name="APKTOOL_DUMMYVAL_0x7f121772">"Couldn't create backup. Check your internet connection and try again. &lt;a href=\"passkey-encrypted-backups-learn-more\">Learn more&lt;/a>"</string>
strings.xml:5960:    <string name="APKTOOL_DUMMYVAL_0x7f121773">I used an encryption key instead</string>
strings.xml:5964:    <string name="APKTOOL_DUMMYVAL_0x7f121777">This is the password you use to protect your end-to-end encrypted backup.</string>
strings.xml:5966:    <string name="APKTOOL_DUMMYVAL_0x7f121779">On occasion, you must enter the password you created when you turned on end-to-end encrypted backup. This helps secure your backup.</string>
strings.xml:5968:    <string name="APKTOOL_DUMMYVAL_0x7f12177b">Turn Off Encrypted Backups</string>
strings.xml:5973:    <string name="APKTOOL_DUMMYVAL_0x7f121780">To turn off end-to-end encryption for your backup, enter your password.</string>
strings.xml:5977:    <string name="APKTOOL_DUMMYVAL_0x7f121784">WhatsApp secures your conversations with end-to-end encryption. This means your messages, calls and statuses stay between you and the people you choose. Not even WhatsApp can read or listen to them.</string>
strings.xml:5978:    <string name="APKTOOL_DUMMYVAL_0x7f121785">Encryption is verified. Tap to view.</string>
strings.xml:5985:    <string name="APKTOOL_DUMMYVAL_0x7f12178c">End-to-end encrypted</string>
strings.xml:6549:    <string name="APKTOOL_DUMMYVAL_0x7f1219bd">Event details are visible to guests and WhatsApp. Your personal messages and calls remain end-to-end encrypted. &lt;a href=\"learn-more\">Learn more&lt;/a></string>
strings.xml:7097:Personal messages and calls remain end-to-end encrypted. No one else, not even WhatsApp or Meta, can read or listen to them."</string>
strings.xml:7285:    <string name="APKTOOL_DUMMYVAL_0x7f121cb0">Enter end-to-end encryption password to back up.</string>
strings.xml:7286:    <string name="APKTOOL_DUMMYVAL_0x7f121cb1">Enter end-to-end encryption key to back up.</string>
strings.xml:7287:    <string name="APKTOOL_DUMMYVAL_0x7f121cb2">Enter end-to-end encryption passkey to back up.</string>
strings.xml:7314:    <string name="APKTOOL_DUMMYVAL_0x7f121ccd">The encryption key you entered is incorrect.</string>
strings.xml:7401:    <string name="APKTOOL_DUMMYVAL_0x7f121d23">Messages and calls are now end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.</string>
strings.xml:7402:    <string name="APKTOOL_DUMMYVAL_0x7f121d24">Messages and calls are now end-to-end encrypted. Only people in this chat can read, listen to, or share them. Learn more.</string>
strings.xml:7471:    <string name="APKTOOL_DUMMYVAL_0x7f121d6a">"&lt;b>We can't read or listen to your personal conversations&lt;/b>, as they are end-to-end encrypted. This will never change."</string>
strings.xml:7495:    <string name="APKTOOL_DUMMYVAL_0x7f121d82">Messages are private and secured by end-to-end encryption.</string>
strings.xml:7678:    <string name="APKTOOL_DUMMYVAL_0x7f121e3b">Group history messages are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them.</string>
strings.xml:7721:    <string name="APKTOOL_DUMMYVAL_0x7f121e66">Messages and calls are end-to-end encrypted. Learn more</string>
strings.xml:8053:    <string name="APKTOOL_DUMMYVAL_0x7f121fac">"This group is end-to-end encrypted. WhatsApp can't see or read messages from this group."</string>
strings.xml:8226:    <string name="APKTOOL_DUMMYVAL_0x7f122060">This message was secured with end-to-end encryption.</string>
strings.xml:8252:    <string name="APKTOOL_DUMMYVAL_0x7f12207b">Use this code to verify the WhatsApp messages and calls between us are end-to-end encrypted:</string>
strings.xml:8363:    <string name="APKTOOL_DUMMYVAL_0x7f1220f4">"When you send a message to Meta AI, it's encrypted as it travels from your device to a confidential computing environment, where Meta and WhatsApp can't access it."</string>
strings.xml:8476:    <string name="APKTOOL_DUMMYVAL_0x7f122165">When you use WhatsApp with Ray-Ban Stories, the contents of your personal messages and calls are always secured with end-to-end encryption. Not even WhatsApp can read or listen to them.</string>
strings.xml:8477:    <string name="APKTOOL_DUMMYVAL_0x7f122166">When you use WhatsApp with your device, the contents of your personal messages and calls are always secured with end-to-end encryption. Not even WhatsApp can read or listen to them.</string>
strings.xml:8478:    <string name="APKTOOL_DUMMYVAL_0x7f122167">When you use WhatsApp with your watch, the contents of your personal messages and calls are always secured with end-to-end encryption. Not even WhatsApp can read or listen to them.</string>
strings.xml:8479:    <string name="APKTOOL_DUMMYVAL_0x7f122168">When you use WhatsApp with your glasses, the contents of your personal messages and calls are always secured with end-to-end encryption. Not even WhatsApp can read or listen to them.</string>
strings.xml:8507:    <string name="APKTOOL_DUMMYVAL_0x7f122185">Your personal calls and messages are always end-to-end encrypted &lt;a href=\"%1$s\">Learn more&lt;/a></string>
strings.xml:8537:    <string name="APKTOOL_DUMMYVAL_0x7f1221a3">Your messages are always end-to-end encrypted. Not even WhatsApp can read them.</string>
strings.xml:8543:    <string name="APKTOOL_DUMMYVAL_0x7f1221a9">"Scam Alert doesn't change end-to-end encryption. Your messages stay private, and WhatsApp can't read them."</string>
strings.xml:9325:    <string name="APKTOOL_DUMMYVAL_0x7f1224c4">By continuing, you allow WhatsApp to review technical information about your account to help answer your question. Messages from WhatsApp Support may be generated by AI using a secure technology from Meta. Your pe [... omitted end of lo
strings.xml:9376:    <string name="APKTOOL_DUMMYVAL_0x7f122501">Encrypted storage, extra pins, and more</string>
strings.xml:9442:    <string name="APKTOOL_DUMMYVAL_0x7f122555">Your personal messages and calls will continue to be end-to-end encrypted.</string>
strings.xml:9769:    <string name="APKTOOL_DUMMYVAL_0x7f12269b">End-to-end encryption keeps personal messages that you send to yourself private. Not even WhatsApp can read or listen to them. This includes your:</string>
strings.xml:9770:    <string name="APKTOOL_DUMMYVAL_0x7f12269c">End-to-end encryption keeps the personal messages that you send to yourself private. No one else, not even WhatsApp, can read, listen to, or share them. This includes your:</string>
strings.xml:9772:    <string name="APKTOOL_DUMMYVAL_0x7f12269e">Messages to yourself are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.</string>
strings.xml:9773:    <string name="APKTOOL_DUMMYVAL_0x7f12269f">Messages to yourself are end-to-end encrypted. No one else, not even WhatsApp, can read, listen to, or share them. *Learn more*</string>
strings.xml:9776:    <string name="APKTOOL_DUMMYVAL_0x7f1226a2">End-to-end encryption keeps personal messages that you send to yourself private. Not even WhatsApp can read or listen to them.</string>
strings.xml:9778:    <string name="APKTOOL_DUMMYVAL_0x7f1226a4">To verify that messages with yourself are end-to-end encrypted, scan or upload this code on your device. You can also compare the number above instead. &lt;a href=\"%1$s\"> Learn more&lt;/a></string>
strings.xml:9821:    <string name="APKTOOL_DUMMYVAL_0x7f1226d0">"To give you more relevant responses, Meta AI remembers details you choose to share in this chat. Meta may use these details to improve AI at Meta. You can delete them anytime. &lt;a href=\"learn-more\">Learn more [... omitted end of lo
strings.xml:10298:    <string name="APKTOOL_DUMMYVAL_0x7f1228b2">"Mute reminders about messages or statuses you haven't seen. This won't change your regular message or status notifications."</string>
strings.xml:10373:    <string name="APKTOOL_DUMMYVAL_0x7f1228fd">Your personal calls are always end-to-end encrypted.</string>
strings.xml:10406:    <string name="APKTOOL_DUMMYVAL_0x7f12291d">Dismiss yourself as admin</string>
strings.xml:10786:    <string name="APKTOOL_DUMMYVAL_0x7f122a9b">"Ownership transferred but couldn't dismiss yourself as admin."</string>
strings.xml:11027:    <string name="APKTOOL_DUMMYVAL_0x7f122b8c">"You'll remain an admin or choose to dismiss yourself"</string>
strings.xml:11167:    <string name="APKTOOL_DUMMYVAL_0x7f122c18">Welcome back to WhatsApp. Verify your account so you can start chatting.</string>
strings.xml:11168:    <string name="APKTOOL_DUMMYVAL_0x7f122c19">%s - Welcome back to WhatsApp. Verify your account so you can start chatting.</string>
strings.xml:11892:    <string name="APKTOOL_DUMMYVAL_0x7f122ef9">Your parent is now managing your account and can adjust some of your settings. Your messages are still end-to-end encrypted. No one, not even WhatsApp, can read them.</string>
strings.xml:11893:    <string name="APKTOOL_DUMMYVAL_0x7f122efa">Your parent is managing your new account and can adjust some of your settings. Your messages are end-to-end encrypted. No one, not even WhatsApp, can read them.</string>
strings.xml:13186:    <string name="APKTOOL_DUMMYVAL_0x7f12341d">To send a nearby place or your location, allow WhatsApp access to your location. WhatsApp protects your personal calls and messages with default end-to-end encryption.</string>
strings.xml:13350:    <string name="APKTOOL_DUMMYVAL_0x7f1234c3">Your personal calls are &lt;a href=\"%s\">end-to-end encrypted&lt;/a></string>
strings.xml:13352:    <string name="APKTOOL_DUMMYVAL_0x7f1234c5">Your personal messages are &lt;a href=\"%s\">end-to-end encrypted&lt;/a></string>
strings.xml:13353:    <string name="APKTOOL_DUMMYVAL_0x7f1234c6">Your personal messages are &lt;a href=\"%s\">end-to-end encrypted&lt;/a> on all your devices.</string>
strings.xml:13645:    <string name="APKTOOL_DUMMYVAL_0x7f1235ea">"Come back to %1$s's phone to finish setting up parental controls."</string>
strings.xml:13646:    <string name="APKTOOL_DUMMYVAL_0x7f1235eb">"Come back to your child's phone to finish setting up parental controls."</string>
strings.xml:13690:    <string name="APKTOOL_DUMMYVAL_0x7f123617">Your messages are still end-to-end encrypted. No one, not even WhatsApp, can read them.</string>
strings.xml:13755:    <string name="APKTOOL_DUMMYVAL_0x7f123659">Your messages are still end-to-end encrypted. No one, not even WhatsApp, can read them.</string>
strings.xml:14030:    <string name="APKTOOL_DUMMYVAL_0x7f12376a">Encrypt your backup so that nobody, not even Google or WhatsApp, will be able to access it.</string>
strings.xml:14031:    <string name="APKTOOL_DUMMYVAL_0x7f12376b">End-to-end encrypted backups</string>
strings.xml:14043:    <string name="APKTOOL_DUMMYVAL_0x7f123777">End-to-end encrypted</string>
strings.xml:14046:    <string name="APKTOOL_DUMMYVAL_0x7f12377a">Chats between only you and this business are managed by a secure service from Meta.&lt;br/>&lt;br/>For group chats, calls and statuses, this business is using the WhatsApp Business app. These communications remain [... omitted end of l
strings.xml:14047:    <string name="APKTOOL_DUMMYVAL_0x7f12377b">Chats between only your business and one other person are managed by a secure service from Meta.&lt;br/>&lt;br/>For group chats, calls and statuses, your business is using the WhatsApp Business app. These communic [... omitted end of l
strings.xml:14048:    <string name="APKTOOL_DUMMYVAL_0x7f12377c">Your business uses a secure service from Meta to manage messages and calls in this and other 1:1 chats.&lt;br/>&lt;br/>For group chats and statuses, your business is using the WhatsApp Business app. These communic [... omitted end of l
strings.xml:14076:    <string name="APKTOOL_DUMMYVAL_0x7f123785">This business has chosen to use multiple tools to chat with its customers.&lt;br/>&lt;br/>Chats between only you and this business are managed by a secure service from Meta.&lt;br/>&lt;br/>For group chats, calls a [... omitted end of l
strings.xml:14077:    <string name="APKTOOL_DUMMYVAL_0x7f123786">Your business has chosen to use multiple tools to chat with your customers.&lt;br/>&lt;br/>Chats between only your business and one other person are managed by a secure service from Meta.&lt;br/>&lt;br/>For group  [... omitted end of l
strings.xml:14078:    <string name="APKTOOL_DUMMYVAL_0x7f123787">"WhatsApp secures your conversations with end-to-end encryption.
strings.xml:14081:    <string name="APKTOOL_DUMMYVAL_0x7f123788">"WhatsApp secures your conversations with end-to-end encryption.
strings.xml:14097:    <string name="APKTOOL_DUMMYVAL_0x7f12378c">"Chats between only you and this business are managed by a secure service from Meta.&lt;br/>&lt;br/>For group chats and statuses, this business is using the WhatsApp Business app. These communications remain end-t [... omitted end of l
strings.xml:14098:    <string name="APKTOOL_DUMMYVAL_0x7f12378d">Chats between only your business and one other person are managed by a secure service from Meta.&lt;br/>&lt;br/>For group chats and statuses, your business is using the WhatsApp Business app. These communications  [... omitted end of l
strings.xml:14102:    <string name="APKTOOL_DUMMYVAL_0x7f123791">WhatsApp secures your conversations with end-to-end encryption.</string>
strings.xml:14249:    <string name="APKTOOL_DUMMYVAL_0x7f123820">To verify end-to-end encryption, scan the QR code on their device or ask them to scan your QR code.</string>
strings.xml:14255:    <string name="APKTOOL_DUMMYVAL_0x7f123827">"End-to-end encryption couldn't be verified"</string>
strings.xml:14256:    <string name="APKTOOL_DUMMYVAL_0x7f123829">End-to-end encryption is verified</string>
strings.xml:14702:    <string name="APKTOOL_DUMMYVAL_0x7f1239da">"You sent your payment successfully. We couldn't load the details right now due to a connection issue. Come back to this chat later or check on %1$s."</string>
strings.xml:15243:    <string name="APKTOOL_DUMMYVAL_0x7f123be9">Your messages stay private and end-to-end encrypted with Scam Alert turned on. Not even WhatsApp can read them.</string>
strings.xml:15246:    <string name="APKTOOL_DUMMYVAL_0x7f123bec">"Scam Alert doesn't change end-to-end encryption. Your messages stay private, and WhatsApp can't read them."</string>
strings.xml:15251:Your messages stay private and end-to-end encrypted. You can manage or turn off Scam Alert at any time in Settings."</string>
strings.xml:15254:Scam Alert doesn't change end-to-end encryption. Your messages stay private, and WhatsApp can't read them. You can manage or turn off Scam Alert at any time in Settings."</string>
strings.xml:15260:    <string name="APKTOOL_DUMMYVAL_0x7f123bf6">Scam Alert runs on your device, so your messages stay end-to-end encrypted. Not even WhatsApp can read them.</string>
strings.xml:15261:    <string name="APKTOOL_DUMMYVAL_0x7f123bf7">"Scam Alert doesn't change end-to-end encryption. Your messages stay private, and WhatsApp can't read them."</string>
strings.xml:15292:    <string name="APKTOOL_DUMMYVAL_0x7f123c16">Scheduling details are visible to guests and WhatsApp. Your personal messages and calls remain end-to-end encrypted. &lt;a href=\"learn-more\">Learn more&lt;/a></string>
strings.xml:15342:    <string name="APKTOOL_DUMMYVAL_0x7f123c48">Screen sharing is end-to-end encrypted and is never recorded by WhatsApp.</string>
strings.xml:15355:    <string name="APKTOOL_DUMMYVAL_0x7f123c55">Screen sharing is end-to-end encrypted and is never recorded by WhatsApp.</string>
strings.xml:15509:    <string name="APKTOOL_DUMMYVAL_0x7f123cf1">"Get notified when your security code changes for a contact's phone in an end-to-end encrypted chat. If you have multiple devices, this setting must be enabled on each device where you want to get notifications. & [... omitted end of l
strings.xml:15512:    <string name="APKTOOL_DUMMYVAL_0x7f123cf4">Messages and calls in end-to-end encrypted chats stay between you and the people you choose. Not even WhatsApp can read or listen to them. &lt;a href=\"%s\">Learn more&lt;/a></string>
strings.xml:15583:    <string name="APKTOOL_DUMMYVAL_0x7f123d3d">"Your security code with all members changed because there was a login on a new device of yours. To verify a contact's security code, open their contact info page and tap \"Encryption\"."</string>
strings.xml:15584:    <string name="APKTOOL_DUMMYVAL_0x7f123d3e">"Your security code with all recipients changed because there was a login on a new device of yours. To verify a contact's security code, open their contact info page and tap \"Encryption\"."</string>
strings.xml:15586:    <string name="APKTOOL_DUMMYVAL_0x7f123d40">"Your security code with all members changed because there was a logout from one of your devices. To verify a contact's security code, open their contact info page and tap \"Encryption\"."</string>
strings.xml:15587:    <string name="APKTOOL_DUMMYVAL_0x7f123d41">"Your security code with all recipients changed because there was a logout from one of your devices. To verify a contact's security code, open their contact info page and tap \"Encryption\"."</string>
strings.xml:15589:    <string name="APKTOOL_DUMMYVAL_0x7f123d43">"Your security code with all members changed because there was a login or logout from one or more of your devices. To verify a contact's security code, open their contact info page and tap \"Encryption\"."</string [... omitted end of l
strings.xml:15590:    <string name="APKTOOL_DUMMYVAL_0x7f123d44">"Your security code with all recipients changed because there was a login or logout from one or more of your devices. To verify a contact's security code, open their contact info page and tap \"Encryption\"."</str [... omitted end of l
strings.xml:15924:    <string name="APKTOOL_DUMMYVAL_0x7f123e96">For added security, you can protect your backup with end-to-end encryption.</string>
strings.xml:15925:    <string name="APKTOOL_DUMMYVAL_0x7f123e97">End-to-end encryption</string>
strings.xml:15946:    <string name="APKTOOL_DUMMYVAL_0x7f123eac">Your backup is being end-to-end encrypted for the first time. This process can take a while. When it is complete, this message will disappear and your backup will be fully end-to-end encrypted.</string>
strings.xml:15965:    <string name="APKTOOL_DUMMYVAL_0x7f123ebf">A new backup is needed before you restore on a new device, because you changed your backup encryption method.</string>
strings.xml:15969:    <string name="APKTOOL_DUMMYVAL_0x7f123ec3">Wait for the current backup to finish before changing backup encryption.</string>
strings.xml:15971:    <string name="APKTOOL_DUMMYVAL_0x7f123ec5">Wait for your media to restore before changing backup encryption.</string>
strings.xml:16049:    <string name="APKTOOL_DUMMYVAL_0x7f123f14">"This passkey protects your end-to-end encrypted backup on WhatsApp. To delete it, first change your backup's end-to-end encryption method."</string>
strings.xml:16060:    <string name="APKTOOL_DUMMYVAL_0x7f123f1d">"Deleting this passkey will replace your current backup with one that isn't protected by end-to-end encryption.
strings.xml:16062:You can turn on encrypted backups again later."</string>
strings.xml:16167:    <string name="APKTOOL_DUMMYVAL_0x7f123f84">"Get occasional reminders about messages, calls or status updates you haven't seen"</string>
strings.xml:16192:    <string name="APKTOOL_DUMMYVAL_0x7f123f9e">"Get occasional reminders about messages or status updates you haven't seen"</string>
strings.xml:16811:    <string name="APKTOOL_DUMMYVAL_0x7f124281">End-to-end encrypted</string>
strings.xml:16851:    <string name="APKTOOL_DUMMYVAL_0x7f1242aa">Your statuses are &lt;a href=\"%1$s\">end-to-end encrypted&lt;/a>. They will disappear after %2$d hours.</string>
strings.xml:16891:    <string name="APKTOOL_DUMMYVAL_0x7f1242d2">Your statuses are &lt;a href=\"%1$s\">end-to-end encrypted&lt;/a></string>
strings.xml:17000:    <string name="APKTOOL_DUMMYVAL_0x7f124342">Your statuses are &lt;a href=\"%s\">end-to-end encrypted&lt;/a></string>
strings.xml:17120:    <string name="APKTOOL_DUMMYVAL_0x7f1243ba">Sad stickers</string>
strings.xml:17135:    <string name="APKTOOL_DUMMYVAL_0x7f1243c9">Sad</string>
strings.xml:17149:    <string name="APKTOOL_DUMMYVAL_0x7f1243d7">Sad</string>
strings.xml:17867:    <string name="APKTOOL_DUMMYVAL_0x7f1246a1">Your personal voice messages and transcripts remain end-to-end encrypted. No one outside of this chat, not even WhatsApp, can listen to them. &lt;a href=\"transcripts-learn-more\">Learn More&lt;/a></string>
strings.xml:17929:    <string name="APKTOOL_DUMMYVAL_0x7f1246df">Your personal messages remain end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read them. Translations are meant to be helpful, but may not always be accurate.</string>
strings.xml:18197:    <string name="APKTOOL_DUMMYVAL_0x7f1247f3">Messages will stay on your device until this person joins WhatsApp. Once they join, your messages will be delivered with end-to-end encryption.</string>
strings.xml:18199:    <string name="APKTOOL_DUMMYVAL_0x7f1247f5">Messages will be end-to-end encrypted once this person joins WhatsApp.</string>
strings.xml:18675:    <string name="APKTOOL_DUMMYVAL_0x7f1249d0">To comply with laws and regulations, this description is not end-to-end encrypted. %1$s</string>
strings.xml:18800:    <string name="APKTOOL_DUMMYVAL_0x7f124a4d">Your account details are encrypted and stored securely. Update them anytime.</string>
strings.xml:18842:    <string name="APKTOOL_DUMMYVAL_0x7f124a77">Your payment info is encrypted and stored securely. Update it anytime.</string>
strings.xml:18852:    <string name="APKTOOL_DUMMYVAL_0x7f124a81">Your payment info is encrypted and stored securely. Update it anytime.</string>
strings.xml:19222:    <string name="APKTOOL_DUMMYVAL_0x7f124bf5">To verify that messages and calls with %1$s are end-to-end encrypted, scan this code on their device. You can also compare the number above instead. &lt;a href=\"%2$s\"> Learn more&lt;/a></string>
strings.xml:19223:    <string name="APKTOOL_DUMMYVAL_0x7f124bf6">"We can't automatically verify end-to-end encryption at this time."</string>
strings.xml:19226:    <string name="APKTOOL_DUMMYVAL_0x7f124bf9">End-to-end encryption is currently being verified.</string>
strings.xml:19229:    <string name="APKTOOL_DUMMYVAL_0x7f124bfc">End-to-end encryption was automatically verified</string>
strings.xml:19230:    <string name="APKTOOL_DUMMYVAL_0x7f124bfd">To verify end-to-end encryption for group chats, calls and status updates with this business, scan this code on their device. You can also compare the numbers above instead. &lt;a href=\"%1$s\"> Learn more&lt;/a>< [... omitted end of l
strings.xml:19231:    <string name="APKTOOL_DUMMYVAL_0x7f124bfe">To verify end-to-end encryption for group chats and status updates with this business, scan this code on their device. You can also compare the numbers above instead. &lt;a href=\"%1$s\"> Learn more&lt;/a></string [... omitted end of l
strings.xml:19232:    <string name="APKTOOL_DUMMYVAL_0x7f124c01">To verify that messages and calls with %1$s are end-to-end encrypted, scan this code on their device. You can also compare the number above instead. &lt;a href=\"%2$s\"> Learn more&lt;/a></string>
strings.xml:19233:    <string name="APKTOOL_DUMMYVAL_0x7f124c02">To verify that messages and calls with %1$s are end-to-end encrypted, scan this code on their device. &lt;a href=\"%2$s\"> Learn more&lt;/a></string>
strings.xml:19235:    <string name="APKTOOL_DUMMYVAL_0x7f124c06">Verify encryption</string>
strings.xml:19632:    <string name="APKTOOL_DUMMYVAL_0x7f124d94">End-to-end encrypted</string>
strings.xml:19633:    <string name="APKTOOL_DUMMYVAL_0x7f124d95">End-to-end encrypted video call with %s</string>
strings.xml:19634:    <string name="APKTOOL_DUMMYVAL_0x7f124d96">End-to-end encrypted voice call with %s</string>
strings.xml:19644:    <string name="APKTOOL_DUMMYVAL_0x7f124da1">Your private calls remain end-to-end encrypted.</string>
strings.xml:19795:    <string name="APKTOOL_DUMMYVAL_0x7f124e38">"Messages to this chat and calls are now secured with end-to-end encryption, which means third parties can't read or listen to them."</string>
strings.xml:20161:    <string name="APKTOOL_DUMMYVAL_0x7f124fa1">"You haven't seen any advertisers"</string>
strings.xml:20204:    <string name="APKTOOL_DUMMYVAL_0x7f124fcf">"Your personal messages, calls and statuses are &lt;a href=\"%s\">end-to-end encrypted&lt;/a> and can't be used to show you ads."</string>
strings.xml:20239:    <string name="APKTOOL_DUMMYVAL_0x7f124ff3">"Your personal messages, calls and statuses are end-to-end encrypted and can't be used to show you ads. &lt;b>&lt;a href=\"%s\">Learn about other info used to show you ads&lt;/a>&lt;/b>"</string>
strings.xml:20457:    <string name="APKTOOL_DUMMYVAL_0x7f1250ca">If you forgot your PIN, you will need to turn off two-step verification. We will send you a code to log into your account.</string>
strings.xml:20767:    <string name="APKTOOL_DUMMYVAL_0x7f125205">You marked %1$s as verified. Tap to view encryption.</string>
strings.xml:20774:    <string name="APKTOOL_DUMMYVAL_0x7f12520c">You removed the verified mark for %1$s. Tap to view encryption.</string>
strings.xml:21702:    <string name="APKTOOL_DUMMYVAL_0x7f1255d3">End-to-end encrypted backup</string>
```

### subscription_copy — 150 strings

```
plurals.xml:234:        <item quantity="other">Broadcast or create a new group with a maximum of %1$d people at a time.</item>
plurals.xml:235:        <item quantity="one">Broadcast or create a new group with a maximum of %1$d person at a time.</item>
plurals.xml:238:        <item quantity="other">Broadcast to a maximum of %1$d people at a time.</item>
plurals.xml:239:        <item quantity="one">Broadcast to a maximum of %1$d person at a time.</item>
plurals.xml:884:        <item quantity="other">You reached the maximum of %1$d admins for this community</item>
plurals.xml:885:        <item quantity="one">You reached the maximum of %1$d admin for this community</item>
plurals.xml:1032:        <item quantity="other">Maximum group capacity of %1$d members reached.</item>
plurals.xml:1033:        <item quantity="one">Maximum group capacity of %1$d member reached.</item>
plurals.xml:2632:        <item quantity="other">Share status with a maximum of %1$d people at a time.</item>
plurals.xml:2633:        <item quantity="one">Share status with a maximum of %1$d person at a time.</item>
plurals.xml:3176:        <item quantity="other">"Couldn't place call. WhatsApp only supports a maximum of %d people in a group call"</item>
plurals.xml:3177:        <item quantity="one">"Couldn't place call. WhatsApp only supports a maximum of %d person in a group call"</item>
strings.xml:197:    <string name="APKTOOL_DUMMYVAL_0x7f1200c7">View premium sticker</string>
strings.xml:687:    <string name="APKTOOL_DUMMYVAL_0x7f1202ae">"Since you recently removed your WhatsApp account from your Accounts Center, the price of your subscription for no ads in Status &amp; Channels has decreased.
strings.xml:689:Review your subscription to accept the new price of &lt;b>%1$s/month&lt;/b> or choose to use Status &amp; Channels free of charge with ads."</string>
strings.xml:690:    <string name="APKTOOL_DUMMYVAL_0x7f1202af">"Since you recently moved WhatsApp out of your Meta Account, the price of your subscription for no ads in Status &amp; Channels has decreased.
strings.xml:692:Review your subscription to accept the new price of &lt;b>%1$s/month&lt;/b> or choose to use Status &amp; Channels free of charge with ads."</string>
strings.xml:693:    <string name="APKTOOL_DUMMYVAL_0x7f1202b0">Review subscription</string>
strings.xml:694:    <string name="APKTOOL_DUMMYVAL_0x7f1202b1">"You're overpaying for your subscription"</string>
strings.xml:697:Since you changed your age, your subscription is no longer needed and should be canceled.
strings.xml:699:You can cancel your subscription in Google Play.
strings.xml:980:    <string name="APKTOOL_DUMMYVAL_0x7f1203ce">"You reached your subscription's limit. To create AI images, wait until %1$s."</string>
strings.xml:983:    <string name="APKTOOL_DUMMYVAL_0x7f1203d1">"You reached your subscription's limit. To create AI videos, wait until %1$s."</string>
strings.xml:986:    <string name="APKTOOL_DUMMYVAL_0x7f1203d4">"You reached your subscription's limit. To use Thinking, wait until %1$s."</string>
strings.xml:1093:    <string name="APKTOOL_DUMMYVAL_0x7f120438">To enable this feature, first set up face or fingerprint unlock in your device settings.</string>
strings.xml:1098:    <string name="APKTOOL_DUMMYVAL_0x7f12043d">Unlock to use WhatsApp</string>
strings.xml:1284:    <string name="APKTOOL_DUMMYVAL_0x7f1204fa">Premium sticker. Tap to replay.</string>
strings.xml:1311:    <string name="APKTOOL_DUMMYVAL_0x7f120515">Included with your subscription. &lt;a href=\"%1$s\">See all benefits&lt;/a></string>
strings.xml:1313:    <string name="APKTOOL_DUMMYVAL_0x7f120517">Change your app icon, share premium stickers and more when you subscribe to %1$s.</string>
strings.xml:1314:    <string name="APKTOOL_DUMMYVAL_0x7f120518">Change the color of your app, share premium stickers and more when you subscribe to %1$s.</string>
strings.xml:1319:    <string name="APKTOOL_DUMMYVAL_0x7f12051d">Pin extra chats, share premium stickers and more when you subscribe to %1$s.</string>
strings.xml:1320:    <string name="APKTOOL_DUMMYVAL_0x7f12051e">Change your ringtone, share premium stickers and more when you subscribe to %1$s.</string>
strings.xml:1321:    <string name="APKTOOL_DUMMYVAL_0x7f12051f">Share premium stickers, get new app icons and more when you subscribe to %1$s.</string>
strings.xml:1326:    <string name="APKTOOL_DUMMYVAL_0x7f120525">WhatsApp Plus</string>
strings.xml:1332:    <string name="APKTOOL_DUMMYVAL_0x7f12052c">Included with your subscription.</string>
strings.xml:1335:    <string name="APKTOOL_DUMMYVAL_0x7f12052f">Exclusive stickers are included with your subscription. &lt;a href=\"%1$s\">See all benefits&lt;/a></string>
strings.xml:1336:    <string name="APKTOOL_DUMMYVAL_0x7f120530">Change your ringtone, share premium stickers and more when you subscribe to %1$s.</string>
strings.xml:1337:    <string name="APKTOOL_DUMMYVAL_0x7f120531">Explore WhatsApp Plus on your primary device</string>
strings.xml:1343:    <string name="APKTOOL_DUMMYVAL_0x7f120538">Included with your subscription. &lt;a href=\"%1$s\">See all benefits&lt;/a></string>
strings.xml:1347:    <string name="APKTOOL_DUMMYVAL_0x7f12053d">Explore WhatsApp Plus on your primary device to share premium stickers and more when you subscribe.</string>
strings.xml:1348:    <string name="APKTOOL_DUMMYVAL_0x7f12053f">"Premium sticker packs aren't available to you, but you can receive and view them."</string>
strings.xml:1349:    <string name="APKTOOL_DUMMYVAL_0x7f120540">"Premium stickers aren't available to you, but you can receive and view them."</string>
strings.xml:1629:    <string name="APKTOOL_DUMMYVAL_0x7f120664">%1$d GB with %2$s subscription</string>
strings.xml:1630:    <string name="APKTOOL_DUMMYVAL_0x7f120665">%1$s TB with %2$s subscription</string>
strings.xml:1631:    <string name="APKTOOL_DUMMYVAL_0x7f120666">Get %1$d GB with a subscription</string>
strings.xml:1632:    <string name="APKTOOL_DUMMYVAL_0x7f120667">Get %1$s TB with a subscription</string>
strings.xml:1633:    <string name="APKTOOL_DUMMYVAL_0x7f120668">%1$d GB included with your subscription</string>
strings.xml:1634:    <string name="APKTOOL_DUMMYVAL_0x7f120669">%1$s TB included with your subscription</string>
strings.xml:2430:    <string name="APKTOOL_DUMMYVAL_0x7f12099e">Confirm every payment with your fingerprint or face unlock</string>
strings.xml:3132:    <string name="APKTOOL_DUMMYVAL_0x7f120c64">Your Meta One subscription increases your new chat limit to %1$d per month.</string>
strings.xml:3133:    <string name="APKTOOL_DUMMYVAL_0x7f120c65">Your Meta Verified subscription increases your new chat limit to %1$d per month.</string>
strings.xml:3488:    <string name="APKTOOL_DUMMYVAL_0x7f120dcf">Unlock to continue</string>
strings.xml:3498:    <string name="APKTOOL_DUMMYVAL_0x7f120dd9">Unlock chats</string>
strings.xml:3500:    <string name="APKTOOL_DUMMYVAL_0x7f120ddb">Unlock chat</string>
strings.xml:3501:    <string name="APKTOOL_DUMMYVAL_0x7f120ddc">You need a way to unlock chats</string>
strings.xml:3503:    <string name="APKTOOL_DUMMYVAL_0x7f120dde">You need a way to unlock chats</string>
strings.xml:3518:    <string name="APKTOOL_DUMMYVAL_0x7f120ded">Unlock and clear</string>
strings.xml:3519:    <string name="APKTOOL_DUMMYVAL_0x7f120dee">"This will clear all messages, photos and videos in locked chats. Locked chats will be unlocked on the main chat list.
strings.xml:3522:    <string name="APKTOOL_DUMMYVAL_0x7f120def">Locked chats will be cleared and unlocked</string>
strings.xml:3523:    <string name="APKTOOL_DUMMYVAL_0x7f120df0">If you forgot your secret code, you can clear it. This will also unlock and clear messages, photos and videos in locked chats.</string>
strings.xml:3524:    <string name="APKTOOL_DUMMYVAL_0x7f120df1">Unlock and clear locked chats</string>
strings.xml:3525:    <string name="APKTOOL_DUMMYVAL_0x7f120df2">"We couldn't unlock and clear locked chats. Try again."</string>
strings.xml:3526:    <string name="APKTOOL_DUMMYVAL_0x7f120df3">All locked chats are now unlocked and cleared.</string>
strings.xml:3568:    <string name="APKTOOL_DUMMYVAL_0x7f120e1b">Keep your phone unlocked and accept the invitation to connect on your new phone.</string>
strings.xml:3627:    <string name="APKTOOL_DUMMYVAL_0x7f120e59">Keep both phones unlocked and next to each other to finish connecting.</string>
strings.xml:3658:    <string name="APKTOOL_DUMMYVAL_0x7f120e77">Keep both phones unlocked and near each other to transfer chat history.</string>
strings.xml:3680:You can unlock without a verification method, but the chats will be cleared."</string>
strings.xml:3753:    <string name="APKTOOL_DUMMYVAL_0x7f120ed5">Unlock and clear chats?</string>
strings.xml:3754:    <string name="APKTOOL_DUMMYVAL_0x7f120ed6">"If you unlock without your face, fingerprint or device passcode, these chats will be cleared.
strings.xml:4032:    <string name="APKTOOL_DUMMYVAL_0x7f120fe8">Already reached maximum group size in community</string>
strings.xml:5132:    <string name="APKTOOL_DUMMYVAL_0x7f121434">Any channels you created will be deleted and any channel subscriptions associated with this account will be cancelled.</string>
strings.xml:5144:    <string name="APKTOOL_DUMMYVAL_0x7f121440">Your Meta Verified subscription will be canceled as per the Meta Verified terms of service.</string>
strings.xml:5351:    <string name="APKTOOL_DUMMYVAL_0x7f12150c">dial plus</string>
strings.xml:5578:    <string name="APKTOOL_DUMMYVAL_0x7f1215ef">If you use %1$s for WhatsApp Messenger, information related to your business profile, labels, and products and AI agent will be deleted in accordance with the applicable policies and your Meta Verified subscriptio [... omitted end of lo
strings.xml:6134:    <string name="APKTOOL_DUMMYVAL_0x7f121822">People cannot be added because the maximum number of requests have been made.</string>
strings.xml:6135:    <string name="APKTOOL_DUMMYVAL_0x7f121823">Requests maximum reached</string>
strings.xml:7445:    <string name="APKTOOL_DUMMYVAL_0x7f121d50">Keep your phone unlocked and this app open.</string>
strings.xml:8150:    <string name="APKTOOL_DUMMYVAL_0x7f122013">Manage subscription</string>
strings.xml:8195:    <string name="APKTOOL_DUMMYVAL_0x7f122041">Find locked chats by entering your code into the search bar in the Chats tab. Chats will be unlocked and cleared if you forget your code and create a new one.</string>
strings.xml:8296:    <string name="APKTOOL_DUMMYVAL_0x7f1220a6">Use your device’s secure unlock feature, such as fingerprint, face scan or PIN.</string>
strings.xml:8932:    <string name="APKTOOL_DUMMYVAL_0x7f122340">Add WhatsApp to your Meta Account to unlock cross-profile experiences and more.</string>
strings.xml:9010:    <string name="APKTOOL_DUMMYVAL_0x7f122389">Unlock to link a device</string>
strings.xml:9107:    <string name="APKTOOL_DUMMYVAL_0x7f1223e5">"You've created the maximum number of lists."</string>
strings.xml:9152:    <string name="APKTOOL_DUMMYVAL_0x7f122414">%1$s, WhatsApp Plus</string>
strings.xml:9381:    <string name="APKTOOL_DUMMYVAL_0x7f122506">Manage my subscription</string>
strings.xml:9873:    <string name="APKTOOL_DUMMYVAL_0x7f122702">"You've reached the maximum number of chats. Delete one to create another."</string>
strings.xml:10139:    <string name="APKTOOL_DUMMYVAL_0x7f122812">Keep your phone unlocked and this app open.</string>
strings.xml:10220:    <string name="APKTOOL_DUMMYVAL_0x7f122862">Access WhatsApp the same way you unlock your phone: with your fingerprint, face or screen lock.</string>
strings.xml:10424:    <string name="APKTOOL_DUMMYVAL_0x7f122930">Included in your subscription. &lt;a href=\"see-all-benefits\">See all benefits&lt;/a></string>
strings.xml:10869:    <string name="APKTOOL_DUMMYVAL_0x7f122aee">You have reached the maximum number of updates you can schedule for this time.</string>
strings.xml:10872:    <string name="APKTOOL_DUMMYVAL_0x7f122af1">You have reached the maximum number of updates you can schedule.</string>
strings.xml:10922:    <string name="APKTOOL_DUMMYVAL_0x7f122b23">Your verified badge will be removed from this channel. Your Meta Verified subscription will remain active.</string>
strings.xml:11618:    <string name="APKTOOL_DUMMYVAL_0x7f122de9">Keep your phone unlocked and keep this app open, to ensure that chats are restored successfully.</string>
strings.xml:12200:    <string name="APKTOOL_DUMMYVAL_0x7f12302d">"Use your device's secure unlock feature."</string>
strings.xml:12825:    <string name="APKTOOL_DUMMYVAL_0x7f1232ba">Maximum amount is %s</string>
strings.xml:13124:    <string name="APKTOOL_DUMMYVAL_0x7f1233df">To answer this video call from %s, allow WhatsApp access to your camera. Tap Settings, unlock your device, tap Permissions, and turn Camera on.</string>
strings.xml:13125:    <string name="APKTOOL_DUMMYVAL_0x7f1233e0">To answer this video call from %s, tap Continue, unlock your device, and allow WhatsApp access to your camera.</string>
strings.xml:13127:    <string name="APKTOOL_DUMMYVAL_0x7f1233e2">To place a video call to %s, allow WhatsApp access to your camera. Tap Settings, unlock your device, tap Permissions, and turn Camera on.</string>
strings.xml:13199:    <string name="APKTOOL_DUMMYVAL_0x7f12342a">To answer this call from %s, allow WhatsApp access to your microphone. Tap Settings, unlock your device, tap Permissions, and turn Microphone on.</string>
strings.xml:13200:    <string name="APKTOOL_DUMMYVAL_0x7f12342b">To answer this call from %s, tap Continue, unlock your device, and allow WhatsApp access to your microphone.</string>
strings.xml:13206:    <string name="APKTOOL_DUMMYVAL_0x7f123431">To answer this video call from %s, allow WhatsApp access to your microphone and camera. Tap Settings, unlock your device, tap Permissions, and turn Microphone and Camera on.</string>
strings.xml:13207:    <string name="APKTOOL_DUMMYVAL_0x7f123432">To answer this video call from %s, tap Continue, unlock your device, and allow WhatsApp access to your microphone and camera.</string>
strings.xml:14375:    <string name="APKTOOL_DUMMYVAL_0x7f1238a4">Recent activity on your account may not have followed the &lt;a href=\"%s\">WhatsApp Business Messaging Policy&lt;/a> on buying, selling, or facilitating the exchange of digital goods or subscriptions.</string>
strings.xml:14549:    <string name="APKTOOL_DUMMYVAL_0x7f123947" formatted="false">Country code for %s, plus %s</string>
strings.xml:14593:    <string name="APKTOOL_DUMMYVAL_0x7f123974">cannot currently use WhatsApp because it is violating our Commerce Policy for Digital and subscription services.</string>
strings.xml:15195:    <string name="APKTOOL_DUMMYVAL_0x7f123bb9">"Couldn't load premium ringtones. Check your internet connection and try again."</string>
strings.xml:15312:    <string name="APKTOOL_DUMMYVAL_0x7f123c2a">You have reached the maximum number of messages you can schedule.</string>
strings.xml:15491:    <string name="APKTOOL_DUMMYVAL_0x7f123ce3">"Unlock your chats with a secret code instead of your device's passcode."</string>
strings.xml:15492:    <string name="APKTOOL_DUMMYVAL_0x7f123ce4">"Unlock your chats with a secret code instead of your device's passcode. You can also open them on some linked devices."</string>
strings.xml:15495:    <string name="APKTOOL_DUMMYVAL_0x7f123ce7">"If you continue, locked chats will move to the chat list. You'll use your face or fingerprint to unlock them instead of a secret code."</string>
strings.xml:15498:You can still use your face, fingerprint or passcode to unlock them on this device."</string>
strings.xml:15501:You can still use your face, fingerprint or passcode to unlock them on this device."</string>
strings.xml:15502:    <string name="APKTOOL_DUMMYVAL_0x7f123cea">If you continue, Locked chats will move to the chat list. You can still use your face, fingerprint or passcode to unlock them on this device.</string>
strings.xml:15811:    <string name="APKTOOL_DUMMYVAL_0x7f123e1e">You have connected the maximum number of agents.</string>
strings.xml:15901:    <string name="APKTOOL_DUMMYVAL_0x7f123e7f">Explore premium benefits</string>
strings.xml:15902:    <string name="APKTOOL_DUMMYVAL_0x7f123e80">Subscriptions</string>
strings.xml:16056:    <string name="APKTOOL_DUMMYVAL_0x7f123f19">Access WhatsApp the same way you unlock your phone: with your fingerprint, face or screen lock. Your passkey gives you a secure and easy way to log back into your account. &lt;a href=\"passkeys_learn_more_uri\">Le [... omitted end of l
strings.xml:16125:    <string name="APKTOOL_DUMMYVAL_0x7f123f5c">Unlock with biometric</string>
strings.xml:16130:    <string name="APKTOOL_DUMMYVAL_0x7f123f61">Unlock with fingerprint</string>
strings.xml:16488:    <string name="APKTOOL_DUMMYVAL_0x7f124129">&lt;b>Switch to WhatsApp Messenger?&lt;/b>&lt;br/>&lt;br/>-Only your messages and media will remain in your account.&lt;br/>&lt;br/>-Your greeting and away messages, catalog, items and labels will be permanently d [... omitted end of l
strings.xml:16596:    <string name="APKTOOL_DUMMYVAL_0x7f1241a6">Locked amount, tap to unlock</string>
strings.xml:16623:    <string name="APKTOOL_DUMMYVAL_0x7f1241c1">Maximum amount per person is %1$s</string>
strings.xml:17164:    <string name="APKTOOL_DUMMYVAL_0x7f1243e6">Plus</string>
strings.xml:17723:    <string name="APKTOOL_DUMMYVAL_0x7f12460f">Unlock selling on WhatsApp</string>
strings.xml:18235:    <string name="APKTOOL_DUMMYVAL_0x7f124819">Unlock and clear</string>
strings.xml:18236:    <string name="APKTOOL_DUMMYVAL_0x7f12481a">Unlock</string>
strings.xml:18237:    <string name="APKTOOL_DUMMYVAL_0x7f12481b">Unlock without verification</string>
strings.xml:18383:    <string name="APKTOOL_DUMMYVAL_0x7f1248af">Minimum 8 different digits, maximum 9</string>
strings.xml:18475:    <string name="APKTOOL_DUMMYVAL_0x7f12490b">Keep your UPI Lite balance ready for payments. You can pause or cancel anytime.</string>
strings.xml:18505:    <string name="APKTOOL_DUMMYVAL_0x7f12492a">Max</string>
strings.xml:19641:    <string name="APKTOOL_DUMMYVAL_0x7f124d9e">"Couldn't add %s because the maximum number of people has been reached"</string>
strings.xml:20241:    <string name="APKTOOL_DUMMYVAL_0x7f124ff5">Any active channel subscriptions associated with this account will be canceled</string>
strings.xml:20242:    <string name="APKTOOL_DUMMYVAL_0x7f124ff6">"You're subscribed to this channel. If you unfollow, your subscription will also be canceled."</string>
strings.xml:20243:    <string name="APKTOOL_DUMMYVAL_0x7f124ff7">"You're subscribed to the following channels %1$s. If you unfollow, your subscriptions will also be canceled."</string>
strings.xml:20244:    <string name="APKTOOL_DUMMYVAL_0x7f124ff8">"You're subscribed to %1$s. If you unfollow, your subscription will also be canceled."</string>
strings.xml:20245:    <string name="APKTOOL_DUMMYVAL_0x7f124ff9">Unfollow and cancel subscription?</string>
strings.xml:20248:    <string name="APKTOOL_DUMMYVAL_0x7f124ffc">Unfollow and cancel subscription</string>
strings.xml:20249:    <string name="APKTOOL_DUMMYVAL_0x7f124ffd">You subscribed to this channel from a different device. You can manage your subscription or unfollow this channel from your primary device.</string>
strings.xml:20250:    <string name="APKTOOL_DUMMYVAL_0x7f124ffe">You are subscribed to %1$s channels from a different device. You can manage your subscriptions or unfollow these channels from your primary device.</string>
strings.xml:20251:    <string name="APKTOOL_DUMMYVAL_0x7f124fff">Manage subscription from primary device</string>
strings.xml:20254:    <string name="APKTOOL_DUMMYVAL_0x7f125002">"Your active subscription will be canceled and subscribers will get a refund for this month's subscription fees."</string>
strings.xml:20257:    <string name="APKTOOL_DUMMYVAL_0x7f125005">%1$s/month • Renews on %2$s</string>
strings.xml:20259:    <string name="APKTOOL_DUMMYVAL_0x7f125007">"You'll need the Google Play app to buy a subscription. Download the app and try again."</string>
strings.xml:20266:    <string name="APKTOOL_DUMMYVAL_0x7f12500e">Manage subscription</string>
strings.xml:20277:    <string name="APKTOOL_DUMMYVAL_0x7f125019">By tapping Continue, you agree to the &lt;a href=\"wamosub-subscription-terms\"> Channel Subscriptions Terms &lt;/a>and acknowledge the &lt;a href=\"wamosub-privacy-policy\">Channels Privacy Policy.&lt;/a> &lt;a h [... omitted end of l
strings.xml:20279:    <string name="APKTOOL_DUMMYVAL_0x7f12501b">By tapping Continue, you agree to the &lt;a href=\"wamosub-subscription-terms\"> Channel Subscriptions Terms &lt;/a>and acknowledge the &lt;a href=\"wamosub-privacy-policy\">Status and Channels Privacy Policy.&lt; [... omitted end of l
strings.xml:20281:    <string name="APKTOOL_DUMMYVAL_0x7f12501d">%1$s monthly • Cancel anytime</string>
strings.xml:20545:    <string name="APKTOOL_DUMMYVAL_0x7f125124">baseline_profiles_12_plus</string>
strings.xml:20918:    <string name="APKTOOL_DUMMYVAL_0x7f1252a0">"You can't make %s an admin because this group has the maximum number of admins allowed."</string>
strings.xml:21008:    <string name="APKTOOL_DUMMYVAL_0x7f1252fa">Max total</string>
```

### data_copy — 673 strings

```
plurals.xml:12:        <item quantity="other">Edit excluded contacts, %1$d currently excluded</item>
plurals.xml:13:        <item quantity="one">Edit excluded contacts, %1$d currently excluded</item>
plurals.xml:158:        <item quantity="other">%d contacts</item>
plurals.xml:162:        <item quantity="other">%d contacts</item>
plurals.xml:242:        <item quantity="other">%2$d group members are not in your contacts. &lt;font color=#%1$s>&lt;b>Add to contacts&lt;/b>&lt;/font></item>
plurals.xml:243:        <item quantity="one">%2$d group member is not in your contacts. &lt;font color=#%1$s>&lt;b>Add to contacts&lt;/b>&lt;/font></item>
plurals.xml:362:        <item quantity="other">Your new number will be shared with your groups and &lt;a href=\"contacts-link\">%d contacts&lt;/a>.</item>
plurals.xml:363:        <item quantity="one">Your new number will be shared with your groups and &lt;a href=\"contacts-link\">%d contact&lt;/a>.</item>
plurals.xml:366:        <item quantity="other">Out of &lt;a href=\"contacts-link\">%1$d contacts&lt;/a>, only the people who have your old number will be notified about your new number.</item>
plurals.xml:367:        <item quantity="one">Out of &lt;a href=\"contacts-link\">%1$d contact&lt;/a>, only the people who have your old number will be notified about your new number.</item>
plurals.xml:370:        <item quantity="other">Your new number will be shared with your groups and &lt;a href=\"contacts-link\">%1$d people&lt;/a>.</item>
plurals.xml:371:        <item quantity="one">Your new number will be shared with your groups and &lt;a href=\"contacts-link\">%1$d person&lt;/a>.</item>
plurals.xml:514:        <item quantity="other">"You can't select more than %1$d contacts."</item>
plurals.xml:546:        <item quantity="other">%1$s and %2$d other contacts</item>
plurals.xml:578:        <item quantity="other">You can add %1$d other members of %2$s to your contacts.</item>
plurals.xml:579:        <item quantity="one">You can add %1$d other member of %2$s to your contacts.</item>
plurals.xml:690:        <item quantity="other">Message privately with your %d WhatsApp contacts, no matter what device they use.</item>
plurals.xml:691:        <item quantity="one">Message privately with your WhatsApp contacts, no matter what device they use.</item>
plurals.xml:694:        <item quantity="other">Chat with your %d WhatsApp contacts, or invite a friend to WhatsApp.</item>
plurals.xml:695:        <item quantity="one">WhatsApp is better with friends. Use the button below to invite your contacts.</item>
plurals.xml:920:        <item quantity="other">This status will be sent to your contacts excluding %1$d.</item>
plurals.xml:921:        <item quantity="one">This status will be sent to your contacts excluding %1$d.</item>
plurals.xml:924:        <item quantity="other">This status will be sent to %1$d contacts.</item>
plurals.xml:1000:        <item quantity="other">%d contacts excluded</item>
plurals.xml:1100:        <item quantity="other">"%d people not shown because they aren't in your contacts"</item>
plurals.xml:1101:        <item quantity="one">"%d person not shown because they aren't in your contacts"</item>
plurals.xml:1188:        <item quantity="other">Found %1$d contact cards for this number. Add to your contacts?</item>
plurals.xml:1189:        <item quantity="one">Found %1$d contact card for this number. Add to your contacts?</item>
plurals.xml:1196:        <item quantity="other">This status will be shared with your contacts excluding %d.</item>
plurals.xml:1197:        <item quantity="one">This status will be shared with your contacts excluding %d.</item>
plurals.xml:1200:        <item quantity="other">This status will be shared with %d contacts.</item>
plurals.xml:1240:        <item quantity="other">%1$d contacts</item>
plurals.xml:1362:        <item quantity="other">"You can't select more than %1$d contacts."</item>
plurals.xml:1370:        <item quantity="other">Location marker for %s</item>
plurals.xml:1371:        <item quantity="one">Location marker for %s</item>
plurals.xml:1578:        <item quantity="other">%d contacts</item>
plurals.xml:1582:        <item quantity="other">%d contacts</item>
plurals.xml:1586:        <item quantity="other">At least %d contacts must be selected</item>
plurals.xml:1666:        <item quantity="other">You can only select %1$d contacts</item>
plurals.xml:1774:        <item quantity="other">%s reactions from contacts</item>
plurals.xml:1775:        <item quantity="one">%s reaction from contacts</item>
plurals.xml:1868:        <item quantity="other">"You can't select more than %1$d contacts."</item>
plurals.xml:1932:        <item quantity="other">You have %1$d contacts on WhatsApp</item>
plurals.xml:1936:        <item quantity="other">&lt;b>%1$s&lt;/b> and %2$d more of your contacts are on WhatsApp</item>
plurals.xml:1940:        <item quantity="other">&lt;b>%1$s&lt;/b>, &lt;b>%2$s&lt;/b>, &lt;b>%3$s&lt;/b> and %4$d more of your contacts are on WhatsApp</item>
plurals.xml:1944:        <item quantity="other">&lt;b>%1$s&lt;/b>, &lt;b>%2$s&lt;/b> and %3$d more of your contacts are on WhatsApp</item>
plurals.xml:1984:        <item quantity="other">"%d members not displayed because they aren't in your contacts"</item>
plurals.xml:1985:        <item quantity="one">"%d member not displayed because they aren't in your contacts"</item>
plurals.xml:2024:        <item quantity="other">Sending invites to %1$d contacts</item>
plurals.xml:2100:        <item quantity="other">%1$d contacts</item>
plurals.xml:2144:        <item quantity="other">%1$d contacts included</item>
plurals.xml:2148:        <item quantity="other">%d contacts selected</item>
plurals.xml:2552:        <item quantity="other">Contacts except - %d excluded</item>
plurals.xml:2553:        <item quantity="one">Contacts except - %d excluded</item>
plurals.xml:2556:        <item quantity="other">%1$d contacts</item>
plurals.xml:2564:        <item quantity="other">%1$d contacts included</item>
plurals.xml:2580:        <item quantity="other">%d contacts excluded</item>
plurals.xml:2584:        <item quantity="other">%d contacts selected</item>
plurals.xml:2608:        <item quantity="other">%d contacts selected</item>
plurals.xml:2900:        <item quantity="other">%1$s members added to your contacts.</item>
plurals.xml:2901:        <item quantity="one">%1$s member added to your contacts.</item>
plurals.xml:2924:        <item quantity="other">%1$d contacts</item>
plurals.xml:2932:        <item quantity="other">%1$d contacts</item>
strings.xml:93:    <string name="APKTOOL_DUMMYVAL_0x7f12005a">Third-party chats are offered to our European Region users as required by law.</string>
strings.xml:112:    <string name="APKTOOL_DUMMYVAL_0x7f12006d">About third-party groups</string>
strings.xml:114:    <string name="APKTOOL_DUMMYVAL_0x7f12006f">My contacts except %1$d</string>
strings.xml:130:    <string name="APKTOOL_DUMMYVAL_0x7f120084">My contacts except…</string>
strings.xml:243:    <string name="APKTOOL_DUMMYVAL_0x7f1200f5">location</string>
strings.xml:288:    <string name="APKTOOL_DUMMYVAL_0x7f120122">To start calling contacts who have WhatsApp, tap phone icon at the bottom of your screen.</string>
strings.xml:402:    <string name="APKTOOL_DUMMYVAL_0x7f120196">Securely transfer all your chats and media to this phone. Have your &lt;b>%1$s&lt;/b> handy and Wi-Fi and Location turned on.</string>
strings.xml:482:    <string name="APKTOOL_DUMMYVAL_0x7f1201e3">Advertise on Facebook &amp; Instagram</string>
strings.xml:515:    <string name="APKTOOL_DUMMYVAL_0x7f120204">Add to contacts</string>
strings.xml:517:    <string name="APKTOOL_DUMMYVAL_0x7f120206">Add contacts to notify</string>
strings.xml:548:    <string name="APKTOOL_DUMMYVAL_0x7f120225">Add paid partnership</string>
strings.xml:550:    <string name="APKTOOL_DUMMYVAL_0x7f120227">Add members to contacts</string>
strings.xml:583:    <string name="APKTOOL_DUMMYVAL_0x7f120248">Add to contacts</string>
strings.xml:704:    <string name="APKTOOL_DUMMYVAL_0x7f1202b6">"All set. You'll use Status &amp; Channels free of charge with less-personalized ads."</string>
strings.xml:705:    <string name="APKTOOL_DUMMYVAL_0x7f1202b7">"All set. You'll use Status &amp; Channels free of charge with personalized ads."</string>
strings.xml:910:    <string name="APKTOOL_DUMMYVAL_0x7f120387">Use information sources to help personalize responses in this chat.</string>
strings.xml:911:    <string name="APKTOOL_DUMMYVAL_0x7f120389">Personalization</string>
strings.xml:914:    <string name="APKTOOL_DUMMYVAL_0x7f12038c">Personalization responses</string>
strings.xml:975:    <string name="APKTOOL_DUMMYVAL_0x7f1203c9">Search your WhatsApp chats and contacts, or send a question to Meta AI. &lt;a href=\"%s\">Learn more&lt;/a></string>
strings.xml:1004:    <string name="APKTOOL_DUMMYVAL_0x7f1203e6">"Meta AI is an optional service from Meta that uses AI models to provide responses. Don't share information, including sensitive topics, about others or yourself that you don't want the AI to retain and use. Meta  [... omitted end of lo
strings.xml:1007:    <string name="APKTOOL_DUMMYVAL_0x7f1203e7">"Meta AI is an optional service from Meta that uses AI models to provide responses. Meta AI can only read messages people share with it. Meta can't read any other messages in your personal chats, as your personal  [... omitted end of lo
strings.xml:1008:    <string name="APKTOOL_DUMMYVAL_0x7f1203e8">"Meta AI is an optional service from Meta that uses AI models to provide responses. Meta AI can only read messages people share with it. Meta can't read any other messages in your personal chats, as your personal  [... omitted end of lo
strings.xml:1230:    <string name="APKTOOL_DUMMYVAL_0x7f1204c3">Location</string>
strings.xml:1418:    <string name="APKTOOL_DUMMYVAL_0x7f120586">See saved contacts and payments</string>
strings.xml:1900:    <string name="APKTOOL_DUMMYVAL_0x7f12077a">But we will be soon! For now, try a different location.</string>
strings.xml:1912:    <string name="APKTOOL_DUMMYVAL_0x7f120786">Catalog not available in your location</string>
strings.xml:1924:    <string name="APKTOOL_DUMMYVAL_0x7f120792">Allow location access</string>
strings.xml:1928:    <string name="APKTOOL_DUMMYVAL_0x7f120796">Change location</string>
strings.xml:1930:    <string name="APKTOOL_DUMMYVAL_0x7f120798">Clear currently set location?</string>
strings.xml:1944:    <string name="APKTOOL_DUMMYVAL_0x7f1207a6">Select a location on a map or try enabling your location in settings</string>
strings.xml:1945:    <string name="APKTOOL_DUMMYVAL_0x7f1207a7">"Couldn't set your location"</string>
strings.xml:1946:    <string name="APKTOOL_DUMMYVAL_0x7f1207a8">To discover businesses near you, allow WhatsApp to access your location.</string>
strings.xml:1947:    <string name="APKTOOL_DUMMYVAL_0x7f1207a9">"Share your location to discover 
strings.xml:1956:    <string name="APKTOOL_DUMMYVAL_0x7f1207b1">"Your location stays private. It can't be seen by businesses or WhatsApp. &lt;a href=learn-more>Learn more&lt;/a>"</string>
strings.xml:1957:    <string name="APKTOOL_DUMMYVAL_0x7f1207b2">"Your location stays private. It can't be seen by businesses or WhatsApp. &lt;a href=clear-search-location>Clear currently set location&lt;/a> or &lt;a href=learn-more>Learn more&lt;/a>"</string>
strings.xml:1962:    <string name="APKTOOL_DUMMYVAL_0x7f1207b7">Pick location on map</string>
strings.xml:1975:    <string name="APKTOOL_DUMMYVAL_0x7f1207c4">Setting your location…</string>
strings.xml:1978:    <string name="APKTOOL_DUMMYVAL_0x7f1207d5">Set your location to see more relevant businesses.</string>
strings.xml:1983:    <string name="APKTOOL_DUMMYVAL_0x7f1207da">Check that your GPS is enabled and try again, or choose the location using another option.</string>
strings.xml:1995:    <string name="APKTOOL_DUMMYVAL_0x7f1207e7">Finding your location…</string>
strings.xml:2002:    <string name="APKTOOL_DUMMYVAL_0x7f1207ee">Location Settings</string>
strings.xml:2003:    <string name="APKTOOL_DUMMYVAL_0x7f1207f1">Near current location</string>
strings.xml:2039:    <string name="APKTOOL_DUMMYVAL_0x7f120815">To see businesses that are near you, allow WhatsApp to use your location.</string>
strings.xml:2042:    <string name="APKTOOL_DUMMYVAL_0x7f120818">[Internal] Set location to Colombia</string>
strings.xml:2044:    <string name="APKTOOL_DUMMYVAL_0x7f12081a">Set a different location</string>
strings.xml:2052:    <string name="APKTOOL_DUMMYVAL_0x7f120822">Unknown location</string>
strings.xml:2055:    <string name="APKTOOL_DUMMYVAL_0x7f120825">Use current location</string>
strings.xml:2056:    <string name="APKTOOL_DUMMYVAL_0x7f120826">Approximate location</string>
strings.xml:2058:    <string name="APKTOOL_DUMMYVAL_0x7f120828">"Couldn't determine location"</string>
strings.xml:2060:    <string name="APKTOOL_DUMMYVAL_0x7f12082a">Use precise location</string>
strings.xml:2065:    <string name="APKTOOL_DUMMYVAL_0x7f12082f">Block %s? Blocked contacts will no longer be able to call you or send you messages.</string>
strings.xml:2081:    <string name="APKTOOL_DUMMYVAL_0x7f12083f">Blocked in third-party chats</string>
strings.xml:2088:    <string name="APKTOOL_DUMMYVAL_0x7f120846">People you blocked will no longer be able to call you or send you messages. &lt;br/>&lt;br/>People you block on WhatsApp may still be able to contact you in third-party apps. If this happens, you can also block th [... omitted end of lo
strings.xml:2122:    <string name="APKTOOL_DUMMYVAL_0x7f120868">%1$s is registered as an official business account. The business is saved as a different name in your contacts.</string>
strings.xml:2124:    <string name="APKTOOL_DUMMYVAL_0x7f12086a">This chat is with the official business account of %1$s. The business is saved as a different name in your contacts.</string>
strings.xml:2130:    <string name="APKTOOL_DUMMYVAL_0x7f120870">"%1$s is now registered as an official business account, but it's saved as a different name in your contacts. This business no longer uses Facebook to manage its WhatsApp conversations. Tap to learn how this chang [... omitted end of lo
strings.xml:2131:    <string name="APKTOOL_DUMMYVAL_0x7f120871">"%1$s is now a verified account, but it's saved as a different name in your contacts. It no longer uses Meta to manage its WhatsApp conversations. This changes privacy in this chat. Learn more"</string>
strings.xml:2134:    <string name="APKTOOL_DUMMYVAL_0x7f120874">"%1$s is now registered as an official business account, but it's saved as a different name in your contacts. This business only uses Facebook to manage its WhatsApp conversations. Tap to learn how this changes pr [... omitted end of lo
strings.xml:2135:    <string name="APKTOOL_DUMMYVAL_0x7f120875">"%1$s is now a verified account, but it's saved as a different name in your contacts. This account only uses Meta to manage its WhatsApp conversations. This changes privacy in this chat. Learn more"</string>
strings.xml:2157:    <string name="APKTOOL_DUMMYVAL_0x7f12088b">"%1$s is now registered as an official business account, but it's saved as a different name in your contacts. This business now uses other companies instead of Facebook to manage its WhatsApp conversations. Tap to [... omitted end of lo
strings.xml:2158:    <string name="APKTOOL_DUMMYVAL_0x7f12088c">"%1$s is now a verified account, but it's saved as a different name in your contacts. The account now uses other companies instead of Meta to manage its WhatsApp conversations. This changes privacy in this chat. L [... omitted end of lo
strings.xml:2174:    <string name="APKTOOL_DUMMYVAL_0x7f12089c">"%1$s is now registered as an official business account, but it's saved as a different name in your contacts. This business uses Facebook and other companies to manage its WhatsApp conversations. Tap to learn how  [... omitted end of lo
strings.xml:2175:    <string name="APKTOOL_DUMMYVAL_0x7f12089d">"%1$s is now a verified account, but it's saved as a different name in your contacts. This account uses Meta and other companies to manage its WhatsApp conversations. This changes privacy in this chat. Learn more" [... omitted end of lo
strings.xml:2178:    <string name="APKTOOL_DUMMYVAL_0x7f1208a0">"%1$s is now registered as an official business account, but it's saved as a different name in your contacts. This business uses other companies to manage its WhatsApp conversations. Tap to learn how this changes  [... omitted end of lo
strings.xml:2179:    <string name="APKTOOL_DUMMYVAL_0x7f1208a1">"%1$s is now a verified account, but it's saved as a different name in your contacts. The account uses other companies to manage its WhatsApp conversations. This changes privacy in this chat. Learn more"</string>
strings.xml:2182:    <string name="APKTOOL_DUMMYVAL_0x7f1208a4">"%1$s is now registered as an official business account, but it's saved as a different name in your contacts. This business uses Facebook to manage its WhatsApp conversations. Tap to learn how this changes privacy [... omitted end of lo
strings.xml:2183:    <string name="APKTOOL_DUMMYVAL_0x7f1208a5">"%1$s is now a verified account, but it's saved as a different name in your contacts. This account uses Meta to manage its WhatsApp conversations. This changes privacy in this chat. Learn more"</string>
strings.xml:2199:    <string name="APKTOOL_DUMMYVAL_0x7f1208b5">Booking location address</string>
strings.xml:2222:    <string name="APKTOOL_DUMMYVAL_0x7f1208cc">Pin location icon</string>
strings.xml:2384:    <string name="APKTOOL_DUMMYVAL_0x7f120970">"By continuing, you accept WhatsApp's payments &lt;a href=\"wa-terms\">terms&lt;/a> and &lt;a href=\"wa-privacy-policy\">privacy policy&lt;/a>, and Meta's &lt;a href=\"fb-payments-terms\">payments terms&lt;/a> and [... omitted end of lo
strings.xml:2392:    <string name="APKTOOL_DUMMYVAL_0x7f120978">Payment in a third-party app can only be confirmed by the receiver.</string>
strings.xml:2526:    <string name="APKTOOL_DUMMYVAL_0x7f120a03">Only contacts who have you in their address book will receive your broadcast messages.</string>
strings.xml:2546:    <string name="APKTOOL_DUMMYVAL_0x7f120a18">Use current location</string>
strings.xml:2599:    <string name="APKTOOL_DUMMYVAL_0x7f120a4c">Location sharing</string>
strings.xml:2608:    <string name="APKTOOL_DUMMYVAL_0x7f120a55">Save to contacts</string>
strings.xml:2647:    <string name="APKTOOL_DUMMYVAL_0x7f120a7d">Limited liability partnership</string>
strings.xml:2651:    <string name="APKTOOL_DUMMYVAL_0x7f120a81">Partnership</string>
strings.xml:2936:    <string name="APKTOOL_DUMMYVAL_0x7f120b9f">Not in your contacts</string>
strings.xml:2937:    <string name="APKTOOL_DUMMYVAL_0x7f120ba0">Contacts</string>
strings.xml:2989:    <string name="APKTOOL_DUMMYVAL_0x7f120bd4">To make it harder for people to infer your location, calls on this device will be securely relayed through WhatsApp servers. This will reduce call quality. &lt;a href=call_relaying_help>Learn more&lt;/a></string> [... omitted end of lon
strings.xml:3006:    <string name="APKTOOL_DUMMYVAL_0x7f120be5">This caller is not in your contacts</string>
strings.xml:3030:    <string name="APKTOOL_DUMMYVAL_0x7f120bfd">Personalize your video calls with a variety of effects, filters and backgrounds!</string>
strings.xml:3150:    <string name="APKTOOL_DUMMYVAL_0x7f120c76">Location</string>
strings.xml:3163:    <string name="APKTOOL_DUMMYVAL_0x7f120c83">Search contacts</string>
strings.xml:3299:    <string name="APKTOOL_DUMMYVAL_0x7f120d0a">"%1$s changed their phone number. You're currently chatting with their new number. Tap to add it to your contacts."</string>
strings.xml:3303:    <string name="APKTOOL_DUMMYVAL_0x7f120d0e">"%1$s changed their phone number. You're currently chatting with their new number: %2$s. Add it to your contacts?"</string>
strings.xml:3307:    <string name="APKTOOL_DUMMYVAL_0x7f120d12">All contacts</string>
strings.xml:3309:    <string name="APKTOOL_DUMMYVAL_0x7f120d14">"All contacts and people you've chatted with"</string>
strings.xml:3310:    <string name="APKTOOL_DUMMYVAL_0x7f120d15">Contacts I have chats with</string>
strings.xml:3319:    <string name="APKTOOL_DUMMYVAL_0x7f120d1e">Share my new number with my contacts</string>
strings.xml:3331:    <string name="APKTOOL_DUMMYVAL_0x7f120d2f">Third-party chats are only available to people who have a European Region phone number. &lt;br/>&lt;br/>If you change your phone number to a non-European Region number, you will not be able to continue using third [... omitted end of lo
strings.xml:3337:    <string name="APKTOOL_DUMMYVAL_0x7f120d37">Contacts (%1$d)</string>
strings.xml:3424:    <string name="APKTOOL_DUMMYVAL_0x7f120d8e">This feature isn’t available in %1$s’s location.</string>
strings.xml:3444:    <string name="APKTOOL_DUMMYVAL_0x7f120da2">"%1$s changed their phone number. You're currently chatting with their new number. Tap to add it to your contacts."</string>
strings.xml:3452:    <string name="APKTOOL_DUMMYVAL_0x7f120daa">"You're messaging someone outside of WhatsApp. Third-party apps may have different security. *Learn more*"</string>
strings.xml:3615:    <string name="APKTOOL_DUMMYVAL_0x7f120e4c">"Allow precise location and media access so your phones can connect over Wi-Fi. WhatsApp doesn't store this data. &lt;font color=#%2$s>&lt;a href=\"%1$s\">Learn more&lt;/a>&lt;/font>"</string>
strings.xml:3616:    <string name="APKTOOL_DUMMYVAL_0x7f120e4d">Precise location &amp; media</string>
strings.xml:3617:    <string name="APKTOOL_DUMMYVAL_0x7f120e4e">"Allow precise location access so your phones can connect over Wi-Fi. WhatsApp doesn't store this data. &lt;font color=#%2$s>&lt;a href=\"%1$s\">Learn more&lt;/a>&lt;/font>"</string>
strings.xml:3618:    <string name="APKTOOL_DUMMYVAL_0x7f120e4f">Precise location</string>
strings.xml:3662:    <string name="APKTOOL_DUMMYVAL_0x7f120e7b">Turn on location to continue the transfer.</string>
strings.xml:3663:    <string name="APKTOOL_DUMMYVAL_0x7f120e7c">Turn on location</string>
strings.xml:4099:    <string name="APKTOOL_DUMMYVAL_0x7f12102b">On your primary device, turn on WhatsApp contacts to start managing contacts from companion devices. Go to WhatsApp > Settings > Privacy > Contacts.</string>
strings.xml:4100:    <string name="APKTOOL_DUMMYVAL_0x7f12102c">Manage contacts from companions</string>
strings.xml:4145:    <string name="APKTOOL_DUMMYVAL_0x7f12105a">"Only contacts with a phone number can be synced. Syncing will add it to your primary's address book."</string>
strings.xml:4166:    <string name="APKTOOL_DUMMYVAL_0x7f121070">"You haven't selected any third-party apps"</string>
strings.xml:4167:    <string name="APKTOOL_DUMMYVAL_0x7f121071">New third-party chat</string>
strings.xml:4215:    <string name="APKTOOL_DUMMYVAL_0x7f1210a3">Connecting shares your contact details. If confirmed, you’ll be added to each other’s WhatsApp contacts.</string>
strings.xml:4221:    <string name="APKTOOL_DUMMYVAL_0x7f1210a9">Since you added WhatsApp to your Meta Account, you can connect with Instagram friends and be added to each other’s WhatsApp contacts.</string>
strings.xml:4224:    <string name="APKTOOL_DUMMYVAL_0x7f1210ac">Connecting adds you to each other’s WhatsApp contacts.</string>
strings.xml:4247:    <string name="APKTOOL_DUMMYVAL_0x7f1210c3">This business can see that you contacted them from find business. Your location stays private and is not seen by any businesses or WhatsApp.</string>
strings.xml:4273:    <string name="APKTOOL_DUMMYVAL_0x7f1210dd">%1$s was added to your WhatsApp contacts.</string>
strings.xml:4283:    <string name="APKTOOL_DUMMYVAL_0x7f1210e7">This person is already in your contacts.</string>
strings.xml:4335:    <string name="APKTOOL_DUMMYVAL_0x7f121119">Live location</string>
strings.xml:4351:    <string name="APKTOOL_DUMMYVAL_0x7f12112c">Sync contacts</string>
strings.xml:4352:    <string name="APKTOOL_DUMMYVAL_0x7f12112d">You won’t be able to find your friends and family unless you sync your contacts.</string>
strings.xml:4353:    <string name="APKTOOL_DUMMYVAL_0x7f12112e">You won’t be able to quickly call friends and family unless you sync your contacts.</string>
strings.xml:4354:    <string name="APKTOOL_DUMMYVAL_0x7f12112f">You won’t be able to quickly chat with friends and family unless you sync your contacts.</string>
strings.xml:4355:    <string name="APKTOOL_DUMMYVAL_0x7f121130">Your contacts aren’t synced</string>
strings.xml:4356:    <string name="APKTOOL_DUMMYVAL_0x7f121131">Sync contacts before calling</string>
strings.xml:4357:    <string name="APKTOOL_DUMMYVAL_0x7f121132">Sync contacts before chatting</string>
strings.xml:4371:    <string name="APKTOOL_DUMMYVAL_0x7f121141">New third-party chat</string>
strings.xml:4376:    <string name="APKTOOL_DUMMYVAL_0x7f121146">Share group invite links alongside contacts.</string>
strings.xml:4382:    <string name="APKTOOL_DUMMYVAL_0x7f12114c">No WhatsApp contacts</string>
strings.xml:4398:    <string name="APKTOOL_DUMMYVAL_0x7f12115c">Contacts on %1$s</string>
strings.xml:4399:    <string name="APKTOOL_DUMMYVAL_0x7f12115d">Contacts on WhatsApp</string>
strings.xml:4407:    <string name="APKTOOL_DUMMYVAL_0x7f121165">Other contacts</string>
strings.xml:4408:    <string name="APKTOOL_DUMMYVAL_0x7f121166">Other contacts</string>
strings.xml:4417:    <string name="APKTOOL_DUMMYVAL_0x7f121170">Add to contacts</string>
strings.xml:4482:    <string name="APKTOOL_DUMMYVAL_0x7f1211b5">Contacts</string>
strings.xml:4483:    <string name="APKTOOL_DUMMYVAL_0x7f1211b6">Share contacts and groups</string>
strings.xml:4484:    <string name="APKTOOL_DUMMYVAL_0x7f1211b7">Contacts help</string>
strings.xml:4485:    <string name="APKTOOL_DUMMYVAL_0x7f1211b8">Active contacts</string>
strings.xml:4487:    <string name="APKTOOL_DUMMYVAL_0x7f1211ba">"Couldn't add contacts"</string>
strings.xml:4492:    <string name="APKTOOL_DUMMYVAL_0x7f1211bf">Add to contacts</string>
strings.xml:4493:    <string name="APKTOOL_DUMMYVAL_0x7f1211c0">Added to your contacts</string>
strings.xml:4515:    <string name="APKTOOL_DUMMYVAL_0x7f1211d6">See all contacts</string>
strings.xml:4518:    <string name="APKTOOL_DUMMYVAL_0x7f1211d9">All contacts</string>
strings.xml:4523:    <string name="APKTOOL_DUMMYVAL_0x7f1211de">Add and manage contacts</string>
strings.xml:4524:    <string name="APKTOOL_DUMMYVAL_0x7f1211df">Contacts</string>
strings.xml:4525:    <string name="APKTOOL_DUMMYVAL_0x7f1211e0">Contacts</string>
strings.xml:4526:    <string name="APKTOOL_DUMMYVAL_0x7f1211e1">Contacts on WhatsApp</string>
strings.xml:4527:    <string name="APKTOOL_DUMMYVAL_0x7f1211e2">Contacts on WhatsApp</string>
strings.xml:4530:    <string name="APKTOOL_DUMMYVAL_0x7f1211e5">Contacts to send</string>
strings.xml:4709:    <string name="APKTOOL_DUMMYVAL_0x7f121286">Live location</string>
strings.xml:4734:    <string name="APKTOOL_DUMMYVAL_0x7f12129f">Live location</string>
strings.xml:4735:    <string name="APKTOOL_DUMMYVAL_0x7f1212a0">Location</string>
strings.xml:4744:    <string name="APKTOOL_DUMMYVAL_0x7f1212a9">Sent a location</string>
strings.xml:4748:    <string name="APKTOOL_DUMMYVAL_0x7f1212ad">Sharing live location</string>
strings.xml:4917:    <string name="APKTOOL_DUMMYVAL_0x7f121359">Current location marker</string>
strings.xml:4960:    <string name="APKTOOL_DUMMYVAL_0x7f121384">Add other members to contacts?</string>
strings.xml:5063:    <string name="APKTOOL_DUMMYVAL_0x7f1213ee">To make it harder for people to infer your location, calls on this device will be securely relayed through WhatsApp servers. This will reduce call quality.</string>
strings.xml:5064:    <string name="APKTOOL_DUMMYVAL_0x7f1213ef">Only contacts can add you to groups.</string>
strings.xml:5065:    <string name="APKTOOL_DUMMYVAL_0x7f1213f0">To help protect your IP address from being inferred by third-party websites, previews for the links you share in chats will no longer be generated.</string>
strings.xml:5067:    <string name="APKTOOL_DUMMYVAL_0x7f1213f2">Only contacts can see your last seen and online, profile picture, about, profile links and status.</string>
strings.xml:5253:    <string name="APKTOOL_DUMMYVAL_0x7f1214ae">"%1$s's contacts"</string>
strings.xml:5254:    <string name="APKTOOL_DUMMYVAL_0x7f1214af">"Your child's contacts"</string>
strings.xml:5255:    <string name="APKTOOL_DUMMYVAL_0x7f1214b0">"Messages from unknown contacts are stored in %1$s's Requests folder. Your parent PIN is required to view these chats."</string>
strings.xml:5256:    <string name="APKTOOL_DUMMYVAL_0x7f1214b1">"Messages from unknown contacts are stored in your child's Requests folder. Your parent PIN is required to view these chats."</string>
strings.xml:5438:    <string name="APKTOOL_DUMMYVAL_0x7f121562">To help protect your IP address from being inferred by third-party websites, previews for the links you share in chats will no longer be generated. &lt;a href=disable_link_previews_help>Learn more&lt;/a></string> [... omitted end of lon
strings.xml:5524:    <string name="APKTOOL_DUMMYVAL_0x7f1215b7">When turned on, all new individual chats will start with disappearing messages set to the duration you select. This setting will not affect your existing chats. &lt;br/>&lt;br/>It also does not apply to third-part [... omitted end of lo
strings.xml:5525:    <string name="APKTOOL_DUMMYVAL_0x7f1215b8">Start new chats with a disappearing message timer. This will not affect your existing chats. &lt;br/>&lt;br/>It also does not apply to third-party chats, because disappearing messages are not supported in third-pa [... omitted end of lo
strings.xml:5527:    <string name="APKTOOL_DUMMYVAL_0x7f1215ba">This does not affect your existing chats. Apply this message timer to existing chats &lt;a href=\"%s\">by selecting them&lt;/a>.&lt;br/>&lt;br/>It also does not apply to third-party chats, because disappearing mes [... omitted end of lo
strings.xml:5566:    <string name="APKTOOL_DUMMYVAL_0x7f1215e3">Location</string>
strings.xml:5727:    <string name="APKTOOL_DUMMYVAL_0x7f121687">live location shared</string>
strings.xml:5728:    <string name="APKTOOL_DUMMYVAL_0x7f121688">location: %s</string>
strings.xml:5828:    <string name="APKTOOL_DUMMYVAL_0x7f1216ef">To sync your contacts, allow access on the next screen.</string>
strings.xml:5832:    <string name="APKTOOL_DUMMYVAL_0x7f1216f2">"To start a chat with someone on a third-party app, tap %s 
strings.xml:5834:You will need to know the third-party app name and their user ID."</string>
strings.xml:6161:    <string name="APKTOOL_DUMMYVAL_0x7f12183d">"Our partners' systems are temporarily down. Please wait before trying again."</string>
strings.xml:6202:    <string name="APKTOOL_DUMMYVAL_0x7f121865">Family, friends and other people who use our service may have uploaded your number to WhatsApp. If so, they can see you in their contacts after you sign up. &lt;a href=\"learn-more\">Learn more&lt;/a> &lt;br/>&lt; [... omitted end of lo
strings.xml:6206:    <string name="APKTOOL_DUMMYVAL_0x7f121869">Family, friends and other people who use our service may have uploaded your number to WhatsApp. If so, they can see you in their contacts after you sign up. &lt;a href=\"learn-more\">Learn more&lt;/a> &lt;br/>&lt; [... omitted end of lo
strings.xml:6212:    <string name="APKTOOL_DUMMYVAL_0x7f12186f">Add location</string>
strings.xml:6261:    <string name="APKTOOL_DUMMYVAL_0x7f12189e">Copy location</string>
strings.xml:6351:    <string name="APKTOOL_DUMMYVAL_0x7f1218f6">"You can only see guests in your contacts or who you've messaged on WhatsApp."</string>
strings.xml:6422:    <string name="APKTOOL_DUMMYVAL_0x7f12193e">Event Location Address: %s</string>
strings.xml:6423:    <string name="APKTOOL_DUMMYVAL_0x7f12193f">Location copied</string>
strings.xml:6424:    <string name="APKTOOL_DUMMYVAL_0x7f121940">Event Location Name: %s</string>
strings.xml:6425:    <string name="APKTOOL_DUMMYVAL_0x7f121941">Event Location Point: %s</string>
strings.xml:6426:    <string name="APKTOOL_DUMMYVAL_0x7f121942">Respond to see location</string>
strings.xml:6427:    <string name="APKTOOL_DUMMYVAL_0x7f121943">Location</string>
strings.xml:6429:    <string name="APKTOOL_DUMMYVAL_0x7f121945">Respond to see the event location and more.</string>
strings.xml:6476:    <string name="APKTOOL_DUMMYVAL_0x7f121974">Remove location</string>
strings.xml:6521:    <string name="APKTOOL_DUMMYVAL_0x7f1219a1">Event date and location have been updated.</string>
strings.xml:6523:    <string name="APKTOOL_DUMMYVAL_0x7f1219a3">Event date, time and location have been updated.</string>
strings.xml:6524:    <string name="APKTOOL_DUMMYVAL_0x7f1219a4">Event location has been updated.</string>
strings.xml:6527:    <string name="APKTOOL_DUMMYVAL_0x7f1219a7">Event time and location have been updated.</string>
strings.xml:6735:    <string name="APKTOOL_DUMMYVAL_0x7f121a7c">"Couldn't add to favorites. Only contacts can be added."</string>
strings.xml:6737:    <string name="APKTOOL_DUMMYVAL_0x7f121a7e">"Favorite your contacts or groups to instantly call them with one tap, just like speed dial.
strings.xml:6776:    <string name="APKTOOL_DUMMYVAL_0x7f121aa7">Contacts</string>
strings.xml:6791:    <string name="APKTOOL_DUMMYVAL_0x7f121ab6">Non-contacts</string>
strings.xml:6798:    <string name="APKTOOL_DUMMYVAL_0x7f121abd">Third-party chats</string>
strings.xml:6829:    <string name="APKTOOL_DUMMYVAL_0x7f121add">This status will be sent to your contacts.</string>
strings.xml:6875:    <string name="APKTOOL_DUMMYVAL_0x7f121b0b">Change if contacts or non-contacts can add you to groups in &lt;a href=\"privacy-settings\">privacy settings&lt;/a>.</string>
strings.xml:6890:    <string name="APKTOOL_DUMMYVAL_0x7f121b1a">Profile name and photo are not available in third-party chats. Before sharing personal information, be sure you know who this person is.</string>
strings.xml:6896:    <string name="APKTOOL_DUMMYVAL_0x7f121b20">"When calling or messaging with someone who isn't saved in your contacts, you can take any of these actions. They won't be notified if you do."</string>
strings.xml:6998:    <string name="APKTOOL_DUMMYVAL_0x7f121b86">Third-party chats and more moved here.</string>
strings.xml:6999:    <string name="APKTOOL_DUMMYVAL_0x7f121b87">Third-party chats have moved here.</string>
strings.xml:7025:    <string name="APKTOOL_DUMMYVAL_0x7f121ba1">Third-party chats settings</string>
strings.xml:7070:    <string name="APKTOOL_DUMMYVAL_0x7f121bd2">From contacts</string>
strings.xml:7208:    <string name="APKTOOL_DUMMYVAL_0x7f121c5d">Location</string>
strings.xml:7276:    <string name="APKTOOL_DUMMYVAL_0x7f121ca7">To find and restore your backup from Google storage, allow WhatsApp to access your contacts.</string>
strings.xml:7277:    <string name="APKTOOL_DUMMYVAL_0x7f121ca8">To find and restore your backup from Google storage, allow WhatsApp to access your contacts, photos and other media.</string>
strings.xml:7467:    <string name="APKTOOL_DUMMYVAL_0x7f121d66">Show location settings?</string>
strings.xml:7516:    <string name="APKTOOL_DUMMYVAL_0x7f121d97">My contacts except…</string>
strings.xml:7519:    <string name="APKTOOL_DUMMYVAL_0x7f121d9a">"You were added by someone who's not in your contacts"</string>
strings.xml:7520:    <string name="APKTOOL_DUMMYVAL_0x7f121d9b">"You were added by someone who's not in your contacts."</string>
strings.xml:7554:    <string name="APKTOOL_DUMMYVAL_0x7f121dbd">Select contacts to call</string>
strings.xml:7634:    <string name="APKTOOL_DUMMYVAL_0x7f121e0e">"You've added too many contacts to groups too quickly. Try again later."</string>
strings.xml:7682:    <string name="APKTOOL_DUMMYVAL_0x7f121e3f">&lt;b>Message history sent by %1$s, someone not in your contacts.&lt;/b> History may not always be accurate or complete. &lt;b>&lt;a href=\"%2$s\">Learn More.&lt;/a>&lt;/b></string>
strings.xml:7683:    <string name="APKTOOL_DUMMYVAL_0x7f121e40">&lt;b>Message history sent by someone not in your contacts.&lt;/b> History may not always be accurate or complete. &lt;b>&lt;a href=\"%1$s\">Learn More.&lt;/a>&lt;/b></string>
strings.xml:7852:    <string name="APKTOOL_DUMMYVAL_0x7f121ee7">Contacts</string>
strings.xml:7920:    <string name="APKTOOL_DUMMYVAL_0x7f121f2b">You can only be added to third-party chats by people who either use or have selected the same messaging app. Learn more</string>
strings.xml:7921:    <string name="APKTOOL_DUMMYVAL_0x7f121f2c">Third-party groups</string>
strings.xml:7925:    <string name="APKTOOL_DUMMYVAL_0x7f121f30">"People will see you as %1$s if you aren't in their Contacts."</string>
strings.xml:8208:    <string name="APKTOOL_DUMMYVAL_0x7f12204e">This status will be shared with your contacts.</string>
strings.xml:8302:    <string name="APKTOOL_DUMMYVAL_0x7f1220ac">Your contacts</string>
strings.xml:8432:    <string name="APKTOOL_DUMMYVAL_0x7f122139">How Meta works with selected partners to improve AI responses</string>
strings.xml:8465:    <string name="APKTOOL_DUMMYVAL_0x7f12215a">Call, message or send photos to your WhatsApp contacts hands-free.</string>
strings.xml:8466:    <string name="APKTOOL_DUMMYVAL_0x7f12215b">Call, message, send photos to contacts, and make payments hands-free.</string>
strings.xml:8593:    <string name="APKTOOL_DUMMYVAL_0x7f1221e6">Third-party chats</string>
strings.xml:8594:    <string name="APKTOOL_DUMMYVAL_0x7f1221e7">To create this third-party group, you need to select at least one %1$s user.</string>
strings.xml:8596:    <string name="APKTOOL_DUMMYVAL_0x7f1221e9">%1$s was added to your %2$s contacts on WhatsApp.</string>
strings.xml:8598:    <string name="APKTOOL_DUMMYVAL_0x7f1221eb">Make sure everyone you add to this group has third-party chats enabled.</string>
strings.xml:8600:    <string name="APKTOOL_DUMMYVAL_0x7f1221ed">Third-Party Group</string>
strings.xml:8606:    <string name="APKTOOL_DUMMYVAL_0x7f1221f3">Allow people to message you in WhatsApp from selected third-party apps.</string>
strings.xml:8630:    <string name="APKTOOL_DUMMYVAL_0x7f12220b">No contacts to invite</string>
strings.xml:8631:    <string name="APKTOOL_DUMMYVAL_0x7f12220c">Followers who are contacts</string>
strings.xml:8652:    <string name="APKTOOL_DUMMYVAL_0x7f122221">Only contacts who have you in their address book will receive your invite.</string>
strings.xml:9233:    <string name="APKTOOL_DUMMYVAL_0x7f12246a">Live Location</string>
strings.xml:9234:    <string name="APKTOOL_DUMMYVAL_0x7f12246b">Sharing live location is not available on this device. Share live location on your primary phone.</string>
strings.xml:9237:    <string name="APKTOOL_DUMMYVAL_0x7f12246e">Live location ended</string>
strings.xml:9248:    <string name="APKTOOL_DUMMYVAL_0x7f122479">"Members in this chat will see your location in real time. This feature shares your location for the duration you choose even if you're not using the app. You can stop sharing at any time. &lt;a href=\"%s\">Learn  [... omitted end of lo
strings.xml:9249:    <string name="APKTOOL_DUMMYVAL_0x7f12247a">"Can't update your location. Tap to fix."</string>
strings.xml:9252:    <string name="APKTOOL_DUMMYVAL_0x7f12247d">No one is currently sharing live location</string>
strings.xml:9253:    <string name="APKTOOL_DUMMYVAL_0x7f12247e">"You aren't sharing live location in any chats"</string>
strings.xml:9254:    <string name="APKTOOL_DUMMYVAL_0x7f12247f">Live Location not available</string>
strings.xml:9255:    <string name="APKTOOL_DUMMYVAL_0x7f122480">Live location is not available on this device. View location on your primary phone.</string>
strings.xml:9257:    <string name="APKTOOL_DUMMYVAL_0x7f122482">Live location requires background location. You can manage this in your device settings.</string>
strings.xml:9261:    <string name="APKTOOL_DUMMYVAL_0x7f122486">Tap to share your live location</string>
strings.xml:9263:    <string name="APKTOOL_DUMMYVAL_0x7f122488">Share live location</string>
strings.xml:9264:    <string name="APKTOOL_DUMMYVAL_0x7f122489">Live location ended</string>
strings.xml:9268:    <string name="APKTOOL_DUMMYVAL_0x7f12248d">Stop sharing live location with all chats?</string>
strings.xml:9271:    <string name="APKTOOL_DUMMYVAL_0x7f122490">View live location</string>
strings.xml:9287:    <string name="APKTOOL_DUMMYVAL_0x7f12249e">Location</string>
strings.xml:9288:    <string name="APKTOOL_DUMMYVAL_0x7f12249f">Edit location</string>
strings.xml:9291:    <string name="APKTOOL_DUMMYVAL_0x7f1224a2">Location marker</string>
strings.xml:9296:    <string name="APKTOOL_DUMMYVAL_0x7f1224a7">To search for nearby places, turn on location services in your device settings.</string>
strings.xml:9298:    <string name="APKTOOL_DUMMYVAL_0x7f1224a9">Your live location won’t be shared.</string>
strings.xml:9300:    <string name="APKTOOL_DUMMYVAL_0x7f1224ab">Businesses near your location</string>
strings.xml:9446:    <string name="APKTOOL_DUMMYVAL_0x7f122559">Sync your contacts to instantly find people you know. Your contacts are stored securely, and you can change this setting anytime.</string>
strings.xml:9447:    <string name="APKTOOL_DUMMYVAL_0x7f12255a">Your contacts are not synced</string>
strings.xml:9448:    <string name="APKTOOL_DUMMYVAL_0x7f12255b">Sync contacts</string>
strings.xml:9449:    <string name="APKTOOL_DUMMYVAL_0x7f12255c">Sync your contacts</string>
strings.xml:9494:    <string name="APKTOOL_DUMMYVAL_0x7f122589">May include location and other information</string>
strings.xml:9511:    <string name="APKTOOL_DUMMYVAL_0x7f12259a">Location</string>
strings.xml:9611:    <string name="APKTOOL_DUMMYVAL_0x7f1225fc">"Contacts can see their own mention when they see your status. They can't see other mentions."</string>
strings.xml:9629:    <string name="APKTOOL_DUMMYVAL_0x7f12260e">Contacts</string>
strings.xml:9642:    <string name="APKTOOL_DUMMYVAL_0x7f12261c">Refresh contacts</string>
strings.xml:10055:    <string name="APKTOOL_DUMMYVAL_0x7f1227be">You can search for results from third-party sticker and GIF providers and WhatsApp. &lt;a href=\"%1$s\"> Learn more&lt;/a></string>
strings.xml:10157:    <string name="APKTOOL_DUMMYVAL_0x7f122822">Move to your location</string>
strings.xml:10213:    <string name="APKTOOL_DUMMYVAL_0x7f12285b">"Can't send these contacts because they're too large."</string>
strings.xml:10312:    <string name="APKTOOL_DUMMYVAL_0x7f1228c0">Shared with all of your contacts</string>
strings.xml:10344:    <string name="APKTOOL_DUMMYVAL_0x7f1228e0">Send Location</string>
strings.xml:10367:    <string name="APKTOOL_DUMMYVAL_0x7f1228f7">Contacts</string>
strings.xml:10374:    <string name="APKTOOL_DUMMYVAL_0x7f1228fe">Call selected WhatsApp contacts hands-free, just by asking neptune.</string>
strings.xml:10375:    <string name="APKTOOL_DUMMYVAL_0x7f1228ff">"By linking with %1$s and selecting contacts, you agree to share your WhatsApp contact information with %2$s to enable WhatsApp calling on %3$s internal testing in accordance with &lt;a href=\"shared-device-privac [... omitted end of l
strings.xml:10376:    <string name="APKTOOL_DUMMYVAL_0x7f122900">Select contacts</string>
strings.xml:10380:    <string name="APKTOOL_DUMMYVAL_0x7f122903">Make and receive calls from these contacts on your Neptune. Change them anytime in Linked Devices > Neptune > Contacts.</string>
strings.xml:10382:    <string name="APKTOOL_DUMMYVAL_0x7f122905">Select contacts</string>
strings.xml:10384:    <string name="APKTOOL_DUMMYVAL_0x7f122907">These are the contacts you shared when you linked a Neptune device before. Continue to use the same list here, or reselect to change it on all your Neptune devices.</string>
strings.xml:10385:    <string name="APKTOOL_DUMMYVAL_0x7f122908">"By linking with %1$s and selecting contacts, you agree to share your WhatsApp contact information with %2$s to enable WhatsApp calling on %3$s internal testing in accordance with &lt;a href=\"shared-device-privac [... omitted end of l
strings.xml:10386:    <string name="APKTOOL_DUMMYVAL_0x7f122909">Reselect contacts</string>
strings.xml:10387:    <string name="APKTOOL_DUMMYVAL_0x7f12290a">Review your Neptune contacts</string>
strings.xml:10396:    <string name="APKTOOL_DUMMYVAL_0x7f122913">Unstable connection. Try a new location.</string>
strings.xml:10409:    <string name="APKTOOL_DUMMYVAL_0x7f122920">Contacts on WhatsApp</string>
strings.xml:10437:    <string name="APKTOOL_DUMMYVAL_0x7f12293d">%s was added to your contacts</string>
strings.xml:10474:    <string name="APKTOOL_DUMMYVAL_0x7f122963">Some updates shared by this channel have been reported by a third party for not following local advertising laws.</string>
strings.xml:10475:    <string name="APKTOOL_DUMMYVAL_0x7f122964">"Your content was reported by a third party for not following local laws, which doesn't follow our &lt;a href=\"%s\">Channels Guidelines&lt;/a>. As a result, action was taken."</string>
strings.xml:10477:    <string name="APKTOOL_DUMMYVAL_0x7f122966">Some updates shared by this channel have been reported by a third party for not following local defamation laws.</string>
strings.xml:10478:    <string name="APKTOOL_DUMMYVAL_0x7f122967">Some updates shared by this channel have been reported by a third party for not following local laws or rights.</string>
strings.xml:10479:    <string name="APKTOOL_DUMMYVAL_0x7f122968">Some updates shared by this channel have been reported by a third party for not following local hate speech laws.</string>
strings.xml:10480:    <string name="APKTOOL_DUMMYVAL_0x7f122969">Some updates shared by this channel have been reported by a third party for not following local insult laws.</string>
strings.xml:10481:    <string name="APKTOOL_DUMMYVAL_0x7f12296a">Some updates shared by this channel have been reported by a third party for not following local privacy laws.</string>
strings.xml:10683:    <string name="APKTOOL_DUMMYVAL_0x7f122a34">You can only view individual followers who are contacts.</string>
strings.xml:10684:    <string name="APKTOOL_DUMMYVAL_0x7f122a35">You can only search for individual followers who are your contacts.</string>
strings.xml:10685:    <string name="APKTOOL_DUMMYVAL_0x7f122a36">You can only search for contacts from your first 5,000 followers.</string>
strings.xml:10686:    <string name="APKTOOL_DUMMYVAL_0x7f122a37">You can only view contacts from your first 5,000 followers.</string>
strings.xml:10688:    <string name="APKTOOL_DUMMYVAL_0x7f122a39">You can only view individual followers who are contacts or admins.</string>
strings.xml:10709:    <string name="APKTOOL_DUMMYVAL_0x7f122a4e">Your content was reported by a third party for infringing their intellectual property rights, which doesn’t follow our &lt;a href=\"%1$s\">Channels Guidelines&lt;/a>. As a result, action was taken.</string>
strings.xml:10814:    <string name="APKTOOL_DUMMYVAL_0x7f122ab7">You can only view individual reactions from contacts.</string>
strings.xml:10815:    <string name="APKTOOL_DUMMYVAL_0x7f122ab8">No contacts have reacted yet</string>
strings.xml:10817:    <string name="APKTOOL_DUMMYVAL_0x7f122aba">Contacts</string>
strings.xml:11012:    <string name="APKTOOL_DUMMYVAL_0x7f122b7d">Contacts</string>
strings.xml:11015:    <string name="APKTOOL_DUMMYVAL_0x7f122b80">Not in your contacts</string>
strings.xml:11043:    <string name="APKTOOL_DUMMYVAL_0x7f122b9c">No chats with contacts</string>
strings.xml:11044:    <string name="APKTOOL_DUMMYVAL_0x7f122b9d">No contacts excluded</string>
strings.xml:11045:    <string name="APKTOOL_DUMMYVAL_0x7f122b9e">No contacts selected</string>
strings.xml:11065:    <string name="APKTOOL_DUMMYVAL_0x7f122bb2">No contacts</string>
strings.xml:11104:    <string name="APKTOOL_DUMMYVAL_0x7f122bd9">No third-party chats</string>
strings.xml:11130:    <string name="APKTOOL_DUMMYVAL_0x7f122bf3">"%1$s was added to your contacts but isn't on WhatsApp. We'll send an invite for you."</string>
strings.xml:11131:    <string name="APKTOOL_DUMMYVAL_0x7f122bf4">"%1$s was added to your contacts but isn't on WhatsApp. We'll send a one-time SMS invite for you."</string>
strings.xml:11146:    <string name="APKTOOL_DUMMYVAL_0x7f122c03">Not in your contacts</string>
strings.xml:11231:    <string name="APKTOOL_DUMMYVAL_0x7f122c58">Location sharing in progress</string>
strings.xml:11232:    <string name="APKTOOL_DUMMYVAL_0x7f122c59">Open WhatsApp to resume live location sharing</string>
strings.xml:11236:    <string name="APKTOOL_DUMMYVAL_0x7f122c5d">WhatsApp Live Location</string>
strings.xml:11237:    <string name="APKTOOL_DUMMYVAL_0x7f122c5e">Live location sharing stopped</string>
strings.xml:11250:    <string name="APKTOOL_DUMMYVAL_0x7f122c6b">"You'll get notifications only for @mentions, replies, messages from contacts and more for larger groups. Change in &lt;b>&lt;a href=\"%s\">group settings&lt;/a>&lt;/b>."</string>
strings.xml:11281:    <string name="APKTOOL_DUMMYVAL_0x7f122c8a">Not in your contacts</string>
strings.xml:11502:    <string name="APKTOOL_DUMMYVAL_0x7f122d69">Orders aren’t available in %1$s’s location.</string>
strings.xml:11561:    <string name="APKTOOL_DUMMYVAL_0x7f122da8">For additional security, your contacts will be fully restored later. &lt;a href=\"learn-more\">Learn more&lt;/a></string>
strings.xml:11562:    <string name="APKTOOL_DUMMYVAL_0x7f122da9">"Can't restore WhatsApp contacts. &lt;a href=\"learn-more\">Learn more&lt;/a>"</string>
strings.xml:11569:    <string name="APKTOOL_DUMMYVAL_0x7f122db0">Back up contacts</string>
strings.xml:11571:    <string name="APKTOOL_DUMMYVAL_0x7f122db2">Blocked accounts, WhatsApp contacts</string>
strings.xml:11572:    <string name="APKTOOL_DUMMYVAL_0x7f122db3">Contacts</string>
strings.xml:11573:    <string name="APKTOOL_DUMMYVAL_0x7f122db4">To stop syncing this contact to your phone, you need to turn on WhatsApp contacts. Your contacts will be saved to your WhatsApp account to manage them across devices.</string>
strings.xml:11574:    <string name="APKTOOL_DUMMYVAL_0x7f122db5">Turn on WhatsApp contacts?</string>
strings.xml:11576:    <string name="APKTOOL_DUMMYVAL_0x7f122db7">Contacts</string>
strings.xml:11577:    <string name="APKTOOL_DUMMYVAL_0x7f122db8">WhatsApp contacts is turned on. Contacts can be managed across devices and restored.</string>
strings.xml:11578:    <string name="APKTOOL_DUMMYVAL_0x7f122db9">"Your contacts will be saved to your WhatsApp account.
strings.xml:11581:    <string name="APKTOOL_DUMMYVAL_0x7f122dba">Turn on WhatsApp contacts?</string>
strings.xml:11583:    <string name="APKTOOL_DUMMYVAL_0x7f122dbc">"WhatsApp contacts is turned off. Contacts can't be managed across devices or restored."</string>
strings.xml:11584:    <string name="APKTOOL_DUMMYVAL_0x7f122dbd">Save all contacts to phone</string>
strings.xml:11585:    <string name="APKTOOL_DUMMYVAL_0x7f122dbe">&lt;b>This will delete all contacts saved to your WhatsApp account. &lt;/b></string>
strings.xml:11586:    <string name="APKTOOL_DUMMYVAL_0x7f122dbf">"You can still save contacts to your phone so you don't lose them."</string>
strings.xml:11587:    <string name="APKTOOL_DUMMYVAL_0x7f122dc0">"You won't be able to manage contacts across your linked devices. Contacts won't be automatically restored if you change phones or reinstall WhatsApp.&lt;br/>&lt;br/>"</string>
strings.xml:11588:    <string name="APKTOOL_DUMMYVAL_0x7f122dc1">Usernames and contacts added to third-party chats will not save to your phone.</string>
strings.xml:11590:    <string name="APKTOOL_DUMMYVAL_0x7f122dc3">&lt;b>This will delete all contacts saved to your WhatsApp account.&lt;/b></string>
strings.xml:11591:    <string name="APKTOOL_DUMMYVAL_0x7f122dc4">"&lt;br/>&lt;br/>You won't be able to manage contacts across your linked devices. Contacts won't be automatically restored if you change phones or reinstall WhatsApp."</string>
strings.xml:11592:    <string name="APKTOOL_DUMMYVAL_0x7f122dc5">Delete all WhatsApp contacts?</string>
strings.xml:11612:    <string name="APKTOOL_DUMMYVAL_0x7f122dda">Contacts are saved to your WhatsApp account to manage them across devices. &lt;a href=backup-contacts-learn-more>Learn more&lt;/a></string>
strings.xml:11613:    <string name="APKTOOL_DUMMYVAL_0x7f122ddb">WhatsApp contacts</string>
strings.xml:11615:    <string name="APKTOOL_DUMMYVAL_0x7f122ddd">"Some contacts that are used for your privacy settings aren't fully restored. &lt;a href=\"learn-more\">Learn more&lt;/a>"</string>
strings.xml:11770:    <string name="APKTOOL_DUMMYVAL_0x7f122e7f">%1$s deleted %2$s from their contacts</string>
strings.xml:11771:    <string name="APKTOOL_DUMMYVAL_0x7f122e80">Your child deleted %1$s from their contacts</string>
strings.xml:11834:    <string name="APKTOOL_DUMMYVAL_0x7f122ebf">Add %1$s to your contacts</string>
strings.xml:11835:    <string name="APKTOOL_DUMMYVAL_0x7f122ec0">Add your child to your contacts</string>
strings.xml:11836:    <string name="APKTOOL_DUMMYVAL_0x7f122ec1">Add your teen to your contacts</string>
```

