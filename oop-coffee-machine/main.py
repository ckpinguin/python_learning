from art import logo
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()


def main_loop():
    running = True
    while running:
        choice = input(
            f"Welcome! Please choose drink from {menu.get_items()}: ")
        if choice == "off":
            running = False
            break
        elif choice == "report":
            coffeeMaker.report()
            moneyMachine.report()
            continue
        drink = menu.find_drink(choice)
        if not drink:
            print("Invalid choice")
            continue
        if coffeeMaker.is_resource_sufficient(drink):
            moneyMachine.make_payment(drink.cost)
            coffeeMaker.make_coffee(drink)
        else:
            print("Insufficient resources: ")
            coffeeMaker.report()

    print("Turning machine off...")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(logo)
    main_loop()
