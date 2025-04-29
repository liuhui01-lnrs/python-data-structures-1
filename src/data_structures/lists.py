class ListDemo:
    """
    A class to demonstrate basic list operations.

    Methods:
        __init__():
            Initializes an empty list.

        append_item(item):
            Appends an item to the list and prints a confirmation message.

        remove_item(item):
            Removes an item from the list if it exists, otherwise prints an error message.

        iterate_items():
            Iterates through the list and prints each item.

        get_length():
            Returns the number of items in the list.

        clear_items():
            Clears all items from the list and prints a confirmation message.
    """

    def __init__(self):
        self.items = []

    def append_item(self, item):
        self.items.append(item)
        print(f"Appended: {item}")

    def remove_item(self, item):
        try:
            self.items.remove(item)
            print(f"Removed: {item}")
        except ValueError:
            print(f"Item not found: {item}")

    def iterate_items(self):
        print("Items in the list:")
        for item in self.items:
            print(item)

    def get_length(self):
        return len(self.items)

    def clear_items(self):
        self.items.clear()
        print("Cleared all items from the list")
