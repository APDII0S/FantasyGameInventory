# inventory.py

# Displays the user's inventory in the format: "{count} {item}"
# followed by "Total Items: {itemCount}"

# `display_inventory` displays user's current inventory for viewing purposes
# `add_to_inventory` adds elements from a list, to the user's inventory



"""~ More concise message above. ~"""



"""# This program's first half will look at a user's current inventory, and display them with the following format:
# "{v} {k}", where `v` means count of an item in inventory, and `k`—the actual item
# f"Total Items: {itemCount}"

# But for the other half, it will look at things to add to a user's inventory"""





stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_count = 0

    for k, v in inventory.items():
        print(f"{v} {k}")
        item_count += v
    
    print(f"Total items: {item_count}")




dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def add_to_inventory(inventory, addedItems):

    """
    Add items to an inventory.
    
    Args: 
        inventory (dict): Dictionary with item names as keys, item quantities as values
        addedItems (list): List with duplicate item names inside
    """

    for i in addedItems:

        # updatedInventory.setdefault(i, 0)
        # 
        # for k, v in updatedInventory.items():
        #     if i == k:
        #         updatedInventory[k] += 1

        """~ More efficient code below. No need for `setdefault(i, 0), or the nested loop. ~"""

        inventory[i] = inventory.get(i, 0) + 1

    return inventory

print('INVENTORY with "stuff"')
display_inventory(stuff)

print('\n\nINVENTORY with "dragonLoot" added to "stuff"')
display_inventory(add_to_inventory(stuff, dragonLoot))

