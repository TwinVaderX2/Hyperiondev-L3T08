# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:03:17 2023

@author: Phillip van Staden

Task 

Description:
    
    Contains functions and classes for 'On Sale'
    
"""
# import modules
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import babel.numbers

#import capstone modules
from capstone_IV_general import *


def on_sale(root):
    """
    Function creates new window that displays item with the highest stock qty

    Parameters
    ----------
    root : Tk()
        Root/main window.

    Returns
    -------
    None.

    """
    
    # create new window
    on_sale_win = tk.Toplevel()
    on_sale_win.title("Item On Sale")
    on_sale_win.geometry("900x350")
    
    # center window
    center(on_sale_win)
    
    # add menubar
    m = Menubar(on_sale_win, root)
    
    # add label
    label1 = tk.Label(on_sale_win, text = "The item listed below is on sale",
                      font = "ariel 12 underline"
                      ).grid(row = 0, column = 2, columnspan = 2,
                             padx = 5, pady = 5, sticky = "w")

    # create border frame
    black_border1 = tk.Frame(on_sale_win,background = "black")
    black_border2 = tk.Frame(on_sale_win,background = "black")
    black_border3 = tk.Frame(on_sale_win,background = "black")
    black_border4 = tk.Frame(on_sale_win,background = "black")
    black_border5 = tk.Frame(on_sale_win,background = "black")
    
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
    
    # set variables
    inventory = get_inventory()
    highest_stock_item = inventory.highest_stock_on_hand()
    
    # add entry widgets and display results
    for idx in inventory.inventory_list:
        if idx.code == highest_stock_item:
            # add entry widgets
            country_ent = tk.Entry(on_sale_win,highlightthickness = 2, width = 27)
            country_ent.config(background = "white", highlightcolor = "#6AD7DC")
            # add item info
            country_ent.insert(0,idx.country)
            country_ent.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
            
            code_ent = tk.Entry(on_sale_win,highlightthickness = 2, width = 27)
            code_ent.config(background = "white", highlightcolor = "#6AD7DC")
            # add item info
            code_ent.insert(0,idx.code)
            code_ent.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "w")
            
            product_ent = tk.Entry(on_sale_win,highlightthickness = 2, width = 27)
            product_ent.config(background = "white", highlightcolor = "#6AD7DC")
            # add item info
            product_ent.insert(0,idx.product)
            product_ent.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "w")
            
            cost_ent = tk.Entry(on_sale_win,highlightthickness = 2, width = 27)
            cost_ent.config(background = "white", highlightcolor = "#6AD7DC")
            # add item info
            item_cost = babel.numbers.format_currency(int(idx.cost), "ZAR", locale = "en_ZA")
            cost_ent.insert(0,item_cost)
            cost_ent.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "w")
            
            qty_ent = tk.Entry(on_sale_win,highlightthickness = 2, width = 27)
            qty_ent.config(background = "white", highlightcolor = "#6AD7DC")
            # add item info
            qty_ent.insert(0,idx.qty)
            qty_ent.grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "w")
    
    # add buttons
    back_but = tk.Button(on_sale_win,text = "Back",
                         font = "ariel 9", width = 15, height = 2,
                         command = on_sale_win.destroy
                         ).place(x = 660,y = 300)
    
    exit_but = tk.Button(on_sale_win,text = "Exit",
                         font = "ariel 9", width = 15, height = 2,
                         command = root.destroy
                         ).place(x = 780,y = 300)
    
