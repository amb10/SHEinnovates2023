from FoodItem import FoodItem
from GroceryList import GroceryList
from frntHomeRef import frntHomeRef
from inventory import inventory

@app.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username)