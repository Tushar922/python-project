class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added to inventory.")

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product '{product.name}' removed from inventory.")
                return
        print("Product not found in inventory.")

    def update_quantity(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity += quantity
                print(f"Quantity of product '{product.name}' updated to {product.quantity}.")
                return
        print("Product not found in inventory.")

    def display_inventory(self):
        print("Inventory:")
        for product in self.products:
            print(f"Product ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}")

def add_product_from_input():
    product_id = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    return Product(product_id, name, category, price, quantity)

# Example usage:
if __name__ == "__main__":
    inventory = Inventory()

    while True:
        print("\nInventory Management System Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Quantity")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product = add_product_from_input()
            inventory.add_product(product)
        elif choice == '2':
            product_id = int(input("Enter product ID to remove: "))
            inventory.remove_product(product_id)
        elif choice == '3':
            product_id = int(input("Enter product ID to update quantity: "))
            quantity = int(input("Enter quantity to add/remove: "))
            inventory.update_quantity(product_id, quantity)
        elif choice == '4':
            inventory.display_inventory()
        elif choice == '5':
            print("Exiting the inventory management system. Thank you!")
            break
        else:
            print("Invalid choice. Please choose again.")