#!/usr/bin/env python3
"""
Validate Royalty OS v0.5 example YAML files against JSON Schema files.

Required packages:
pip install pyyaml jsonschema

Usage:
python scripts/validate_examples.py
"""

import json
import sys
from pathlib import Path

try:
import yaml
except ImportError as exc:
print("Missing dependency: PyYAML")
print("Install with: pip install pyyaml")
raise SystemExit(1) from exc

try:
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError, ValidationError
except ImportError as exc:
print("Missing dependency: jsonschema")
print("Install with: pip install jsonschema")
raise SystemExit(1) from exc

REPO_ROOT = Path(**file**).resolve().parents[1]

VALIDATION_TARGETS = [
{
"name": "Personal AI Agent",
"schema": REPO_ROOT / "schemas" / "personal-agent.schema.json",
"example": REPO_ROOT / "examples" / "personal-agent.example.yaml",
},
{
"name": "Personal Trace Fingerprint",
"schema": REPO_ROOT / "schemas" / "trace-fingerprint.schema.json",
"example": REPO_ROOT / "examples" / "trace-fingerprint.example.yaml",
},
{
"name": "Agent-Mediated Usage Detection Event",
"schema": REPO_ROOT / "schemas" / "usage-detection-event.schema.json",
"example": REPO_ROOT / "examples" / "usage-detection-event.example.yaml",
},
]

def load_json(path: Path) -> dict:
"""Load a JSON file."""
try:
with path.open("r", encoding="utf-8") as file:
return json.load(file)
except FileNotFoundError as exc:
raise RuntimeError(f"JSON file not found: {path}") from exc
except json.JSONDecodeError as exc:
raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc

def load_yaml(path: Path) -> dict:
"""Load a YAML file."""
try:
with path.open("r", encoding="utf-8") as file:
data = yaml.safe_load(file)
except FileNotFoundError as exc:
raise RuntimeError(f"YAML file not found: {path}") from exc
except yaml.YAMLError as exc:
raise RuntimeError(f"Invalid YAML in {path}: {exc}") from exc

```
if data is None:
    raise RuntimeError(f"YAML file is empty: {path}")

if not isinstance(data, dict):
    raise RuntimeError(f"YAML root must be an object/mapping: {path}")

return data
```

def format_validation_path(error: ValidationError) -> str:
"""Return a readable JSON path for validation errors."""
if not error.absolute_path:
return "$"

```
parts = ["$"]
for item in error.absolute_path:
    if isinstance(item, int):
        parts.append(f"[{item}]")
    else:
        parts.append(f".{item}")

return "".join(parts)
```

def validate_target(name: str, schema_path: Path, example_path: Path) -> None:
"""Validate one example YAML file against one JSON Schema file."""
print(f"Validating target: {name}")
print(f"Schema:  {schema_path.relative_to(REPO_ROOT)}")
print(f"Example: {example_path.relative_to(REPO_ROOT)}")

```
schema = load_json(schema_path)
example = load_yaml(example_path)

try:
    Draft202012Validator.check_schema(schema)
except SchemaError as exc:
    raise RuntimeError(f"Invalid JSON Schema in {schema_path}: {exc.message}") from exc

validator = Draft202012Validator(schema, format_checker=FormatChecker())
errors = sorted(
    validator.iter_errors(example),
    key=lambda err: list(err.absolute_path),
)

if errors:
    print("")
    print("Validation failed.")
    print(f"Target: {name}")
    print("")

    for error in errors:
        path = format_validation_path(error)
        print(f"- Path: {path}")
        print(f"  Error: {error.message}")

    raise RuntimeError(f"Validation failed for target: {name}")

print("Validation passed.")
print("")
```

def main() -> int:
print("Royalty OS v0.5 example validation")
print("")

```
try:
    for target in VALIDATION_TARGETS:
        validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )
except RuntimeError as exc:
    print(str(exc))
    return 1

print("All examples passed validation.")
return 0
```

if **name** == "**main**":
sys.exit(main())
