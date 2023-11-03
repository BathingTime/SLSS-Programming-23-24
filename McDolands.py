# McDoland's
# Sunny Lin
# Nov 3, 23

# CONSTS:
TAX=0.14
BURGER_COST=5
FRIES_COST=3

# Initialise a variable for the total cost.
total_cost=0

# Ask the user if they want a burger; if so, add $5.00 to their cost.
if input(f'Would you like a burger for ${BURGER_COST}? (Yes/No) ').lower().strip(' ,.!?')=='yes':
    total_cost+=BURGER_COST

# Ask the user if they want fries; if so, add $3.00 to their cost.
if input(f'Would you like fries for ${FRIES_COST}? (Yes/No) ').lower().strip(' ,.!?')=='yes':
    total_cost+=FRIES_COST

# Calculate and output the total cost with tax.
print(f'Your total is ${total_cost*(1+TAX):.2f}')