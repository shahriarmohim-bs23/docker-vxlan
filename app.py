from flask import Flask, jsonify, request
import os
import random
import string
import requests
from datetime import datetime


app = Flask(__name__)

@app.route("/alive", methods=["GET"])
def alive():
    resp = jsonify({"ping": "pong"})
    return resp, 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)