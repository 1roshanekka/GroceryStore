# wsgi.py for production 
from core.app import app


# wsgi.py is a Python file that serves as the entry point for the WSGI server, which is responsible for handling HTTP requests and passing them on to the Flask application.
if __name__ == "__main__":
    app.run()

#---------------------------------------------------
