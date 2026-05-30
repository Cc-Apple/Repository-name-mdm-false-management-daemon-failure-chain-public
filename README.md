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

---

## Shadow Cloud Hypothesis Mapping

This repository is a focused technical anchor for the MDMStatus:false / management-adjacent daemon failure chain.

It should be read as a supporting package for the main Shadow Cloud working model, not as a standalone attribution claim.

This anchor is most relevant to three reviewer-facing hypotheses:

1. **Policy-as-Persistence**
2. **Deniability-first Design**
3. **Evidence-Suppression Objective**

These hypotheses are not conclusions.

They are validation targets for qualified DFIR, CTI, mobile forensic, platform-security, or OS-security review.

---

## 1. Policy-as-Persistence

### Relevance to this anchor

This repository focuses on repeated management-adjacent daemon activity and failure chains while visible management indicators remain false or absent.

The main question is whether policy state, restriction state, ScreenTime state, ManagedSettings behavior, or management-adjacent daemon activity could act as a persistence surface without visible classic MDM enrollment.

This does not require a classic malware payload to be visible.

### Reviewer question

> Is policy state acting as persistence while visible MDM / supervised indicators remain false?

### Relevant signal categories

* MDMStatus:false
* supervised:false
* userIsManaged:false
* managedappdistributiond
* dmd
* RemoteManagementAgent
* ScreenTimeAgent
* ManagedSettings
* FamilyControls
* restriction-like behavior
* repeated management-adjacent daemon failures

### What would support this hypothesis

* repeated management-adjacent daemon activity while MDMStatus remains false
* restriction-like behavior without visible enrollment or supervision
* recurrence across multiple devices or dates
* correlation between daemon failure chains and user-visible restriction symptoms
* mismatch between visible management state and effective policy behavior

### What would weaken it

* all daemon activity fully explained by normal Apple / iOS background behavior
* no restriction-like effect associated with the daemon activity
* same daemon failure chain reproduced on clean control devices
* vendor-confirmed benign explanation for the full pattern

---

## 2. Deniability-first Design

### Relevance to this anchor

The MDMStatus:false condition may make the activity appear non-actionable or benign during ordinary review.

If management-adjacent daemons fail or repeat while visible MDM indicators remain false, the pattern can be dismissed as iOS noise, ordinary daemon failure, configuration residue, or tool interpretation error.

This anchor asks whether that false-negative surface is itself meaningful.

### Reviewer question

> Are individually benign-looking daemon failures masking a cross-layer management or restriction pattern?

### Relevant signal categories

* normal-looking daemon failures
* repeated management-adjacent errors
* MDM false state
* restriction-layer signals
* resource-pressure logs
* backup / evidence-preservation anomalies
* cross-device recurrence
* timing correlation with important user events

### What would support this hypothesis

* daemon failures cluster around restriction, backup, or evidence-relevant events
* multiple benign-looking symptoms align across time and device
* the same MDM false / daemon failure pattern repeats on affected devices
* comparison devices do not show the same clustered pattern
* failures appear individually harmless but become meaningful when aligned

### What would weaken it

* ordinary Apple behavior explains the full daemon pattern
* no timing relationship to restriction, backup, or evidence-relevant events
* clean control devices show the same pattern under similar conditions
* all failures are isolated and non-recurring

---

## 3. Evidence-Suppression Objective

### Relevance to this anchor

Management-adjacent daemon failures may be relevant if they correlate with the user’s inability to preserve, export, explain, or validate evidence.

This does not prove malicious suppression.

It defines a review question: whether evidence-preservation behavior remained normal during MDM false / management-daemon failure windows.

### Reviewer question

> Did evidence preservation behave normally during management-adjacent daemon failure windows?

### Relevant signal categories

* backup inconsistency
* Manifest / RTCR abnormality
* log preservation degradation
* storage pressure
* screenshot or screen-recording difficulty
* artifact export difficulty
* repeated daemon activity near evidence-relevant events
* mismatch between successful user action and abnormal backend artifacts

### What would support this hypothesis

* preservation failures repeat during high-value event windows
* evidence actions correlate with daemon, resource-pressure, backup, or restriction anomalies
* affected devices show degradation while comparison devices preserve normally
* failure modes align with MDM false / management-daemon failure chains
* backup or Manifest anomalies appear near the same windows

### What would weaken it

* preservation failures fully explained by storage exhaustion, user error, tool limitations, or ordinary iOS behavior
* no timing relationship to management-adjacent daemon activity
* same preservation failures reproduce on clean devices
* no relationship between daemon failure chains and evidence degradation

---

## Boundary

This repository does not assert:

* malware attribution
* actor attribution
* state attribution
* Apple-side causation
* classic MDM enrollment
* known spyware family deployment
* confirmed C2
* confirmed payload
* confirmed exploit chain
* Evil Twin / rogue AP use as a proven fact

This anchor only asks whether MDMStatus:false combined with repeated management-adjacent daemon failures should be treated as a meaningful control-layer signal for deeper review.

The preferred outcome is not confirmation.

The preferred outcome is a reproducible explanation that supports, weakens, or falsifies each hypothesis.

