import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mynameis@btr143",
        database="task_manager_db"
    )
