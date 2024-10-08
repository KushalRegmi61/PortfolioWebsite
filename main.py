from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, ValidationError, Email, Length
from dotenv import load_dotenv
import smtplib
import os
load_dotenv()

#loading email and password from .env file
EMAIL = os.getenv("my_email")
PASSWORD = os.getenv("EMAIL_PASSWORD")

#creating a flask app
app = Flask(__name__)

#creating a contact form 
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField(label="Send", render_kw={"size": 30})



#creating home page 
@app.route('/')
def home():
    return render_template("index.html")

#creating page page
@app.route('/projects')
def projects():
    return render_template("project.html")

#creating contact page and passing contact form data to the server
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name=data["name"]
        email=data["email"]
        message=data["message"]
        
        msg_data=(
            f"Subject: New Msg Alert\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"{message}"
        )
        #sending email....
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=email, to_addrs="kushalbro82@gmail.com", msg=msg_data)
            
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

#degug the website 
if __name__ == "__main__":
    app.run(debug=True , port=5000)

#<header
#   class="masthead"
#   style="background-image: url('../static/assets/img/home-bg.jpg')"
# >