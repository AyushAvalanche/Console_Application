class Product:
    def __init__(self, pid=0, pname="", pprice=0.0, pstock=0):
        self.id = pid
        self.name = pname
        self.price = pprice
        self.stock = pstock

class Order:
    def __init__(self):
        self.cart = []  
        self.cart_quantities = [] 
        self.total_amount = 0

    def add_to_cart(self, product, quantity):
        if quantity > product.stock:
            print(f"Insufficient stock for {product.name}")
            return
        if len(self.cart) >= 10:  # maxcart = 10
            print("Cart is full. Cannot add more items.")
            return

        product.stock -= quantity
        self.cart.append(product)
        self.cart_quantities.append(quantity)
        self.total_amount += product.price * quantity

        print(f"Added {quantity} of {product.name} to cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty!")
            return

        print("\nItems in Cart:")
        for i in range(len(self.cart)):
            product = self.cart[i]
            quantity = self.cart_quantities[i]
            print(f"- {product.name} x{quantity} @ ₹{product.price} each")
        print(f"Total: ₹{self.total_amount}")

    def checkout(self):
        if not self.cart:
            print("Cart is empty. Add items before checkout.")
            return

        print("\nCheckout Summary:")
        self.view_cart()
        print("Thank you for your purchase!")

        # Clear the cart
        self.cart = []
        self.cart_quantities = []
        self.total_amount = 0


def display_products(products):
    print("\nAvailable Products:")
    for product in products:
        print(f"{product.id}. {product.name} - ₹{product.price} (Stock: {product.stock})")

def show_menu():
    print("\nE-commerce System Menu:")
    print("1. View Product Catalog")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")
    print("Choose an option: ", end="")

def main():
    # Product initialization
    products = [
        Product(1, "Laptop", 100000, 10),
        Product(2, "Headphones", 3999.99, 50),
        Product(3, "Smartphone", 49999.99, 20),
        Product(4, "Keyboard", 2999.99, 100)
    ]

    user_order = Order()

    while True:
        show_menu()
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            display_products(products)

        elif choice == 2:
            display_products(products)
            try:
                product_id = int(input("Enter Product ID to add to cart: "))
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if 1 <= product_id <= len(products):
                user_order.add_to_cart(products[product_id - 1], quantity)
            else:
                print("Invalid Product ID.")

        elif choice == 3:
            user_order.view_cart()

        elif choice == 4:
            user_order.checkout()

        elif choice == 5:
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
