"""Detect third-party tracker SDKs by matching Exodus Privacy code signatures
against class descriptors in every DEX file of each APK (no decompilation)."""
import json, re, sys, zipfile, os

trackers = json.load(open(sys.argv[1]))["trackers"].values()
sigs = []
for t in trackers:
    sig = t["code_signature"].strip()
    if not sig:
        continue
    for part in sig.split("|"):
        part = part.strip().rstrip(".")
        if not part:
            continue
        desc = "L" + part.replace("\\.", "/").replace(".", "/")
        sigs.append((t["name"], desc.encode()))

result = {}
for apk in sys.argv[2:]:
    name = os.path.splitext(os.path.basename(apk))[0]
    blob = b""
    with zipfile.ZipFile(apk) as z:
        for n in z.namelist():
            if re.fullmatch(r"classes\d*\.dex", n):
                blob += z.read(n)
    found = sorted({tn for tn, d in sigs if d in blob})
    result[name] = found
    print(f"{name} ({len(found)}): {', '.join(found)}")
json.dump(result, open("work/trackers.json", "w"), indent=1)
