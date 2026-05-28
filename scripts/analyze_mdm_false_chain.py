import argparse
import hashlib
import json
import os
import re
import zipfile
from pathlib import Path


EXPECTED_FILES = [
    {
        "device": "15G",
        "date": "2026-03-16",
        "path": "logs/15G/2026-03-16.zip",
        "sha256": "b632d8f855f0f9690f5adb606ed419a30dab0aaec4d6c8f8b21fbf2df3ae104d",
        "role": "cluster_1_start",
    },
    {
        "device": "15G",
        "date": "2026-03-17",
        "path": "logs/15G/2026-03-17.zip",
        "sha256": "74310591fe05bb35350e88d52a84168192349a71c5fbc8ea95ec363f4d26e695",
        "role": "cluster_1_confirmation",
    },
    {
        "device": "15G",
        "date": "2026-03-18",
        "path": "logs/15G/2026-03-18.zip",
        "sha256": "568866ea64f2775cad82fa9324ce5e91e7b9bd2e27496edd0f4778847476c211",
        "role": "cluster_1_strongest",
    },
    {
        "device": "15G",
        "date": "2026-03-23",
        "path": "logs/15G/2026-03-23.zip",
        "sha256": "101f2e7f1f4e4488e8fb0c14c6e7f20a0a3b91d3cc599cf89c8ce91016a1fdf2",
        "role": "cluster_2_start",
    },
    {
        "device": "15G",
        "date": "2026-03-24",
        "path": "logs/15G/2026-03-24.zip",
        "sha256": "c16e40bcc00c8769bc8d35036ac163a6572c0b34c85a0264301782010ac32ee7",
        "role": "cluster_2_confirmation",
    },
    {
        "device": "mini1",
        "date": "2026-04-03",
        "path": "logs/mini1/mini1-2026-04-03.zip",
        "sha256": "fdb016ed7a74ef2e7a7ddf86fd6d2b74f353025636d1c0ad9675864f75cc51a4",
        "role": "cross_device_anchor",
    },
    {
        "device": "15G",
        "date": "2026-05-05",
        "path": "logs/15G/2026-05-05.zip",
        "sha256": "abc6d099414b517fb966d12d4ff571d58c494e36a4cdb624184940e59c97bbd2",
        "role": "follow_up_anchor",
    },
    {
        "device": "15G",
        "date": "2026-05-21",
        "path": "logs/15G/2026-05-21.zip",
        "sha256": "b6a081fd8ce18dcd25006b2ce084849f55494335e646e23f6eacb5f4e13536be",
        "role": "telecom_restriction_crash_anchor",
    },
]


TERMS = {
    "mdm_negative_status": [
        '"mdmstatus":false',
        "mdmstatus:false",
        "mdmstatus = false",
        "mdmenrollmentstatus_powerlog",
        "powerlogmdmenrollmentstatus",
    ],
    "mdm_general": [
        "mdm",
        "mdmstatus",
        "mdmenrollment",
        "manageddevice",
        "managed device",
        "device management",
    ],
    "management_adjacent": [
        "managedappdistributiond",
        "dmd",
        "remotemanagement",
    ],
    "restriction_related": [
        "screentimeagent",
        "screentime",
        "managedsettings",
        "familycontrols",
        "restrictions",
    ],
    "telecom_baseband": [
        "commcenter",
        "baseband",
        "telephonybaseband",
        "basebandpowercycle",
        "cellularmcc",
        "cellularmnc",
        "carrier",
        "plmn",
        "mcc",
        "mnc",
        "mobifone",
    ],
    "account_cloud": [
        "sfa",
        "ckks",
        "cloudservices",
        "icloud",
        "cloudkit",
        "pcs",
        "sos",
        "authkit",
        "keychain",
        "trust",
        "trusted",
        "transparency",
    ],
    "co_location_artifacts": [
        "forcereset",
        "stacks",
        "jetsamevent",
        "analytics",
    ],
    "failure_markers": [
        "exc_crash",
        "exc_breakpoint",
        "sigabrt",
        "sigtrap",
        "abort trap",
        "cpu_resource",
        "diskwrites_resource",
        "jetsam",
        "0xbaaaaaad",
    ],
}


IMPORTANT_NAME_PATTERNS = [
    "analytics",
    "managedappdistributiond",
    "dmd-",
    "screentimeagent",
    "forcereset",
    "stacks",
    "jetsamevent",
    "sfa-",
    "commcenter",
    "baseband",
    "preferences",
    "contactsd",
    "facetime",
    "maild",
    "searchd",
    "deleted",
    "duetexpertd",
    "triald",
    "backgroundshortcut",
]


META_KEYS = [
    "bug_type",
    "timestamp",
    "procName",
    "bundleID",
    "coalitionName",
    "procLaunch",
    "captureTime",
    "os_version",
    "incident",
    "modelCode",
    "exception",
    "termination",
    "procRole",
    "is_first_party",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_decode(data: bytes) -> str:
    return data.decode("utf-8", "replace")


def extract_meta(text: str) -> dict:
    out = {}
    head = text[:100000]

    for key in META_KEYS:
        m = re.search(
            r'"%s"\s*:\s*(".*?"|[\d\.\-]+|true|false|null)' % re.escape(key),
            head,
            re.I,
        )
        if m:
            out[key] = m.group(1).strip('"')

    return out


def count_terms(text: str) -> dict:
    low = text.lower()
    return {
        group: sum(low.count(term) for term in terms)
        for group, terms in TERMS.items()
    }


def is_important_file(name: str, counts: dict) -> bool:
    lname = name.lower()

    if any(p in lname for p in IMPORTANT_NAME_PATTERNS):
        return True

    if counts.get("mdm_negative_status", 0) > 0:
        return True

    if counts.get("management_adjacent", 0) > 0:
        return True

    if counts.get("restriction_related", 0) > 0:
        return True

    if counts.get("telecom_baseband", 0) > 3:
        return True

    if counts.get("account_cloud", 0) > 3:
        return True

    return False


def compact_hits(text: str) -> dict:
    low = text.lower()
    return {
        "MDMStatus_false": (
            low.count('"mdmstatus":false')
            + low.count("mdmstatus:false")
            + low.count("mdmstatus = false")
        ),
        "MDMEnrollmentStatus_Powerlog": low.count("mdmenrollmentstatus_powerlog"),
        "PowerlogMDMEnrollmentStatus": low.count("powerlogmdmenrollmentstatus"),
        "managedappdistributiond": low.count("managedappdistributiond"),
        "dmd": low.count("dmd"),
        "ScreenTimeAgent": low.count("screentimeagent"),
        "ScreenTime": low.count("screentime"),
        "ManagedSettings": low.count("managedsettings"),
        "CommCenter": low.count("commcenter"),
        "Baseband": low.count("baseband"),
        "TelephonyBaseband": low.count("telephonybaseband"),
        "BasebandPowerCycle": low.count("basebandpowercycle"),
        "SFA": low.count("sfa"),
        "CKKS": low.count("ckks"),
        "CloudServices": low.count("cloudservices"),
        "forceReset": low.count("forcereset"),
        "stacks": low.count("stacks"),
        "JetsamEvent": low.count("jetsamevent"),
        "EXC_CRASH": low.count("exc_crash"),
        "EXC_BREAKPOINT": low.count("exc_breakpoint"),
        "SIGABRT": low.count("sigabrt"),
        "SIGTRAP": low.count("sigtrap"),
        "bad_stackshot": low.count("0xbaaaaaad"),
    }


def scan_zip(zip_path: Path, expected: dict) -> dict:
    actual_sha = sha256_file(zip_path)

    result = {
        "device": expected["device"],
        "date": expected["date"],
        "role": expected["role"],
        "path": expected["path"],
        "expected_sha256": expected["sha256"],
        "actual_sha256": actual_sha,
        "sha256_match": actual_sha == expected["sha256"],
        "entries_total": 0,
        "important_entries": [],
        "aggregate_counts": {k: 0 for k in TERMS},
        "aggregate_compact_hits": {},
        "observed_flags": {
            "MDMStatus_false_seen": False,
            "managedappdistributiond_seen": False,
            "dmd_seen": False,
            "ScreenTimeAgent_seen": False,
            "ManagedSettings_seen": False,
            "CommCenter_seen": False,
            "Baseband_seen": False,
            "TelephonyBaseband_seen": False,
            "SFA_or_CKKS_or_CloudServices_seen": False,
            "forceReset_seen": False,
            "stacks_seen": False,
            "JetsamEvent_seen": False,
        },
    }

    compact_total = {}

    with zipfile.ZipFile(zip_path) as z:
        entries = [i for i in z.infolist() if not i.is_dir()]
        result["entries_total"] = len(entries)

        for info in entries:
            data = z.read(info.filename)
            text = safe_decode(data)
            counts = count_terms(text)
            hits = compact_hits(text)

            for k, v in counts.items():
                result["aggregate_counts"][k] += v

            for k, v in hits.items():
                compact_total[k] = compact_total.get(k, 0) + v

            if hits["MDMStatus_false"] > 0:
                result["observed_flags"]["MDMStatus_false_seen"] = True
            if hits["managedappdistributiond"] > 0:
                result["observed_flags"]["managedappdistributiond_seen"] = True
            if hits["dmd"] > 0:
                result["observed_flags"]["dmd_seen"] = True
            if hits["ScreenTimeAgent"] > 0:
                result["observed_flags"]["ScreenTimeAgent_seen"] = True
            if hits["ManagedSettings"] > 0:
                result["observed_flags"]["ManagedSettings_seen"] = True
            if hits["CommCenter"] > 0:
                result["observed_flags"]["CommCenter_seen"] = True
            if hits["Baseband"] > 0:
                result["observed_flags"]["Baseband_seen"] = True
            if hits["TelephonyBaseband"] > 0:
                result["observed_flags"]["TelephonyBaseband_seen"] = True
            if hits["SFA"] > 0 or hits["CKKS"] > 0 or hits["CloudServices"] > 0:
                result["observed_flags"]["SFA_or_CKKS_or_CloudServices_seen"] = True

            lname = info.filename.lower()
            if "forcereset" in lname:
                result["observed_flags"]["forceReset_seen"] = True
            if "stacks" in lname:
                result["observed_flags"]["stacks_seen"] = True
            if "jetsamevent" in lname:
                result["observed_flags"]["JetsamEvent_seen"] = True

            if not is_important_file(info.filename, counts):
                continue

            result["important_entries"].append({
                "path": info.filename,
                "size": len(data),
                "sha256": sha256_bytes(data),
                "meta": extract_meta(text),
                "term_counts": {k: v for k, v in counts.items() if v > 0},
                "compact_hits": {k: v for k, v in hits.items() if v > 0},
            })

    result["aggregate_compact_hits"] = {
        k: v for k, v in sorted(compact_total.items()) if v > 0
    }

    return result


def summarize_case(results: list) -> dict:
    by_device = {}
    dates_with_mdm_false = []
    dates_with_management = []
    dates_with_restriction = []
    dates_with_telecom = []
    dates_with_account_cloud = []
    dates_with_colocation = []

    for r in results:
        device = r.get("device", "unknown")
        by_device.setdefault(device, 0)
        by_device[device] += 1

        flags = r.get("observed_flags", {})
        label = f"{r.get('date')} / {device}"

        if flags.get("MDMStatus_false_seen"):
            dates_with_mdm_false.append(label)

        if flags.get("managedappdistributiond_seen") or flags.get("dmd_seen"):
            dates_with_management.append(label)

        if flags.get("ScreenTimeAgent_seen") or flags.get("ManagedSettings_seen"):
            dates_with_restriction.append(label)

        if (
            flags.get("CommCenter_seen")
            or flags.get("Baseband_seen")
            or flags.get("TelephonyBaseband_seen")
        ):
            dates_with_telecom.append(label)

        if flags.get("SFA_or_CKKS_or_CloudServices_seen"):
            dates_with_account_cloud.append(label)

        if (
            flags.get("forceReset_seen")
            or flags.get("stacks_seen")
            or flags.get("JetsamEvent_seen")
        ):
            dates_with_colocation.append(label)

    return {
        "devices_seen": by_device,
        "dates_with_MDMStatus_false": dates_with_mdm_false,
        "dates_with_management_adjacent": dates_with_management,
        "dates_with_restriction_related": dates_with_restriction,
        "dates_with_telecom_baseband": dates_with_telecom,
        "dates_with_account_cloud": dates_with_account_cloud,
        "dates_with_forceReset_stacks_or_JetsamEvent": dates_with_colocation,
        "core_interpretation": (
            "The key observation is not MDM=true. "
            "The key observation is repeated MDMStatus:false co-occurring with "
            "management-adjacent, restriction-related, telecom/baseband, account-cloud, "
            "and co-location artifacts across dates and devices."
        ),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze MDM-false management daemon failure chain artifacts."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root directory. Default: current directory.",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Optional JSON output path. If omitted, prints to stdout.",
    )
    args = parser.parse_args()

    root = Path(args.root)
    results = []
    missing = []

    for expected in EXPECTED_FILES:
        p = root / expected["path"]

        if not p.exists():
            missing.append({
                "device": expected["device"],
                "date": expected["date"],
                "path": expected["path"],
                "expected_sha256": expected["sha256"],
                "status": "missing",
            })
            continue

        results.append(scan_zip(p, expected))

    output = {
        "case": "MDM-False Management Daemon Failure Chain",
        "purpose": "Read-only reproducibility scan for selected iOS log ZIP artifacts.",
        "safety": "This script reads ZIP files only. It does not modify raw artifacts.",
        "expected_files": EXPECTED_FILES,
        "missing_files": missing,
        "summary": summarize_case(results),
        "results": results,
    }

    js = json.dumps(output, ensure_ascii=False, indent=2)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(js, encoding="utf-8")
        print(f"Wrote: {out_path}")
    else:
        print(js)


if __name__ == "__main__":
    main()
