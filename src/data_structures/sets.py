class SetOperations:
    def __init__(self):
        self.data_set = set()

    def add_element(self, element):
        self.data_set.add(element)

    def remove_element(self, element):
        self.data_set.discard(element)

    def check_membership(self, element):
        return element in self.data_set

    def union(self, other_set):
        return self.data_set.union(other_set)

    def intersection(self, other_set):
        return self.data_set.intersection(other_set)

    def difference(self, other_set):
        return self.data_set.difference(other_set)

    def display(self):
        return self.data_set

def main():
    set_ops = SetOperations()
    set_ops.add_element(1)
    set_ops.add_element(2)
    set_ops.add_element(3)
    print("Current Set:", set_ops.display())
    
    set_ops.remove_element(2)
    print("After removing 2:", set_ops.display())
    
    print("Is 1 in the set?", set_ops.check_membership(1))
    
    another_set = {3, 4, 5}
    print("Union with {3, 4, 5}:", set_ops.union(another_set))
    print("Intersection with {3, 4, 5}:", set_ops.intersection(another_set))
    print("Difference with {3, 4, 5}:", set_ops.difference(another_set))

if __name__ == "__main__":
    main()