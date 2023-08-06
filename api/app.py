"""This is the main entrypoint for the flask app"""
from flask import Flask, request, jsonify
from flask_cors import CORS

from helpers.generate import generate_data

app = Flask(__name__)

CORS(app)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    return "Hello! :)"


@app.route("/generate", methods=["POST"])
def generate():
    """Generate neuron visualizations"""
    try:
        data = request.get_json()

        modules = data["modules"]

        response = generate_data(modules)

        return jsonify(response)
    # pylint: disable=broad-except
    except Exception as error:
        return error


@app.route("/cache-me")
def cache():
    """Cache this response"""
    return "nginx will cache this response"


@app.route("/info")
def info():
    """Return headers and other info"""
    resp = {
        "connecting_ip": request.headers["X-Real-IP"],
        "proxy_ip": request.headers["X-Forwarded-For"],
        "host": request.headers["Host"],
        "user-agent": request.headers["User-Agent"],
    }

    return jsonify(resp)


@app.route("/flask-health-check")
def flask_health_check():
    """Check flask health"""
    return "success"
