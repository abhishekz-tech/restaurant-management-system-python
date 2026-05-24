# Restaurant Management System - Beginner Python Project

menu = {
    1: {"item": "Burger", "price": 120},
    2: {"item": "Pizza", "price": 250},
    3: {"item": "Pasta", "price": 180},
    4: {"item": "Cold Drink", "price": 60},
    5: {"item": "Coffee", "price": 90}
}

cart = []
total = 0

print("===================================")
print("   WELCOME TO FOODIE RESTAURANT")
print("===================================")

while True:
    print("\n------ MENU ------")

    for key, value in menu.items():
        print(f"{key}. {value['item']} - ₹{value['price']}")

    print("6. Generate Bill & Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 6:
        break

    if choice in menu:
        quantity = int(input("Enter quantity: "))

        item_name = menu[choice]["item"]
        item_price = menu[choice]["price"]

        amount = item_price * quantity
        total += amount

        cart.append({
            "item": item_name,
            "quantity": quantity,
            "amount": amount
        })

        print(f"{item_name} added successfully!")
    else:
        print("Invalid Choice!")

print("\n===================================")
print("          FINAL BILL")
print("===================================")

for order in cart:
    print(f"{order['item']} x {order['quantity']} = ₹{order['amount']}")

print("-----------------------------------")
print(f"Total Amount: ₹{total}")
print("===================================")
print("Thank You! Visit Again.")