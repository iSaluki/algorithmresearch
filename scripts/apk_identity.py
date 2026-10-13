"""Print package identity, version and signing-certificate details for APKs."""
import hashlib, sys
from androguard.core.apk import APK
from androguard.util import set_log
set_log("ERROR")

for path in sys.argv[1:]:
    a = APK(path)
    certs = a.get_certificates()
    print(f"== {path}")
    print(f"  package={a.get_package()} version={a.get_androidversion_name()} ({a.get_androidversion_code()}) "
          f"minSdk={a.get_min_sdk_version()} targetSdk={a.get_target_sdk_version()}")
    print(f"  signed v1={a.is_signed_v1()} v2={a.is_signed_v2()} v3={a.is_signed_v3()}")
    for c in certs:
        der = c.dump()
        print(f"  cert subject: {c.subject.human_friendly}")
        print(f"  cert sha256 : {hashlib.sha256(der).hexdigest()}")
