import os
import math
import re
from unicodedata import name # regex
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

app.jinja_env.globals.update(usd=usd)
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]
    """Show portfolio of stocks"""
    stocks = db.execute("SELECT symbol, sum(shares) AS shares, price, name FROM shares WHERE user_id = ? GROUP BY symbol", user_id)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash[0]["cash"]
    
    total = cash - sum([stock["price"] * stock["shares"] for stock in stocks])
    
    return render_template("index.html",stocks=stocks, cash=cash, total=total)
    
    
    
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    
    if request.method == "POST":
        date = datetime.datetime.now()
        try:    
            symbol = request.form.get("symbol")
        except: 
            return apology("Please enter a symbol", 400)
        try:
            stock = lookup(symbol.upper())
        except:
            return apology("Invalid symbol")
        try:
            price = stock["price"]
        except:
            return apology("invalid symbol price", 400)
        try:
            shares = int(request.form.get("shares"))
        except: 
            return apology("Shares must be an integer number", 400)
        
        cash = db.execute("SELECT cash FROM users WHERE id = ? ", session["user_id"])[0]["cash"]
        
        if not symbol:
            return apology("must provide symbol", 400)
        if not shares:
            return apology("must provide shares", 400)
        if price * shares > cash:
            return apology("not enough cash", 400)
        if shares <= 0:
            return apology("shares must be positive", 400)
        name = stock["name"]
        
        db.execute("INSERT INTO shares (user_id, symbol ,shares, price, date, name) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], stock["symbol"] ,shares, price, date, name)
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", price * shares, session["user_id"])
        flash("Bought!")
        return redirect("/")
    else:
        return render_template("buy.html")
        


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    
    transactions = db.execute("SELECT * FROM shares WHERE user_id = ?", user_id)
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    
    if request.method == "POST": 
        symbol = request.form.get("symbol")
        
        stock = lookup(symbol.upper())
        if not symbol:
            return apology("must provide symbol", 400)
        if not stock:
            return apology("invalid symbol", 400)
        price = float(stock["price"])
        return render_template("quoted.html", name=stock["name"], price = price, symbol = stock["symbol"])
    else:
        return render_template("quote.html")
    
    
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST": 
        # getting input from the user and storing it in variables
        name = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")  
        # checking if the user entered a username
        if not name or not password or not confirmation:
            return apology("must provide username, password, and confirmation", 400)
        if password != confirmation:
            # checking if the password and confirmation are the same
            return apology("passwords do not match", 400)
        # checking if the username is already in the database
        if len(db.execute("SELECT username FROM users WHERE username = ?", name)) != 0:
            return apology("username already exists", 400)
        
        # validate password 
        if len(password) < 8:   
            return apology("password must be at least 8 characters", 400)
        elif re.search("[0-9]", password) is None:
            return apology("password must contain at least one number", 400)
        elif re.search("[A-Z]", password) is None:
            return apology("password must contain at least one uppercase letter", 400)
        
        # hashing the password and inserting the user into the database
        db.execute("INSERT INTO users (username, hash)  VALUES (? ,?)", name ,generate_password_hash(request.form.get("password")))
        
        flash("Registered!")
        
        # redirecting the user to the home page
        return redirect("/")
    # if the user reaches the register page
    else:
        return render_template("register.html")
    
    



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        try:
            symbol = request.form.get("symbol")
        except:
            return apology("Please enter a symbol", 400)
        try:
            stock = lookup(symbol.upper())
        except: 
            return apology("Invalid symbol", 400)
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("shares must be an integer", 400)
        if not shares:
            return apology("must provide shares", 400)
        if  shares < 0:
            return apology("shares must be positive", 400)
        if shares > db.execute("SELECT SUM(shares) FROM shares WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)[0]["SUM(shares)"]:
            return apology("not enough shares", 400)
        price = stock["price"]
        total = price * shares
        updated_cash = cash + total
        name = stock["name"]
        date = datetime.datetime.now()
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updated_cash, session["user_id"])
        db.execute("INSERT INTO SHARES (user_id, symbol, shares, price, date, name) VALUES(?,?,?,?,?,?)", session["user_id"], symbol, (-1)*shares, price, date, name)
        
        flash("sold")
        return redirect("/")
        
    else:
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        stocks = db.execute("SELECT symbol FROM shares WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", session["user_id"])
        return render_template("sell.html", stocks = [stock["symbol"] for stock in stocks] )