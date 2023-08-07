# database.py

import sqlite3

DB_NAME = 'earnings.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS earnings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        earnings FLOAT NOT NULL
    );
    """
    conn.execute(create_table_query)
    conn.close()

def save_earning_to_db(date_input, earnings):
    conn = sqlite3.connect(DB_NAME)
    insert_query = "INSERT INTO earnings (date, earnings) VALUES (?, ?);"
    conn.execute(insert_query, (date_input, earnings))
    conn.commit()
    conn.close()

def get_earnings_table():
    conn = sqlite3.connect(DB_NAME)
    query = "SELECT date, earnings FROM earnings;"
    cursor = conn.execute(query)
    earnings_table = [{'date': row[0], 'earnings': row[1]} for row in cursor.fetchall()]
    conn.close()
    return earnings_table
