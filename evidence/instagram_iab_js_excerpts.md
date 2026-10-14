# Instagram in-app browser scripts — excerpts

Short excerpts (around 200 characters each) quoted for research and commentary. The full scripts ship inside the
Instagram APK as raw resources. To check them, decode `com.instagram.android` 451.0.0.53.80
(APK SHA-256 `4c0e618298317eac84afa7ee9059a3c28561b055d474e4b983a817f19a120c37`) with
`apktool d -s` and compare `res/raw/iabjs_<name>` against the SHA-256 below.

## `iabjs_data_layer_interceptor`
- size: 1006 bytes
- sha256: `fc97995a4c8ca72e8661dbe0f8174076f4f6863a1b245640eea6573ba263850a`

```js
…turn args.forEach(reportAnalyticsHealth),result}:Reflect.get(obj,property)});if(window.dataLayer){const queued=window.dataLayer.slice();window.dataLayer=monitorAnalyticsHealth(window.dataLayer),queued…
```
```js
…s({event_name:"string"==typeof eventValue&&""!==eventValue?eventValue:"unknown",event_data:JSON.stringify(eventData)??"",event_source:"0"})},monitorAnalyticsHealth=target=>new Proxy(target,{get:(obj,p…
```
```js
…entValue:"unknown",event_data:JSON.stringify(eventData)??"",event_source:"0"})},monitorAnalyticsHealth=target=>new Proxy(target,{get:(obj,property)=>"push"===property?function(...args){const result=ob…
```

## `iabjs_tiktok_pixel_interceptor`
- size: 1066 bytes
- sha256: `52ac54e36200842542099ecd4d7e23d915c0950ce5ec0769e1b165c98364bcdf`

```js
…entData)??"",event_source:"1"})},isTikTokPixelUrl=url=>""!==url&&(url.includes("analytics.tiktok.com")||url.includes("business.tiktok.com")),originalSendBeacon=navigator.sendBeacon;navigator.sendBeaco…
```
```js
…)||url.includes("business.tiktok.com")),originalSendBeacon=navigator.sendBeacon;navigator.sendBeacon=new Proxy(originalSendBeacon,{apply(target,thisArg,args){const url="string"==typeof args[0]?args[0]…
```

## `iabjs_snap_pixel_interceptor`
- size: 1336 bytes
- sha256: `66e9e5c06e64baee3f359fdd9571f755509b0bef18e7e9c2d8e09e209bda39a6`

```js
…{apply(target,thisArg,args){const command=args[0];let eventName,eventData;return"init"===command?(eventName="init",eventData=args[2]||{}):"string"==typeof args[1]&&UUID_RE.test(args[1])?(eventName="st…
```
```js
…ntData}),Reflect.apply(target,thisArg,args)}});if(void 0!==window.snaptr)return window.snaptr=proxySnaptr(window.snaptr),void 0;let _snaptr;Object.defineProperty(window,"snaptr",{configurable:!0,enume…
```

## `iabjs_reddit_pixel_interceptor`
- size: 1211 bytes
- sha256: `2d152a1233bca7850da6a7afaf5a6b456cb03a05d2dd41096a0ac800d152f90b`

```js
…eventData}),Reflect.apply(target,thisArg,args)}});if(void 0!==window.rdt)return window.rdt=proxyRdt(window.rdt),void 0;let _rdt;Object.defineProperty(window,"rdt",{configurable:!0,enumerable:!0,get:fu…
```

## `iabjs_pinterest_pixel_interceptor`
- size: 1366 bytes
- sha256: `f9d16b0a39cecef88a24104616fc586bcde554a9b031c09bf0f200770723d186`

```js
…event_data:eventData}),Reflect.apply(target,thisArg,args)}});if(void 0!==window.pintrk)return window.pintrk=proxyPintrk(window.pintrk),void 0;let _pintrk;Object.defineProperty(window,"pintrk",{configu…
```

## `iabjs_x_pixel_interceptor`
- size: 1231 bytes
- sha256: `93ba2138e8c39184257904c10c096e999898e21ffdf8840c5f68c1483b2c211b`

```js
…event_data:eventData}),Reflect.apply(target,thisArg,args)}});if(void 0!==window.twq)return window.twq=proxyTwq(window.twq),void 0;let _twq;Object.defineProperty(window,"twq",{configurable:!0,enumerabl…
```

## `iabjs_detect_3p_analytics_tools`
- size: 22818 bytes
- sha256: `633effbc735ca6dd5ea8d183884ec582b8f423b8cbfbd7e07bedb93e1f78db63`

```js
…og("postMessage error: "+(err instanceof Error?err.message:String(err)))}}const SCRIPT_SRC_KEYWORDS=["gtag/js?id=","googletagmanager.com/gtm.js","clarity.ms","hotjar.com","bat.bing.com","analytics.tik…
```
```js
…ow&&void 0!==window.webkit;function sendMessage(providers){const message={type:"analytics_tool_detected",analytics_providers:providers};log("sending "+providers.length+" provider(s) to native: "+provi…
```

## `iabjs_credentials_api_interceptor`
- size: 4502 bytes
- sha256: `64752807857b06b2e14718e971f0d6b2ec1f1071daccd63179fab39d03b2a389`

```js
…edentialsAPIInterceptor.js]",ENABLE_DEBUG_LOGS=!1,CREDENTIALS_GET_MESSAGE_TYPE="credentials_get",CREDENTIALS_CREATE_MESSAGE_TYPE="credentials_create",IS_UVPAA_MESSAGE_TYPE="is_user_verifying_platform_…
```
```js
…ayload)}function hasBridge(){return hasIOSBridge()||hasAndroidBridge()}function getCredentialsType(args){const argsKeys=args.flatMap((arg=>Object.keys(arg)));return argsKeys.includes("publicKey")?"pub…
```

## `iabjs_detect_login_forms`
- size: 16278 bytes
- sha256: `27d3617b118d645a18e6c639279b97269592f3b5bd246decba4e19d0f7033c10`

```js
…"login_form_field_detected",LOGIN_FORM_FIELD_FOCUSED="login_form_field_focused",LOGIN_SUBMIT_BUTTON_CLICKED="login_submit_button_clicked",LOGIN_FIELD_EMAIL_OR_USERID="email_or_userid",LOGIN_FIELD_PASS…
```
```js
…]','input[type="tel"][name*="phone" i][autocomplete="username"]'].join(",\n  "),PASSWORD_SELECTOR=['input[type="password"]','input[autocomplete="current-password"]','input[autocomplete="new-password"]…
```

## `iabjs_extract_text_for_classification`
- size: 1700 bytes
- sha256: `09e70005b6458913da8bbe104c12625b1eac40f7bfea9acbdeee76122adacca1`

```js
….stringify({strings:stringsToSend})};return window.__call_iabjs_unified_bridge("text_classification",window.__iabjs_unified_bridge_nonce,messageData),void 0}}}catch{}classifyAttempts<delays.length&&(s…
```
```js
…+1));[shuffled[i],shuffled[j]]=[shuffled[j],shuffled[i]]}stringsToSend=shuffled.slice(0,10)}const messageData={message:JSON.stringify({strings:stringsToSend})};return window.__call_iabjs_unified_bridg…
```

## `iabjs_sim_hash_logging`
- size: 3315 bytes
- sha256: `524b3b5f35b6edd47d54e2b7d30c6fe6f17fc281d95deb154be8c16a91f21889`

```js
…n hashDomNode(document.documentElement,countsDOM,countsTextAndDOM),console.log("text_and_dom: "+generateFinalHash(countsTextAndDOM)),console.log("text_only: "+generateFinalHash(countsText)),console.lo…
```

## `iabjs_utm_recovery`
- size: 4638 bytes
- sha256: `3e9dd49dedabceaf6d0d8706e0c668e1ff07dcde29cdcade97c1395aa610644c`

```js
…IPPED_HOST_MISMATCH="skipped_host_mismatch",OUTCOME_ERROR="error",MESSAGE_NAME="IABUtmRecoveryJS";function hostMatches(host,base){return host===base||host.endsWith("."+base)}function isKnownRedirector…
```
```js
…owedInitialDomainsJson,enableLogging,blockParamsJson,redirectorHostsJson){const OUTCOME_INJECTED="injected",OUTCOME_SKIPPED_EXISTING_UTM="skipped_existing_utm",OUTCOME_SKIPPED_FOREIGN_CLICK_ID="skippe…
```

## `iabjs_get_outbound_links`
- size: 1631 bytes
- sha256: `4cb542d1d2b13fb56c6c255c4171c116d2776d1ddd4def88a2489fb0d140e145`

```js
(function(){return getOutboundLinks();function getOutboundLinks(){const MAX_OUTBOUND_LINKS=10,GOOGLE_COLLECTIONS_URL_REGEX=undefined,isGoogleCollectionsPage=/^https?:\/\/www\.google\.com\/coll…
```

## `iabjs_capture_html_source`
- size: 81 bytes
- sha256: `c637510e696ae4c1286269eec49ed1ab00e3ee25e51ee33008ba8c891c211d9c`

```js
(function(){const root=document.documentElement;return root?root.innerHTML:""})()
```
