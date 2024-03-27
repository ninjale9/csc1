def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = quantity
    return inventory
def add_to_fruit(inventory, add_more):
    for key,value in inventory.items():
        if len(inventory) == 1:
            inventory[key] += add_more
        return inventory
            
# make these tests work...
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
#  test that 'strawberries' in new_inventory
print('strawberries' in new_inventory)
#  test that new_inventory['strawberries'] is 10
print(new_inventory)
add_to_fruit(new_inventory, 25)
#  test that new_inventory['strawberries'] is now 35)
print(new_inventory)