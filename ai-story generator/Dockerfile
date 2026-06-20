# Use an official lightweight Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file into the container
COPY ./requirements.txt /code/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the entire app directory into the container
COPY ./app /code/app

# Command to run the application module when the container starts
CMD ["python", "-m", "app.main"]