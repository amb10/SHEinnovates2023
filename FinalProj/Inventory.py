from FoodItem import FoodItem
from flask import Flask, render_template, request
from datetime import date
import os


# Flask stuff
app = Flask(__name__)

# Master inventory:
masterInventory = []
addedItem = []

# Today's date
today = [date.today().month, date.today().day, date.today().year]


# Banner stuff
picFolder = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picFolder

# Inventory Screen
@app.route('/inventory', methods = ['POST', 'GET'])
def inventory():

    banner = os.path.join(app.config['UPLOAD_FOLDER'], 'banner3.jpeg')

    print("DEBUG LINE: INVENTORY FUNCTION")

    if request.method == "POST":
        print(request.form)
        # Delete an item from the inventory
        if request.form.__contains__("Delete"):
            quantity = request.form.get("Quantity")
            deleted = False
            for item in masterInventory:
                if item.get_name() == request.form.get("Delete"):
                    deleted = True
                    if (int(quantity) >= int(item.get_inventory())):
                        print(quantity)
                        print(item.get_inventory)
                        print("remove all")
                        masterInventory.remove(item)
                    elif (int(quantity) < int(item.get_inventory()) and int(quantity) > 0):
                        print("remove some")
                        item.set_inventory(int(item.get_inventory()) - int(quantity))
                    elif(int(quantity) < 0):
                        print('negative quantity')
                    print("deleted")

            if (deleted == False):
                print("did not delete")
            debugPrint()

        # Add an item to the inventory
        elif request.form.__contains__("Name"):

            # Creating and intializing a new item
            newItem = FoodItem(request.form.get("Name"), [00, 00, 0000])
            newItem.set_expiration([request.form.get("Month"), request.form.get("Day"), request.form.get("Year")])
            newItem.set_inventory(request.form.get("Quantity"))
            newItem.set_allergens(request.form.get("GF"), request.form.get("DF"), request.form.get("NF"), request.form.get("Vegan"), request.form.get("Vegetarian"))

            # Adding new item to the overall master inventory
            masterInventory.append(newItem)
            
            debugPrint()
        
        elif request.form.__contains__("SortName"):
            sortName()

        elif request.form.__contains__("SortDateDescending"):
            sortDateDescending()

        elif request.form.__contains__("SortDateAscending"):
            sortDateAscending()
        
    # Loading the page
    if request.method == "GET":
        print("Page")
        print("CALling debug print:")
        debugPrint()

    return render_template("inventory.html", object_list = masterInventory, user_image = banner)


# Updates the expiration of a FoodItem object
def updateExpiration(expiration, intake):
    print("updating expiration")

    if(int(expiration[2]) < int(intake[2])):          # expiration year is before current year
        print("1")
        return True
    elif(int(expiration[2]) > int(intake[2])):        # expiration year is after current year
        print("2")
        return False
    else:                                   # expiration year is this year
        if(int(expiration[0]) > int(intake[0])):          # BUT it is after this month
            print("3")
            return False
        elif(int(expiration[0]) < int(intake[0])):        # BUT it is before this month
            print("4")
            return True
        else:                                   # BUT it is this month
            if(int(expiration[1]) > int(intake[1])):          # AND expiration date is later
                print("5")
                return False
            elif(int(expiration[1]) < int(intake[1])):        # AND expiration date passed
                print("6")
                return True
            else:                                   # AND expiration date is today
                print("7")
                return False            

def debugPrint():
    print("DEBUG PRINT")
    print("master inventory:", end = " ")
    print(masterInventory)
    print("breakdown:")
    # for item in masterInventory:
    #     print(item.name)
    #     print(item.intake)
    #     print(item.expiration)
    #     print(item.inventory)
    #     print(item.glutenFree)
    #     print(item.dairyFree)
    #     print(item.nutFree)
    #     print(item.vegan)
    #     print(item.vegetarian)
    #     print(item.expired)


def sortName():
    print("Sorting by name")
    masterInventory.sort(key=lambda x: x.get_name().lower())
    debugPrint()

def sortDateDescending():
    print("Sorting by date descending")
    masterInventory.sort(key=lambda x: x.get_expiration()[0], reverse=True)
    masterInventory.sort(key=lambda x: x.get_expiration()[1], reverse=True)
    masterInventory.sort(key=lambda x: x.get_expiration()[2], reverse=True)
    debugPrint()

def sortDateAscending():
    print("Sorting by date ascending")
    masterInventory.sort(key=lambda x: x.get_expiration()[0], reverse=False)
    masterInventory.sort(key=lambda x: x.get_expiration()[1], reverse=False)
    masterInventory.sort(key=lambda x: x.get_expiration()[2], reverse=False)
    debugPrint()
