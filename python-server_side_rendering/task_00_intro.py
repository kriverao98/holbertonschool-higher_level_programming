#!/usr/bin/python3
import os

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
    if not isinstance(template, str):
        print("Error: Template should be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(index, dict) for index in attendees):
        print("Error: Attendees should be a list of dictionaries")
        return

    # Handle empty template
    if not template:
        print("Template is empty, no output files generated.")
        return
    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return


    for index, attendee in enumerate(attendees, start=1):
        try:
            output = template.replace("{name}", attendee.get("name", "N/A"))
            output = output.replace("{event_title}", attendee.get("event_title", "N/A"))
            output = output.replace("{event_date}", attendee.get("event_date", "N/A") or "N/A")
            output = output.replace("{event_location}", attendee.get("event_location", "N/A"))

            with open(f'output_{index}.txt', 'w', encoding="UTF-8") as output_file:
                output_file.write(output)
        except Exception as e:
            print(f"Error generating file for attendee {index}: {e}")