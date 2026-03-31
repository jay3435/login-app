from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)
@app.route("/")
def home():
    return redirect(url_for("login"))


# Load users from file
def load_users():
    if not os.path.exists("users.json"):
        return {}
    with open("users.json") as f:
        return json.load(f)

# Save users to file
def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()
        if username in users:
            message = "User already exists!"
        else:
            users[username] = password
            save_users(users)
            message = "Registered successfully!"
    return render_template("register.html", message=message)

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()
        if username in users and users[username] == password:
            message = "Login successful! Welcome, " + username
        else:
            message = "Invalid username or password!"
    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)