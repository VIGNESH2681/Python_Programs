# Initialize a dictionary to store menu items and their prices
menu = {
    "Margherita": 10.99,
    "Pepperoni": 12.99,
    "Vegetarian": 11.99,
    "Hawaiian": 13.99,
}

# Initialize an empty list to store the customer's order
order = []

# Function to display the menu
def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

# Function to take customer orders
def take_order():
    while True:
        display_menu()
        choice = input("Enter the name of the pizza you'd like to order (or 'done' to finish): ")
        if choice == 'done':
            break
        if choice in menu:
            order.append(choice)
        else:
            print("Invalid choice. Please select a pizza from the menu.")

# Function to calculate the total cost of the order
def calculate_total():
    total_cost = sum(menu[item] for item in order)
    return total_cost

# Main program
take_order()
total_cost = calculate_total()
print(f"Your order is: {', '.join(order)}")
print(f"Total cost: ${total_cost:.2f}")