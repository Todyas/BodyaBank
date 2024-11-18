from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from bank import Bank
import config

app = Flask(__name__)
app.config.from_object(config.Config)

db.init_app(app)

bank = Bank(db)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        user_id = request.form["user_id"]
        amount = int(request.form["amount"])
        user = User.query.get(user_id)
        if user:
            bank.deposit(amount, user)
        return redirect(url_for("hello"))
    return render_template("deposit.html")


@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        user_id = request.form["user_id"]
        amount = int(request.form["amount"])
        user = User.query.get(user_id)
        if user:
            bank.withdraw(amount, user)
        return redirect(url_for("index"))
    return render_template("withdraw.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        name = request.form["name"]
        balance = int(request.form["balance"])
        user = User(name=name, balance=balance)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("registration.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
