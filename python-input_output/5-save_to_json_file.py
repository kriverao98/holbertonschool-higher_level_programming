import json
#!/usr/bin/python34


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
