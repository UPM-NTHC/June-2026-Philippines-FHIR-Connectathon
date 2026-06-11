# June 2026 Philippines FHIR® Connectathon – Boracay, Aklan, Philippines

<PLACE HOLDER FOR GRAPHIC DESIGN>

The June 2026 Philippines FHIR® Connectathon is co-organized by the National Telehealth Center (NTHC), under the University of the Philippines Manila National Institutes of Health, in partnership with the Department of Health (DOH), Philippine Health Insurance Corporation (PhilHealth), The Strengthening Standards Capability Project (SSCP) of  Commonwealth Scientific and Industrial Research Organisation (CSIRO), Aklan Provincial Health Office, and othterkey stakeholders.

This Connectathon represents a milestone in the Philippines' digital health interoperability journey, bringing together healthcare systems, EMR vendors, and government agencies to advance standardized health data exchange using FHIR® profiles including PH Core, eReferral (PeReF), and Immunization specifications.

The Connectathon aims to foster interoperability across health systems by providing opportunities for healthcare system developers, business owners, vendors, government agencies, hospitals, and EMR providers to participate in critical use-case scenarios, validate emerging FHIR Implementation Guides, and build a community of practice around standards-based digital health.

## CONNECTATHON OBJECTIVES

- ### Primary Objectives
  1. **Capacity Building**: Equip IT professionals, decision-makers, and healthcare teams with foundational knowledge of interoperability standards and FHIR implementation best practices
  2. **Standards Validation**: Test and validate emerging FHIR Implementation Guides (PH Core, eReferral, and Immunization) across real-world health system use cases
  3. **Interoperability Testing**: Demonstrate data exchange and system interoperability using standardized FHIR profiles across multiple tracks
  4. **Feedback & Refinement**: Capture technical issues, gaps, and lessons learned to inform the next iteration of FHIR IGs and national interoperability standards
  5. **Governance & Scale-up**: Engage national agencies, hospitals, LGUs, and EMR vendors in governance discussions to generate policy recommendations for national scale-up

- ### Secondary Objectives
  1. Validate terminology mappings and workflow simulations in alignment with WHO SMART Guidelines
  2. Establish a sustainable community of practice around FHIR standards in the Philippines
  3. Conduct a formal handover of refined FHIR IGs to the Department of Health for long-term adoption
  4. Generate evidence and documentation to support the Digital Health Roadmap of the Philippines

## DISCLAIMER: 
- ***The PH Core IG and PH eReferral IG are draft versions under active development and are not intended for production use. Both guides will be refined and updated based on feedback, issues, and recommendations gathered during the June Connectathon. Content, profiles, and implementation details are subject to change.***

## CONNECTATHON TRACK DETAILS

- ### Track 1: PH eReferral IG [Draft PH eReferral FHIR Implementation Guide (IG)](https://build.fhir.org/ig/ph-ereferral-organization/ph-ereferral/en/index.html)
  - **Objective**: Demonstrate the end-to-end referral lifecycle (create, accept, reject, refer onward, complete/back-refer) between HCPN facilities using ServiceRequest and Task built on PH Core profiles, consistent with UHC Act and DOH AO 2020-0019 requirements.
  - <mark>**Link to Bundle Examples**</mark>


- ### Track 2: PH Core IG [Draft PH Core FHIR Implementation Guide (IG)](https://build.fhir.org/ig/UP-Manila-SILab/ph-core/en/index.html)
  - **Objective**: Validate that PH Core IG v0.2.0 profiles are implementable by creating, exchanging, and validating a complete encounter record — using the Encounter profile (primary) with Patient, Organization, Condition, Observation, Practitioner, and optionally PractitionerRole — including Philippine-specific identifiers, extensions, and terminology bindings.
  - <mark>**Link to Bundle Examples**</mark>



## FHIR SERVERS AVAILABLE FOR TESTING DURING THE CONNECTATHON

| Version | Server | Endpoint | Capabilities |
|-------------|---------|-------------|-------------|
| FHIR R4 | FHIRLab (HAPI FHIR) | https://cdr.fhirlab.net/fhir | CRUD, transaction, validation |
| FHIR R4 | Ontoserver Terminology | https://tx.fhirlab.net/fhir | $expand, $validate-code, $lookup |
| FHIR R4 | Ontoserver with Shrimp Viewer | https://ontoserver.csiro.au/shrimp/ | Terminology browsing & visualization |
| FHIR R4 | FHIRPortal (HAPI FHIR) | https://fhirportal.telehealth.ph/| Back Up HAPI FHIR Server. **Do not use unless instructed**|

> **Note**: FHIRLab is an open interoperability sandbox maintained as part of The Strengthening Standards Capability Project (SSCP), co-funded by CSIRO Australia and the Australian Government, Department of Foreign Affairs and Trade. FHIR servers will remain accessible for testing and ongoing learning activities post-Connectathon.


## INTERNATIONAL SYNTACTIC AND SEMANTIC STANDARDS

**Participants should familiarize themselves with the following foundational standards:**

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

## FHIRLab TOOLS AND RESOURCES

- ### FHIR Servers and Tooling
  - **[FHIR Server (HAPI FHIR Endpoint)](https://cdr.fhirlab.net/fhir)** - Main FHIR server for resource submissions and retrieval
  - **[Terminology Server (Ontoserver Endpoint)](https://tx.fhirlab.net/fhir)** - ValueSet and terminology operations
  - **[Terminology Browser (Ontoserver + Shrimp)](https://ontoserver.csiro.au/shrimp/)** - Visual terminology browsing and mapping

- ### Local Testing Tools (Optional)
  - **[FHIR CLI](https://hapifhir.io/hapi-fhir/docs/tools/hapi_fhir_cli.html#server-run-server)** - Run a local HAPI FHIR server for testing
  - **[FHIR Validator](https://validator.fhirlab.net)** - Online resource validation against FHIR IGs
  - **[Postman](https://www.postman.com/)** - API testing and development tool
  - **[UploadFIG Utility](https://github.com/brianpos/UploadFIG)** - Upload custom FHIR IGs to local servers
    
> Note: FHIR® Lab is part of The Strengthening Standards Capability Project (SSCP), co-funded by CSIRO Australia and Australian Government, Department of Foreign Affairs and Trade.

## CONNECTATHON SUCCESS CRITERIA

**Participants will demonstrate success through the following activities:**

1. ✅ Validate FHIR resources against the draft PH Core and eReferral Implementation Guides
2. ✅ Successfully submit individual FHIR resources to the test FHIR server
3. ✅ Successfully submit FHIR bundles containing related resources in a single transaction
4. ✅ Perform FHIR search queries using standard search parameters
5. ✅ Retrieve resources using patient identifiers and clinical filters
6. ✅ Verify content accuracy and completeness of exchanged data
7. ✅ Provide structured feedback on gaps, issues, and recommendations for profile refinement
8. ✅ Document lessons learned and best practices for implementation


## HOW TO PREPARE FOR THE CONNECTATHON?

1. **Review the FHIR IGs**: Familiarize yourself with the PH Core and eReferral Implementation Guides
2. **Understand FHIR Basics**: Review HL7 FHIR fundamentals and REST API conventions
3. **Set Up Access**: Ensure you have access to the FHIRLab servers (no credentials required)
4. **Download Tools**: Install Postman and review the prepared collections and sample data
5. **Test Locally**: Use the sample Postman requests to test against the FHIRLab servers
6. **Bring Questions**: Come prepared with questions about implementation challenges or unclear specifications

## SUPPLEMENTARY INFORMATION

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

👉 [FHIR IG Technical Feedback Sheet](https://docs.google.com/spreadsheets/d/1WU8-8s-SLfpmF04wGHurtX7mRZnqGI2dcPfHgsN7LxA/edit?usp=sharing)

---

## Disclaimer

FHIR® is a registered trademark of Health Level Seven International.

This Connectathon is made possible through the collaborative efforts of the University of the Philippines Manila National Institutes of Health, Department of Health (DOH), Philippine Health Insurance Corporation (PhilHealth), The Strengthening Standards Capability Project (SSCP) of Commonwealth Scientific and Industrial Research Organisation (CSIRO), Aklan Provincial Health Office, and othterkey stakeholders.

For questions and queries regarding the Connectathon, please contact **nih-nthc.upmanila@up.edu.ph**.

---

**Last Updated**: June 11, 2026  
**Next Review**: Post-Connectathon Debrief
