#!/usr/bin/python3
"""This module fetches data from specified url"""
import requests
import csv


def fetch_and_print_posts(url):
    """
    Fetches data from the specified URL and prints the posts.

    Args:
        url (str): The URL to fetch the data from.

    Returns:
        None
    """
    get_requests = requests.get(url)
    print(f"Status Code: {response.get_requests}")
    if response.get_requests == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
    else:
        print("Failed to retrieve data")


def fetch_and_save_posts(url):
    """
    Fetches data from the specified URL and saves the posts to a CSV file.

    Args:
        url (str): The URL to fetch the data from.

    Returns:
        None
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        posts = []
        for post in data:
            post_data = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            posts.append(post_data)
            
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)
            
        print("Data saved to posts.csv")
    else:
        print("Failed to retrieve data")
