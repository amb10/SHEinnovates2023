import FoodItem

class GroceryList:
    #intializes a list of FoodItems that does NOT accept duplicates
    def __init__(self):
        self.grocery_list = []

    #accepts Strings items as parameters
    #public method to add items
    def add(self, item):
        #adds item if list is empty
        if (len(self.grocery_list) == 0):
            print("Entered first add")
            self.__add_item(item)

        #verifies item is not in list
        try:
            self.grocery_list.index(item)
            return #returns if item already in list
        except ValueError:
            self.__add_item(item)
            print("Entered adds")

    #private method to add items internally
    def __add_item(self, name):
        self.grocery_list.append(name)

    #accepts String items as parameters
    #public method that checks conditions
    def cross_off(item):
        #returns from function if list is empty
        if (len(self.grocery_list) == 0):
            return

        #deletes item if in list and returns if
        #item not found in list
        try:
            i = self.grocery_list.index(item)
            self.grocery_list.pop(i)
        except ValueError:
            return
    
    #returns a copy of grocery list
    def get_list(self):
        return self.grocery_list.copy()

    #returns item if found and None if not found
    def get_item(self, item):
        try:
            i = self.grocery_list.index(item)
            return self.grocery_list[i]
        except ValueError:
            return None

    #returns a copy of sorted list
    def sort_alpha(self):
        self.grocery_list.sort()
        return self.grocery_list.copy()