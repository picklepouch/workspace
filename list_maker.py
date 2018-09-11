groceries = []
print("Type help for assistance")
def list_items():
    for items in groceries:
        print ("-", items)
while True:
    new_item = input("Add item : ")
    if new_item.lower() == "help":
        print("""
            To add an item to your list, simply type it in. 
            Type 'done' when finished. 
            To view your list type 'list'.
            To clear the list type 'CLEAR LIST'.
        """)
    elif new_item.lower() == "list":
        print("Here is your list")
        list_items()
    elif new_item.lower() == "done":
        break
    elif new_item == "CLEAR LIST":
        list.clear(groceries)
    else:
        groceries.append(new_item)
        print("There are currently {} items on your list.".format(len(groceries)))

list_items()