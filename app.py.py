from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>My First DevOps Project</h1><p>Running with Docker!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)