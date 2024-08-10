# Importing the clear function from the replit module to clear the terminal screen.
from replit import clear

# Welcome message to the user.
print("Welcome to the my shopping")

# Initializes an empty shopping cart dictionary.
shopping_card = {}

# Defines a dictionary of store products with their respective prices.
store_products = {
    "laptop": 2000,
    "smartphone": 1500,
    "headphones": 1000,
    "keyboard": 500,
}


# Function to ask the user if they want to try again or exit.
def shop_again():
    while True:
        again = input("Do you want to try again: Type 'Yes' or 'No': ").lower()
        if again == "yes":
            clear()  # Clears the screen.
            return main()  # Restarts the main function.
        else:
            exit(0)  # Exits the program.


# Function to display and handle shopping options.
def status():
    ls_options = ["Add item to cart: ", "View cart: ", "Remove item from cart: ", "Exit: "]
    print("=========================")
    for count, op in enumerate(ls_options, 1):
        print(f"{count}. {op}")
    print("=========================")

    # Takes user choice for actions.
    choice = int(input("Enter your choice (1-4): "))

    # Adds items to the shopping cart.
    if choice == 1:
        print("\n=========================")
        for index, (product, price) in enumerate(store_products.items(), 1):
            print(f"{index}. {product} ${price}")
        print("=========================")

        option_number = int(input("Enter the number of the product you want to add to your cart shop: "))

        if 1 <= option_number <= len(store_products):
            list_keys_store_product = list(store_products.keys())
            selected_product = list_keys_store_product[option_number - 1]
            quantitiy_to_add = int(input(f"How many {selected_product.capitalize()} do you want to buy: "))
            current_shop = shopping_card.get(selected_product, 0)
            shopping_card[selected_product] = quantitiy_to_add + current_shop
            print(f"{quantitiy_to_add} {selected_product}(s) to added your card.")

        card_check = input("Do you want to check your shop card: Type 'yes' or 'no': ").lower()

        if card_check == "yes":
            for cart_index, (item, quantity) in enumerate(shopping_card.items(), 1):
                print(f"{cart_index}. {item.capitalize()}: {quantity}")

    # Views items in the shopping cart.
    if choice == 2:
        print("View shopping card...")
        for cart_index, (item, quantity) in enumerate(shopping_card.items(), 1):
            print(f"{cart_index}. {item.capitalize()}: {quantity}")

    # Removes items from the shopping cart.
    if choice == 3:
        if not shopping_card:
            print("Your shopping card is empty...")
        else:
            print("=========================")
            for index, (product, price) in enumerate(store_products.items(), 1):
                print(f"{index}. {product} ${price}")
            print("=========================")

            option_number = int(input("Enter the number of the product you want to remove: "))

            if 1 <= option_number <= len(shopping_card):
                list_keys_shopping_card = list(shopping_card.keys())
                selected_product = list_keys_shopping_card[option_number - 1]

                quantity_to_remove = int(input(f"Enter the quantity of {selected_product.capitalize()} to remove from tour cart: "))
                current_quantity = shopping_card[selected_product]

                if quantity_to_remove >= current_quantity:
                    del shopping_card[selected_product]  # Removes the item if quantity to remove is equal to or greater than current quantity.
                    print("Your shopping card is empty...")
                else:
                    shopping_card[selected_product] = current_quantity - quantity_to_remove  # Adjusts the quantity in the cart.
                    card_check = input("Do you want to check your shop card: Type 'yes' or 'no': ").lower()
                    if card_check == "yes":
                        for cart_index, (item, quantity) in enumerate(shopping_card.items(), 1):
                            print(f"{cart_index}. {item.capitalize()}: {quantity}")
            else:
                print("Invalid option. Please choose a valid option.")

    # Exits the program.
    if choice == 4:
        print("Exiting..., Thanks for shopping")
        exit(0)


# Main function to handle the flow of the shopping program.
def main():
    ask_user = input("Please enter the \"Report\" so that we can show you the resources: ").lower()
    if ask_user == "report":
        print("\n=========================")
        for index, (product, price) in enumerate(store_products.items(), 1):
            print(f"{index}. {product} ${price}")
        print("=========================")

    elif ask_user != "report":
        print("\n==========================ERROR==============================")
        print("Please enter correctly report that show you the resources.")
        print("========================================================")
        return shop_again()  # Asks the user if they want to try again.

    while True:
        ask_user1 = input("Please enter the \"Options\" so that we can show you the resources: ").lower()

        if ask_user1 == "options":
            while True:
                status()  # Shows the status menu.
                add = input("Do you want to Add item/ View card/ Remove item or Exit: Just type 'Yes' or 'No': ").lower()
                if add == "yes":
                    clear()  # Clears the screen for the next action.
                    continue
                elif add == "no":
                    print("Thanks for visiting. See you later.")
                    break
                else:
                    print("Invalid input. Try again")
            break
        else:
            print("please enter correcly. Try again.")

# Ensures the main function runs if this script is executed directly.
if __name__ == "__main__":
    main()
