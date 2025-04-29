class ListDemo:
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