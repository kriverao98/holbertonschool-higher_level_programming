import json
#!/usr/bin/python34


def save_to_json_file(my_obj, filename):
    """Save the given object to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
