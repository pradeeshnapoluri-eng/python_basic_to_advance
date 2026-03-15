menu = {
    "espresso": {
        "items_involved":{
            "water":250,
            "milk":150,
            "coffee":25,
        },
        "cost":300
    },
    "cappuccino": {
        "items_involved":{
            "water":150,
            "milk":20,
            "coffee":30,
        },
        "cost":200
    },
    "latte": {
        "items_involved":{
            "water":50,
            "milk":30,
            "coffee":30,
        },
        "cost":150
    }
}
profit = 0
ingredients = {
    "water":500,
    "milk":200,
    "coffee":100,
}
print("Welcome to coffee machine..here the lists of coffees and their prices !")
print("latte price = 150rs")
print("cappuccino price = 200rs")
print("espresso price = 300rs")

def check_resources(ordered_drink):
    for item in ordered_drink:
        if ordered_drink[item] > ingredients[item]:
            print(f"sorry there is no enough {item}")
            return False
    return True
def receiving_coins():
    print("please insert coins here...")
    total = 0
    coins_five = int(input("insert how many 5Rs coins : "))
    coins_ten = int(input("insert how many 10Rs coins : "))
    coins_twenty = int(input("insert how many 20Rs coins : "))
    total = coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

def is_payment_successful(money_received,coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"here is your rs{change} in change.")
        return True
    else:
        print("you don't have enough money!")
        return False
def prepare_coffee(coffee_name,coffee_ingredient):
    for component in coffee_ingredient:
        ingredients[component] -= coffee_ingredient[component]
    print(f"here is your {coffee_name}....Enjoy the drink!!!")

machine_on = True
while machine_on:
    choice = input("What do you want here?(latte/espresso/cappuccino)?: ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"water = {ingredients['water']}ml")
        print(f"milk = {ingredients['milk']}ml")
        print(f"coffee = {ingredients['coffee']}gm")
        print(f"money = Rs {profit}")
    else:
        coffee_type = menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['items_involved']):
            payment = receiving_coins()
            if is_payment_successful(payment,coffee_type['cost']):
                prepare_coffee(choice,coffee_type['items_involved'])


