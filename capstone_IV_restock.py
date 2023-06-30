# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:49:33 2023

@author: Phillip van Staden

Task 

Description:
    
    Contains functions and classes for 'Restock Item'
    
"""

# import modules
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import babel.numbers

#import capstone modules
from capstone_IV_general import *

def restock(root):
    """
    Function creates new window and displays item with the lowest stock_qty
    Gives user ability to restock the item

    Parameters
    ----------
    root : Tk()
        Main/Root window.

    Returns
    -------
    None.

    """
    
    # create new window
    restock_win = tk.Toplevel()
    restock_win.title("Item On Sale")
    restock_win.geometry("900x350")
    
    # center window
    center(restock_win)
    
    # add menubar
    m = Menubar(restock_win, root)
    
    # add label
    label1 = tk.Label(restock_win, text = "The item listed below needs to be restocked",
                      font = "ariel 12 underline"
                      ).grid(row = 0, column = 1, columnspan = 2,
                             padx = 5, pady = 5, sticky = "e")

    # create border frame
    black_border1 = tk.Frame(restock_win,background = "black")
    black_border2 = tk.Frame(restock_win,background = "black")
    black_border3 = tk.Frame(restock_win,background = "black")
    black_border4 = tk.Frame(restock_win,background = "black")
    black_border5 = tk.Frame(restock_win,background = "black")
    
    # add column labels to frames
    country_lab = tk.Label(black_border1,text = "Country",
                           font = "ariel 12 underline",
                            background = "#9E9EA0", bd = 0.5,
                            width = 18
                           ).grid(row = 0, column = 0, padx = 2, pady = 2)
    black_border1.grid(row = 1, column = 0,padx = 5, pady = 5, sticky = "w")
    
    code_lab = tk.Label(black_border2,text = "Item Code",
                           font = "ariel 12 underline",
                           background = "#9E9EA0", bd = 0.5,
                           width = 18
                           ).grid(row = 0, column = 1, padx = 2, pady = 2)
    black_border2.grid(row = 1, column = 1,padx = 5, pady = 5, sticky = "w")
    
    product_lab = tk.Label(black_border3,text = "Product Description",
                           font = "ariel 12 underline",
                           background = "#9E9EA0", bd = 0.5,
                           width = 18
                           ).grid(row = 0, column = 2, padx = 2, pady = 2)
    black_border3.grid(row = 1, column = 2,padx = 5, pady = 5, sticky = "w")
    
    cost_lab = tk.Label(black_border4,text = "Cost per Item",
                           font = "ariel 12 underline",
                           background = "#9E9EA0", bd = 0.5,
                           width = 18
                           ).grid(row = 0, column = 3, padx = 2, pady = 2)
    black_border4.grid(row = 1, column = 3,padx = 5, pady = 5, sticky = "w")
    
    qty_lab = tk.Label(black_border5,text = "Quantity",
                           font = "ariel 12 underline",
                           background = "#9E9EA0", bd = 0.5,
                           width = 18
                           ).grid(row = 0, column = 4, padx = 2, pady = 2)
    black_border5.grid(row = 1, column = 4,padx = 5, pady = 5, sticky = "w")    
    
    # call insert_data function to add entry widgets with data
    insert_data(restock_win, root)
    
    # add buttons
    restock_but = tk.Button(restock_win,text = "Restock",
                          font = "ariel 9", width = 15, height = 2,
                           command = lambda : update_inventory(restock_win, root)
                          ).place(x = 660,y = 110)
    
    refresh_but = tk.Button(restock_win,text = "Refresh",
                          font = "ariel 9", width = 15, height = 2,
                          command = lambda : insert_data(restock_win,root)
                          ).place(x = 780,y = 110)
    back_but = tk.Button(restock_win,text = "Back",
                         font = "ariel 9", width = 15, height = 2,
                         command = restock_win.destroy
                         ).place(x = 660,y = 300)
    
    exit_but = tk.Button(restock_win,text = "Exit",
                         font = "ariel 9", width = 15, height = 2,
                         command = root.destroy
                         ).place(x = 780,y = 300)
    
def insert_data(win,root):
    """
    Function adds entry widgets to window and populates data
    for stock_item with lowest stock_qty

    Parameters
    ----------
    win : Toplevel()
        Restock window.
    root : Tk()
        Root/main window.

    Returns
    -------
    None.

    """
    # set global variable
    inventory = get_inventory()
    lowest_stock_on_hand = inventory.lowest_stock_on_hand()
    
    for idx in inventory.inventory_list:
        if idx.code == lowest_stock_on_hand:
            # add entry widgets
            country_ent = tk.Entry(win,highlightthickness = 2, width = 27)
            country_ent.config(background = "white", highlightcolor = "#6AD7DC")
            # add item info
            country_ent.insert(0,idx.country)
            country_ent.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
            
            code_ent = tk.Entry(win,highlightthickness = 2, width = 27)
            code_ent.config(background = "white", highlightcolor = "#6AD7DC")
            # add item info
            code_ent.insert(0,idx.code)
            code_ent.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "w")
            
            product_ent = tk.Entry(win,highlightthickness = 2, width = 27)
            product_ent.config(background = "white", highlightcolor = "#6AD7DC")
            # add item info
            product_ent.insert(0,idx.product)
            product_ent.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "w")
            
            cost_ent = tk.Entry(win,highlightthickness = 2, width = 27)
            cost_ent.config(background = "white", highlightcolor = "#6AD7DC")
            # add item info
            item_cost = babel.numbers.format_currency(int(idx.cost), "ZAR", locale = "en_ZA")
            cost_ent.insert(0,item_cost)
            cost_ent.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "w")
            
            qty_ent = tk.Entry(win,highlightthickness = 2, width = 27)
            qty_ent.config(background = "white", highlightcolor = "#6AD7DC")
            # add item info
            qty_ent.insert(0,idx.qty)
            qty_ent.grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "w")
            
def update_inventory(win,root):
    """
    Function retrieves information from user
    Updates inventory list
    Writes new inventory to source

    Parameters
    ----------
    win : Toplevel()
        Restock window.
    root : Tk()
        Root/main window.

    Returns
    -------
    None.

    """
    
    # create list of widgets
    widget_list = win.grid_slaves()
    
    # set variable
    inventory = get_inventory()
    
    for idx in inventory.inventory_list:
        if idx.code == widget_list[3].get():
            idx.change_qty(widget_list[0].get())
            
    # write new inventory to source
    with open(source.source,"w") as f:
        f.write("Country,Code,Product,Cost,Quantity")
    
    with open(source.source,"a") as f:
        for idx in inventory.inventory_list:
            f.write("\n"+idx.country+","+idx.code+","+idx.product+","+str(idx.cost)+","+str(idx.qty))
        
        