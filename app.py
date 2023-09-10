from flask import Flask
from flask import render_template
from flask import request
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

@app.route("/manager") # this targets the templates folder 
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
@app.route('/UserLogin', methods = ['GET', 'POST'])

def user():
    if(request.method =="POST"):
        # print(request.form['email'])
        submittedUsername = request.form['email'] #coming in hot from html POST request
        submittedPassword = request.form['passkey']
        print("******-------posted--------******")

        # new_user = registry(username="aaass@gmail.com", password="qwertsssy12345", dateCreated=current_dat  etime)
        new_user = registry(username=submittedUsername, password=submittedPassword, dateCreated=current_datetime)
        db.session.add(new_user)
        db.session.commit() 
        print("now reloading userLogin.html")

        
    
    print ("User added successfully!")
    print("--Rendering User Login Page")
    return render_template("userLogin.html")




# -------------------------------

# !! Maintain level of integrity as the code blocks execute serially

# Make sure to include the app context when working with the database
with app.app_context():
    # Create the database tables
    db.create_all()

    # idk why not to use this below code 
    # app.app_context().push() 


# -------------------------------
@app.route("/users") 

def showUsers():
    print("--Rendering Manager Login Page")


    allUsers = registry.query.all()
    print(allUsers)   
    # to the console

    return render_template("users.html", fullDB=allUsers) # when /users page is requested render the user page and also pass the database as fullDB

# -------------------------------

# def userLoggedIn():
#     return render_template(); 

# Mac OSX Monterey (12.x) currently uses ports 5000 and 7000 for its Control centre hence the issue.
# Try running your app from port other than 5000 and 7000

if __name__ == "__main__":
    app.debug = True
    app.run(port=9000)
    # app.run(debug=True)
