from data import MENU, resources


def reporting():
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g"


def print_cost(choice):
    return float(MENU[choice]['cost'])


def check_resources(choice, resource):
    water_choice = MENU[choice]['ingredients']['water']
    coffee_choice = MENU[choice]['ingredients']['coffee']
    if 'milk' in MENU[choice]['ingredients']:
        milk_choice = MENU[choice]['ingredients']['milk']
    else:
        milk_choice = 0

    water_resource = resource['water']
    milk_resource = resource['milk']
    coffee_resource = resource['coffee']

    if (water_resource > water_choice) and (coffee_resource > coffee_choice) and (milk_resource > milk_choice):
        return True
    else:
        return False


def inserted_coins(quarters, dimes, nickels, pennies):
    ins_coins = 0
    ins_coins = ((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01))
    return ins_coins


def compere_price(coins, choice):
    if coins >= MENU[choice]['cost']:
        return True
    else:
        return False


def make_coffee(choice, resource, machine_money, coins):
    resource['water'] -= MENU[choice]['ingredients']['water']
    resource['coffee'] -= MENU[choice]['ingredients']['coffee']
    if 'milk' in MENU[choice]['ingredients']:
        resource['milk'] -= MENU[choice]['ingredients']['milk']
    else:
        resource['milk'] -= 0

    machine_money += float(MENU[choice]['cost'])
    change = coins - float(MENU[choice]['cost'])
    return machine_money, change


def machine():
    power = True
    machine_money = 0.0

    while power:
        command = input("What would you like? (espresso/latte/cappuccino): ")
        if command == "espresso" or command == "latte" or command == "cappuccino":
            choice = command

            if not check_resources(choice, resources):
                print("The machine not have enough ingredient! Please choose something else!")
            elif check_resources(choice, resources):
                print(f"Please insert {print_cost(choice)}$ to the machine:")
                quarters = int(input("How many quarters?"))
                dimes = int(input("How many dimes?"))
                nickels = int(input("How many nickels?"))
                pennies = int(input("How many pennies?"))
                coins = inserted_coins(quarters, dimes, nickels, pennies)
                print(f"You're inserted {coins}$")

                if not compere_price(coins, choice):
                    print("You not have enough coins! Here is your money! Please choose something else!")
                    quarters = 0
                    dimes = 0
                    nickels = 0
                    pennies = 0
                else:
                    machine_money, change = make_coffee(choice, resources, machine_money, coins)
                    print(f"Here is your {choice}, and here is your change: {change}$")
                    change = 0
        elif command == "report":
            print(reporting())
            print(f"Money inside the machine: {machine_money}$")
        elif command == "off":
            print("The machine is turning off!")
            power = False
        else:
            print("Wrong command please select from the list!")


machine()
