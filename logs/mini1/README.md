# mini1 Referenced Raw Log Archive

## Purpose

This directory documents the referenced raw iOS log ZIP archive for the device internally labeled **mini1**.

Raw iOS log ZIP files are **not included** in this public repository.

This directory exists only to list the referenced mini1 archive name, date, role, and review relevance.

## Device context

Internal label: **mini1**

Physical class: **iPhone 12 mini class device**

Observed model identifier: **iPhone13,1**

Observed OS generation: **iPhone OS 18.5 / 22F76**

mini1 is included as the cross-device replication anchor for the MDM-false management daemon failure chain.

## Public repository boundary

This public repository does not include:

* raw iOS log ZIP archives
* .ips files
* .ips.ca.synced files
* crash logs
* spin logs
* Manifest.db files
* iMazing backup folders
* BSSID values
* Apple ID values
* banking records
* OTP records
* private screenshots

The original raw mini1 log archive is preserved separately.

It can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.

## Referenced mini1 raw log archive

The following raw ZIP file is referenced by this package, but is not included here:

* mini1-2026-04-03.zip

## Role

### 2026-04-03 / mini1

Role: Cross-device anchor.

Relevant structure:

* MDMStatus:false
* managedappdistributiond crashes
* ScreenTimeAgent crash
* Analytics with CommCenter / Baseband / SFA context
* stacks containing dmd / ScreenTime / ManagedSettings / CommCenter / Baseband
* SFA / CKKS / CloudServices later the same day

## Why mini1 matters

The mini1 artifact is important because it shows that the observed structure is not limited to 15G.

This weakens a single-device-only explanation.

It supports review of the pattern as a cross-device artifact structure.

## Main observed pattern

The referenced mini1 archive supports review of this structure:

* MDMStatus:false
* managedappdistributiond crashes
* ScreenTimeAgent crash
* Analytics with CommCenter / Baseband / SFA context
* stacks containing dmd / ScreenTime / ManagedSettings / CommCenter / Baseband
* SFA / CKKS / CloudServices later the same day

## Evidence integrity

The SHA256 value for the referenced archive is recorded in:

* evidence_index/sha256_index.txt

A reviewer should verify SHA256 before relying on the raw artifact provided later.

## Boundary

The referenced mini1 raw log archive supports technical validation only.

It does not establish:

* malware
* payload
* C2
* exploit chain
* APT attribution
* state attribution
* Apple attribution
* criminal attribution
* attacker identity
* MDM enrollment
