from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "ThisIsAsecretKey"

@app.route("/")
def index():
    if "message" in session:
        message = session["message"]
        return render_template("index.html", message = message)
    else:
        session["rand"] = random.randrange(1, 11)
        print(session["rand"])
        return render_template("index.html")

@app.route("/restart", methods=["POST"])
def restart():
    session.clear()
    return redirect("/")

@app.route("/guess", methods=["POST"])
def rand():
    print(session["rand"])
    session["num_guess"] = int(request.form["guess"])
    if session["num_guess"] == session["rand"]:
        session["message"] = f"You guessed it, the number is {session['rand']}!"
    if session["rand"] > session["num_guess"]:
        session["message"] = "Too low"
    if session["rand"] < session["num_guess"]:
        session["message"] = "Too high"
    return redirect ("/")

app.run(debug=True)