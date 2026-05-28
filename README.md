# MDM-False Management Daemon Failure Chain - Public Package

## Status

Public preliminary technical review package.

This repository is intended for qualified digital forensics, incident response, mobile forensic, legal-technical, or security research review.

It is not a public accusation or attribution claim.

## Core observation

This repository documents a repeated cross-device artifact pattern observed across the devices internally labeled **15G** and **mini1**.

The key observation is not that MDM enrollment is confirmed.

The key observation is that `MDMStatus:false` repeatedly appears on days where management-adjacent daemons and restriction-related services fail, crash, or cluster together.

Observed component families include:

- managedappdistributiond
- dmd
- ScreenTimeAgent
- ScreenTime
- ManagedSettings
- CommCenter
- Baseband
- TelephonyBaseband
- SFA / CKKS / CloudServices
- forceReset
- stacks
- JetsamEvent

## Public repository boundary

Raw iOS logs are **not included** in this public repository.

Raw sysdiagnose archives are **not included** in this public repository.

Large debug archives are **not included** in this public repository.

This public repository contains only:

- written technical summaries
- timeline summaries
- device matrix
- artifact indexes
- SHA256 references
- referenced log titles
- forensic review questions
- non-attribution statement
- raw artifact handling policy
- reviewer quick-start notes
- reproducibility / analysis script

The original raw logs, debug archives, and sysdiagnose archives are preserved separately and can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.

## Devices

### 15G

Internal label: **15G**

Physical class: **iPhone 12 mini class device**

Observed model identifier: **iPhone13,1**

Observed OS generation: **iPhone OS 18.5 / 22F76**

Important note: **15G is an internal Ghost / Apple ID lineage label. It does not mean the physical device is an iPhone 15 Pro.**

### mini1

Internal label: **mini1**

Physical class: **iPhone 12 mini class device**

Observed model identifier: **iPhone13,1**

Observed OS generation: **iPhone OS 18.5 / 22F76**

mini1 is included as a cross-device replication anchor.

## Reviewed anchor dates

- 2026-03-16 / 15G
- 2026-03-17 / 15G
- 2026-03-18 / 15G
- 2026-03-23 / 15G
- 2026-03-24 / 15G
- 2026-04-03 / mini1
- 2026-05-05 / 15G
- 2026-05-21 / 15G

## Why this matters

A simple interpretation would be:

- `MDMStatus:false` means the device was not MDM-enrolled.

However, the reviewed artifacts show a more complex repeated structure:

- `MDMStatus:false` appears repeatedly.
- Management-adjacent daemons fail or cluster on the same dates.
- Restriction-related components appear in the same artifact windows.
- Telecom / baseband / account-cloud components appear in the same broader context.
- The pattern appears on more than one device.

This creates the following technical question:

Can this repeated structure be explained by normal iOS behavior, or does it represent a support-invisible, policy-adjacent, account/cloud, or management-layer anomaly requiring formal forensic review?

## High-level timeline

### 2026-03-16 to 2026-03-18 / 15G

Cluster 1.

Observed structure:

- managedappdistributiond crash
- `MDMStatus:false`
- dmd crash
- forceReset context
- ScreenTime / ManagedSettings context
- SFA family context

### 2026-03-23 to 2026-03-24 / 15G

Cluster 2.

Observed structure:

- `MDMStatus:false`
- managedappdistributiond repeated crashes
- forceReset artifacts
- ScreenTime / ManagedSettings context
- SFA / CKKS / CloudServices context
- CommCenter / Baseband context

### 2026-04-03 / mini1

Cross-device anchor.

Observed structure:

- `MDMStatus:false`
- managedappdistributiond crashes
- ScreenTimeAgent crash
- Analytics with CommCenter / Baseband / SFA context
- stacks containing dmd / ScreenTime / ManagedSettings / CommCenter / Baseband
- SFA / CKKS / CloudServices later the same day

### 2026-05-05 / 15G

Follow-up anchor.

Observed structure:

- `MDMStatus:false`
- managedappdistributiond crash cluster
- ScreenTimeAgent crash cluster
- CommCenter / Baseband / TelephonyBaseband context in Analytics
- BasebandPowerCycle context
- Preferences crash

### 2026-05-21 / 15G

Telecom / restriction crash anchor.

Observed structure:

- `MDMStatus:false`
- CommCenter crash
- ScreenTimeAgent crashes
- FaceTime service crash
- contactsd crash
- JetsamEvent containing managedappdistributiond / dmd / ScreenTime / ManagedSettings / SFA / CommCenter
- SFA / CKKS / CloudServices in morning and evening windows
- CommCenter / Baseband / TelephonyBaseband context in Analytics

## Core repeated structure

The repeated structure under review is:

- `MDMStatus:false`
- managedappdistributiond / dmd
- ScreenTimeAgent / ScreenTime / ManagedSettings
- CommCenter / Baseband / TelephonyBaseband
- SFA / CKKS / CloudServices
- forceReset / stacks / JetsamEvent
- recurrence across 15G and mini1

## Referenced raw log archives

The raw ZIP files listed below are **not included** in this public repository.

They are listed only to support later verification and evidence matching.

### 15G

- 2026-03-16.zip
- 2026-03-17.zip
- 2026-03-18.zip
- 2026-03-23.zip
- 2026-03-24.zip
- 2026-05-05.zip
- 2026-05-21.zip

### mini1

- mini1-2026-04-03.zip

## Working interpretation

The observed structure is consistent with a management-adjacent failure chain operating while normal MDM enrollment indicators remain false.

This does not prove malware.

This does not prove MDM enrollment.

This does not prove attribution.

It does justify qualified forensic review because the same structure appears repeatedly across dates and across more than one device.

## What this repository claims

This repository claims only the following:

- A repeated artifact pattern exists.
- The pattern includes `MDMStatus:false` and same-day or near-same-day management-adjacent daemon failures or clustering.
- The pattern appears across more than one device.
- The pattern is technically meaningful enough to preserve and submit for qualified forensic review.

## Important boundary

This repository does **not** establish:

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

## Repository structure

- docs/
  - written technical summaries
  - timeline
  - device matrix
  - forensic review questions
  - external debug / sysdiagnose storage notes

- machine/
  - machine-readable summary

- evidence_index/
  - SHA256 references
  - artifact index

- scripts/
  - reproducibility / analysis script

- logs/
  - public README references only
  - raw ZIP files are not included in this public repository

- analysis_output/
  - README for generated script output

## Main review question

Can repeated `MDMStatus:false` observations normally coexist with repeated management-adjacent daemon failures across more than one device, or does this structure justify deeper mobile forensic review?

## Evidence handling

Raw artifacts are preserved separately.

If a qualified reviewer requests the raw files, the transfer method should be agreed first.

Preferred options:

- secure upload portal provided by the reviewer
- encrypted archive with password shared through a separate channel
- formal evidence-handling agreement
- NDA if required
- controlled physical review if device-level examination is required
