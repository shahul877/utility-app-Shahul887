class VendingMachine:
    def __init__(self):
        self.items = {
            'A1': {'name': 'Soda', 'price': 1.50},
            'A2': {'name': 'Chips', 'price': 1.00},
            'A3': {'name': 'Candy', 'price': 0.75},
            
        }
        self.balance = 0.0
        self.purchase_history = []

    def display_items(self):
        print("Available Items:")
        for code, item in self.items.items():
            print(f"{code}: {item['name']} - ${item['price']}")

    def insert_money(self, amount):
        if amount < 0:
            print("Invalid amount. Please insert a positive amount.")
        else:
            self.balance += amount
            print(f"Balance: ${self.balance:.2f}")

    def select_item(self, item_code):
        if item_code in self.items:
            item = self.items[item_code]
            if self.balance >= item['price']:
                self.balance -= item['price']
                self.purchase_history.append(item)
                print(f"Enjoy your {item['name']}! Remaining Balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds. Please insert more money.")
        else:
            print("Invalid item code. Please choose a valid item.")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def provide_receipt(self):
        if not self.purchase_history:
            print("No purchases made.")
        else:
            print("Purchase History:")
            total_spent = 0
            for item in self.purchase_history:
                total_spent += item['price']
                print(f"{item['name']} - ${item['price']}")
            print(f"Total spent: ${total_spent:.2f}")

# Example Usage:
if __name__ == "__main__":
    vending_machine = VendingMachine()

    while True:
        vending_machine.display_items()

        try:
            amount = float(input("Insert money (Enter 0 to exit): "))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue

        vending_machine.insert_money(amount)

        if vending_machine.balance == 0:
            print("Exiting the vending machine. Thank you for using!")
            vending_machine.provide_receipt()
            break

        selected_item = input("Enter the item code you want to purchase (Enter 'B' to check balance): ").upper()

        if selected_item == 'B':
            vending_machine.check_balance()
        else:
            vending_machine.select_item(selected_item)
