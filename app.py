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


@app.route("/american")
def american():
    return render_template("american.html", page_title="American")


@app.route("/thai")
def thai():
    return render_template("thai.html", page_title="Thai")


@app.route("/italian")
def italian():
    return render_template("italian.html", page_title="Italian")


@app.route("/indian")
def indian():
    return render_template("indian.html", page_title="Indian")


@app.route("/mexican")
def mexican():
    return render_template("mexican.html", page_title="Mexican")


@app.route("/chinese")
def chinese():
    return render_template("chinese.html", page_title="Chinese")


# Routing for the recipes page
@app.route("/recipies")
# find recipes from MongoDB database and render to recipes template
def recipies():
    # display last added recipe first
    recipies = list(mongo.db.recipe.find().sort("_id", -1))
    return render_template("recipies.html", recipe=recipies, username=session["user"])


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have resieved your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact Us", username=session["user"])


@app.route("/register", methods=["GET", "POST"])
def register():    
    if request.method == "POST":
        # check if username already exists within the database
        username = request.form.get("username").lower()
        existing_user = mongo.db.users.find_one({"username": username})

        if existing_user:
            # message to alert user that the username already exists
            flash("Username already exists, please try again")
            # return user to register page to try again
            return redirect(url_for("register"))

        # else if no existing user, register the user
        register = {
            "username": username,
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = username
        flash("Registration Successful")
        return redirect(url_for("recipies", username=session["user"]))  # Redirect to user recipe page after successful registration

    # Render the registration form
    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(
                        url_for("recipies"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login.html"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("recipies.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    #remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        # get add recipe form inputs to add to database
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "category_ingredients": request.form.get("category_ingredients"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "category_method": request.form.get("category_method"),
            "recipe_method": request.form.get("recipe_method"),
            "date_added": request.form.get("date_added"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]

        }
        # insert into database
        mongo.db.recipe.insert_one(recipe)
        # success message
        flash("Recipe successfully added")
        # return user to recipe page
        return redirect(url_for("recipies"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories, username=session["user"])


# Routing for the edit recipe page
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        # get add recipe form inputs to add to database
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "category_ingredients": request.form.get("category_ingredients"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "category_method": request.form.get("category_method"),
            "recipe_method": request.form.get("recipe_method"),
            "date_added": request.form.get("date_added"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }
        # find recipe in database and update with new form details
        mongo.db.recipe.update_one({"_id": ObjectId(recipe_id)}, {"$set": submit})

        # success message
        flash("Recipe successfully updated")
    # find the recipe in database
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories, username=session["user"])


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipe.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipies", username=session["user"]))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )