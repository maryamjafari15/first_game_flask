from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "super-secret-key"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        guess = int(request.form["guess"])

        if "number" not in session:
            session["number"] = random.randint(1, 50)
            session["count"] = 0

        session["count"] += 1

        if guess < session["number"]:
            session["message"] = "❌ Nope! My number is higher! 🔼"
        elif guess > session["number"]:
            session["message"] = "❌ Nah! My number is lower! 🔽"
        else:
            session["message"] = f"🎉 Whoa! You got it in {session['count']} tries! 🏆"
            session.pop("number")
            session.pop("count")

        return redirect(url_for("index"))

    # حالت GET
    message = session.pop("message", "")
    show_game = "number" in session and message != ""

    return render_template("index.html", message=message, show_game=show_game)

if __name__ == "__main__":
    app.run(debug=True)