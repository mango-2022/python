MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_machine = 0


def check_sufficient(need_resources):
    """Return True when order can be made, False if ingredients are insufficient"""
    if resources['water'] < need_resources['water']:
        print('water is not enough')
        return False
    elif resources['milk'] < need_resources['milk']:
        print('milk is not enough')
        return False
    elif resources['coffee'] < need_resources['coffee']:
        print('coffee is not enough')
        return False
    else:
        return True


# def check_sufficient(order_ingredients):
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"sorry, there is not enough {item}")
#             return False
#     return True


def calculate_coins(quarters, dimes, nickles, pennies):
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def check_transaction(coin_value, coffee_value):
    """Return True when payment is accepted, or False if money is insufficient"""
    if coin_value < coffee_value:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(coin_value - coffee_value, 2)
        global money_machine
        money_machine += coffee_value
        print(f"change: ${change}, here is your coffee.")
        return True


def update_resources(remain_resources, need_resources):
    water = remain_resources['water'] - need_resources['water']
    milk = remain_resources['milk'] - need_resources['milk']
    coffee = remain_resources['coffee'] - need_resources['coffee']
    return {"water": water, "milk": milk, "coffee": coffee}


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources"""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name}. Enjoy!")


end_of_machine = False

while not end_of_machine:
    customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_input == 'off':
        end_of_machine = True
    elif customer_input == 'report':
        print(f"water:{resources['water']} ml")
        print(f"milk:{resources['milk']} ml")
        print(f"coffee:{resources['coffee']} g")
        print(f"Money: ${money_machine}")
    elif customer_input == 'espresso' or customer_input == 'latte' or customer_input == 'cappuccino':
        customer_choice = MENU[customer_input]

        if check_sufficient(customer_choice['ingredients']):

            quarters_input = int(input("Please insert quarters: "))
            dimes_input = int(input("Please insert dimes: "))
            nickles_input = int(input("Please insert nickles: "))
            pennies_input = int(input("Please insert pennies: "))

            customer_coin_value = calculate_coins(quarters_input, dimes_input, nickles_input, pennies_input)
            if check_transaction(customer_coin_value, customer_choice['cost']):
                resources = update_resources(resources, customer_choice['ingredients'])

    else:
        print('Please enter valid credentials.')
