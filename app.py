from flask import Flask, render_template, request
from bank import BankAccount
from user import User

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", name=name)


@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    return render_template("deposit.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        name = request.form["name"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    Bodya = User("Bodya")
