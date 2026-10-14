# algorithmresearch

Independent research into **dark patterns, manipulative design and data collection in popular Android apps**,
done by statically reverse-engineering the apps as shipped to users.

**Start with [REPORT.md](REPORT.md)**, which has the ranked findings, per-app detail and evidence pointers.

## Apps covered

| Batch | Apps |
|-------|------|
| 1 | Instagram, Snapchat, Reddit, Duolingo, Dexcom G7, Proton Mail |
| 2 | Facebook\*, WhatsApp, Telegram, Google Photos, Discord, Chess.com, Waze, BBC News (UK and International), Signal, Proton VPN\*\* |

\* Facebook's main code ships in Meta's proprietary Superpack compression and could not be decompiled. Its
section rests on the manifest, resources, bundled assets and the names of its server-side feature switches
(see `scripts/superpack/`).

\*\* Proton VPN was analysed from its open-source F-Droid build, which may differ from the Play Store build.

Claude was also requested but no APK could be obtained.

Exact versions, package names and signing-certificate fingerprints are listed in `evidence/apk_identity*.txt`
and `evidence/apk_sha256.txt`.

## What this research is (and is not)

- **Static analysis only.** The apps were decompiled and read; they were never installed, run, or connected to a
  network. Findings describe what the shipped code and bundled text *do* or *can do*.
- **Capability is not the same as current use.** Much app behaviour is controlled by server-side flags and
  experiments that can't be seen in an APK. Where a finding depends on such a switch, the report says so and
  gives the shipped default. It can't say how many users have a feature switched on.
- **Evidence is citable and reproducible.** Findings point to decompiled class files and strings. Class names in
  obfuscated apps are decompiler aliases (e.g. `X/C657102iX`, `defpackage/AKi`), which are stable for the listed
  APK versions but change between app versions.
- **Not legal advice.** "Dark pattern" and "should not be tracking" are the researcher's assessments, not legal
  conclusions. Corrections are welcome; please open an issue with the class or string that contradicts a finding.

## How the analysis was done

1. **Acquire** APKs with [apkeep](https://github.com/EFForg/apkeep) (APKPure, or F-Droid where noted), then
   **verify** every base APK's signing certificate against the publisher (`scripts/apk_identity.py`). No APKs or
   decompiled app code are committed to this repository.
2. **Inventory**: manifest permissions, `<queries>` package-visibility declarations, exported components and
   meta-data (`scripts/manifest_audit.py`); third-party SDKs via [Exodus Privacy](https://exodus-privacy.eu.org/)
   tracker signatures matched against DEX class descriptors (`scripts/tracker_scan.py`).
3. **Decompile** with JADX 1.5.3, one DEX file at a time for very large apps (`scripts/decompile_per_dex.sh`), and
   decode resources with Apktool 2.12.1. React Native apps (Discord, BBC News International) ship Hermes bytecode,
   which was disassembled (hermes-dec) or read from string tables.
4. **Sweep and read**: `scripts/scan_patterns.py` flags privacy-sensitive APIs and engagement or dark-pattern
   identifiers and copy; every finding in the report was then confirmed by reading the code. Leads that turned
   out benign are listed in the report as "checked and cleared".
5. **Trace** specific questions with **[REA — Reverse Engineer Anything](https://github.com/morluto/rea)**, which
   produces evidence records bound to the APK's SHA-256 (`evidence/rea/`).

The analysis was carried out with AI assistance (Claude Code, driving the tools above; batch-2 deep reads were run
by parallel AI agents and the headline claims re-checked against the code). All claims are grounded in the cited
code and strings, which readers can check independently.

## Repository layout

| Path | Contents |
|------|----------|
| `REPORT.md` | The findings report |
| `notes/` | Per-app working notes with additional file/line pointers |
| `evidence/` | APK identities and hashes, manifest audits, tracker inventory, pattern-scan output, REA evidence records, short excerpts of injected browser scripts |
| `scripts/` | Analysis helpers used to produce the evidence; `scripts/superpack/` is the (unsuccessful) Facebook unpacking attempt |
| `tools/setup.sh` | Installs REA, JADX, Apktool and the audited jadx-headless-mcp engine |
| `.mcp.json`, `.claude/skills/reverse-engineer-anything/` | REA registration and its workflow skill for Claude Code (MIT, © morluto; see the `LICENSE` in that folder) |

`apks/`, `work/` (decompiler output) and `tools/bin/` are git-ignored.

## Reproducing

```bash
tools/setup.sh                                   # REA + JADX + Apktool
export REA_JADX_MCP_JAR=$PWD/tools/bin/jadx-headless-mcp-0.7.1-all.jar
export REA_APKTOOL_COMMAND=$PWD/tools/bin/apktool
tools/bin/apkeep -a <package> -d apk-pure -o 'acknowledge_dangers=true,arch=arm64-v8a' apks/
python3 scripts/apk_identity.py apks/<app>.apk  # verify the signer before analysing
scripts/decompile_per_dex.sh <app>               # expects apks/base/<app>.apk
```

APKPure is a third-party mirror. Always check the signing certificate before trusting a downloaded APK.
