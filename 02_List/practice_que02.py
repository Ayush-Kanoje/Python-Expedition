# 2. Shopping Cart

# A customer's shopping cart contains:

# cart = ["Milk", "Bread", "Eggs"]

# Tasks:

# Add "Butter"
# Remove "Bread"
# Check if "Eggs" exists
# Print updated cart

# Real-world use:
# E-commerce websites.



cart = ["Milk", "Bread", "Eggs","Bread"]

cart.append("Butter")
cart.remove("Bread") #remove based on first occerance 
cart.pop(1) #based on index value 
print("Eggs" in cart)  # Return "true" is element exist in list
print(cart)