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
# **Code Toolbox**:

# Adding items to a list - use string concatenation to create lists, eg

# list = ""
# list += ",Apple"

# **Removing items from a list**

# remove = "Apple"
# occurance = list.find(remove)

# if occurance == 0:
#     list = list[:len(remove)+1]
# else:
#     list = list[:occurence-1] + list[occurence+len(remove):]




### Step by step task: ###

# Create variables that will be used to store items and their prices as strings

items_list = ""
item_prices = []

# ** Displaying a list of items stored in a string

done = False
pointer = 0
counter = 1

while (not done):
    print("\n")
    print("-"*80)
    print("This is your shopping cart:")
       # Print items in the list formatted neatly
    # Find the next occurence of the , by specifying the start value
    while (not done):
        index = items_list.find(",", pointer)

        if index == -1:
            done = True
            index = len(items_list)
        
        print("Item {:2}: \t {}".format(counter, list[pointer:index]))
        counter += 1
        pointer = index + 1
    # Display the user a clear menu and cart until continously until checkout

    print("-" * 80)
    print("Would you like to: ")
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. View the total cost of your cart")
    print("4. Checkout")
    choice = input("Enter the number of the option you would like to choose:\n")
    
    if choice == "4":
    # Exit from the program
        print("Thank you for shopping with Paws n Cart!")
        break
    elif choice not in ["1", "2", "3"]:
        print("That is not a valid option")
        continue

    if choice == "1":
        # Find out item and price and add it to cart
        item = input("What item would you like to add to your cart: ")
        price = float(input("How much does the item cost: £"))

        items_list += "," + item
        item_prices.append(price)

        print("{} has been added to your cart successfully.".format(item))
    
    elif choice == "2":
        # Find item that must be removed and check that its in the cart
        remove = input("Which item would you like to remove: ")

        if remove in items_list:
            # Remove item from cart and pricelist
            index = items_list.index(remove)
            items_list = items_list[:index] + items_list[index + len(remove):]
            item_prices.pop(index)
    
            print("{} has been removed from cart successfully.".format(remove))
        else:
            print("That item is not in your cart silly!")
    
    elif choice == "3":
        total_sum = sum(item_prices)
        print("Total cost of your cart is: £", total_sum)





