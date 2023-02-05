from datetime import date
from flask import request

#FoodItem class defines data fields related to food items and returns them
class FoodItem:
    #def __init__ (name, expiration, category, inventory, intake) for food bank
    #def __init__ (name, expiration) for average person
    def __init__ (self, *args):
        if len(args) <= 3:
            self.__today = date.today() # setting intake date to today
            self.__intake = [self.__today.month, self.__today.day, self.__today.year] # [mm,dd,yyyy]
            self.__name = args[0]
            self.__category = "default" # for example: can, box, produce, jar, etc.
            self.__expiration = args[1] # [mm,dd,yyyy]
            self.__inventory = 0
            #self.FoodItem(name, expiration, "default", 0, [today.month, today.day, today.year])

    #constructor for average person's FoodItem
    #def __init__ (self, name, expiration):
        #setting categorical variables
        #self.__today = date.today() # setting intake date to today
        #self.FoodItem(name, expiration, "default", 0, [today.month, today.day, today.year])

    #constructor for food bank's FoodItem
    #def __init__ (self, name, expiration, category, inventory, intake):
        #setting categorical variables
        else:
            self.__intake = args[4] # [mm,dd,yyyy]
            self.__name = args[0]
            self.__category = args[2] # for example: can, box, produce, jar, etc.
            self.__expiration = args[1] # [mm,dd,yyyy]
            self.__inventory = args[3]
            self.__today = date.today() # setting intake date to today

        #checks if item is expired
        if self.is_expired():
            self.__expired = True
        else:
           self.__expired = False

        #sets allergens to false - can be
        #changed in set_allergens()
        self.__glutenFree = False
        self.__dairyFree = False
        self.__nutFree = False
        self.__vegan = False
        self.__vegetarian = False

    #checks if item is expired by comparing year, month, then day
    def is_expired(self):
        #if expired before this year
        if self.__expiration[2] < self.__today.year:
            return True
        else:
            #if expired before this month
            if self.__expiration[0] < self.__today.month:
                return True
            else:
                #if expired before this day
                if self.__expiration[1] < self.__today.day:
                    return True
                else:
                    return False

    #sets all of the allergen fields to true/false
    def set_allergens(self, glutenFree, dairyFree, nutFree, vegan, vegetarian):
        self.__glutenFree = glutenFree
        self.__dairyFree = dairyFree
        self.__nutFree = nutFree
        self.__vegan = vegan
        self.__vegetarian = vegetarian

    #returns true if any allergen field is true
    def check_allergens(self):
        if self.__glutenFree or self.__dairyFree or self.__nutFree or self.__vegan or self.__vegetarian:
            return True
        else:
            return False

    #sets name data field
    def set_name(self, name):
        self.__name = name
    
    #returns name data field
    def get_name(self):
        return self.__name
    
    #sets expiration data field
    def set_expiration(self, expiration):
        self.__expiration = expiration
    
    #returns expiration data field
    def get_expiration(self):
        return self.__expiration
    
    #sets category data field
    def set_category(self, category):
        self.__category = category
    
    #returns category data field
    def get_category(self):
        return self.__category
    
    #sets inventory data field
    def set_inventory(self, inventory):
        self.__inventory = inventory
    
    #returns inventory data field
    def get_inventory(self):
        return self.__inventory
    
    #sets intake data field
    def set_intake(self, intake):
        self.__intake = intake

    #returns intake data field
    def get_intake(self):
        return self.__intake