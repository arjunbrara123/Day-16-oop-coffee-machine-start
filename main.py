from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

usrReq = ""
cm = CoffeeMaker()
cm_menu = Menu()
mm = MoneyMachine()

while usrReq != "No":
    usrReq = input(f"What would you like? ({cm_menu.get_items()}): ").lower()
    if usrReq == "no":
        break
    elif usrReq == "report":
        cm.report()
    else:
        drink = cm_menu.find_drink(usrReq)
        if drink != None:
            if cm.is_resource_sufficient(drink):
                if mm.make_payment(drink.cost):
                    cm.make_coffee(drink)
