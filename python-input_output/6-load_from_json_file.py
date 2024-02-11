import json
#!/usr/bin/python3


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
