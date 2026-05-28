# Timeline

## Purpose

This document summarizes the reviewed anchor dates for the MDM-false management daemon failure chain.

The purpose is to show recurrence across time and across devices.

This document does not claim malware, MDM enrollment, payload, C2, exploit chain, attribution, attacker identity, or criminal activity.

Raw iOS logs, raw log ZIP archives, debug archives, and sysdiagnose archives are not included in this public repository.

## Timeline overview

Reviewed dates:

* 2026-03-16 / 15G
* 2026-03-17 / 15G
* 2026-03-18 / 15G
* 2026-03-23 / 15G
* 2026-03-24 / 15G
* 2026-04-03 / mini1
* 2026-05-05 / 15G
* 2026-05-21 / 15G

## 2026-03-16 / 15G

Role:

Cluster 1 start.

Observed structure:

* managedappdistributiond crash
* SFA family context
* BackgroundShortcutRunner / search / mail / resource-pressure context

Interpretation:

This date begins the first management-adjacent failure cluster.

MDMStatus:false was not the strongest element on this date, but the management daemon failure is important as the lead-in to 2026-03-17 and 2026-03-18.

## 2026-03-17 / 15G

Role:

Cluster 1 confirmation.

Observed structure:

* MDMStatus:false
* managedappdistributiond crash
* SFA / CKKS / CloudServices family
* deleted / searchd / maild context

Interpretation:

This date connects MDMStatus:false with managedappdistributiond failure and account-cloud diagnostic context.

## 2026-03-18 / 15G

Role:

Cluster 1 strongest date.

Observed structure:

* MDMStatus:false
* managedappdistributiond multiple crashes
* dmd crash
* forceReset-full
* SFA family appears in multiple windows
* ScreenTime / ManagedSettings context appears in forceReset

Interpretation:

This date is a strong anchor because MDMStatus:false, managedappdistributiond, dmd, forceReset, ScreenTime, ManagedSettings, and SFA context appear together.

## 2026-03-23 / 15G

Role:

Cluster 2 start.

Observed structure:

* MDMStatus:false
* managedappdistributiond multiple crashes
* forceReset-full
* maild crashes
* searchd crashes
* SFA / CKKS / CloudServices repeated across several time windows
* BackgroundShortcutRunner / duetexpertd / assetsd resource context

Interpretation:

This date shows that the structure is not limited to 2026-03-16 through 2026-03-18.

It starts a second March cluster.

## 2026-03-24 / 15G

Role:

Cluster 2 confirmation.

Observed structure:

* MDMStatus:false
* managedappdistributiond crash
* multiple forceReset-full artifacts
* SFA / CKKS / CloudServices
* CommCenter / Baseband context
* ScreenTime / ManagedSettings context in forceReset

Interpretation:

This date confirms the second cluster.

The repeated forceReset artifacts make the co-location of components important.

## 2026-04-03 / mini1

Role:

Cross-device anchor.

Observed structure:

* MDMStatus:false
* managedappdistributiond crashes
* ScreenTimeAgent crash
* Analytics with CommCenter / Baseband / SFA context
* stacks containing dmd / ScreenTime / ManagedSettings / CommCenter / Baseband
* SFA / CKKS / CloudServices family later the same day

Interpretation:

This is a key cross-device replication point.

The same broad structure appears on mini1, not only on 15G.

This weakens a single-device-only explanation.

## 2026-05-05 / 15G

Role:

Follow-up anchor.

Observed structure:

* MDMStatus:false
* managedappdistributiond crash cluster
* ScreenTimeAgent crash cluster
* CommCenter / Baseband / TelephonyBaseband context in Analytics
* BasebandPowerCycle context
* Preferences crash
* deleted / duetexpertd / spotlightknowledged / triald resource context

Interpretation:

This date shows the pattern continuing into May.

The same-time managedappdistributiond and ScreenTimeAgent crash cluster is important.

## 2026-05-21 / 15G

Role:

Telecom / restriction crash anchor.

Observed structure:

* MDMStatus:false
* CommCenter crash
* ScreenTimeAgent crashes
* FaceTime service crash
* contactsd crash
* JetsamEvent containing managedappdistributiond / dmd / ScreenTime / ManagedSettings / SFA / CommCenter
* SFA / CKKS / CloudServices in morning and evening windows
* CommCenter / Baseband / TelephonyBaseband context in Analytics

Interpretation:

This date strongly connects the MDM-false chain with telecom/baseband and restriction-related crash clustering.

## Pattern summary

Cluster 1:

* 2026-03-16 to 2026-03-18 / 15G

Cluster 2:

* 2026-03-23 to 2026-03-24 / 15G

Cross-device anchor:

* 2026-04-03 / mini1

Follow-up anchor:

* 2026-05-05 / 15G

Telecom / restriction crash anchor:

* 2026-05-21 / 15G

## Core repeated structure

The repeated structure under review is:

* MDMStatus:false
* managedappdistributiond
* dmd
* ScreenTimeAgent / ScreenTime / ManagedSettings
* CommCenter / Baseband / TelephonyBaseband
* SFA / CKKS / CloudServices
* forceReset / stacks / JetsamEvent
* recurrence across 15G and mini1

## Review meaning

The timeline suggests that the pattern is not isolated to one day.

It appears across:

* multiple March dates
* a separate April cross-device anchor
* multiple May follow-up anchors
* two device labels: 15G and mini1

This does not prove malicious activity.

It does justify qualified review of whether the repeated structure can be explained by normal iOS behavior, shared iOS build behavior, shared Apple ID lineage, benign diagnostics, or policy/account-cloud state.

## Boundary

This timeline does not establish:

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

This document supports technical review only.

## Evidence boundary

The raw log archives referenced by this timeline are preserved separately.

They are not included in this public repository.

They can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.
