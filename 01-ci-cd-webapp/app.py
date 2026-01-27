from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Client Web App - Updated via PR"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
