#!/bin/bash

# This script is the entrypoint for the Docker application container.
# It ensures the database is ready before launching the data pipeline.

set -e  # Exit immediately if a command exits with a non-zero status.

echo "Waiting for PostgreSQL database to be ready..."

# The `pg_isready` command checks the connection status of a PostgreSQL server.
# We loop until it returns a success code (0).
# The environment variables (PG_HOST, PG_PORT, etc.) are passed from the docker-compose.yml file.
while ! pg_isready -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DBNAME" -q; do
  echo "Database is not ready yet. Retrying in 2 seconds..."
  sleep 2
done

echo "✅ PostgreSQL is ready."
echo "---"

# Execute the Jupyter notebooks in sequence to run the entire data pipeline.
# `nbconvert` is used to execute the notebook from the command line.
# The `--execute` flag runs the notebook.
# The `--to notebook` flag saves the output as a new notebook file.
# The `--output` flag specifies the name of the executed notebook.

echo "STEP 1: Running Data Preprocessing Notebook..."
jupyter nbconvert --to notebook --execute notebooks/data_preprocessing.ipynb --output notebooks/data_preprocessing.executed.ipynb --allow-errors
echo "✅ Data preprocessing finished."
echo "---"

echo "STEP 2: Running Model Training Notebook..."
jupyter nbconvert --to notebook --execute notebooks/model_training.ipynb --output notebooks/model_training.executed.ipynb --allow-errors
echo "✅ Model training finished."
echo "---"

echo "STEP 3: Running Prediction Notebook..."
jupyter nbconvert --to notebook --execute notebooks/prediction.ipynb --output notebooks/prediction.executed.ipynb --allow-errors
echo "✅ Prediction finished."
echo "---"

echo "🎉🎉🎉 Project pipeline executed successfully! 🎉🎉🎉"
echo "The database is populated, and the final view 'election_data_for_bi' is ready."
echo "You can now connect to the database or run the Streamlit dashboard."

# Keep the container running if needed, e.g., for inspection.
# In this case, we just want to run the script and then the container can exit.
# tail -f /dev/null 