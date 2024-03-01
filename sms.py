class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        return sum(item.price for item in self.items)

class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, item):
        self.menu_items[item.name] = item

    def display_menu(self):
        print("Menu:")
        for name, item in self.menu_items.items():
            print(f"{name}: Rs.{item.price}")

def main():
    # Create menu
    menu = Menu()
    menu.add_item(FoodItem("Pizza", 100))
    menu.add_item(FoodItem("Burger", 30))
    menu.add_item(FoodItem("Fries", 10))

    # Create order
    order = Order()

    while True:
        print("\nOptions:")
        print("1. Display Menu")
        print("2. Add Item to Order")
        print("3. View Order")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            menu.display_menu()
        elif choice == '2':
            item_name = input("Enter item name: ")
            if item_name in menu.menu_items:
                order.add_item(menu.menu_items[item_name])
                print("Item added to order.")
            else:
                print("Item not found in menu.")
        elif choice == '3':
            print("Current Order:")
            for item in order.items:
                print(f"{item.name}: Rs.{item.price}")
            print(f"Total Price: Rs.{order.total_price()}")
        elif choice == '4':
            print(f"Total Price: Rs.{order.total_price()}")
            print("Thank you for your order!")
            break
        elif choice == '5':
            print("Exiting the food ordering system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()