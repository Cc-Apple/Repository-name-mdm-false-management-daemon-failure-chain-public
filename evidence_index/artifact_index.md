# Artifact Index

## Purpose

This document lists the referenced raw log ZIP archives and their role in the MDM-false management daemon failure chain.

Raw iOS log ZIP files are not included in this public repository.

This index is intended to help a qualified forensic reviewer understand which original files exist, what role each file plays, and which artifacts are primary anchors versus supporting context.

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
- sysdiagnose archives
- debug archives

The original raw artifacts are preserved separately and can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.

## Boundary

This artifact index does not establish:

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

It supports evidence organization and forensic review only.

## Device: 15G

### 2026-03-16.zip

Role:

Cluster 1 start.

Key observed relevance:

- managedappdistributiond crash
- SFA family context
- BackgroundShortcutRunner / search / mail / resource-pressure context

Review meaning:

This date begins the first management-adjacent failure cluster.

It is relevant as a lead-in to the stronger 2026-03-17 and 2026-03-18 observations.

### 2026-03-17.zip

Role:

Cluster 1 confirmation.

Key observed relevance:

- MDMStatus:false
- managedappdistributiond crash
- SFA / CKKS / CloudServices context
- deleted / searchd / maild context

Review meaning:

This date connects MDMStatus:false with managedappdistributiond failure and account-cloud diagnostic context.

### 2026-03-18.zip

Role:

Cluster 1 strongest date.

Key observed relevance:

- MDMStatus:false
- managedappdistributiond multiple crashes
- dmd crash
- forceReset-full
- ScreenTime / ManagedSettings context
- SFA family in multiple windows

Review meaning:

This is a strong anchor because MDMStatus:false, managedappdistributiond, dmd, forceReset, ScreenTime, ManagedSettings, and SFA context appear together.

### 2026-03-23.zip

Role:

Cluster 2 start.

Key observed relevance:

- MDMStatus:false
- managedappdistributiond multiple crashes
- forceReset-full
- maild crashes
- searchd crashes
- SFA / CKKS / CloudServices repeated across multiple windows

Review meaning:

This date starts a second March cluster and shows that the structure is not limited to 2026-03-16 through 2026-03-18.

### 2026-03-24.zip

Role:

Cluster 2 confirmation.

Key observed relevance:

- MDMStatus:false
- managedappdistributiond crash
- multiple forceReset-full artifacts
- ScreenTime / ManagedSettings context in forceReset
- SFA / CKKS / CloudServices
- CommCenter / Baseband context

Review meaning:

This date confirms the second March cluster.

The repeated forceReset artifacts are important because they show component co-location.

### 2026-05-05.zip

Role:

Follow-up anchor.

Key observed relevance:

- MDMStatus:false
- managedappdistributiond crash cluster
- ScreenTimeAgent crash cluster
- CommCenter / Baseband / TelephonyBaseband context in Analytics
- BasebandPowerCycle context
- Preferences crash
- deleted / duetexpertd / spotlightknowledged / triald resource context

Review meaning:

This date shows the pattern continuing into May.

The same-time managedappdistributiond and ScreenTimeAgent crash cluster is important.

### 2026-05-21.zip

Role:

Telecom / restriction crash anchor.

Key observed relevance:

- MDMStatus:false
- CommCenter crash
- ScreenTimeAgent crashes
- FaceTime service crash
- contactsd crash
- JetsamEvent containing managedappdistributiond / dmd / ScreenTime / ManagedSettings / SFA / CommCenter
- SFA / CKKS / CloudServices in morning and evening windows
- CommCenter / Baseband / TelephonyBaseband context in Analytics

Review meaning:

This date strongly connects the MDM-false chain with telecom/baseband and restriction-related crash clustering.

## Device: mini1

### mini1-2026-04-03.zip

Role:

Cross-device anchor.

Key observed relevance:

- MDMStatus:false
- managedappdistributiond crashes
- ScreenTimeAgent crash
- Analytics with CommCenter / Baseband / SFA context
- stacks containing dmd / ScreenTime / ManagedSettings / CommCenter / Baseband
- SFA / CKKS / CloudServices later the same day

Review meaning:

This is a key cross-device replication point.

The same broad structure appears on mini1, not only on 15G.

This weakens a single-device-only explanation.

## Key artifact families

### Analytics

Relevant observations:

- MDMStatus:false
- MDMEnrollmentStatus_Powerlog
- PowerlogMDMEnrollmentStatus
- CommCenter
- Baseband
- TelephonyBaseband
- BasebandPowerCycle
- SFA context

### managedappdistributiond

Relevant observations:

- management-adjacent daemon
- repeated crashes
- often bug_type 309
- EXC_BREAKPOINT / SIGTRAP pattern observed

### dmd

Relevant observations:

- appears in dmd crash, forceReset, stacks, or JetsamEvent contexts
- management-adjacent component
- important when co-located with ScreenTime / ManagedSettings

### ScreenTimeAgent / ScreenTime / ManagedSettings

Relevant observations:

- ScreenTimeAgent crashes
- ScreenTime references
- ManagedSettings references
- restriction-related component group

### CommCenter / Baseband / TelephonyBaseband

Relevant observations:

- CommCenter crash
- Baseband context
- TelephonyBaseband context
- BasebandPowerCycle
- carrier / cellular context

### SFA / CKKS / CloudServices

Relevant observations:

- SFA family artifacts
- CKKS context
- CloudServices context
- PCS / SOS / networking / transparency context

### forceReset / stacks / JetsamEvent

Relevant observations:

- co-location artifacts
- show multiple components together
- more meaningful than isolated string hits

## Raw artifact location

The raw ZIP files referenced in this index are not included in this public repository.

Referenced original layout:

15G:

- logs/15G/2026-03-16.zip
- logs/15G/2026-03-17.zip
- logs/15G/2026-03-18.zip
- logs/15G/2026-03-23.zip
- logs/15G/2026-03-24.zip
- logs/15G/2026-05-05.zip
- logs/15G/2026-05-21.zip

mini1:

- logs/mini1/mini1-2026-04-03.zip

## SHA256 verification

SHA256 values are recorded in:

- evidence_index/sha256_index.txt

A reviewer should verify SHA256 before relying on any raw artifact provided later.

## Review priority

Highest-priority raw archives if requested later:

- 2026-03-18.zip
- 2026-03-23.zip
- 2026-03-24.zip
- mini1-2026-04-03.zip
- 2026-05-05.zip
- 2026-05-21.zip

Supporting raw archives:

- 2026-03-16.zip
- 2026-03-17.zip

## Final boundary

This index organizes referenced artifacts for review.

It does not prove compromise.

It does not prove MDM enrollment.

It does not assign attribution.

It identifies the preserved artifact set and explains why each referenced archive is relevant.
