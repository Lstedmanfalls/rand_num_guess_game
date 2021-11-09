from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "ThisIsAsecretKey"

@app.route("/")
def index():
    rand = random.randrange(1, 11)
    if "message" in session:
        message = session["message"]
        return render_template("index.html", message = message, rand = session["rand"])
    else:
        return render_template("index.html", rand = rand)

@app.route("/restart", methods=["POST"])
def restart():
    session.clear()
    return redirect("/")

@app.route("/guess", methods=["POST"])
def rand():
    session["guess"] = request.form["guess"]
    session["rand"] = request.form["rand"]
    if session["guess"] == session["rand"]:
        session["message"] = f"You guessed it correctly, the number is {session['rand']}!"
    if session["guess"] > session["rand"]:
        session["message"] = "Too high"
    if session["guess"] < session["rand"]:
        session["message"] = "Too low"
    return redirect ("/")

app.run(debug=True)