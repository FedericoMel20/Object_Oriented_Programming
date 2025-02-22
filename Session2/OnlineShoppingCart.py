class CartItem:
    cart = []
    
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        CartItem.cart.append(self)
    
    def add_item(self):
        print(f"Added {self.quantity} x {self.item_name} to the cart.")
    
    @classmethod
    def remove_item(cls, item_name):
        for item in cls.cart:
            if item.item_name.lower() == item_name.lower():
                cls.cart.remove(item)
                print(f"Removed {item.item_name} from the cart.")
                return
        print("Item not found in the cart.")
    
    @classmethod
    def calculate_total(cls):
        total = sum(item.price * item.quantity for item in cls.cart)
        print(f"Total Price: ${total:.2f}")
    
    @classmethod
    def list_cart(cls):
        if cls.cart:
            print("\nShopping Cart:")
            for item in cls.cart:
                print(f"Item: {item.item_name}, Price: ${item.price}, Quantity: {item.quantity}")
        else:
            print("Cart is empty.")

# Menu-driven approach

while True:
    print("\nOnline Shopping Cart")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Calculate Total")
    print("5. Exit")
        
    choice = input("Enter your choice: ")
        
    if choice == "1":
        item_name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        item = CartItem(item_name, price, quantity)
        item.add_item()
    elif choice == "2":
        item_name = input("Enter item name to remove: ")
        CartItem.remove_item(item_name)
    elif choice == "3":
        CartItem.list_cart()
    elif choice == "4":
        CartItem.calculate_total()
    elif choice == "5":
        print("Exiting... Thank you for shopping!")
        break
    else:
        print("Invalid choice. Try again.")
