# Pattern scan: work/protonvpn/jdex

## Code categories (library packages excluded)

### installed_apps — 6 hits in 4 files

- `classes2:pl/c.java` (2)
- `classes2:vg/j.java` (2)
- `classes:androidx/core/widget/i.java` (1)
- `classes:s0/c.java` (1)

```
classes:androidx/core/widget/i.java:132:                for (ResolveInfo resolveInfo : packageManager.queryIntentActivities(a(), 0)) {
classes:s0/c.java:68:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(f22410a.c(), 0);
classes2:pl/c.java:202:        List<ResolveInfo> listQueryIntentActivities = context.getPackageManager().queryIntentActivities(new Intent("android.intent.action.VIEW", uri), 131072);
classes2:pl/c.java:203:        sn.t.f(listQueryIntentActivities, "queryIntentActivities(...)");
classes2:vg/j.java:267:            List<ApplicationInfo> installedApplications = j.this.c.getInstalledApplications(0);
classes2:vg/j.java:268:            t.f(installedApplications, "getInstalledApplications(...)");
```

### usage_stats — 0 hits in 0 files


```
```

### clipboard — 8 hits in 4 files

- `classes3:me/proton/core/challenge/presentation/ProtonCopyPasteEditText.java` (4)
- `classes:androidx/compose/ui/platform/l.java` (2)
- `classes:androidx/appcompat/widget/v.java` (1)
- `classes3:zv/e.java` (1)

```
classes:androidx/appcompat/widget/v.java:67:        ClipData primaryClip = clipboardManager == null ? null : clipboardManager.getPrimaryClip();
classes:androidx/compose/ui/platform/l.java:26:        ClipData primaryClip = this.f2116a.getPrimaryClip();
classes:androidx/compose/ui/platform/l.java:57:        ClipData primaryClip = this.f2116a.getPrimaryClip();
classes3:zv/e.java:67:        clipboardManager.addPrimaryClipChangedListener(onPrimaryClipChangedListener);
classes3:me/proton/core/challenge/presentation/ProtonCopyPasteEditText.java:62:    private final String getPrimaryClip() {
classes3:me/proton/core/challenge/presentation/ProtonCopyPasteEditText.java:65:        ClipData primaryClip = this.clipboard.getPrimaryClip();
classes3:me/proton/core/challenge/presentation/ProtonCopyPasteEditText.java:77:        if (this.clipboard.hasPrimaryClip() && f(getPrimaryClipDescription())) {
classes3:me/proton/core/challenge/presentation/ProtonCopyPasteEditText.java:78:            return getPrimaryClip();
```

### contacts — 3 hits in 1 files

- `classes2:com/bumptech/glide/load/data/n.java` (3)

```
classes2:com/bumptech/glide/load/data/n.java:7:import android.provider.ContactsContract;
classes2:com/bumptech/glide/load/data/n.java:42:        Uri uriLookupContact = ContactsContract.Contacts.lookupContact(contentResolver, uri);
classes2:com/bumptech/glide/load/data/n.java:50:        return ContactsContract.Contacts.openContactPhotoInputStream(contentResolver, uri, true);
```

### call_log — 0 hits in 0 files


```
```

### sms — 0 hits in 0 files


```
```

### location — 1 hits in 1 files

- `classes:androidx/appcompat/app/u.java` (1)

```
classes:androidx/appcompat/app/u.java:59:                return this.f656b.getLastKnownLocation(str);
```

### wifi_bt_scan — 0 hits in 0 files


```
```

### device_ids — 13 hits in 7 files

- `classes:f5/h.java` (3)
- `classes:androidx/core/widget/NestedScrollView.java` (3)
- `classes:androidx/compose/ui/platform/AndroidComposeView.java` (2)
- `classes3:me/proton/core/auth/data/api/request/LoginTokenMdmRequest.java` (2)
- `classes:androidx/appcompat/app/v.java` (1)
- `classes:androidx/appcompat/app/s.java` (1)
- `classes:androidx/appcompat/app/h.java` (1)

```
classes:f5/h.java:69:        iArr[0] = q0.g(context, viewConfiguration, motionEvent.getDeviceId(), i8, motionEvent.getSource());
classes:f5/h.java:70:        iArr[1] = q0.f(context, viewConfiguration, motionEvent.getDeviceId(), i8, motionEvent.getSource());
classes:f5/h.java:75:        int deviceId = motionEvent.getDeviceId();
classes:androidx/core/widget/NestedScrollView.java:705:            getScrollFeedbackProvider().c(motionEvent.getDeviceId(), motionEvent.getSource(), i9, scrollY2);
classes:androidx/core/widget/NestedScrollView.java:717:                    getScrollFeedbackProvider().b(motionEvent.getDeviceId(), motionEvent.getSource(), i9, true);
classes:androidx/core/widget/NestedScrollView.java:726:                getScrollFeedbackProvider().b(motionEvent.getDeviceId(), motionEvent.getSource(), i9, false);
classes:androidx/appcompat/app/v.java:604:        menuE.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
classes:androidx/appcompat/app/s.java:229:        menuW.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);
classes:androidx/appcompat/app/h.java:1136:            boolean z9 = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;
classes:androidx/compose/ui/platform/AndroidComposeView.java:1276:        return getFocusOwner().i(new x2.b(f5.q0.h(viewConfiguration, getContext()) * f9, f9 * f5.q0.e(viewConfiguration, getContext()), event.getEventTime(), event.getDeviceId()), new k(event));
classes:androidx/compose/ui/platform/AndroidComposeView.java:1609:        MotionEvent motionEventObtain = MotionEvent.obtain(motionEvent.getDownTime() == motionEvent.getEventTime() ? eventTime : motionEvent.getDownTime(), eventTime, action, pointerCount, pointerPropertiesArr, pointerCoordsArr, motio
classes3:me/proton/core/auth/data/api/request/LoginTokenMdmRequest.java:189:    public final String getDeviceId() {
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

### accounts — 0 hits in 0 files


```
```

### battery_state — 1 hits in 1 files

- `classes2:fh/z.java` (1)

```
classes2:fh/z.java:61:        return "charging: " + (batteryManager != null ? Boolean.valueOf(batteryManager.isCharging()) : "unknown") + ", device idle mode: " + powerManager.isDeviceIdleMode() + ", power save mode: " + powerManager.isPowerSaveMode() + ", ignores optimizations: "  [... omitted end 
```

### screen_capture_detect — 0 hits in 0 files


```
```

### audio_capture — 4 hits in 1 files

- `classes:androidx/leanback/widget/SearchBar.java` (4)

```
classes:androidx/leanback/widget/SearchBar.java:12:import android.speech.SpeechRecognizer;
classes:androidx/leanback/widget/SearchBar.java:44:    private SpeechRecognizer J;
classes:androidx/leanback/widget/SearchBar.java:442:    public void setSpeechRecognizer(SpeechRecognizer speechRecognizer) {
classes:androidx/leanback/widget/SearchBar.java:444:        SpeechRecognizer speechRecognizer2 = this.J;
```

### accessibility — 97 hits in 21 files

- `classes:k1/m1.java` (17)
- `classes:g5/c.java` (12)
- `classes:androidx/compose/ui/platform/t.java` (9)
- `classes2:com/google/android/material/textfield/v.java` (7)
- `classes:k1/h.java` (5)
- `classes:androidx/compose/ui/platform/j.java` (5)
- `classes:o5/a.java` (5)
- `classes2:com/google/android/material/snackbar/BaseTransientBottomBar.java` (5)
- `classes2:com/google/android/material/textfield/p.java` (5)
- `classes:androidx/recyclerview/widget/RecyclerView.java` (4)
- `classes2:com/google/android/material/snackbar/Snackbar.java` (4)
- `classes2:com/google/android/material/textfield/r.java` (4)

```
classes:k1/m1.java:5:import android.view.accessibility.AccessibilityManager;
classes:k1/m1.java:6:import android.view.accessibility.AccessibilityManager$AccessibilityServicesStateChangeListener;
classes:k1/m1.java:13:final class m1 implements AccessibilityManager.AccessibilityStateChangeListener, w5 {
classes:k1/m1.java:39:        public static final void a(AccessibilityManager accessibilityManager, AccessibilityManager$AccessibilityServicesStateChangeListener accessibilityManager$AccessibilityServicesStateChangeListener) {
classes:k1/m1.java:43:        public static final void b(AccessibilityManager accessibilityManager, AccessibilityManager$AccessibilityServicesStateChangeListener accessibilityManager$AccessibilityServicesStateChangeListener) {
classes:k1/m1.java:49:    public static final class b implements AccessibilityManager$AccessibilityServicesStateChangeListener {
classes:k1/m1.java:79:        public void onAccessibilityServicesStateChanged(AccessibilityManager accessibilityManager) {
classes:k1/m1.java:86:    public static final class c implements AccessibilityManager.TouchExplorationStateChangeListener {
classes:k1/m1.java:102:        @Override // android.view.accessibility.AccessibilityManager.TouchExplorationStateChangeListener
classes:k1/m1.java:124:    public final boolean o(AccessibilityManager accessibilityManager) {
classes:k1/m1.java:125:        List<AccessibilityServiceInfo> enabledAccessibilityServiceList = accessibilityManager.getEnabledAccessibilityServiceList(16);
classes:k1/m1.java:137:    public final boolean q(AccessibilityManager accessibilityManager) {
```

### root_emulator — 15 hits in 10 files

- `classes:e1/r3.java` (3)
- `classes:h1/n.java` (2)
- `classes:e1/u3.java` (2)
- `classes3:cv/e5.java` (2)
- `classes:h1/v.java` (1)
- `classes:h1/b.java` (1)
- `classes:e1/e4.java` (1)
- `classes2:com/google/android/material/textfield/p.java` (1)
- `classes3:io/sentry/android/core/internal/util/m.java` (1)
- `classes4:p70/b.java` (1)

```
classes:h1/v.java:203:                c0.n(-864350873, i9, -1, "androidx.compose.material.internal.PopupLayout.Content (ExposedDropdownMenuPopup.android.kt:303)");
classes:h1/n.java:121:                c0.n(1705178815, i12, -1, "androidx.compose.material.internal.ExposedDropdownMenuPopup (ExposedDropdownMenuPopup.android.kt:80)");
classes:h1/n.java:264:                c0.n(1879981140, i8, -1, "androidx.compose.material.internal.ExposedDropdownMenuPopup.<anonymous>.<anonymous>.<anonymous> (ExposedDropdownMenuPopup.android.kt:99)");
classes:e1/u3.java:37:                n1.c0.n(1063434120, i9, -1, "androidx.compose.material.OnPlatformWindowBoundsChange (ExposedDropdownMenu.android.kt:41)");
classes:e1/u3.java:87:            n1.c0.n(-1216067952, i8, -1, "androidx.compose.material.platformWindowBoundsCalculator (ExposedDropdownMenu.android.kt:35)");
classes:e1/r3.java:22:                n1.c0.n(1604457564, i8, -1, "androidx.compose.material.ExposedDropdownMenuBoxScope.ExposedDropdownMenu.<anonymous> (ExposedDropdownMenu.kt:211)");
classes:e1/r3.java:42:            throw new UnsupportedOperationException("Super calls with default arguments not supported in this target, function: exposedDropdownSize");
classes:e1/r3.java:140:                            n1.c0.n(-1576205770, i10, -1, "androidx.compose.material.ExposedDropdownMenuBoxScope.ExposedDropdownMenu (ExposedDropdownMenu.kt:186)");
classes:h1/b.java:24:                c0.n(-1578637197, i8, -1, "androidx.compose.material.internal.ComposableSingletons$ExposedDropdownMenuPopup_androidKt.lambda$-1578637197.<anonymous> (ExposedDropdownMenuPopup.android.kt:287)");
classes:e1/e4.java:180:                    n1.c0.n(-1337700255, i10, -1, "androidx.compose.material.ExposedDropdownMenuBox (ExposedDropdownMenu.kt:94)");
classes2:com/google/android/material/textfield/p.java:84:        throw new RuntimeException("EditText needs to be an AutoCompleteTextView if an Exposed Dropdown Menu is being used.");
classes3:io/sentry/android/core/internal/util/m.java:26:        this(context, p0Var, iLogger, new String[]{"/system/app/Superuser.apk", "/sbin/su", "/system/bin/su", "/system/xbin/su", "/data/local/xbin/su", "/data/local/bin/su", "/system/sd/xbin/su", "/system/bin/failsafe/su", "/data/local/su", "/s
```

### js_bridge — 1 hits in 1 files

- `classes3:me/proton/core/humanverification/presentation/ui/hv3/a.java` (1)

```
classes3:me/proton/core/humanverification/presentation/ui/hv3/a.java:858:        webView.addJavascriptInterface(new c(), "AndroidInterface");
```

### boot_persist — 3 hits in 2 files

- `classes2:com/protonvpn/android/OnUpdateReceiver.java` (2)
- `classes2:com/protonvpn/android/vpn/autoconnect/AutoConnectBootReceiver.java` (1)

```
classes2:com/protonvpn/android/OnUpdateReceiver.java:42:        if (t.b(intent.getAction(), "android.intent.action.MY_PACKAGE_REPLACED")) {
classes2:com/protonvpn/android/OnUpdateReceiver.java:44:            a0.a.l(n.v, "ACTION_MY_PACKAGE_REPLACED has stored intent: " + (aVarC != null));
classes2:com/protonvpn/android/vpn/autoconnect/AutoConnectBootReceiver.java:36:        if (t.b(intent.getAction(), "android.intent.action.BOOT_COMPLETED")) {
```

### full_screen_intent — 1 hits in 1 files

- `classes:o4/m.java` (1)

```
classes:o4/m.java:230:        builderA.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, dVar.f20477j).setVibrate(notification.vibrate).setLights(notification.ledARGB, notificat [... omitted end 
```

### health_connect — 0 hits in 0 files


```
```

### keystroke_text_capture — 35 hits in 23 files

- `classes:androidx/emoji2/text/n.java` (3)
- `classes4:me/proton/core/presentation/ui/view/ProtonInput.java` (3)
- `classes:androidx/appcompat/widget/f.java` (2)
- `classes:androidx/appcompat/widget/AppCompatTextView.java` (2)
- `classes:androidx/appcompat/widget/SearchView.java` (2)
- `classes:androidx/leanback/widget/SearchBar.java` (2)
- `classes2:com/google/android/material/textfield/TextInputLayout.java` (2)
- `classes2:com/google/android/material/button/MaterialButton.java` (2)
- `classes4:q30/g.java` (2)
- `classes4:me/proton/core/presentation/ui/view/ProtonAutoCompleteInput.java` (2)
- `classes:y5/g.java` (1)
- `classes:y5/a.java` (1)

```
classes:y5/g.java:104:    public void onTextChanged(CharSequence charSequence, int i8, int i9, int i10) {
classes:y5/a.java:37:            editText.addTextChangedListener(gVar);
classes:androidx/appcompat/widget/f.java:161:    protected void onTextChanged(CharSequence charSequence, int i8, int i9, int i10) {
classes:androidx/appcompat/widget/f.java:162:        super.onTextChanged(charSequence, i8, i9, i10);
classes:androidx/appcompat/widget/AppCompatTextView.java:302:    protected void onTextChanged(CharSequence charSequence, int i8, int i9, int i10) {
classes:androidx/appcompat/widget/AppCompatTextView.java:303:        super.onTextChanged(charSequence, i8, i9, i10);
classes:androidx/appcompat/widget/SearchView.java:1422:        searchAutoComplete.addTextChangedListener(this.E0);
classes:androidx/appcompat/widget/SearchView.java:1467:        public void onTextChanged(CharSequence charSequence, int i8, int i9, int i10) {
classes:androidx/leanback/widget/SearchBar.java:384:        this.f4545e.addTextChangedListener(new d(new c()));
classes:androidx/leanback/widget/SearchBar.java:589:        public void onTextChanged(CharSequence charSequence, int i8, int i9, int i10) {
classes:androidx/emoji2/text/n.java:100:        public void onTextChanged(CharSequence charSequence, int i8, int i9, int i10) {
classes:androidx/emoji2/text/n.java:101:            ((TextWatcher) this.f3521e).onTextChanged(charSequence, i8, i9, i10);
```

### webview_tracking — 0 hits in 0 files


```
```

### streaks — 0 hits in 0 files


```
```

### reengagement — 114 hits in 46 files

- `classes3:io/sentry/android/core/b0.java` (13)
- `classes3:io/sentry/android/replay/viewhierarchy/a.java` (11)
- `classes2:mi/i3.java` (6)
- `classes2:com/protonvpn/android/ui/vpn/b.java` (5)
- `classes4:me/proton/core/plan/presentation/view/DynamicPlanCardView.java` (5)
- `classes2:ch/qos/logback/core/rolling/TimeBasedRollingPolicy.java` (4)
- `classes2:com/google/android/material/textfield/TextInputLayout.java` (4)
- `classes2:mi/c3.java` (3)
- `classes2:vi/f3.java` (3)
- `classes2:com/protonvpn/android/components/QuickTileService.java` (3)
- `classes2:ch/qos/logback/core/rolling/TimeBasedFileNamingAndTriggeringPolicyBase.java` (3)
- `classes3:q00/p.java` (3)

```
classes:q/c.java:106:        public void onActionViewCollapsed() {
classes:q/c.java:107:            this.f21042e.onActionViewCollapsed();
classes:g5/p.java:521:        return i8 != 0 ? i8 != 1 ? i8 != 2 ? i8 != 3 ? "UNKNOWN" : "FULL" : "PARTIAL" : "COLLAPSED" : "UNDEFINED";
classes:j1/fc.java:92:            n1.c0.n(-1757023234, i8, -1, "androidx.compose.material3.TopAppBarDefaults.exitUntilCollapsedScrollBehavior (AppBar.kt:1801)");
classes:j1/v2.java:260:                throw new IllegalArgumentException("The collapsedHeight is expected to be specified and finite");
classes:j1/v2.java:266:                throw new IllegalArgumentException("The expandedHeight is expected to be greater or equal to the collapsedHeight");
classes:d1/p.java:16:    public static final p f7687t = new p("COLLAPSED", 2);
classes:androidx/appcompat/widget/SearchView.java:1153:    public void onActionViewCollapsed() {
classes:androidx/appcompat/widget/Toolbar.java:1894:                ((androidx.appcompat.view.c) callback).onActionViewCollapsed();
classes:androidx/appcompat/view/c.java:6:    void onActionViewCollapsed();
classes2:fh/v.java:478:        sn.t.g(aVar, "elapsedRealtimeClock");
classes2:mi/c3.java:1825:                                rn.a elapsedRealtimeClock = i3Var2.getElapsedRealtimeClock();
```

### notif_permission_nag — 0 hits in 0 files


```
```

### cancellation_retention — 6 hits in 1 files

- `classes3:bu/i.java` (6)

```
classes3:bu/i.java:27:@Metadata(d1 = {"\u0000°\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n [... omitted end 
classes3:bu/i.java:41:    private final br.e0 cancellationFlow;
classes3:bu/i.java:848:            br.e0 e0Var = i.this.cancellationFlow;
classes3:bu/i.java:852:            ?? r13 = i.this.cancellationFlow;
classes3:bu/i.java:997:        this.cancellationFlow = u0.a(new z(false, null, null, null, 15, null));
classes3:bu/i.java:1032:        return br.k.m(br.k.D(this.observeUser.a(this.userId)), this.observeUserRecovery.b(this.userId), this.cancellationFlow, this.shouldShowCancellationForm, br.k.D(this.selfInitiated), new b(null));
```

### urgency_countdown — 97 hits in 15 files

- `classes2:com/protonvpn/android/promooffers/data/ApiNotificationOfferPanel.java` (19)
- `classes2:com/protonvpn/android/models/login/LoginResponse.java` (17)
- `classes3:io/sentry/android/core/internal/util/p.java` (11)
- `classes2:com/protonvpn/android/appconfig/ForkedSessionResponse.java` (10)
- `classes2:ch/qos/logback/classic/net/SimpleSocketServer.java` (8)
- `classes3:io/sentry/android/core/ViewHierarchyEventProcessor.java` (6)
- `classes3:io/sentry/android/core/d1.java` (4)
- `classes3:io/sentry/cache/f.java` (4)
- `classes4:okhttp3/internal/publicsuffix/PublicSuffixDatabase.java` (4)
- `classes3:io/sentry/android/ndk/SentryNdk.java` (3)
- `classes3:io/sentry/p.java` (3)
- `classes3:io/sentry/hints/d.java` (3)

```
classes2:ci/d1.java:139:            n1.c0.n(-810974780, i, -1, "com.protonvpn.android.promooffers.ui.rememberCountDownState (PromoOfferBanner.kt:114)");
classes2:ci/d1.java:200:                    n1.c0.n(1777873539, i3, -1, "com.protonvpn.android.promooffers.ui.BannerWithCountdown (PromoOfferBanner.kt:151)");
classes2:ci/f.java:40:            n1.c0.n(-104831895, i, -1, "com.protonvpn.android.promooffers.ui.CountDownState.getTimeLeftText (PromoOfferBanner.kt:89)");
classes2:ci/f.java:80:            n1.c0.n(651106139, i, -1, "com.protonvpn.android.promooffers.ui.CountDownState.<get-timeLeftText> (PromoOfferBanner.kt:82)");
classes2:ci/h.java:362:                return new e1(url, fullScreenImage2.getAlternativeText(), apiNotification.getOffer().getPanel().getButton(), apiNotification.getOffer().getPanel().isDismissible(), apiNotification.getOffer().getPanel().getShowCountdown() ? Long.valueOf(TimeUnit [... omitted end
classes2:com/protonvpn/android/models/login/LoginResponse.java:27:@Metadata(d1 = {"\u0000B\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0002\b\t\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n
classes2:com/protonvpn/android/models/login/LoginResponse.java:35:    private final int expiresIn;
classes2:com/protonvpn/android/models/login/LoginResponse.java:54:            h2Var.p("ExpiresIn", false);
classes2:com/protonvpn/android/models/login/LoginResponse.java:200:        this.expiresIn = i2;
classes2:com/protonvpn/android/models/login/LoginResponse.java:213:            i = loginResponse.expiresIn;
classes2:com/protonvpn/android/models/login/LoginResponse.java:239:        output.w(serialDesc, 1, self.expiresIn);
classes2:com/protonvpn/android/models/login/LoginResponse.java:253:    public final int getExpiresIn() {
```

### infinite_autoplay — 0 hits in 0 files


```
```

### badges — 2 hits in 1 files

- `classes:o4/m.java` (2)

```
classes:o4/m.java:158:            return builder.setBadgeIconType(i8);
classes:o4/m.java:230:        builderA.setWhen(notification.when).setSmallIcon(notification.icon, notification.iconLevel).setContent(notification.contentView).setTicker(notification.tickerText, dVar.f20477j).setVibrate(notification.vibrate).setLights(notification.ledARGB, notificat [... omitted end 
```

### minors_age — 0 hits in 0 files


```
```

### screen_time — 1 hits in 1 files

- `classes2:jj/i0.java` (1)

```
classes2:jj/i0.java:705:        mapC.put("session_length", Long.valueOf(jLongValue));
```

## UI string categories (default locale)

### loss_aversion_copy — 0 strings

```
```

### urgency_copy — 1 strings

```
strings.xml:1192:    <string name="plans_limited_offer">Limited time offer</string>
```

### confirmshaming_copy — 3 strings

```
strings.xml:235:    <string name="auth_login_no_it_wasnt_me">"No, it wasn't me"</string>
strings.xml:1034:    <string name="no_thanks">No thanks</string>
strings.xml:1720:    <string name="upgrade_not_now_button">Not now</string>
```

### social_pressure_copy — 3 strings

```
strings.xml:1406:    <string name="settingsSendCrashReportsDescription">Crash reports help us fix bugs, detect firewalls, and avoid VPN blocks.</string>
strings.xml:1664:    <string name="troubleshootProxyFirewallProblemDescription">Disable any proxies or firewalls, or contact your network administrator.</string>
strings.xml:1665:    <string name="troubleshootProxyFirewallProblemTitle">Proxy/Firewall interference</string>
```

### guilt_copy — 25 strings

```
strings.xml:184:    <string name="auth_credentialless_settings_subtitle">Get a password manager, encrypted Mail and Calendar, and 1 GB of cloud storage for free with a Proton Account.</string>
strings.xml:285:    <string name="auth_signup_create_secure_proton_address">Get a new encrypted email address</string>
strings.xml:459:    <string name="connection_feature_secure_core_description">Your activity is encrypted behind 2 high-security VPN servers.</string>
strings.xml:554:    <string name="crypto_keystore_error_continue_action">Continue</string>
strings.xml:555:    <string name="crypto_keystore_error_exit_action">Exit</string>
strings.xml:556:    <string name="crypto_keystore_error_logout_action">Sign out</string>
strings.xml:557:    <string name="crypto_keystore_error_message">This device uses a faulty implementation of Android Keystore, which we use to keep your data safe. This means your data can be compromised if an attacker gets physical access to this device. What would you like  [... omitted end of lon
strings.xml:558:    <string name="crypto_keystore_error_more_info_action">Get more information</string>
strings.xml:559:    <string name="crypto_keystore_error_title">Encryption error</string>
strings.xml:560:    <string name="crypto_keystore_help_url">https://proton.me/support/android-keystore-issues</string>
strings.xml:1321:    <string name="secure_core_upsell_banner_description">Add another layer of encryption to your VPN connection</string>
strings.xml:1729:    <string name="upgrade_secure_core_message">Add another layer of encryption to your VPN connection with &lt;b>Secure Core&lt;/b>.</string>
strings.xml:1730:    <string name="upgrade_secure_core_title">Double the encryption</string>
strings.xml:1747:    <string name="upgrade_unlimited_drive_encryption">Encrypted file storage</string>
strings.xml:1764:    <string name="upgrade_unlimited_pass_manager">Encrypted password manager</string>
strings.xml:1787:    <string name="upsell_card_secure_core_description">Add another layer of encryption to your VPN connection</string>
strings.xml:1837:    <string name="upsell_panel_secure_core_title">Two layers of encryption between you and the web</string>
strings.xml:1901:    <string name="welcome_subtitle">Encryption keeps your data private. Your data truly belongs to you.</string>
strings.xml:1902:    <string name="welcome_subtitle_calendar">Encrypted calendar that keeps your life events private, safe, and secure.</string>
strings.xml:1903:    <string name="welcome_subtitle_calendar_alt">Our end-to-end encrypted calendar helps you stay organized, on track, and in control.</string>
strings.xml:1904:    <string name="welcome_subtitle_drive">The convenience of cloud storage and the security of encryption technology. Finally a cloud storage solution you can trust.</string>
strings.xml:1905:    <string name="welcome_subtitle_drive_alt">The safest way to store your files. Upload, sync, and share with the strongest encryption available.</string>
strings.xml:1906:    <string name="welcome_subtitle_mail">Encrypted email that keeps your conversations private. Your inbox truly belongs to you.</string>
strings.xml:1907:    <string name="welcome_subtitle_mail_alt">Privacy. Security. Convenience. Encrypted email that gives you full control of your personal data.</string>
strings.xml:1910:    <string name="welcome_subtitle_vpn">High-speed Swiss VPN that safeguards your privacy by encrypting your internet connection.</string>
```

### subscription_copy — 138 strings

```
plurals.xml:15:    <plurals name="auth_user_check_max_free_error">
plurals.xml:131:    <plurals name="notification_max_sessions_upsell_content">
plurals.xml:132:        <item quantity="other">Please disconnect another device to connect this one or upgrade to Plus to get up to %1$d devices connected at the same time.</item>
plurals.xml:133:        <item quantity="one">Please disconnect another device to connect this one or upgrade to Plus to get up to %1$d device connected at the same time.</item>
plurals.xml:144:        <item quantity="other">Special offer. Auto renews at %1$s every %2$d days</item>
plurals.xml:145:        <item quantity="one">Special offer. Auto renews at %1$s/day</item>
plurals.xml:148:        <item quantity="other">Special offer. Auto renews at %1$s every %2$d months</item>
plurals.xml:149:        <item quantity="one">Special offer. Auto renews at %1$s/month</item>
plurals.xml:152:        <item quantity="other">Special offer. Auto renews at %1$s every %2$d weeks</item>
plurals.xml:153:        <item quantity="one">Special offer. Auto renews at %1$s/week</item>
plurals.xml:156:        <item quantity="other">Special offer. Auto renews at %1$s every %2$d years</item>
plurals.xml:157:        <item quantity="one">Special offer. Auto renews at %1$s/year</item>
plurals.xml:192:        <item quantity="other">then auto renews at %1$s every %2$d days</item>
plurals.xml:193:        <item quantity="one">then auto renews at %1$s/day</item>
plurals.xml:196:        <item quantity="other">then auto renews at %1$s every %2$d months</item>
plurals.xml:197:        <item quantity="one">then auto renews at %1$s/month</item>
plurals.xml:200:        <item quantity="other">then auto renews at %1$s every %2$d weeks</item>
plurals.xml:201:        <item quantity="one">then auto renews at %1$s/week</item>
plurals.xml:204:        <item quantity="other">then auto renews at %1$s every %2$d years</item>
plurals.xml:205:        <item quantity="one">then auto renews at %1$s/year</item>
plurals.xml:224:        <item quantity="other">Subscription auto renews at %1$s every %2$d days</item>
plurals.xml:225:        <item quantity="one">Subscription auto renews at %1$s/day</item>
plurals.xml:228:        <item quantity="other">Subscription auto renews at %1$s every %2$d months</item>
plurals.xml:229:        <item quantity="one">Subscription auto renews at %1$s/month</item>
plurals.xml:232:        <item quantity="other">Subscription auto renews at %1$s every %2$d weeks</item>
plurals.xml:233:        <item quantity="one">Subscription auto renews at %1$s/week</item>
plurals.xml:236:        <item quantity="other">Subscription auto renews at %1$s every %2$d years</item>
plurals.xml:237:        <item quantity="one">Subscription auto renews at %1$s/year</item>
plurals.xml:276:        <item quantity="other">Unlock geoblocked content from %1$d countries with VPN Plus</item>
plurals.xml:277:        <item quantity="one">Unlock geoblocked content from %1$d country with VPN Plus</item>
plurals.xml:299:    <plurals name="upgrade_plus_countries">
plurals.xml:303:    <plurals name="upgrade_plus_servers_new">
strings.xml:261:    <string name="auth_mailbox_title">Unlock your mailbox</string>
strings.xml:262:    <string name="auth_mailbox_unlock_action">Unlock</string>
strings.xml:283:    <string name="auth_signup_create_account_dialog_text">Your Google Pay payment was successfully processed. To activate your subscription, please create your Proton account.</string>
strings.xml:284:    <string name="auth_signup_create_account_dialog_title">Activate your subscription</string>
strings.xml:358:    <string name="badge_plan_plus">Plus</string>
strings.xml:436:    <string name="connection_details_server_load_description">"Server load shows how close a server is to its maximum capacity. 
strings.xml:496:    <string name="countries_upsell_banner_description">Access all countries with VPN Plus</string>
strings.xml:499:    <string name="country_filter_all_list_header_free">Plus countries (%1$d)</string>
strings.xml:632:    <string name="errorMaxSessions">You have hit the maximum number of simultaneous connections allowed for your account. Please upgrade your Proton VPN plan to get more connections.</string>
strings.xml:683:    <string name="free_connections_info_banner_text">Access all countries with VPN Plus</string>
strings.xml:696:    <string name="home_upsell_carousel_headline">Discover VPN Plus</string>
strings.xml:714:    <string name="info_dialog_how_to_stream_step_3">Connect to any Plus server and start streaming</string>
strings.xml:730:    <string name="info_dialog_secure_core_description">"Secure Core connects you to your destination server via a second, maximum security VPN server.
strings.xml:760:    <string name="initial_profile_name_max_security">Max security</string>
strings.xml:772:    <string name="intro_origin_biometrics_title">Unlock your device to continue</string>
strings.xml:821:    <string name="m3_exceed_max_badge_text_suffix">%1$s%2$s</string>
strings.xml:959:    <string name="mtrl_exceed_max_badge_number_content_description">More than %1$d new notifications</string>
strings.xml:960:    <string name="mtrl_exceed_max_badge_number_suffix">%1$d%2$s</string>
strings.xml:1044:    <string name="notification_cancel_to_delinquent">You will be able to access premium features again after pending invoices are paid.</string>
strings.xml:1046:    <string name="notification_delinquent_content">Please take a moment to update your billing information to keep your subscription active.</string>
strings.xml:1048:    <string name="notification_max_sessions_content">Please disconnect another device to connect this one.</string>
strings.xml:1049:    <string name="notification_max_sessions_title">You have reached your maximum device limit</string>
strings.xml:1052:    <string name="notification_streaming_blocked_text">Many streaming services detect and block connections from free VPN servers. Upgrade to Proton VPN Plus to bypass these blocks</string>
strings.xml:1054:    <string name="notification_subscription_expired_content">We had to downgrade your plan, but we’re reconnecting you to the fastest server available on that plan.</string>
strings.xml:1055:    <string name="notification_subscription_expired_no_reconnection_content">Your subscription has been downgraded.</string>
strings.xml:1056:    <string name="notification_subscription_expired_title">Your Proton VPN subscription plan has expired</string>
strings.xml:1122:    <string name="payments_error_subscription_managed_other_app">Subscription managed by other app.</string>
strings.xml:1147:    <string name="plan_auto_renew_message_annual">Subscription auto renews at %1$s/year</string>
strings.xml:1148:    <string name="plan_auto_renew_message_monthly">Subscription auto renews at %1$s/month</string>
strings.xml:1149:    <string name="plan_auto_renew_message_two_years">Subscription auto renews at %1$s/2 years</string>
strings.xml:1156:    <string name="plan_id_plus_header">Full-featured mailbox with advanced protection.</string>
strings.xml:1164:    <string name="plan_id_vpnplus_adblock">Adblocker (NetShield)</string>
strings.xml:1165:    <string name="plan_id_vpnplus_countries">63 countries</string>
strings.xml:1166:    <string name="plan_id_vpnplus_header">VPN Plus</string>
strings.xml:1167:    <string name="plan_id_vpnplus_highest_speed">Highest speed</string>
strings.xml:1168:    <string name="plan_id_vpnplus_streaming">Streaming service support</string>
strings.xml:1169:    <string name="plan_manage_subscription_app_missing_got_it">Got it</string>
strings.xml:1170:    <string name="plan_manage_subscription_no_app_subtitle">You can manage your subscription in %1$s application. Download and install the latest version of %2$s to upgrade to %3$s.</string>
strings.xml:1171:    <string name="plan_manage_subscription_no_app_title">Install %s</string>
strings.xml:1172:    <string name="plan_manage_subscription_subtitle">You can manage your subscription in %1$s application. Open %2$s to upgrade to %3$s.</string>
strings.xml:1173:    <string name="plan_manage_subscription_title">Upgrade in %s</string>
strings.xml:1176:    <string name="plan_welcome_price_message_annual">Welcome offer. Auto renews at %1$s/year</string>
strings.xml:1177:    <string name="plan_welcome_price_message_monthly">Welcome offer. Auto renews at %1$s/month</string>
strings.xml:1178:    <string name="plan_welcome_price_message_other_fallback">Subscription auto renews</string>
strings.xml:1179:    <string name="plan_welcome_price_message_two_year">Welcome offer. Auto renews at %1$s/2 years</string>
strings.xml:1180:    <string name="plans_autorenew_subscriptions">Only auto-renewing annual subscriptions are available via this app.</string>
strings.xml:1181:    <string name="plans_billed_monthly">Billed monthly</string>
strings.xml:1182:    <string name="plans_billed_yearly">*Billed annually at %s</string>
strings.xml:1186:    <string name="plans_can_not_upgrade_from_mobile">"Your subscription can't be managed inside the Android app."</string>
strings.xml:1193:    <string name="plans_manage_subscription_play_store">Manage subscription</string>
strings.xml:1194:    <string name="plans_manage_your_subscription">Manage your subscription at <a href="https://account.proton.me">account.proton.me</a></string>
strings.xml:1195:    <string name="plans_manage_your_subscription_google">Your subscription is managed by Google Play.</string>
strings.xml:1196:    <string name="plans_manage_your_subscription_other">Your subscription can’t be managed inside the mobile app.</string>
strings.xml:1207:    <string name="plans_subscription">Subscription</string>
strings.xml:1208:    <string name="plans_subscription_base_storage_full_title">Your Mail storage is full</string>
strings.xml:1209:    <string name="plans_subscription_base_storage_nearly_full_title">Your Mail storage is almost full</string>
strings.xml:1210:    <string name="plans_subscription_drive_storage_full_title">Your Drive storage is full</string>
strings.xml:1211:    <string name="plans_subscription_drive_storage_nearly_full_title">Your Drive storage is almost full</string>
strings.xml:1212:    <string name="plans_subscription_storage_full_description">Upgrade your plan in the web app to continue to use your account without interruptions.</string>
strings.xml:1213:    <string name="plans_subscription_storage_get_more">Get more storage</string>
strings.xml:1330:    <string name="server_change_max_reached">You’ve reached the maximum number of Free server changes for now.</string>
strings.xml:1332:    <string name="server_change_upsell">Get unlimited changes with VPN Plus.</string>
strings.xml:1496:    <string name="settings_lan_allow_direct_connection_description">Connect to Smart TVs, Android Auto, and other devices that create their own network. For maximum security, only enable when connecting to these devices.</string>
strings.xml:1616:    <string name="subscription_renewal_info_annual">The discounted price of %1$s is valid for the first year. Your subscription automatically renews on &lt;b>%2$s&lt;/b> at &lt;b>%3$s&lt;/b>.</string>
strings.xml:1617:    <string name="subscription_renewal_info_monthly">The discounted price of %1$s is valid for the first month. Your subscription automatically renews on &lt;b>%2$s&lt;/b> at &lt;b>%3$s&lt;/b>.</string>
strings.xml:1618:    <string name="subscription_renewal_info_two_years">The discounted price of %1$s is valid for the first two years. Your subscription automatically renews on &lt;b>%2$s&lt;/b> at &lt;b>%3$s&lt;/b>.</string>
strings.xml:1675:    <string name="tv_detail_connect_streaming">Stream with Plus</string>
strings.xml:1677:    <string name="tv_detail_description_country_not_available">This country isn’t available. Get more streaming options with a Proton VPN Plus plan.</string>
strings.xml:1678:    <string name="tv_detail_description_no_streaming_country">Stream more of your favourite content with a Proton VPN Plus plan.</string>
strings.xml:1679:    <string name="tv_detail_description_plus">Stream your favourite videos, movies, or sports with your apps.</string>
strings.xml:1680:    <string name="tv_detail_description_streaming_country">Stream your favorite content. Access more apps with a Proton VPN Plus plan.</string>
strings.xml:1713:    <string name="upgrade_country_message">Unlock &lt;b>country selection&lt;/b> with VPN Plus.</string>
strings.xml:1715:    <string name="upgrade_customization_message">Unlock &lt;b>LAN connections&lt;/b>, &lt;b>Custom DNS&lt;/b>, and &lt;b>NAT type 2&lt;/b> with VPN Plus.</string>
strings.xml:1716:    <string name="upgrade_customization_title">Unlock advanced VPN customization</string>
strings.xml:1722:    <string name="upgrade_p2p_title">Unlock peer-to-peer (P2P) downloads and file sharing</string>
strings.xml:1724:    <string name="upgrade_plus_countries_title_new">Unlock %1$s in %2$s with &lt;b>VPN Plus&lt;/b>.</string>
strings.xml:1725:    <string name="upgrade_plus_message">Get advanced privacy features and higher speed with VPN Plus.</string>
strings.xml:1726:    <string name="upgrade_plus_title">Upgrade your privacy</string>
strings.xml:1727:    <string name="upgrade_profiles_text">Unlock profiles with VPN Plus</string>
strings.xml:1736:    <string name="upgrade_streaming_block_text">VPN Plus servers let you enjoy your favorite movies and TV shows from around the world.</string>
strings.xml:1743:    <string name="upgrade_unlimited_all_apps_description">Unlock all premium features from Proton VPN, Mail, Calendar, Drive, and Pass.</string>
strings.xml:1766:    <string name="upgrade_unlimited_vpn_all_features">All other VPN Plus features</string>
strings.xml:1772:    <string name="upgrade_unlimited_vpn_unlimited_countries">Unlock all countries</string>
strings.xml:1773:    <string name="upgrade_vpn_accelerator_message">Unlock faster, less crowded servers with speeds of up to %1$d Gbps.</string>
strings.xml:1778:    <string name="upsell_card_customization_description">Unlock even more performance and privacy features</string>
strings.xml:1800:    <string name="upsell_panel_adv_customization_description">Allow LAN connections, set a custom DNS, and choose your NAT type. The advanced controls, all on Plus.</string>
strings.xml:1804:    <string name="upsell_panel_content_description_value_prefix_plus">Plus plan:</string>
strings.xml:1806:    <string name="upsell_panel_countries_title">Unlock all countries with VPN Plus</string>
strings.xml:1809:    <string name="upsell_panel_country_title">Unlock %1$s with VPN Plus</string>
strings.xml:1827:    <string name="upsell_panel_onboarding_title">Get more with VPN Plus</string>
strings.xml:1852:    <string name="upsell_panel_streaming_block_description">VPN Plus servers let you enjoy your favorite movies and TV shows from around the world.</string>
strings.xml:1854:    <string name="upsell_panel_streaming_footer">* Streaming platform subscription required.</string>
strings.xml:1861:    <string name="upsell_tv_all_countries_description">Unlock %1$s in %2$s.</string>
strings.xml:1862:    <string name="upsell_tv_all_countries_title">Access all countries with Plus</string>
strings.xml:1863:    <string name="upsell_tv_customization_description">Unlock &lt;b>LAN connections&lt;/b>, &lt;b>Custom DNS&lt;/b>, and more advanced VPN features.</string>
strings.xml:1864:    <string name="upsell_tv_customization_title">Get advanced VPN customization with Plus</string>
strings.xml:1867:    <string name="upsell_tv_netshield_title">Enjoy ad-free browsing with Plus</string>
strings.xml:1869:    <string name="upsell_tv_split_tunneling_title">Get the best of both worlds with Plus</string>
strings.xml:1870:    <string name="upsell_tv_subscription_expired_description">Upgrade to get access to Plus servers and features again.</string>
strings.xml:1871:    <string name="upsell_tv_subscription_expired_title">Subscription expired</string>
strings.xml:1895:    <string name="vpnplus_upsell_banner_description">Upgrade to VPN Plus</string>
strings.xml:1896:    <string name="welcome_generic_description">"You've upgraded your subscription. Enjoy advanced privacy features and next-level performance."</string>
strings.xml:1898:    <string name="welcome_plus_description">Enjoy extra privacy features, supercharged performance, and next-level VPN customization.</string>
strings.xml:1899:    <string name="welcome_plus_title">Welcome to VPN Plus</string>
strings.xml:1911:    <string name="welcome_subtitle_vpn_alt">High-speed Swiss VPN that protects your privacy. Maximum security, 1,600+ servers, and no restrictions.</string>
strings.xml:1913:    <string name="welcome_unlimited_description">You unlocked all premium Proton VPN, Mail, Calendar, Drive, Pass, and Wallet features.</string>
```

### data_copy — 49 strings

```
strings.xml:122:    <string name="activityLicensesTitle">Third party licenses</string>
strings.xml:401:    <string name="connectionAllocationHelpAssignConnectionsButton">Enable VPN connections</string>
strings.xml:402:    <string name="connectionAllocationHelpDescription1">To start your journey in Proton VPN please assign VPN connections to your account or any other sub-account.</string>
strings.xml:403:    <string name="connectionAllocationHelpDescription1AskAdmin">There is currently no VPN connection enabled for this account. To start your journey with Proton VPN, please contact your administrator.</string>
strings.xml:404:    <string name="connectionAllocationHelpDescription2">This step will take just a few minutes. After that you will be able to sign in and protect all your devices.</string>
strings.xml:405:    <string name="connectionAllocationHelpLoginAgainButton">Sign in again</string>
strings.xml:406:    <string name="connectionAllocationHelpTitle">Thanks for upgrading</string>
strings.xml:480:    <string name="connection_preferences_smart_discovery_dialog_message">If there are locations you don’t want to be automatically connected to, you can exclude them from Fastest country.</string>
strings.xml:550:    <string name="create_profile_type_and_location_title">Select connection type and location</string>
strings.xml:651:    <string name="exclude_locations">Exclude locations</string>
strings.xml:652:    <string name="excluded_locations">Excluded locations</string>
strings.xml:653:    <string name="excluded_locations_adoption_description">You can now exclude countries and cities from &lt;b>Fastest&lt;/b> connections.</string>
strings.xml:654:    <string name="excluded_locations_adoption_title">Avoid unwanted locations</string>
strings.xml:666:    <string name="fastest_country_description">The best server based on your location</string>
strings.xml:684:    <string name="free_connections_info_message">Proton Free automatically connects you to the fastest available server. This will normally be the closest server to your location.</string>
strings.xml:685:    <string name="free_connections_info_server_locations">Free server locations (%1$d)</string>
strings.xml:712:    <string name="info_dialog_how_to_stream_step_1">Go to your phone settings and turn off location services</string>
strings.xml:715:    <string name="info_dialog_ipaddress_description">Your VPN IP masks your real IP address. This makes it look like you’re browsing from your VPN location, so your online activity can’t be linked to your device.</string>
strings.xml:728:Set your preferred location and optimize your settings for security, performance, gaming, or any other scenario."</string>
strings.xml:943:    <string name="message_server_location_excluded">Server location excluded</string>
strings.xml:994:    <string name="netshield_ads_details">Advertisements and invisible ad trackers</string>
strings.xml:1005:    <string name="netshield_settings_description_tv">"Protects you from third-party ads, trackers, and malware. NetShield doesn't block ads that are built into streaming services like YouTube and Netflix."</string>
strings.xml:1032:    <string name="no_logs_banner_description">Your VPN activity is protected by Swiss privacy laws. We’ll never track you online or share your information with third parties.</string>
strings.xml:1241:    <string name="private_dns_conflict_banner_custom_dns_description">Your device is using a third-party DNS which prevents Proton VPN’s Custom DNS from working. Learn more</string>
strings.xml:1242:    <string name="private_dns_conflict_banner_custom_dns_description_tv">Your device is using a third-party DNS which prevents Proton VPN’s Custom DNS from working.</string>
strings.xml:1244:    <string name="private_dns_conflict_banner_netshield_description">Your device is using a third-party DNS which prevents NetShield from working. Learn more</string>
strings.xml:1267:    <string name="profile_location_excluded_dialog_message">Your server selection for &lt;b>%1$s&lt;/b> is unavailable. Select a different server, check your excluded locations or try again later.</string>
strings.xml:1274:    <string name="profiles_zero_state_description">Profiles are saved connections with your choice of location, server, and protocol.</string>
strings.xml:1300:    <string name="restricted_location_excluded_dialog_description">No servers available. Choose a location manually or edit your excluded locations.</string>
strings.xml:1301:    <string name="restricted_location_excluded_dialog_title">Connection failed</string>
strings.xml:1414:    <string name="settingsTelemetryScreenInfo">"These statistics do not contain your IP address, and they cannot be used to identify you. We'll never share them with third parties. &lt;a href=%1$s>Learn more&lt;/a>"</string>
strings.xml:1437:    <string name="settings_advanced_dns_description">Connect to VPN with a self-hosted or third-party domain name system (DNS). Learn more</string>
strings.xml:1468:    <string name="settings_connection_preferences_snackbar_message_excluded_location_removed">Item removed</string>
strings.xml:1470:    <string name="settings_custom_dns_description_tv">Connect to VPN with a self-hosted or third-party domain name system (DNS).</string>
strings.xml:1481:    <string name="settings_excluded_locations_accessibility_label_city">City</string>
strings.xml:1482:    <string name="settings_excluded_locations_accessibility_label_country">Country</string>
strings.xml:1483:    <string name="settings_excluded_locations_accessibility_label_deletion">Remove from excluded locations</string>
strings.xml:1484:    <string name="settings_excluded_locations_accessibility_label_state">State</string>
strings.xml:1485:    <string name="settings_excluded_locations_description">The selected locations will never be used when you connect to Fastest.</string>
strings.xml:1486:    <string name="settings_excluded_locations_selection_hint">Select…</string>
strings.xml:1487:    <string name="settings_excluded_locations_title">Excluded locations</string>
strings.xml:1488:    <string name="settings_excluded_locations_unavailable">No locations available</string>
strings.xml:1581:    <string name="settings_third_party_licenses">Third party licenses</string>
strings.xml:1767:    <string name="upgrade_unlimited_vpn_any_location">Choose any location</string>
strings.xml:1776:    <string name="upsell_card_countries_description">%1$d+ server locations in %2$s</string>
strings.xml:1791:    <string name="upsell_card_split_tunneling_description">Browse from two locations at once</string>
strings.xml:1816:    <string name="upsell_panel_general_benefit_location">Choose your location</string>
strings.xml:1894:    <string name="vpn_status_disabled_location">%1$s · %2$s</string>
strings.xml:1916:    <string name="whats_new_profiles_description">Create and save custom connections with your choice of location, server, and protocol.</string>
```

