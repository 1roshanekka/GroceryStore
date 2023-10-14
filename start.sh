# #!/bin/bash
# app="tbs"
# docker build -t ${app} .
# docker run -d -p 56733:80 \
#   --name=${app} \
#   -v $PWD:/app ${app}


#!/bin/bash

# Activate your virtual environment (if applicable)
source venv/bin/activate

# Navigate to the directory containing your Flask app
cd core

#path

# Add the directory containing the 'core' folder to the Python path
# Start the Gunicorn server
# gunicorn -b 127.0.0.1:8000 wsgi:application

# Ensure the server is listening on 0.0.0.0, and not 127.0.0.1.
gunicorn --log-level debug -b 0.0.0.0:8080 wsgi:application
# it will search for wsgi.py and find 'app' object