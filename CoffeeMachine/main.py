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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


choice = input("What would you like? (espresso/latte/cappuccino): ")
if choice == "off":
    quit()



def report():
    for key, value in resources.items():
        print(f"{key}: {value}")



def check_resources():
    for key in resources:
        if (MENU[choice]["ingredients"][key]) > resources[key]:
            return(f"Sorry there is not enough {key}")
    else:
        print("thanks")
# if MENU[x][0] == r