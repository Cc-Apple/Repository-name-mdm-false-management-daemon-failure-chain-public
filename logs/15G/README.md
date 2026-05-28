# 15G Referenced Raw Log Archives

## Purpose

This directory documents referenced raw iOS log ZIP archives for the device internally labeled **15G**.

Raw iOS log ZIP files are **not included** in this public repository.

This directory exists only to list the referenced 15G archive names, dates, roles, and review relevance.

## Device context

Internal label: **15G**

Physical class: **iPhone 12 mini class device**

Observed model identifier: **iPhone13,1**

Observed OS generation: **iPhone OS 18.5 / 22F76**

Important note: **15G is an internal Ghost / Apple ID lineage label. It does not mean the physical device is an iPhone 15 Pro.**

## Public repository boundary

This public repository does not include:

- raw iOS log ZIP archives
- .ips files
- .ips.ca.synced files
- crash logs
- spin logs
- Manifest.db files
- iMazing backup folders
- BSSID values
- Apple ID values
- banking records
- OTP records
- private screenshots

The original raw 15G logs are preserved separately.

They can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.

## Referenced 15G raw log archives

The following raw ZIP files are referenced by this package, but are not included here:

- 2026-03-16.zip
- 2026-03-17.zip
- 2026-03-18.zip
- 2026-03-23.zip
- 2026-03-24.zip
- 2026-05-05.zip
- 2026-05-21.zip

## Role by date

### 2026-03-16

Role: Cluster 1 start.

Relevant structure:

- managedappdistributiond crash
- SFA family context
- BackgroundShortcutRunner / search / mail / resource-pressure context

### 2026-03-17

Role: Cluster 1 confirmation.

Relevant structure:

- MDMStatus:false
- managedappdistributiond crash
- SFA / CKKS / CloudServices context
- deleted / searchd / maild context

### 2026-03-18

Role: Cluster 1 strongest date.

Relevant structure:

- MDMStatus:false
- managedappdistributiond multiple crashes
- dmd crash
- forceReset-full
- ScreenTime / ManagedSettings context
- SFA family in multiple windows

### 2026-03-23

Role: Cluster 2 start.

Relevant structure:

- MDMStatus:false
- managedappdistributiond multiple crashes
- forceReset-full
- maild crashes
- searchd crashes
- SFA / CKKS / CloudServices repeated across multiple windows

### 2026-03-24

Role: Cluster 2 confirmation.

Relevant structure:

- MDMStatus:false
- managedappdistributiond crash
- multiple forceReset-full artifacts
- ScreenTime / ManagedSettings context in forceReset
- SFA / CKKS / CloudServices
- CommCenter / Baseband context

### 2026-05-05

Role: Follow-up anchor.

Relevant structure:

- MDMStatus:false
- managedappdistributiond crash cluster
- ScreenTimeAgent crash cluster
- CommCenter / Baseband / TelephonyBaseband context in Analytics
- BasebandPowerCycle context
- Preferences crash

### 2026-05-21

Role: Telecom / restriction crash anchor.

Relevant structure:

- MDMStatus:false
- CommCenter crash
- ScreenTimeAgent crashes
- FaceTime service crash
- contactsd crash
- JetsamEvent containing managedappdistributiond / dmd / ScreenTime / ManagedSettings / SFA / CommCenter
- SFA / CKKS / CloudServices in morning and evening windows
- CommCenter / Baseband / TelephonyBaseband context in Analytics

## Main observed pattern

The referenced 15G archives support review of this repeated structure:

- MDMStatus:false
- managedappdistributiond / dmd
- ScreenTimeAgent / ScreenTime / ManagedSettings
- CommCenter / Baseband / TelephonyBaseband
- SFA / CKKS / CloudServices
- forceReset / JetsamEvent / crash clusters

## Evidence integrity

The SHA256 values for the referenced archives are recorded in:

- evidence_index/sha256_index.txt

A reviewer should verify SHA256 before relying on any raw artifact provided later.

## Boundary

The referenced 15G raw logs support technical validation only.

They do not establish:

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
