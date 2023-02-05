from FoodItem import FoodItem
import GroceryList
import frntHomeRef
import Inventory
from FoodItem import FoodItem
from flask import Flask, render_template, request
from datetime import date
import os

app = Flask(__name__)

@app.route("/")
def index():
    return frntHomeRef.index()

@app.route('/inventory', methods = ['POST', 'GET'])
def inventory():
    return Inventory.inventory()

@app.route('/GroceryList', methods = ['POST', 'GET'])
def Grocery():
    return GroceryList.Grocery()
