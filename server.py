from flask import Flask, jsonify
import time

app = Flask(__name__)
START_TIME = time.time()


@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "Hello from myapp"})


@app.route("/health")
def health():
    uptime = round(time.time() - START_TIME, 2)
    return jsonify({"status": "healthy", "uptime_seconds": uptime})


@app.route("/error")
def error():
    return "hi"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)  # nosec B104
