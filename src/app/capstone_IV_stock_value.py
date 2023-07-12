# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:24:28 2023

@author: Phillip van Staden

Task 

Description:
    
    Contains functions and classes for 'stock value'
    
"""

# import modules
import tkinter as tk
import babel.numbers

# import capstone modules
from capstone_IV_general import *
from capstone_IV_add_item import *


def stock_value(root):
    """
    Function creates new window for 'stock value'
    Display list of all items according to code
    Display total value for stock on hand

    Parameters
    ----------
    root : Tk()
        Root/main window.

    Returns
    -------
    None.

    """
    

    # set variables
    inventory = get_inventory()
    product_list = inventory.product_discription_dict()
    price_list = inventory.product_price_dict()
    qty_list = inventory.product_qty_dict()
    item_price = 0
    total_val = 0

    # create new window
    stock_value_win = tk.Toplevel()
    stock_value_win.geometry("930x600")
    stock_value_win.title("Stock Values")

    # add menubar
    m = Menubar(stock_value_win, root)
    
    # center window in screen
    center(stock_value_win)

    # create canvas
    canvas = tk.Canvas(stock_value_win)
    # create scrollbar
    scroll_y = tk.Scrollbar(
        stock_value_win, orient="vertical", command=canvas.yview)

    # create frame
    global inventory_frame
    inventory_frame = tk.Frame(canvas)

    # create border frame
    black_border1 = tk.Frame(stock_value_win, background="black")
    black_border2 = tk.Frame(stock_value_win, background="black")
    black_border3 = tk.Frame(stock_value_win, background="black")
    black_border4 = tk.Frame(stock_value_win, background="black")
    black_border5 = tk.Frame(stock_value_win, background="black")

    # add column labels to frames
    code_lab = tk.Label(black_border2, text="Item Code",
                        font="ariel 12 underline",
                        background="#9E9EA0", bd=0.5,
                        width=18
                        ).grid(row=0, column=1, padx=2, pady=2)
    black_border2.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    product_lab = tk.Label(black_border3, text="Product Description",
                           font="ariel 12 underline",
                           background="#9E9EA0", bd=0.5,
                           width=18
                           ).grid(row=0, column=2, padx=2, pady=2)
    black_border3.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    cost_lab = tk.Label(black_border4, text="Cost per Item",
                        font="ariel 12 underline",
                        background="#9E9EA0", bd=0.5,
                        width=18
                        ).grid(row=0, column=3, padx=2, pady=2)
    black_border4.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    qty_lab = tk.Label(black_border5, text="Quantity",
                       font="ariel 12 underline",
                       background="#9E9EA0", bd=0.5,
                       width=18
                       ).grid(row=0, column=4, padx=2, pady=2)
    black_border5.grid(row=0, column=3, padx=5, pady=5, sticky="w")

    total_lab = tk.Label(black_border1, text="Total",
                         font="ariel 12 underline",
                         background="#9E9EA0", bd=0.5,
                         width=18
                         ).grid(row=0, column=0, padx=2, pady=2)
    black_border1.grid(row=0, column=4, padx=5, pady=5, sticky="w")

    # add entry widgets to frame

    for count, idx in enumerate(product_list):
        code_ent = tk.Entry(inventory_frame, highlightthickness=2, width=27)
        code_ent.config(background="white", highlightcolor="#6AD7DC")
        # add item info to entry widget
        code_ent.insert(0, idx)
        code_ent.grid(row=count, column=0, padx=5, pady=5, sticky="w")

        product_ent = tk.Entry(inventory_frame, highlightthickness=2, width=27)
        product_ent.config(background="white", highlightcolor="#6AD7DC")
        # add item info to entry widget
        product_ent.insert(0, product_list[idx])
        product_ent.grid(row=count, column=1, padx=5, pady=5, sticky="w")

        cost_ent = tk.Entry(inventory_frame, highlightthickness=2, width=27)
        cost_ent.config(background="white", highlightcolor="#6AD7DC")
        # add item info to entry widget
        item_price = babel.numbers.format_currency(
            price_list[idx], "ZAR", locale="en_ZA")
        cost_ent.insert(0, item_price)
        cost_ent.grid(row=count, column=2, padx=5, pady=5, sticky="w")

        qty_ent = tk.Entry(inventory_frame, highlightthickness=2, width=27)
        qty_ent.config(background="white", highlightcolor="#6AD7DC")
        # add item info to entry widget

        qty_ent.insert(0, qty_list[idx])
        qty_ent.grid(row=count, column=3, padx=5, pady=5, sticky="w")

        total_ent = tk.Entry(inventory_frame, highlightthickness=2, width=27)
        total_ent.config(background="white", highlightcolor="#6AD7DC")
        # add item info to entry widget
        total_val = babel.numbers.format_currency(
            int(price_list[idx])*int(qty_list[idx]), "ZAR", locale="en_ZA")
        total_ent.insert(0, total_val)
        total_ent.grid(row=count, column=4, padx=5, pady=5, sticky="w")

    # put inventory_frame in canvas
    canvas.create_window(0, 600, anchor="center", window=inventory_frame)
    canvas.update_idletasks()
    # config scroll area
    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)
    # place widgets using grid method
    canvas.grid(row=1, column=0, columnspan=5,
                sticky=("ew", "ns"))
    scroll_y.grid(row=1, column=5, sticky=tk.NS)

    back_but = tk.Button(stock_value_win, text="Back",
                         font="ariel 9", width=15, height=2,
                         command=stock_value_win.destroy
                         ).place(x=630, y=550)

    exit_but = tk.Button(stock_value_win, text="Exit",
                         font="ariel 9", width=15, height=2,
                         command=root.destroy
                         ).place(x=750, y=550)
