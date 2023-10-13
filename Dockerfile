# FROM un

# WORKDIR /app
# COPY . /app

# RUN pip install -r requirements.txt
# EXPOSE 3000
# ENV NAME World

# # CMD python ./app.py
# CMD ["python", "app.py"]

# FROM ubuntu:16.04
# RUN apt-get update -y
# RUN apt-get install python -y
# RUN apt-get install python-pip -y
# RUN pip install flask
# COPY . /app
# ENTRYPOINT FLASK_APP=/home/app.py flask run --host=0.0.0.0

# Use Ubuntu as the base image
FROM ubuntu:20.04

# Set the working directory in the container
WORKDIR /app

# Update and install necessary packages
RUN apt-get install -y python3 python3-pip

# Copy the current directory contents into the container at /app
ADD . /app

# Install Flask and other necessary packages
RUN pip3 install Flask

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "app.py"]
