# Raw Artifact Handling Policy

## Purpose

This document defines how raw logs, debug archives, sysdiagnose files, and other sensitive artifacts should be handled for the MDM-false management daemon failure chain review.

This public repository does **not** contain raw evidence.

It contains only public summaries, indexes, SHA256 references, referenced log titles, review questions, and analysis scripts.

## Public repository boundary

Raw artifacts are not included in this public repository.

The following are excluded:

* raw iOS logs
* raw log ZIP archives
* raw sysdiagnose archives
* large debug archives
* Manifest.db files
* iMazing backup folders
* Apple ID values
* account traces
* device identifiers
* BSSID / Wi-Fi identifiers
* banking records
* OTP records
* private screenshots
* friend or third-party identifiers
* full physical-location records

## Safe to keep in this public repository

The following are suitable for public preliminary review:

* README.md
* technical summaries
* timeline
* device matrix
* machine-readable summary
* SHA256 references
* artifact indexes
* referenced log titles
* forensic review questions
* reviewer quick-start notes
* non-attribution statement
* extraction / analysis scripts
* raw artifact handling notes

## Referenced raw artifacts for this case

The MDM-false management daemon failure chain is associated with selected preserved raw iOS log ZIP archives.

These files are **not included** in this public repository.

### Referenced 15G raw log archives

* 2026-03-16.zip
* 2026-03-17.zip
* 2026-03-18.zip
* 2026-03-23.zip
* 2026-03-24.zip
* 2026-05-05.zip
* 2026-05-21.zip

### Referenced mini1 raw log archive

* mini1-2026-04-03.zip

## Large debug / sysdiagnose handling

Large debug and sysdiagnose archives are not stored directly in this public GitHub repository.

Reason:

* they may contain sensitive device, account, network, app, and location-related data
* they may contain diagnostic databases and process history
* they may be too large for normal GitHub handling
* forensic reviewers may prefer a controlled evidence-transfer process

Large debug and sysdiagnose files are preserved separately and can be provided later if required by a qualified reviewer.

## SHA256 handling

Raw artifacts should be identified by SHA256.

The SHA256 index for this case is stored at:

* evidence_index/sha256_index.txt

A reviewer should verify SHA256 before relying on any raw artifact provided later.

## Recommended transfer process

If a qualified forensic reviewer requests raw artifacts, the transfer method should be agreed first.

Preferred options:

* secure upload portal provided by the reviewer
* encrypted archive with password shared through a separate channel
* NDA / evidence-handling agreement
* formal chain-of-custody process
* controlled physical review if device-level examination is required

Avoid casual public sharing of raw iOS logs, raw sysdiagnose archives, debug archives, or backup artifacts.

## External storage note

Large raw diagnostic archives may be stored offline, in restricted storage, or transferred through a forensic provider’s secure upload process.

Public GitHub is used only for the summary package, not for raw evidence distribution.

## Boundary

Raw artifacts are preserved for technical validation.

They do not by themselves establish:

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

This handling policy exists to preserve reviewability while avoiding unnecessary public exposure of sensitive raw evidence.
