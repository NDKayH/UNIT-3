
# Unit3 Project
***IMAGE GOES HERE***
**Fig.1** Image of XXXXX. (SOURCE HERE)

# Criteria A: Planning

## Problem definition (Client Identification)
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sodales consequat vulputate. Cras cursus vulputate massa non accumsan. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut a arcu ex. Proin in finibus nunc, in vehicula sapien. Duis finibus odio vitae dolor bibendum, in dignissim nisi suscipit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi vitae libero in sapien vulputate auctor.

Praesent ullamcorper orci odio, nec dignissim ante blandit vitae. Sed consequat tempor vestibulum. Nullam mollis egestas faucibus. Praesent at orci lacinia, molestie metus et, tempor erat. Cras eget nisl lacus. Duis tincidunt nibh at nisl gravida tempus. Maecenas sit amet odio pellentesque, dignissim augue sit amet, cursus libero. Etiam quis ante eu mi accumsan lacinia. In et nisl sit amet mauris aliquam mattis at in sapien. Sed tempus bibendum erat ut blandit.

(see evidence of consultation in (AppendixA) SOMEWHERE IDFK)

## Proposed Solution
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sodales consequat vulputate. Cras cursus vulputate massa non accumsan. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut a arcu ex. Proin in finibus nunc, in vehicula sapien. Duis finibus odio vitae dolor bibendum, in dignissim nisi suscipit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi vitae libero in sapien vulputate auctor.


## Tools of my solution
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sodales consequat vulputate. Cras cursus vulputate massa non accumsan. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut a arcu ex. Proin in finibus nunc, in vehicula sapien. Duis finibus odio vitae dolor bibendum, in dignissim nisi suscipit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi vitae libero in sapien vulputate auctor.

## Initial Interview with Client 

# Transcript of First Interview

Developer (Dev): All right, let’s start. This is our first interview for the project. You’re the owner of Fresh Bite Meal Prep, correct?

Client: Yes, that’s right. I own Fresh Bite Meal Prep. We provide healthy, pre-prepared meals for fitness enthusiasts.

Dev: Great. So, what kind of application are you looking for?

Client: I need a simple web and mobile application that allows me to manage orders and track deliveries. We don’t have physical restaurants; we operate from a central warehouse in Karuizawa and handle deliveries across the city.

Dev: Got it. What are the core functionalities you’re looking for?

Client: The app should allow customers to select meals, track orders, and have a management system for warehouse stock levels and ingredient inventory.

Dev: So, you need an inventory management system for both fully prepared meals and ingredients?

Client: Exactly. We also have a dedicated kitchen, so managing ingredient stock is important.

Dev: Understood. What about deliveries?

Client: We need route tracking and estimated delivery times for our drivers. Additionally, I’d like to include a customer feedback page.

Dev: Do you want the app to be mobile-first?

Client: Yes, most of our customers will use mobile devices.

Dev: Okay, and will this be for your internal management only, or do customers need access as well?

Client: Both. I need it for management, but customers should also be able to access it to place and track orders.
Dev: So, you’ll need a login system. Would you prefer a single login page with different user roles, or separate login pages for customers and administrators?

Client: I’m open to suggestions, but a single login page with role-based access would be ideal.

Dev: That makes sense. Any other specific features you need?

Client: No, I think that covers everything for now.

Dev: Great. I have enough information to move forward. I’ll put together a detailed project plan.

Client: Awesome! Looking forward to it.

## Success Criteria
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sodales consequat vulputate. Cras cursus vulputate massa non accumsan. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut a arcu ex. Proin in finibus nunc, in vehicula sapien. Duis finibus odio vitae dolor bibendum, in dignissim nisi suscipit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi vitae libero in sapien vulputate auctor.


# Criteria B: Design

## System Diagram
####SYSTEM DIAGRAM***

**Fig.2** shows the system diagram of the GUI application. I used Macbook Air computer as the development tool and Pycharm for the coding editor. 
Inside the Pycharm, I have the `project.py`, `project_lib.py`, `project.kv`, and `project.db` files and database.
Inside the database of `project.db` which uses sqlite3, I have table users, inventory, orders, order_history, purchases and ledger.

## ER Diagram
![ER_diagram.jpg](Project_md_image%2FER_diagram.jpg)
**Fig3** shows the ER diagram of the database `project.db`. 
The database has 6 tables, users, inventory, orders, order_history, purchases and ledger.
The rectangle shapes shows the name of the table and the circle which connected to each rectangle shows the attributes in the table.
Primary key of each table is showed with underline.
Table user connected to the table orders and purchases by one-to-many relationship because one user can make many orders.
Table orders has one-to-one relationship with the table order_history because one each orde has each order records.
Table orders and purchases are connected with ledger as one-to-one relationship because each order and purchases make the record in the ledger.
Table orders and purchases are also connected to the table inventory as one-to-many relationship because one order contains several ingredients which affects the number of stock in the inventory.

## UML Diagram
![UML_diagram.jpg](Project_md_image%2FUML_diagram.jpg)
**Fig4** shows the UML diagram of the GUI application.
There are 13 classes and all the classes gets attributes from the kv file. One class receive MDApp as an attribute and others receive MDScreen as an attribute.
Each of the class name is the same as the names in the kv file.


## Wireframe
![wire_frame2.png](Project_md_image%2Fwire_frame2.png)
**Fig5** shows the wireframe of the GUI application. 
The screen flow follow the arrows in the figfure.

## Flow Diagrams
### Screen Change
![Screen_change.jpg](Project_md_image%2FScreen_change.jpg)
**Fig6** shows the flow diagram of the screen change function.

### Login
![Login_flow.jpg](Project_md_image%2FLogin_flow.jpg)
**Fig7** shows the flow diagram of the login function.

### Purchase Candle
![Purchase.jpg](Project_md_image%2FPurchase.jpg)
**Fig8** shows the flow diagram of the candle purchase fnction.

# Criteria C: Development

| Task No | Planned Action              | Planned Outcome                                                                                                                                                                                                                                                                                                                                                                | Time estimate (min) | Target completion date | Criteria |
|---------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|------------------------|----------|
| 1       | Consultation with my client | I interviewed my client and defined the problem she had.                                                                                                                                                                                                                                                                                                                       | 30                  | Jan 29                 | A        |
| 2       | Success criteria            | I made success criteria and got approval from the client.                                                                                                                                                                                                                                                                                                                      | 40                  | Feb 17                 | A        |
| 3       | Justification of tools      | I searched for the advantages and disadvantages of the tools I use and the second candidate tools to justify my development tools.                                                                                                                                                                                                                                             | 30                  | Feb 25                 | A        |
| 4       | ER diagram                  | I created an ER diagram to figure out the data that I needed to collect.                                                                                                                                                                                                                                                                                                       | 30                  | Feb 18                 | B        |
| 5       | UML diagram                 | I drew a UML diagram of a relational database to visualize the relationship of each table.                                                                                                                                                                                                                                                                                     | 30                  | Feb 14                 | B        |
| 6       | Sketch                      | I created a Sketch of a GUI application to propose to my client.                                                                                                                                                                                                                                                                                                               | 60                  | Feb 18                 | B        |
| 7       | Home Screen                 | I created a signup button and a login button which move to different pages by click.                                                                                                                                                                                                                                                                                           | 20                  | Feb 22                 | C        |
| 8       | Sign Up                     | I created a signup function that records username and hash made from username and password into the table user.                                                                                                                                                                                                                                                                | 40                  | Feb 26                 | C        |
| 9       | Login                       | I created a login function which validate the inputted username and password by using hash.                                                                                                                                                                                                                                                                                    | 30                  | Mar 3                  | C        |
| 10      | Menu                        | I created menu screen and 6 buttons which moves to different pages.                                                                                                                                                                                                                                                                                                            | 40                  | Mar 3                  | C        |
| 11      | Take Order (order)          | I created a take-order screen by using MDDropItemList. Lists take ingredients data from the inventory table and display as drop-down lists. It allows customers to choose ingredients from the list and record chosen ingredients into the table orders.                                                                                                                       | 120                 | Mar 3                  | C        |
| 12      | Order Check (check)         | I created an order-check screen by using MDDatatable by referring orders table and the button that guides the user to move to purchase candles. After a user presses the payment button, the number of used ingredients is subtracted from the amount in the inventory table, and record orders in the order-history. Also, the profit will be recorded into the ledger table. | 90                  | Mar 4                  | C        |
| 13      | Success Order               | I created a success-order which displays the order done successfully and guides user to the menu page.                                                                                                                                                                                                                                                                         | 15                  | Mar 4                  | C        |
| 14      | Order History               | I created a order history table which displays the past order of candles.                                                                                                                                                                                                                                                                                                      | 40                  | Mar 4                  | C        |
| 15      | Inventory (inventory)       | I created an inventory table and added functions which allows user to select ingredients by checkbox and input the amount they want.                                                                                                                                                                                                                                           | 70                  | Mar 4                  | C        |
| 16      | Inventory Order (purchase)  | I created an inventory-order screen in which the user can see the ingredients that they want to purchase. After the user presses purchase button, the purchased ingredients are added to the amount of inventory. Also, the expenditure will be recorded in the table ledger.                                                                                                  | 40                  | Mar 4                  | C        |
| 17      | Ledger                      | I created a ledger screen that displays the ledger table. Also the descending and ascending button allows the user to flip the order of the ledger based on date.                                                                                                                                                                                                              | 40                  | Mar 4                  | C        |
| 18      | Description                 | I created a description screen that refers to the data in the inventory table and displays the information in the form of MDCardScreen.                                                                                                                                                                                                                                        | 180                 | Mar 6                  | C        |
| 19      | Dialog                      | I create a dialog function and added it error message of signup and login, purchase check, and inventory description.                                                                                                                                                                                                                                                          | 30                  | Mar 6                  | C        |
| 20      | UI                          | I edited the kv file to make the UI better by changing the color and position of the components and adding images.                                                                                                                                                                                                                                                             | 120                 | Mar 8                  | C        |
| 21      | Topbar                      | I created the topbar that has three lines to open the side menu bar.                                                                                                                                                                                                                                                                                                           | 50                  | Mar 8                  | C        |
| 22      | Navigationbar               | I created the side men navigation by using MDNavigationDrawer which guides users to selected pages.                                                                                                                                                                                                                                                                            | 40                  | Mar 8                  | C        |
| 23      | Film video                  | I filmed a video to introduce my development.                                                                                                                                                                                                                                                                                                                                  | 60                  | Mar 9                  | D        |
## Testing plan
| Test                         | Type               | Process (input)                                                                                                                                                                                                                                    | Expected output                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User Signup                  | Unit testing       | 1. Choose 1 as a signup option (1) 2. Enter a username. (mano) 3. Enter a password. (1357) 4. Enter a confirmation password. (1357)                                                                                                                | If the username is not used already sign upped users,  and the password and a confirmation password match,  record the username and the password in the csv file. If the user successfully can sign up, the login menu is displayed.                                                                                                                                                                                                |
| User Login                   | Unit testing       | 1. Enter a username. (mano) 2. Enter a password. (1357)                                                                                                                                                                                            | If the username and the password that the user entered match with the  data on the csv file of user data, the user successfully logged in.                                                                                                                                                                                                                                                                                          |
| Validate the Integer of menu | Unit testing       | 1. Enter the number depending on the menu the user chooses. (1 or 2 or 3 or 4 or 5 or 6)                                                                                                                                                           | If the thing that the user entered is an integer and either one of the numbers in menu, program move on to the session depending on the number the user chooses.                                                                                                                                                                                                                                                                    |
| Deposit                      | Unit testing       | 1. Choose deposit in menu (1). 2. Enter a description of the deposit. (food) 3. Enter the amount of the deposit. (150)                                                                                                                             | If the user enter description and the amount in integer, date, description, deposit(category), amount, balance is recorded in the user's own atm csv file. If the deposit system is successfully done, it displays "Saved" and shows the balance that the user currently has. Also, if the balance is bigger than 0, it displays "You're not debt", and if it is below 0, displays "You're debt"                                    |
| Currency exchange            | Unit testing       | 1. Choose either us dollar or Japanese yen and enter  the choice in integer (1 or 2)                                                                                                                                                               | If the user enter her currency exchange option in integer in 1 or 2, the currency exchange starts. If the user chooses us dollar, get the LTC price in us dollar and multiply with balance, and displays it. If the user chooses Japanese dollar, get the LTC price in Japanese dollar and multiply with balance, and displays it.                                                                                                  |
| Withdrawal                   | Unit testing       | 1. Choose withdrawal in menu (2). 2. Enter a description of the withdrawal. (house) 3. Enter the amount of the deposit. (200)                                                                                                                      | If the user enter description and the amount in integer, date, description, withdrawal(category), amount, balance is recorded in the user's own atm csv file. If the withdrawal system is successfully done, it displays "Saved" and shows the balance that the user currently has. Also, if the balance is bigger than 0, it displays "You're not debt", and if it is below 0, displays "You're debt"                              |
| Balance                      | Unit testing       | 1. Choose balance in menu (3).                                                                                                                                                                                                                     | By reading the user's own atm csv file, it displays the recent balance.                                                                                                                                                                                                                                                                                                                                                             |
| Transaction table            | Unit testing       | 1. Choose transaction table in menu (4).                                                                                                                                                                                                           | By readin the user's own atm csv file, it displays the table without index in markdown style.                                                                                                                                                                                                                                                                                                                                       |
| Chart                        | Unit testing       | 1. Choose chart in menu (5). 2. Choose deposit, withdrawal or balance and enter the option in number. (1 or 2 or 3).                                                                                                                               | If the number that the user entered is an integer and either 1, 2, or 3, it successfully moves to draw the chart. If the number is not fill the requirement above, the program ask the user to enter number again. Depending on the category the user choose, draws line graph which x_axis is date and y_axis is amount.                                                                                                           |
| Logout                       | Unit testing       | 1. Choose logout in menu (6). 2. Enter y or Y if the user wants to logout,  and enter n or N if the user wants to go back to the main menu.                                                                                                        | If the user doesn't enter y, Y, n, or N, the program asks user to enter the letter again. If the user enters y or Y, it displays "You logged out", exit the program by exit code(1).  If the user enter n or N, it displays the main menu.                                                                                                                                                                                          |
| Going back to Main Menu      | Integrated testing | 1. Enter the number depending on the menu the user chooses. (1 or 2 or 3 or 4 or 5 or 6) 2. Session successfully occurs. 3. Go back to the menu and the user enter the number depending on the menu the user chooses. (1 or 2 or 3 or 4 or 5 or 6) | If the thing that the user entered is an integer and either one of the numbers in menu, program move on to the session depending on the number the user chooses. After the session is done, set option_book as False go back to the code of the main menu, and displays the menu. If the user enter the option number correctly as following the above process, this code runs permanently  except when the user chooses to logout. |
| Overall review               | System testing     | 1. Open the pycharm and start the program. 2. Choose signup or login and follow the procedure above. 3. Choose one of the options from the main menu, go to that session, and follow the procedure above. 4. Choose logout. (y or Y)               | All of the output went through well, and there was no error or confusion during the program. If the user chooses to logout, the program ends successfully without any errors.                                                                                                                                                                                                                                                       |


# Criteria C: Development
## Create  Database
As a requirement from the client about the record of the order of candle and money tracking, database is needed to achieve this goal.
Therefore, I decided to use sqlite3 relational database to store the data with relations to apply stored data in many ways.

File from: `project_lib.py`
```.py
import sqlite3
class DatabaseWorker:
    def __init__(self, name:str):
        self.name_db = name
        # Step1: Create a connection to the file
        self.connection =  sqlite3.connect(self.name_db)
        self.cursor = self.connection.cursor()
        
   def run_query(self, query:str):
    self.cursor.execute(query) # run query
    self.connection.commit() # save changes
    
    def search(self, query:str, multiple=False):
        results = self.cursor.execute(query)
        if multiple:
            return results.fetchall() # return multiple rows in a list
        return results.fetchone() # return single value

    def search_variable(self, query:str, *args, multiple=False):
        results = self.cursor.execute(query, args)
        if multiple:
            return results.fetchall() # return multiple rows in a list
        return results.fetchone() # return single value

```
First, I imported the module `sqlite3` to obtain the module to create sqlite3 database. 
I created the class `DatabaseWorker` to connect database and use it in the main python file `project.py`.
I also created functions, `run_query` to run the query code from the python file, `search` and `search_variable` to search the data in the tables.

File from: `project.py`
```.py
from project_lib import DatabaseWorker, make_hash, check_hash

db_name = "project_db"
db_connection = DatabaseWorker(name=db_name)
db_connection.create()
```
By importing the `DatabaseWorker` from the file `project_lib.py`, I created the database called `project_db` and variable `db_connection` to connect with the database.

I created 6 tables in the case of these tables are not existed.

**users**
```.py
        query_users = """CREATE TABLE if not exists users(
                id INTEGER PRIMARY KEY,
                username VARCHAR(30),
                hash TEXT);"""
        db_connection.run_query(query_users)

```

**inventory**
```.py
    query_inventory ="""CREATE TABLE if not exists inventory(
                 id INTEGER PRIMARY KEY,
                 name text,
                 genre text,
                 description text,
                 purchase_price int,
                 selling_price int,
                 amount int);"""
    b_connection.run_query(query_inventory)
```

**orders**
```.py
query_orders="""CREATE TABLE if not exists orders(
                 id INTEGER PRIMARY KEY,
                 staff_id int,
                 model int,
                 wax int,
                 date TEXT,
                 scent int,
                 package TEXT,
                 amount INT,
                 price INT,
                 total_price INT
                 );
 db_connection.run_query(query_orders)
"""
```

**purchases**
```.py
    query_purchases="""
    CREATE TABLE if not exists purchases(
                 id INTEGER PRIMARY KEY,
                 staff_id INT,
                 date TEXT,
                 material TEXT,
                 amount INT,
                 price INT,
                 total INT);"""                
    db_connection.run_query(query_purchases)
```

**order_hisotry**
```.py
    query_order_hisotry="""CREATE TABLE if not exists order_history(
                 id INTEGER PRIMARY KEY,
                 staff_id INT,
                 date TEXT,
                 model int,
                 wax int,
                 scent int,
                 package TEXT,
                 amount int);
```

**ledger**
```.py
    query_ledger="""CREATE TABLE if not exists ledger(
                 id INTEGER PRIMARY KEY,
                 staff_id INT,
                 date TEXT,
                 description TEXT,
                 price INT,
                 balance int);"""
    db_connection.run_query(query_ledger)
```

Also, to calculate the balance, I created the trigger in the conosole of the database.
```.py
-- trigger
CREATE TRIGGER update_balance
AFTER INSERT ON ledger
FOR EACH ROW
BEGIN
    UPDATE ledger
    SET balance = (
        SELECT COALESCE(SUM(price), 0)
        FROM ledger AS prev
        WHERE (prev.date < NEW.date OR (prev.date = NEW.date AND prev.id < NEW.id))
    ) + NEW.price
    WHERE id = NEW.id;
END;
```
This query happens every time the table `ledger` is updated.
I set the for loop which calculates the sum of the price column of the table.
The trigger consider the table `ledger` as `prev`, and define the id by the newer date or the same date as previous row to prevent the miss order allocation.
The new balance is calculated based on the sum of the `price` column for the current row and the cumulative sum of the 'price' column from previous rows.
The subquery calculates the cumulative sum `(SUM(price))` of the `price` column from row in the `ledger`table that have a date earlier than the date of the newly inserted row `(prev.date < NEW.date)`. 
If the dates are the same, it uses the row with the lower id ` (prev.id < NEW.id)`. 
The` COALESCE `function is used to manage cases where there are no previous rows, to make sure that the sum is more htan 0.
Then, the balance is updated only to the row with the same id as the newly inserted row `(WHERE id = NEW.id)`.

I decided to use trigger in the console rather than putting the query to calculate the balance every after orders or purchases, because if I put the calculation coding in two different part of the python file, it will be redundant.

## Signup System (Success Criteria 1)
As a requirement for the solution to clarify the user to make the attribution of responsibility, signup system is needed.
Users make username and user password for the signup, and the system create hash from these data and store the hash instead of password to raise the level of security.

From file `project_lib.py`:
```.py
    from passlib.hash import sha256_crypt
    hasher = sha256_crypt.using(rounds=30000)
```

I imported the module `sha256_crypt` from the `passlib.hash` to create hash.

From file `project.py`:

```.py
class SignupScreen(MDScreen):
    dialog=None
    def try_signup(self):
        uname = self.ids.uname.text
        upass = self.ids.upass.text
        upass_conf = self.ids.upass_conf.text
```

To receive the data inputted in the GUI application, I connected the inputted username and user password by referring the `ids` of those `MDTextField`.
Store the inputted username and password in the variable, `uname`, `upass`, `upass_conf`.

```.py
        if not 0<len(uname)<16 or not 0<len(upass)<9 or not 0<len(upass_conf)<9:
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Please check the number of letters again.",
                    buttons=[MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed
                    )]
                )
            self.dialog.open()
        elif upass != upass_conf:
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Please check the password again.",
                    buttons=[MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed
                    )]
                )
            self.dialog.open()
```
Since, I set the maximum number of letters that user can input, if the user press signup button while inputted data doesn't qualify the given number of letters, the dialog shows the error message.
Also, the case of password and confirmation password are different, it also shows the error message.

```.py
        else:
            hash_text = f"name {uname},pass {upass}"
            hash = make_hash(hash_text)
            results = db_connection.search(query="SELECT * FROM users", multiple=True)
            for row in results:
                signature = row[2]
                valid = check_hash(hashed_text=signature, text=hash_text)
                print(valid)

                if valid:
                    if not self.dialog:
                        self.dialog = MDDialog(
                            text="Your password is invalid, so please enter again.",
                            buttons=[MDFlatButton(
                                text="OK",
                                theme_text_color="Custom",
                                text_color=(1, 0.647, 0, 1),
                                on_release=self.cancel_pressed
                            )]
                        )
                    self.dialog.open()
```

To validate the combination of username and password, I decided to se hash instead of the jst comparison of username and password to make sure the stronger security.
First, I created the hash based on given username and password, then get the data from the table `users` amd compare with the stored hash`signature`.
If it is valid which means that the set of username and password are already exists, the dialog ask the user to enter username and password.

```.py
            else:
                query = f"""
                INSERT into users (username, hash)
                values ('{uname}','{hash}');
                """
                db_connection.run_query(query)
                self.ids.uname.text=""
                self.ids.upass.text=""
                self.ids.upass_conf.text=""
                self.parent.current = "Login"
```
If the inputted data meets those recommendations, by using the sqlite3 query the system create username and password (hash).
After the system stored the information about username and password, make the text fields
Then, the page automatically movse to the login page.

## Login System (Success Criteria 1)
Following the requirement above, I created a login system to verify the username and password. 
It uses the hash to raise the level of security in the process of login.

From file: `project_lib.py`
```.py
    from passlib.hash import sha256_crypt
    hasher = sha256_crypt.using(rounds=30000)
    
    def make_hash(text:str):
        return hasher.hash(text)
    
    def check_hash(hashed_text, text):
        return hasher.verify(text, hashed_text)
```

I created `make_hash` and `check_hash` function in the file `project_lib.py`. 
Putting the code in the sub library file, prevent redundant code and makes the main python code organized.

From file: `project.py`
```.py
class LoginScreen(MDScreen): #Login
    dialog = None
    def try_login(self):
        uname = self.ids.uname.text
        upass = self.ids.upass.text
        query="SELECT * FROM users"
        results= db_connection.search(query=query,multiple=True)

```
To receive the data inputted in the GUI application, I connected the inputted username and user password by referring the `ids` of those `MDTextField`.
Store the inputted username and password in the variable, `uname`, `upass`.
I connected to the database in the table `users` by the query `"SELECT * FROM users"`.
It returns the all user information and stored in the list of `results`.

```.py
        for row in results:
            signature = row[2]
            hash_text=f"name {uname},pass {upass}"
            valid=check_hash(hashed_text=signature, text=hash_text)

```
After receiving the users' information from `results`, extract only hash part.
The system creates the hash with given username and password, and the verify by comparing with stored hash in every row of `users` table by using `check_hash` function.

```.py
            if valid:
                app = MDApp.get_running_app()
                app.staff_id_value = row[0]
                self.ids.uname.text=""
                self.ids.upass.text=""
                self.parent.current = "Menu"
                app.root.ids.topbar.pos_hint = {"top": 1}
                self.dialog=None
                break
            else:
                if not self.dialog:
                    self.dialog = MDDialog(
                        text="Your username or password is incorrect, so please enter again.",
                        buttons=[MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            text_color=(1, 0.647, 0, 1),
                            on_release=self.cancel_pressed
                        )]
                    )
                self.dialog.open()

```

If the inputted username and password matches, it stores the user's `staff_id` from the `id` in the`users` table.
This `staff_id` will be stored in `MDApp` as `staff_id_value`.
Also, after the login, the text fields for the username and password become empty for the next login.
The change in position of `topbar` means that hidden topbar in the home, sigup, and login screen will appear from the menu screen.
After the success login, the page moves to "Menu" and break the for loop.

In the case of username and password doesn't match with hash in the `users` table, it shows the error message.

## Inventory (Success Criteria 2,6)
To meet the **success criteria 2** about the track of inventory, I decided to create a table which shows the inventory condition.
I created `inventory` table in the database, and the table includes the value of id, name of items, the current amount of stock, and shortage (the current amount of stock - the expected storage amount (default_amount)).
```.py
    def on_pre_enter(self, *args):
        columns_names = [('number',50),('material', 100), ('amount', 100),('shortage',100)]
        # columns_names = [column for column in columns_names if column[0] not in ['id', 'genre']]

        self.data_tables = MDDataTable(
            size_hint=(.9, .6),
            pos_hint={'center_x': .5, 'top': .8},
            use_pagination=True,
            check=True,
            background_color_header="#FFC697",
            background_color_selected_cell="f5deb3",
            rows_num=10,
            column_data=columns_names,
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()


    def update(self):
        data = db_connection.search(query='SELECT id, name, amount, default_amount FROM inventory', multiple=True)
        # Perform calculations and update the data before updating the MDDataTable
        calculated_data = [(id, name, amount, (default_amount - amount)) for
                           id, name, amount, default_amount in data]
        # print(data)
        print(calculated_data)
        self.data_tables.update_row_data(
            None, calculated_data
        )
```
I set the column name first, `number`, `material`,`amount` and `shortage`, and stored those names in the list of `columns_names`.
Then, I create the `MDDataTable` which leads to the `update()` function.
In the `update()` function, I run the query to select rows and specified columns from the `inventory` table.
I stored those data into the list of `calculated_data`, and for the part of shortage, I calculated `default_amount - amount`.
The `MDDataTable `will be updated and shows the table of inventory.


To meet the **success criteria 6**, I added the function to suggest the ingredients which are likely to lack.
I already have the shortage column in the above table, and when the calculation button is pressed, the table shows the ingredients which have more than 5 shortages.
```.py
    def calculate_pressed(self):
        if self.calculate:
            data = db_connection.search(query='SELECT id, name, amount, default_amount FROM inventory', multiple=True)
            calculated_data = [(id, name, amount, (default_amount - amount)) for
                               id, name, amount, default_amount in data]
            calculated_data_2=[]
            for row in calculated_data:
                if row[3] >=5:
                    calculated_data_2.append(row)

            self.data_tables.update_row_data(
                None, calculated_data_2
            )
            self.calculate=None
            self.ids.calculate_btn.text="Original"
            self.ids.calculate_btn.icon = "backup-restore"

        else:
            data = db_connection.search(query='SELECT id, name, amount, default_amount FROM inventory', multiple=True)
            # Perform calculations and update the data before updating the MDDataTable
            calculated_data = [(id, name, amount, (default_amount - amount)) for
                               id, name, amount, default_amount in data]
            # print(data)
            print(calculated_data)
            self.data_tables.update_row_data(
                None, calculated_data
            )
            self.calculate = True
            self.ids.calculate_btn.text = "Calculate"
            self.ids.calculate_btn.icon = "calculator"
```
I set the variable `calculate=True` first, so if the user press the calculate button for the first time, it leads to the if statement of `if self.calculate:`.
For the data used in the data table, I set the for loop for the table `inventory`, and if statement says that the rows where the shortage is bigger than 5 are added into the variable list of `calculated_data_2`.
Then, the `MDDataTable` will be updated for the table `calculated_data_2`, and the state of `calculate` become `None` and the text of button changes, too.
This allows the user to find items which are likely to run out soon.
When the user press the button again, it shows the original table of the inventory and change the state of `calculate` and the tet of button.
c

## Ledger (Success Criteria 3)
To meet the **success criteria 3** of trak of money, I decided to create the ledger table.
The table shows the date, the name of staff, description, price, and balance for both sale and purchase orders.

```.py
    def on_pre_enter(self, *args):
        columns_names = [('Date',80),('Staff', 80), ('Description', 80),('Price', 80),('Balance',100)]
        # columns_names = [column for column in columns_names if column[0] not in ['id', 'genre']]
        self.data_tables = MDDataTable(
            size_hint=(.9, .6),
            pos_hint={'center_x': .5, 'top': .65},
            use_pagination=True,
            check=True,
            background_color_header="#FFC697",
            background_color_selected_cell="f5deb3",
            rows_num=10,
            column_data=columns_names
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = db_connection.search(query='SELECT date, staff_id, description, price, balance FROM ledger', multiple=True)
        staff_name = db_connection.search(
            query='SELECT users.username FROM users, ledger where ledger.staff_id = users.id',
            multiple=False)[0]
        # Perform calculations and update the data before updating the MDDataTable
        calculated_data = [(date, staff_name, description, price, balance) for
                           date, staff_id, description, price, balance in data]
        print(data)
        print(calculated_data)
        self.data_tables.update_row_data(
            None, calculated_data
        )
```
As same as the other datatables , I set the name of the column, create `MDDataTable`, update the content in the table in `update()`.
In this case, I used `ledger` table for the money part and `users` table for username part.

## Take Order (Create candle) (Success Criteria 2, 4)
To meet the success criteria 4 about the creation of candle, I made three pages to take order and make candle successfully.
This order process divided into three pages `TakeOrderScreen`, `CheckScreen`, `SuccessOrderScreen`.

### TakeOrderScreen
```.py
class TakeOrderScreen(MDScreen):
    dialog = None
    
        def drop_menu(self, drop_item_element, drop_instance):
        key = drop_instance.text
        genre_d = {"Choose model":"model", "Choose wax":"wax", "Choose scent":"scent"}
        for k,v in genre_d.items():
            if key ==k:
                genre_value = v
        query = f"""
        SELECT * from inventory where genre=?
        """
        results = db_connection.search_variable(query, genre_value, multiple=True)
```
I created  item drop-down lists which allows the user to choose ingredients and amount from the lists.
It receives the drop-down lists' title as `key = drop_instance.text`, and by referring the `genre_d` dictionary, it recognizes the selected list's genre.
After receive the genre, I connected to the database and obtain the items in the table `inventory` which `genre` is selected value.

```.py
        self.model = results
        self.model_item=[]
        self.model_item = [c[1] for c in self.model]

        button_menu=[]
        for item in self.model_item:
            button_dict = {"text": str(item),
                        "viewclass": "OneLineListItem",
                        "on_release": lambda x=item: self.button_pressed(x)}
            button_menu.append(button_dict)

        self.menu = MDDropdownMenu(caller=drop_item_element,
                                   ver_growth="down",
                                   items=button_menu,
                                   width_mult=4,
                                   position="center"
                                   )
        self.menu.open()
```
The above query obtains the rows from `inventory` table which the genre matches, so I extracted the name from the table by using for loop.
I added obtained item name values in the list `button_menu` and created dwop-down lists by using kv components, `MDDropdownMenu`.
The selected item `x` is pass to the function `button_pressed` by using `lambda`.

```.py
    def button_pressed(self,x):
        item = db_connection.search(f"SELECT * from inventory where name='{x}'")

        label = self.ids[item[2]] #item[2] =genre
        if label:
            label.text = item[1]
            self.ids.candle_image.source=f"Project_Images/{item[8]}"

        self.menu.dismiss()
```
By referring the selected item received from `lambda`, obtain the selected item name from the table `inventory`.
In the case of model, the image will change depending on the model the user choose.


```.py
        app = MDApp.get_running_app()
        model=self.ids.model.text
        wax=self.ids.wax.text
        scent=self.ids.scent.text
        package=self.ids.package.text
        amount=self.ids.amount.text
        print(model,wax,scent,package,amount)
```

After the "make more candle" button pressed, it received the selected items by referring the `MDLabel` texts.

```.py
        if len(model) <1 or len(wax) <1 or len(scent) <1 or len(package) <1 or len(amount) <1:
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Please check the order again.",
                    buttons=[
                        MDFlatButton(
                            text="CLOSE",
                            theme_text_color="Custom",
                            text_color=(1, 0.647, 0, 1),
                            on_release=self.cancel_pressed)
                    ],
                )
            self.dialog.open()
```
If any order is missing, the dialog shows the error message to ask the user to check the order.


```.py
        else:
            model_id_query=f"""SELECT * from inventory where name=?"""
            model_id = db_connection.search_variable(model_id_query,model,multiple=False)[0]
            wax_id_query=f"""SELECT * from inventory where name=?"""
            wax_id = db_connection.search_variable(wax_id_query,wax,multiple=False)[0]
            scent_id_query=f"""SELECT * from inventory where name=?"""
            scent_id = db_connection.search_variable(scent_id_query,scent,multiple=False)[0]

            order_list = [model_id, wax_id, scent_id, package, amount]
            print(order_list)
            price = 0
            for order in range(3):
                price_query = f"""SELECT selling_price from inventory where id=?"""
                each_price = db_connection.search_variable(price_query, order_list[order], multiple=False)[0]
                price += each_price
            if order_list[3] == 'Yes':
                price += 30
            total_price = price * int(amount)

            query=f"""
            INSERT INTO orders 
            (model,wax,scent,package,amount,price,total_price,staff_id,date)values(
            '{model_id}',
            '{wax_id}',
            '{scent_id}',
            '{package}',
            '{amount}',
            '{price}',
            '{total_price}',
            '{app.staff_id_value}',
            '{app.today_date}'
            )"""

            db_connection.run_query(query) #insert order in table orders
            self.parent.current = "TakeOrder"
            self.ids.model.text=""
            self.ids.wax.text =""
            self.ids.scent.text=""
            self.ids.package.text=""
            self.ids.amount.text=""
```

If the items are selected correctly, it obtains the item's ids amd price from the `inventory` table.
The price of one candle is calculated by using for loop and multiply by the amount to lead to the total price.
After the calculation, all the ids and price values are stored in the table `orders`.
Then, the text fields are left empty for the next order.

```.py
    def go_to_check(self):
        app = MDApp.get_running_app()
        count_query="""
        SELECT COUNT(*) FROM orders"""
        count_result=db_connection.search(count_query)[0]

        model = self.ids.model.text
        wax = self.ids.wax.text
        scent = self.ids.scent.text
        package = self.ids.package.text
        amount = self.ids.amount.text
        print(model, wax, scent, package, amount)
```

After the "Go to check" button is pressed, it received the selected items by referring the `MDLabel` texts.
It also counts the number or rows in the table `orders` to check the number of orders created in this order.


```.py
        if len(model) > 1 or len(wax) > 1 or len(scent) > 1 or len(package) > 1 or len(amount) > 1:#even if one section is filled
            if len(model) < 1 or len(wax) < 1 or len(scent) < 1 or len(package) < 1 or len(amount) < 1:
                if not self.dialog:
                    self.dialog = MDDialog(
                        text="Please check the order again.",
                        buttons=[
                            MDFlatButton(
                                text="CLOSE",
                                theme_text_color="Custom",
                                text_color=(1, 0.647, 0, 1),
                                on_release=self.cancel_pressed)
                        ],
                    )
                self.dialog.open()
```

If at least one item is selected and missing some items, the dialog shows the error message to ask the user to check the order again.

```.py
            else:
                model_id_query = f"""SELECT * from inventory where name=?"""
                model_id = db_connection.search_variable(model_id_query, model, multiple=False)[0]
                wax_id_query = f"""SELECT * from inventory where name=?"""
                wax_id = db_connection.search_variable(wax_id_query, wax, multiple=False)[0]
                scent_id_query = f"""SELECT * from inventory where name=?"""
                scent_id = db_connection.search_variable(scent_id_query, scent, multiple=False)[0]

                order_list = [model_id, wax_id, scent_id, package, amount]
                print(order_list)
                price = 0
                for order in range(3):
                    price_query = f"""SELECT selling_price from inventory where id=?"""
                    each_price = db_connection.search_variable(price_query, order_list[order], multiple=False)[0]
                    price += each_price
                if order_list[3] == 'Yes':
                    price += 30
                total_price = price * int(amount)

                query = f"""
                        INSERT INTO orders 
                        (model,wax,scent,package,amount,price,total_price,staff_id,date)values(
                        '{model_id}',
                        '{wax_id}',
                        '{scent_id}',
                        '{package}',
                        '{amount}',
                        '{price}',
                        '{total_price}',
                        '{app.staff_id_value}',
                        '{app.today_date}'
                        )"""
                db_connection.run_query(query)
                self.ids.model.text = ""
                self.ids.wax.text = ""
                self.ids.scent.text = ""
                self.ids.package.text = ""
                self.ids.amount.text = ""
                self.parent.current="Check"
```

As same as the `make_more_candle()`, it stores the selected items and price in the table ` orders`, and moves to the page `CheckScreen`.

```.py
        elif count_result>1: #if there is no data in the text, but in the orders
            self.parent.current = "Check"
        elif count_result<1: #if there is no data in the orders
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Please make the order.",
                    buttons=[
                        MDFlatButton(
                            text="CLOSE",
                            theme_text_color="Custom",
                            text_color=(1, 0.647, 0, 1),
                            on_release=self.cancel_pressed)
                    ],
                )
            self.dialog.open()
```

The "Go to check" button works even if there is no selected items in the screen, but there is a order creted before.
It allows the user to go to payment after they press "create more candle' button, but didn't order anything after that.

### CheckScreen
```.py
    def on_pre_enter(self, *args):
        columns_names = [('No.',40),('Model',70),('Wax', 40), ('Scent', 40),('Package', 40),('Price',40), ('Amount',30),('Total',50)]
        self.data_tables = MDDataTable(
            size_hint=(.9, .6),
            pos_hint={'center_x': .5, 'top': .8},
            use_pagination=True,
            check=True,
            background_color_header="#FFC697",
            background_color_selected_cell="f5deb3",
            rows_num=10,
            column_data=columns_names,
        )
        # self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()
        
    def update(self):
        data = db_connection.search(query='SELECT id, model, wax, scent, package, price, amount, total_price FROM orders', multiple=True)
        candle=db_connection.search(query=f"SELECT description from inventory, orders where inventory.id=orders.model")[0]
        wax_name=db_connection.search(query=f"SELECT name from inventory, orders where inventory.id=orders.wax")[0]
        scent_name=db_connection.search(query=f"SELECT name from inventory, orders where inventory.id=orders.scent")[0]
        calculated_data = [(id,candle, wax_name, scent_name, package, price, amount, total_price) for
                           id,model, wax, scent, package, price, amount, total_price in data]
        self.data_tables.update_row_data(
            None, calculated_data
        )
        total_price_query=db_connection.search(query="SELECT SUM(total_price) FROM orders")[0]
        self.ids.total_price_label.text=f'¥ {total_price_query}'
```
It created the table of made orders by referring the table `orders`. Since the items are stored in the form of id in `inventory` table, it converted into the name for the display.

```.py
    def checkbox_pressed(self, table, current_row):
        self.ids.select_item.text=f"Select: {str(current_row[0])}"
        self.check_select=current_row
```
If the order is checked in the datatable, the selected order is showed in the `MDLabel` of id `select_item`.

```.py
    def item_delete(self):
        m = re.findall(r'\d+', self.ids.select_item.text)
        print(m[0])
        item_id=int(m[0])
        db_connection.run_query(query=f"""delete FROM orders WHERE id={item_id}""")
        self.update()
```
If the delete button is pressed, the selected order is deleted from the table `orders`, and update the datatable.

```.py
    def lets_check(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="I would like to proceed with the payment. Is it okay?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed
                    ),
                    MDFlatButton(
                        text="PROCEED",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.proceed_pressed
                    ),
                ],
            )
        self.dialog.open()
        
            def cancel_pressed(self,*args):
        if self.dialog:
            self.dialog.dismiss()

```
If the "Payment" button is pressed, the dialog confirm the user whether they want to make payment or not.


```.py
    def proceed_pressed(self,*args):
        app = MDApp.get_running_app()

        count_query="""
        SELECT COUNT(*) FROM orders"""
        count_result=db_connection.search(count_query)[0]
        print(count_result)


        if self.dialog:
            order_history_query = """
                INSERT INTO order_history (staff_id, date, model, wax, scent, package, amount)
                SELECT staff_id, date, model, wax, scent, package, amount
                FROM orders;
            """
            ledger_query = """
                INSERT INTO ledger (order_id, staff_id, date, price,description)
                SELECT id, staff_id, date, price,'sale'
                FROM orders;
            """

            for i in range(count_result):
                update_model_inventory = f"""
                    UPDATE inventory
                    SET amount = (SELECT amount FROM inventory WHERE inventory.id
                         = (SELECT model FROM orders WHERE orders.id = {i+1})) 
                         - (SELECT amount FROM orders WHERE orders.id = {i+1})
                    WHERE inventory.id = (SELECT model FROM orders WHERE orders.id = {i+1}
                    );
                """
                db_connection.run_query(update_model_inventory)

                update_wax_inventory = f"""
                                    UPDATE inventory
                                    SET amount = (SELECT amount FROM inventory WHERE inventory.id
                                         = (SELECT wax FROM orders WHERE orders.id = {i + 1})) 
                                         - (SELECT amount FROM orders WHERE orders.id = {i + 1})
                                    WHERE inventory.id = (SELECT wax FROM orders WHERE orders.id = {i + 1}
                                    );
                                """
                db_connection.run_query(update_wax_inventory)

                update_scent_inventory = f"""
                                    UPDATE inventory
                                    SET amount = (SELECT amount FROM inventory WHERE inventory.id
                                         = (SELECT scent FROM orders WHERE orders.id = {i + 1})) 
                                         - (SELECT amount FROM orders WHERE orders.id = {i + 1})
                                    WHERE inventory.id = (SELECT scent FROM orders WHERE orders.id = {i + 1}
                                    );
                                """
                db_connection.run_query(update_scent_inventory)

                update_package_inventory = f"""
                                    UPDATE inventory
                                    SET amount = (SELECT amount FROM inventory WHERE inventory.id= 16)
                                         - (SELECT amount FROM orders WHERE orders.id = {i + 1} and orders.package = 'Yes')
                                    WHERE inventory.id = 16
                                    ;
                                """
                db_connection.run_query(update_package_inventory)

            db_connection.run_query(order_history_query)
            db_connection.run_query(ledger_query)

            db_connection.run_query(query="""DELETE FROM orders""")
            self.dialog.dismiss()
            self.parent.current = "Success"
```
After the "Proceed" is pressed in the confirmation dialog, count the number of orders made and insert in the variable `count_result`.
Orders are recorded in the `order_history` table, and profit is recorded in the `ledger` table as the description is "sale".

```.py
        if self.dialog:
            order_history_query = """
                INSERT INTO order_history (staff_id, date, model, wax, scent, package, amount)
                SELECT staff_id, date, model, wax, scent, package, amount
                FROM orders;
            """
            ledger_query = """
                INSERT INTO ledger (order_id, staff_id, date, price,description)
                SELECT id, staff_id, date, price,'sale'
                FROM orders;
            """

            for i in range(count_result):
                update_model_inventory = f"""
                    UPDATE inventory
                    SET amount = (SELECT amount FROM inventory WHERE inventory.id
                         = (SELECT model FROM orders WHERE orders.id = {i+1})) 
                         - (SELECT amount FROM orders WHERE orders.id = {i+1})
                    WHERE inventory.id = (SELECT model FROM orders WHERE orders.id = {i+1}
                    );
                """
                db_connection.run_query(update_model_inventory)

                update_wax_inventory = f"""
                                    UPDATE inventory
                                    SET amount = (SELECT amount FROM inventory WHERE inventory.id
                                         = (SELECT wax FROM orders WHERE orders.id = {i + 1})) 
                                         - (SELECT amount FROM orders WHERE orders.id = {i + 1})
                                    WHERE inventory.id = (SELECT wax FROM orders WHERE orders.id = {i + 1}
                                    );
                                """
                db_connection.run_query(update_wax_inventory)

                update_scent_inventory = f"""
                                    UPDATE inventory
                                    SET amount = (SELECT amount FROM inventory WHERE inventory.id
                                         = (SELECT scent FROM orders WHERE orders.id = {i + 1})) 
                                         - (SELECT amount FROM orders WHERE orders.id = {i + 1})
                                    WHERE inventory.id = (SELECT scent FROM orders WHERE orders.id = {i + 1}
                                    );
                                """
                db_connection.run_query(update_scent_inventory)

                update_package_inventory = f"""
                                    UPDATE inventory
                                    SET amount = (SELECT amount FROM inventory WHERE inventory.id= 16)
                                         - (SELECT amount FROM orders WHERE orders.id = {i + 1} and orders.package = 'Yes')
                                    WHERE inventory.id = 16
                                    ;
                                """
                db_connection.run_query(update_package_inventory)

            db_connection.run_query(order_history_query)
            db_connection.run_query(ledger_query)

            db_connection.run_query(query="""DELETE FROM orders""")
            self.dialog.dismiss()
            self.parent.current = "Success"
```
To meet the **success criteria2** of track of inventory, the amount in `inventory` table is updated depending on the number of ingredients used.
After the all queries done, the system removes all the orders in the `orders` table, and move to the `SuccessOrderScreen`.

```.py
class SuccessOrderScreen(MDScreen):
    def go_back_to_menu(self):
        self.parent.current = "Menu"
```
In the success order screen, there is a button to go back to the menu.

## Order History (Success Criteria 4)
By considering the requirement of the track of orders, the orders created is recorded in the `order_history` table, and displays the table in the form od `MDDataTable`.
```.py
   def on_pre_enter(self, *args):
        columns_names = [('Staff',50),('Prodct', 100), ('Wax', 100),('Scent',100)]

        self.data_tables = MDDataTable(
            size_hint=(.9, .6),
            pos_hint={'center_x': .5, 'top': .7},
            use_pagination=True,
            check=True,
            background_color_header="#FFC697",
            background_color_selected_cell="f5deb3",
            rows_num=10,
            column_data=columns_names
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = db_connection.search(query="""SELECT users.username AS staff, inventory.name AS candle, inventory.name AS wax, inventory.name AS scent
                                                FROM users
                                                JOIN order_history ON order_history.staff_id = users.id
                                                JOIN inventory ON order_history.model = inventory.id OR order_history.wax = inventory.id OR order_history.scent = inventory.id;
                                    """, multiple=True)
        # Perform calculations and update the data before updating the MDDataTable
        calculated_data = [(staff, candle, wax, scent) for
                           staff, candle, wax, scent in data]
        self.data_tables.update_row_data(
            None, calculated_data
        )

```
I set the column name in the first part and created the `MDDataTable`. The content of the datatable is obtained and updated in the `update()`.

## Description (Success Criteria 5)
Too meet the requirement from the client about the checking description of teh candle, I decided to develop the description screen.
In the description page, the items are listed in the form of cards, and if the user pressed the icon in the right top of the cards, the description will be shown in the dialog.

```.py
    def on_enter(self, *args):
        count_query = """
                        SELECT COUNT(*) FROM inventory"""
        count_result = db_connection.search(count_query)[0]
        box_count = count_result  # 追加する MDBoxLayout の数を指定
        self.update_layout(box_count)
        print(f'box_cont: {box_count}')

    def update_layout(self, box_count, box_layout=None):
        container = self.ids.container_desc
        container.clear_widgets()  # delete all children widget
        source='Project_Images/'

        for i in range(box_count):
            count = i+1
            image_query = f"""SELECT image, name, id from inventory where id={count}"""
            material_name = db_connection.search_variable(image_query, multiple=False)[1]
            image_name = db_connection.search_variable(image_query, multiple=False)[0]
            id_numb = db_connection.search_variable(image_query, multiple=False)[2]
            print(f'{material_name}, {source+image_name}',{id_numb})
            box_layout = MDBoxLayout(orientation='vertical', adaptive_size=True, spacing="4dp")

            box_layout.add_widget(
                MD3Card(
                    MDRelativeLayout(
                        MDIconButton(
                            text=f"{id_numb}",
                            icon="dots-vertical",
                            pos_hint={"top": 1, "right": 1},
                            md_bg_color= "FFC697",
                            on_press= lambda x=id_numb: self.press_material(x)
                        ),
                        MDLabel(
                            text=material_name.capitalize(),
                            adaptive_size=True,
                            color="grey",
                            pos_hint={"bottom": 1, "left": 1},
                            size_hint_x=1,
                            halign="center"
                        ),
                        Image(
                            source=f'{source+image_name}',
                            size_hint_y= None,
                            height= '100dp', # Set the desired height
                            width= '200dp',  # Set the desired width
                            pos_hint = {"center_x": .5, "center_y": .5}
            )
                    ),
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    orientation="vertical",
                    padding="4dp",
                    size_hint=(None, None),
                    size=("300dp", "150dp"),
                    md_bg_color="ffdead",
                    shadow_softness=0,
                    shadow_offset=(0, 0),
                )
            )

            container.add_widget(box_layout)  # 新しい MDBoxLayout を追加
```

First I counted the number of items in the table `inventory` to determine the number of `MDBoxLayout` which I will add.
Then, I obtained the image, name, and id of items from the table `inventory`.
In the creation of MD3Card, I made Icon, Label, Image with clear UI.


```.py
    def press_material(self, numb):
        number=int(numb.text)
        text_query=f"""SELECT description from inventory where id={number}"""
        text_desc = db_connection.search(text_query,multiple=False)[0]

        if not self.dialog:
            self.dialog = MDDialog(
                text=f"{text_desc}",
                buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed)
                ],
            )
        else:
            self.dialog.text=f"{text_desc}"
        self.dialog.open()
```
When the IconButton pressed, it receives the id number by the function `lambda` in the previous section, and refers that id number for the description display.
The id number is an id in `inventory` table, and it refers to the `description` column.
If the dialog does not exist, it creates a dialog, if exists, it updates the description.

## UI
Since I decided to use GUI application for easy and clear User Interface (UI), I decided edit the appearance of application to make it easier for the users to use.
Therefore, I created the topbar and side navigation bar for easier page transition.

**topbar**
From file: 'project.kv'
```.py
MDScreen:

    MDNavigationLayout:

        MDScreenManager:
         id: screen_manager
            HomeScreen:
                name: "Home"
                ```  the screen code continues ```
        
        MDTopAppBar:
            id: topbar
            title: "Candlique"
            elevation: 4
            pos_hint: {"top": 2} #when not home it is 1
            md_bg_color: "e7e4c0"
            specific_text_color: "#4a4939"
            left_action_items:[['menu', lambda x: nav_drawer.set_state("open")]]
       
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            NavigationMenu:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                
<NavigationMenu>:
    MDNavigationDrawerHeader:
        title: "Candlique"
        title_color: "#4a4939"
        font_family: "JetBrainsMono"
        spacing: "4dp"
        padding: "12dp", 0, 0, "56dp"

    MDNavigationDrawerLabel:
        text: "Menu"

    DrawerClickableItem:
        icon: "home"
        text: "Home"
        on_press:
            root.nav_drawer.set_state("close")
            
            ```the code continues```
```

In the kv file, I created a `MDTopAppBar` as the same level of `MDScreenManager` to allow the all screen to show the topbar.
In the topbar, there is a title and icon, and if the user click the icon, the `lambda` sets the navigation drawer open.
For the side menu bar, I used `MDNavigationDrawer` and add `DrawerClickableItem` to guide the user to move to the clicked pages.

```.py
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"

<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True
```
To make the selected items more visible, I set the class `DrawerClickableItem@MDNavigationDrawerItem` and `DrawerLabelItem@MDNavigationDrawerItem` which is the code to change the color of the labele they select.
If the user move the cursor and set the focus on the `DrawerLabelItem`, the color of the item will change from `#ffffff` to `"#4a4939"`.

# CriteriaD: Functionality
The video of the application.
https://drive.google.com/drive/folders/1EOk0Dfd0fRsdDp4kjif_ZqO6UlDEUuEq?usp=drive_link

## Citation
[^1]: Gomez, Jose. “Web Apps Vs. Desktop Apps: Understanding the Differences.” Koombea, 16 November 2023, https://www.koombea.com/blog/web-apps-vs-desktop-apps/. Accessed 10 March 2024.
[^2]: “Exploring The Advantages And Disadvantages Of Python.” RedSwitches, 11 January 2024, https://www.redswitches.com/blog/advantages-and-disadvantages-of-python/. Accessed 10 March 2024.
[^3]: Juviler, Jamie. “What Is GUI? Graphical User Interfaces, Explained.” HubSpot Blog, 30 August 2023, https://blog.hubspot.com/website/what-is-gui. Accessed 10 March 2024.
[^4]:“Python: Console Application Structure | by Areyana | Analytics Vidhya.” Medium, 3 March 2020, https://medium.com/analytics-vidhya/python-console-application-structure-ab337c5e94d7. Accessed 10 March 2024.
[^5]:“SQLite Advantages and Disadvantages - javatpoint.” Javatpoint, https://www.javatpoint.com/sqlite-advantages-and-disadvantages. Accessed 10 March 2024.
[^6]: Rodríguez, Andrés, et al. “NavigationDrawer - KivyMD 1.1.1 documentation.” KivyMD's documentation, 2022, https://kivymd.readthedocs.io/en/1.1.1/components/navigationdrawer/index.html. Accessed 10 March 2024.
  
