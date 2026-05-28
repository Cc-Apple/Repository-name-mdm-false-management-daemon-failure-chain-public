# External Debug / Sysdiagnose Storage

## Purpose

This document explains why large debug and sysdiagnose archives are not stored directly in this public GitHub repository.

This repository contains only public summaries, indexes, scripts, referenced artifact titles, SHA256 references, and review guidance.

Large debug archives, sysdiagnose archives, full diagnostic archives, and other sensitive raw evidence are preserved separately.

## Public repository boundary

This public repository does not include:

* raw iOS logs
* raw log ZIP archives
* raw sysdiagnose archives
* large debug archives
* full diagnostic archives
* Manifest.db files
* iMazing backup folders
* Apple ID values
* account traces
* device identifiers
* BSSID / Wi-Fi identifiers
* banking records
* OTP records
* private screenshots
* third-party identifiers

## Reason for external storage

Large debug and sysdiagnose archives may contain highly sensitive information, including:

* device identifiers
* Apple account traces
* installed app state
* network metadata
* Wi-Fi / Bluetooth context
* carrier / telecom context
* location-adjacent metadata
* timestamps
* local paths
* diagnostic databases
* usage and process history
* third-party identifiers

They may also be too large for normal GitHub handling.

For these reasons, large debug and sysdiagnose files are intentionally excluded from this public repository.

## Storage model

The full debug / sysdiagnose archive set is preserved separately.

Possible storage methods include:

* offline evidence storage
* restricted cloud storage
* forensic provider secure upload portal
* encrypted archive transfer
* controlled physical transfer if device-level review is required

Public GitHub is used only for the summary package, not for raw evidence distribution.

## Access policy

Access to externally stored raw evidence should be granted only to:

* qualified DFIR reviewers
* mobile forensic specialists
* legal-technical reviewers
* forensic provider staff assigned to the review
* other explicitly approved qualified reviewers

Do not share raw evidence through anonymous public links.

Do not make external debug or sysdiagnose folders public.

## Verification

Files stored externally should be verified using SHA256 hashes where available.

The public repository keeps hash and artifact indexes under:

* evidence_index/sha256_index.txt
* evidence_index/artifact_index.md

If a reviewer receives an external debug, sysdiagnose, or raw log file, they should calculate SHA256 and compare it against the recorded index before relying on the artifact.

## Relationship to this GitHub repository

This public GitHub repository contains:

* README
* technical summaries
* timeline
* device matrix
* machine-readable summary
* SHA256 reference index
* artifact index
* forensic review questions
* raw artifact handling policy
* reproducibility analysis script

Externally preserved evidence may include:

* large debug archives
* sysdiagnose archives
* full diagnostic archives
* raw iOS log ZIP archives
* large raw evidence packages
* files too sensitive or too large for public GitHub

## Preferred forensic transfer

If a forensic provider offers a secure upload portal, encrypted evidence submission method, or formal chain-of-custody process, that method should be preferred.

Restricted external storage is a temporary evidence-preservation method, not a public evidence release.

## Boundary

External storage of debug / sysdiagnose archives does not establish:

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

This document only explains why sensitive raw evidence is not stored directly in the public repository.
