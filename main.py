from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Welcome to Ryan's Test Flask app"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
