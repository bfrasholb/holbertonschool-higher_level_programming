#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user store
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    # Validate JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Validate username
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check duplicate
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Create user object
    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = user

    return jsonify({
        "message": "User added",
        "user": user
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
