from datetime import date
from flask import request

#FoodItem class defines data fields related to food items and returns them
class FoodItem:
    # data fields:

    # basic info:
    name = "default"
    category = "default" # for example: can, box, produce, jar, etc.
    intake = [00, 00, 0000] # mm/dd/yyyy
    expiration = [00, 00, 0000] # mm/dd/yyyy

    # amount
    inventory = 0 # keeps track of # of items

    # booleans:
    expired = False         # create a method to update this like in main or something that runs often/ every use
    glutenFree = False
    dairyFree = False
    nutFree = False
    vegan = False
    vegetarian = False
    
    def __init__ (self, name, expiration):
        # setting intake date
        today = date.today()
        intake = [today.month, today.day, today.year]

    def test(void):
        return 0
