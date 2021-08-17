#  --------- Instructions  --------- 

# To run this project, execute the following steps

# create a new environment
python -m venv venv

# activate the new environment
venv\scripts\activate.bat

# upgrade pip to the latest version
python.exe -m pip install --upgrade pip

# install the requirements 
pip install -r requirements.txt 

# execute the run.py file

# ----- Build an empty database (This step isn't required if you use the database we included) -----  

# We've included a database called site.db.  However, you can build your own empty database from scratch 
# by typing "/build_database" in your browser.

#  ----- Using the site ----- 

# At a minimum, you will need one administrator account and one customer account.  To create each of 
# these accounts, go to the Sign Up page.  For simplicity, we allow the user to make himself/herself
# an administrator by checking the administrator checkbox at the end of the form.

# The Sign Up page includes extensive validations.  All fields are required.  The user name and email address
# must be unique.  The telephone number must be a valid US telephone number.

# When logging in as an administrator, the user can access the Add Inventory and View Inventory pages.  These
# pages allow the user to add, view, update and delete inventory items.

# The Add / Update Inventory page includes validations that require each field be filled out. 

# When logging in as a customer, the user can go to the Browse Products page and select items to buy.  Then,
# the user can go to the View Cart page and review thier items, delete items from the cart and enter thier credit card
# information.  After the user can click the Purchase button to finalize the transaction.




