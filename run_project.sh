#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Wait for the PostgreSQL database to be ready before proceeding.
# It uses the environment variables from the .env file to connect.
echo "Waiting for PostgreSQL to be ready..."
until PGPASSWORD=$PG_PASSWORD psql -h "$PG_HOST" -U "$PG_USER" -d "$PG_DBNAME" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres is up - starting notebook execution."

# Execute the Jupyter notebooks in sequence.
# The output will be saved to new files with the '.executed.ipynb' suffix.
echo "Running data preprocessing notebook..."
jupyter nbconvert --to notebook --execute notebooks/data_preprocessing.ipynb --output data_preprocessing.executed.ipynb

echo "Running model training notebook..."
jupyter nbconvert --to notebook --execute notebooks/model_training.ipynb --output model_training.executed.ipynb

echo "Running prediction notebook..."
jupyter nbconvert --to notebook --execute notebooks/prediction.ipynb --output prediction.executed.ipynb

echo "Project execution finished successfully. Executed notebooks are available." 