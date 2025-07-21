from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "super-secret-key"

@app.route("/", methods=["GET", "POST"])
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 50)
        session["count"] = 0


    message = ""
    if request.method == "POST":
        guess = int(request.form["guess"])
        session["count"] += 1

        if guess < session["number"]:
            message = "❌ Nope! My number is higher! 🔼"
        elif guess > session["number"]:
            message = "❌ Nah! My number is lower! 🔽"
        else:
            message = f"🎉 Whoa! You got it in {session['count']} tries! 🏆"
            session.pop("number")
            session.pop("count")
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)