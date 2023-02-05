import FoodItem
from flask import Flask, render_template, request
from datetime import date

class GroceryList:
    #intializes a list of FoodItems that does NOT accept duplicates
    def __init__(self):
        self.grocery_list = []

    #accepts Strings items as parameters
    #public method to add items
    def add(self, item):
        #adds item if list is empty
        if (len(self.grocery_list) == 0):
            self.__add_item(item)
            return

        #verifies item is not in list
        try:
            self.grocery_list.index(item)
            return #returns if item already in list
        except ValueError:
            self.__add_item(item)
            return

    #private method to add items internally
    def __add_item(self, name):
        self.grocery_list.append(str(name))

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
            i = self.grocery_list.index(str(item))
            return self.grocery_list[int(i)]
        except ValueError:
            return None

    #returns a copy of sorted list
    def sort_alpha(self):
        self.grocery_list.sort()
        return self.grocery_list.copy()
#end of GroceryList class definition

app = Flask(__name__)

grocery_unordered = []

@app.route('/GroceryList', methods = ['POST', 'GET'])
def Grocery():
    newItem = GroceryList()
    print(request.form)
    if request.method == "POST":

        if request.form.__contains__("Add Item"):
            addedItem = request.form.get("Add Item")
            newItem.add(addedItem)

            grocery_unordered.append(addedItem)
            print(grocery_unordered)

        elif request.form.__contains__("Delete Item"):
            #will be added to

    
    # Loading the page
    if request.method == "GET":
        print("Page")
        print("Calling debug print:")
    return render_template('GroceryList.html', object_list = grocery_unordered)

app.run(host='localhost', port=5000)