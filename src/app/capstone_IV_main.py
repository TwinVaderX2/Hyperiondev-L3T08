# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:42:19 2023

@author: Phillip van Staden

Task Capstone project IV - OOP SE T1L30

Description:
Code a Python program that will read from the text file inventory.txt and
perform the following on the data, to prepare for presentation to your
managers:
o   We've provided a template for you in a file named inventory.py.
o   Inside this file, you will find a class named Shoe with the following
    attributes:
    ●   country,
    ●   code,
    ●   product,
    ●   cost, and
    ●   quantity.
o   Inside this class define the following methods:
    ▪   get_cost - Returns the cost of the shoes.
    ▪   get_quantity - Returns the quantity of the shoes.
    ▪   __str__ - This method returns a string representation of a
        class.
o   Outside this class create a variable with an empty list. This variable
    will be used to store a list of shoes objects
o   Then you must define the following functions outside the class:
    ▪   read_shoes_data - This function will open the file
        inventory.txt and read the data from this file, then create a
        shoes object with this data and append this object into the
        shoes list. One line in this file represents data to create one
        object of shoes. You must use the try-except in this function
        for error handling. Remember to skip the first line using your
        code.
    ▪   capture_shoes - This function will allow a user to capture
        data about a shoe and use this data to create a shoe object
        and append this object inside the shoe list.
    ▪   view_all - This function will iterate over the shoes list and
        print the details of the shoes returned from the __str__
        function. Optional: you can organise your data in a table
        format by using Python's tabulate module.
    ▪   re_stock - This function will find the shoe object with the
        lowest quantity, which are the shoes that need to be
        re-stocked. Ask the user if they want to add this quantity of
        shoes and then update it. This quantity should be updated
        on the file for this shoe.
    ▪   seach_shoe - This function will search for a shoe from the list
        using the shoe code and return this object so that it will be
        printed.
    ▪   value_per_item - This function will calculate the total value
        for each item . Please keep the formula for value in mind;
        value = cost * quantity. Print this information on the console
        for all the shoes.
    ▪   highest_qty - Write code to determine the product with the
        highest quantity and print this shoe as being for sale.
    
o   Now in your main create a menu that executes each function
above. This menu should be inside the while loop. Be creative!
"""
# import modules
import os

import tkinter as tk
from PIL import Image, ImageTk

# import capstone_IV project modules
from capstone_IV_general import *
from capstone_IV_view_all import *
from capstone_IV_add_item import *
from capstone_IV_search_item import *
from capstone_IV_stock_value import *
from capstone_IV_on_sale import *
from capstone_IV_restock import *

# create root window
root = tk.Tk()
root.geometry("450x300")
root.title("Stock Manager")
center(root)

# change window icon
icon = Image.open(os.path.abspath("src/images/twinvader_icon.png"))
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(True,photo)

# add menu bar
menubar = tk.Menu(root)
root.config(menu = menubar)
file_menu = tk.Menu(menubar)
# add menu item that allows user to change the directory for inventory
file_menu.add_command(label = "Import Inventory", command = lambda : change_source_win(root))
# add menu item that will terminate program
file_menu.add_command(label = "Exit", command = root.destroy)

# add file menu to menubar
menubar.add_cascade(label = "File", menu = file_menu)

# add label
heading_lab = tk.Label(root,text = "Please choose from options below:",
                       font = "ariel 12 bold underline"
                       ).grid(row = 0, column = 0, columnspan = 2)

# add images/logos
nike_logo = Image.open(os.path.abspath("src/images/nike.png"))
nike_logo = nike_logo.resize((80,50))
nike_logo = ImageTk.PhotoImage(nike_logo)

addidas_logo = Image.open(os.path.abspath("src/images/addidas.png"))
addidas_logo = addidas_logo.resize((80,50))
addidas_logo = ImageTk.PhotoImage(addidas_logo)

puma_logo = Image.open(os.path.abspath("src/images/puma.png"))
puma_logo = puma_logo.resize((80,50))
puma_logo = ImageTk.PhotoImage(puma_logo)

# add logos to label and place using grid
nike_lab = tk.Label(root, image = nike_logo).grid(row = 1, column = 3)
addidas_lab = tk.Label(root, image = addidas_logo).grid(row = 2, column = 3)
puma_lab = tk.Label(root, image = puma_logo).grid(row = 3, column = 3)

# add buttons
view_all_but = tk.Button(root, text = "View Inventory",
                         height = 2, width = 20,
                         command = lambda : view_all(root),
                         font = "ariel 10"
                         ).grid(row = 1, column = 0, padx = 5, pady = 10)

search_but = tk.Button(root, text = "Search Item",
                         height = 2, width = 20,
                         command = lambda: search_item(root),
                         font = "ariel 10"
                         ).grid(row = 2, column = 0, padx = 5, pady = 10)

stock_val_but = tk.Button(root, text = "Stock Value",
                         height = 2, width = 20,
                         command = lambda : stock_value(root),
                         font = "ariel 10"
                         ).grid(row = 3, column = 0, padx = 5, pady = 10)

sale_but = tk.Button(root, text = "On Sale",
                         height = 2, width = 20,
                         command = lambda : on_sale(root),
                         font = "ariel 10"
                         ).grid(row = 1, column = 1, padx = 5, pady = 10)

add_but = tk.Button(root, text = "Add Item",
                         height = 2, width = 20,
                         command = lambda : add_item(root),
                         font = "ariel 10"
                         ).grid(row = 2, column = 1, padx = 5, pady = 10)

restock_but = tk.Button(root, text = "Restock Item",
                         height = 2, width = 20,
                         command = lambda : restock(root),
                         font = "ariel 10"
                         ).grid(row = 3, column = 1, padx = 5, pady = 10)

exit_but = tk.Button(root, text = "Exit",
                         height = 1, width = 15,
                         command = root.destroy,
                         font = "ariel 8"
                         ).grid(row = 4, column = 1, padx = 5, pady = 10,
                                sticky = "e")


root.mainloop()

