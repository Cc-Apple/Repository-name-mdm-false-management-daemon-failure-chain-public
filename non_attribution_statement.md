# Non-Attribution Statement

## Purpose

This repository does not claim that any specific actor, APT group, state, company, government, organization, or individual is responsible for the observed artifacts.

This repository documents a repeated technical artifact pattern for qualified DFIR / mobile forensic review.

The purpose is technical review, not attribution.

## What is claimed

The current claim is limited to the following:

- A repeated artifact pattern exists across more than one device.
- The pattern includes MDMStatus:false and same-day or near-same-day management-adjacent daemon failures or clustering.
- The pattern appears across the devices internally labeled 15G and mini1.
- The pattern is technically meaningful enough to preserve and submit for qualified forensic review.

## What is not claimed

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

## Important distinction

This repository does not claim:

- MDM=true

The observed pattern is different:

- MDMStatus:false appears repeatedly on days where management-adjacent daemons and restriction-related services fail or cluster together.

Observed components include:

- managedappdistributiond
- dmd
- ScreenTimeAgent
- ManagedSettings
- CommCenter
- Baseband
- TelephonyBaseband
- SFA / CKKS / CloudServices
- forceReset
- stacks
- JetsamEvent

## Technical review boundary

The key review question is not:

Who did this?

The key review question is:

Can repeated MDMStatus:false observations normally coexist with repeated management-adjacent daemon failures across more than one device, or does the structure justify deeper mobile forensic review?

## Normal explanation remains possible

This repository does not exclude benign explanations.

Possible benign explanations may include:

- normal iOS diagnostic behavior
- local iOS policy state
- non-malicious daemon instability
- ordinary Screen Time / ManagedSettings behavior
- ordinary account / cloud / keychain diagnostics
- device-specific crash behavior

However, the repeated cross-device structure is preserved because it may be technically meaningful.

## Evidence handling

Raw logs may contain sensitive identifiers, account traces, app activity, network metadata, carrier context, timestamps, and personal usage patterns.

Raw logs are not included in this public repository.

Large debug or sysdiagnose archives are not stored directly in this public repository.

They are preserved separately and can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.

## Boundary

This repository supports technical review only.

It does not assign responsibility.

It does not identify an attacker.

It does not prove compromise by itself.
