#!/usr/bin/python3

"""
This function generates personalized invitation files from a template
with placeholders and a lis of object. The outputted files are named
sequentially, starting from 1.
"""

"""Open template.txt and read file"""
try:
    template = "template.txt"
    with open(template, 'r', encoding="UTF-8") as file:
        template_file = file.read()
except FileNotFoundError as e:
    print(f"Error, {e}, template file not found.")


"""
Function for invitation generator.
Parameters:
template, file from which new file will be based off.
attendees: List of dict containing attendees data.
"""
def generate_invitations(template, attendees):
    try:
        if not isinstance(template, str):
            raise TypeError("Template should be a string")
        if not isinstance(attendees, list) or not all(isinstance(index, dict)
                                                      for index in attendees):
            raise TypeError("Attendees should be a list of dictionaries")
    except TypeError as e:
        print(f"Error: {e}")

    try:
        if template is None:
            raise ValueError("Template file is empty")
        if attendees is None:
            raise ValueError("Attendees is empty")
    except ValueError as e:
        print(f"Error: {e}")


    for index, attendee in enumerate(attendees, start = 1):
        try:
            output = template.replace("{name}", attendee.get
                                      ("name", "N/A"))
            output = template.replace("{event_title}", attendee.get
                                      ("event_title", "N/A"))
            output = template.replace("{event_date}", attendee.get
                                      ("event_date", "N/A") or "N/A")
            output = template.replace("{event_location}", attendee.get
                                      ("event_location", "N/A"))

            with open(f'output_{index}.txt', 'w', encoding="UTF-8") as output_file:
                output_file.write(output)
        except Exception:
            print(f"Error generating file")
