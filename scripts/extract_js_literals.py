"""Extract Java string literals carrying `//# sourceURL=<scheme>://<name>` into
standalone .js files (one per script name) for review.

Usage: python extract_js_literals.py <out_dir> <java files...>
"""
import re, sys, os, codecs

lit = re.compile(r'"((?:[^"\\\n]|\\.)*)"')
out = sys.argv[1]
count = 0
for path in sys.argv[2:]:
    src = open(path, encoding="utf-8", errors="replace").read()
    for m in lit.finditer(src):
        raw = m.group(1)
        if "sourceURL=" not in raw:
            continue
        try:
            text = codecs.decode(raw.encode("latin-1", "backslashreplace"), "unicode_escape")
        except Exception:
            text = raw
        name = re.search(r"sourceURL=[a-z]+://([\w.-]*)", text)
        fn = (name.group(1) if name and name.group(1) else "root") + ".js"
        with open(os.path.join(out, fn), "a", encoding="utf-8") as f:
            f.write(text + "\n")
        count += 1
print(count, "scripts")
