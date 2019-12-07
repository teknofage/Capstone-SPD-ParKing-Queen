from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    """Show Homepage"""
    return render_template("index.html", index=index)


@app.route('/login')
def login():
    """Show login"""
    return render_template("login.html", login=login)


@app.route('/registration')
def registration():
    """Show registration"""
    return render_template("registration.html", registration=registration)


@app.route('/payment_details')
def payment_details():
    """Show payment details"""
    return render_template("payment_details.html", payment_details=payment_details)


@app.route('/choose_vehicle')
def choose_vehicle():
    """Show choose vehicle"""
    return render_template("choose_vehicle.html", choose_vehicle=choose_vehicle)


if __name__ == "__main__":
    app.run(debug=True)