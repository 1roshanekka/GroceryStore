from flask import Flask
from flask import render_template

# without this rennder_template we cant use ->
# return render_template("which file to load")

# only possible is return "Hello, World :P"

app = Flask(__name__)

@app.route("/") # this targets the templates folder 

def manager():
    return render_template("managerLogin.html")
def user():
    return render_template("userLogin.html")

# def userLoggedIn():
#     return render_template(); 

# Mac OSX Monterey (12.x) currently uses ports 5000 and 7000 for its Control centre hence the issue.
# Try running your app from port other than 5000 and 7000

if __name__ == "__main__":
    app.debug = True
    app.run(port=6969)
    # app.run(debug=True)
