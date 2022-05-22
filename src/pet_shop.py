# WRITE YOUR FUNCTIONS HERE
from unicodedata import name


def get_pet_shop_name(pet_shop):
    name = pet_shop["name"]
    return name

def get_total_cash(pet_shop):
    sum = pet_shop["admin"]["total_cash"]
    return int(sum)

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    return amount
    

def get_pets_sold(pet_shop):
    pets_sold = pet_shop["admin"]["pets_sold"]
    return pets_sold

def increase_pets_sold(pet_shop, pet_sales):
    pet_shop["admin"]["pets_sold"] += pet_sales
    return pet_sales

def get_stock_count(pet_shop):
    stock_count = 0
    for pet in pet_shop["pets"]:
        stock_count += 1
    return stock_count

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop, pet_name):
    for index, pet in enumerate(pet_shop["pets"]):        
       if pet["name"] == pet_name:
            pet_shop["pets"].pop(index)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append({
                    "name": "Raffles",
                    "pet_type": "dog",
                    "breed": "Border Collie",
                    "price": 800
                })
    count = 0
    for pet in pet_shop["pets"]:
        count += 1
    return count    

def get_customer_cash(customers):
    cash = customers["cash"]
    return cash

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
    return amount

def get_customer_pet_count(customers):
    count = 0
    for pet in customers["pets"]:
        count += 1
    return count

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    
def customer_can_afford_pet(customer, new_pet):
    if new_pet["price"] > customer["cash"]:
        return False
    else:
        return True


def sell_pet_to_customer(pet_shop, pet, customer):
        add_pet_to_customer(customer, pet)
        pet_shop["admin"]["pets_sold"] += 1 # should be able to use functions
        get_pets_sold(pet_shop)
        amount = pet["price"]
        remove_customer_cash(customer, amount)
        get_customer_cash(customer)
        add_or_remove_cash(pet_shop, amount)

    
# def sell_pet_to_customer(pet_shop, pet, customer):
#     for index, pet in enumerate(pet_shop["pets"]):        
#        if pet_shop["pets"][index]["name"] == pet:        
#             add_pet_to_customer(customer, pet)
#             pet_shop["admin"]["pets_sold"] += 1 # should be able to use functions
#             get_pets_sold(pet_shop)
#             amount = pet["price"]
#             remove_customer_cash(customer, amount)
#             get_customer_cash(customer)
#             add_or_remove_cash(pet_shop, amount)
#     # else: 
#     #     pass
