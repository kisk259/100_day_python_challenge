from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def machine():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    power = True
    machine_money = 0.0

    while power:
        options = menu.get_items()
        command = input(f"What would you like? ({options}): ")
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
            coffee_maker.report()
            money_machine.report()
        elif command == "off":
            print("The machine is turning off!")
            power = False
        else:
            print("Wrong command please select from the list!")


machine()