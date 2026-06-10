# June 2026 Philippines FHIR® Connectathon – Quezon City, Philippines

<PLACE HOLDER FOR GRAPHIC DESIGN>

The June 2026 Philippines FHIR® Connectathon is co-organized by the National Telehealth Center (NTHC), under the University of the Philippines Manila National Institutes of Health, in partnership with the Department of Health (DOH), Philippine Health Insurance Corporation (PhilHealth), The Strengthening Standards Capability Project (SSCP) of  Commonwealth Scientific and Industrial Research Organisation (CSIRO), Aklan Provincial Health Office, and othterkey stakeholders.

This Connectathon represents a milestone in the Philippines' digital health interoperability journey, bringing together healthcare systems, EMR vendors, and government agencies to advance standardized health data exchange using FHIR® profiles including PH Core, eReferral (PeReF), and Immunization specifications.

The Connectathon aims to foster interoperability across health systems by providing opportunities for healthcare system developers, business owners, vendors, government agencies, hospitals, and EMR providers to participate in critical use-case scenarios, validate emerging FHIR Implementation Guides, and build a community of practice around standards-based digital health.

## Important Information

- <Link to Program of Activities>
- <Link to Logistics Notes>
- [Draft PH Core FHIR Implementation Guide (IG)](https://build.fhir.org/ig/UP-Manila-SILab/ph-core/en/index.html))
- [Draft PH eReferral FHIR Implementation Guide (IG)](https://build.fhir.org/ig/ph-ereferral-organization/ph-ereferral/en/index.html))

## Connectathon Objectives

### Primary Objectives

- **Capacity Building**: Equip IT professionals, decision-makers, and healthcare teams with foundational knowledge of interoperability standards and FHIR implementation best practices
- **Standards Validation**: Test and validate emerging FHIR Implementation Guides (PH Core, eReferral, and Immunization) across real-world health system use cases
- **Interoperability Testing**: Demonstrate data exchange and system interoperability using standardized FHIR profiles across multiple tracks
- **Feedback & Refinement**: Capture technical issues, gaps, and lessons learned to inform the next iteration of FHIR IGs and national interoperability standards
- **Governance & Scale-up**: Engage national agencies, hospitals, LGUs, and EMR vendors in governance discussions to generate policy recommendations for national scale-up

### Secondary Objectives

- Validate terminology mappings and workflow simulations in alignment with WHO SMART Guidelines
- Establish a sustainable community of practice around FHIR standards in the Philippines
- Conduct a formal handover of refined FHIR IGs to the Department of Health for long-term adoption
- Generate evidence and documentation to support the Digital Health Roadmap of the Philippines

## Use Case Summary (Tracks)

| **USE CASE** | **STATION** | **END USER** | **DETAILS** |
|-----------------|-----------------|----------|----------|
| **UC1: Data Submission to Shared Health Record (SHR)** | Point of Service | EMR/Clinic Systems | Users will submit clinical data bundle to SHR. **(POST)** |
| 👉 [Click for track details of Use Case #1](use-case-1.md) | | | |
| **UC2: Data Retrieval from SHR** | Facility | Hospital Systems | Users will retrieve data bundle from SHR. **(GET)** |
| 👉 [Click for track details of Use Case #2](use-case-2.md) | | | |
| **UC3: Terminology Validation** | Development | System Developers | Users will validate terminology codes and mappings. **(GET & POST)** |
| 👉 [Click for track details of Use Case #3](use-case-3.md) | | | |
| **UC4: Profile Conformance Testing** | Testing | QA Teams | Users will test conformance to FHIR profiles. **(POST)** |
| 👉 [Click for track details of Use Case #4](use-case-4.md) | | | |
| **UC5: Cross-System Interoperability** | Integration | System Vendors | Users will exchange data across multiple systems. **(POST & GET)** |
| 👉 [Click for track details of Use Case #5](use-case-5.md) | | | |

## Connectathon Tracks and Sample Data

This Connectathon is organized into multiple tracks, each focusing on specific use cases and FHIR profiles:

### Track Overview

- **Track 1**: PH Core Profile Implementation - Point of Service Data Submission
- **Track 2**: PH Core Profile Implementation - FHIR Search and Retrieval
- **Track 3**: eReferral (PeReF) Profile Implementation - Referral Workflow
- **Track 4**: Immunization Profile Implementation - Vaccine Record Exchange
- **Bonus Tracks**: Advanced interoperability scenarios and cross-profile integration

### Sample Data and Resources

To help participants get started quickly, we have prepared comprehensive resources for each track:

- **Postman Collections**: Ready-to-use API requests for each use case
- **Sample JSON/XML Files**: Example FHIR resources conforming to PH Core, eReferral, and Immunization profiles
- **Validation Scripts**: Scripts for local testing and resource validation
- **Documentation**: Detailed setup guides and troubleshooting resources

👉 [Postman Collection and Environment](./postman/)

👉 [Sample Data and Resources](./sample-data/)

## FHIR Servers Available for Testing During the Connectathon

| Version | Server | Endpoint | Capabilities |
|-------------|---------|-------------|-------------|
| FHIR R4 | FHIRLab (HAPI FHIR) | https://cdr.fhirlab.net/fhir | CRUD, transaction, validation |
| FHIR R4 | Ontoserver Terminology | https://tx.fhirlab.net/fhir | $expand, $validate-code, $lookup |
| FHIR R4 | Ontoserver with Shrimp Viewer | https://ontoserver.csiro.au/shrimp/ | Terminology browsing & visualization |

> **Note**: FHIRLab is an open interoperability sandbox maintained as part of The Strengthening Standards Capability Project (SSCP), co-funded by CSIRO Australia and the Australian Government, Department of Foreign Affairs and Trade. FHIR servers will remain accessible for testing and ongoing learning activities post-Connectathon.

## Connectathon Track Details

### Track 1: Point of Service Data Submission

**Objective**: Demonstrate how a Point of Service (POS) application can submit clinical data to a central health data repository.

**Focus Profiles**: PH Core (Patient, Encounter, Observation, Condition, Medication, Procedure)

👉 [Full Track 1 Details](./track-1/README.md)

### Track 2: FHIR Search and Retrieval

**Objective**: Test RESTful search and retrieval of clinical data submitted by POS applications.

**Focus Profiles**: PH Core (Patient, Encounter, Observation) with search parameters

👉 [Full Track 2 Details](./track-2/README.md)

### Track 3: eReferral Workflow Implementation

**Objective**: Demonstrate referral request creation, transmission, and acceptance workflows using FHIR.

**Focus Profiles**: eReferral (PeReF) - ServiceRequest, Communication, Task

👉 [Full Track 3 Details](./track-3/README.md)

### Track 4: Immunization Record Exchange

**Objective**: Validate immunization data exchange and conformance to Immunization Implementation Guide.

**Focus Profiles**: Immunization, Immunization Recommendation, Patient

👉 [Full Track 4 Details](./track-4/README.md)

## International Semantic and Syntactic Standards

Participants should familiarize themselves with the following foundational standards:

- **[HL7 FHIR](https://www.fhir.org/)** (Fast Healthcare Interoperability Resources)
  - FHIR R4 standard resources and REST API conventions
  - Profile definition and implementation guidance
  - How to submit FHIR resources with Profiles from a FHIR Implementation Guide
  - How to retrieve and expand ValueSets
  
  > Note: FHIR R4 is aligned with national digital health initiatives in the Philippines.

- **[OpenHIE Architecture](https://ohie.org/architecture-specification/)** - Digital health system reference architecture

- **[SNOMED CT](https://www.snomed.org/what-is-snomed-ct)** - Clinical terminology standard

- **[ICD-10](https://icd.who.int/browse10/2019/en)** - International disease classification

- **[LOINC](https://loinc.org/)** - Laboratory and clinical observation codes

- **[WHO SMART Guidelines](https://www.who.int/teams/digital-health-and-innovation/smart-guidelines)** - Standards-based workflow approach

## FHIRLab Tools and Resources

### FHIR Servers and Tooling

- **[FHIR Server (HAPI FHIR Endpoint)](https://cdr.fhirlab.net/fhir)** - Main FHIR server for resource submissions and retrieval
- **[Terminology Server (Ontoserver Endpoint)](https://tx.fhirlab.net/fhir)** - ValueSet and terminology operations
- **[Terminology Browser (Ontoserver + Shrimp)](https://ontoserver.csiro.au/shrimp/)** - Visual terminology browsing and mapping

### Local Testing Tools (Optional)

- **[FHIR CLI](https://hapifhir.io/hapi-fhir/docs/tools/hapi_fhir_cli.html#server-run-server)** - Run a local HAPI FHIR server for testing
- **[FHIR Validator](https://validator.fhirlab.net)** - Online resource validation against FHIR IGs
- **[Postman](https://www.postman.com/)** - API testing and development tool
- **[UploadFIG Utility](https://github.com/brianpos/UploadFIG)** - Upload custom FHIR IGs to local servers

> Note: FHIR® Lab is part of The Strengthening Standards Capability Project (SSCP), co-funded by CSIRO Australia and Australian Government, Department of Foreign Affairs and Trade.

## Connectathon Success Criteria

Participants will demonstrate success through the following activities:

1. ✅ Validate FHIR resources against the draft PH Core, eReferral, and Immunization Implementation Guides
2. ✅ Successfully submit individual FHIR resources to the test FHIR server
3. ✅ Successfully submit FHIR bundles containing related resources in a single transaction
4. ✅ Perform FHIR search queries using standard search parameters
5. ✅ Retrieve resources using patient identifiers and clinical filters
6. ✅ Verify content accuracy and completeness of exchanged data
7. ✅ Provide structured feedback on gaps, issues, and recommendations for profile refinement
8. ✅ Document lessons learned and best practices for implementation

## Postman Collection and Environment

To help participants get started, we have prepared a Postman collection and environment file with pre-configured requests for each use case. The collection includes:

- **Expanding valuesets** - Test terminology server capabilities
- **Validating resources** - Test conformance to FHIR profiles
- **Submitting resources** - Individual and batch submissions
- **Submitting transaction bundles** - Multi-resource transactions
- **Retrieving resources** - Search and read operations

📥 [Download Postman Collection](./postman/fhir_connectathon_collection.json)
📥 [Download Postman Environment](./postman/fhir_connectathon_environment.json)

## How to Prepare for the Connectathon

1. **Review the FHIR IGs**: Familiarize yourself with the PH Core, eReferral, and Immunization Implementation Guides
2. **Understand FHIR Basics**: Review HL7 FHIR fundamentals and REST API conventions
3. **Set Up Access**: Ensure you have access to the FHIRLab servers (no credentials required)
4. **Download Tools**: Install Postman and review the prepared collections and sample data
5. **Test Locally**: Use the sample Postman requests to test against the FHIRLab servers
6. **Bring Questions**: Come prepared with questions about implementation challenges or unclear specifications

## Supplementary Information

### Key Contacts

- **For Connectathon Inquiries**: [Contact Email TBD]
- **For Technical Support**: [Tech Support Email TBD]
- **For FHIR IG Feedback**: [Feedback Email TBD]

### Additional Resources

- [FHIR Official Documentation](https://www.fhir.org/summary.html)
- [HL7 FHIR Community Chat](https://chat.fhir.org/)
- [Philippine eHealth Roadmap](https://doh.gov.ph/)
- [NTHC Publications and Resources](https://nthc.upmanila.edu.ph/)

### Feedback and Reporting

Participants are encouraged to submit structured feedback on:

- **Profile Conformance**: Gaps or inconsistencies in the FHIR profiles
- **Terminology Mappings**: Issues with local code mappings
- **Server Responses**: Technical issues or unexpected behavior
- **Implementation Challenges**: Real-world barriers to adoption
- **Best Practices**: Recommendations for streamlined implementation

👉 [FHIR IG Technical Feedback Sheet](https://docs.google.com/spreadsheets/d/)

---

## Disclaimer

FHIR® is a registered trademark of Health Level Seven International.

This Connectathon is made possible through the collaborative efforts of the National Telehealth Center, UP Manila SILab, the Department of Health, and partners in the digital health ecosystem.

For questions and queries regarding the Connectathon, please contact **nih-nthc.upmanila@up.edu.ph** or visit the [NTHC website](https://nthc.upmanila.edu.ph/).

---

**Last Updated**: June 2026  
**Next Review**: Post-Connectathon Debrief
