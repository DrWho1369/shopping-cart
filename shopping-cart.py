# PAWS N CART

''' This is a shopping cart - background:
Challenge: Develop a shopping cart application, for pet related products
to help manage your products and that can provide information on adoption centres
and pet care advice

Objective: Develop a program to:
1. Create a shopping cart for a user which they can view
2. Allow user to add and remove items from their cart
3. Calculate the total cost of the cart when requested
'''


### Step by step task: ###

# Create variables that will be used to store items and their prices as strings

items_list = []
item_prices = []
print("\n")
print("-" * 80)
print(f"{"*" * 18} WELCOME TO TOM BAKER'S SHOPPING EXPERIENCE {"*" * 18}")
# ** Displaying a list of items stored in basket
while True:
    # Standardizing variable names and improving readability
    print("-" * 80)
    print("""This is your shopping cart:
    Items in your Cart: {items_list}
    Item Prices: {item_prices}
    Total Cost: £ {sum(item_prices)}""")
    print("-" * 80)

    # Display the user a clear menu and cart continuously until checkout
    print("""Would you like to:
    1. Add an item to your cart
    2. Remove an item from your cart
    3. View the total cost of your cart
    4. Checkout""")
    print("-" * 80)

    # Allowing the user to input their choice and removing unnecessary debugging statement
    choice = input("Enter the number of the option you would like to choose:\n")
    print("-" * 80)

    
    if choice == "4":
    # Exit from the program
        print("*" * 80)
        print("\nThank you for shopping with Paws n Cart!\n")
        print("*" * 80)
        break
    
    elif choice == "1":
        # Find out item and price and add it to cart
        item_input = input("What item would you like to add to your cart: ")
        price = float(input("How much does the item cost: £"))
        item = item_input.upper()
        items_list.append(item)
        item_prices.append(price)
        print("-+-" * 27)
        print(f"{"*" * 15} {item} has been added to your cart successfully. {"*" * 16}")
        print("-+-" * 27)
        continue
    
    elif choice == "2":
        # Find item that must be removed and check that its in the cart
        remove_input = input("Which item would you like to remove: ")
        remove = remove_input.upper()
        if remove in items_list:
            # Remove item from cart and pricelist
            index = items_list.index(remove)
            del items_list[index]
            del item_prices[index]
            print("-:" * 40)
            print(f"{"*" * 15} {remove} has been removed from cart successfully. {"*" * 16}")
            print("-:" * 40)
            continue
        else:
            print("-!-" * 26)
            print(f"{"*" * 18} That item is not in your cart silly! {"*" * 18}")
            print("-!-" * 26)
            continue
    
    elif choice == "3":
        print(f"- {"-£-" * 26} -")
        print(f"{"*" * 23} Total cost of your cart is: £ {sum(item_prices)} {"*" * 22}")
        print(f"- {"-£-" * 26} -")
        continue

    elif choice not in ["1", "2", "3", "4"]:
        print("-!-" * 26)
        print(f"{"*" * 18} That is not a valid option {"*" * 18}")
        print("-!-" * 26)
        continue





