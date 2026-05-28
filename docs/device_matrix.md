# Device Matrix

## Purpose

This document separates the observed MDM-false management daemon failure chain by device.

The purpose is to show that the observed pattern is not limited to a single device line.

This document does not claim malware, MDM enrollment, payload, C2, exploit chain, attribution, attacker identity, or criminal activity.

Raw iOS logs, raw log ZIP archives, debug archives, and sysdiagnose archives are not included in this public repository.

## Device overview

### 15G

15G is the main observed device line for this repository.

It contains multiple anchor dates from 2026-03 to 2026-05.

### mini1

mini1 is included as a cross-device replication anchor.

It contains one key anchor date on 2026-04-03.

## 15G

### Device context

Internal label: **15G**

Physical class: **iPhone 12 mini class device**

Observed model identifier: **iPhone13,1**

Observed OS generation: **iPhone OS 18.5 / 22F76**

Important note: **15G is an internal Ghost / Apple ID lineage label. It does not mean the physical device is an iPhone 15 Pro.**

### Reviewed 15G dates

- 2026-03-16
- 2026-03-17
- 2026-03-18
- 2026-03-23
- 2026-03-24
- 2026-05-05
- 2026-05-21

### 15G pattern summary

The 15G line shows:

- repeated MDMStatus:false observations
- managedappdistributiond crashes
- dmd context
- ScreenTimeAgent / ScreenTime / ManagedSettings context
- forceReset / JetsamEvent support
- SFA / CKKS / CloudServices recurrence
- CommCenter / Baseband / TelephonyBaseband context

### Strong 15G anchors

#### 2026-03-18

Observed structure:

- MDMStatus:false
- managedappdistributiond multiple crashes
- dmd crash
- forceReset-full
- ScreenTime / ManagedSettings / SFA context

Review meaning:

This is one of the strongest March anchors because management-adjacent, restriction-related, and account-cloud components appear together.

#### 2026-03-23

Observed structure:

- MDMStatus:false
- managedappdistributiond multiple crashes
- forceReset-full
- SFA / CKKS / CloudServices repeated

Review meaning:

This date starts the second March cluster and shows recurrence beyond the first cluster.

#### 2026-03-24

Observed structure:

- MDMStatus:false
- managedappdistributiond crash
- multiple forceReset-full artifacts
- SFA / CKKS / CloudServices
- CommCenter / Baseband context

Review meaning:

This date confirms the second March cluster and adds telecom / baseband context.

#### 2026-05-05

Observed structure:

- MDMStatus:false
- managedappdistributiond crash cluster
- ScreenTimeAgent crash cluster
- CommCenter / Baseband / TelephonyBaseband context

Review meaning:

This date shows the pattern continuing into May.

The same-time managedappdistributiond and ScreenTimeAgent crash cluster is important.

#### 2026-05-21

Observed structure:

- MDMStatus:false
- CommCenter crash
- ScreenTimeAgent crashes
- JetsamEvent containing managedappdistributiond / dmd / ScreenTime / ManagedSettings / SFA / CommCenter
- SFA / CKKS / CloudServices in repeated same-day windows

Review meaning:

This date is the strongest telecom / restriction crash anchor.

It connects management-adjacent, restriction-related, telecom, and account-cloud components in the same broader artifact window.

## mini1

### Device context

Internal label: **mini1**

Physical class: **iPhone 12 mini class device**

Observed model identifier: **iPhone13,1**

Observed OS generation: **iPhone OS 18.5 / 22F76**

### Reviewed mini1 date

- 2026-04-03

### mini1 pattern summary

The mini1 line shows:

- MDMStatus:false
- managedappdistributiond crashes
- ScreenTimeAgent crash
- Analytics with CommCenter / Baseband / SFA context
- stacks containing dmd / ScreenTime / ManagedSettings / CommCenter / Baseband
- SFA / CKKS / CloudServices later the same day

### mini1 anchor details

#### 2026-04-03 07:15

Observed structure:

- Analytics contains MDMStatus:false
- CommCenter / Baseband / SFA context

#### 2026-04-03 07:16

Observed structure:

- managedappdistributiond crashes
- ScreenTimeAgent crashes

#### 2026-04-03 07:56

Observed structure:

- stacks contains dmd / ScreenTime / ManagedSettings / CommCenter / Baseband

#### 2026-04-03 14:27

Observed structure:

- stacks again contains management / restriction / telecom context

#### 2026-04-03 22:14

Observed structure:

- SFA / CKKS / CloudServices family appears

## Cross-device significance

The mini1 2026-04-03 anchor is important because it shows that the pattern is not limited to 15G.

The structure appears across more than one device:

15G:

- repeated March and May anchor dates

mini1:

- April cross-device anchor

This does not prove malicious activity.

However, it weakens a simple single-device-only explanation.

## Pattern comparison

### 15G

15G shows:

- repeated long-range recurrence
- March clusters
- May follow-up anchors
- stronger telecom / CommCenter anchor on 2026-05-21

### mini1

mini1 shows:

- single strong cross-device anchor
- MDMStatus:false
- managedappdistributiond
- ScreenTimeAgent
- dmd / ScreenTime / ManagedSettings stack context
- CommCenter / Baseband context
- SFA / CKKS / CloudServices later the same day

## Review question

Can the same broad structure appearing on both 15G and mini1 be explained by normal iOS behavior, shared iOS build behavior, shared Apple ID lineage, common user behavior, or benign diagnostics?

Or does the cross-device recurrence justify deeper mobile forensic review?

## Boundary

This document does not establish:

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

## Evidence boundary

The raw log archives referenced by this device matrix are preserved separately.

They are not included in this public repository.

They can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.
