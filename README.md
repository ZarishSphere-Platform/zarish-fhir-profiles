# Zarish FHIR Profiles

**Part of the ZarishSphere Platform - A No-Code FHIR Healthcare Data Management System**

This repository contains FHIR profile definitions, implementation guides, and conformance resources for the ZarishSphere Platform. It defines how FHIR resources should be structured and constrained for use in the platform.

## 🚀 Technology Stack

- **FHIR Version**: R4 (4.0.1)
- **Profiling Tool**: FHIR Shorthand (FSH)
- **IG Publisher**: FHIR IG Publisher
- **Documentation**: MkDocs Material with Mermaid diagrams

## 📋 Prerequisites

- **Java**: Version 11+ for IG Publisher ([Download Java](https://www.java.com/))
- **Node.js**: Version 18+ for SUSHI ([Download Node.js](https://nodejs.org/))
- **Python**: Version 3.8+ for MkDocs ([Download Python](https://www.python.org/))
- **Git**: For version control

### Checking Your Installation

```bash
java -version    # Should show Java 11 or higher
node --version   # Should show v18.x or higher
python3 --version # Should show Python 3.8 or higher
```

## 🛠️ Step-by-Step Development Setup

### Step 1: Clone the Repository

```bash
cd ~/Desktop
git clone https://github.com/ZarishSphere-Platform/zarish-fhir-profiles.git
cd zarish-fhir-profiles
```

### Step 2: Install SUSHI (FSH Compiler)

```bash
# Install SUSHI globally
npm install -g fsh-sushi

# Verify installation
sushi --version
```

### Step 3: Install IG Publisher

```bash
# Download IG Publisher
curl -L https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar -o publisher.jar

# Or use the update script
./_updatePublisher.sh
```

### Step 4: Build the Implementation Guide

```bash
# Compile FSH to FHIR
sushi .

# Run IG Publisher
java -jar publisher.jar -ig ig.ini
```

The output will be in the `output` directory.

### Step 5: View the Implementation Guide

```bash
# Open in browser
open output/index.html

# Or serve with a local server
cd output
python3 -m http.server 8000
```

## 📁 Project Structure

```
zarish-fhir-profiles/
├── input/
│   ├── fsh/                    # FHIR Shorthand definitions
│   │   ├── profiles/          # Profile definitions
│   │   ├── extensions/        # Extension definitions
│   │   ├── valuesets/         # Value set definitions
│   │   └── examples/          # Example instances
│   ├── pagecontent/           # IG narrative content
│   └── images/                # Diagrams and images
├── docs/                      # MkDocs documentation
│   ├── index.md
│   ├── profiles/
│   ├── extensions/
│   └── guides/
├── output/                    # Generated IG (gitignored)
├── mkdocs.yml                # MkDocs configuration
├── ig.ini                    # IG Publisher configuration
├── sushi-config.yaml         # SUSHI configuration
└── README.md
```

## 📚 Defined Profiles

### Patient Profiles

- **ZarishPatient**: Extended patient profile with Bangladesh-specific extensions
- **ZarishPediatricPatient**: Specialized profile for pediatric patients

### Clinical Profiles

- **ZarishObservation**: Vital signs and clinical observations
- **ZarishCondition**: Diagnoses and health conditions
- **ZarishMedicationRequest**: Medication prescriptions
- **ZarishEncounter**: Patient encounters and visits

### Administrative Profiles

- **ZarishPractitioner**: Healthcare provider information
- **ZarishOrganization**: Healthcare organization details
- **ZarishLocation**: Facility and location information

## 🔍 Profile Features

### Extensions

- **Bangladesh National ID**: Extension for national identification
- **Religion**: Patient religious affiliation
- **Ethnicity**: Ethnic background
- **Occupation**: Patient occupation
- **Emergency Contact**: Extended emergency contact information

### Terminology Bindings

All profiles use appropriate value sets from:
- SNOMED CT
- LOINC
- ICD-10
- Custom Bangladesh-specific terminologies

## 📖 Documentation

Comprehensive documentation is available at:
**https://zarishsphere-platform.github.io/zarish-fhir-profiles/**

The documentation includes:
- Profile definitions with constraints
- Extension documentation
- Usage examples
- Implementation guides
- Interactive diagrams

### Building Documentation Locally

```bash
# Install MkDocs Material
pip install mkdocs-material mkdocs-mermaid2-plugin

# Serve documentation
mkdocs serve

# Build documentation
mkdocs build
```

## 🔧 Available Commands

| Command | Description |
|---------|-------------|
| `sushi .` | Compile FSH to FHIR JSON |
| `java -jar publisher.jar -ig ig.ini` | Build Implementation Guide |
| `mkdocs serve` | Serve documentation locally |
| `mkdocs build` | Build documentation |

## 🧪 Validation

### Validate Profiles

```bash
# Compile FSH
sushi .

# Validate with IG Publisher
java -jar publisher.jar -ig ig.ini
```

### Validate Examples

```bash
# All examples are validated during IG build
# Check output/qa.html for validation results
```

## 📝 Creating New Profiles

### Step 1: Create FSH File

Create a new file in `input/fsh/profiles/`:

```fsh
Profile: ZarishNewProfile
Parent: Patient
Id: zarish-new-profile
Title: "Zarish New Profile"
Description: "Description of the new profile"

* identifier 1..* MS
* name 1..* MS
* gender 1..1 MS
```

### Step 2: Compile and Validate

```bash
sushi .
java -jar publisher.jar -ig ig.ini
```

### Step 3: Add Documentation

Create documentation in `docs/profiles/new-profile.md`

### Step 4: Update Navigation

Update `mkdocs.yml` to include the new profile

## 🌐 FHIR Compliance

- **FHIR Version**: R4 (4.0.1)
- **Base Profiles**: US Core, International Patient Summary
- **Validation**: All profiles validated against FHIR specification
- **Conformance**: Meets FHIR conformance requirements

## 🐛 Troubleshooting

### SUSHI Compilation Fails

```bash
# Check FSH syntax
sushi . --log-level debug

# Validate YAML configuration
cat sushi-config.yaml
```

### IG Publisher Fails

```bash
# Update publisher
./_updatePublisher.sh

# Run with verbose logging
java -jar publisher.jar -ig ig.ini -tx n/a
```

### Documentation Build Fails

```bash
# Check MkDocs configuration
mkdocs build --strict

# Reinstall dependencies
pip install --upgrade mkdocs-material
```

## 📚 Learning Resources

- [FHIR Profiling](https://www.hl7.org/fhir/profiling.html)
- [FHIR Shorthand Tutorial](https://fshschool.org/)
- [IG Publisher Documentation](https://confluence.hl7.org/display/FHIR/IG+Publisher+Documentation)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)

## 🤝 Contributing

1. Fork the repository
2. Create/modify FSH profiles
3. Build and validate
4. Update documentation
5. Submit pull request

## 📄 License

This project is part of the ZarishSphere Platform.

## 🔗 Related Repositories

- [zarish-fhir-server](https://github.com/ZarishSphere-Platform/zarish-fhir-server) - FHIR Server Implementation
- [zarish-fhir-data](https://github.com/ZarishSphere-Platform/zarish-fhir-data) - Terminology Data
- [zarish-frontend-shell](https://github.com/ZarishSphere-Platform/zarish-frontend-shell) - Frontend Application

## 🆘 Getting Help

- Browse [Documentation](https://zarishsphere-platform.github.io/zarish-fhir-profiles/)
- Check [Issues](https://github.com/ZarishSphere-Platform/zarish-fhir-profiles/issues)
- Review [IG Publisher QA Report](output/qa.html)
