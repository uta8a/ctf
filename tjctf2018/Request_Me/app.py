from flask import Flask, request, redirect
import os
app = Flask(__name__)

from functools import wraps
from flask import request, Response

username_pass = {}

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username in username_pass and password == username_pass[username]

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.route("/", methods=["GET", "POST", "PUT", "OPTIONS", "DELETE"])
def hello():
    if request.method == "GET":
        return "<p>WRONG <a href='http://lmgtfy.com/?q=http+request+options'>FLAG</a></p>"
    elif request.method == "POST":
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return "Maybe you should take your credentials back?"
    elif request.method == "PUT":
        vals = request.values
        username = request.values.get("username")
        password = request.values.get("password")
        if username and password:
            username_pass[username] = password
            return "I stole your credentials!"
        else:
            return "I couldn't steal your credentials! Where did you hide them?"
    elif request.method == "DELETE":
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        del username_pass[auth.username]
        return "Finally! The flag is tjctf{wHy_4re_th3r3_s0_m4ny_Opt10nS}"
    elif request.method == "OPTIONS":
        return "GET, POST, PUT, DELETE, OPTIONS\nParameters: username, password\nSome methods require HTTP Basic Auth"

if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", "9999")))

