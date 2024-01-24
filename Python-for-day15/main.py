from menu import MENU, resources
profit = 0


# TODO: 1 machine check
def machine_check():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"profit: $ {profit}")


# TODO: 2 check the sufficiency of the resources
def check_sufficiency(order_ingredients):
    """当材料充足返回‘真’，否则为‘否’"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("😟 Sorry, there is not enough {item}.")
            return False
    print("😁 Here is available to enjoy a coffee.")
    return True


# TODO: 3 process coins
def count_coins():
    """返回值总共多少钱（不懂外国人的coin的说法）"""
    print("Please insert your coin:")
    total = int(input("How many loonies:"))
    total += int(input("How many quarters:")) * 0.25
    total += int(input("How many dimes:")) * 0.1
    total += int(input("How many nickels:")) * 0.05
    total += int(input("How many pennies:")) * 0.01
    return total


# TODO: 4 check transition successful or not
def transaction(get_money, drink_cost):
    """返回'真'为够钱并收钱了，'否'为不够钱并返钱"""
    if get_money >= drink_cost:
        change = round(get_money - drink_cost, 2)
        print(f"Here are your change ${change} ")
        global profit
        profit += drink_cost
        return True
    else:
        print("😖 Sorry that's not enough money. Money refunded. ")
        return False


# TODO: 5 make coffee
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕, enjoy!")


is_on = True
while is_on:
    print("espresso $1.5 /latte $2.5 /cappuccino $3")
    choice = input("Please select your option:\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        machine_check()
    else:
        drink = MENU[choice]  # dict
        if check_sufficiency(drink["ingredients"]):
            payment = count_coins()
            transaction(payment, drink["cost"])
            make_coffee(choice, drink["ingredients"])
