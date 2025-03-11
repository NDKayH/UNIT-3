from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from my_lib import DatabaseManager
from secure_password import check_password as check_hash
from secure_password import encrypt_password


class LoginScreen(MDScreen):
    current_user = None

    def try_login(self):
        username = self.ids.username.text
        passwd1 = self.ids.password.text

        # Check if user exists
        query = f"""SELECT * from user where
        username = '{username}' and password = '{encrypt_password(passwd1)}'
        """

        db = DatabaseManager(name="login.sql")
        results = db.search(query=query)
        if len(results) == 1:
            # User exists
            print(results)
            hash_column = results[0][hash_column]
            if check_hash(input_str=passwd1, hash=hash):
                LoginScreen.current_user = username
                # user and password are correct

        else:
            # passwords does not match
            print("Username or password is incorrect")

        LoginScreen.current_user = username
        self.parent.current = "LoginScreen"

        print(LoginScreen.current_user)


class RegisterScreen(MDScreen):
    def try_register(self):
        username = self.ids.username.text
        email = self.ids.email.text
        password = self.ids.password.text
        repassword = self.ids.repassword.text

        # Checks and validation
        # 1 - Is Username and Email unique?
        check1_query = f"""SELECT * from user where
        username = '{username}' or email = '{email}'
        """

        db = DatabaseManager(name="login.sql")
        results = db.search(query=check1_query)
        if len(results) > 0:
            # username or email already used
            self.ids.username.error = True
            self.ids.username.helper_text = "Username or Email already in use"
            return

        # 2 - CHeck if password match
        print(password, repassword)
        if password != repassword:
            self.ids.password.error = True
            self.ids.password.helper_text = "Passwords do not match"

        if len(password) * len(repassword) * len(username) * len(email) != 0:
            insert_query = f"""INSERT into user(username, email, password)
values('{username}','{email}','{encrypt_password(password)}')"""
            db.run_save(query=insert_query)

            LoginScreen.current_user = username
            self.parent.current = "LoginScreen"

            print(encrypt_password(password), LoginScreen.current_user)


class example_login(MDApp):
    def build(self):
        query_table = '''CREATE Table if not exists user(
            id INTERGER PRIMARY KEY,
            username TEXT UNIQUE,
            password VARCHAR(256),
            email text unique
        )
        '''

        x = DatabaseManager(name="login.sql")
        x.run_save(query_table)
        x.close()

        return

    def login(self):
        print("Login button pressed")

    def register(self):
        print("Register button pressed")


t = example_login()
t.run()