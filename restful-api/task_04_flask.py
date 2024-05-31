#!/usr/local/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store user data
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

# Endpoint for root URL
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to serve JSON data
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

# Endpoint for /status
@app.route('/status')
def get_status():
    return "OK"

# Endpoint to get user details by username
@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404

# Endpoint to add new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'username' in data:
        username = data['username']
        users[username] = data
        return f"User {username} added successfully", 201
    else:
        return "Missing username in request data", 400

if __name__ == "__main__":
    app.run