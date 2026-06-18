# **TRACK 1 - PH eReferral**
## ***1. Initiating Facility — new patient, create record***
  - Search for existing patient record (GET) → 200 OK – empty result (no match = new patient)
  - Since no record exists, create patient record – demographics (POST) → 201 Created
  - Update patient record – clinical data (PUT) → 200 OK
## ***2. Receiving Facility — record already exists, update it***
  - Search and retrieve patient record (GET) → 200 OK – returns existing record (created by Initiating Facility)
  - Update patient record – clinical data (PUT) → 200 OK
## ***3. LGU Dashboard (PHO Only) — read-only reporting***
  - Search patients seen by facility based on Referral Category and Reason for Referral (GET) → 200 OK – returns list
  - Generate report based on Referral Category and Reason for Referral (GET) → 200 OK – returns report
