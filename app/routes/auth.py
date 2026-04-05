from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User

# Create the auth Blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    errors = []

    
    if request.method == "POST":
        username = (request.form.get("username")or "").strip()
        email = (request.form.get("email")or "").strip()
        password = request.form.get("password")or ""
        confirm = request.form.get("confirm_password")or ""
        
        # Basic validation

        # Check if username is empty
        if not (3 <= len(username) <= 80):
            errors.append("Username must be between 3 and 80 characters")

        # Check if email is empty
        if email == "":
            errors.append("Email is required")

        # Check if password is empty
        if password == "":
            errors.append("Password is required")
        elif len(password) < 8:
            errors.append("Password must be at least 8 characters")

        # Check if passwords match
        if confirm == "":
            errors.append("Please confirm your password")
        
        elif password != confirm:
            errors.append("Passwords do not match")



        # Check if username already exists
        if errors == []:
            if User.query.filter_by(username=username).first():
                errors.append("Username already exists")
            elif User.query.filter_by(email=email).first():
                errors.append("Email already exists")
            else:    
                # If we get here, all validation has passed - create the user
                password_hash = generate_password_hash(password)
                new_user = User(username=username, email=email, password_hash=password_hash)
                db.session.add(new_user)
                db.session.commit()
                flash("Registration successful! Please log in.", "success")




        if errors:
            return render_template("register.html", errors=errors)

        return redirect(url_for("auth.login"))
    

    
    return render_template("register.html", errors=errors)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    errors = []


    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for("dashboard", name=user.username))
        else:
            errors.append("Invalid username or password")
    return render_template("login.html", errors=errors)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))