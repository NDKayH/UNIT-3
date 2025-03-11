import os
from my_lib import DatabaseManager
from secure_password import encrypt_password

DB_PATH = os.path.join("/Users/noahhoffman/UWCISAK/Classwork3/Project_3_Real", "main_db.sql")

def initialize_user_database():
    db = DatabaseManager(name=DB_PATH)

    create_table_query = """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        );
    """
    db.run_save(create_table_query)

def add_admin_account(username="admin", email="admin@example.com", password="password"):

    initialize_user_database()
    
    db = DatabaseManager(name=DB_PATH)
    existing_admin = db.search("SELECT * FROM user WHERE username = ? AND role = 'admin'", (username,))
    if existing_admin:
        print(f"Admin account '{username}' already exists.")
        return
    insert_query = "INSERT INTO user(username, email, password, role) VALUES (?, ?, ?, ?)"
    db.run_save(insert_query, (username, email, encrypt_password(password), "admin"))
    print("Account created successfully.")

if __name__ == "__main__":
    add_admin_account()
