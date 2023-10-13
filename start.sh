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

# Start the Gunicorn server
gunicorn -b 127.0.0.1:8000 wsgi:app
