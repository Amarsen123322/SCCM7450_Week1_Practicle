def celsius_to_fahrenheit(celsius):   # 1. name  2. input in brackets, then a colon
    fahrenheit = celsius * 1.8 + 32   # 3. indented body does the work
    return fahrenheit                 # 4. return sends the result back out

def cups_to_ml(cups):
    ml = cups *  236.588
    return ml
# print(cups_to_ml(1))
# print(cups_to_ml(5))
# print(cups_to_ml(10))

def ml_to_grams(ml, density):
    grams = ml * density
    return grams

def cups_to_grams(no_of_cups, ingredient="water"):
    ml = cups_to_ml(no_of_cups)

    ingredient = ingredient.lower()      # "Oat Milk" → "oat milk"

    if ingredient == "water":
        specific_weight = 1
    elif ingredient == "flour":
        specific_weight = 0.53
    elif ingredient == "oil":
        specific_weight = 0.92
    elif ingredient == "oat milk":
        specific_weight = 1.03
    else:
        raise ValueError("Unknown ingredient: " + ingredient)

    print(specific_weight)               # temporary check, delete later
    return ml



# print(cups_to_grams(2))            # 473.176
# print(cups_to_grams(5))            # 1182.94
# print(cups_to_grams(2, "flour"))   # 473.176
#
# def total_price(quantity, unit_price):
#     return quantity * unit_price
#
# def basket_total(quantity, fruit="apple"):
#     if fruit == "apple":
#         unit_price = 0.50
#     elif fruit == "mango":
#         unit_price = 1.20
#     else:
#         raise ValueError("Unknown fruit: " + fruit)
#
#     total = total_price(quantity, unit_price)   # call the helper with 2 inputs
#     return total                                # hand the result back
#
# print(basket_total(4, "mango"))   # 4 × 1.20 = 4.8

import numpy as np

def distance(a, b, metric="euclidean"):
    gaps = b - a
    if metric == "euclidean":
        return np.sqrt(np.sum(gaps ** 2))
    elif metric == "manhattan":
        return np.sum(np.abs(gaps))

U = np.array([2, -1, 0])
V = np.array([1, 3, 8])
print(distance(U, V))
print(distance(U, V, "manhattan"))