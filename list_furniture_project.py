inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

#how many items in the inventory?
invetory_len = len(inventory)
print(inventory)

# the 1st element
first = inventory[1]
print(first)

#the last element 
last = inventory[-1]
print(last)

#index from 2 to 6
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

#the 1st 3 items
first3 = inventory[:3]
print(first3)

#how many 'twin bed'
twin_beds = inventory.count('twin bed')
print(twin_beds)

#sort
inventory.sort()
print(inventory)
