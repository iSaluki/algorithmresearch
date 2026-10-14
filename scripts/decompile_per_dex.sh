#!/usr/bin/env bash
# Decompile every classesN.dex of the given apps separately (low memory), two at a time.
cd "$(dirname "$0")/.."
export JAVA_OPTS="${JAVA_OPTS:--Xmx6g}"
run() { app=$1; dex=$2; out=work/$app/jdex/${dex%.dex}
  [ -f "$out/.done" ] && return
  rm -rf "$out"; mkdir -p "$out"
  tools/bin/jadx/bin/jadx -j 2 --no-res --show-bad-code -d "$out" "work/$app/dex/$dex" > "$out.log" 2>&1
  touch "$out/.done"; echo "$app $dex done"; }
for app in "$@"; do
  mkdir -p work/$app/dex work/$app/jdex
  unzip -o -q apks/base/$app.apk 'classes*.dex' -d work/$app/dex
  set -- $(ls work/$app/dex | sort -V)
  while [ $# -gt 0 ]; do
    run $app $1 & [ $# -gt 1 ] && run $app $2 & wait
    shift; [ $# -gt 0 ] && shift
  done
done
