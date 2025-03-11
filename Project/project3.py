import os
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import ThreeLineListItem
from kivy.properties import NumericProperty, DictProperty
from my_lib import DatabaseManager
from secure_password import check_password as check_hash, encrypt_password
from passlib.exc import UnknownHashError
from kivy.app import App
import random


Window.size = (450, 950)
DB_PATH = os.path.join("/Users/noahhoffman/UWCISAK/Classwork3/Project_3_Real", "main_db.sql")
order_items = []

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

class LoginScreen(MDScreen):
    def try_login(self):
        username = self.ids.user.text.strip()
        password = self.ids.login_password.text.strip()
        if not username or not password:
            print("Username and password are required!")
            return
        query = "SELECT password, role FROM user WHERE username = ?"
        db = DatabaseManager(name=DB_PATH)
        results = db.search(query, (username,))
        if results:
            stored_hash, role = results[0]
            if check_hash(stored_hash, password):
                print(f"User {username} logged in with role: {role}!")
                App.get_running_app().current_user = username
                if role == "admin":
                    self.manager.current = "admin_dashboard"
                elif role == "customer":
                    self.manager.current = "customer_home"
                else:
                    self.manager.current = "home"
                return
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")
        self.ids.user.error = True
        self.ids.user.helper_text = "Invalid username or password"

class RegisterScreen(MDScreen):
    def try_register(self):
        username = self.ids.uname.text.strip()
        email = self.ids.email.text.strip()
        password = self.ids.passwd.text
        repassword = self.ids.passwd_check.text
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
        try:
            db = DatabaseManager(name=DB_PATH)
            check_query = "SELECT * FROM user WHERE username = ? OR email = ?"
            results = db.search(check_query, (username, email))
            if results:
                self.ids.uname.error = True
                self.ids.uname.helper_text = "Username or Email already in use"
                return
            insert_query = "INSERT INTO user(username, email, password, role) VALUES (?, ?, ?, ?)"
            db.run_save(insert_query, (username, email, encrypt_password(password), "customer"))
            print(f"User {username} registered successfully!")
            self.go_to_login()
        except Exception as e:
            print("Registration error:", e)
            self.ids.uname.error = True
            self.ids.uname.helper_text = "Registration failed: Database error"
    def go_to_login(self):
        self.manager.current = "login"

class AdminLoginScreen(MDScreen):
    def try_admin_login(self):
        username = self.ids.admin_user.text.strip()
        password = self.ids.admin_passwd.text.strip()
        if not username or not password:
            print("Admin username and password are required!")
            return
        db = DatabaseManager(name=DB_PATH)
        query = "SELECT password FROM user WHERE username = ? AND role = 'admin'"
        results = db.search(query, (username,))
        if not results:
            print("No admin account found. Please contact the system administrator.")
            self.ids.admin_user.error = True
            self.ids.admin_user.helper_text = "No admin account found."
            return
        stored_hash = results[0][0]
        try:
            if check_hash(stored_hash, password):
                print(f"Admin {username} logged in!")
                self.manager.current = "admin_dashboard"
            else:
                print("Incorrect password.")
                self.ids.admin_passwd.error = True
                self.ids.admin_passwd.helper_text = "Incorrect password."
        except UnknownHashError:
            print("Error: Stored admin password hash is unrecognized.")
            self.ids.admin_passwd.error = True
            self.ids.admin_passwd.helper_text = "Hash error."

class HomeScreen(MDScreen):
    def go_to_customer_dashboard(self):
        print("Navigating to Customer Dashboard...")
        self.manager.current = "customer_home"

class CustomerHomeScreen(MDScreen):
    def view_menu(self):
        print("Navigating to Meal Selection Screen...")
        self.manager.current = "meal_selection"
    def track_orders(self):
        print("Navigating to Order Tracking Screen...")
        self.manager.current = "order_tracking"
    def view_profile(self):
        print("Navigating to Profile Screen...")
        self.manager.current = "profile"
    def submit_feedback(self):
        print("Navigating to Feedback Screen...")
        self.manager.current = "feedback"
    def view_cart(self):
        print("Navigating to Order Checkout Screen...")
        self.manager.current = "order_checkout"
    def logout(self):
        print("Logging out and returning to Login Screen...")
        self.manager.current = "login"

class MealSelectionScreen(MDScreen):
    def on_enter(self):
        db = DatabaseManager(name=DB_PATH)
        query = "SELECT id, name, description, price, image_path FROM food_items"
        items = db.search(query)
        self.ids.food_list.clear_widgets()
        for item in items:
            food_id, name, description, price, image_path = item
            list_item = OneLineListItem(
                text=f"{name} - ${price:.2f}",
                on_release=lambda x, fid=food_id: self.show_food_detail(fid)
            )
            self.ids.food_list.add_widget(list_item)
    def show_food_detail(self, food_id):
        meal_detail_screen = self.manager.get_screen("meal_detail")
        meal_detail_screen.selected_food_id = food_id
        self.manager.current = "meal_detail"

class MealDetailScreen(MDScreen):
    selected_food_id = NumericProperty(0)
    selected_food = DictProperty({})
    def on_pre_enter(self):
        if self.selected_food_id:
            db = DatabaseManager(name=DB_PATH)
            query = "SELECT id, name, description, price FROM food_items WHERE id = ?"
            result = db.search(query, (self.selected_food_id,))
            if result:
                food_id, name, description, price = result[0]
                self.selected_food = {"id": food_id, "name": name, "description": description, "price": price}
                self.ids.food_name.text = name
                self.ids.food_description.text = description
                self.ids.food_price.text = f"${price:.2f}"
            else:
                print("Food not found!")
        else:
            print("No food selected.")
    def add_to_order(self):
        global order_items
        order_items.append(self.selected_food)
        print("Added to order:", self.selected_food)

class OrderCheckoutScreen(MDScreen):
    def on_enter(self):
        global order_items
        self.ids.order_list.clear_widgets()
        total = 0
        for item in order_items:
            list_item = OneLineListItem(text=f"{item['name']} - ${item['price']:.2f}")
            self.ids.order_list.add_widget(list_item)
            total += item['price']
        self.ids.total_label.text = f"Total: ${total:.2f}"

    def confirm_order(self):
        global order_items
        address_field = self.ids.address.text.strip()
        bank_field = self.ids.bank_info.text.strip()
        print("Order confirmed:", order_items)
        db = DatabaseManager(name=DB_PATH)
        estimated_time = random.randint(10, 50)
        customer = App.get_running_app().current_user or "anonymous"
        order_details = ", ".join([item['name'] for item in order_items])
        insert_query = """INSERT INTO orders 
            (customer_username, order_details, status, address, bank_info, estimated_time)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        db.run_save(insert_query, (customer, order_details, "pending", address_field, bank_field, estimated_time))
        order_items = []
        self.manager.current = "customer_home"

    def cancel_order(self):
        global order_items
        order_items = []
        self.manager.current = "customer_home"
        print("Order cancelled")

class OrderTrackingScreen(MDScreen):
    def on_enter(self):
        self.load_customer_orders()
    def load_customer_orders(self):
        username = App.get_running_app().current_user
        if not username:
            print("No customer logged in.")
            return
        db = DatabaseManager(name=DB_PATH)
        query = "SELECT id, order_details, status, estimated_time FROM orders WHERE customer_username = ?"
        orders = db.search(query, (username,))
        self.ids.order_list.clear_widgets()
        for order in orders:
            order_id, details, status, estimated_time = order
            list_item = ThreeLineListItem(
                text=f"Order #{order_id}",
                secondary_text=f"Details: {details}",
                tertiary_text=f"Status: {status} (ETA: {estimated_time} mins)"
            )
            self.ids.order_list.add_widget(list_item)

class AdminDashboardScreen(MDScreen):
    def load_orders(self):
        db = DatabaseManager(name=DB_PATH)
        query = "SELECT id, customer_username, order_details, status FROM orders WHERE status <> 'complete'"
        orders = db.search(query)
        self.ids.order_list.clear_widgets()
        for order in orders:
            order_id, customer, details, status = order
            list_item = ThreeLineListItem(
                text=f"Order #{order_id}",
                secondary_text=f"Customer: {customer}",
                tertiary_text=f"Details: {details} - Status: {status}"
            )
            self.ids.order_list.add_widget(list_item)
    def open_order_detail(self, order_id):
        detail_screen = self.manager.get_screen("order_detail")
        detail_screen.order_id = order_id
        self.manager.current = "order_detail"
    def view_feedback(self):
        self.manager.current = "admin_feedback"

class OrderManagementScreen(MDScreen):
    def on_enter(self):
        self.load_all_orders()
    def load_all_orders(self):
        db = DatabaseManager(name=DB_PATH)
        query = "SELECT id, customer_username, order_details, status FROM orders WHERE status <> 'complete'"
        orders = db.search(query)
        self.ids.order_list.clear_widgets()
        for order in orders:
            order_id, customer, details, status = order
            list_item = OneLineListItem(text=f"Order #{order_id} by {customer}: {details} - {status}", on_release=lambda x, oid=order_id: self.open_order_detail(oid))
            self.ids.order_list.add_widget(list_item)
    def open_order_detail(self, order_id):
        detail_screen = self.manager.get_screen("order_detail")
        detail_screen.order_id = order_id
        self.manager.current = "order_detail"

class OrderDetailScreen(MDScreen):
    order_id = NumericProperty(0)
    order_info = DictProperty({})

    def on_pre_enter(self):
        if self.order_id:
            db = DatabaseManager(name=DB_PATH)
            query = """
                SELECT id, customer_username, order_details, status, address, bank_info, estimated_time 
                FROM orders WHERE id = ?
            """
            result = db.search(query, (self.order_id,))
            if result:
                id_val, customer, details, status, address, bank_info, estimated_time = result[0]
                self.order_info = {
                    "id": id_val,
                    "customer": customer,
                    "order_details": details,
                    "status": status,
                    "address": address,
                    "bank_info": bank_info,
                    "estimated_time": estimated_time
                }
            else:
                print("Order not found!")
        else:
            print("No order selected.")

    def mark_as_complete(self):
        db = DatabaseManager(name=DB_PATH)
        query = "UPDATE orders SET status = 'complete' WHERE id = ?"
        db.run_save(query, (self.order_id,))
        print(f"Order {self.order_id} marked as complete.")
        self.manager.get_screen("order_management").load_all_orders()
        self.manager.current = "order_management"

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
            list_item = OneLineListItem(text=f"{name}: {quantity}", on_release=lambda x, iid=item_id, qty=quantity, iname=name: self.edit_item(iid, qty, iname))
            self.ids.inventory_list.add_widget(list_item)
    def edit_item(self, item_id, quantity, item_name):
        update_screen = self.manager.get_screen("update_inventory")
        update_screen.item_id = item_id
        update_screen.current_quantity = quantity
        update_screen.item_name = item_name
        self.manager.current = "update_inventory"

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

class DeliveryManagementScreen(MDScreen):
    def on_enter(self):
        self.load_deliveries()
    def load_deliveries(self):
        db = DatabaseManager(name=DB_PATH)
        query = "SELECT id, customer_username, order_details, status FROM orders WHERE status = 'pending'"
        deliveries = db.search(query)
        self.ids.delivery_list.clear_widgets()
        for order in deliveries:
            order_id, customer, details, status = order
            list_item = OneLineListItem(text=f"Delivery Order #{order_id}: {details} - {status}", on_release=lambda x, oid=order_id: self.open_delivery_detail(oid))
            self.ids.delivery_list.add_widget(list_item)
    def open_delivery_detail(self, order_id):
        detail_screen = self.manager.get_screen("delivery_detail")
        detail_screen.order_id = order_id
        self.manager.current = "delivery_detail"

class DriverDashboardScreen(MDScreen):
    def on_enter(self):
        self.load_deliveries()
    def load_deliveries(self):
        db = DatabaseManager(name=DB_PATH)
        query = "SELECT id, order_details, status FROM orders WHERE status = 'pending'"
        deliveries = db.search(query)
        self.ids.driver_delivery_list.clear_widgets()
        for delivery in deliveries:
            order_id, details, status = delivery
            list_item = OneLineListItem(text=f"Delivery #{order_id}: {details} - {status}", on_release=lambda x, oid=order_id: self.open_delivery_detail(oid))
            self.ids.driver_delivery_list.add_widget(list_item)
    def open_delivery_detail(self, order_id):
        detail_screen = self.manager.get_screen("delivery_detail")
        detail_screen.order_id = order_id
        self.manager.current = "delivery_detail"

class DeliveryDetailScreen(MDScreen):
    order_id = NumericProperty(0)
    order_info = DictProperty({})
    def on_pre_enter(self):
        if self.order_id:
            db = DatabaseManager(name=DB_PATH)
            query = """
                SELECT id, customer_username, order_details, status, address, bank_info 
                FROM orders WHERE id = ?
            """
            result = db.search(query, (self.order_id,))
            if result:
                id_val, customer, details, status, address, bank_info = result[0]
                self.order_info = {"id": id_val, "customer": customer, "order_details": details, "status": status, "address": address, "bank_info": bank_info}
            else:
                print("Order not found!")
        else:
            print("No order selected.")
    def mark_as_delivered(self):
        db = DatabaseManager(name=DB_PATH)
        query = "UPDATE orders SET status = 'delivered' WHERE id = ?"
        db.run_save(query, (self.order_id,))
        print(f"Order {self.order_id} marked as delivered.")
        self.manager.get_screen("delivery_management").load_deliveries()
        self.manager.current = "delivery_management"

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

class ProfileScreen(MDScreen):
    pass

class LoginApp(MDApp):
    current_user = None
    def build(self):
        root = Builder.load_file("project3.kv")
        initialize_user_database()
        initialize_food_database()
        initialize_orders_database()
        initialize_feedback_database()
        initialize_ingredients_database()
        root.current = "login"
        return root

if __name__ == "__main__":
    LoginApp().run()
