# Hyperiondev SE L3T08 - Containers_ Dockers
Compulsory task as part of training
Purpose is to illustrate the students ability to dockerize python program and publish on Docker Hub

## Instructions
Containerise your Python app application from the last capstone of Level I. Do all of the following instructions:
* Create an appropriate Dockerfile for your code.
* Create an image from this Dockerfile.
* Upload your image to Docker Hub.
* Ensure that your image can run on a machine that isn't your computer by using Docker Playground.

Submit the following:
* The Dockerfile you created.
* A link to your Docker Hub repository in a text file called docker1.txt.

# Local use
## Installation
1. Clone repository
2. Create virtual environment (Command: python -m venv [virtual environment name])
3. Activate virtual environment (Command: [virtual environment name]\scripts\activate)
4. install requirements from requirements.txt (Command: python -m pip install -r requirements.txt)
5. cd into directory (/compulsory task/src/app)
6. To run program (command: python captsone_IV_main.py)

# Docker
KNOWN PROBLEM
Tkinter creates a graphical user interface and has built in functions that allow access to the user interface of your desktop. Since docker creates a virtual environment (image) that runs apart from your desktop, you need to map the bindings correctly.

I am currently unable to correctly bind the image to the desktop interface, i.e. the docker image is created succesfully, but will not run.

Error:   File "/usr/local/lib/python3.11/tkinter/__init__.py", line 2326, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_tkinter.TclError: no display name and no $DISPLAY environment variable

## User guide
User is able to make selection by clicking on the appropriate icon.
* View Inventory - Shows all items listed in the inventory
* Search Item - Allows user to search for an item using specified creteria
* Add item - Allows user to add item to inventory
* Stock Value - Shows the stock value for all the items in the inventory
* On Sale - Shows the item with the highest quantity
* Restock Item - Shows the item with the lowest quantity, allows user the increase the amount and refresh 

Exit button - will close/exit the program

###### View Inventory
This window display a list of all the items in the inventory.
The user is can make changes to the data base and use the "Update Inventory" button to capture any changes.

Buttons:
Refresh List: Allows user to refresh the list after making alterations.
Add Item: will open the Add Item window
Update Inventory: Will capture any changes that the user has made to the inventory document

Back: closes current window
Exit: will exit/close the program

###### Search Item
This window allows user to search for specific item in inventory.
User is not able to alter/change any data from this window.

User must enter search criteria into relevant field. (note - only enter data into one field at a time)
Once the user has enter the search criteria, click on "Search"; this will display list of items that matches the search criteria.

Buttons:
Clear: Will clear all fields (not search history)
Search: Will return items that matches the search criteria

Back: closes current window
Exit: will exit/close the program

###### Add Item
This window will allow the user to add an item to the inventory.

User must complete all fields. Click on submit to capture data. This will submit the data to the inventory list and clear all fields.

Buttons:
Clear: Will clear all fields
Submit: Will capture all data to the inventory list

Back: closes current window
Exit: will exit/close the program

###### Stock Value
This window displays the stock value for all the items in the inventory.
User is not able to alter/change any data from this window.

Buttons:
Back: closes current window
Exit: will exit/close the program

###### On Sale
This window displays the item with the highest stock quantity, recommended to be placed on sale.
User is not able to alter/change any data from this window.

Buttons:
Back: closes current window
Exit: will exit/close the program

###### Restock Item
This window displays the item with the lowest stock quantity and allows the user to change/ increase the qty number (only). 
User must change (increase) the number in the Qty-field; click "Restock"
This will update the item's quantity in the inventory list.
To display the next item (with the lowest stock count/qty); click "Refresh"

Buttons:
Restock: will update the current item's Qty-field in the inventory list.
Refresh: will return the item with the lowest stock/qty count.

Back: closes current window
Exit: will exit/close the program

