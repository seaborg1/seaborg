from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>HELLO! This is the main page for my website./n/nGoodbye<h1>"

@app.route("/admin")
def admin():
    return "<h1> HOLA! You found the admin page <h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
