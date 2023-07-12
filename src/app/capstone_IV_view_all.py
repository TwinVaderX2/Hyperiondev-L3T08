# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:20:49 2023

@author: Phillip van Staden

Task 

Description:
    
    Contains functions for 'view all window'
    
"""
# import modules
import tkinter as tk
import babel.numbers

# import capstone modules
from capstone_IV_general import *
from capstone_IV_add_item import add_item

def view_all(root):
    # create new window
    view_all_win = tk.Toplevel()
    view_all_win.geometry("930x600")
    view_all_win.title("View Inventory")
    
    # add_menubar
    m = Menubar(view_all_win, root)

    #center window in screen
    center(view_all_win)
    
    # create canvas
    canvas = tk.Canvas(view_all_win)
    # create scrollbar
    scroll_y = tk.Scrollbar(view_all_win,orient = "vertical",command = canvas.yview)
    
    # create frame
    global inventory_frame
    inventory_frame = tk.Frame(canvas)   
    
    # create border frame
    black_border1 = tk.Frame(view_all_win,background = "black")
    black_border2 = tk.Frame(view_all_win,background = "black")
    black_border3 = tk.Frame(view_all_win,background = "black")
    black_border4 = tk.Frame(view_all_win,background = "black")
    black_border5 = tk.Frame(view_all_win,background = "black")
    
    # add column labels
    country_lab = tk.Label(black_border1,text = "Country",
                           font = "ariel 12 underline",
                            background = "#9E9EA0", bd = 0.5,
                            width = 18
                           ).grid(row = 0, column = 0, padx = 2, pady = 2)
    black_border1.grid(row = 0, column = 0,padx = 5, pady = 5, sticky = "w")
    
    code_lab = tk.Label(black_border2,text = "Item Code",
                           font = "ariel 12 underline",
                           background = "#9E9EA0", bd = 0.5,
                           width = 18
                           ).grid(row = 0, column = 1, padx = 2, pady = 2)
    black_border2.grid(row = 0, column = 1,padx = 5, pady = 5, sticky = "w")
    
    product_lab = tk.Label(black_border3,text = "Product Description",
                           font = "ariel 12 underline",
                           background = "#9E9EA0", bd = 0.5,
                           width = 18
                           ).grid(row = 0, column = 2, padx = 2, pady = 2)
    black_border3.grid(row = 0, column = 2,padx = 5, pady = 5, sticky = "w")
    
    cost_lab = tk.Label(black_border4,text = "Cost per Item",
                           font = "ariel 12 underline",
                           background = "#9E9EA0", bd = 0.5,
                           width = 18
                           ).grid(row = 0, column = 3, padx = 2, pady = 2)
    black_border4.grid(row = 0, column = 3,padx = 5, pady = 5, sticky = "w")
    
    qty_lab = tk.Label(black_border5,text = "Quantity",
                           font = "ariel 12 underline",
                           background = "#9E9EA0", bd = 0.5,
                           width = 18
                           ).grid(row = 0, column = 4, padx = 2, pady = 2)
    black_border5.grid(row = 0, column = 4,padx = 5, pady = 5, sticky = "w")
    
    # add entry widgets to frame
        
    view_inventory(root)
    
    # put inventory_frame in canvas
    canvas.create_window(0,600, anchor = "center", window = inventory_frame)
    canvas.update_idletasks()
    # config scroll area
    canvas.configure(scrollregion=canvas.bbox('all'), 
                 yscrollcommand = scroll_y.set)
    # place widgets using grid method
    canvas.grid(row = 1, column = 0, columnspan = 5,
                sticky = ("ew","ns"))
    scroll_y.grid(row = 1, column = 5, sticky = tk.NS)
    
    
    #add buttons
    refresh_but = tk.Button(view_all_win, text = "Refresh List",
                        command = lambda : view_inventory(root),
                        font = "ariel 9", width = 15, height = 1
                        ).place(x = 530,y = 320)
    
    add_but = tk.Button(view_all_win, text = "Add Item",
                        command = lambda : add_item(root),
                        font = "ariel 9", width = 15, height = 1
                        ).place(x = 650,y = 320)
    
    update_but = tk.Button(view_all_win, text = "Update Inventory",
                        command = lambda : update_inventory(inventory_frame),
                        font = "ariel 9", width = 15, height = 1
                        ).place(x = 770,y = 320)
    
    
    back_but = tk.Button(view_all_win,text = "Back",
                         font = "ariel 9", width = 15, height = 2,
                         command = view_all_win.destroy
                         ).place(x = 630,y = 550)
    
    exit_but = tk.Button(view_all_win,text = "Exit",
                         font = "ariel 9", width = 15, height = 2,
                         command = root.destroy
                         ).place(x = 750,y = 550)

def view_inventory(root):
    inventory = get_inventory()
    item_price = 0
    for idx in range(len(inventory.inventory_list)):
        country_ent = tk.Entry(inventory_frame,highlightthickness = 2, width = 27)
        country_ent.config(background = "white", highlightcolor = "#6AD7DC")
        # add item info to entry widget
        country_ent.insert(0, inventory.inventory_list[idx].country)
        country_ent.grid(row = idx, column = 0, padx = 5, pady = 5, sticky = "w")
        
        code_ent = tk.Entry(inventory_frame,highlightthickness = 2, width = 27)
        code_ent.config(background = "white", highlightcolor = "#6AD7DC")
        # add item info to entry widget
        code_ent.insert(0,inventory.inventory_list[idx].code)
        code_ent.grid(row = idx, column = 1, padx = 5, pady = 5, sticky = "w")
        
        product_ent = tk.Entry(inventory_frame,highlightthickness = 2, width = 27)
        product_ent.config(background = "white", highlightcolor = "#6AD7DC")
        # add item info to entry widget
        product_ent.insert(0,inventory.inventory_list[idx].product)
        product_ent.grid(row = idx, column = 2, padx = 5, pady = 5, sticky = "w")
        
        cost_ent = tk.Entry(inventory_frame,highlightthickness = 2, width = 27)
        cost_ent.config(background = "white", highlightcolor = "#6AD7DC")
        # add item info to entry widget
        item_price = babel.numbers.format_currency(float(inventory.inventory_list[idx].cost), "R")
        cost_ent.insert(0,item_price)
        cost_ent.grid(row = idx, column = 3, padx = 5, pady = 5, sticky = "w")
        
        qty_ent = tk.Entry(inventory_frame,highlightthickness = 2, width = 27)
        qty_ent.config(background = "white", highlightcolor = "#6AD7DC")
        # add item info to entry widget
        qty_ent.insert(0,inventory.inventory_list[idx].qty)
        qty_ent.grid(row = idx, column = 4, padx = 5, pady = 5, sticky = "w")

def update_inventory(frame):
    
    # create new inventory
    inventory = Inventory()
    
    # retrieve amendments/ changes from screen
    # create list of widgets (this list is not arranged per entry/ item)
    widget_list = frame.grid_slaves()
    
    # to sort according to each line/entry; create 2d list of entry_widgets
    # create list of 5 for length of widget list; this will help split the list
    len_list = []
    for idx in range(int(len(widget_list)/5)):
        len_list.append(5)

    # create 2d list of widgets
    list_2d = []
    idx = 0 
    for var_len in len_list:
        list_2d.append(widget_list[idx:idx + var_len])
        idx += var_len
    
    # run through 2d list in reverse to ensure the inventory is read from top to bottom
    for idx in list_2d[::-1]:
        # add new item for each line/ entry
        inventory.add_item(idx[-1].get(), idx[-2].get(), idx[-3].get(), float(idx[-4].get().translate({ord(i): None for i in "R ,"})), int(idx[-5].get()))
    
    # re-write source
    with open(source.source,"w") as f:
        f.write("Country,Code,Product,Cost,Quantity")
    
    # append inventory to new source
    with open(source.source,"a") as f:
        for idx in inventory.inventory_list:
            f.write("\n"+idx.country+","+idx.code+","+idx.product+","+str(idx.cost)+","+str(idx.qty))