from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>HELLO! This is the main page for my website.<h1>"
    return " "
    return "<h1> The website is still heavily under development. Check back soon! <h1>"

@app.route("/haruka")
def haruka():
    return "<h1> Hello Haruka! <h1>"

@app.route("/kayle")
def kale():
    return "<h1> Wassup Kayle <h1>"

@app.route("/tess")
def tess():
    return "<h1> Hello Tess! <h1>" 

@app.route("/admin")
def admin():
    return "<h1> HOLA! You found the admin page <h1>"

if __name__ == "__main__":
    app.run(host='164.92.75.123')
