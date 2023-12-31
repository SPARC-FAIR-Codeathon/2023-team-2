"""Entry point for the flask app"""
import os
from app import app

if __name__ == "__main__":
    port = int(os.environ.get("FLASK_SERVER_PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
