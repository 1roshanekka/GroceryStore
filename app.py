from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

# without this "render_template" we cant use ->
# return render_template("which file to load")

# only possible is return "Hello, World :P"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite :///member.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------------

# we are defining our schema


class member(db.Model):
    username = db.Column(db.String(30), primary_key = True)
    password = db.Column(db.String(30), nullable=True) 

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

@app.route("/UserLogin")

def user():
    print("--Rendering User Login Page")
    return render_template("userLogin.html")

# -------------------------------

# def userLoggedIn():
#     return render_template(); 

# Mac OSX Monterey (12.x) currently uses ports 5000 and 7000 for its Control centre hence the issue.
# Try running your app from port other than 5000 and 7000

if __name__ == "__main__":
    app.debug = True
    app.run(port=9000)
    # app.run(debug=True)
