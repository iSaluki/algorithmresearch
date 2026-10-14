"""Summarise privacy-relevant manifest declarations for each APK into JSON."""
import json, sys, os, re
from androguard.core.apk import APK
from androguard.util import set_log
set_log("ERROR")

NS = "{http://schemas.android.com/apk/res/android}"
out_dir = sys.argv[1]
for path in sys.argv[2:]:
    name = os.path.splitext(os.path.basename(path))[0]
    a = APK(path)
    m = a.get_android_manifest_xml()
    perms = sorted(a.get_permissions())
    details = a.get_details_permissions()
    dangerous = sorted(p for p, d in details.items() if d and "dangerous" in str(d[0]))
    queries = {"packages": [], "intents": [], "providers": []}
    for q in m.findall("queries"):
        for p in q.findall("package"):
            queries["packages"].append(p.get(NS + "name"))
        for i in q.findall("intent"):
            acts = [x.get(NS + "name") for x in i.findall("action")]
            data = [{k.replace(NS, ""): v for k, v in x.attrib.items()} for x in i.findall("data")]
            queries["intents"].append({"actions": acts, "data": data})
        for p in q.findall("provider"):
            queries["providers"].append(p.get(NS + "authorities"))
    app = m.find("application")
    meta = {x.get(NS + "name"): x.get(NS + "value") or x.get(NS + "resource") for x in app.iter("meta-data")}
    # Redact embedded client tokens/keys so audits can be published.
    meta = {k: ("[redacted]" if re.search(r"token|apikey|api_key|secret|client_?key|client_?id", k or "", re.I) and v and not str(v).startswith("@") else v) for k, v in meta.items()}
    def comps(tag):
        res = []
        for c in app.findall(tag):
            filters = []
            for f in c.findall("intent-filter"):
                filters += [x.get(NS + "name") for x in f.findall("action")]
            exported = c.get(NS + "exported")
            res.append({"name": c.get(NS + "name"), "exported": exported, "actions": filters,
                        "permission": c.get(NS + "permission"),
                        "foregroundServiceType": c.get(NS + "foregroundServiceType")})
        return res
    data = {
        "package": a.get_package(), "version": a.get_androidversion_name(),
        "permissions": perms, "dangerous_permissions": dangerous, "queries": queries,
        "app_attrs": {k.replace(NS, ""): v for k, v in app.attrib.items()},
        "meta_data": meta,
        "activities": len(app.findall("activity")) + len(app.findall("activity-alias")),
        "services": comps("service"), "receivers": comps("receiver"), "providers": comps("provider"),
    }
    with open(os.path.join(out_dir, f"{name}.manifest.json"), "w") as f:
        json.dump(data, f, indent=1)
    print(f"{name}: {len(perms)} perms ({len(dangerous)} dangerous), {len(queries['packages'])} queried pkgs, "
          f"{len(data['services'])} services, {len(data['receivers'])} receivers")
