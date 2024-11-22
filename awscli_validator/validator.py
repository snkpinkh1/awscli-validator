import json
from typing import Dict, Any, Union
from jsonschema import validate, ValidationError

class AWSCLIValidator:
    """Validates AWS CLI command outputs."""

    def __init__(self, schema: Dict[str, Any]):
        """
        Initialize the validator with a schema.
        :param schema: A JSON schema to validate against.
        """
        self.schema = schema

    def validate_output(self, output: Union[str, Dict[str, Any]]) -> bool:
        """
        Validate AWS CLI output against the provided schema.
        :param output: AWS CLI JSON output as a string or dictionary.
        :return: True if valid, raises an exception if invalid.
        """
        if isinstance(output, str):
            try:
                output = json.loads(output)
            except json.JSONDecodeError:
                raise ValueError("Output is not valid JSON.")

        try:
            validate(instance=output, schema=self.schema)
        except ValidationError as e:
            raise ValueError(f"Validation failed: {e.message}")

        return True
