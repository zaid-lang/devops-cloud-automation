from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "DevOps Microservice is Running!"


@app.route("/health")
def health():
    return {"status": "UP"}


@app.route("/api/info")
def info():
    return {
        "application": "DevOps Cloud Automation Microservice",
        "version": "1.0",
        "environment": "development"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)