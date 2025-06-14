# Use an official Python runtime as a parent image
# Using python:3.11-slim as it is a good balance of size and functionality.
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and to run in unbuffered mode.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies. postgresql-client is needed for the `psql` command in `run_project.sh` to check DB connection.
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container.
COPY . .

# Make the run script executable. This script will be created in the next step.
RUN dos2unix run_project.sh && \
    chmod +x run_project.sh
# The command to run when the container launches.
CMD ["./run_project.sh"] 