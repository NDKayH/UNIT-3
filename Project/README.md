
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

5. **The application is optimized for mobile usage, ensuring responsiveness and a user-friendly experience, and includes a dedicated customer feedback section where users can input feedback and administrators can access it on the Admin-Dashboard page.**  
  *Issue Addressed: “An unresponsive, poor unintuitive application decreases user satisfaction” and “Lack of a formal feedback system, because of which the company is unable to address customer problems effectively.”*

6. 

---

# Criteria B: Design

## System Diagram
![project3_system_diagram](https://github.com/user-attachments/assets/30d295fa-5075-41df-9392-b97d5ed29892)

**Fig.2** shows the system diagram of the Kivy-Based GUI application. I used M3 Macbook Air 13" computer my development tool and Visual Studio Code as my designated coding editor. 

Inside the Visual Studio Code, I have the `project_3.py`, `secure_password.py`, `my_lib.kv`, and `main_db.sql` files and database.
Inside the database of `main_db.sql` which uses sqlite3, I have table users, food_items, inventory, orders, and purchases. 





## UML Diagram
![project3_UML diagram](https://github.com/user-attachments/assets/62bf2320-9cad-479a-88bc-65f58f44b13f)

**Fig4** shows the UML diagram of the GUI application.
Each of the class name is the same as the names in the kv file.


## Flow Diagrams
### Registration
![Login_flow.jpg](Project_md_image%2FLogin_flow.jpg)
**Fig6** shows the flow diagram of the registration process.

### Login
![Screen_change.jpg](Project_md_image%2FScreen_change.jpg)
**Fig5** shows the flow diagram of the screen login process.

### Purchase Candle
![Purchase.jpg](Project_md_image%2FPurchase.jpg)
**Fig8** shows the flow diagram of the candle purchase fnction.

# Criteria C: Development

## Testing plan

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
            bank_info TEXT
        );
    """
    db.run_save(query)
    try:
        db.run_save("ALTER TABLE orders ADD COLUMN estimated_time INTEGER")
    except Exception as e:
        print("Estimated_time column might already exist:", e)
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

Here is your **Inventory Management Dashboard (Success Criteria #3)** section, formatted properly in **Markdown** without changing your words:

## Inventory Management Dashboard (Success Criteria #3)

Next requirements are an **administrator’s dashboard** that allows for **comprehensive inventory management**. Thus, in my app, I designed an **admin dashboard** that provides the employee with an **overview of ingredient inventory**, allowing the administrator to **update inventory levels in real-time**.  

---

### Database Setup for Inventory Tracking:

To **store and manage** the ingredient inventory data, I created a **dedicated table** within my `main_db.sql` **SQLite3 database**, as seen above in my database creation section. This ensures that the table **exists upon app startup** and it contains: 

- The **names** of the ingredients  
- The **quantity** available in stock  

The reason for this inclusion was to remain **faithful to the client's goal** of ensuring that **preventable shortages and oversupply issues** for inventory are **mitigated** by a more **intuitive and partly automated system** of inventory management.  

In my **orders table**, I also included an added section for **estimated preparation and delivery arrival time**, which is also something **available and viewable for the customer**, ensuring **better tracking of inventory usage** over time.  

```python
try:
    db.run_save("ALTER TABLE orders ADD COLUMN estimated_time INTEGER")
except Exception as e:
    print("Estimated_time column might already exist:", e)
```
Here, I chose to use a **`try:` statement** and an **SQL query** for the addition of the `estimated_time` column.  

**Reasoning:**  
- During the process of making the **order tracking screen**, I had already completed my `initialize_orders_database()` function.  
- To **prevent any issues with existing data retention**, this approach **ensured no data loss**.
- Instead of modifying the original database schema, I **appended the column dynamically**, though this **may have been a non-issue**.

---

## **Administrator Inventory Management Panel**  

The **admin panel** includes an **ingredient inventory management screen**, where **admins can**:  
✔ **View** current stock levels  
✔ **Update** ingredient quantities  
✔ **Manage** stock adjustments in real-time  

### **From file: `project3.py`**
```python
class InventoryManagementScreen(MDScreen):
    def on_enter(self):
        self.load_inventory()

    def load_inventory(self):
        db = DatabaseManager(name=DB_PATH)
        query = "SELECT id, name, quantity FROM ingredients"
        items = db.search(query)
        self.ids.inventory_list.clear_widgets()

        for item in items:
            item_id, name, quantity = item
            list_item = OneLineListItem(
                text=f"{name}: {quantity}",
                on_release=lambda x, iid=item_id, qty=quantity, iname=name: self.edit_item(iid, qty, iname)
            )
            self.ids.inventory_list.add_widget(list_item)
```

### **How This Works:**
- **Retrieves** all **ingredients and their stock levels** from the database.  
- **Displays** them dynamically in the **UI** (`InventoryManagementScreen`).  
- Allows **admins to edit stock levels** when selecting an item in the UI.  

---

## **Editing Inventory in Real-Time**  
Admins can **increase or decrease stock levels** based on the **current supply levels** and the **periodic restocks** on a **bi-monthly basis**.

### **From file: `project3.py`**
```python
class UpdateInventoryScreen(MDScreen):
    item_id = NumericProperty(0)
    current_quantity = NumericProperty(0)
    item_name = ""

    def update_quantity(self):
        new_qty_str = self.ids.new_quantity.text.strip()
        try:
            new_qty = int(new_qty_str)
        except ValueError:
            print("Invalid quantity")
            return

        db = DatabaseManager(name=DB_PATH)
        query = "UPDATE ingredients SET quantity = ? WHERE id = ?"
        db.run_save(query, (new_qty, self.item_id))

        print(f"Updated {self.item_name} (id: {self.item_id}) to quantity {new_qty}")
        self.manager.get_screen("inventory_management").load_inventory()
        self.manager.current = "inventory_management"
```

### **How This Works:**  
- The **admin inputs a new quantity** for an ingredient.  
- **Data validation** ensures **only valid numbers** are entered.  

```python
except ValueError:
    print("Invalid quantity")
    return
```
- The **database is updated** in real-time, preventing **incorrect stock tracking**.  
- The inventory list **refreshes automatically**.  

---

## **Preventing Overstock & Shortages**  
By integrating this **inventory management system**, my application **and the administrator** can:  

- **Track inventory levels dynamically**
- **Prevent overstocking** by ordering only necessary ingredients
- **Prevent shortages** by allowing proactive restocking  

This system **fully meets Success Criteria #3**, ensuring that the **administrator’s dashboard provides real-time inventory control** for better management of **ingredients and fully prepared meals**.

## Mobile Optimization and Customer Feedback System (User Experience) [Success Criteria] #5

To ensure that the application is **optimized for mobile users** primarily and delivers a **user-friendly experience**, I added features such as **dynamic screen scaling** and **intuitive "idiot-proof" navigation**, along with a **dedicated customer feedback screen** that allows any user to submit feedback directly from within the app. This feedback can then be viewed by administrators.

Like the success criteria suggest, this addresses several issues:

- **“An unresponsive, poor unintuitive application decreases user satisfaction”**  
- **“Lack of a formal feedback system, because of which the company is unable to address customer problems effectively”**  

---

## **Mobile Optimization**
Firstly, for the **user experience**, I applied **responsive design principles** and optimized my GUI’s **layout for different mobile screen sizes** for maximum compatibility.

### **From file: `project3.py`**
```python
Window.size = (450, 950)
```
With the default window size being **450x950 pixels**, I believe that it is a **good middle ground** between mobile phone screen sizes and aspect ratios, allowing for **maximum compatibility** with UI elements **not appearing disproportionate or distorted**. 

I also used **KivyMD components** to incorporate this **more modern design philosophy**:
```python
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
```
This was because **KivyMD** automatically adjusts UI components to look **clean and scalable**, and the **Material Design principles** provide **better usability**, making the app more intuitive to use.

Additionally, I used **ScreenManager** (imported from Kivy) to make **switching between screens more seamless**.

---

## **Customer Feedback System**
To ensure that customers can **submit feedback efficiently**, I created a **dedicated feedback screen** where customers can input their concerns, and administrators can review and address them.

### **From file: `project3.py`**
```python
class FeedbackScreen(MDScreen):
   def submit_feedback(self):
       username = getattr(self.manager, "current_customer", "anonymous")
       feedback_text = self.ids.feedback_input.text.strip()

       if not feedback_text:
           print("Feedback cannot be empty")
           return

       db = DatabaseManager(name=DB_PATH)
       query = "INSERT INTO feedback (customer_username, feedback_text) VALUES (?, ?)"
       db.run_save(query, (username, feedback_text))

       print("Feedback submitted")
       self.ids.feedback_input.text = ""
```
### **How it Works**
1. A user enters their feedback into the text field.  
2. The system **validates** that **no empty feedback** was submitted, preventing blank responses.  
3. The feedback is **stored in the SQLite3 database (`main_db.sql`)** with the corresponding username.  
4. After submission, the **text field clears automatically** for a seamless experience.  

---

## **Administrator Feedback Review**
On the **admin’s side**, feedback is displayed **in a structured format** for easy review.

### **From file: `project3.py`**
```python
class AdminFeedbackScreen(MDScreen):
    def on_enter(self):
        self.show_table_feedback()

    def show_table_feedback(self):
        db = DatabaseManager(name=DB_PATH)
        feedbacks = db.search("SELECT id, customer_username, feedback_text FROM feedback")

        if hasattr(self, 'data_table'):
            self.remove_widget(self.data_table)

        table_rows = []
        for fb_id, customer, text in feedbacks:
            table_rows.append((str(fb_id), customer, text))

        self.data_table = MDDataTable(
            size_hint=(0.9, 0.8),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            column_data=[("ID", dp(30)), ("Customer", dp(30)), ("Feedback", dp(60))],
            row_data=table_rows
        )
        self.add_widget(self.data_table)
```
### **How it Works for Admins**
- **Feedback is automatically loaded** when the page is opened.  
- The feedback is displayed using a **structured format (`MDDataTable`)**, making it **organized and easy to navigate**.  
- Admins can **review all customer input in one place**, ensuring that issues are addressed efficiently.  

---

## **Impact of These Features**
By implementing **mobile optimization and a structured feedback system**, my application:
- **Enhances user experience** via simple and intuitive navigation.
- **Decreases customer frustration** with an organized, responsive interface.
- **Improves business decision-making** by providing a systematic framework for capturing and addressing customer complaints.
- **Increases engagement** as users feel their feedback is valued and addressed. 

```

# CriteriaD: Functionality
The video of the application.
VIDEO GOES HERE

## Citation
