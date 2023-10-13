# wsgi.py for production 
from core.app import app


# wsgi.py is a Python file that serves as the entry point for the WSGI server, which is responsible for handling HTTP requests and passing them on to the Flask application.
if __name__ == "__main__":
    app.run()

import sys
import os

# Add the path to your Flask application
path = '/home/username/mysite'
if path not in sys.path:
    sys.path.append(path)

# Import your Flask application
from core.app import app as application  # Assuming your Flask app object is named 'app'

# Optional: Set environment variables or configurations here, if needed

# Optional: Configure logging or other settings here, if needed

# IMPORTANT: Do not call app.run() here, as it will interfere with the WSGI server
