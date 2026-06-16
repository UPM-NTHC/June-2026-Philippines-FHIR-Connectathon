#!/usr/bin/env python3
"""
Create a new PSGC CodeSystem on the FHIRLab Terminology Server.

Fetches the existing PSGC resource (id: ba9149a0-2f5d-4604-8490-8535ce7bd5b7),
updates its metadata per Issue #23, removes the old server identity, and PUTs
it to tx.fhirlab.net as /CodeSystem/PSGC.

Usage:
    python3 scripts/create-psgc-codesystem.py [--dry-run]

Options:
    --dry-run   Transform and save locally, skip the PUT to the server.
"""

import json
import sys
import urllib.request

SOURCE_URL = "https://tx.fhirlab.net/fhir/CodeSystem/ba9149a0-2f5d-4604-8490-8535ce7bd5b7"
TARGET_URL = "https://tx.fhirlab.net/fhir/CodeSystem/PSGC"
OUTPUT_PATH = "terminology/CodeSystem-PSGC.json"

NEW_METADATA = {
    "id": "PSGC",
    "url": "https://fhir.doh.gov.ph/phcore/CodeSystem/PSGC",
    "name": "PSGC",
    "title": "PSGC",
    "version": "0.1.0",
    "status": "active",
    "publisher": "UP Manila - National Institutes of Health - National Telehealth Center",
    "description": "Philippine Standard Geographic Code",
    "valueSet": "https://fhir.doh.gov.ph/phcore/ValueSet/PSGC",
}


def fetch(url):
    print(f"Fetching {url} ...")
    req = urllib.request.Request(url, headers={"Accept": "application/fhir+json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    print(f"  id={data.get('id')}  url={data.get('url')}  count={data.get('count')}")
    return data


def transform(cs):
    # Drop server-assigned identity so the PUT creates/replaces cleanly
    cs.pop("meta", None)
    # Drop old contact (admin@upmsilab.org is not the new publisher)
    cs.pop("contact", None)
    # Apply new metadata (overwrites matching keys, adds missing ones)
    cs.update(NEW_METADATA)
    return cs


def put(cs, url):
    print(f"PUTing to {url} ...")
    body = json.dumps(cs).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="PUT",
        headers={
            "Content-Type": "application/fhir+json",
            "Accept": "application/fhir+json",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        status = resp.status
        result = json.loads(resp.read())
    print(f"  HTTP {status}  id={result.get('id')}  url={result.get('url')}")
    return status, result


def main():
    dry_run = "--dry-run" in sys.argv

    cs = fetch(SOURCE_URL)
    cs = transform(cs)
    print(f"Transformed: id={cs['id']}  url={cs['url']}  status={cs['status']}")

    with open(OUTPUT_PATH, "w") as f:
        json.dump(cs, f, indent=2)
    print(f"Saved to {OUTPUT_PATH}")

    if dry_run:
        print("Dry run — skipping PUT.")
        return 0

    status, _ = put(cs, TARGET_URL)
    if status not in (200, 201):
        print(f"ERROR: unexpected HTTP status {status}", file=sys.stderr)
        return 1

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
