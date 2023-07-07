# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:47:41 2023

@author: Phillip van Staden

Task Capstone IV

Description:
    This contains all general functions and classes
    
"""
# import modules
import os
import tkinter as tk


def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    code copied from stackoverflow https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def change_source_win(root):
    """
    Function creates new window with input field.

    Parameters
    ----------
    root : Window (Tk)
        Root window for program.

    Returns
    -------
    None.

    """
    
    # create new window
    inventory_win = tk.Toplevel()
    inventory_win.title("Change inventory source")
    inventory_win.geometry("400x200")
    center(inventory_win)
    
    # add menubar
    m = Menubar(inventory_win, root)
    
    # add label
    label1 = tk.Label(inventory_win,text = "Please enter name of inventory source:",
                      font = "ariel 11"
                      ).grid(row = 0, column = 0, padx = 5, pady = 5)
    
    # add entry widget
    entry1 = tk.Entry(inventory_win,width = 25)
    entry1.grid(row = 1, column = 0, padx = 5, pady = 5)
    
    # add buttons
    get_but = tk.Button(inventory_win,text = "Submit",
                        width = 15, height = 2,
                        command = lambda : change_source(inventory_win)
                        ).grid(row = 1, column = 1, padx = 5, pady = 5)
    
    back_but = tk.Button(inventory_win,text = "Back",
                         width = 15, height = 2,
                         command = inventory_win.destroy
                         ).grid(row = 2, column = 1, padx = 5, pady = 5)
    
    exit_but = tk.Button(inventory_win,text = "Exit",
                         width = 15, height = 2,
                         command = root.destroy
                         ).grid(row = 3, column = 1, padx = 5, pady = 5)
    
def change_source(win):
    """
    Function changes global variable: 'source'
    Captures new information from input field in window

    Parameters
    ----------
    win : Window (Toplevel)
        Window from which information must be captured.

    Returns
    -------
    None.

    """
    
    # create list of widgets in window
    widget_list = win.grid_slaves()
    
    # change global variable using method
    source.change_source(widget_list[-2].get())
    # close window
    win.destroy()


def get_inventory():
    """
    Function returns an inventory of items.
    Gathers information from source (txt file)
    If file cannot be found, return error message

    Parameters
    ----------
    root : Window (Tk)
        Root window for program.

    Returns
    -------
    inventory : LIST
        List of items (Shoe).

    """
    
    data_list = []
    country = ""
    code = ""
    product = ""
    cost = 0
    qty = 0
    
    try:
        with open(source.source,"r") as f:
            for line in f:
                data_list.append(line.split(","))
                
        data_list = data_list[1:]
        
    except FileNotFoundError:
        e = Error_message("The inventory could not be found.")
        

    inventory = Inventory()

    for idx in data_list:
        country = idx[0]
        code = idx[1]
        product = idx[2]
        cost = float(idx[3])
        qty = int(idx[4])
        inventory.add_item(country, code, product, cost, qty)
    
    return inventory

class Source:
    
    def __init__(self):
        self.source = os.path.abspath("src/textfiles/inventory.txt")
        
    #method to change source
    def change_source(self,source):
        self.source = source

class Shoe:
    
    def __init__(self,country,code,product,cost,qty):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.qty = qty
    
    # method to change country for item
    def change_country(self,country):
        self.country = country
        
    # method to change code for item    
    def change_code(self,code):
        self.code = code
    
    # method to change product description for item
    def change_product(self,product):
        self.product = product
    
    # method to change price for item
    def change_price(self,price):
        self.cost = price
    
    # method to change quantity of item
    def change_qty(self,qty):
        self.qty = qty

class Inventory:
    
    def __init__(self):
        self.inventory_list = []
        
    # method to add item to inventory list
    def add_item(self,country,code,product,cost,qty):
        self.inventory_list.append(Shoe(country, code, product, cost, qty))
        
    # method to search for given country and return a list of index numbers
    def search_country(self,country):
        
        search_index = []
        
        for idx in self.inventory_list:
            if idx.country == country:
                search_index.append(self.inventory_list.index(idx))
       
        return search_index
    
    # method to search for given code and return a list of index numbers
    def search_code(self,code):
        
        search_index = []
        
        for idx in self.inventory_list:
            if idx.code == code:
                search_index.append(self.inventory_list.index(idx))
       
        return search_index
    
    # method to search for given product and return a list of index numbers
    def search_product(self,product):
        
        search_index = []
        
        for idx in self.inventory_list:
            if idx.product == product:
                search_index.append(self.inventory_list.index(idx))
       
        return search_index
    
    # method to create dictionary of product_codes and product_names
    def product_discription_dict(self):
        
        #create list of all codes in inventory
        code_list = []
        for idx in self.inventory_list:
            code_list.append(idx.code)
                
        # create a list of discription of all products discriptions in inventory
        discript_list = []
        for idx in self.inventory_list:
            discript_list.append(idx.product)
        # create a dictionary from two lists
        prod_discript_dict = dict(zip(code_list,discript_list))
        
        return prod_discript_dict
    
    # method to create dictionary of product_codes and product_prices
    def product_price_dict(self):
            
        #create list of all codes in inventory
        code_list = []
        for idx in self.inventory_list:
            code_list.append(idx.code)
                
        # create a list of all product prices in inventory
        price_list = []
        for idx in self.inventory_list:
            price_list.append(idx.cost)
            
        # create dictionary from two lists
        prod_price_dict = dict(zip(code_list,price_list))
        
        return prod_price_dict
    
    #method to create dictionary of product_codes and product_qty
    def product_qty_dict(self):
        
        #create list of all codes in inventory
        code_list = []
        for idx in self.inventory_list:
            code_list.append(idx.code)
            
        # create dictionary from two lists
        prod_qty_dict = dict.fromkeys(code_list,0)
        
        # if multiple entries for specified item, add qty totals
        for idx in self.inventory_list:
            prod_qty_dict[idx.code] = prod_qty_dict[idx.code]+idx.qty
        
        return prod_qty_dict
    
    # method to determine product with the highest stock_qty
    def highest_stock_on_hand(self):
        
        item_code = ""
        stock_val = 0
        
        for idx in self.inventory_list:
            if stock_val < idx.qty:
                stock_val = idx.qty
                item_code = idx.code
        
        return item_code
    
    # method to determine product with the lowest stock_qty
    def lowest_stock_on_hand(self):
        
        item_code = ""
        stock_val = 100000000
        
        for idx in self.inventory_list:
            if stock_val > idx.qty:
                stock_val = idx.qty
                item_code = idx.code
        
        return item_code
        
# class creates new toplevel window with error_message provided
class Error_message(tk.Toplevel):
    
    def __init__(self, error_message,root):
        super().__init__()        
        self.title("Error Message")
        self.geometry("400x200")
        
        # center window
        center(self)
        
        # add label (with error_message provided)
        self.error_lab = tk.Label(self, text = error_message, font = "ariel 12").pack(side = "top", pady = 30)
        
        # add close button
        self.close_but = tk.Button(self, text = "Close", 
                              font = "ariel 12",
                              command = self.destroy,
                              height = 2, width = 15,
                              ).pack(side = "bottom", pady = 30)
        
# class creates standard menubar options
class Menubar(tk.Menu):
    
    def __init__(self,win,root):
        #create new menubar in window
        super().__init__()
        self.menubar = tk.Menu(win)
        win.config(menu = self.menubar)
        
        # create menu: file
        self.file_menu = tk.Menu(self.menubar)
        
        # create menu: options
        self.options_menu = tk.Menu(self.menubar)
        
        # add menu items to file_menu
        self.file_menu.add_command(label = "Back",command = win.destroy)
        self.file_menu.add_command(label = "Exit", command = root.destroy)
        
        # add menu items to options_menu
        self.options_menu.add_command(label = "View All")
        self.options_menu.add_command(label = "Stock Value")
        self.options_menu.add_command(label = "Search Item")
        self.options_menu.add_command(label = "Add Item")
        self.options_menu.add_command(label = "Restock Item")
        
        
        # add menu to menubar
        self.menubar.add_cascade(label = "File", menu = self.file_menu)
        self.menubar.add_cascade(label = "Options", menu = self.options_menu)
        
# set variables
global source
source = Source()
