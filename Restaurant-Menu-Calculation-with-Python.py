# import color library
from clint.textui import colored

# Create three dictionary to list items and prices from three different restaurant menus.
joey_menu={
    'Nachos': 23.50,
    'Pizza Margherita': 29,
    'Hummus': 19,
    'Jumbo Lump Crab Cake': 22.75,
    'Szechuan Chicken Lettuce Wraps': 22.50,
    'Sushi Cone': 6.50,
    'Steak & Sushi': 33.25,
    'House Salad': 9.50,
    'California Chicken': 23.50,
    'Ravioli Bianco': 33.25,
    'Prime New York Strip': 64.50,
    'Warm Italian Donuts': 12.50
}
cheesecake_factory_menu={
    'Crab Wontons': 12.95,
    'Thai Chili Shrimp': 14.95,
    'Housemade Meatballs': 14.50,
    'Petite Filet': 36.50,
    'Street Corn': 9.95,
    'Fried Zucchini': 10.95,
    'Roadside Sliders': 14.95,
    'Quesadilla': 14.95,
    'Caesar Salad': 15.95,
    'Pepperoni Flatbread Pizza': 13.95,
    'Orange Chicken': 17.95,
    'Old Fashioned Burger': 17.95
}
wild_genger_menu={
    'Won Ton Mein Soup': 17,
    'Green Papaya Salad': 18.5,
    'Indian Butter Chicken': 25,
    'Chicken Pad Thai': 22,
    'Monks Curry': 21,
    'Beef Rendang': 24,
    'Sichuan Green Beans': 16,
    'Green Curry Chicken': 23,
    'Mongolian Noodles': 24,
    'Seven Flavor Beef': 28.5,
    'Thai Spring Rolls': 12,
    'Chicken Wings': 17
}

# Create a function to prompt the user to order items from the chosen menu
def order_item(menu):
    ordered_item = ''
    try:
        ordered_item = input('What would you like to order?\n')
        ordered_item = ordered_item.lower().title()
    except ValueError:
        print()
    if ordered_item not in menu:
        print(colored.red("Invalid item, please order from the menu\n"))
    return ordered_item

# Create a function calculate cost for items ordered from the menu.
def calculate_sub_total(menu, items):
    total = 0.00
    for item in items:
        total += menu[item]
    return total

# Create a function to print out ordered items, their prices, and combined price.
def print_item(menu, items):
    for item in items:
        print(colored.green(f"{item:32}: ${menu[item]: .2f}"))
    print()
    sub_total = calculate_sub_total(menu, items)
    print(colored.green(f"Sub_Total{' '*23}: ${sub_total: .2f}\n"))

# Create a function to display chosen restaurant's menu
def menu():
    restaurant_menu = {}
    restaurant =''
    while True:
        try:
            #Prompt the user to input a restaurant they like from given three restaurants.
            restaurant  = input("What Restaurant would like to you eat tonight?\n"
                               "Here are some good opetions: Joey, Cheesecake Factory, Wild Genger.\n> ")
            # Ensure inputed restaurants name is lower cased and titled only.
            restaurant = restaurant.lower().title()
            print()
        # if input is not one of the three restaurants, break out the loop and keep asking.
        except ValueError:
            print()
            break
        # assign menu to chosen restaurant's menu based on the condition
        if restaurant == "Joey":
            restaurant_menu = joey_menu
            break
        elif restaurant == 'Cheesecake Factory':
            restaurant_menu = cheesecake_factory_menu
            break
        elif restaurant == 'Wild Genger':
            restaurant_menu = wild_genger_menu
            break
        else:
            print (colored.red('Sorry, it is not an option.\n'
                               'Please only choose from Joey, Cheesecake Factory, Wild Genger.\n'))
    # return menu for further use.
    print(colored.green(f"You have chosen a restaurant called {restaurant}."))
    return restaurant_menu

# Call the function and assign it to a variable called chosen_menu
chosen_restaurant_menu = menu()
print("Here is the menu for restaurant you have chosen:\n")
# print out all items and their prices in a desired format
for item in chosen_restaurant_menu:
    print(f"{item:32}: ${chosen_restaurant_menu[item]}")
print()

# Create a empty list to list all items ordered by user
all_item_ordered = []
# create a function to calculate final cost of all items ordered from menu
def bill():
    while True:
        ordered_item = order_item(chosen_restaurant_menu)
        if ordered_item in chosen_restaurant_menu:
            all_item_ordered.append(ordered_item)
            print_item(chosen_restaurant_menu, all_item_ordered)

            # Ask user whether they want to order more
            while True:
                order_more = ''
                # if user want to order more, ask what they want to order from the menu
                try:
                    order_more = input("Would you like to order more? 'y' or 'n' only.\n>")
                    order_more = order_more.lower()
                    print()
                except ValueError:
                    print(colored.red("'y'or 'n' only please. Try again.\n"))
                if order_more == 'y':
                    more_item = order_item(chosen_restaurant_menu)
                    if more_item in chosen_restaurant_menu:
                        all_item_ordered.append(more_item)
                        print_item(chosen_restaurant_menu, all_item_ordered)

                # stop asking and summarize item ordered and total cost
                elif order_more == 'n':
                    print_item(chosen_restaurant_menu, all_item_ordered)
                    print(colored.green("Your order will be ready soon:)\n"))
                    break
                else:
                    print(colored.red("'y'or 'n' only please. Try again.\n"))
            break
    # return formated_total
    return  calculate_sub_total(chosen_restaurant_menu, all_item_ordered)

# Create a function to calculate the final bill after tips and tax
def final_bill(food_bill, tip_percentage, tax):
    tip = food_bill* tip_percentage
    final_bill = food_bill + tip +tax
    return final_bill

food_bill = bill()
# Call the function based on 20% tip and 10% tax.
final = final_bill(food_bill, 0.20, 0.10)
# Format final bill with two decimals.
formated_final = "{:,.2f}".format(final)
print(colored.yellow(f'Your final total bill including tax and tips is: ${final: .2f}'))
print(colored.yellow("Thank you for choosing us and please come back again:)"))

