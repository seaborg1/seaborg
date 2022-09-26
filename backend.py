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

@app.route("/one kiss")
def one_kiss():
    return """"<h1> For Ethan and Daniel: <h1> One kiss is all it takes
Fallin' in love with me
Possibilities
I look like all you need
Let me take the night, I love real easy
And I know that you'll still wanna see me
On the Sunday morning, music real loud
Let me love you while the moon is still out
Something in you, lit up heaven in me
The feeling won't let me sleep
'Cause I'm lost in the way you move, the way you feel
One kiss is all it takes
Fallin' in love with me
Possibilities
I look like all you need
One kiss is all it takes
Fallin' in love with me
Possibilities
I look like all you need
One
One
One
One
I just wanna feel your skin on mine
Feel your eyes do the exploring
Passion in the message when you smile
Take my time
Something in you lit up heaven in me
The feeling won't let me sleep
'Cause I'm lost in the way you move, the way you feel
One kiss is all it takes
Fallin' in love with me
Possibilities
I look like all you need
One kiss is all it takes
Fallin' in love with me
Possibilities
I look like all you need
One
One
One
One
See a wonderland in your eyes
Might need your company tonight
Something in you lit up heaven in me
The feeling won't let me sleep
'Cause I'm lost in the way you move, the way you feel
One kiss is all it takes
Fallin' in love with me
Possibilities
I look like all you need
One kiss is all it takes
Fallin' in love with me
Possibilities
I look like all you need
One
One
One
One
""""

@app.route("/admin")
def admin():
    return "<h1> HOLA! You found the admin page <h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
