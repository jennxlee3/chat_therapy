import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established.")
    except Error as error:
        print(f"An error occurred while connecting: {error}")
    return conn


def create_table(conn):
    """ create a table if it doesn't already exist """
    try:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        session_notes TEXT,
        session_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    except Error as error:
        print(f"Failed to create table: {error}")


def insert_session(conn, user_id, session_notes):
    """ insert a new session into the sessions table """
    try:
        c = conn.cursor()
        c.execute("INSERT INTO SESSION (user_id, session_notes) VALUES (?, ?)", (user_id, session_notes))
        conn.commit()
    except Error as error:
        print(f"Failed to insert session: {error}")


def query_all_sessions(conn):
    """ query all rows in the sessions table """
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM sessions")
        rows = c.fetchall()
        for row in rows:
            print(row)
    except Error as error:
        print(f"Failed to read sessions: {error}")


def main():
    database = "therapy_chatbot.db"
    conn = create_connection(database)
    create_table(conn)

    if conn:
        conn.close()


if __name__ == "__main__":
    main()
