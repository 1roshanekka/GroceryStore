from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

from flask import session
from flask import g
from flask import url_for
from flask import flash
from flask_migrate import Migrate
from sqlalchemy.orm import relationship

# from flask import flask_login

import os

# create the app
app = Flask(__name__)

#app secret key
# (hard coded)
# session is enrypted in server

app.secret_key = "admin90"





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

app.config['SQLALCHEMY_BINDS'] = {
    'store': "sqlite:///store.db",
    'item' : "sqlite:///store.db",
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)

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

# we are defining our schema of sales item
class category(db.Model):
    __bind_key__ = 'store'
    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(50), nullable=False)

    # products = db.relationship('product', backref='Category', lazy=True)

    # itemName = db.Column(db.String(255), primary_key=False, nullable=True)

    # itemName = db.Column(db.String, primary_key=True)
    # unit = db.Column(db.Integer, nullable=True)
    # rate = db.Column(db.Integer, nullable=True)
    # quantity = db.Column(db.Integer, nullable=True)
    # checkbox = db.Column(db.Integer, nullable=True)  
    #as we are declaring directly, we should remove unique as it will coflict in the database

    # item = relationship('product', backref='category', lazy=True)

    def __repr__(self) -> str:
        return f"Category('{self.categoryName}')"
        return f"{self.categoryName}"
        
    

# -------------------------------
# we are defining our schema of sales item
class product(db.Model):
    __bind_key__ = 'store'

    id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(50), nullable=False)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    # category = db.relationship('Category', backref=db.backref('products', lazy=True))
    # category = db.relationship('Category', backref=db.backref('items', lazy=True))
    # itemName = db.Column(db.String, primary_key=True)
    # unit = db.Column(db.Integer, nullable=True)
    # rate = db.Column(db.Integer, nullable=True)
    # quantity = db.Column(db.Integer, nullable=True)
    # checkbox = db.Column(db.Integer, nullable=True)  
    #as we are declaring directly, we should remove unique as it will coflict in the database
      
    def __repr__(self) -> str:
        return f"Product('{self.itemName}')"
        return f"{self.itemName}"
# -------------------------------

# to get database
@app.route("/adminCockpit", methods=['GET', 'POST'])

def bossPanel():

    if (request.method=='GET'):
        print("--loading DB--")
        return redirect('/usersDataBase')
    else:
        return redirect("/manager")
# -------------------------------
# to get items on sale and panel
@app.route("/adminCockpit_option1-sales", methods=['GET', 'POST'])

def sales_forAdmin():

    if (request.method=='GET'):
        print("--loading sales--")
        # return redirect('/sales')
        # this was not passing db when it was loaded first 

        
        return redirect('/updatedSales')
    else:
        return redirect("/manager")
# -------------------------------
@app.route("/adminCockpit_option2-summary", methods=['GET', 'POST'])

def summary_forAdmin():

    if (request.method=='GET'):
        print("--loading DB--")
        return redirect('/summary')
    else:
        return redirect("/manager")
    
# -------------------------------

@app.route






# login_admin = LoginManager()
@app.route("/admin", methods=['GET', 'POST']) # this targets the templates folder 
# "/" means it is by default looking for index.html unless specified, like here its managerLogin.html

def admin():

        # if request=='POST' : will not work
        if (request.method=='POST') :
            session.pop('user', None) # drops the current session before you submit a request through POST

            # fetch from the form present in manager login page
            owner = request.form['email']
            owner_passkey = request.form['passkey']
            print(owner, owner_passkey)

            if (owner == '1roshanekka@gmail.com' and owner_passkey == 'qwerty12345'):
                session['user'] = owner
                # return redirect( url_for('showUsers') ) 
                # or 
                # flash("Login Successfull", 'info')
                print("--gotcha homie--")
                print("--Login Successfull--")

                # if user in session

                # if login is success
                return redirect('/adminSecured')

                return render_template('adminPanel.html', user = owner)

                return redirect('/usersDataBase')
            
            elif (owner!='1roshanekka@gmail.com'):
                print ('Wrong Username')
                flag = 0
                # flash("Wrong Username", 'info')

            elif(owner=='1roshanekka@gmail.com' and owner_passkey != 'qwerty12345'):
                print ('Wrong Password')
                flag = 1
                # flash("Wrong Password", 'info')
            else:
                print ('Wrong Credentials')
                flag = 2
                # flash("Wrong Credentials", 'info')
                
            print('--who tf are you--')
            # return redirect('/manager', param = flag )
            # if you probably want to pass params value || but this will take route variable
            # redirect(url_for('index', logout=logout))

            # return redirect( url_for('managerFunc', params = flag))
        
            # Redirects: Depending on the outcome of the validation, it redirects to different routes. The managerFunc route is called with params set to the value of flag.

            # to pass variable use render template
            return render_template('managerLogin.html', params = flag)


            # return render_template('users.html') this will return empty DB as we dont pass DB with the render template
        # elif request=='GET':
        #     return render_template("/manager.html")
        else:
            if "user" in session:
                return redirect(url_for('adminLoggged'))
            print('--access denied--')
            return render_template("/managerLogin.html") # same as redirect('/manager')

    # return render_template("/")
    # or
    # return redirect(url_for("login"))

    
    # we cant access this as to access the maanger login page we need to pass POST request other wise accessing through link or route will lead to login page


    # return render_template("/") for html link not route link
    # url_for is helper to find the route when the function name is passed 
    # but it has to be used with redirect
# -------------------------------

@app.route("/adminSecured", methods=['GET', 'POST']) 

def adminLogged():
    if "user" in session:
        
        user = session["user"]

        print(user)

        return render_template('adminPanel.html', user = user)

        return f"<h1>{user}</h1>"
    else:
        print('--admin not in session babu --')
        return redirect("/manager")

# -------------------------------

@app.route("/adminRetired", methods=['GET', 'POST']) 

def adminLoggedOut():
    session.pop('user', None)
    print("--Admin has been logged out--")
    return redirect('/manager')

# -------------------------------
#!! adds category to DATABASE which has binds to --store--
@app.route("/addCategory", methods=['GET', 'POST'])

def khata():

    if (request.method=='POST') :

        submittedCategory = request.form['categoryNameform']
        print(submittedCategory, '*****-----posted-----*****') 

        # ! here categoryName from category class is targetted
        newCategory = category(categoryName=submittedCategory)
        db.session.add(newCategory)
        db.session.commit()

        print(submittedCategory, "category added successfully !")
    else:
        print('--loading back into sales--')
        return redirect('/updatedSales')

    print("--rendering admin panel for Sales")
    return redirect('/updatedSales')


# -------------------------------
#!! adds item to DATABASE which has binds to --store--
@app.route("/addItems", methods=['GET', 'POST'])

def samaan():

    if (request.method=='POST') :

        submittedItem = request.form['itemNameForm']
        print(submittedItem, '*****-----posted-----*****') 

        # ! here itemName from product class is targetted
        category_id = request.form['category_id']

        newItem = product(itemName=submittedItem, category_id=category_id)
        db.session.add(newItem)
        db.session.commit()

        print(submittedItem, "Item added successfully !")
    else:
        print('--loading back into sales--')
        return redirect('/updatedSales')

    print("--rendering admin panel for Sales")
    return redirect('/updatedSales')


# -------------------------------
#!! deletes item from DATABASE which has binds to --store--
@app.route("/deleteItem/<int:id>")  # what if you want to pass username, should it be the primary key

def deleteItem(id): 
    print("--deleting--")

    # slno from the database must match with the serial_no that we pass to delete
    particularItem = product.query.filter_by(id=id).first()
    db.session.delete(particularItem) 
    db.session.commit() # do not forget to commit

    updatedDB = registry.query.all()

    print(particularItem)   

    # this Flask's redirect function does not accept additional arguments like this. Instead, you should pass data using query parameters.
    # return redirect("/users", fullDB = updatedDB) 

    # this is working
    # return redirect(f"/users?fullDB={updatedDB}")
    return redirect('/updatedSales')


    return render_template("users.html", fullDB = updatedDB)  # fullDB is the variable taken by jinja template
    
    # to the console
    return render_template("users.html", fullDB = updatedDB)  # fullDB is the variable taken by jinja template
    return render_template("users.html", fullDB=allUsers) # when /users page is requested render the user page and also pass the database as fullDB


# -------------------------------

@app.route("/editItem/<int:id>")  # what if you want to pass username, should it be the primary key

def editItem(id): 
    print("--editing Item--")

    # display modal

    
    return redirect('/updatedSales')

# -------------------------------

@app.route("/deleteCategory/<int:id>")  # what if you want to pass username, should it be the primary key

def deleteCategory(id): 
    print("--deleting Category--")

    # slno from the database must match with the serial_no that we pass to delete
    particularCategory = category.query.filter_by(id=id).first()
    db.session.delete(particularCategory) 
    db.session.commit() # do not forget to commit

    updatedDB = registry.query.all()

    print(particularCategory)  
    return redirect('/updatedSales')

# -------------------------------
# @app.route("/addCategory", methods=['GET', 'POST'])

# def section():
#     if (request=="POST") :


           



# -------------------------------

@app.route('/updatedSales')

def salesNewList():

    user = session["user"]

    print('--loading new list from category DB--')

    allCategory = category.query.all()
    allItems = product.query.all()
    print(allCategory)
    print(allItems)

    # return redirect('addItems', totalStocks=allCategory)
    return render_template("saleAdmin.html", totalCategory=allCategory, totalItems=allItems, user=user)



# -------------------------------

# This route should expect a parameter named params.
# @app.route('/managerFunc/<int:params>')

@app.route("/manager", methods=['GET', 'POST']) # this targets the templates folder 
# "/" means it is by default looking for index.html unless specified, like here its managerLogin.html
def managerFunc():

        # if request=='POST' : will not work
        # if (request.method=='POST') :
        #     session.pop('user', None) # drops the current session before you submit a request through POST

        #     # fetch from the form present in manager login page
        #     owner = request.form['email']
        #     owner_passkey = request.form['passkey']
        #     print(owner, owner_passkey)

        #     if (owner == 'a@gmail.com' and owner_passkey == 'a'):
        #         # session.['user'] = request.form['username']
        #         print("--Rendering Manager Login Page")
        #         # return redirect( url_for('showUsers') ) 
        #         # or 
        #         return redirect('/usersDataBase')

                # return render_template('users.html') this will return empty DB as we dont pass DB with the render template
        # elif request=='GET':
        #     return render_template("/manager.html")
        return render_template("/managerLogin.html")

    # return render_template("/")
    # or
    # return redirect(url_for("login"))

    
    # we cant access this as to access the maanger login page we need to pass POST request other wise accessing through link or route will lead to login page


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
@app.route('/register', methods = ['GET', 'POST'])

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
        return render_template("userLogin.html")

    elif(request.method == "GET"):
        # session['user_info'] = {'email': request.form['email'], 'password': request.form['passkey']}

        # thisSessionEmail = session['user_info']['email']
        # thisSessionPassword = session['user_info']['password']

        return render_template("register.html")




    print("--Rendering User Login Page")
    return render_template("userLogin.html")




# -------------------------------
@app.route('/regRoute')
def routeRegistration():
    return render_template("register1.html")
# @app.route("/UserLogin", methods=['GET', 'POST'])
@app.route('/userlogin', methods = ['GET', 'POST'])

def login():
    if(request.method =="POST"):
        session.pop('customer', None)
        
        print('a post request')
        login_username = request.form["email"]
        login_password = request.form["passkey"]
        print(login_username, login_password)

        E = registry.query.filter_by(username=login_username).first()
        print(E)
        EP = registry.query.filter_by(username=login_username, password=login_password).first()
        print(EP)

        # if( E==True and EP==False):
        #     print("User in Database but Wrong Password")
        # else:
        #     if check :
        #         session['customer'] = login_username  # making dictionary key

        #         print('--login successful--')
        #         return redirect('/userSecured')
                
        #     else:
        #         message = "Wrong Credentials"
        #         print('--login failed-- --wrong password--')
        #         return redirect('/user')


        if EP is not None:
            session['customer'] = login_username  # making dictionary key
            print("--gotcha homie--")
            print("--User Login Successfull--")

            print('--login successful--')
            return redirect('/userSecured')
                
        print("now reloading userLogin.html")
        return redirect('/user')
    else:
        print('not a POST request')
        if "customer" in session:
            return redirect('/userSecured')
        
        print('--access denied--')
        return render_template("/userLogin.html") 
    
    # elif(request.method == "GET"):
    #     return render_template("userLogin.html")
    
    # print(" error userLogin.html")
    # return redirect('/')
# -------------------------------


@app.route("/userSecured", methods=['GET', 'POST']) 

def userLogged():
    if "customer" in session:
        
        customer = session["customer"]

        print(customer)

        return render_template('baseShop.html', customer = customer)

        return f"<h1>{user}</h1>"
    else:
        print('--not in session babu :( --')
        return redirect("/user")
# -------------------------------

@app.route("/userRetired", methods=['GET', 'POST']) 

def userLoggedOut():
    session.pop('customer', None)
    print("--customer has been logged out--")
    return redirect('/user')

# -------------------------------
# ! this routes and renders the userLogin html
@app.route("/user", methods=['GET', 'POST']) # this targets the templates folder 
# "/" means it is by default looking for index.html unless specified, like here its managerLogin.html
def userFunc():
        print('sent to /user route')
        return render_template("/userLogin.html")

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
    user = session.get('user')

    print("--Rendering DataBase")


    allUsers = registry.query.all()
    print(allUsers)   
    # to the console

    return render_template("users.html", fullDB=allUsers, user=user) # when /users page is requested render the user page and also pass the database as fullDB

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

@app.route('/sales')
def getSalesforAdmin() :
    return render_template('saleAdmin.html')

# -------------------------------
@app.route('/summary')
def getSummaryforAdmin() :
    user = session.get('user')
    return render_template('summaryAdmin.html', user=user)

# -------------------------------
@app.route('/agreements')
def getAgreements() :
    # user = session.get('user')
    return render_template('agreements.html')
# -------------------------------
@app.route('/privacy')
def getPrivacy() :
    # user = session.get('user')
    return render_template('privacy.html')
# -------------------------------
@app.route('/return')
def getReturn() :
    # user = session.get('user')
    return render_template('return.html')
# -------------------------------
@app.route('/warranty')
def getWarranty() :
    # user = session.get('user')
    return render_template('warranty.html')
# -------------------------------
@app.route('/help')
def getHelp() :
    # user = session.get('user')
    return render_template('help.html')
# -------------------------------
@app.route('/account')
def getAccount() :
    # user = session.get('user')
    return render_template('account.html')
# -------------------------------
@app.route('/terms')
def getTerms() :
    # user = session.get('user')
    return render_template('terms.html')
# -------------------------------
@app.route('/about')
def getAbout() :
    # user = session.get('user')
    return render_template('about.html')
# -------------------------------
@app.route('/shop')
def getShop() :
    # user = session.get('user')
    customerLogged = session.get('customer')
    return render_template('baseShop.html',customerLogged=customerLogged)
# -------------------------------

@app.route('/')
def index() :
    return render_template('index.html')

# -------------------------------


# def customerLoggedLoggedIn():
#     return render_template(); 

# Mac OSX Monterey (12.x) currently uses ports 5000 and 7000 for its Control centre hence the issue.
# Try running your app from port other than 5000 and 7000

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    # app.run(debug=True)
 