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


@app.route("/get_categories")
def get_categories():
    # Check MongoDB connection
    print(mongo.db)  # This line should have the same indentation as the next line.

    if mongo.db is not None:
        categories = mongo.db.categories.find()
        # Proceed with handling categories
    else:
        raise Exception("Database connection failed")
    return render_template("categories.html", categories=categories)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have resieved your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact Us")


# Routing for the register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form.get("username")
    if username:
        username = username.lower()
    else:
        return "Username is required", 400

    
    if request.method == 'POST':
        username = request.form.get("username")
        if not username:
            return "Username is required", 400  # Handle POST validation
        # Process registration
    return render_template('register.html')  # Render the registration page for GET
    
    
    if request.method == "POST":
        # check if username already exists within the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # message to alert user that the username already exists
            flash("Username already exists, please try again")
            # return user to register page to try again
            return redirect(url_for("register"))

        # else if no existing user, register user
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
    
    return render_template("register.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)