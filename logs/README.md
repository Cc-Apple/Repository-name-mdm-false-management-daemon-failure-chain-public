# Logs Directory

## Purpose

This directory documents referenced raw iOS log ZIP archives for the MDM-false management daemon failure chain.

Raw iOS log ZIP files are not included in this public repository.

This directory exists only to list the referenced log archive names, device labels, dates, roles, and verification purpose.

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

The original raw logs are preserved separately.

They can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.

## Referenced log archive layout

The following raw archive layout is referenced by this package, but the raw ZIP files are not included here.

15G:

* logs/15G/2026-03-16.zip
* logs/15G/2026-03-17.zip
* logs/15G/2026-03-18.zip
* logs/15G/2026-03-23.zip
* logs/15G/2026-03-24.zip
* logs/15G/2026-05-05.zip
* logs/15G/2026-05-21.zip

mini1:

* logs/mini1/mini1-2026-04-03.zip

## Role by date

### 2026-03-16 / 15G

Role:

Cluster 1 start.

Relevant structure:

* managedappdistributiond crash
* SFA family context
* BackgroundShortcutRunner / search / mail / resource-pressure context

### 2026-03-17 / 15G

Role:

Cluster 1 confirmation.

Relevant structure:

* MDMStatus:false
* managedappdistributiond crash
* SFA / CKKS / CloudServices context
* deleted / searchd / maild context

### 2026-03-18 / 15G

Role:

Cluster 1 strongest date.

Relevant structure:

* MDMStatus:false
* managedappdistributiond multiple crashes
* dmd crash
* forceReset-full
* ScreenTime / ManagedSettings context
* SFA family in multiple windows

### 2026-03-23 / 15G

Role:

Cluster 2 start.

Relevant structure:

* MDMStatus:false
* managedappdistributiond multiple crashes
* forceReset-full
* maild crashes
* searchd crashes
* SFA / CKKS / CloudServices repeated across multiple windows

### 2026-03-24 / 15G

Role:

Cluster 2 confirmation.

Relevant structure:

* MDMStatus:false
* managedappdistributiond crash
* multiple forceReset-full artifacts
* ScreenTime / ManagedSettings context in forceReset
* SFA / CKKS / CloudServices
* CommCenter / Baseband context

### 2026-04-03 / mini1

Role:

Cross-device anchor.

Relevant structure:

* MDMStatus:false
* managedappdistributiond crashes
* ScreenTimeAgent crash
* Analytics with CommCenter / Baseband / SFA context
* stacks containing dmd / ScreenTime / ManagedSettings / CommCenter / Baseband
* SFA / CKKS / CloudServices later the same day

### 2026-05-05 / 15G

Role:

Follow-up anchor.

Relevant structure:

* MDMStatus:false
* managedappdistributiond crash cluster
* ScreenTimeAgent crash cluster
* CommCenter / Baseband / TelephonyBaseband context in Analytics
* BasebandPowerCycle context
* Preferences crash

### 2026-05-21 / 15G

Role:

Telecom / restriction crash anchor.

Relevant structure:

* MDMStatus:false
* CommCenter crash
* ScreenTimeAgent crashes
* FaceTime service crash
* contactsd crash
* JetsamEvent containing managedappdistributiond / dmd / ScreenTime / ManagedSettings / SFA / CommCenter
* SFA / CKKS / CloudServices in morning and evening windows
* CommCenter / Baseband / TelephonyBaseband context in Analytics

## Evidence integrity

Each referenced raw ZIP file is identified by SHA256 in:

* evidence_index/sha256_index.txt

A reviewer should verify the SHA256 value before relying on any raw artifact provided later.

## Privacy warning

Raw iOS logs may contain sensitive information, including:

* device identifiers
* account traces
* app activity
* network metadata
* carrier / telecom context
* timestamps
* local paths
* personal usage patterns
* third-party identifiers

For this reason, raw logs are not published in this public repository.

## Boundary

The referenced raw logs are preserved for technical validation only.

They do not establish:

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
