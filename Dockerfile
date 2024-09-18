# Use an official Python runtime as a base image
FROM python:3.9-slim

# Install dependencies
RUN pip install flask numpy

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port Flask runs on
EXPOSE 5000

# Set the working directory in the container
WORKDIR /app

# Command to run the Flask app
CMD ["python3", "app.py"]
