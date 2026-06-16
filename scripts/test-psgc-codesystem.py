#!/usr/bin/env python3
"""
Test that the PSGC CodeSystem was correctly created on tx.fhirlab.net.

Verifies all metadata changes from Issue #23 and spot-checks code content.
Exits 0 on success, 1 on any failure.
"""

import json
import sys
import urllib.request

FHIR_BASE = "https://tx.fhirlab.net/fhir"
CS_ID = "PSGC"
VS_ID = "PSGC"


def fetch(url):
    req = urllib.request.Request(url, headers={"Accept": "application/fhir+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def check(label, actual, expected):
    if actual == expected:
        print(f"  PASS  {label}: {actual!r}")
        return True
    else:
        print(f"  FAIL  {label}: expected {expected!r}, got {actual!r}", file=sys.stderr)
        return False


def run_tests():
    failures = 0

    # ── CodeSystem ──────────────────────────────────────────────────────────
    # _elements fetches specific fields without pulling all 43 770 inline concepts
    _elements = "id,url,name,title,version,status,publisher,description,valueSet,count,hierarchyMeaning,content"
    print(f"GET {FHIR_BASE}/CodeSystem/{CS_ID}?_elements=...")
    cs = fetch(f"{FHIR_BASE}/CodeSystem/{CS_ID}?_elements={_elements}")

    tests = [
        ("id",          cs.get("id"),          "PSGC"),
        ("url",         cs.get("url"),          "https://fhir.doh.gov.ph/phcore/CodeSystem/PSGC"),
        ("name",        cs.get("name"),         "PSGC"),
        ("title",       cs.get("title"),        "PSGC"),
        ("version",     cs.get("version"),      "0.1.0"),
        ("status",      cs.get("status"),       "active"),
        ("publisher",   cs.get("publisher"),    "UP Manila - National Institutes of Health - National Telehealth Center"),
        ("description", cs.get("description"), "Philippine Standard Geographic Code"),
        ("valueSet",    cs.get("valueSet"),     "https://fhir.doh.gov.ph/phcore/ValueSet/PSGC"),
        ("count",       cs.get("count"),        43770),
        ("hierarchyMeaning", cs.get("hierarchyMeaning"), "part-of"),
        ("content",     cs.get("content"),      "complete"),
    ]

    for label, actual, expected in tests:
        if not check(label, actual, expected):
            failures += 1

    # ── Spot-check: $lookup on a known PSGC code ────────────────────────────
    print(f"\nGET {FHIR_BASE}/CodeSystem/$lookup (code=1300000000, NCR)")
    lookup_url = (
        f"{FHIR_BASE}/CodeSystem/$lookup"
        f"?system=https://fhir.doh.gov.ph/phcore/CodeSystem/PSGC"
        f"&code=1300000000"
    )
    lookup = fetch(lookup_url)
    display = next(
        (p["valueString"] for p in lookup.get("parameter", []) if p.get("name") == "display"),
        None,
    )
    if not check("$lookup display for 1300000000", display, "National Capital Region (NCR)"):
        failures += 1

    # ── Spot-check: $validate-code ───────────────────────────────────────────
    print(f"\nGET {FHIR_BASE}/CodeSystem/$validate-code (code=1380100000, City of Caloocan)")
    validate_url = (
        f"{FHIR_BASE}/CodeSystem/$validate-code"
        f"?url=https://fhir.doh.gov.ph/phcore/CodeSystem/PSGC"
        f"&code=1380100000"
    )
    validate = fetch(validate_url)
    result_param = next(
        (p["valueBoolean"] for p in validate.get("parameter", []) if p.get("name") == "result"),
        None,
    )
    if not check("$validate-code result for 1380100000", result_param, True):
        failures += 1

    # ── Summary ─────────────────────────────────────────────────────────────
    print()
    if failures == 0:
        print(f"All tests passed.")
    else:
        print(f"{failures} test(s) FAILED.", file=sys.stderr)

    return failures


if __name__ == "__main__":
    sys.exit(run_tests())
