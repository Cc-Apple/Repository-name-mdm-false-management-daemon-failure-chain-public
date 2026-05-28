# Scripts Directory

## Purpose

This directory contains reproducibility scripts for the MDM-false management daemon failure chain review.

The scripts are intended to help a qualified reviewer re-scan the referenced raw ZIP artifacts in a consistent way if those raw artifacts are later provided through a secure evidence-transfer process.

Raw iOS log ZIP files are not included in this public repository.

## Main script

- `analyze_mdm_false_chain.py`

## What the script does

The script performs a read-only scan of selected raw log ZIP files when they are available locally.

It checks for:

- MDMStatus:false
- MDMEnrollmentStatus_Powerlog
- PowerlogMDMEnrollmentStatus
- managedappdistributiond
- dmd
- ScreenTimeAgent
- ScreenTime
- ManagedSettings
- CommCenter
- Baseband
- TelephonyBaseband
- BasebandPowerCycle
- SFA
- CKKS
- CloudServices
- forceReset
- stacks
- JetsamEvent
- EXC_CRASH
- EXC_BREAKPOINT
- SIGABRT
- SIGTRAP
- 0xbaaaaaad

## What the script does not do

The script does not:

- modify files
- delete files
- rename files
- rewrite logs
- extract private data for publication
- prove malware
- prove MDM enrollment
- prove attribution
- prove payload
- prove C2
- prove exploit chain

## Expected raw artifact layout

The following raw ZIP layout is referenced by the script.

These files are not included in this public repository.

15G:

- `logs/15G/2026-03-16.zip`
- `logs/15G/2026-03-17.zip`
- `logs/15G/2026-03-18.zip`
- `logs/15G/2026-03-23.zip`
- `logs/15G/2026-03-24.zip`
- `logs/15G/2026-05-05.zip`
- `logs/15G/2026-05-21.zip`

mini1:

- `logs/mini1/mini1-2026-04-03.zip`

## Run command

From the repository root, after raw artifacts have been supplied locally:

`python scripts/analyze_mdm_false_chain.py --root . --out analysis_output/mdm_false_chain_scan.json`

## Output

The script writes JSON output containing:

- missing file list
- SHA256 verification
- per-ZIP summary
- important entries
- term counts
- compact hit counts
- observed flags
- case-level summary
- per-date results
- cross-device recurrence indicators

## Public repository note

Because raw logs are not included in this public repository, the script may report missing files if run directly from the public repository alone.

That is expected.

The script is included to document the reproducibility method and allow a reviewer to run the same scan if raw artifacts are later provided securely.

## Safety

The script is read-only.

It does not modify raw logs.

It does not publish extracted content.

It only scans provided local artifacts and writes a JSON summary if an output path is specified.

## Review use

The script is not a forensic conclusion.

It is a reproducibility aid.

A reviewer should inspect the raw artifacts directly after using the script output as an index.

## Boundary

The script output does not establish:

- malware
- payload
- C2
- exploit chain
- APT attribution
- state attribution
- Apple attribution
- criminal attribution
- attacker identity
- MDM enrollment
