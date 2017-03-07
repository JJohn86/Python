#Simple shopping list exercise from Treehouse Python class


shopping_list = []

def show_help():
    print("""
What should we pick up at the store?
    Enter 'HELP' for list of commands
    Enter 'SHOW' to see current list
    Enter 'DONE' to stop adding items."""
    )

def show_list():
    print("""
    List contains {} items. Here's your list:
    """.format(len(shopping_list)))
    for item in shopping_list:
        print(item)
    print(""" """)

def add_to_list(new_item):
        shopping_list.append(new_item)
        print("""
        {} added to list.  List contains {} items.
        """.format(new_item, len(shopping_list)))

show_help()

while True:
    new_item = input("> ")
    new_item = new_item.lower()
    if new_item == 'help':
        show_help()
    elif new_item == 'show':
        show_list()
    elif new_item == 'done':
        break
    else:
        add_to_list(new_item)

show_list()

print("""
END
""")
