def find_item(item):

    return item in inventory

inventory = ["Nycklar", "Smörkniv", "Ved"]

index = find_item("Nycklar")

item = inventory.pop(index)
print(item)

trade = "lite ved"
print(f"Du byter {item} med en {trade}.")

inventory.append(trade)

def get_item(item_to_find):
    item_index = find_item(item_to_find)
    
    if item_index > 0:
        return inventory.pop(item_index)
    
    else:
        print(F"{item_to_find} finns inte i inventory")
        return None



