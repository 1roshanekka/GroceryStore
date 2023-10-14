# ! uncomment below for using base ubuntu docker image
# # Use Ubuntu as the base image
# FROM ubuntu:20.04

# # Set the working directory in the container
# WORKDIR /app

# # Update and install necessary packages
# RUN apt-get install -y python3 python3-pip

# # Copy the current directory contents into the container at /app
# ADD . /app

# # Install Flask and other necessary packages
# RUN pip3 install Flask

# # Make port 8080 available to the world outside this container
# EXPOSE 8080

# # Define environment variable
# ENV NAME World

# # Run app.py when the container launches
# CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:application"]





# !uncomment below for using base python docker image

# Use a Python base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port your app runs on
EXPOSE 8080

# Define the command to start your Flask app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:application"]