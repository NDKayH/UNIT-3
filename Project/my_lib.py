import sqlite3

class DatabaseManager:
    def __init__(self, name: str):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query, params=()):
        result = self.cursor.execute(query, params).fetchall()
        return result

    def close(self):
        self.connection.close()

    def run_save(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    # def get_user(self, identifier):
    #     query = "SELECT * FROM user WHERE username = ? OR email = ?"
    #     return self.search(query, (identifier, identifier))
    
    # def get_user_by_id(self, user_id):
    #     query = "SELECT * FROM user WHERE id = ?"
    #     return self.search(query, (user_id,))
    
    # def get_user_by_username(self, username):
    #     query = "SELECT * FROM user WHERE username = ?"
    #     return self.search(query, (username,))

    # def get_user_by_email(self, email):
    #     query = "SELECT * FROM user WHERE email = ?"
    #     return self.search(query, (email,)) 
