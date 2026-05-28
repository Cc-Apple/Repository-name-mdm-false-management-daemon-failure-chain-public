# Email Note to Forensic Reviewer

## Purpose

This note is intended to help introduce the public repository to a qualified DFIR / mobile forensic reviewer.

This is a suggested message only.

## Suggested message

Dear Reviewer,

I have prepared a public GitHub repository documenting a repeated cross-device iOS artifact pattern involving `MDMStatus:false` and management-adjacent daemon failures across the devices internally labeled 15G and mini1.

The repository does not claim malware, MDM enrollment, attribution, C2, payload, exploit chain, attacker identity, or criminal activity.

The key observation is not that `MDM=true` appears.

The key observation is that `MDMStatus:false` repeatedly appears on days where management-adjacent daemons and restriction-related services fail, crash, or cluster together.

Relevant components include:

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

The reviewed anchor dates are:

- 2026-03-16 / 15G
- 2026-03-17 / 15G
- 2026-03-18 / 15G
- 2026-03-23 / 15G
- 2026-03-24 / 15G
- 2026-04-03 / mini1
- 2026-05-05 / 15G
- 2026-05-21 / 15G

The public repository includes:

- README
- technical summaries
- timeline
- device matrix
- machine-readable summary
- SHA256 reference index
- artifact index
- forensic review questions
- raw artifact handling notes
- reproducibility analysis script

Raw iOS logs, raw ZIP archives, debug archives, sysdiagnose archives, Manifest.db files, full backups, BSSID values, Apple ID values, banking records, OTP records, and private screenshots are not included in the public repository.

The original raw artifacts are preserved separately and can be provided later through a secure upload method, NDA, evidence-handling procedure, or another method preferred by your team.

The main question for review is:

Can repeated `MDMStatus:false` observations normally coexist with repeated management-adjacent daemon failures across more than one device, or does this structure justify deeper mobile forensic review?

Best regards,

YT
