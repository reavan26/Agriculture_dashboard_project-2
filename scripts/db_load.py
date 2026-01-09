# db_load.py
import pandas as pd
import mysql.connector
from mysql.connector import Error

# === File Path ===
CSV_PATH = r"C:\Users\Admin\Downloads\project 2\agriculture_dashboard\data\ICRISAT-District Level Data_clean.csv"

# === MySQL Credentials ===
MYSQL_USER = "root"
MYSQL_PASSWORD = "Luffy@123"
MYSQL_DB = "Agriculture_dashboard"
MYSQL_HOST = "localhost"

# === Table Name ===
TABLE_NAME = "agriculture_data"

def create_connection():
    """Create MySQL connection"""
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        if conn.is_connected():
            print("✅ Connected to MySQL Database")
            return conn
    except Error as e:
        print(f"❌ Error: {e}")
        return None

def create_table(conn, df):
    """Create table dynamically from dataframe columns"""
    cursor = conn.cursor()

    # drop table if exists (optional, for fresh load)
    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

    # Build CREATE TABLE statement
    cols = []
    for col in df.columns:
        cols.append(f"{col} TEXT")  # store all as TEXT for safety
    create_stmt = f"CREATE TABLE {TABLE_NAME} ({', '.join(cols)})"

    cursor.execute(create_stmt)
    conn.commit()
    print(f"✅ Table {TABLE_NAME} created successfully")

def insert_data(conn, df):
    """Insert dataframe rows into MySQL table"""
    cursor = conn.cursor()

    # Prepare insert statement
    placeholders = ", ".join(["%s"] * len(df.columns))
    insert_stmt = f"INSERT INTO {TABLE_NAME} VALUES ({placeholders})"

    # Convert DataFrame to list of tuples
    data = [tuple(str(x) if pd.notna(x) else None for x in row) for row in df.values]

    cursor.executemany(insert_stmt, data)
    conn.commit()
    print(f"✅ Inserted {cursor.rowcount} rows into {TABLE_NAME}")

def main():
    # Load cleaned CSV
    df = pd.read_csv(CSV_PATH)
    print(f"📂 Loaded CSV with {df.shape[0]} rows and {df.shape[1]} columns")

    # Connect to MySQL
    conn = create_connection()
    if conn is None:
        return

    # Create table
    create_table(conn, df)

    # Insert data
    insert_data(conn, df)

    # Close connection
    conn.close()
    print("🔒 Connection closed")

if __name__ == "__main__":
    main()