import json
#!/usr/bin/python3


def from_json_string(my_str):
    """Convert a JSON string to a Python object."""
    return json.loads(my_str)
