import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About Us")


@app.route("/")
@app.route("/get_categories")
def get_categories():
    categories = mongo.db.categories.find()
    return render_template("categories.html", categories=categories)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have resieved your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact Us")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # CHECK IF USERNAME OR EMAIL IS ALREADY REGISTERED ON SITE
        existing_user = mongo.db.users.find_one(
            {"user_name": request.form.get("username")})
        # ERROR MESSAGE IF USERNAME ALREADY EXISTS
        if existing_user:
            flash("Sorry, that username already exists")
            return redirect(url_for("register"))

        existing_email = mongo.db.users.find_one(
            {"user_email": request.form.get("email")})
        # ERROR MESSAGE IF EMAIL ALREADY EXISTS
        if existing_email:
            flash("Sorry, that email's already registered")
            return redirect(url_for("register"))
        # DETAILS TO REGISTER IN MONGO DB FOR NEW USERS
        register = {
            "user_name": request.form.get("username"),
            "user_email": request.form.get("email"),
            "user_password": request.form.get("password")
        }
        mongo.db.users.insert_one(register)

        #put the new user into the 'session' cookie
        session["user"] = request.form.get("username")
        flash("Registration Successful!")
    
    return render_template("register.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)