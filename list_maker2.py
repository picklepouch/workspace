import os
groceries = []
print("Type help for assistance")
def clear_screen():
    os.system(cls if os.name == "nt" else clear)
def list_items():
    clear_screen()
    for items in groceries:
        print ("-", items)
def remove_item():
    list_items()
    what_remove = input("What would you like to remove?  ")
    try:
        groceries.remove(what_remove)
    except ValueError:
        pass
    clear_screen()
    list_items()
while True:
    new_item = input("Add item : ")
    if new_item.lower() == "help":
        print("""
            To add an item to your list, simply type it in. 
            Type 'done' when finished. 
            To view your list type 'list'.
            To remove an item typer 'delete'
            To clear the list type 'CLEAR LIST'.
        """)
        
    elif new_item.lower() == "list":
        print("Here is your list")
        list_items()
    elif new_item.lower() == "done":
        break
    elif new_item == "CLEAR LIST":
        list.clear(groceries)
    elif new_item.lower() == "delete":
        remove_item()
        new_item = input("Add item : ")
    else:
        groceries.append(new_item)
        print("There are currently {} items on your list.".format(len(groceries)))

list_items()