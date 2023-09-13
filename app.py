from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

from flask import session
from flask import g
from flask import url_for
# from flask import flask_login

import os

# create the app
app = Flask(__name__)

#app secret key
# (hard coded)
# session is enrypted in server

app.secretkey = "admin90"





from datetime import datetime
current_datetime = datetime.now()
# without this "render_template" we cant use ->
# return render_template("which file to load")

# only possible is return "Hello, World :P"

# -------------------------------
# create the extension
db = SQLAlchemy()

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///members.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#import database after you instantiate your db.

# db = SQLAlchemy()  # create the extension
# initialize the app with the extension
db.init_app(app)

# we will do this manually by db.create_all() ----- its depricated IG 

# no-use

# def create_app():
#     app = Flask(__name__)
#     db.init_app(app)
#     return app


# def create_app():
#     app = Flask(__name__)

#     with app.app_context():
#         db.create_all()
#         # init_db()
#         # app.app_context().push()

#     return app

# direct init
# db = SQLAlchemy(app)
#this above 'db' we call

# -------------------------------

# we are defining our schema
class registry(db.Model):
    slno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False) 

    #as we are declaring directly, we should remove unique as it will coflict in the database

    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.slno} - {self.username}"

# -------------------------------


# login_admin = LoginManager()


# -------------------------------

@app.route("/manager", methods=['GET', 'POST']) # this targets the templates folder 
# "/" means it is by default looking for index.html unless specified, like here its managerLogin.html

def manager():

    if request=='POST' :
        session.pop('user', None) # drops the current session before you submit a request through POST

        # fetch from the form present in manager login page
        owner = request.form("email")
        owner_passkey = request.form("password")

        if owner == '1roshanekka@gmail.com' and owner_passkey == 'Norah69':
            # session.['user'] = request.form['username']
            print("--Rendering Manager Login Page")
            return redirect( url_for('usersDataBase') )
        
    # return render_template("/")
    # or
    return redirect(url_for("login"))

    we cant access this as to access the maanger login page we need to pass POST request other wise accessing through link or route will lead to login page


    # return render_template("/") for html link not route link
    # url_for is helper to find the route when the function name is passed 
    # but it has to be used with redirect


# -------------------------------



# @app.route("/UserLogin")

# def user():
#     print("--Rendering User Login Page")
#     return render_template("userLogin.html")

# ``` only routing was done uptill now, to post data and to get data we need to configure in the flask app

# -------------------------------


# @app.route("/UserLogin", methods=['GET', 'POST'])
@app.route('/UserLogin', methods = ['GET', 'POST'])

def registerUser():
    if(request.method =="POST"):
        # print(request.form['email'])
        submittedUsername = request.form['email'] #coming in hot from html POST request
        submittedPassword = request.form['passkey']
        print("******-------posted--------******")

        # new_user = registry(username="aaass@gmail.com", password="qwertsssy12345", dateCreated=current_dat  etime)
        new_user = registry(username=submittedUsername, password=submittedPassword, dateCreated=current_datetime)
        db.session.add(new_user)
        db.session.commit() 
        print ("User added successfully!")
        print("now reloading userLogin.html")

    print("--Rendering User Login Page")
    return render_template("userLogin.html")




# -------------------------------

# @app.route("/UserLogin", methods=['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])

def login():
    if(request.method =="POST"):
        username_in = request.form("username")

        session['user'] = username_in  # making dictionary key
        print("now reloading userLogin.html")
        return render_template( url_for("user"), person = user)
        
    
    print ("User added successfully!")
    print("--Rendering User Login Page")
    return render_template("userLogin.html")

# -------------------------------

# @app.route("/UserLogin", methods=['GET', 'POST'])
# @app.route('/user')

# def user(): 
#     if "username_in" in session:
#         user_got = session["username_in"]
#         return f"<h1>{user_got}</h1>"

#         session['user'] = user
#         print("now reloading userLogin.html")
#         return render_template( url_for("user"), person = user)
#     else: # no use in session
#         return redirect(url_for("login"))
    
#     print ("User added successfully!")
#     print("--Rendering User Login Page")
#     return render_template("userLogin.html")



# !! Maintain level of integrity as the code blocks execute serially

# Make sure to include the app context when working with the database
with app.app_context():
    # Create the database tables
    db.create_all()

    # idk why not to use this below code 
    # app.app_context().push() 


# -------------------------------
@app.route("/usersDataBase") 

def showUsers():
    print("--Rendering DataBase")


    allUsers = registry.query.all()
    print(allUsers)   
    # to the console

    return render_template("users.html", fullDB=allUsers) # when /users page is requested render the user page and also pass the database as fullDB

# -------------------------------
# Creating a CRUD Operation

# the above was read and create was from the login page

# This is update function

@app.route("/update") 

def update():
    print("--updating--")


    allUsers = registry.query.all()
    print(allUsers)   
    # to the console

    return render_template("users.html", fullDB=allUsers) # when /users page is requested render the user page and also pass the database as fullDB

# -------------------------------

@app.route("/delete/<int:slno>")  # what if you want to pass username, should it be the primary key

def delete(slno): 
    print("--deleting--")

    # slno from the database must match with the serial_no that we pass to delete
    particularUser = registry.query.filter_by(slno=slno).first()
    db.session.delete(particularUser) 
    db.session.commit() # do not forget to commit

    updatedDB = registry.query.all()

    print(particularUser)   

    # this Flask's redirect function does not accept additional arguments like this. Instead, you should pass data using query parameters.
    # return redirect("/users", fullDB = updatedDB) 

    # this is working
    # return redirect(f"/users?fullDB={updatedDB}")

    return render_template("users.html", fullDB = updatedDB)  # fullDB is the variable taken by jinja template
    
    # to the console
    return render_template("users.html", fullDB = updatedDB)  # fullDB is the variable taken by jinja template
    return render_template("users.html", fullDB=allUsers) # when /users page is requested render the user page and also pass the database as fullDB





# -------------------------------

@app.route('/')
def index() :
    return render_template('index.html')

# -------------------------------


# def userLoggedIn():
#     return render_template(); 

# Mac OSX Monterey (12.x) currently uses ports 5000 and 7000 for its Control centre hence the issue.
# Try running your app from port other than 5000 and 7000

if __name__ == "__main__":
    app.debug = True
    app.run(port=9000)
    # app.run(debug=True)
