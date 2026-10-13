# Dexcom G7 2.2.1.7105 — working notes (paths under work/dexcom_g7/jadx/sources)

## Permissions beyond core CGM function
QUERY_ALL_PACKAGES, RECORD_AUDIO, READ_PHONE_STATE, CALL_PHONE, CAMERA, ACCESS_BACKGROUND_LOCATION + FINE/COARSE, Health Connect READ heart rate/steps/exercise/distance/active+basal calories, WRITE blood glucose, SCHEDULE_EXACT_ALARM, REQUEST_IGNORE_BATTERY_OPTIMIZATIONS.
- QUERY_ALL_PACKAGES: only observed use = check/launch Dexcom Clarity app (com/dexcom/dexcomone/ui/uiutils/PackageManagerUtils.java via reflection; callers EventsScreenViewModel.java:1609, ClarityInfoViewModel.java:172). A <queries> entry would suffice.
- RECORD_AUDIO: SpeechRecognizer for voice entry (com/dexcom/phoenixuikit/uikit/SpeechToTextParser.java).
- Location: CountryOfResidenceService compares phone location against account country (com/dexcom/dexcomone/utils/CountryOfResidenceService.java:252-385); transmitter LocationServicesHelper requests updates at 0 ms / 0 m (com/dexcom/coresdk/transmitterG7/util/LocationServicesHelper.java:476). Copy: "You must always allow location permission to continue."
- Health Connect reads into IAggregatedActivityRepository / IWorkoutActivityRepository (com/dexcom/coresdk/cgmkit/health/HealthDataService.java). Upload path not traced.

## Consent gating
Strings: "You can't use Share if you don't allow data sharing to the cloud." / "Must Share with Dexcom" (to use Lilly Tempo pen) / "If you'd like to be able to restore data next time, change your data consents to share data with Dexcom now." / "You've revoked consent to data sharing — Share cannot be used until consent is restored."
Consent texts are server-side (CAMS); bundle scope not determinable from APK.

## Opacity
All literals string-encrypted (e.g. HandlerC2189.m53923, C10757.m74498), PackageManager calls via reflection; impedes independent audit of a regulated medical device app.
Trackers: Firebase Analytics (collection deactivated by default in manifest), Crashlytics, Qualtrics (in-app surveys). Extensive EventLogger (Bluetooth, networking, consent events) feeding BulkDataManager uploads.
