class DictionaryDemo:
    def __init__(self):
        self.data = {}

    def add_item(self, key, value):
        self.data[key] = value
        print(f"Added: {key} -> {value}")

    def remove_item(self, key):
        if key in self.data:
            del self.data[key]
            print(f"Removed: {key}")
        else:
            print(f"Key '{key}' not found.")

    def access_item(self, key):
        return self.data.get(key, "Key not found.")

    def display_items(self):
        if not self.data:
            print("Dictionary is empty.")
        else:
            for key, value in self.data.items():
                print(f"{key}: {value}")

    def clear_dictionary(self):
        self.data.clear()
        print("Dictionary cleared.")