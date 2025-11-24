#!/usr/bin/env python3
"""
Generate MkDocs documentation for FHIR profiles repository.
Scans the repository for JSON resources (StructureDefinition, CodeSystem, ValueSet)
under the `input/` or `terminology/` directories and creates markdown pages.
"""

import json
import os
from pathlib import Path

BASE_DIR = Path("/home/ariful/Desktop/ZarishSphere-Platform/zarish-fhir-profiles")
INPUT_DIRS = [BASE_DIR / "input", BASE_DIR / "terminology"]
DOCS_DIR = BASE_DIR / "docs"
PROFILES_DIR = DOCS_DIR / "profiles"
CODESYSTEMS_DIR = DOCS_DIR / "codesystems"
VALUESETS_DIR = DOCS_DIR / "valuesets"

# Ensure directories exist
for d in [PROFILES_DIR, CODESYSTEMS_DIR, VALUESETS_DIR]:
    d.mkdir(parents=True, exist_ok=True)


def write_md(file_path: Path, content: str):
    with open(file_path, "w") as f:
        f.write(content)


def generate_overview(resource, kind: str):
    """Create a markdown overview for a given FHIR resource"""
    resource_id = resource.get("id", "")
    name = resource.get("name", "")
    title = resource.get("title", "") or name
    url = resource.get("url", "")
    status = resource.get("status", "draft")
    description = resource.get("description", "")
    version = resource.get("version", "")
    # Concept count if applicable
    count = len(resource.get("concept", [])) if "concept" in resource else None
    md = f"# {title}\n\n{description}\n\n## Overview\n\n- **ID**: `{resource_id}`\n- **Name**: {name}\n- **URL**: `{url}`\n- **Status**: {status}\n- **Version**: {version}\n"
    if count is not None:
        md += f"- **Concept Count**: {count}\n"
    md += "\n## Example Usage\n\n```json\n{\n  \"resourceType\": \"Reference\",\n  \"reference\": \"{resource_type}/{resource_id}\"\n}\n```\n"
    md += "\n---\n\n*Generated automatically by `generate_profiles_docs.py`*\n"
    return md


def process_file(file_path: Path):
    with open(file_path) as f:
        data = json.load(f)
    resource_type = data.get("resourceType")
    if resource_type == "StructureDefinition":
        md = generate_overview(data, "profile")
        out_path = PROFILES_DIR / f"{data.get('id')}.md"
    elif resource_type == "CodeSystem":
        md = generate_overview(data, "codesystem")
        out_path = CODESYSTEMS_DIR / f"{data.get('id')}.md"
    elif resource_type == "ValueSet":
        md = generate_overview(data, "valueset")
        out_path = VALUESETS_DIR / f"{data.get('id')}.md"
    else:
        return None
    write_md(out_path, md)
    print(f"Created: {out_path}")
    return out_path


def main():
    processed = []
    for dir_path in INPUT_DIRS:
        if not dir_path.is_dir():
            continue
        for json_file in dir_path.rglob("*.json"):
            result = process_file(json_file)
            if result:
                processed.append(result)
    print(f"\n✅ Generated {len(processed)} documentation pages")

if __name__ == "__main__":
    main()
