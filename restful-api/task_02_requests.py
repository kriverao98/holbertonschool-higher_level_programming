#!/usr/local/bin/python3
"""This module fetches data from specified url"""
import requests
import json
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com')
    status_code = response.status_code
    print(f"Status Code: {status_code}")
    
    if status_code == 200:
        posts = response.json()
        for post in posts:
                print(post["title"])
def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com')
    status_code = response.status_code
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
        return True
    else:
        return False
