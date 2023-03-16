# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django application
EXPOSE 8000

# Run the command to start the Django server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD sh -c 'python manage.py runserver 0.0.0.0:8000 && python manage.py makemigrations && python manage.py migrate'