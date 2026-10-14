# Pattern scan: work/gphotos/jdex

## Code categories (library packages excluded)

### installed_apps — 40 hits in 35 files

- `classes2:defpackage/bsql.java` (3)
- `classes5:defpackage/anll.java` (2)
- `classes6:defpackage/bfzr.java` (2)
- `classes7:defpackage/cbci.java` (2)
- `classes:defpackage/vpf.java` (1)
- `classes:defpackage/czq.java` (1)
- `classes:defpackage/kwn.java` (1)
- `classes:defpackage/qrt.java` (1)
- `classes2:defpackage/btcp.java` (1)
- `classes2:defpackage/btbg.java` (1)
- `classes2:defpackage/aism.java` (1)
- `classes2:defpackage/asii.java` (1)

```
classes:defpackage/vpf.java:40:                        optionalEmpty = Build.VERSION.SDK_INT >= 33 ? Optional.of(ExternalSyntheticApiModelOutline0.m(packageManager, "com.google.android.mediaprovider", ExternalSyntheticApiModelOutline0.m(1073741824L))) : Optional.of(packageManager.getPackage [... omi
classes:defpackage/czq.java:137:                List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(dbh.a(), 0);
classes:defpackage/kwn.java:1486:        Iterator<ResolveInfo> it = context.getPackageManager().queryIntentActivities(intentPutExtra, 0).iterator();
classes:defpackage/qrt.java:39:                List<ResolveInfo> listQueryIntentActivities = packageManager.queryIntentActivities(new Intent("android.media.action.STILL_IMAGE_CAMERA"), 0);
classes2:defpackage/btcp.java:160:        } else if (!((Activity) this.a).getPackageManager().queryIntentActivities(data, 0).isEmpty()) {
classes2:defpackage/btbg.java:191:            PackageInfo packageInfo = context.getPackageManager().getPackageInfo("com.google.android.gms", 64);
classes2:defpackage/aism.java:27:            List<ResolveInfo> listQueryIntentActivities = packageManager.queryIntentActivities(intent, 65536);
classes2:defpackage/asii.java:23:            for (ResolveInfo resolveInfo : packageManager.queryIntentActivities(intent, 0)) {
classes2:defpackage/cabu.java:129:        List<ResolveInfo> listM = Build.VERSION.SDK_INT >= 33 ? ExternalSyntheticApiModelOutline0.m(context.getPackageManager(), intent, ExternalSyntheticApiModelOutline0.m(0L)) : context.getPackageManager().queryIntentActivities(intent, 0);
classes2:defpackage/akks.java:18:            return Build.VERSION.SDK_INT >= 28 ? ExternalSyntheticApiModelOutline1.m(context.getPackageManager().getPackageInfo("com.google.android.googlequicksearchbox", 0)) : r2.versionCode;
classes2:defpackage/aebs.java:118:        return context.getPackageManager().queryIntentActivities(intent, 65536);
classes2:defpackage/brvi.java:130:                        packageInfo = ((bwvw) this.a).b.getPackageManager().getPackageInfo("com.android.chrome", 0);
```

### usage_stats — 8 hits in 3 files

- `classes4:defpackage/ubk.java` (3)
- `classes5:defpackage/ahlp.java` (3)
- `classes:defpackage/vft.java` (2)

```
classes:defpackage/vft.java:4:import android.app.usage.UsageStatsManager;
classes:defpackage/vft.java:57:                int iM = ExternalSyntheticApiModelOutline1.m((UsageStatsManager) context.getSystemService("usagestats"));
classes4:defpackage/ubk.java:3:import android.app.usage.UsageStatsManager;
classes4:defpackage/ubk.java:55:        Object systemService = context.getSystemService("usagestats");
classes4:defpackage/ubk.java:58:            int iM = ExternalSyntheticApiModelOutline1.m((UsageStatsManager) systemService);
classes5:defpackage/ahlp.java:3:import android.app.usage.UsageStatsManager;
classes5:defpackage/ahlp.java:48:        UsageStatsManager usageStatsManager;
classes5:defpackage/ahlp.java:92:                if (Build.VERSION.SDK_INT >= 28 && (usageStatsManager = (UsageStatsManager) context.getSystemService(UsageStatsManager.class)) != null) {
```

### clipboard — 4 hits in 4 files

- `classes:defpackage/kn.java` (1)
- `classes:defpackage/fsd.java` (1)
- `classes3:defpackage/dhy.java` (1)
- `classes4:defpackage/wzq.java` (1)

```
classes:defpackage/kn.java:182:            ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
classes:defpackage/fsd.java:16:        ClipData primaryClip = this.a.a().getPrimaryClip();
classes3:defpackage/dhy.java:205:        boolean zHasPrimaryClip = fsc.b(fsdVar).hasPrimaryClip();
classes4:defpackage/wzq.java:30:        if (d(context).hasPrimaryClip()) {
```

### contacts — 22 hits in 9 files

- `classes7:defpackage/cbob.java` (4)
- `classes:defpackage/mli.java` (3)
- `classes7:defpackage/cboa.java` (3)
- `classes2:defpackage/bygh.java` (2)
- `classes4:defpackage/yml.java` (2)
- `classes7:defpackage/cawe.java` (2)
- `classes7:defpackage/cavs.java` (2)
- `classes7:defpackage/cboy.java` (2)
- `classes7:defpackage/cbon.java` (2)

```
classes:defpackage/mli.java:7:import android.provider.ContactsContract;
classes:defpackage/mli.java:29:        return ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uri, true);
classes:defpackage/mli.java:46:            Uri uriLookupContact = ContactsContract.Contacts.lookupContact(contentResolver, uri);
classes2:defpackage/bygh.java:7:import android.provider.ContactsContract;
classes2:defpackage/bygh.java:383:                Uri uriBuild = ContactsContract.CommonDataKinds.Email.CONTENT_FILTER_URI.buildUpon().appendPath(cbmtVar.b).appendQueryParameter("directory", String.valueOf(cbolVar.b)).appendQueryParameter("limit", String.valueOf(cbfhVar.e)).appendQueryParamete [... 
classes4:defpackage/yml.java:7:import android.provider.ContactsContract;
classes4:defpackage/yml.java:27:            yqgVar.b(ContactsContract.Contacts.CONTENT_URI);
classes7:defpackage/cawe.java:15:import android.provider.ContactsContract;
classes7:defpackage/cawe.java:126:            Uri lookupUri = ContactsContract.Contacts.getLookupUri(Long.parseLong(str), str2);
classes7:defpackage/cavs.java:5:import android.provider.ContactsContract;
classes7:defpackage/cavs.java:34:        Uri uriBuild = ContactsContract.Data.CONTENT_URI.buildUpon().appendQueryParameter("android.provider.extra.ADDRESS_BOOK_INDEX", "true").build();
classes7:defpackage/cboy.java:4:import android.provider.ContactsContract;
```

### call_log — 0 hits in 0 files


```
```

### sms — 0 hits in 0 files


```
```

### location — 2 hits in 2 files

- `classes:defpackage/qfx.java` (1)
- `classes6:defpackage/bbhn.java` (1)

```
classes:defpackage/qfx.java:985:                return ((LocationManager) obj).getLastKnownLocation(str);
classes6:defpackage/bbhn.java:107:        e = byij.d("LocationClient.requestLocationUpdates");
```

### wifi_bt_scan — 0 hits in 0 files


```
```

### device_ids — 31 hits in 19 files

- `classes:android/support/v7/widget/RecyclerView.java` (6)
- `classes:defpackage/gtz.java` (4)
- `classes:androidx/core/widget/NestedScrollView.java` (3)
- `classes:defpackage/fsr.java` (2)
- `classes2:defpackage/bsat.java` (2)
- `classes:defpackage/gz.java` (1)
- `classes:defpackage/gs.java` (1)
- `classes2:defpackage/bulr.java` (1)
- `classes2:defpackage/bvzn.java` (1)
- `classes2:defpackage/bwur.java` (1)
- `classes2:defpackage/bsno.java` (1)
- `classes3:defpackage/hf.java` (1)

```
classes:androidx/core/widget/NestedScrollView.java:568:            O().at(motionEvent.getDeviceId(), motionEvent.getSource(), i3, scrollY2);
classes:androidx/core/widget/NestedScrollView.java:579:                    O().as(motionEvent.getDeviceId(), motionEvent.getSource(), i3, z2);
classes:androidx/core/widget/NestedScrollView.java:588:                O().as(motionEvent.getDeviceId(), motionEvent.getSource(), i3, i8);
classes:android/support/v7/widget/RecyclerView.java:2078:                bc().at(motionEvent.getDeviceId(), motionEvent.getSource(), i3, i6);
classes:android/support/v7/widget/RecyclerView.java:2081:                bc().at(motionEvent.getDeviceId(), motionEvent.getSource(), i4, i7);
classes:android/support/v7/widget/RecyclerView.java:2099:                    bc().as(motionEvent.getDeviceId(), motionEvent.getSource(), i3, true);
classes:android/support/v7/widget/RecyclerView.java:2106:                        bc().as(motionEvent.getDeviceId(), motionEvent.getSource(), i3, false);
classes:android/support/v7/widget/RecyclerView.java:2113:                            bc().as(motionEvent.getDeviceId(), motionEvent.getSource(), i4, true);
classes:android/support/v7/widget/RecyclerView.java:2121:                                bc().as(motionEvent.getDeviceId(), motionEvent.getSource(), i4, false);
classes:defpackage/fsr.java:1879:            MotionEvent motionEventA = Build.VERSION.SDK_INT >= 34 ? fua.a(downTime, j, i, pointerCount, pointerPropertiesArr, pointerCoordsArr, motionEvent.getMetaState(), buttonState, motionEvent.getXPrecision(), motionEvent.getYPrecision(), motionEvent.getD [... o
classes:defpackage/fsr.java:2673:            motionEvent.getDeviceId();
classes:defpackage/gz.java:81:        menuM.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
```

### gsf_id — 2 hits in 1 files

- `classes2:defpackage/buby.java` (2)

```
classes2:defpackage/buby.java:9:    public static final Uri a = Uri.parse("content://com.google.android.gsf.gservices");
classes2:defpackage/buby.java:10:    public static final Uri b = Uri.parse("content://com.google.android.gsf.gservices/prefix");
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

### accounts — 13 hits in 13 files

- `classes2:defpackage/bvql.java` (1)
- `classes2:defpackage/bvvp.java` (1)
- `classes2:defpackage/bxes.java` (1)
- `classes2:defpackage/byfw.java` (1)
- `classes2:defpackage/ccmz.java` (1)
- `classes2:defpackage/bulx.java` (1)
- `classes2:defpackage/bvvo.java` (1)
- `classes2:defpackage/cadw.java` (1)
- `classes7:defpackage/cdjr.java` (1)
- `classes7:defpackage/bqzm.java` (1)
- `classes7:defpackage/bunv.java` (1)
- `classes7:defpackage/bqyv.java` (1)

```
classes2:defpackage/bvql.java:647:        this.a = AccountManager.get(context);
classes2:defpackage/bvvp.java:25:            Account[] accounts = AccountManager.get(context).getAccounts();
classes2:defpackage/bxes.java:82:            AccountManager accountManager = AccountManager.get(this.b);
classes2:defpackage/byfw.java:17:        this.c = AccountManager.get(context.getApplicationContext());
classes2:defpackage/ccmz.java:661:                new cdks(context2, str, new cclv(AccountManager.get(context2), cgfmVarG), strJ, bukbVarB, ccmlVar, cqfjVar, 97, cqewVar, cgfmVarG, new atgm(context2)).a(context2, new ccnm());
classes2:defpackage/bulx.java:105:                                    cfdo cfdoVarJ = cfdo.j(((AccountManager) bvqlVar.a).getAccountsByTypeForPackage("com.google", (String) bvqlVar.b));
classes2:defpackage/bvvo.java:25:            Account[] accounts = AccountManager.get(context).getAccounts();
classes2:defpackage/cadw.java:45:        AccountManager.get(this.a).addAccount("com.google", "webupdates", null, bundle, null, new cadu(ccVar), null);
classes7:defpackage/cdjr.java:1210:                cclv cclvVar = new cclv(AccountManager.get(context.getApplicationContext()), this.f);
classes7:defpackage/bqzm.java:179:                    AccountManager.get(context).addAccount("com.google", null, null, null, (Activity) byow.O(context, Activity.class), new AccountManagerCallback() { // from class: bxrc
classes7:defpackage/bunv.java:53:            Account[] accountsByType = AccountManager.get(context).getAccountsByType("com.google");
classes7:defpackage/bqyv.java:281:                Account[] accountsByType = AccountManager.get(context).getAccountsByType("com.google");
```

### battery_state — 3 hits in 2 files

- `classes2:defpackage/bxeo.java` (2)
- `classes2:defpackage/bppw.java` (1)

```
classes2:defpackage/bppw.java:198:                boolean zIsCharging = ((BatteryManager) systemService2).isCharging();
classes2:defpackage/bxeo.java:88:                batteryManager.isCharging();
classes2:defpackage/bxeo.java:89:                return ceui.i(Boolean.valueOf(batteryManager.isCharging()));
```

### screen_capture_detect — 69 hits in 43 files

- `classes5:defpackage/akiw.java` (6)
- `classes5:defpackage/akiv.java` (6)
- `classes:defpackage/rhl.java` (4)
- `classes:defpackage/ngh.java` (2)
- `classes:defpackage/nfv.java` (2)
- `classes2:defpackage/boem.java` (2)
- `classes2:defpackage/bbzi.java` (2)
- `classes3:defpackage/cntc.java` (2)
- `classes6:defpackage/clym.java` (2)
- `classes6:defpackage/bcts.java` (2)
- `classes6:defpackage/cpuq.java` (2)
- `classes6:defpackage/cmlh.java` (2)

```
classes:defpackage/ngh.java:35833:                this.aF.put("LENS_SCREENSHOT", 3553);
classes:defpackage/ngh.java:35868:                this.aG.put("LENS_SCREENSHOT", 3553);
classes:defpackage/xyg.java:35:        xyg xygVar5 = new xyg("SCREENSHOTS", 4);
classes:defpackage/nfv.java:12357:        cfdsVarH.g("LENS_SCREENSHOT", ngaVar.Dk);
classes:defpackage/nfv.java:12388:        cfdsVarH.g("LENS_SCREENSHOT", ngaVar.DJ);
classes:defpackage/rhl.java:118:            str5 = "UNKNOWN_SCREENSHOTS_FOLDER_BACKUP_STATE";
classes:defpackage/rhl.java:120:            str5 = "SCREENSHOTS_FOLDER_NOT_FOUND";
classes:defpackage/rhl.java:122:            str5 = "SCREENSHOTS_FOLDER_BACKUP_DISABLED";
classes:defpackage/rhl.java:124:            str5 = "SCREENSHOTS_FOLDER_BACKUP_ENABLED";
classes:defpackage/aaxt.java:3874:        aaxt aaxtVar100 = new aaxt("LOCAL_SCREENSHOTS_INDEX_PROCESSOR", 99, new aaxr() { // from class: aaxn
classes2:defpackage/boem.java:151:        ccawVar.r(bkvu.class, "LENS_SCREENSHOT", (bkvu) ((ctyc) ((bleg) crji.b(context, bleg.class)).VA().get("LENS_SCREENSHOT")).a());
classes2:defpackage/boem.java:167:        ccawVar.r(bkvx.class, "LENS_SCREENSHOT", (bkvx) ((ctyc) ((bleg) crji.b(context, bleg.class)).VB().get("LENS_SCREENSHOT")).a());
```

### audio_capture — 0 hits in 0 files


```
```

### accessibility — 310 hits in 88 files

- `classes7:defpackage/bpsu.java` (15)
- `classes:defpackage/fsx.java` (7)
- `classes:defpackage/fuk.java` (7)
- `classes3:defpackage/ehf.java` (7)
- `classes7:com/google/android/material/behavior/HideBottomViewOnScrollBehavior.java` (7)
- `classes7:com/google/android/material/behavior/HideViewOnScrollBehavior.java` (7)
- `classes7:com/google/android/material/bottomsheet/BottomSheetDragHandleView.java` (7)
- `classes7:defpackage/cedy.java` (7)
- `classes7:defpackage/ceec.java` (7)
- `classes3:defpackage/dwt.java` (6)
- `classes7:defpackage/bpog.java` (6)
- `classes7:defpackage/ceeh.java` (6)

```
classes:android/support/v7/widget/RecyclerView.java:29:import android.view.accessibility.AccessibilityManager;
classes:android/support/v7/widget/RecyclerView.java:156:    private final AccessibilityManager au;
classes:android/support/v7/widget/RecyclerView.java:265:        recyclerView.au = (AccessibilityManager) recyclerView.getContext().getSystemService("accessibility");
classes:android/support/v7/widget/RecyclerView.java:2003:        AccessibilityManager accessibilityManager = this.au;
classes:defpackage/dow.java:4:import android.view.accessibility.AccessibilityManager;
classes:defpackage/dow.java:33:    /* JADX WARN: Type inference failed for: r15v40, types: [android.view.accessibility.AccessibilityManager$AccessibilityStateChangeListener, java.lang.Object] */
classes:defpackage/dow.java:143:                AccessibilityManager accessibilityManager = (AccessibilityManager) obj6;
classes:defpackage/ngw.java:5:import android.view.accessibility.AccessibilityManager;
classes:defpackage/ngw.java:42:                return new nkp((AccessibilityManager) this.a.b().getSystemService("accessibility"));
classes:defpackage/ful.java:8:import android.view.accessibility.AccessibilityManager;
classes:defpackage/ful.java:360:            AccessibilityManager accessibilityManager = (AccessibilityManager) this.v.a;
classes:defpackage/ful.java:363:            this.c = zIsEnabled && accessibilityManager.isTouchExplorationEnabled();
```

### root_emulator — 4 hits in 3 files

- `classes5:defpackage/aguw.java` (2)
- `classes5:defpackage/aguu.java` (1)
- `classes7:defpackage/cedy.java` (1)

```
classes5:defpackage/aguu.java:121:                if (str.equals("BCLunderexposed_200.emd")) {
classes5:defpackage/aguw.java:106:                agut agutVar = new agut(aguoVar.k() ? new agur() : new aguq(), "facenet_mobile_v1_8bits.tflite", ctzs.x(new String[]{"BCLblurred_100.emd", "BCLfrontalgaze_200.emd", "BCLnonhuman_100.emd", "BCLunderexposed_200.emd", true == arqeVar.g() ? "CLqual [... 
classes5:defpackage/aguw.java:132:                agut agutVar2 = new agut(new agur(), "model.tflite", ctzu.ba(new String[]{"BCLblurred_100.emd", "BCLfrontalgaze_200.emd", "BCLnonhuman_100.emd", "BCLunderexposed_200.emd"}), 1);
classes7:defpackage/cedy.java:80:            throw new RuntimeException("EditText needs to be an AutoCompleteTextView if an Exposed Dropdown Menu is being used.");
```

### js_bridge — 4 hits in 4 files

- `classes5:defpackage/anga.java` (1)
- `classes5:defpackage/bbvh.java` (1)
- `classes7:defpackage/cdjr.java` (1)
- `classes8:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java` (1)

```
classes5:defpackage/anga.java:103:                    webView.addJavascriptInterface(new aodb(obj6), "KumaBridge");
classes5:defpackage/bbvh.java:77:            webView.addJavascriptInterface(new bbvm(bbxdVar), "GooglePhotosBridge");
classes7:defpackage/cdjr.java:213:                webView2.addJavascriptInterface(cdkcVar, "UpsellInterface");
classes8:org/chromium/support_lib_boundary/WebViewBuilderBoundaryInterface.java:54:        public void addJavascriptInterface(Object obj, String str, List list) {
```

### boot_persist — 6 hits in 6 files

- `classes2:defpackage/bxnb.java` (1)
- `classes4:com/google/android/apps/photos/account/full/FetchAccountPropertiesAppUpgradeBroadcastReceiver.java` (1)
- `classes5:com/google/android/apps/photos/notificationchannels/AppUpdateBroadcastReceiver.java` (1)
- `classes5:com/google/android/apps/photos/notificationchannels/BootCompleteBroadcastReceiver.java` (1)
- `classes6:com/google/android/apps/photos/restore/service/RestoreRestartReceiver.java` (1)
- `classes7:defpackage/bwel.java` (1)

```
classes2:defpackage/bxnb.java:61:        JobInfo.Builder persisted = new JobInfo.Builder(iV, new ComponentName(context, bwrnVar.h)).setExtras(persistableBundle).setPersisted(byow.bn(context, "android.permission.RECEIVE_BOOT_COMPLETED"));
classes4:com/google/android/apps/photos/account/full/FetchAccountPropertiesAppUpgradeBroadcastReceiver.java:18:        if ("android.intent.action.MY_PACKAGE_REPLACED".equals(intent.getAction())) {
classes5:com/google/android/apps/photos/notificationchannels/AppUpdateBroadcastReceiver.java:17:        if ("android.intent.action.MY_PACKAGE_REPLACED".equals(intent.getAction())) {
classes5:com/google/android/apps/photos/notificationchannels/BootCompleteBroadcastReceiver.java:17:        if ("android.intent.action.BOOT_COMPLETED".equals(intent.getAction())) {
classes6:com/google/android/apps/photos/restore/service/RestoreRestartReceiver.java:32:        if ("android.intent.action.MY_PACKAGE_REPLACED".equals(intent.getAction())) {
classes7:defpackage/bwel.java:21:            return i != 2 ? i != 3 ? i != 4 ? i != 5 ? cueh.f("android.intent.action.MY_PACKAGE_REPLACED", intent.getAction()) : cueh.f("android.intent.action.TIMEZONE_CHANGED", intent.getAction()) : cueh.f("android.intent.action.BOOT_COMPLETED", intent.getAct [... o
```

### full_screen_intent — 1 hits in 1 files

- `classes7:defpackage/cakg.java` (1)

```
classes7:defpackage/cakg.java:58:        builder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.ledARGB, notification.ledOn [... o
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 71 hits in 59 files

- `classes:android/support/v7/widget/AppCompatTextView.java` (2)
- `classes:android/support/v7/widget/AppCompatButton.java` (2)
- `classes2:com/google/android/material/button/MaterialButton.java` (2)
- `classes3:defpackage/hix.java` (2)
- `classes4:defpackage/sxq.java` (2)
- `classes4:defpackage/oer.java` (2)
- `classes5:defpackage/akut.java` (2)
- `classes6:defpackage/birq.java` (2)
- `classes6:defpackage/bfic.java` (2)
- `classes7:com/google/android/material/timepicker/ChipTextInputComboView.java` (2)
- `classes7:defpackage/cdvm.java` (2)
- `classes7:defpackage/cefr.java` (2)

```
classes:android/support/v7/widget/AppCompatTextView.java:224:    protected final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:android/support/v7/widget/AppCompatTextView.java:225:        super.onTextChanged(charSequence, i, i2, i3);
classes:android/support/v7/widget/AppCompatButton.java:217:    protected void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes:android/support/v7/widget/AppCompatButton.java:218:        super.onTextChanged(charSequence, i, i2, i3);
classes:defpackage/hpq.java:305:        editText.addTextChangedListener(hjeVar);
classes2:com/google/android/material/button/MaterialButton.java:780:    protected final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes2:com/google/android/material/button/MaterialButton.java:781:        super.onTextChanged(charSequence, i, i2, i3);
classes3:defpackage/ctnt.java:66:                editText2.addTextChangedListener(ceecVar.k);
classes3:defpackage/hje.java:30:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes3:defpackage/hix.java:60:    public final void onTextChanged(CharSequence charSequence, int i, int i2, int i3) {
classes3:defpackage/hix.java:61:        ((TextWatcher) this.a).onTextChanged(charSequence, i, i2, i3);
classes4:defpackage/sxq.java:83:            this.f.addTextChangedListener((TextWatcher) akhkVar.a());
```

### webview_tracking — 0 hits in 0 files


```
```

### streaks — 4 hits in 3 files

- `classes8:defpackage/ckxv.java` (2)
- `classes2:defpackage/anor.java` (1)
- `classes7:defpackage/buhr.java` (1)

```
classes2:defpackage/anor.java:124:        anor anorVar7 = new anor("INSIGHT_SNACKS_STREAKS", 6, 11);
classes7:defpackage/buhr.java:183:        buhr buhrVar52 = new buhr("TRANSLATE_LANGUAGE_LEARNING_STREAK", 51, "Translate Language Learning Streak");
classes8:defpackage/ckxv.java:241:    END_OF_YEAR_MEMORY_INSIGHT_SNACKS_STREAKS(8041),
classes8:defpackage/ckxv.java:1863:                                                                                return END_OF_YEAR_MEMORY_INSIGHT_SNACKS_STREAKS;
```

### reengagement — 891 hits in 310 files

- `classes3:defpackage/ajp.java` (41)
- `classes3:defpackage/ajn.java` (35)
- `classes8:defpackage/cqew.java` (18)
- `classes7:defpackage/bqkb.java` (16)
- `classes3:defpackage/jed.java` (15)
- `classes2:defpackage/bsar.java` (14)
- `classes3:defpackage/ijd.java` (14)
- `classes3:defpackage/anp.java` (13)
- `classes7:defpackage/bpwi.java` (13)
- `classes2:defpackage/asei.java` (12)
- `classes3:defpackage/alf.java` (12)
- `classes3:defpackage/ish.java` (12)

```
classes:com/google/android/apps/photos/backup/core/BackupAlarmManager$ScheduleAlarmTask.java:62:                        trxVar.c.setInexactRepeating(3, SystemClock.elapsedRealtime() + lValueOf.longValue(), lValueOf.longValue(), pendingIntentC);
classes:defpackage/fpn.java:238:        this.b = "NearDupesCollapsedDateHeaderManager";
classes:defpackage/fpn.java:262:        this.b = "NearDupesCollapsedCountManager";
classes:defpackage/fpn.java:268:        this.b = "NdCollapsed";
classes:defpackage/vus.java:33:        return "OfferCategories(isWinback=" + this.a + ')';
classes:defpackage/iai.java:1331:        return j2 == -9223372036854775807L ? System.currentTimeMillis() : j2 + SystemClock.elapsedRealtime();
classes:defpackage/aaha.java:7:    NEAR_DUPES_COLLAPSED("day_segmented_date_headers_nd_collapsed", "day_segmented_date_headers_nd_collapsed_idx");
classes:defpackage/aaha.java:9:    public static final cfdo c = cfdo.l(DAY, NEAR_DUPES_COLLAPSED);
classes:defpackage/rrs.java:29:            byqzVar.b = new bymz(SystemClock.elapsedRealtime(), SystemClock.uptimeMillis());
classes:defpackage/rrs.java:32:        ajth.c = Long.valueOf(SystemClock.elapsedRealtime());
classes:defpackage/rrs.java:61:            byqzVar.c = new bymz(SystemClock.elapsedRealtime(), SystemClock.uptimeMillis());
classes:defpackage/qie.java:80:        return "MainGridCollection(accountId=" + this.a + ", nearDupesCollapsed=" + this.b + ", gridFilterSettings=" + this.c + ", featureSet=" + this.d + ')';
```

### notif_permission_nag — 6 hits in 4 files

- `classes6:defpackage/bffp.java` (2)
- `classes8:defpackage/ckxv.java` (2)
- `classes2:defpackage/bfgx.java` (1)
- `classes2:defpackage/bepf.java` (1)

```
classes2:defpackage/bfgx.java:25:        bfgx bfgxVar4 = new bfgx("SHOW_REPROMPT", 3);
classes2:defpackage/bepf.java:257:        ccge.b("photos.pfc.force_reprompt");
classes6:defpackage/bffp.java:99:                        if (bfgxVarA == bfgxVar && cacwVar.e(i).c("com.google.android.apps.photos.search.peoplegroupingonboarding.reprompt").j("job-ran", false)) {
classes6:defpackage/bffp.java:101:                            cadj cadjVarP = cacwVar.q(i).p("com.google.android.apps.photos.search.peoplegroupingonboarding.reprompt");
classes8:defpackage/ckxv.java:299:    LOCAL_PFC_OPT_IN_REPROMPT_NOTIFICATION(1030),
classes8:defpackage/ckxv.java:1023:                        return LOCAL_PFC_OPT_IN_REPROMPT_NOTIFICATION;
```

### cancellation_retention — 1 hits in 1 files

- `classes6:com/google/android/apps/photos/share/interstitial/ShareIntentInterstitialActivity.java` (1)

```
classes6:com/google/android/apps/photos/share/interstitial/ShareIntentInterstitialActivity.java:21:@Metadata(d1 = {"\u0000b\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u001
```

### urgency_countdown — 292 hits in 69 files

- `classes8:defpackage/ctut.java` (18)
- `classes3:defpackage/hko.java` (11)
- `classes3:defpackage/anb.java` (10)
- `classes7:defpackage/ceiu.java` (10)
- `classes3:defpackage/ifg.java` (7)
- `classes7:defpackage/bpga.java` (7)
- `classes8:defpackage/ctuw.java` (7)
- `classes3:defpackage/alo.java` (6)
- `classes3:defpackage/iel.java` (6)
- `classes3:defpackage/ajx.java` (6)
- `classes3:defpackage/ifj.java` (6)
- `classes5:defpackage/ahpd.java` (6)

```
classes2:com/google/android/libraries/performance/primes/metrics/crash/NativeCrashHandlerImpl.java:9:import java.util.concurrent.CountDownLatch;
classes2:com/google/android/libraries/performance/primes/metrics/crash/NativeCrashHandlerImpl.java:14:    final CountDownLatch a = new CountDownLatch(1);
classes2:com/google/android/libraries/performance/primes/metrics/crash/NativeCrashHandlerImpl.java:15:    final CountDownLatch b = new CountDownLatch(1);
classes2:com/google/android/libraries/performance/primes/metrics/crash/NativeCrashHandlerImpl.java:53:            this.b.countDown();
classes2:com/google/android/libraries/performance/primes/metrics/crash/NativeCrashHandlerImpl.java:63:                this.a.countDown();
classes2:com/google/android/gms/common/api/internal/BasePendingResult.java:14:import java.util.concurrent.CountDownLatch;
classes2:com/google/android/gms/common/api/internal/BasePendingResult.java:22:    private final CountDownLatch a;
classes2:com/google/android/gms/common/api/internal/BasePendingResult.java:40:        this.a = new CountDownLatch(1);
classes2:com/google/android/gms/common/api/internal/BasePendingResult.java:80:        this.a.countDown();
classes2:com/google/android/gms/common/api/internal/BasePendingResult.java:220:        this.a = new CountDownLatch(1);
classes2:defpackage/bxyo.java:22:import java.util.concurrent.CountDownLatch;
classes2:defpackage/bxyo.java:645:        CountDownLatch countDownLatch = new CountDownLatch(1);
```

### infinite_autoplay — 36 hits in 18 files

- `classes5:defpackage/bmbk.java` (10)
- `classes5:defpackage/bkoc.java` (4)
- `classes2:defpackage/azah.java` (2)
- `classes2:defpackage/aoaj.java` (2)
- `classes3:defpackage/cwrb.java` (2)
- `classes3:defpackage/jpa.java` (2)
- `classes5:defpackage/bjka.java` (2)
- `classes5:defpackage/bjss.java` (2)
- `classes2:defpackage/athc.java` (1)
- `classes2:defpackage/apvp.java` (1)
- `classes2:defpackage/atoq.java` (1)
- `classes2:defpackage/asip.java` (1)

```
classes2:defpackage/athc.java:18:    public static final agxw k = agxx.b("photos.enableScrollMemoryDiffAutoplayBreakdown").h(new asrm(7)).a();
classes2:defpackage/azah.java:11:    private static final byij b = byij.d("Photos.GridScrollMemoryDiff.AutoplayOn");
classes2:defpackage/azah.java:12:    private static final byij c = byij.d("Photos.GridScrollMemoryDiff.AutoplayOff");
classes2:defpackage/aoaj.java:685:        v = agxx.b("debug.photos.enable_autoplay_badge_redesign").h(new aoaa(9)).a();
classes2:defpackage/aoaj.java:1947:        Y = agxx.b("debug.photos.enable_extend_media_autoplay_duration_before_video").h(new BooleanSupplier() { // from class: aoag
classes2:defpackage/apvp.java:1182:        K = agxx.b("photos.movies.enable_autoplay_recipes_on_create_tab").h(new apvo(7)).a();
classes2:defpackage/atoq.java:213:        agxx.b("video.enable_dynamic_autoplay").h(new BooleanSupplier() { // from class: atoo
classes2:defpackage/asip.java:43:        return "CastMedia{isViewingMedia=" + this.c + ", accountId=" + i2 + ", direction=" + str + ", showSplashScreen=" + z + ", autoPlayEnabled=" + z2 + ", isLoading=false, isMediaUpdated=" + z3 + ", isMotionOff=" + z4 + ", startTime=" + strValueOf + ", curr [... o
classes3:defpackage/cwrb.java:589:    INFO_PANEL_RELATED_AUTOPLAY_LATENCY(589),
classes3:defpackage/cwrb.java:1814:                                                                        return INFO_PANEL_RELATED_AUTOPLAY_LATENCY;
classes3:defpackage/jpa.java:76:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
classes3:defpackage/jpa.java:83:        	at jadx.core.dex.visitors.regions.maker.LoopRegionMaker.makeEndlessLoop(LoopRegionMaker.java:281)
```

### badges — 1 hits in 1 files

- `classes7:defpackage/cakg.java` (1)

```
classes7:defpackage/cakg.java:58:        builder.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, null).setVibrate(notification.vibrate).setLights(notification.ledARGB, notification.ledOn [... o
```

### minors_age — 4 hits in 3 files

- `classes5:defpackage/arey.java` (2)
- `classes8:defpackage/cnbs.java` (1)
- `classes8:defpackage/cnbj.java` (1)

```
classes5:defpackage/arey.java:19:    MINORS_AGE_GATED_ILLEGAL(13),
classes5:defpackage/arey.java:66:                return MINORS_AGE_GATED_ILLEGAL;
classes8:defpackage/cnbs.java:120:                            cnbjVar = cnbj.DATA_USAGE_VERIFICATION_TESTING_VALIDATION_NEEDS_PRIVACY_APPROVAL;
classes8:defpackage/cnbj.java:43:    DATA_USAGE_VERIFICATION_TESTING_VALIDATION_NEEDS_PRIVACY_APPROVAL(40),
```

### screen_time — 0 hits in 0 files


```
```

## UI string categories (default locale)

### loss_aversion_copy — 8 strings

```
strings.xml:1238:    <string name="photos_autobackuppromos_backupfavorites_sunset_title">{number_of_days, plural, =1 {Backing up favorites will end in # day} other {Backing up favorites will end in # days}}</string>
strings.xml:1252:    <string name="photos_autobackuppromos_bbd_title_enable">Don’t lose your photos, turn on backup today</string>
strings.xml:1903:    <string name="photos_cloudstorage_storagesweeper_swipe_page_exit_confirmation_dialog_subtitle_v1">Your current selections won’t be saved if you exit and you’ll lose the progress you’ve made</string>
strings.xml:3778:    <string name="photos_genaiconsent_settings_opt_out_dialog_message_retention_enabled">"You’ll lose access to Gemini features in Photos, like Ask Photos and smart, personalized editing. Your experience overall will be less personalized.
strings.xml:3783:    <string name="photos_genaiconsent_settings_opt_out_dialog_message_v2">"This will permanently delete any data in your Remember List. You’ll lose access to Gemini features in Photos, like Ask Photos and more personalized memories.
strings.xml:4702:    <string name="photos_movies_activity_storyboard_upgrade_dialog_message">"To use the new editor, you need to update your movie. Themes are no longer supported, so you'll lose any effects you may have."</string>
strings.xml:6616:    <string name="photos_printingskus_printsubscription_storefront_action_dialog_cancel_message">Your series will end and your printing preferences for this series will be deleted.</string>
strings.xml:7755:    <string name="photos_settings_fujifilm_disconnect_dialog_message">By disconnecting, your Fujifilm for Google Photos account will close. This means:&lt;br/>• You won’t be able to see your print drafts&lt;br/>• You’ll lose access to past or in-progress order [... omitted end of lo
```

### urgency_copy — 9 strings

```
strings.xml:905:    <string name="photos_album_ui_albumsuggestion_enable_notification_title">Don’t miss new photos, comments, and more</string>
strings.xml:2551:    <string name="photos_devicesetup_setup_guide_notifications_title">Don’t miss anything important</string>
strings.xml:4790:    <string name="photos_notifications_optinpromo_title_comments">Don’t miss comments from friends and loved ones</string>
strings.xml:4791:    <string name="photos_notifications_optinpromo_title_memories">Don’t miss out on new Memories!</string>
strings.xml:5216:    <string name="photos_permissions_notification_title_new_memories">Don’t miss out on new memories</string>
strings.xml:6412:    <string name="photos_printingskus_kioskprints_ui_pickup_summary_ready_split_date_and_time">Print reference number is valid until %1$s at %2$s and can be reused until it expires</string>
strings.xml:7876:    <string name="photos_settings_promos_description">Limited time offers and discounts for printed products</string>
strings.xml:8654:    <string name="photos_updateshub_notification_opt_in_title_v5">Don’t miss a moment</string>
strings.xml:8655:    <string name="photos_updateshub_notification_opt_in_title_v6">Don’t miss the good stuff</string>
```

### confirmshaming_copy — 41 strings

```
strings.xml:1130:    <string name="photos_auratab_promo_halfsheet_no_thanks">No thanks</string>
strings.xml:1145:    <string name="photos_authfailure_dialog_not_now">Not now</string>
strings.xml:1273:    <string name="photos_autobackuppromos_notifications_not_now">Not now</string>
strings.xml:1309:    <string name="photos_backup_devicefolders_half_sheet_dismissal_button_label">Not now</string>
strings.xml:1357:    <string name="photos_backup_overnight_no_thanks_button">No thanks</string>
strings.xml:1529:    <string name="photos_backup_settings_samsung_turn_on_backup_dialog_cancel">Not now</string>
strings.xml:1812:    <string name="photos_cloudstorage_main_grid_storage_banner_not_now">Not now</string>
strings.xml:1869:    <string name="photos_cloudstorage_promo_oosaccountalert_negative_button">Not now</string>
strings.xml:2664:    <string name="photos_editor_bluejay_looks_promo_no_thanks">No thanks</string>
strings.xml:2673:    <string name="photos_editor_bluejay_not_now_button_text">Not now</string>
strings.xml:3150:    <string name="photos_ellmann_maybe_later">Maybe later</string>
strings.xml:3162:    <string name="photos_ellmann_mecluster_promo_not_now">Not now</string>
strings.xml:3249:    <string name="photos_ellmann_not_now">Not now</string>
strings.xml:3254:    <string name="photos_ellmann_onboarding_location_not_now_1">Not now</string>
strings.xml:3512:    <string name="photos_envelope_signedoutpromo_not_now_button">Not now</string>
strings.xml:3643:    <string name="photos_flyingsky_ellmann_optin_skip_button_text">Not now</string>
strings.xml:3651:    <string name="photos_flyingsky_fragment_bulk_confirmation_banner_skip_button_text">Not now</string>
strings.xml:3710:    <string name="photos_flyingsky_title_suggestions_opt_in_no_thanks">No thanks</string>
strings.xml:3885:    <string name="photos_importsurfaces_promo_all_photos_import_banner_dismiss_button_text">Not now</string>
strings.xml:4133:    <string name="photos_mars_entry_not_now">Not now</string>
strings.xml:4162:    <string name="photos_mars_grid_custom_backup_dialog_not_now">Not now</string>
strings.xml:4312:    <string name="photos_memories_ab_off_mode_no_thanks">No thanks</string>
strings.xml:4464:    <string name="photos_memories_promo_dailymultistep_decline">No thanks</string>
strings.xml:4484:    <string name="photos_memories_promo_eventtriptitling_decline_v2">No thanks</string>
strings.xml:4607:    <string name="photos_memoriesapi_connection_do_not_allow">Not now</string>
strings.xml:4785:    <string name="photos_notifications_optinpromo_dismiss_button">No thanks</string>
strings.xml:5110:    <string name="photos_partneraccount_promo_share_back_no_thanks">No thanks</string>
strings.xml:5210:    <string name="photos_permissions_notification_negative_button">Not now</string>
strings.xml:5260:    <string name="photos_photoeditor_ask_photos_opt_in_dismiss_button">Not now</string>
strings.xml:5325:    <string name="photos_photoeditor_enchilada_ask_optin_bottom_sheet_dismiss_button_test_tag">not now</string>
strings.xml:5774:    <string name="photos_photoeditor_fragments_editor3_not_now">Not now</string>
strings.xml:5959:    <string name="photos_photoeditor_udon_backup_required_dialog_not_now_button_text">Not now</string>
strings.xml:6181:    <string name="photos_picker_backup_promo_confirm_dialog_not_now">Not now</string>
strings.xml:7200:    <string name="photos_sdk_appconnection_gallery_connection_promo_dialog_not_now">Not now</string>
strings.xml:7414:    <string name="photos_search_functional_cal_permissions_neg_button">No thanks</string>
strings.xml:7588:    <string name="photos_search_pfc_promo_not_now_label">Not now</string>
strings.xml:8350:    <string name="photos_stories_promo_clusternaming_skip_naming_button_text">No thanks</string>
strings.xml:8435:    <string name="photos_strings_no_thanks">No thanks</string>
strings.xml:8436:    <string name="photos_strings_not_now">Not now</string>
strings.xml:8632:    <string name="photos_update_treatment_not_now_button">Not now</string>
strings.xml:9623:    <string name="survey_prompt_no_thanks">No thanks</string>
```

### social_pressure_copy — 36 strings

```
strings.xml:273:    <string name="firebase_database_url">https://photos-android.firebaseio.com</string>
strings.xml:976:    <string name="photos_allphotos_gridcontrols_hide_clutter_base_filter_setting_subtitle_v3">Backed-up photos like screenshots, GIFs, and memes are hidden</string>
strings.xml:977:    <string name="photos_allphotos_gridcontrols_hide_clutter_base_filter_setting_subtitle_v4">Photos like screenshots, GIFs, and memes are hidden after they are backed up</string>
strings.xml:1418:    <string name="photos_backup_settings_backup_options_custom_backup_subtext">Photos &amp; videos that you choose, such as screenshots and favorites will be backed up</string>
strings.xml:1458:    <string name="photos_backup_settings_custom_backup_options_screenshots_label">Screenshots</string>
strings.xml:1462:    <string name="photos_backup_settings_custom_subtext_all">People, favorites, screenshots and device folders</string>
strings.xml:1465:    <string name="photos_backup_settings_custom_subtext_favorites_screenshots">Favorites and screenshots</string>
strings.xml:1466:    <string name="photos_backup_settings_custom_subtext_favorites_screenshots_folders">Favorites, screenshots and device folders</string>
strings.xml:1471:    <string name="photos_backup_settings_custom_subtext_people_favorites_screenshots">People, favorites and screenshots</string>
strings.xml:1473:    <string name="photos_backup_settings_custom_subtext_people_screenshots">People and screenshots</string>
strings.xml:1474:    <string name="photos_backup_settings_custom_subtext_people_screenshots_folders">People, screenshots and device folders</string>
strings.xml:1475:    <string name="photos_backup_settings_custom_subtext_screenshots">Screenshots only</string>
strings.xml:1476:    <string name="photos_backup_settings_custom_subtext_screenshots_folders">Screenshots and device folders</string>
strings.xml:1698:    <string name="photos_c2pa_infopanel_origin_type_screenshots_with_ai_title">Parts of this screenshot or recording may include AI content</string>
strings.xml:3045:    <string name="photos_ellmann_agent_navigating_to_screenshots">Opening Screenshots</string>
strings.xml:3112:    <string name="photos_ellmann_feedback_warning_body_v2">"Feedback sent to us will include the prompt, response, and contextual data. Your photos or videos will not be saved in relation to this feedback. You may optionally include a screenshot to help us see [... omitted end of lo
strings.xml:3148:    <string name="photos_ellmann_include_screenshot">Include screenshot</string>
strings.xml:3282:    <string name="photos_ellmann_screenshot">Screenshot</string>
strings.xml:3283:    <string name="photos_ellmann_screenshot_thumbnail">Screenshot thumbnail</string>
strings.xml:3904:    <string name="photos_launchershortcuts_full_view_screenshots">View screenshots</string>
strings.xml:3905:    <string name="photos_launchershortcuts_full_view_screenshots_short">Screenshot</string>
strings.xml:7066:    <string name="photos_quotamanagement_celebration_clean_up_screenshots">Clean up screenshots</string>
strings.xml:7089:    <string name="photos_quotamanagement_data_screenshots_category_title">Screenshots</string>
strings.xml:7144:    <string name="photos_screenshots_deeplink_title">View screenshots</string>
strings.xml:7145:    <string name="photos_screenshots_module_subtitle">{count, plural, =1{# new} other{# new}}</string>
strings.xml:7146:    <string name="photos_screenshots_module_title">{count, plural, =1{Screenshot} other{Screenshots}}</string>
strings.xml:7238:    <string name="photos_search_autocomplete_zeroprefix_screenshots_and_screen_recordings_title">Screenshots &amp; recordings</string>
strings.xml:7259:    <string name="photos_search_destination_list_item_screenshots">Screenshots</string>
strings.xml:7324:    <string name="photos_search_explore_category_screenshots">Screenshots</string>
strings.xml:7424:    <string name="photos_search_functional_categorization_screenshots_removal_confirm_button_text">Back up and remove</string>
strings.xml:7425:    <string name="photos_search_functional_categorization_screenshots_removal_message">Photos and videos that you remove from <b>Screenshots &amp; recordings</b> will need to be backed up first</string>
strings.xml:7426:    <string name="photos_search_functional_categorization_screenshots_removal_title">Back up and remove?</string>
strings.xml:7491:    <string name="photos_search_menu_screenshots_device_folder">Screenshots device folder</string>
strings.xml:8456:    <string name="photos_suggestedactions_archive_dialog_content">"Hide photos that you don't want to see in your Photos view, like screenshots or receipts. 
strings.xml:8499:    <string name="photos_suggestedactions_lens_screenshot">Search inside screenshot</string>
strings.xml:8500:    <string name="photos_suggestedactions_lens_screenshot_short">Search inside photo</string>
```

### guilt_copy — 6 strings

```
strings.xml:1948:    <string name="photos_cloudstorage_winback_pre_header">Come back to Google One</string>
strings.xml:2454:    <string name="photos_devicemanagement_activity_nothing_to_free_up_tip">Come back after you back up more photos &amp; videos</string>
strings.xml:2466:    <string name="photos_devicemanagement_foregroundservice_impl_notification_content_stopped">Come back at any time to free up more space</string>
strings.xml:2542:    <string name="photos_devicesetup_restore_settings_title">Welcome back!</string>
strings.xml:5756:    <string name="photos_photoeditor_fragments_editor3_install_more_editing_tools_dialog_body">Installing more editing tools (%1$d %2$s) on your device may take some time. Save your edits and come back later to use your new editing tools.</string>
strings.xml:8855:    <string name="photos_varenyky_audio_picker_bottom_sheet_sad_mood_button_title">Sad</string>
```

### subscription_copy — 196 strings

```
plurals.xml:78:    <plurals name="photos_album_highlight_editor_max_reached_count_text_updated">
plurals.xml:79:        <item quantity="other">Max reached • %d items selected</item>
plurals.xml:80:        <item quantity="zero">Max reached • %d items selected</item>
plurals.xml:81:        <item quantity="one">Max reached • %d item selected</item>
plurals.xml:184:    <plurals name="photos_create_mediabundle_validation_error_max">
plurals.xml:328:    <plurals name="photos_peoplepicker_exceed_max_allowed">
plurals.xml:356:    <plurals name="photos_printingskus_common_ui_max_prints_dialog_message">
plurals.xml:360:    <plurals name="photos_printingskus_common_ui_max_prints_in_order_dialog_message">
plurals.xml:418:    <plurals name="photos_printingskus_printsubscription_ui_add_photos_tooltip">
plurals.xml:434:    <plurals name="photos_restore_notification_max_photo_count_restored">
strings.xml:194:    <string name="duration_title">Set Maximum Video Duration</string>
strings.xml:628:    <string name="og_storage_card_unlock_storage_discount">Unlock storage discount</string>
strings.xml:711:    <string name="peoplekit_maxview_close">Close</string>
strings.xml:712:    <string name="peoplekit_maxview_default_action_bar_title">Select people</string>
strings.xml:713:    <string name="peoplekit_maxview_select_people">Select people</string>
strings.xml:714:    <string name="peoplekit_maxview_send_button">Send</string>
strings.xml:1783:    <string name="photos_cloudstorage_g1_tos_photos_storage_no_discount_23q3">Cancel anytime. By subscribing, you agree to &lt;a href=>our terms&lt;/a>. See how &lt;a href=>Google handles data&lt;/a>.</string>
strings.xml:1784:    <string name="photos_cloudstorage_g1_tos_photos_storage_with_discount_in_eu_23q3">Personalized pricing. Cancel anytime. By subscribing, you agree to &lt;a href=>our terms of service&lt;/a> and &lt;a href=>offer terms&lt;/a>. See how &lt;a href=>Google hand [... omitted end of lo
strings.xml:1785:    <string name="photos_cloudstorage_g1_tos_photos_storage_with_discount_in_non_eu_23q3">Cancel anytime. By subscribing, you agree to &lt;a href=>our terms of service&lt;/a> and &lt;a href=>offer terms&lt;/a>. See how &lt;a href=>Google handles data&lt;/a>.</ [... omitted end of lo
strings.xml:1794:    <string name="photos_cloudstorage_kirby_buy_button_no_offer_subtitle">Google One subscription</string>
strings.xml:1842:    <string name="photos_cloudstorage_premium_onboarding_feature_1">{count, plural, =1{Store {count}+ photos &amp; videos} other{Store {count}+ photos &amp; videos} }</string>
strings.xml:1843:    <string name="photos_cloudstorage_premium_onboarding_feature_2">Use across Google Photos, Gmail &amp; Drive</string>
strings.xml:1844:    <string name="photos_cloudstorage_premium_onboarding_feature_3">{count, plural, =1{Share storage with up to {count} other} other{Share storage with up to {count} others} }</string>
strings.xml:1845:    <string name="photos_cloudstorage_premium_onboarding_headline_v4">"Keep years of memories
strings.xml:1847:    <string name="photos_cloudstorage_premium_onboarding_no_subscription_cta_text">Continue without subscription</string>
strings.xml:1848:    <string name="photos_cloudstorage_premium_onboarding_no_subscription_feature_1">Continue using the %1$s of storage that comes with your Google Account</string>
strings.xml:1849:    <string name="photos_cloudstorage_premium_onboarding_no_subscription_feature_1_v1">Continue using the %1$s of storage shared across your Google Account</string>
strings.xml:1850:    <string name="photos_cloudstorage_premium_onboarding_no_subscription_feature_2_v1">New photos won’t be seen in search results and Memories when you run out of storage</string>
strings.xml:1851:    <string name="photos_cloudstorage_premium_onboarding_no_subscription_storage_feature_v1">Limited to %1$s of storage</string>
strings.xml:1852:    <string name="photos_cloudstorage_premium_onboarding_no_subscription_title">No subscription</string>
strings.xml:1853:    <string name="photos_cloudstorage_premium_onboarding_premium_tag_v1">Most popular plan</string>
strings.xml:1854:    <string name="photos_cloudstorage_premium_onboarding_premium_tag_with_discount" formatted="false">{count, plural, =1{#% off} other{#% off}}</string>
strings.xml:1855:    <string name="photos_cloudstorage_premium_onboarding_subtitle_free_trial">%1$s after Google One trial</string>
strings.xml:1856:    <string name="photos_cloudstorage_premium_onboarding_subtitle_intro_price">%1$s after Google One offer</string>
strings.xml:1857:    <string name="photos_cloudstorage_premium_onboarding_subtitle_no_offer">Google One Basic plan</string>
strings.xml:1858:    <string name="photos_cloudstorage_premium_onboarding_title_with_discount">%1$s of storage for %2$s &lt;font color=%3$s>&lt;s>%4$s&lt;/s>&lt;/font></string>
strings.xml:1859:    <string name="photos_cloudstorage_premium_onboarding_title_with_no_discount">%1$s of storage for %2$s</string>
strings.xml:1885:    <string name="photos_cloudstorage_stamp_gtm1_title">Unlock new features</string>
strings.xml:1927:    <string name="photos_cloudstorage_ui_exitpathoptions_getstorage_nonmember_body_offer_monthly_trial_monthly_subscription_v1">{billing_period_count, plural, =1{Store an average of {num_photos} photos with a Google One %1$s plan. %2$s for {billing_period_coun [... omitted end of lo
strings.xml:1928:    <string name="photos_cloudstorage_ui_exitpathoptions_getstorage_nonmember_body_offer_monthly_trial_yearly_subscription_v1">{billing_period_count, plural, =1{Store an average of {num_photos} photos with a Google One %1$s plan. %2$s for {billing_period_count [... omitted end of lo
strings.xml:1929:    <string name="photos_cloudstorage_ui_exitpathoptions_getstorage_nonmember_body_offer_yearly_trial_monthly_subscription_v1">{billing_period_count, plural, =1{Store an average of {num_photos} photos with a Google One %1$s plan. %2$s for {billing_period_count [... omitted end of lo
strings.xml:1930:    <string name="photos_cloudstorage_ui_exitpathoptions_getstorage_nonmember_body_offer_yearly_trial_yearly_subscription_v1">{billing_period_count, plural, =1{Store an average of {num_photos} photos with a Google One %1$s plan. %2$s for {billing_period_count} [... omitted end of lo
strings.xml:1943:    <string name="photos_cloudstorage_unlock_discount">Unlock discount</string>
strings.xml:1944:    <string name="photos_cloudstorage_unlock_storage_discount">Unlock storage discount</string>
strings.xml:1952:    <string name="photos_cloudstorage_winback_share_subs">{count, plural, =1 {Share your subscription with up to # other} other {Share your subscription with up to # others} }</string>
strings.xml:1953:    <string name="photos_cloudstorage_xray_expandable_header_subtitle">Photos and videos are not backing up. Clean up space or get {quota} for &lt;s>{original_price}&lt;/s> {subscription_fee} for {offer_duration}.</string>
strings.xml:1955:    <string name="photos_cloudstorage_xray_expandable_header_subtitle_no_offer">Photos and videos are not backing up. Clean up space or get {quota} for {subscription_fee}.</string>
strings.xml:2411:    <string name="photos_database_hdrtype_hdr_10_plus">HDR10+</string>
strings.xml:2552:    <string name="photos_devicesetup_setup_guide_progress">%1$d of %2$d unlocked</string>
strings.xml:2553:    <string name="photos_devicesetup_setup_guide_title">Unlock the power of Google Photos</string>
strings.xml:2644:    <string name="photos_editor_bluejay_kefir_life_understanding_primer_title">Unlock more fun, personalized edits</string>
strings.xml:2689:    <string name="photos_editor_bluejay_phototovideo_soba_intro_text">Get cinematic relighting, immersive background swaps, and beautiful stylization for your video in one tap. Sounds may also be generated. Enjoy daily limited generations at no charge. Upgrade [... omitted end of lo
strings.xml:2707:    <string name="photos_editor_bluejay_phototovideo_soba_trim_subtitle">{num_seconds, plural, =1{Select a section of the video (max # second)} other{Select a section of the video (max # seconds)}}</string>
strings.xml:3194:    <string name="photos_ellmann_mft_outfitcreation_max_selection_reached">You can select up to %1$d items</string>
strings.xml:3585:    <string name="photos_flowers_collab_cam_setup_error_duration_exceeds_max">{count, plural, =1{Group camera can last up to # hour} other{Group camera can last up to # hours}}</string>
strings.xml:3770:    <string name="photos_genaiconsent_settings_description">"Google’s Gemini models help you unlock a deeper understanding of your photos &amp; videos, bringing you more helpful features. 
strings.xml:4001:    <string name="photos_lumos_backingup_max_time_remaining_hour">{hours, plural, =1{More than 1 hour remaining} other{More than # hours remaining} }</string>
strings.xml:4110:    <string name="photos_mars_auth_unlock_message_body">Using your current device screen lock option</string>
strings.xml:4443:    <string name="photos_memories_promo_contextualnotificationnudge_subtitle_v7">Get notified to stroll through it. Plus shared album alerts &amp; more.</string>
strings.xml:5204:    <string name="photos_peoplepicker_exceed_max_people_and_pets">{count, plural, =1{Select up to # person or pet} other{Select up to # people &amp; pets}}</string>
strings.xml:5386:    <string name="photos_photoeditor_enchilada_effects_face_retouch_max_faces_toast">This editing tool can only edit up to %1$d faces.</string>
strings.xml:5807:You can save 10 edited photos every month or subscribe to a Google One Premium plan for unlimited saves.
strings.xml:5843:    <string name="photos_photoeditor_fragments_editor3_upsell_banner">Unlock this feature and more with a Google One membership</string>
strings.xml:6003:    <string name="photos_photoeditor_udon_meterered_bottom_sheet_body">Your %s saves are refreshed on the first day of every month. Get unlimited saves in Magic Editor, extra storage, and more with a Google One Premium subscription.</string>
strings.xml:6027:    <string name="photos_photoeditor_ui_a11y_aspect_ratio_free">Unlock the crop rectangle aspect ratio</string>
strings.xml:6189:    <string name="photos_picker_impl_max_selection_exceeded_dialog_title">Maximum number of photos selected</string>
strings.xml:6196:    <string name="photos_picker_restriction_max">Select up to %1$d %2$s</string>
strings.xml:6198:    <string name="photos_picker_restriction_min_max">Select %1$d to %2$d %3$s</string>
strings.xml:6305:    <string name="photos_printingskus_common_ui_max_prints_dialog_title">Too many prints</string>
strings.xml:6616:    <string name="photos_printingskus_printsubscription_storefront_action_dialog_cancel_message">Your series will end and your printing preferences for this series will be deleted.</string>
strings.xml:6617:    <string name="photos_printingskus_printsubscription_storefront_action_dialog_cancel_title">Cancel premium print series</string>
strings.xml:6618:    <string name="photos_printingskus_printsubscription_storefront_action_dialog_confirm">Confirm</string>
strings.xml:6619:    <string name="photos_printingskus_printsubscription_storefront_action_dialog_dismiss">Don’t change</string>
strings.xml:6620:    <string name="photos_printingskus_printsubscription_storefront_action_dialog_skip_disabled_message">You can only skip during monthly review window</string>
strings.xml:6621:    <string name="photos_printingskus_printsubscription_storefront_action_dialog_skip_message">"This delivery will be skipped, and you won't be charged. Prints and payments will resume next month."</string>
strings.xml:6622:    <string name="photos_printingskus_printsubscription_storefront_action_dialog_skip_title">Skip this month</string>
strings.xml:6623:    <string name="photos_printingskus_printsubscription_storefront_archive_dialog_message">Archiving is permanent and you will not be able to receive customer support for this print series order</string>
strings.xml:6624:    <string name="photos_printingskus_printsubscription_storefront_cancel_settings">Cancel service</string>
strings.xml:6625:    <string name="photos_printingskus_printsubscription_storefront_canceled_toast">Premium print series canceled</string>
strings.xml:6626:    <string name="photos_printingskus_printsubscription_storefront_celebrate_message">Decorate your home with photos of your loved ones</string>
strings.xml:6627:    <string name="photos_printingskus_printsubscription_storefront_celebrate_title">Celebrate life’s moments</string>
strings.xml:6628:    <string name="photos_printingskus_printsubscription_storefront_description">"10 premium 4×6″ prints.
strings.xml:6630:    <string name="photos_printingskus_printsubscription_storefront_download">Download as pdf</string>
strings.xml:6631:    <string name="photos_printingskus_printsubscription_storefront_draft_item_review_before">Review before %s</string>
strings.xml:6632:    <string name="photos_printingskus_printsubscription_storefront_draft_item_reviewed">Reviewed [%s]</string>
strings.xml:6633:    <string name="photos_printingskus_printsubscription_storefront_drafts_row_title">Upcoming deliveries</string>
strings.xml:6634:    <string name="photos_printingskus_printsubscription_storefront_get_started">Get started</string>
strings.xml:6635:    <string name="photos_printingskus_printsubscription_storefront_get_started_fab">Get premium prints</string>
strings.xml:6636:    <string name="photos_printingskus_printsubscription_storefront_help">Help</string>
strings.xml:6637:    <string name="photos_printingskus_printsubscription_storefront_ideas">Ideas for your print series</string>
strings.xml:6638:    <string name="photos_printingskus_printsubscription_storefront_memories_message">Relive and preserve your favorite memories from the year in a scrapbook</string>
strings.xml:6639:    <string name="photos_printingskus_printsubscription_storefront_memories_title">Keep memories for a lifetime</string>
strings.xml:6640:    <string name="photos_printingskus_printsubscription_storefront_name">Premium print series</string>
strings.xml:6641:    <string name="photos_printingskus_printsubscription_storefront_order_item_description">Series, [%s]</string>
strings.xml:6642:    <string name="photos_printingskus_printsubscription_storefront_order_item_title">Premium prints</string>
strings.xml:6643:    <string name="photos_printingskus_printsubscription_storefront_order_summary_style">4×6″ %s prints</string>
strings.xml:6644:    <string name="photos_printingskus_printsubscription_storefront_people_settings">Featured people</string>
strings.xml:6645:    <string name="photos_printingskus_printsubscription_storefront_premium_prints">Premium prints</string>
strings.xml:6646:    <string name="photos_printingskus_printsubscription_storefront_premium_prints_message">High quality prints, matte or glossy, with postcard or photo info on the back.</string>
strings.xml:6647:    <string name="photos_printingskus_printsubscription_storefront_price">%1$s/mo</string>
strings.xml:6648:    <string name="photos_printingskus_printsubscription_storefront_price_with_details">%1$s/month &lt;a href=>Details&lt;/a></string>
strings.xml:6649:    <string name="photos_printingskus_printsubscription_storefront_product_option_back_printing">Photo info — Optionally choose to print date information and postcard on your print</string>
strings.xml:6650:    <string name="photos_printingskus_printsubscription_storefront_product_option_border">Border — 1/8″ all around border</string>
strings.xml:6651:    <string name="photos_printingskus_printsubscription_storefront_product_option_glossy">Glossy — Brighter colors, higher contrast, 100lb premium paper</string>
strings.xml:6652:    <string name="photos_printingskus_printsubscription_storefront_product_option_matte">Matte — Softer colors and details,130lb premium cardstock</string>
strings.xml:6653:    <string name="photos_printingskus_printsubscription_storefront_product_option_no_border">No border — edge to edge photo</string>
strings.xml:6654:    <string name="photos_printingskus_printsubscription_storefront_product_options">Product options</string>
strings.xml:6655:    <string name="photos_printingskus_printsubscription_storefront_send_love_message">Share memories by giving a photo and a note to the people who matter</string>
strings.xml:6656:    <string name="photos_printingskus_printsubscription_storefront_send_love_title">Send your love with a photo</string>
strings.xml:6657:    <string name="photos_printingskus_printsubscription_storefront_settings_date">Date</string>
strings.xml:6658:    <string name="photos_printingskus_printsubscription_storefront_settings_date_postcard">Date, postcard</string>
strings.xml:6659:    <string name="photos_printingskus_printsubscription_storefront_settings_glossy_border">Glossy paper, border</string>
strings.xml:6660:    <string name="photos_printingskus_printsubscription_storefront_settings_glossy_no_border">Glossy paper, no border</string>
strings.xml:6661:    <string name="photos_printingskus_printsubscription_storefront_settings_matte_border">Matte paper, border</string>
strings.xml:6662:    <string name="photos_printingskus_printsubscription_storefront_settings_matte_no_border">Matte paper, no border</string>
strings.xml:6663:    <string name="photos_printingskus_printsubscription_storefront_settings_no_selection">No selection</string>
strings.xml:6664:    <string name="photos_printingskus_printsubscription_storefront_settings_postcard">Postcard</string>
strings.xml:6665:    <string name="photos_printingskus_printsubscription_storefront_shipping_payment_settings">Shipping &amp; Payment</string>
strings.xml:6666:    <string name="photos_printingskus_printsubscription_storefront_skip_month">Skip a month</string>
strings.xml:6667:    <string name="photos_printingskus_printsubscription_storefront_skip_month_message">Need a break? Skip any month you wish, or cancel anytime</string>
strings.xml:6668:    <string name="photos_printingskus_printsubscription_storefront_skip_settings">Skip month</string>
strings.xml:6669:    <string name="photos_printingskus_printsubscription_storefront_skipped_toast">Shipment skipped</string>
strings.xml:6670:    <string name="photos_printingskus_printsubscription_storefront_subscription_settings">Settings</string>
strings.xml:6671:    <string name="photos_printingskus_printsubscription_storefront_suggestion">Suggested for you</string>
strings.xml:6672:    <string name="photos_printingskus_printsubscription_storefront_suggestion_message">Start from a selection based on your preferences. Easy to review and edit.</string>
strings.xml:6673:    <string name="photos_printingskus_printsubscription_ui_back_caption">Back</string>
strings.xml:6674:    <string name="photos_printingskus_printsubscription_ui_back_options_title">Back of print</string>
strings.xml:6675:    <string name="photos_printingskus_printsubscription_ui_confirmation_action_bar_title">Confirmation</string>
strings.xml:6676:    <string name="photos_printingskus_printsubscription_ui_confirmation_message">Note: you’ll get a reminder each month to review your selected photos before they’re printed.</string>
strings.xml:6677:    <string name="photos_printingskus_printsubscription_ui_confirmation_title">"Woo-hoo!
strings.xml:6679:    <string name="photos_printingskus_printsubscription_ui_disable_border_card">No border</string>
strings.xml:6680:    <string name="photos_printingskus_printsubscription_ui_disable_border_details">Edge to edge photo</string>
strings.xml:6681:    <string name="photos_printingskus_printsubscription_ui_done_button">Done</string>
strings.xml:6682:    <string name="photos_printingskus_printsubscription_ui_edit_preview_photo">Edit</string>
strings.xml:6683:    <string name="photos_printingskus_printsubscription_ui_enable_border_card">Border</string>
strings.xml:6684:    <string name="photos_printingskus_printsubscription_ui_enable_border_details">1/8\" all around border</string>
strings.xml:6685:    <string name="photos_printingskus_printsubscription_ui_front_caption">Front</string>
strings.xml:6686:    <string name="photos_printingskus_printsubscription_ui_front_options_title">Finish and border</string>
strings.xml:6687:    <string name="photos_printingskus_printsubscription_ui_glossy_finish_card">Glossy</string>
strings.xml:6688:    <string name="photos_printingskus_printsubscription_ui_glossy_finish_details">Bright colors, high contrast</string>
strings.xml:6689:    <string name="photos_printingskus_printsubscription_ui_loading_fragment_message_one">Just a moment…</string>
strings.xml:6690:    <string name="photos_printingskus_printsubscription_ui_loading_fragment_message_three">choosing photos</string>
strings.xml:6691:    <string name="photos_printingskus_printsubscription_ui_loading_fragment_message_two">finding photos</string>
strings.xml:6692:    <string name="photos_printingskus_printsubscription_ui_matte_finish_card">Matte</string>
strings.xml:6693:    <string name="photos_printingskus_printsubscription_ui_matte_finish_details">Softer colors and details</string>
strings.xml:6694:    <string name="photos_printingskus_printsubscription_ui_next_button">Next</string>
strings.xml:6695:    <string name="photos_printingskus_printsubscription_ui_paper_finish">Paper finish</string>
strings.xml:6696:    <string name="photos_printingskus_printsubscription_ui_payment_item_message">Recurring charge each month</string>
strings.xml:6697:    <string name="photos_printingskus_printsubscription_ui_payment_item_title">%1$s/month</string>
strings.xml:6698:    <string name="photos_printingskus_printsubscription_ui_people_picker_helper_text">"Select people or pets you would like to feature. Each month we'll prioritize photos of these people or pets in your suggestions"</string>
strings.xml:6699:    <string name="photos_printingskus_printsubscription_ui_people_picker_title">People selection</string>
strings.xml:6700:    <string name="photos_printingskus_printsubscription_ui_photo_picker_caption">Select a replacement photo</string>
strings.xml:6701:    <string name="photos_printingskus_printsubscription_ui_preview_draft_title">Preview</string>
strings.xml:6702:    <string name="photos_printingskus_printsubscription_ui_preview_settings_help">Settings &amp; help</string>
strings.xml:6703:    <string name="photos_printingskus_printsubscription_ui_preview_title">Your selection</string>
strings.xml:6704:    <string name="photos_printingskus_printsubscription_ui_print_border">Print border</string>
strings.xml:6705:    <string name="photos_printingskus_printsubscription_ui_replace_preview_photo">Replace</string>
strings.xml:6706:    <string name="photos_printingskus_printsubscription_ui_save_button">Save</string>
strings.xml:6707:    <string name="photos_printingskus_printsubscription_ui_save_change_toast">Changes saved. You can still edit your selection until %1$s.</string>
strings.xml:6708:    <string name="photos_printingskus_printsubscription_ui_show_date">Show date</string>
strings.xml:6709:    <string name="photos_printingskus_printsubscription_ui_show_postcard">Show postcard</string>
strings.xml:6710:    <string name="photos_printingskus_printsubscription_ui_subscription_item_message">%1$d photos · 4×6″ prints</string>
strings.xml:6711:    <string name="photos_printingskus_printsubscription_ui_subscription_item_title">Monthly prints</string>
strings.xml:6751:    <string name="photos_printingskus_retailprints_ui_deliveryoptions_plus_shipping">+ shipping</string>
strings.xml:6752:    <string name="photos_printingskus_retailprints_ui_deliveryoptions_plus_tax">+ tax</string>
strings.xml:6753:    <string name="photos_printingskus_retailprints_ui_deliveryoptions_plus_tax_shipping">+ tax &amp; shipping</string>
strings.xml:6790:    <string name="photos_printingskus_retailprints_ui_order_plus_tax">plus tax</string>
strings.xml:6810:    <string name="photos_printingskus_retailprints_ui_pickup_price_details">%1$s plus tax</string>
strings.xml:6831:    <string name="photos_printingskus_retailprints_util_distance_max_number">%d+</string>
strings.xml:7014:    <string name="photos_printstore_error_dialog_max_photos_message">{count, plural, =1{You can select up to # photo to print at a time. Please deselect some photos and try again.} other{You can select up to # photos to print at a time. Please deselect some ph [... omitted end of lo
strings.xml:7015:    <string name="photos_printstore_error_dialog_max_photos_title">Too many photos selected</string>
strings.xml:7430:    <string name="photos_search_functional_explore_locked_promo_description">As a Google One member, you can unlock reminders, auto-archive, and more</string>
strings.xml:7974:    <string name="photos_share_handler_system_selection_too_large_message">{max_items, plural, =1 {Please select up to # item to share.} other {Please select up to # items to share.} }</string>
strings.xml:7976:    <string name="photos_share_handler_system_selection_too_large_verbose_message">{max_items, plural, =1 {Your selection is too large to share. Based on your selections, try choosing up to # item.} other {Your selection is too large to share. Based on your se [... omitted end of lo
strings.xml:8378:    <string name="photos_stories_souvenir_edit_in_capcut_picker_caption">{max_assets, plural, =1{Select {min_assets} to {max_assets} photos or videos to send to CapCut} other{Select {min_assets} to {max_assets} photos &amp; videos to send to CapCut}}</string>
strings.xml:8649:    <string name="photos_updateshub_notification_opt_in_subtitle_v2">Get alerts for activity on this page, plus memories &amp; more</string>
strings.xml:9074:    <string name="photos_varenyky_export_progress_message">Please keep the app open and the screen unlocked.</string>
strings.xml:9363:    <string name="photos_watchface_preview_add_photos_error_dialog_content">You’ve already selected the maximum number of photos (%d). Remove some selected photos to add more.</string>
strings.xml:9373:    <string name="photos_watchface_preview_selection_max">{count, plural, =1{Select up to # photo} other{Select up to # photos}}</string>
strings.xml:9556:    <string name="subscriptions_clean_up_space">Clean up space</string>
strings.xml:9557:    <string name="subscriptions_continue_in_browser_button_text">Continue in browser</string>
strings.xml:9558:    <string name="subscriptions_data_failed_to_load">"Couldn't load data"</string>
strings.xml:9559:    <string name="subscriptions_error_opening_browser">"Couldn't open browser"</string>
strings.xml:9560:    <string name="subscriptions_exempt_storage_used">%1$s &lt;red-50-opacity>&lt;s>%2$s&lt;/s>&lt;/red-50-opacity></string>
strings.xml:9561:    <string name="subscriptions_get_storage">Get storage</string>
strings.xml:9562:    <string name="subscriptions_launch_play_flow_error">"Can't connect to Play's billing service"</string>
strings.xml:9563:    <string name="subscriptions_pbl_error">Temporary error occurred. Try again later.</string>
strings.xml:9564:    <string name="subscriptions_pbl_event_received">Purchase event received</string>
strings.xml:9565:    <string name="subscriptions_sdn_network_error_description">Please try again later.</string>
strings.xml:9566:    <string name="subscriptions_sdn_network_error_title">Network error.</string>
strings.xml:9567:    <string name="subscriptions_storage">Storage</string>
strings.xml:9568:    <string name="subscriptions_storage_used">Storage used</string>
strings.xml:9569:    <string name="subscriptions_update_button_text">Update app</string>
strings.xml:9591:    <string name="super_g_path_cover_24">M12,14.26V10H22.36C22.49,10.72 22.56,11.47 22.56,12.25C22.56,12.943 22.509,13.614 22.409,14.26H17.92H12Z</string>
strings.xml:9592:    <string name="super_g_path_main_24">M12,18.63C15.23,18.63 17.45,16.79 17.92,14.26L20,12L22.409,14.26C21.604,19.462 17.649,23 12,23C5.92,23 1,18.08 1,12C1,5.92 5.92,1 12,1C14.97,1 17.45,2.09 19.36,3.87L16.21,7.02C15.06,5.94 13.62,5.38 12,5.38C8.41,5.38 5.49 [... omitted end of lo
strings.xml:9672:    <string name="tracing_token_summary">A token is required. See go/gplus-trace</string>
```

### data_copy — 272 strings

```
plurals.xml:57:    <plurals name="photos_album_enrichment_ui_locations_added">
plurals.xml:58:        <item quantity="other">%d locations added</item>
plurals.xml:59:        <item quantity="one">%d location added</item>
plurals.xml:61:    <plurals name="photos_album_enrichment_ui_locations_and_maps_added_location_subsentence">
plurals.xml:62:        <item quantity="other">%d locations</item>
plurals.xml:63:        <item quantity="one">%d location</item>
plurals.xml:65:    <plurals name="photos_album_enrichment_ui_locations_and_maps_added_maps_subsentence">
plurals.xml:280:    <plurals name="photos_location_edits_ui_batch_location_editing_toast">
strings.xml:24:    <string name="about_these_results_body">When searching for businesses or places near a location, Google Maps will show local results. Several factors - primarily relevance, distance and prominence - are combined to help find the best results for a search.< [... omitted end of long
strings.xml:673:    <string name="peoplekit_facerows_no_contacts">No contacts</string>
strings.xml:674:    <string name="peoplekit_facerows_search_contacts">Search contacts</string>
strings.xml:675:    <string name="peoplekit_facerows_show_phone_contacts">Show phone contacts</string>
strings.xml:680:    <string name="peoplekit_hide_suggestion_device_contact_cannot_be_hidden_text">To hide this suggestion, you must delete this person from your contacts.</string>
strings.xml:704:    <string name="peoplekit_listview_phone_contacts">All contacts</string>
strings.xml:708:    <string name="peoplekit_listview_show_phone_contacts">Show phone contacts</string>
strings.xml:767:    <string name="photos_activitybasedpersonalization_promos_description">Your Photos experience is now more personalized. Manage settings.</string>
strings.xml:790:    <string name="photos_album_enrichment_ui_add_location_title">Add location</string>
strings.xml:792:    <string name="photos_album_enrichment_ui_add_place_enrichments_popup_add_suggested_locations_item">All suggested locations</string>
strings.xml:793:    <string name="photos_album_enrichment_ui_add_place_enrichments_popup_add_suggested_locations_item_description">Add all suggested locations</string>
strings.xml:794:    <string name="photos_album_enrichment_ui_add_place_enrichments_popup_location_item">Location</string>
strings.xml:795:    <string name="photos_album_enrichment_ui_add_place_enrichments_popup_location_item_description">Add location</string>
strings.xml:799:    <string name="photos_album_enrichment_ui_adding_suggested_locations">Adding locations…</string>
strings.xml:801:    <string name="photos_album_enrichment_ui_edit_location_title">Edit Location</string>
strings.xml:804:    <string name="photos_album_enrichment_ui_error_adding_location">"Couldn't add location to the album"</string>
strings.xml:807:    <string name="photos_album_enrichment_ui_fetch_place_enrichment_autocomplete_suggestions">Unable to get location suggestions.</string>
strings.xml:808:    <string name="photos_album_enrichment_ui_location_editing_check_icon_description">Check icon</string>
strings.xml:809:    <string name="photos_album_enrichment_ui_location_editing_custom_name_decoration">\"%s\"</string>
strings.xml:810:    <string name="photos_album_enrichment_ui_location_editing_custom_subtitle">Use your own name</string>
strings.xml:811:    <string name="photos_album_enrichment_ui_location_editing_delete_text_description">Delete text</string>
strings.xml:812:    <string name="photos_album_enrichment_ui_location_editing_hint_text">Location</string>
strings.xml:813:    <string name="photos_album_enrichment_ui_location_editing_search_image_description">Search image</string>
strings.xml:814:    <string name="photos_album_enrichment_ui_locations_and_maps_added_template">%1$s &amp; %2$s added</string>
strings.xml:822:    <string name="photos_album_enrichment_ui_no_locations_suggested">No locations found</string>
strings.xml:823:    <string name="photos_album_enrichment_ui_saving_location_progress_message">Saving location…</string>
strings.xml:995:    <string name="photos_allphotos_gridcontrols_show_third_party_content_top_level_setting_title">Show content from other apps</string>
strings.xml:1241:    <string name="photos_autobackuppromos_bbd_compare_memories">See memories personalized with your photos</string>
strings.xml:1245:    <string name="photos_autobackuppromos_bbd_compare_search">Search photos by people, pets, locations, and more</string>
strings.xml:1276:    <string name="photos_autobackuppromos_security_description">Google Photos uses world-class security, and we don’t use your photos for advertising. You control how you share your photos.</string>
strings.xml:1398:    <string name="photos_backup_settings_backup_benefits_memories">See memories personalized with your photos</string>
strings.xml:1400:    <string name="photos_backup_settings_backup_benefits_search">Search photos by people, pets, locations, and more</string>
strings.xml:1784:    <string name="photos_cloudstorage_g1_tos_photos_storage_with_discount_in_eu_23q3">Personalized pricing. Cancel anytime. By subscribing, you agree to &lt;a href=>our terms of service&lt;/a> and &lt;a href=>offer terms&lt;/a>. See how &lt;a href=>Google hand [... omitted end of lo
strings.xml:2106:    <string name="photos_collectionstab_places_empty_state_button_text">Manage location settings</string>
strings.xml:2108:    <string name="photos_collectionstab_places_empty_state_subheading">Your photos are organized by the location where they were taken</string>
strings.xml:2321:    <string name="photos_create_viewbinder_partneraccount_shareback_title_personalized">"Share back with
strings.xml:2417:    <string name="photos_dateheaders_locations_2_location_headers">%1$s &amp; %2$s</string>
strings.xml:2418:    <string name="photos_dateheaders_locations_3_location_headers">%1$s, %2$s, %3$s</string>
strings.xml:2419:    <string name="photos_dateheaders_locations_4_location_headers">%1$s, %2$s, %3$s, %4$s</string>
strings.xml:2420:    <string name="photos_dateheaders_locations_5_location_headers">%1$s, %2$s, %3$s, %4$s, %5$s</string>
strings.xml:2421:    <string name="photos_dateheaders_locations_6_location_headers">%1$s, %2$s, %3$s, %4$s, %5$s, %6$s</string>
strings.xml:2422:    <string name="photos_dateheaders_locations_location_count">{count, plural, =1{1 location} other{# locations}}</string>
strings.xml:2423:    <string name="photos_dateheaders_locations_locationlabeledu_message">Your Google Maps labels are now searchable here. &lt;a href=\"%1$s\" >Learn more&lt;/a></string>
strings.xml:2502:    <string name="photos_devicesetup_guide_banner_personalized_title">You’re so close, %1$s</string>
strings.xml:2503:    <string name="photos_devicesetup_guide_banner_personalized_title_fallback">You’re so close</string>
strings.xml:2629:    <string name="photos_editor_bluejay_ineligible_location_message">This feature is not yet available in some countries.</string>
strings.xml:2638:    <string name="photos_editor_bluejay_kefir_consolidated_gai_ack_text">This tool uses GenAI technology, so results may be inaccurate or unexpected. Your use is subject to Google’s <annotation action="gai_policy_link">GenAI Prohibited Use Policy</annotation>. [... omitted end of lo
strings.xml:2641:    <string name="photos_editor_bluejay_kefir_gai_ack_text">This tool uses experimental GenAI technology, so results may be inaccurate or unexpected. Your use is subject to Google’s <annotation action="gai_policy_link">GenAI Prohibited Use Policy</annotation>. [... omitted end of lo
strings.xml:2643:    <string name="photos_editor_bluejay_kefir_life_understanding_primer_body">Do a quick setup for more personalized templates. Turn on Gemini features in Photos to process insights about you from your photos and videos. This will also allow you to access Ask  [... omitted end of lo
strings.xml:2644:    <string name="photos_editor_bluejay_kefir_life_understanding_primer_title">Unlock more fun, personalized edits</string>
strings.xml:3117:    <string name="photos_ellmann_genaiconsent_face_grouping_optout_dialog_message">Face grouping is essential to you getting the best experience. It personalizes search, albums, memories, and more. You can change this setting any time.</string>
strings.xml:3120:    <string name="photos_ellmann_genaiconsent_me_cluster_optout_dialog_title">Don’t allow this type of personalization?</string>
strings.xml:3125:    <string name="photos_ellmann_genaiconsent_upgrade_dialog_body">Google Photos can now tell you more about where you’ve been by matching your face to the locations in your photos with the help of Gemini models. <annotation action="learn_more_link">Learn more [... omitted end of lo
strings.xml:3126:    <string name="photos_ellmann_genaiconsent_upgrade_dialog_title">Improving Gemini features in Photos with location info</string>
strings.xml:3133:    <string name="photos_ellmann_hub_face_opt_in_subtitle">Turn on Face Groups, and select your face so we know who to personalize for</string>
strings.xml:3136:    <string name="photos_ellmann_hub_face_select_opt_in_title">Personalize the app to you</string>
strings.xml:3139:    <string name="photos_ellmann_hub_location_opt_in_subtitle">Allow Google Photos to estimate locations when they’re missing</string>
strings.xml:3140:    <string name="photos_ellmann_hub_location_opt_in_title">Get more location results in search</string>
strings.xml:3153:    <string name="photos_ellmann_mecluster_choose_face_title">Tap on your face to personalize your experience</string>
strings.xml:3154:    <string name="photos_ellmann_mecluster_disclaimer">Your face will be used to personalize search, memories, creations and more. You may also be associated with photo locations based on photos with your face. <annotation action="learn_more_link">Learn more</ [... omitted end of lo
strings.xml:3160:    <string name="photos_ellmann_mecluster_promo_disclaimer">Your face will be used to personalize search, memories, creations and more. You may also be associated with photo locations based on photos with your face. <annotation action="learn_more_link">Learn  [... omitted end of lo
strings.xml:3167:    <string name="photos_ellmann_mecluster_remove_dialog_desc">You’ll miss out on personalized search and creations</string>
strings.xml:3252:    <string name="photos_ellmann_onboarding_location_crater_lake">Crater Lake</string>
strings.xml:3253:    <string name="photos_ellmann_onboarding_location_description">When locations are missing, Google Photos can use landmarks and other sources to estimate locations. <annotation id="use_location_link">Learn more</annotation></string>
strings.xml:3254:    <string name="photos_ellmann_onboarding_location_not_now_1">Not now</string>
strings.xml:3255:    <string name="photos_ellmann_onboarding_location_optout_dialog_message">Estimating locations gives you more results when you search. You can change this setting any time</string>
strings.xml:3256:    <string name="photos_ellmann_onboarding_location_optout_dialog_title">Don’t allow location estimation</string>
strings.xml:3257:    <string name="photos_ellmann_onboarding_location_oregon">Oregon</string>
strings.xml:3258:    <string name="photos_ellmann_onboarding_location_title">Want more results when searching by location?</string>
strings.xml:3259:    <string name="photos_ellmann_onboarding_location_turn_on_1">Turn on</string>
strings.xml:3260:    <string name="photos_ellmann_onboarding_no_faces_dialog_message">You need photos of yourself backed up in your library to turn on personalization</string>
strings.xml:3285:    <string name="photos_ellmann_select_me_cluster_subtitle">Personalize your experience</string>
strings.xml:3317:    <string name="photos_ellmann_updated_disclaimer_1">Your face will be used to personalize search, memories, creations and more. You may also be associated with photo locations based on photos with your face. <annotation action="learn_more_link">Learn more</ [... omitted end of lo
strings.xml:3456:    <string name="photos_envelope_settings_locationsharing_bottom_sheet_title">Album options</string>
strings.xml:3457:    <string name="photos_envelope_settings_locationsharing_caption">Anyone with an invitation will be able to join, view and add photos to this album</string>
strings.xml:3458:    <string name="photos_envelope_settings_locationsharing_collab_off_caption">Anyone with an invitation will be able to join and view this album</string>
strings.xml:3459:    <string name="photos_envelope_settings_locationsharing_collab_off_location_off">People with an invitation will be able to join and view this album. Photo locations will not be shared. <annotation action="album_location_options">Open album options</annotati [... omitted end of lo
strings.xml:3460:    <string name="photos_envelope_settings_locationsharing_collab_off_location_on">People with an invitation will be able to join, view, and see photo locations in this album. <annotation action="album_location_options">Open album options</annotation></string> [... omitted end of lo
strings.xml:3461:    <string name="photos_envelope_settings_locationsharing_collab_on_location_off">People with an invitation will be able to join, view, or add photos. Photo locations will not be shared. <annotation action="album_location_options">Open album options</annotati [... omitted end of lo
strings.xml:3462:    <string name="photos_envelope_settings_locationsharing_collab_on_location_on">People with an invitation will be able to join, view, or add photos, as well as see photo locations in this album. <annotation action="album_location_options">Open album options< [... omitted end of lo
strings.xml:3463:    <string name="photos_envelope_settings_locationsharing_error_updating">Unable to update setting</string>
strings.xml:3464:    <string name="photos_envelope_settings_locationsharing_generic_with_items">{count, plural, =1 {1 item} other {{count} items} }</string>
strings.xml:3465:    <string name="photos_envelope_settings_locationsharing_hidden_with_items">{count, plural, =1 {Location hidden, 1 item} other {Location hidden, {count} items} }</string>
strings.xml:3466:    <string name="photos_envelope_settings_locationsharing_location_default_on_tooltip_banner_body">You can turn it off in album options</string>
strings.xml:3467:    <string name="photos_envelope_settings_locationsharing_location_default_on_tooltip_banner_title">Photo location is ON by default</string>
strings.xml:3468:    <string name="photos_envelope_settings_locationsharing_network_unavailable_error_updating">You need an internet connection to update location settings</string>
strings.xml:3469:    <string name="photos_envelope_settings_locationsharing_saving_changes">Saving changes</string>
strings.xml:3470:    <string name="photos_envelope_settings_locationsharing_share_photo_location_setting_description_with_learn_more_link">Let others see where your shared photos were taken. &lt;a href=help:>Learn more&lt;/a></string>
strings.xml:3471:    <string name="photos_envelope_settings_locationsharing_share_photo_location_setting_title_v2">Share photo locations</string>
strings.xml:3472:    <string name="photos_envelope_settings_locationsharing_update_pending_text">Updating location settings…</string>
strings.xml:3473:    <string name="photos_envelope_settings_locationsharing_visible_with_items">{count, plural, =1 {Location included, 1 item} other {Location included, {count} items} }</string>
strings.xml:3523:    <string name="photos_facegaia_optin_impl_picker_remove_dialog_face_sharing_off_desc">"You'll miss out on personalized search and creations"</string>
strings.xml:3654:    <string name="photos_flyingsky_fragment_bulk_naming_banner_subtitle">Personalize your memories</string>
strings.xml:3750:    <string name="photos_genaiconsent_item_data_process_subtitle_v3_1">"Insights from your photos and videos and Google Account, as well as data you store in your Remember List and Google Account (e.g. age, gender, name) will be used to enhance and personalize [... omitted end of lo
strings.xml:3752:This enables features like Ask Photos, album title suggestions, and smart, personalized editing."</string>
strings.xml:3757:    <string name="photos_genaiconsent_item_location_subtitle">Photos may infer your location, including associating your face in a photo with the photo’s corresponding location data and timestamp. You can stop this processing at any time in the Photos app.</st [... omitted end of lo
strings.xml:3758:    <string name="photos_genaiconsent_item_location_subtitle_1">Insights include inferring your location using information from your photos. This includes associating you with a photo’s location data and timestamp when your face group is in that photo. <annota [... omitted end of lo
strings.xml:3759:    <string name="photos_genaiconsent_item_location_title">Determine your location</string>
strings.xml:3760:    <string name="photos_genaiconsent_item_location_title_v4_1">Infer your location from photos</string>
strings.xml:3778:    <string name="photos_genaiconsent_settings_opt_out_dialog_message_retention_enabled">"You’ll lose access to Gemini features in Photos, like Ask Photos and smart, personalized editing. Your experience overall will be less personalized.
strings.xml:3783:    <string name="photos_genaiconsent_settings_opt_out_dialog_message_v2">"This will permanently delete any data in your Remember List. You’ll lose access to Gemini features in Photos, like Ask Photos and more personalized memories.
strings.xml:3788:    <string name="photos_genaiconsent_settings_remember_list_subtitle">Control what data we use for personalization</string>
strings.xml:3805:    <string name="photos_gridactionpanel_viewbinder_location">Location</string>
strings.xml:3907:        >Korean Location Terms of Service, Google Terms of Service, and Google Privacy Policy&lt;/a>"</string>
strings.xml:3908:    <string name="photos_legal_korean_terms_of_service_dialog_text">By continuing, you agree to the &lt;a href=%s >Location Terms of Service, Google Terms of Service, and Google Privacy Policy&lt;/a>.</string>
strings.xml:3970:    <string name="photos_location_camerasettingspromo_description">Open your camera app and turn on camera location in settings. &lt;a href=help:>Learn more&lt;/a></string>
strings.xml:3971:    <string name="photos_location_camerasettingspromo_open_camera">Open Camera</string>
strings.xml:3972:    <string name="photos_location_camerasettingspromo_settings">Update Camera settings</string>
strings.xml:3973:    <string name="photos_location_camerasettingspromo_title_b">Turn on camera location to see more photos organized and searchable by place</string>
strings.xml:3974:    <string name="photos_location_edits_feedback">Dogfooders - <u>send feedback</u></string>
strings.xml:3975:    <string name="photos_location_edits_info_icon_content_description">Info icon</string>
strings.xml:3976:    <string name="photos_location_edits_ui_batch_location_editing_dialog_cancel_button">Cancel</string>
strings.xml:3977:    <string name="photos_location_edits_ui_batch_location_editing_dialog_learn_more">Learn More</string>
strings.xml:3978:    <string name="photos_location_edits_ui_batch_location_editing_dialog_message">"Google Photos can't edit location information in %1$s of these photos because either they are not backed up or those locations were added by your camera"</string>
strings.xml:3979:    <string name="photos_location_edits_ui_batch_location_editing_dialog_title">"Can't edit all locations"</string>
strings.xml:3980:    <string name="photos_location_edits_ui_batch_location_editing_none_dialog_message">"Google Photos can't edit location information because either the photos are not backed up or the location information was added by your camera."</string>
strings.xml:3981:    <string name="photos_location_edits_ui_batch_location_editing_none_dialog_title">"Can't edit location information"</string>
strings.xml:3982:    <string name="photos_location_edits_ui_location_editing_content_hint">Where was this taken?</string>
strings.xml:3983:    <string name="photos_location_edits_ui_location_editing_delete_text_description">Delete location search</string>
strings.xml:3984:    <string name="photos_location_edits_ui_location_editing_privacy_warning">Edits to location will only be seen within Google Photos</string>
strings.xml:3985:    <string name="photos_location_edits_ui_location_editing_remove_location">Remove Location</string>
strings.xml:3986:    <string name="photos_location_edits_ui_location_editing_search_hint">Enter location</string>
strings.xml:3987:    <string name="photos_location_promo_dialog_message_without_inferred_location">"Google Photos uses location to help you organize and search your photos.
strings.xml:3989: Location may come from info such as:
strings.xml:3992:    <string name="photos_location_promo_dialog_policy_message_title">Locations in Photos</string>
strings.xml:3993:    <string name="photos_location_promo_location_icon_content_description">Location icon</string>
strings.xml:4031:    <string name="photos_mapexplore_ui_current_location">Current location</string>
strings.xml:4032:    <string name="photos_mapexplore_ui_estimated_location_text">View and manage estimated locations</string>
strings.xml:4033:    <string name="photos_mapexplore_ui_estimated_locations">Estimated locations • </string>
strings.xml:4036:    <string name="photos_mapexplore_ui_exifprompt_no_location_desc">Turn on camera location to see future photos on your map</string>
strings.xml:4042:    <string name="photos_mapexplore_ui_interstitial_relive_message_without_inferred_location">"Relive the places you’ve been by exploring your photos that have location info, including shared photos you’ve saved. Your map uses location info such as:
strings.xml:4054:    <string name="photos_mapexplore_ui_options_impl_info_message">Your map shows photos including shared photos you save. It uses location info such as:</string>
strings.xml:4078:    <string name="photos_mars_actionhandler_mars_move_to_temporary_info_collections">{count, plural, =1{The original location of this item is no longer available. You can find Temporary with your other device folders under the Collections tab in Google Photos. [... omitted end of lo
strings.xml:4187:    <string name="photos_mediadetails_conversation_location_sharing_notice">People in this conversation can’t see this photo’s location</string>
strings.xml:4220:    <string name="photos_mediadetails_location_copied_clipboard">Location copied to clipboard</string>
strings.xml:4221:    <string name="photos_mediadetails_location_details_map_content_description">Map of the location at which the photo was taken</string>
strings.xml:4222:    <string name="photos_mediadetails_location_edit_icon_content_description">Edit Photo Location</string>
strings.xml:4223:    <string name="photos_mediadetails_location_edit_not_supported_exif">"Can't edit locations added by your camera."</string>
strings.xml:4224:    <string name="photos_mediadetails_location_edit_not_supported_learn_more">Learn more</string>
strings.xml:4225:    <string name="photos_mediadetails_location_edits_feedback">Send feedback</string>
strings.xml:4226:    <string name="photos_mediadetails_location_exif_inferred_location_learn_more_label_v2">Estimated location</string>
strings.xml:4227:    <string name="photos_mediadetails_location_exif_inferred_location_remove_dialog_confirm_option">Remove</string>
strings.xml:4228:    <string name="photos_mediadetails_location_exif_inferred_location_remove_dialog_title">Remove location?</string>
strings.xml:4229:    <string name="photos_mediadetails_location_exif_inferred_location_remove_menu_item">Remove Location</string>
strings.xml:4230:    <string name="photos_mediadetails_location_exif_location_reverse_geocoding_loading">Loading…</string>
strings.xml:4231:    <string name="photos_mediadetails_location_explore_now_content_description">Launch the Map Explore flow</string>
strings.xml:4232:    <string name="photos_mediadetails_location_from_file">Location from file</string>
strings.xml:4233:    <string name="photos_mediadetails_location_inferred_location_removal_error">Error removing location.</string>
strings.xml:4234:    <string name="photos_mediadetails_location_info_icon_content_description">Info icon</string>
strings.xml:4235:    <string name="photos_mediadetails_location_local_photo_location_dialog_back_up_option">Back up now</string>
strings.xml:4236:    <string name="photos_mediadetails_location_local_photo_location_dialog_message">Locations can only be added to backed-up photos</string>
strings.xml:4237:    <string name="photos_mediadetails_location_local_photo_location_dialog_ok_option">OK</string>
strings.xml:4238:    <string name="photos_mediadetails_location_no_exif_location">Add a location</string>
strings.xml:4239:    <string name="photos_mediadetails_location_open_in_maps">Open in Maps</string>
strings.xml:4240:    <string name="photos_mediadetails_location_removed_from_google_photos">Removed from Google Photos</string>
strings.xml:4241:    <string name="photos_mediadetails_location_removed_from_google_photos_desc">This file still contains location information that cannot be removed by Google Photos</string>
strings.xml:4242:    <string name="photos_mediadetails_location_sharing_notice">People in this album can’t see this photo’s location</string>
strings.xml:4336:    <string name="photos_memories_actions_personalize_video_button">Personalize video</string>
strings.xml:4560:    <string name="photos_memories_settings_video_lane_summary">Personalized feed of your videos</string>
strings.xml:4794:    <string name="photos_offline_action_add_location_item_to_album">You need an internet connection to add a location</string>
strings.xml:4796:    <string name="photos_offline_action_add_suggested_locations_to_album">You need an internet connection to add suggested locations</string>
strings.xml:4816:    <string name="photos_offline_action_edit_locations">You need an internet connection to edit locations</string>
strings.xml:4818:    <string name="photos_offline_action_edit_story_location">You need an internet connection to change a location</string>
strings.xml:4886:    <string name="photos_pager_composeviews_time_location_delimiter">" • "</string>
strings.xml:4985:    <string name="photos_partneraccount_grid_promobanner_autosave_turn_on_auto_save_personalized">Auto-save pictures from %1$s</string>
strings.xml:5015:    <string name="photos_partneraccount_onboarding_confirm_photos_access_location_data_text">The location where your shared photos were taken</string>
strings.xml:5036:    <string name="photos_partneraccount_onboarding_v2_autosave_title_personalized_v2">Turn on auto-save so you never miss a photo from %1$s</string>
strings.xml:5054:    <string name="photos_partneraccount_onboarding_v2_inclusion_card_third_party_option">Include content from other Android apps</string>
strings.xml:5055:    <string name="photos_partneraccount_onboarding_v2_inclusion_card_third_party_summary_exclude">Excluding content from other Android apps</string>
strings.xml:5056:    <string name="photos_partneraccount_onboarding_v2_inclusion_card_third_party_summary_include">Including content from other Android apps</string>
strings.xml:5057:    <string name="photos_partneraccount_onboarding_v2_location_visibility_disclaimer_text">Your partner will be able to see where your shared photos were taken</string>
strings.xml:5061:    <string name="photos_partneraccount_onboarding_v2_receive_decline_confirm_dialog_title_personalized">Decline %1$s’s invite?</string>
strings.xml:5067:    <string name="photos_partneraccount_onboarding_v2_receive_partner_invitation_title_personalized">%1$s wants to start sharing with you</string>
strings.xml:5089:    <string name="photos_partneraccount_onboarding_v2_shareback_title_personalized">"Share back with
strings.xml:5121:    <string name="photos_partneraccount_receive_invitation_dialog_message_personalized_v3">You’ll be able to view photos shared by %1$s. None of your photos will be shared.</string>
strings.xml:5125:    <string name="photos_partneraccount_receive_invitation_has_shared_library_dialog_message_personalized_v3">You’ll be able to view photos shared by %1$s.</string>
strings.xml:5129:    <string name="photos_partneraccount_receive_partner_invitation_dialog_title_personalized">%1$s wants to share photos with you</string>
strings.xml:5130:    <string name="photos_partneraccount_receive_partner_invitation_dialog_title_personalized_v2">%1$s wants to start Partner Sharing with you</string>
strings.xml:5131:    <string name="photos_partneraccount_settings_content_include_third_party_setting_option">Include content from other Android apps</string>
strings.xml:5132:    <string name="photos_partneraccount_settings_content_include_third_party_summary_exclude">Excluding content from other Android apps</string>
strings.xml:5133:    <string name="photos_partneraccount_settings_content_include_third_party_summary_include">Including content from other Android apps</string>
strings.xml:5179:    <string name="photos_partneraccount_settings_sender_summary_location_hidden">%1$s can’t see where your shared photos were taken</string>
strings.xml:5180:    <string name="photos_partneraccount_settings_sender_summary_location_visible">The location where your shared photos were taken</string>
strings.xml:5182:    <string name="photos_partneraccount_settings_sender_summary_share_location">To check if %1$s is able to see where your shared photos were taken, visit Google Photos in your browser to view your location sharing settings.</string>
strings.xml:6059:    <string name="photos_photofragment_ask_flexbrain_tools_tooltip">New! Ask Photos can now take actions like updating a photo’s description, date, or location</string>
strings.xml:6146:    <string name="photos_photoframes_devices_location_other">Other</string>
strings.xml:6732:    <string name="photos_printingskus_retailprints_ui_checkout_contact_show_contact_label">Show contacts</string>
strings.xml:6763:    <string name="photos_printingskus_retailprints_ui_location_actionbar_title">Pick up location</string>
strings.xml:6764:    <string name="photos_printingskus_retailprints_ui_location_clear_location_search_button">Clear location search text</string>
strings.xml:6765:    <string name="photos_printingskus_retailprints_ui_location_close_time">Open until %s</string>
strings.xml:6766:    <string name="photos_printingskus_retailprints_ui_location_confirm_location">Select location</string>
strings.xml:6767:    <string name="photos_printingskus_retailprints_ui_location_current_location">Current location</string>
strings.xml:6768:    <string name="photos_printingskus_retailprints_ui_location_my_location_button">Use your location</string>
strings.xml:6769:    <string name="photos_printingskus_retailprints_ui_location_no_location_found">No results found</string>
strings.xml:6770:    <string name="photos_printingskus_retailprints_ui_location_obtain_current_location_error">Error obtaining your location</string>
strings.xml:6771:    <string name="photos_printingskus_retailprints_ui_location_obtain_current_location_not_found">Could not find your location</string>
strings.xml:6772:    <string name="photos_printingskus_retailprints_ui_location_open_24_hours">Open 24 hours</string>
strings.xml:6773:    <string name="photos_printingskus_retailprints_ui_location_open_time">Opens %s</string>
strings.xml:6774:    <string name="photos_printingskus_retailprints_ui_location_ready_future">Ready %1$s-%2$s %3$s</string>
strings.xml:6775:    <string name="photos_printingskus_retailprints_ui_location_ready_today">Ready %1$s-%2$s</string>
strings.xml:6776:    <string name="photos_printingskus_retailprints_ui_location_ready_tomorrow">Ready tomorrow %1$s-%2$s</string>
strings.xml:6777:    <string name="photos_printingskus_retailprints_ui_location_search_conn_err_msg">Make sure your device is connected to the internet and try again</string>
strings.xml:6778:    <string name="photos_printingskus_retailprints_ui_location_search_conn_err_title">Can’t find location</string>
strings.xml:6779:    <string name="photos_printingskus_retailprints_ui_location_search_error_toast">Unable to find stores</string>
strings.xml:6780:    <string name="photos_printingskus_retailprints_ui_location_search_location">Search this area</string>
strings.xml:6781:    <string name="photos_printingskus_retailprints_ui_location_search_location_hint">Search location</string>
strings.xml:6782:    <string name="photos_printingskus_retailprints_ui_location_store_details">%1$s • %2$s</string>
strings.xml:6783:    <string name="photos_printingskus_retailprints_ui_location_store_header_distant_km">%d+ km away</string>
strings.xml:6784:    <string name="photos_printingskus_retailprints_ui_location_store_header_distant_mi">%d+ miles away</string>
strings.xml:6785:    <string name="photos_printingskus_retailprints_ui_location_store_header_nearby">Nearby</string>
strings.xml:6786:    <string name="photos_printingskus_retailprints_ui_location_store_header_other">Other Locations</string>
strings.xml:6787:    <string name="photos_printingskus_retailprints_ui_location_store_header_previous">Previous</string>
strings.xml:6788:    <string name="photos_printingskus_retailprints_ui_location_store_not_available">Printing not available</string>
strings.xml:6789:    <string name="photos_printingskus_retailprints_ui_location_store_not_available_button">Location unavailable</string>
strings.xml:6804:    <string name="photos_printingskus_retailprints_ui_pickup_location_call_store_for_pickup_time">&lt;a href=%s>Call store&lt;/a> for pick up time</string>
strings.xml:7289:    <string name="photos_search_ellmannchat_dialog_body">Knowing which face is yours is required for Google Photos to deliver this more personalized experience to you.</string>
strings.xml:7521:    <string name="photos_search_peoplegroupingonboarding_promo_recapture_desc_certain_geo">Turning off face grouping will delete all your face groups and names. You won’t be able to search for people, and won’t have access to certain personalized Memories or c [... omitted end of lo
strings.xml:7522:    <string name="photos_search_peoplegroupingonboarding_promo_recapture_desc_global_opt_in_personalized_copy2_1face">Turning off Face Groups will &lt;b>delete face groups for %1$s, and all others&lt;/b>. You won’t be able to keep using Face Groups to personal [... omitted end of lo
strings.xml:7523:    <string name="photos_search_peoplegroupingonboarding_promo_recapture_desc_global_opt_in_personalized_copy2_2faces">Turning off Face Groups will &lt;b>delete face groups for %1$s, %2$s, and all others&lt;/b>. You won’t be able to keep using Face Groups to p [... omitted end of lo
strings.xml:7524:    <string name="photos_search_peoplegroupingonboarding_promo_recapture_desc_global_opt_in_personalized_copy2_3faces">Turning off Face Groups will &lt;b>delete face groups for %1$s, %2$s, %3$s, and all others&lt;/b>. You won’t be able to keep using Face Group [... omitted end of lo
strings.xml:7525:    <string name="photos_search_peoplegroupingonboarding_promo_recapture_desc_global_opt_in_personalized_copy2_4faces">Turning off Face Groups will &lt;b>delete face groups for %1$s, %2$s, %3$s, %4$s, and all others&lt;/b>. You won’t be able to keep using Face [... omitted end of lo
strings.xml:7526:    <string name="photos_search_peoplegroupingonboarding_promo_recapture_desc_v2">Your photos won’t be organized by person or made into some kinds of personalized movies &amp; collages. Your face groups are never shared publicly.</string>
strings.xml:7527:    <string name="photos_search_peoplegroupingonboarding_promo_recapture_description_global_opt_in">Turning off Face Groups will delete all your face groups and names. You won’t be able to keep using Face Groups to personalize search, albums, memories, and oth [... omitted end of lo
strings.xml:7567:    <string name="photos_search_peoplelabeling_contacts_item_title">Show results from contacts</string>
strings.xml:7576:    <string name="photos_search_peoplelabeling_frequent_contacts_header">Frequent contacts</string>
strings.xml:7677:    <string name="photos_selection_cabmode_bulk_location_edits">Edit location</string>
strings.xml:7709:    <string name="photos_settings_activity_personalization_body">Manage how Google Photos uses your data to personalize your Photos experience such as memories. &lt;a href=help:>Learn more&lt;/a></string>
strings.xml:7710:    <string name="photos_settings_activity_personalization_title">Activity-based personalization</string>
strings.xml:7727:    <string name="photos_settings_dialog_disable_location_sharing_confirm">Confirm</string>
strings.xml:7735:    <string name="photos_settings_faceclustering_advanced_my_face_disclaimer_off">Your face will be used to personalize search, memories, creations and more. You may also be associated with photo locations based on photos with your face. &lt;a href=help:>Learn [... omitted end of lo
strings.xml:7736:    <string name="photos_settings_faceclustering_advanced_my_face_disclaimer_on">Your face is used to personalize search, memories, creations and more. You may also be associated with photo locations based on photos with your face. &lt;a href=help:>Learn more& [... omitted end of lo
strings.xml:7742:    <string name="photos_settings_faceclustering_face_recognition_off_dialog_message">"Your photos won't be organized by people or made into some kinds of personalized movies &amp; collages. Any changes you've made to your face groups like added names will be  [... omitted end of lo
strings.xml:7822:    <string name="photos_settings_license_summary">Notice and license details for third party software</string>
strings.xml:7823:    <string name="photos_settings_license_title">Third Party Notices</string>
strings.xml:7824:    <string name="photos_settings_location_delete_location_history_delete">Delete</string>
strings.xml:7825:    <string name="photos_settings_location_delete_location_history_recapture_summary">Deleting estimated photo locations based on Location History may result in permanent loss of those estimated locations. Your photos will be kept.</string>
strings.xml:7826:    <string name="photos_settings_location_delete_location_history_recapture_title">Delete your existing estimated locations?</string>
strings.xml:7827:    <string name="photos_settings_location_delete_location_history_summary">If you change your mind about the estimated locations you previously chose to keep, you can still delete them. Afterward, we’ll try to re-estimate locations using other data sources wh [... omitted end of lo
strings.xml:7828:    <string name="photos_settings_location_delete_location_history_title">Delete estimated locations that may use Location History</string>
strings.xml:7829:    <string name="photos_settings_location_history_exit_will_be_deleted">Your estimated locations will be deleted. This may take a few hours or more to complete.</string>
strings.xml:7830:    <string name="photos_settings_location_options_button_subtitle">Manage your location settings</string>
strings.xml:7831:    <string name="photos_settings_location_setting_camera_settings_summary">Review whether your camera app adds location info to photos</string>
strings.xml:7832:    <string name="photos_settings_location_setting_camera_settings_title">Camera settings</string>
strings.xml:7833:    <string name="photos_settings_location_setting_location_sources_summary">Manage how your photos get location data</string>
strings.xml:7834:    <string name="photos_settings_location_setting_location_sources_title">Location sources</string>
strings.xml:7835:    <string name="photos_settings_location_setting_options">Location options</string>
strings.xml:7836:    <string name="photos_settings_location_setting_photos_with_location_summary">View and manage photos that have location information on your map</string>
strings.xml:7837:    <string name="photos_settings_location_setting_photos_with_location_title">Photos with location</string>
strings.xml:7838:    <string name="photos_settings_location_setting_title">Location</string>
strings.xml:7839:    <string name="photos_settings_location_setting_view_estimated_locations_summary">Some of your photos may contain previously estimated locations</string>
strings.xml:7840:    <string name="photos_settings_location_setting_view_estimated_locations_title">View and manage estimated locations</string>
strings.xml:7841:    <string name="photos_settings_location_sources_infer_locations_summary_without_inferred_locations">Use landmarks and other sources to estimate where your photos were taken &lt;a href=help:>Learn more&lt;/a></string>
strings.xml:7842:    <string name="photos_settings_location_sources_infer_locations_title">Estimate missing locations</string>
strings.xml:8033:    <string name="photos_share_partnersuggestion_close_button_text">Close</string>
strings.xml:8034:    <string name="photos_share_partnersuggestion_helppage_body_text">Sharing this memory with your partner lets you both see all of your photos from this moment together. &lt;p> You can also add others to this shared memory later. &lt;p> &lt;a href=help:>Learn [... omitted end of lo
strings.xml:8035:    <string name="photos_share_partnersuggestion_helppage_button_text">Got it</string>
strings.xml:8036:    <string name="photos_share_partnersuggestion_helppage_title_text">Collaborate on memories with your partner</string>
strings.xml:8037:    <string name="photos_share_partnersuggestion_invite_text">Add %1$s to “%2$s”</string>
strings.xml:8038:    <string name="photos_share_partnersuggestion_num_items">{count, plural, =1 {# item} other{# items}}</string>
strings.xml:8039:    <string name="photos_share_partnersuggestion_send_button_text">Add %1$s</string>
strings.xml:8040:    <string name="photos_share_partnersuggestion_senderidentity_text">Sharing as %1$s</string>
strings.xml:8041:    <string name="photos_share_partnersuggestion_senderidentity_with_location_text">%1$s will be able to see where your shared photos were taken. Sharing as %2$s</string>
strings.xml:8302:    <string name="photos_stories_media_date_location_delimiter">" • "</string>
strings.xml:9440:    <string name="preferences_license_title">Third Party Notices</string>
```

