# awscli-validator

`awscli-validator` is a Python package designed to validate AWS CLI command outputs. This ensures reliability and consistency when integrating AWS CLI commands into automation workflows.

## Features
- Validate AWS CLI outputs against predefined JSON schemas.
- Parse outputs provided as strings or dictionaries.
- Simple, lightweight, and easy to integrate.

## Installation

Install the package via pip:

```bash
pip install awscli-validator
```

## Example

```
from awscli_validator.validator import AWSCLIValidator

# Define a schema
schema = {
    "type": "object",
    "properties": {
        "Buckets": {"type": "array"},
    },
    "required": ["Buckets"],
}

# Initialize the validator
validator = AWSCLIValidator(schema=schema)

# Validate a sample output
output = '{"Buckets": [{"Name": "example-bucket"}]}'
if validator.validate_output(output):
    print("Output is valid.")

```
