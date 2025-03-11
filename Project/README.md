
# Unit3 Project
![Destination-Gym-Inside-Images6](https://github.com/user-attachments/assets/d49968dc-fc8e-4fc1-9ce4-928d0d5749f3)
**Fig.1** Image of The inside of a physical location for one of the stores (The following app is **not** relevant to any physical stores. (https://destinationgym.co.uk/restore/)

# Criteria A: Planning

## Problem definition (Client Identification)
Initially, the business wanted to rely on paper-based, manual operations to track orders, inventory, and financial transactions, which could result in a series of critical issues. Paper records often lead to missed orders, incorrect meals prepared, and delayed delivery. Additionally, tracking ingredient and meal inventory levels manually has been discovered to be error-prone, leading to shortages or overstocking, while maintaining financial records manually makes it hard to accurately compute profit and costs, thereby increasing the risk of mismanagement. This outdated system also poses security threats, as it is difficult to determine who must handle orders and financial information, and it lacks the ability to change menus, serving sizes, and seasonal ingredient options in a cost-effective way. Thus, I was approached by the client as the developer of their very own Fresh Bite Meal Prep application, which would allow customers to order online while also solving all of the issues that come with manual business management by streamlining the administration process through the use of one centralized and secure application. 

## Initial Interview with Client 

### Transcript of First Interview

This interview was conducted and the transcript was compiled by AI, so beware of any discrepancies. The original audio file is sharable however. 

**Developer (Dev):**  
All right, let’s start. This is our first interview for the project. You’re the owner of Fresh Bite Meal Prep, correct?

**Client:**  
Yes, that’s right. I own Fresh Bite Meal Prep. We provide healthy, pre-prepared meals for fitness enthusiasts.

**Dev:**  
Great. So, what kind of application are you looking for?

**Client:**  
I need a simple web and mobile application that allows me to manage orders and track deliveries. We don’t have physical restaurants; we operate from a central warehouse in Karuizawa and handle deliveries across the city.

**Dev:**  
Got it. What are the core functionalities you’re looking for?

**Client:**  
The app should allow customers to select meals, track orders, and have a management system for warehouse stock levels and ingredient inventory.

**Dev:**  
So, you need an inventory management system for both fully prepared meals and ingredients?

**Client:**  
Exactly. We also have a dedicated kitchen, so managing ingredient stock is important.

**Dev:**  
Understood. What about deliveries?

**Client:**  
We need route tracking and estimated delivery times for our drivers. Additionally, I’d like to include a customer feedback page.

**Dev:**  
Do you want the app to be mobile-first?

**Client:**  
Yes, most of our customers will use mobile devices.

**Dev:**  
Okay, and will this be for your internal management only, or do customers need access as well?

**Client:**  
Both. I need it for management, but customers should also be able to access it to place and track orders.

**Dev:**  
So, you’ll need a login system. Would you prefer a single login page with different user roles, or separate login pages for customers and administrators?

**Client:**  
I’m open to suggestions, but a single login page with role-based access would be ideal.

**Dev:**  
That makes sense. Any other specific features you need?

**Client:**  
No, I think that covers everything for now.

**Dev:**  
Great. I have enough information to move forward. I’ll put together a detailed project plan.

**Client:**  
Awesome! Looking forward to it.

## Proposed Solution
Considering the client's requirements, I believe a Kivy-based GUI (Graphical User Interface) application is the ideral choice because it provies a user-friendly, visually appealing interface (if used correctly) that is easy for non-technical usrs to navigate. Under the hood, the application will consist of an SQL Database to store all the essential information such as registered users with role-based access (customer and administrator), order details, and stock levels (for ingredients). Instead of relying on human-prone paper-based (manual) error, the app will handle all of this automatically, digitally recording every change in orders and inventory so supply of ingredients are always curreant and quantities of prepared meals are always correctly accounted for. The system will then have a designated login page that has a separate admin-login section so users can be directed to the correct page depending on who they are, whether they are a customer, an employee, etc. Customers will be able to view the items on sale, view information such as ingredients, calories and macroes, and be able to place orders, while admins will be able to view current ongoing orders, monitor and change stock and prepared meal quantities, and mark orders as complete. To continue with orders, the orders will be able to be monitored in real-time, with customers able to see estimated delivery times and employees/admins able to see this too allowing delivery drivers to be assisted in optiomizing routes and reducing delays. I would design this appliation using Python using an OOP (Object-Oriented Programming) approach, allowing the app to be easily scalable and modular in case of any new client requests down the line. 

## Tools of my solution
By considering the needs of my client, I decided to use a Kivy-based GUI (Graphical User Interface) that operates as a mobile or desktop solution, which eliminates the need for an internet connection to initialize while offering robust security to guard against application hijackings. A GUI application (especially using Kivy) provides a visually intuitive user interface making it accessible to users who may not be familiar with command-line operations. I chose Python as the programming language of choice due to its versatility and extensive range of libraries and frameworks ,which allows for the development of user interfaces, database management/interfacing, and backend functionality within a single language. Python’s widespread usage, being the most utilized coding language across the globe, allows the application to be maintained and enhanced by other programmers in the future. For data storage, an SQLite database is my relational database management system choice of centralized storage, as it works seamlessly with Python applications that use local data sources. The native hash-checking features also add to the security, performance and reliability that surpasses thoe of other file-based systems (such as a .csv file which is remarkably insecure), Using this combination of tools—Gui, Python and SQL—one is able to achieve a secure, efficient and easy-to-use solution that meets the clients needs today and has the ability to expand in the future

## Success Criteria

Now, based on the initial interview I compiled a set of success criteria in order of importance (1 being the most important and 5 being the least). 

1. **Kivy application must use an SQL Database to store all relevant app information, such as registered users with several roles (i.e. Administrator, Customer) and be editable depending on the task being attempted (storing order information, editing listed items).**

2. **Kivy application must include a login page with access to a separate section allowing role-based access control for customers and administrators (both managers and employees) who can access relevant functionalities.**  
   *Issue Addressed: "Difficulty in distinguishing between admin and customer functionality leading to potential misuse or access errors."*

3. **Kivy application must include a comprehensive management dashboard for administrator users that enables them to monitor and update inventory levels for both ingredients and fully prepared meals.**  
   *Issue Addressed: "Inadequate inventory management which causes ingredient shortages and overstocking."*

4. **Kivy app must include integrated progress tracking with estimated delivery times to assist delivery drivers.**  
   *Issue Addressed: "Delays in delivery and route mismanagement resulting in customer unhappiness and operational inefficiencies."*

5. **App must include a dedicated customer feedback section where users can input feedback and administrators can access it on the Admin-Dashboard page.**  
   *Issue Addressed: "Lack of a formal feedback system, because of which the company is unable to address customer problems effectively."*

6. **The application is optimized for mobile usage, ensuring responsiveness and a user-friendly experience.**  
   *Issue Addressed: “An unresponsive, poor unintuitive application decreases user satisfaction.”*

7. **The Kivy application codebase is developed using Python with an object-oriented programming approach (OOP), ensuring that it is modular, reusable and scalable for any potential enhancements and client needs.**  
   *Issue Addressed: "A monolithic, non-modular codebase that will be hard to maintain and change in the future."*

---

# Criteria B: Design

## System Diagram
![project3_system_diagram](https://github.com/user-attachments/assets/30d295fa-5075-41df-9392-b97d5ed29892)

**Fig.2** shows the system diagram of the Kivy-Based GUI application. I used M3 Macbook Air 13" computer my development tool and Visual Studio Code as my designated coding editor. 

Inside the Visual Studio Code, I have the `project_3.py`, `secure_password.py`, `my_lib.kv`, and `main_db.sql` files and database.
Inside the database of `main_db.sql` which uses sqlite3, I have table users, food_items, inventory, orders, and purchases. 

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

## Creating my Database (Success Criteria #1):

To meet my client’s requirements for an app with inventory management, order tracking, and user data storage, I chose an SQL (specifically SQLite3) for the relational database. It is serverless and with seamless Python integration it seemed ideal for our GUI application. 

In `my_lib.py`, I imported the module `sqlite3` so I would be able to create an SQLite3 database. Then I created a `DatabaseManager` class that is responsible for all database operations. This class contains functions used numerous times in my main `project3.py` file.

```python
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
```

These methods each allow my application to interact with the database without me needing to handle any low-level SQLite3 commands directly from within the main project file. 

In my `project3.py` file, the main one in this project, I imported the os library so that I would be able to locate my main_db.sql database file directly using its exact path, as this was a problem previously where when initializing the database and its contents in my start sequence of my app I had my database file spawn outside of my project folder which was something I didn’t want to do for the sake of organization. 

```python
import os

DB_PATH = os.path.join("/Users/REDACTED/UWCISAK/Classwork3/Project_3_Real", "main_db.sql")
```

Shown here is my `project3.py` file, where I initialize the necessary tables using the `”CREATE TABLE IF NOT EXISTS”` statements. For example, the user table is created:

```python
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
```

In addition to the user table, I created several other tables in case they did not exist:

## Food (Items):

```python
def initialize_food_database():
   db = DatabaseManager(name=DB_PATH)
   create_table_query = """
       CREATE TABLE IF NOT EXISTS food_items (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL,
           description TEXT,
           price REAL,
           image_path TEXT
       );
   """
   db.run_save(create_table_query)
   check_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='food_items'"
   table_exists = db.search(check_query)
   if table_exists:
       columns = db.search("PRAGMA table_info(food_items)")
       column_names = [col[1] for col in columns]
       if "image_path" not in column_names:
           try:
               db.run_save("ALTER TABLE food_items ADD COLUMN image_path TEXT")
           except Exception as e:
               print("Error adding image_path column:", e)
```

## Orders:

```python
def initialize_orders_database():
   db = DatabaseManager(name=DB_PATH)
   query = """
       CREATE TABLE IF NOT EXISTS orders (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           customer_username TEXT NOT NULL,
           order_details TEXT NOT NULL,
           status TEXT NOT NULL,
           address TEXT,
           bank_info TEXT,
           estimated_time INTEGER
       );
   """
   db.run_save(query)
```

## Feedback (Form):

```python
def initialize_feedback_database():
   db = DatabaseManager(name=DB_PATH)
   query = """
       CREATE TABLE IF NOT EXISTS feedback (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           customer_username TEXT NOT NULL,
           feedback_text TEXT NOT NULL
       );
   """
   db.run_save(query)
```

## Inventory (Ingredients):

```python
def initialize_ingredients_database():
   db = DatabaseManager(name=DB_PATH)
   query = """
       CREATE TABLE IF NOT EXISTS ingredients (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL,
           quantity INTEGER NOT NULL
       );
   """
   db.run_save(query)
```

As you can see, each table initializer uses `my_lib.py` in some capacity when starting my application, each using the `run_save(query)` function. 

Each table is configured to address the application's unique requirements.

1.  User Table: Having roles and user authentication segregated prevents unauthorized modification and gives administrators and customers varying levels of access.
2.  Orders Table: Adding customer information, order details, and an `estimated_time` column makes it easy to track progress. This facilitates features such as order status updates.
3.  Feedback Table: A separate feedback table ensures customer feedback can be stored and compared without influencing user or order data.
4.  Food & Ingredients Tables: The separation of food items and inventory ingredients isolates menu listings from stock tracking to enable better inventory control. 

Here is your **Login/Signup System (Success Criteria #2)** section formatted correctly in Markdown without altering any words:

## Login/Signup System (Success Criteria #2)

Next, keeping with my client’s requirements for user authentication and different levels of app-usage depending on the role (i.e. admin, customer), I implemented a secure login system that uses hashing to protect user’s passwords. So, instead of storing plaintext passwords in my user table of my database, I used a hashing function in the file `secure_password.py` to make sure that my users' credentials remain protected from breaches in the system.  

### **From file: `secure_password.py`**  
```python
from passlib.hash import bcrypt  
def encrypt_password(password):  
    return bcrypt.hash(password)  

def check_password(hashed_password, password):  
    return bcrypt.verify(password, hashed_password)
```
I used the **Passlib bcrypt hashing algorithm** to hash my users' passwords. It is well-tested, secure, and, being that it is the **SHA-256 (Secure Hash Algorithm 256-bit)**, the most widely considered **strongest hash protection**, it offers me the **simplest and easiest way** to get the strongest security. The `encrypt_password()` function **hashes** the user's passwords before storing them, then the `check_password()` function **verifies the input password** against stored hashes when logging in. **Both these functions were used in my login functions several times.**  

---

## **User Authentication Process**  
Now, onto the **user authentication process**.  

### **From file: `project3.py`**  
```python
class LoginScreen(MDScreen):  
    def try_login(self):  
        username = self.ids.user.text.strip()  
        password = self.ids.login_password.text.strip()  

        if not username or not password:  
            print("Username and password are required!")  
            return  
```
For the **user authentication process**, when a user attempts to log in, the system retrieves the **username and password** from the input fields in the application’s GUI. If either field is **empty**, then an **error message** is displayed.  

```python
        query = "SELECT password, role FROM user WHERE username = ?"  
        db = DatabaseManager(name=DB_PATH)  
        results = db.search(query, (username,))  
```
This process also **requires queries**, which check the database for the **input username**, and if the username **exists**, then the corresponding **password (which is hashed)** along with the corresponding **role** is retrieved.  

```python
      if results:  
            stored_hash, role = results[0]  
            if check_password(stored_hash, password):  
                print(f"User {username} logged in with role: {role}!")  
                App.get_running_app().current_user = username  

                if role == "admin":  
                    self.manager.current = "admin_dashboard"  
                elif role == "customer":  
                    self.manager.current = "customer_home"  
                else:  
                    self.manager.current = "home"  
                return  
```
If the user successfully **logs in**, the system:
- **Validates the password** by checking it against the stored hash.
- **Stores the current user** in the running app for reference.
- **Redirects the user** to the appropriate dashboard based on their **role** (admin or customer).

---

## **User Registration Process**  
For the **user registration process**, we have the `try_register(self)` function.  

### **From file: `project3.py`**  
```python
class RegisterScreen(MDScreen):  
    def try_register(self):  
        username = self.ids.uname.text.strip()  
        email = self.ids.email.text.strip()  
        password = self.ids.passwd.text  
        repassword = self.ids.passwd_check.text  
```
When a user registers, their **input username, email, and password** are retrieved.  

```python
        if not username or not email or not password:  
            self.ids.uname.error = True  
            self.ids.uname.helper_text = "All fields are required"  
            return  

        if password != repassword:  
            self.ids.passwd.error = True  
            self.ids.passwd.helper_text = "Passwords do not match"  
            return  

        if len(password) < 8:  
            self.ids.passwd.error = True  
            self.ids.passwd.helper_text = "Password must be at least 8 characters"  
            return  
```
The system **validates** that:
- **No fields are empty** (username, email, both password fields, including password confirmation).
- **Passwords match** in each password box.
- **Password length is at least 8 characters** for added security.
- **Username and email are unique** and do not already exist in the database (as shown below):  

```python
try:  
    db = DatabaseManager(name=DB_PATH)  
    check_query = "SELECT * FROM user WHERE username = ? OR email = ?"  
    results = db.search(check_query, (username, email))  

    if results:  
        self.ids.uname.error = True  
        self.ids.uname.helper_text = "Username or Email already in use"  
        return  
```
If validation **passes**, then the system:
1. **Hashes the input password** before storing it in the database (using `encrypt_password()` from `secure_password.py`).
2. **Adds the user** to the database with the **default role** `"customer"` (since only customers can register themselves).
3. **Redirects the user back** to the login screen.

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
  
