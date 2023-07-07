# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:06:06 2023

@author: Phillip van Staden

Task 

Description:
    
    Contains functions for 'Add Item window'
    
"""
# import modules
import tkinter as tk

#import capstone modules
from capstone_IV_general import *
from capstone_IV_view_all import *

def add_item(root):
    """
    Function creates new window that allows user to add item to inventory

    Parameters
    ----------
    root : Tk()
        Main window.

    Returns
    -------
    None.

    """
    
    # create new window
    add_item_win = tk.Toplevel()
    add_item_win.title("Add Item")
    add_item_win.geometry("900x350")
    
    # center window
    center(add_item_win)
    
    # add menubar
    m = Menubar(add_item_win, root)
    
    # add label
    label1 = tk.Label(add_item_win, text = "Enter item information",
                      font = "ariel 12 underline"
                      ).grid(row = 0, column = 2, columnspan = 2,
                             padx = 5, pady = 5, sticky = "w")

    # create border frame
    black_border1 = tk.Frame(add_item_win,background = "black")
    black_border2 = tk.Frame(add_item_win,background = "black")
    black_border3 = tk.Frame(add_item_win,background = "black")
    black_border4 = tk.Frame(add_item_win,background = "black")
    black_border5 = tk.Frame(add_item_win,background = "black")
    
    # add column labels to borders
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
    
    # add entry widgets
    country_ent = tk.Entry(add_item_win,highlightthickness = 2, width = 27)
    country_ent.config(background = "white", highlightcolor = "#6AD7DC")
    country_ent.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
    
    code_ent = tk.Entry(add_item_win,highlightthickness = 2, width = 27)
    code_ent.config(background = "white", highlightcolor = "#6AD7DC")
    code_ent.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "w")
    
    product_ent = tk.Entry(add_item_win,highlightthickness = 2, width = 27)
    product_ent.config(background = "white", highlightcolor = "#6AD7DC")
    product_ent.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "w")
    
    cost_ent = tk.Entry(add_item_win,highlightthickness = 2, width = 27)
    cost_ent.config(background = "white", highlightcolor = "#6AD7DC")
    cost_ent.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "w")
    
    qty_ent = tk.Entry(add_item_win,highlightthickness = 2, width = 27)
    qty_ent.config(background = "white", highlightcolor = "#6AD7DC")
    qty_ent.grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "w")
    
    # add buttons
    clear_but = tk.Button(add_item_win,text = "Clear",
                         font = "ariel 9", width = 15, height = 1,
                          command = lambda : clear_fields(add_item_win)
                         ).place(x = 660,y = 110)
    
    submit_but = tk.Button(add_item_win,text = "Submit",
                         font = "ariel 9", width = 15, height = 1,
                          command = lambda : new_item(add_item_win,root)
                         ).place(x = 780,y = 110)
    
    back_but = tk.Button(add_item_win,text = "Back",
                         font = "ariel 9", width = 15, height = 2,
                         command = add_item_win.destroy
                         ).place(x = 660,y = 300)
    
    exit_but = tk.Button(add_item_win,text = "Exit",
                         font = "ariel 9", width = 15, height = 2,
                         command = root.destroy
                         ).place(x = 780,y = 300)

def new_item(win,root):
    """
    Function retrieves user's input
    Creates new item and adds to inventory list
    Writes new inventory list to 'source'

    Parameters
    ----------
    win : Toplevel()
        Add-Item window.
    root : Tk()
        Root/ main window.

    Returns
    -------
    None.

    """
    
    # create list of widgets in window
    widget_list = win.grid_slaves()
    
    # retrieve inventroy list from source
    inventory = get_inventory()
    
    # check user input is numeric
    if widget_list[1].get().isnumeric() and widget_list[0].get().isnumeric():
      
        # add new item to inventory
        inventory.add_item(widget_list[4].get(), widget_list[3].get(), widget_list[2].get(),widget_list[1].get(), widget_list[0].get())
        
        # write new inventory to source
        with open(source.source,"w") as f:
            f.write("Country,Code,Product,Cost,Quantity")
        
        with open(source.source,"a") as f:
            for idx in inventory.inventory_list:
                f.write("\n"+idx.country+","+idx.code+","+idx.product+","+str(idx.cost)+","+str(idx.qty))
        
        # clear entry fields
        widget_list[4].delete(0,"end")
        widget_list[3].delete(0,"end")
        widget_list[2].delete(0,"end")
        widget_list[1].delete(0,"end")
        widget_list[0].delete(0,"end")
        
    else:
        e = Error_message("You've made an incorrect entry", root)
    
    

def clear_fields(win):
    """
    Function clears all fields in window

    Parameters
    ----------
    win : Toplevel()
        Add-item Window.

    Returns
    -------
    None.

    """
    
    # create list of widgets in window
    widget_list = win.grid_slaves()
    
    # clear entry fields
    widget_list[4].delete(0,"end")
    widget_list[3].delete(0,"end")
    widget_list[2].delete(0,"end")
    widget_list[1].delete(0,"end")
    widget_list[0].delete(0,"end")