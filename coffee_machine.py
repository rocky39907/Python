#Report of current inventory, Beverage Cost and Recepie formulae
resources = {"coffee_powder": 1000,
             "water": 1000,
             "milk": 1000}

recepie_price_by_code = {1: 17,
                         2: 22,
                         3: 33}
recepie = {
    1: {"water": 50, "coffee": 18, "milk": 0},
    2: {"water": 200, "coffee": 24, "milk": 150},
    3: {"water": 250, "coffee": 24, "milk": 100}
    }

#Check current inventory status and recharge it if needed
def inventory(option):
    """Takes an input as 'check' or 'recharge' and displays or recharges the current inventory with new quantity."""
    if option == 'check':
        for item in resources:
            print(f"{item.title()}: {resources[item]}")
    elif option == 'recharge':
        coffee_rec = int(input("Enter Coffee quantity in ml: "))
        water_rec = int(input("Enter Water quantity in ml: "))
        milk_rec = int(input("Enter Milk quantity in ml: "))
        resources["coffee_powder"] += coffee_rec
        resources["water"] += water_rec
        resources["milk"] += milk_rec
        for item in resources:
            print(f"{item.title()}: {resources[item]}")
    else:
        print("Invalid option selected!")

#Price List of different flavor of Cofee

def menu():
    """Displays the List of available beverages and their price."""
    beverages = {"Code": {"Beverages": "Price"},
                 1: {"Espresso": 17},
                 2: {"Latte": 22},
                 3: {"Cappuccino": 33}
                 }
    for item in beverages:
        if item == 'Code':
            item_len = 4
        else:
            item_len = 1
        for inner_item in beverages[item]:
            inner_item_len = len(inner_item)
            for col in range(23):
                if col == 0:
                    print(item, end='')
                elif col < item_len or (col > 9 and col < inner_item_len + 9):
                    pass
                elif col == 7 or col == 20:
                    print("|", end='')
                elif col == 9:
                    print(inner_item, end='')
                elif col == 22:
                    if inner_item == "Beverages":
                        print(beverages[item][inner_item])
                    else:
                        print(f"Rs.{beverages[item][inner_item]}")
                else:
                    print(" ", end='')
        if inner_item == "Beverages":
            print(27 * '-')



#Compare with current inventory if required quantities are available to serve the user

def inventory_comperator(recepie_code, quan):
    """Takes beverage code and quantity as input and compare with available Inventory and return True or False based on
    availability of resources."""
    load_receipe = recepie[recepie_code]
    coffee = load_receipe["coffee"] * quan
    water = load_receipe["water"] * quan
    milk = load_receipe["milk"] * quan
    if coffee <= resources["coffee_powder"] and water <= resources["water"] and milk <= resources["milk"]:
        return True
    else:
        return False


#Add all user coins and compare if it's sufficient to buy the Coffee and offer any change remaining
def coin_checker(code, quan, five_coin, ten_coin):
    """Takes beverage code, quantity, coins quantity selected by user(number of Rs.5 and Rs.10 coins)
    as input and return True or False based on whether selected Coins would be sufficient for the purchase."""
    load_receipe_price = recepie_price_by_code[code]
    total_cost = load_receipe_price * quan
    coins_total = 5 * five_coin + 10 * ten_coin
    if coins_total >= total_cost:
        print(f"Required total: Rs.{total_cost}")
        print(f"You will get Rs.{coins_total - total_cost} change. Please proceed with coin insertion.")
        return True
    else:
        print(f"Required total: Rs.{total_cost}")
        print(f"Selected Coins total is Rs.{total_cost - coins_total} short. Please try again.")
        return False

#Prepare the recipe and reduce the inventory accordingly to serve the Coffee to user
def recipe_maker(code, quan):
    """Takes beverage code and user quantity as input and reduces the resources accordingly."""
    load_recipe = recepie[code]
    for cup_no in range(quan):
        resources["coffee_powder"] -= load_recipe["coffee"]
        resources["water"] -= load_recipe["water"]
        resources["milk"] -= load_recipe["milk"]

task_completed = False
while not task_completed:
    user_type = input("Are you an User or Admin?\n")
    if user_type.lower() == 'user':
        #task_completed = True
        #User selection of which flavor they want
        menu()
        user_choice = int(input("Please enter the code number of the beverage that you want:\n"))
        if user_choice not in recepie:
            print("Invalid beverage code entered. Please select from available options!")
        else:
            quantity = int(input("Enter the quantity:\n"))
            check_inven = inventory_comperator(user_choice, quantity)
            if check_inven == False:
                print("Unable to dispense your beverage at the moment due to shortage of resources. Please try again later. "
                      "We apologize for the inconvenience.")
            else:
                #Takes input of the Coins from user
                print("\nOnly Rs.5 and Rs.10 Coins are accepted.")
                five_rupee_coin = int(input("How many Rs.5 Coins you want to insert:\n"))
                ten_rupee_coin = int(input("How many Rs.10 Coins you want to insert:\n"))
                cost_validation = coin_checker(user_choice, quantity, five_rupee_coin, ten_rupee_coin)
                if cost_validation == True:
                    recipe_maker(user_choice, quantity)
                    print("Enjoy your Beverage!")
    elif user_type.lower() == 'admin':
        while not task_completed:
            task = input("Type 'check' to check current Inventory or type 'recharge' to recharge it.\n")
            if task.lower() == 'check' or task.lower() == 'recharge':
                task_completed = True
                inventory(task)
            else:
                print("Invalid Option selected. Please select correct option.")

    else:
        print("Invalid User Type entered. Please try again.")
