from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("HELLO")
    return "<p>Hello, World!</p>"

# Try the following command in Dockerfile to change the host:
# flask run --host=0.0.0.0
# This tells your operating system to listen on all public IPs.
# https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
