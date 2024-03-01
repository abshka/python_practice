# Use an official Python runtime as a base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application files into the container
COPY . /app

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define a command to run the Flask application
CMD ["python", "app.py"]
