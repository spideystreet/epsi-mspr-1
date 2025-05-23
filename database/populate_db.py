'''
Script to populate the SQLite database from CSV files.
'''
import sqlite3
import pandas as pd
import os

# Define file paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BASE_DIR, "database", "ELECTIONS.db")
SCHEMA_FILE = os.path.join(BASE_DIR, "database", "schema.sql")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Mapping of CSV files to table names and their expected columns
TABLE_CONFIG = {
    "UNEMPLOYMENT_DATA": {  # Uppercase table name
        "csv_file": "2017_2024_CHOMAGE_prepared.csv",
        "columns_map": {
            # CSV_Col_Name: SQL_COL_NAME (UPPERCASE)
            "ANNEE": "YEAR",
            "DEPARTEMENT_CODE": "DEPARTMENT_CODE",
            "DEPARTEMENT": "DEPARTMENT",
            "TX_CHOMAGE": "UNEMPLOYMENT_RATE", 
        },
    },
    "CRIME_DATA": {  # Uppercase table name
        "csv_file": "2017_2024_CRIMINALITE_prepared.csv",
        "columns_map": {
            "ANNEE": "YEAR",
            "DEPARTEMENT_CODE": "DEPARTMENT_CODE",
            "DEPARTEMENT": "DEPARTMENT",
            "NB_VICTIMES": "NUMBER_OF_VICTIMS", 
        },
    },
    "ELECTION_DATA": {  # Uppercase table name
        "csv_file": "2017_2024_ELECTIONS_prepared.csv", 
        "columns_map": {
            "ANNEE": "YEAR",
            "DEPARTEMENT_CODE": "DEPARTMENT_CODE",
            "DEPARTEMENT": "DEPARTMENT",
            "WINNER": "WINNER",
            "NB_INSCRITS": "REGISTERED_VOTERS",
            "NB_VOTANTS": "VOTERS",
            "PARTI_1": "PARTY_1",
            "VOIX_1": "VOTES_1",
            "PARTI_2": "PARTY_2",
            "VOIX_2": "VOTES_2",
            "PARTI_3": "PARTY_3",
            "VOIX_3": "VOTES_3",
            "PARTI_4": "PARTY_4",
            "VOIX_4": "VOTES_4",
            "PARTI_5": "PARTY_5",
            "VOIX_5": "VOTES_5",
            "PARTI_6": "PARTY_6",
            "VOIX_6": "VOTES_6",
            "PARTI_7": "PARTY_7",
            "VOIX_7": "VOTES_7",
            "PARTI_8": "PARTY_8",
            "VOIX_8": "VOTES_8",
            "PARTI_9": "PARTY_9",
            "VOIX_9": "VOTES_9",
        },
    },
    "IMMIGRATION_DATA": {  # Uppercase table name
        "csv_file": "2017_2024_IMMIGRATION_prepared.csv",
        "columns_map": {
            "ANNEE": "YEAR",
            "DEPARTEMENT_CODE": "DEPARTMENT_CODE",
            "DEPARTEMENT": "DEPARTMENT",
            "TX_IMMIGRATION": "IMMIGRATION_RATE", 
        },
    },
    "POVERTY_DATA": {  # Uppercase table name
        "csv_file": "2017_2024_PAUVRETE_prepared.csv",
        "columns_map": {
            "ANNEE": "YEAR",
            "DEPARTEMENT_CODE": "DEPARTMENT_CODE",
            "DEPARTEMENT": "DEPARTMENT",
            "TX_PAUVRETE": "POVERTY_RATE", 
        },
    },
}

def create_connection(db_file):
    """ Create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Successfully connected to SQLite database: {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def execute_schema(conn, schema_file):
    """ Execute SQL script to create tables """
    try:
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema_script = f.read()
        conn.executescript(schema_script)
        conn.commit()
        print(f"Schema from {schema_file} executed successfully.")
    except sqlite3.Error as e:
        print(f"Error executing schema: {e}")
    except FileNotFoundError:
        print(f"Schema file not found: {schema_file}")

def load_csv_to_table(conn, table_name, csv_file_path, columns_map):
    """ Load data from CSV file into the specified table """
    try:
        df = pd.read_csv(csv_file_path)
        if columns_map:
            # Before renaming, store the original CSV columns that are keys in the map
            csv_cols_to_rename = {k: v for k, v in columns_map.items() if k in df.columns}
            df.rename(columns=csv_cols_to_rename, inplace=True)
        
        # Select only the columns that are now named as the SQL columns (values from columns_map)
        # and actually exist in the DataFrame after renaming.
        sql_target_columns = [v for v in columns_map.values()]
        df_to_insert = df[[col for col in sql_target_columns if col in df.columns]]

        df_to_insert.to_sql(table_name, conn, if_exists='append', index=False)
        print(f"Data loaded successfully from {csv_file_path} to table {table_name}.")
    except FileNotFoundError:
        print(f"CSV file not found: {csv_file_path}")
    except pd.errors.EmptyDataError:
        print(f"CSV file is empty: {csv_file_path}")
    except KeyError as e:
        print(f"Error processing columns for {csv_file_path}. Missing key in DataFrame: {e}")
        print("This might be due to an incorrect CSV column name in `columns_map` keys")
        print(f"or the column {e} is not present in the CSV file.")
        print(f"Columns available in CSV '{csv_file_path}': {list(pd.read_csv(csv_file_path).columns)}") # Reread for original columns
        print(f"Columns in DataFrame after rename attempt: {list(df.columns)}")
        print(f"Mapped SQL columns expected: {list(columns_map.values())}")
    except Exception as e:
        print(f"An error occurred while loading data to {table_name}: {e}")

def main():
    conn = create_connection(DB_FILE)

    if conn is not None:
        execute_schema(conn, SCHEMA_FILE)

        for table_name, config in TABLE_CONFIG.items():
            csv_path = os.path.join(DATA_DIR, config["csv_file"])
            print(f"Processing {table_name} from {config['csv_file']}...")
            load_csv_to_table(conn, table_name, csv_path, config["columns_map"])

        conn.close()
        print("Database population process finished.")
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main() 