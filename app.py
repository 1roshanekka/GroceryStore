from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
current_datetime = datetime.now()
# without this "render_template" we cant use ->
# return render_template("which file to load")

# only possible is return "Hello, World :P"

# -------------------------------
# create the extension
db = SQLAlchemy()

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///member.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialize the app with the extension
db.init_app(app)

# direct init
# db = SQLAlchemy(app)
#this above 'db' we call

# Make sure to include the app context when working with the database
with app.app_context():
    # Create the database tables
    db.create_all()

# -------------------------------

def create_app():
    with app.app_context():
        db.create_all()
    return app


# we are defining our schema


class member(db.Model):
    username = db.Column(db.String(30), primary_key = True)
    password = db.Column(db.String(30), unique=False, nullable=False) 

    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.username} - {self.password}"


# -------------------------------


@app.route("/") # this targets the templates folder 
# "/" means it is by default looking for index.html unless specified, like here its managerLogin.html

def manager():
    print("--Rendering Manager Login Page")
    return render_template("managerLogin.html")

# -------------------------------

# @app.route("/UserLogin")

# def user():
#     print("--Rendering User Login Page")
#     return render_template("userLogin.html")

# ``` only routing was done uptill now, to post data and to get data we need to configure in the flask app

# -------------------------------


# @app.route("/UserLogin", methods=['GET', 'POST'])
@app.route("/UserLogin")

def user():
    users = member(username="1roshanekka@gmail.com", password="qwerty12345" ,dateCreated=current_datetime)
    
    db.session.add(users)    
    db.session.commit()

    print("--Rendering User Login Page")
    return render_template("userLogin.html")


# -------------------------------
@app.route("/users") 

def showUsers():
    print("--Rendering Manager Login Page")

    allUsers = member.query.all()
    print(allUsers)
    # to the console

    return render_template("users.html", fullDB=allUsers)

# -------------------------------

# def userLoggedIn():
#     return render_template(); 

# Mac OSX Monterey (12.x) currently uses ports 5000 and 7000 for its Control centre hence the issue.
# Try running your app from port other than 5000 and 7000

if __name__ == "__main__":
    app.debug = True
    app.run(port=9000)
    # app.run(debug=True)
