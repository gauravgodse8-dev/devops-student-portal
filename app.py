from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Student Portal</title>
    </head>
    <body>
        <h1>DevOps Student Portal</h1>
        <h2>TE IT - Semester V</h2>

        <p>Welcome to the DevOps End-to-End Pipeline Project.</p>

        <p>
            Application deployed using:
            GitHub → Jenkins → Docker → Kubernetes → AWS
        </p>

        <p>Status: Application Running Successfully</p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)