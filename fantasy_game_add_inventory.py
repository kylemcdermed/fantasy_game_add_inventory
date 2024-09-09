inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    #sort the inventory right here
    count = 0
    for k,v in inventory.items():
        count += v
        print(str(v) + ' ' + str(k))
    print(f'Total number of items {count}')

def addToInventory(inventory, addedItems):
    for i in dragonLoot:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory
        
updatedInventory = addToInventory(inventory, dragonLoot)

displayInventory(updatedInventory)
