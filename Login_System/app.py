# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulazione di un database di utenti
users = {"admin": "admin", "user1": "mypassword"}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return f"Welcome, {username}!"
    else:
        return "Invalid credentials. Please try again.", 401

if __name__ == '__main__':
    app.run(debug=True)
