# Quiz 041

## Paper Solution
_____


## Code
```.py

import sqlite3
import hashlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TransactionValidator:
    def __init__(self, database_file="payments.db"):
        self.database_file = database_file

    def generate_hash(self, txn_id, amount, timestamp, private_key="secure_secret"):
        """
        Produce a hash to validate transaction integrity.
        """
        data_string = f"{txn_id}{amount}{timestamp}{private_key}"
        return hashlib.sha256(data_string.encode()).hexdigest()

    def verify_transactions(self):

Compare stored hash signatures with recalculated values
        to detect potential fraudulent entries.

        connection = sqlite3.connect(self.database_file)
        cursor = connection.cursor()
        cursor.execute("SELECT id, amount, timestamp, hash_signature FROM transactions")
        records = cursor.fetchall()

        suspicious_ids = []

        for txn_id, amount, timestamp, existing_hash in records:
            new_hash = self.generate_hash(txn_id, amount, timestamp)
            if existing_hash != new_hash:
                suspicious_ids.append(txn_id)

        connection.close()

        if suspicious_ids:
            print("Suspicious transactions found:", suspicious_ids)
        else:
            print("No discrepancies detected.")

        return suspicious_ids


class ValidationScreen(BoxLayout):
    """
    Basic screen layout for fraud validation results.
    """
    pass


class TransactionApp(App):
    def build(self):
        return ValidationScreen()

    def initiate_validation(self):
        checker = TransactionValidator()
        flagged_transactions = checker.verify_transactions()

        results_label = self.root.ids.results_label
        if flagged_transactions:
            results_label.text = f"Alert! Fraud identified in: {flagged_transactions}"
        else:
            results_label.text = "All transactions appear valid."


if __name__ == "__main__":
    TransactionApp().run()
 
```

