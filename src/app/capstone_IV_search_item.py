# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:47:01 2023

@author: Phillip van Staden

Task:

Description:
    
    contains functions and classes for Search

"""

# import modules
import tkinter as tk
import babel.numbers

# import capstone modules
from capstone_IV_general import *
from capstone_IV_add_item import *

def search_item(root):
    """
    Function creates new window for 'search item'
    Request user input either: Country / Code / Product
    
    Search for and display items in inventory that matches criteria

    Parameters
    ----------
    root : Tk()
        Root/main window.

    Returns
    -------
    None.

    """
    
    # create new window
    search_win = tk.Toplevel()
    search_win.title("Search Item")
    search_win.geometry("930x350")
    center(search_win)
    
    # add menubar
    m = Menubar(search_win, root)
    
    # create canvas
    global canvas
    canvas = tk.Canvas(search_win, height = 100)
    
    # create scrollbar
    global scroll_y
    scroll_y = tk.Scrollbar(search_win,orient = "vertical",command = canvas.yview)
    canvas.config(yscrollcommand = scroll_y.set)
    
    # add label
    label1 = tk.Label(search_win, text = "Enter item information",
                      font = "ariel 12 underline"
                      ).grid(row = 0, column = 2, columnspan = 2,
                             padx = 5, pady = 5, sticky = "w")
        
    # create border frame
    black_border1 = tk.Frame(search_win,background = "black")
    black_border2 = tk.Frame(search_win,background = "black")
    black_border3 = tk.Frame(search_win,background = "black")
    black_border4 = tk.Frame(search_win,background = "black")
    black_border5 = tk.Frame(search_win,background = "black")
    
    # add column labels to frame
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
    country_ent = tk.Entry(search_win,highlightthickness = 2, width = 27)
    country_ent.config(background = "white", highlightcolor = "#6AD7DC")
    country_ent.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
    
    code_ent = tk.Entry(search_win,highlightthickness = 2, width = 27)
    code_ent.config(background = "white", highlightcolor = "#6AD7DC")
    code_ent.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "w")
    
    product_ent = tk.Entry(search_win,highlightthickness = 2, width = 27)
    product_ent.config(background = "white", highlightcolor = "#6AD7DC")
    product_ent.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "w")
    
    cost_ent = tk.Entry(search_win,highlightthickness = 2, width = 27)
    cost_ent.config(background = "white", highlightcolor = "#6AD7DC",state = "disabled")
    cost_ent.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "w")
    
    qty_ent = tk.Entry(search_win,highlightthickness = 2, width = 27)
    qty_ent.config(background = "white", highlightcolor = "#6AD7DC",state = "disabled")
    qty_ent.grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "w")
    
    # add label
    result_lab = tk.Label(search_win, text = "SEARCH RESULTS",
                          font = "ariel 12 bold", height = 2 
                          ).grid(row = 4, column = 0, sticky = "w")
    
    # create frame for search results
    global feedback_frame
    feedback_frame = tk.Frame(canvas)

    # create labels for frame
    country_lab = tk.Label(feedback_frame,text = "Country",
                           font = "ariel 10 underline",
                            background = "#9E9EA0", bd = 0.5,
                            width = 15
                           ).grid(row = 0, column = 0, padx = 2, pady = 2)
    
    code_lab = tk.Label(feedback_frame,text = "Code",
                           font = "ariel 10 underline",
                            background = "#9E9EA0", bd = 0.5,
                            width = 15
                           ).grid(row = 0, column = 1, padx = 2, pady = 2)
    
    product_lab = tk.Label(feedback_frame,text = "Product",
                           font = "ariel 10 underline",
                            background = "#9E9EA0", bd = 0.5,
                            width = 15
                           ).grid(row = 0, column = 2, padx = 2, pady = 2)
    
    cost_lab = tk.Label(feedback_frame,text = "Cost",
                           font = "ariel 10 underline",
                            background = "#9E9EA0", bd = 0.5,
                            width = 15
                           ).grid(row = 0, column = 3, padx = 2, pady = 2)
    
    qty_lab = tk.Label(feedback_frame,text = "Quantity",
                           font = "ariel 10 underline",
                            background = "#9E9EA0", bd = 0.5,
                            width = 15
                           ).grid(row = 0, column = 4, padx = 2, pady = 2)
    
    # put feedback_frame in canvas
    canvas.create_window(0,0, anchor = "center", window = feedback_frame)
    canvas.update_idletasks()
    
    # config scroll area
    canvas.configure(scrollregion = canvas.bbox('all'), 
                  )
    # place widgets using grid method
    scroll_y.grid(row = 5, column = 3, sticky = tk.NS) 
    canvas.grid(row = 5, column = 0, columnspan = 5,
                sticky = ("ew","ns"))
    
    
    # add buttons
    clear_but = tk.Button(search_win,text = "Clear",
                         font = "ariel 9", width = 15, height = 1,
                          command = lambda : clear_fields(search_win)
                         ).place(x = 660,y = 110)
    
    search_but = tk.Button(search_win,text = "Search",
                         font = "ariel 9", width = 15, height = 1,
                           command = lambda : search(search_win,root)
                         ).place(x = 780,y = 110)
    
    back_but = tk.Button(search_win,text = "Back",
                         font = "ariel 9", width = 15, height = 2,
                         command = search_win.destroy
                         ).place(x = 660,y = 300)
    
    exit_but = tk.Button(search_win,text = "Exit",
                         font = "ariel 9", width = 15, height = 2,
                         command = root.destroy
                         ).place(x = 780,y = 300)
    
def search(win,root):
    """
    Function retrieves user input
    Use input to search for inventory items that matches input
    create and place widgets in frame/canvas

    Parameters
    ----------
    win : Toplevel()
        Search item window.
    root : Tk()
        Root/main window.

    Returns
    -------
    None.

    """
    
    # create list of widget
    widget_list = win.grid_slaves()
    
    #set variables
    item_cost = 0
    country = widget_list[-7].get()
    code = widget_list[-8].get()
    product = widget_list[-9].get()
    
    inventory = get_inventory()
   
    if country != "":
        index = inventory.search_country(country)
        
        
        for count,idx in enumerate(index):
            country = tk.Label(feedback_frame,text = inventory.inventory_list[idx].country,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 0, padx = 2, pady = 2)
            
            code = tk.Label(feedback_frame,text = inventory.inventory_list[idx].code,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 1, padx = 2, pady = 2)
            
            product = tk.Label(feedback_frame,text = inventory.inventory_list[idx].product,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 2, padx = 2, pady = 2)
            
            item_cost = babel.numbers.format_currency(int(inventory.inventory_list[idx].cost), "ZAR", locale = "en_ZA")
            cost = tk.Label(feedback_frame,text = item_cost,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 3, padx = 2, pady = 2)
            
            qty = tk.Label(feedback_frame,text = inventory.inventory_list[idx].qty,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 4, padx = 2, pady = 2)

    
    elif code != "":
        index = inventory.search_code(code)
        
        for count,idx in enumerate(index):
            country = tk.Label(feedback_frame,text = inventory.inventory_list[idx].country,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 0, padx = 2, pady = 2)
            
            code = tk.Label(feedback_frame,text = inventory.inventory_list[idx].code,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 1, padx = 2, pady = 2)
            
            product = tk.Label(feedback_frame,text = inventory.inventory_list[idx].product,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 2, padx = 2, pady = 2)
            
            item_cost = babel.numbers.format_currency(int(inventory.inventory_list[idx].cost), "ZAR", locale = "en_ZA")
            cost = tk.Label(feedback_frame,text = item_cost,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 3, padx = 2, pady = 2)
            
            qty = tk.Label(feedback_frame,text = inventory.inventory_list[idx].qty,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 4, padx = 2, pady = 2)
              
    elif product != "":
        index = inventory.search_product(product)
        
        for count,idx in enumerate(index):
            country = tk.Label(feedback_frame,text = inventory.inventory_list[idx].country,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 0, padx = 2, pady = 2)
            
            code = tk.Label(feedback_frame,text = inventory.inventory_list[idx].code,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 1, padx = 2, pady = 2)
            
            product = tk.Label(feedback_frame,text = inventory.inventory_list[idx].product,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 2, padx = 2, pady = 2)
            
            item_cost = babel.numbers.format_currency(int(inventory.inventory_list[idx].cost), "ZAR", locale = "en_ZA")
            cost = tk.Label(feedback_frame,text = item_cost,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 3, padx = 2, pady = 2)
            
            qty = tk.Label(feedback_frame,text = inventory.inventory_list[idx].qty,
                                   font = "ariel 10", width = 15
                                   ).grid(row = count+1, column = 4, padx = 2, pady = 2)
    
    # reset scroll region
    canvas.configure(scrollregion = canvas.bbox('all'))
            
def clear_fields(win):
    """
    Function clears all entry fields in window

    Parameters
    ----------
    win : Toplevel()
        Search Item Winsdow.

    Returns
    -------
    None.

    """
    
    # create list of widgets in window
    widget_list = win.grid_slaves()
    
    # clear entry fields
    widget_list[-7].delete(0,"end")
    widget_list[-8].delete(0,"end")
    widget_list[-9].delete(0,"end")
