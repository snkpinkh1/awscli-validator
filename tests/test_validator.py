import pytest
from awscli_validator.validator import AWSCLIValidator

def test_valid_output():
    schema = {
        "type": "object",
        "properties": {
            "Buckets": {"type": "array"},
        },
        "required": ["Buckets"],
    }

    validator = AWSCLIValidator(schema=schema)
    output = '{"Buckets": [{"Name": "example-bucket"}]}'
    assert validator.validate_output(output) is True

def test_invalid_output():
    schema = {
        "type": "object",
        "properties": {
            "Buckets": {"type": "array"},
        },
        "required": ["Buckets"],
    }

    validator = AWSCLIValidator(schema=schema)
    output = '{"WrongKey": "value"}'

    with pytest.raises(ValueError):
        validator.validate_output(output)
