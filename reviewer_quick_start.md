# Reviewer Quick Start

## Purpose

This document gives a qualified reviewer the shortest path to understand this public repository.

The repository documents a repeated MDM-false management daemon failure chain across the devices internally labeled **15G** and **mini1**.

Raw iOS logs and raw diagnostic archives are **not included** in this public repository.

## Core point

This repository does not claim that `MDM=true` appears.

The key observation is:

- `MDMStatus:false` repeatedly appears on days where management-adjacent daemons and restriction-related services fail, crash, or cluster together across more than one device.

## Main reviewed dates

- 2026-03-16 / 15G
- 2026-03-17 / 15G
- 2026-03-18 / 15G
- 2026-03-23 / 15G
- 2026-03-24 / 15G
- 2026-04-03 / mini1
- 2026-05-05 / 15G
- 2026-05-21 / 15G

## Highest-priority review dates

Start with these:

- 2026-03-18 / 15G
- 2026-03-23 / 15G
- 2026-03-24 / 15G
- 2026-04-03 / mini1
- 2026-05-05 / 15G
- 2026-05-21 / 15G

Supporting dates:

- 2026-03-16 / 15G
- 2026-03-17 / 15G

## Key artifact families

Review these component families first:

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

## Suggested review order

1. Read `README.md`.
2. Read `docs/timeline.md`.
3. Read `docs/device_matrix.md`.
4. Read `docs/technical_observations.md`.
5. Check `evidence_index/sha256_index.txt`.
6. Check `evidence_index/artifact_index.md`.
7. Review `forensic_review_questions.md`.
8. Review `raw_artifact_handling.md`.
9. Review the analyzer script under `scripts/`.
10. Request raw log archives only if needed for formal review.

## Expected raw log layout

The following raw ZIP files are referenced by this package but are not included in this public repository.

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

## External debug / sysdiagnose

Large debug and sysdiagnose archives are not stored directly in this public GitHub repository.

They are preserved separately and can be provided to qualified forensic reviewers upon request through a secure transfer method.

See:

- `external_debug_storage.md`
- `raw_artifact_handling.md`

## What should be verified first

A reviewer should first verify whether the following repeated structure is normal or abnormal:

- `MDMStatus:false`
- managedappdistributiond / dmd
- ScreenTimeAgent / ManagedSettings
- CommCenter / Baseband / TelephonyBaseband
- SFA / CKKS / CloudServices
- forceReset / stacks / JetsamEvent
- recurrence across 15G and mini1

## Main review question

Can repeated `MDMStatus:false` observations normally coexist with repeated management-adjacent daemon failures across more than one device, or does this structure justify deeper mobile forensic review?

## Boundary

This repository does not establish:

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

This document is only a quick-start guide for technical review.
