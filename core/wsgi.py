# wsgi.py for production 
# from core.app import app


# # wsgi.py is a Python file that serves as the entry point for the WSGI server, which is responsible for handling HTTP requests and passing them on to the Flask application.
# if __name__ == "__main__":
#     app.run()
#---------------------------------------------------

# this was for local


# # for gunicorn
# import sys
# import os

# # Add the path to your Flask application
# path = os.path.dirname(os.path.abspath('/core/'))  # Replace with your actual path
# if path not in sys.path:
#     sys.path.append(path)
# print(path)
import sys

import os

# Add the directory containing the 'core' folder to the Python path
base_dir = os.path.dirname(os.path.abspath(__file__))
core_dir = os.path.join(base_dir, 'core')
sys.path.append(core_dir)
print(core_dir)
# Import your Flask application
from app import app

# Create an application callable for the WSGI server
application = app

# Import your Flask application
# from .core.app import app as application  # Assuming your Flask app object is named 'app'
# from run import app
# from core.app import app as application