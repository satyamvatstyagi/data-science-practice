# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables to ensure Python runs in unbuffered mode and doesn't write .pyc files
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's source code into the container
COPY . .

# Expose the port on which the FastAPI app will run
EXPOSE 8080

# Set the command to run the app when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
