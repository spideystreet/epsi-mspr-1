# 🗳️ Electoral Results Predictor & Interactive Dashboard

## ✨ Overview
This project aims to predict the results of French elections by department using machine learning techniques. The goal is not only to predict but to build a **robust and reproducible data pipeline** that feeds an **interactive dashboard** for visualizing historical results and future predictions.

## 🚀 Our Workflow Pipeline
The project is structured around three sequential Jupyter notebooks that form a complete and automated pipeline, from raw data to the final result.

1.  `notebooks/data_preprocessing.ipynb`
    *   **Role:** Prepares and cleans the data.
    *   **Actions:**
        *   Aggregates raw data from various CSV files.
        *   Loads the data into a PostgreSQL database.
        *   Performs a temporal split (train < 2024, test = 2024).
        *   Saves the processed datasets and transformation tools (`preprocessor`, `label_encoder`).

2.  `notebooks/model_training.ipynb`
    *   **Role:** Trains and selects the best model.
    *   **Actions:**
        *   Tests several algorithms (e.g., Random Forest).
        *   Evaluates them on the 2024 test set.
        *   **Automatically saves the best-performing model.**

3.  `notebooks/prediction.ipynb`
    *   **Role:** Generates final predictions and prepares data for BI.
    *   **Actions:**
        *   Loads the best model.
        *   Predicts the winners for "2027".
        *   Creates a final table, `election_results_for_bi`, in the database, combining all historical and future results for easy analysis.

## 📊 Visualization with the Dashboard
Once the data pipeline has been executed, a Streamlit dashboard is available to explore the results. It allows you to:
-   Visualize the winning parties by department on an interactive map of France.
-   Filter results by year, including **predictions for 2027**.
-   View aggregated statistics and detailed data for each year.

## 📂 File Structure
```
.
├── assets/                 # Project assets (images, diagrams)
├── data/                   # Raw datasets (.csv, .geojson)
├── database/               # Saved processing artifacts
│   ├── preprocessor_X.joblib # Saved data transformation tool
│   └── label_encoder_y.joblib  # Saved target encoder
├── models/
│   └── random_forest_predictor.joblib # Best saved prediction model
├── notebooks/
│   ├── data_preprocessing.ipynb   # Notebook for data prep
│   ├── model_training.ipynb     # Notebook for model training
│   └── prediction.ipynb         # Notebook for generating predictions
├── streamlit/
│   └── dashboard.py      # Code for the interactive dashboard
├── .env.example          # Example file for environment variables
├── .env                  # Configuration file (ignored by git)
├── .gitignore            # Files and directories ignored by git
├── Dockerfile            # Defines the application's environment
├── docker-compose.yml    # Orchestrates Docker services
├── run_project.sh        # Execution script for the pipeline
├── README.md             # This file
└── requirements.txt      # Project dependencies
```

## 📊 Data Used
Our dataset includes:
- Historical electoral results (turnout, registered voters, votes per party).
- Socio-economic indicators (unemployment, poverty).
- Social data (crime, immigration).

## 🐳 Installation and Launch

### Prerequisites
- [Docker](https://www.docker.com/get-started) & [Docker Compose](https://docs.docker.com/compose/install/)

### Step 1: Run the Data Pipeline
This step uses Docker to create the database, process the data, and train the model.
1.  **Clone the repository** and navigate into the project folder.
2.  **Configure your environment:**
    -   Create a `.env` file by copying the `.env.example` template.
    -   Fill in the environment variables (`PG_USER`, `PG_PASSWORD`, `PG_DBNAME`, `PG_PORT`).
3.  **Launch the project:**
    -   Open a terminal at the project root and run the following command:
      ```bash
      docker-compose up --build
      ```
    -   This single command will build and start the containers. The `run_project.sh` script will automatically execute to run the entire data pipeline.
    -   **Keep this terminal open.**

### Step 2: Launch the Interactive Dashboard
Once the pipeline in Step 1 is complete (you will see the logs of the notebook executions), you can launch the dashboard.
1.  **Install dependencies** (in a **new terminal**):
    -   It is recommended to create a Python virtual environment.
      ```bash
      python3 -m venv venv
      source venv/bin/activate  # On macOS/Linux
      # venv\Scripts\activate   # On Windows
      ```
    -   Install the required libraries:
      ```bash
      pip install -r requirements.txt
      ```
2.  **Launch the dashboard:**
    ```bash
    streamlit run streamlit/dashboard.py
    ```
    -   The dashboard will be accessible in your browser at the address indicated (usually `http://localhost:8501`).

### Stopping the Services
-   To stop the dashboard, press `Ctrl + C` in its terminal.
-   To stop the database and application containers, go back to the Docker terminal, press `Ctrl + C`, and then run:
      ```bash
      docker-compose down
      ```

## 📄 License
This project is licensed under the terms of the LICENSE file.

## 👥 The Team
- [@hicham](https://github.com/spideystreet)
- [@amine](https://github.com/testt753)
- [@wassim](https://github.com/Wassim38)

## 💬 Feedback
Have suggestions or questions? Feel free to open an issue or contact us directly! 