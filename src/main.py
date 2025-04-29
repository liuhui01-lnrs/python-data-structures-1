import sys
# Ensure ListDemo is correctly implemented in data_structures.lists module
from data_structures.lists import ListDemo
from data_structures.tuples import TupleDemo
from data_structures.dictionaries import DictionaryDemo
from data_structures.sets import SetOperations
from data_structures.linked_lists import LinkedList
from data_structures.stacks import Stack
from data_structures.queues import Queue


def display_menu():
    print("\n==== Python Data Structures Demo ====")
    print("1. Lists")
    print("2. Tuples")
    print("3. Dictionaries")
    print("4. Sets")
    print("5. Linked Lists")
    print("6. Stacks")
    print("7. Queues")
    print("8. Exit")
    return input("\nSelect a data structure to demonstrate (1-8): ")


def demonstrate_lists():
    demo = ListDemo()
    print("\n=== List Operations ===")
    demo.append_item(10)
    demo.append_item(20)
    demo.append_item(30)
    print("\nCurrent list:")
    demo.iterate_items()
    print(f"\nList length: {demo.get_length()}")

    demo.remove_item(20)
    print("\nList after removing 20:")
    demo.iterate_items()

    input("\nPress Enter to continue...")


def demonstrate_tuples():
    demo = TupleDemo()
    print("\n=== Tuple Operations ===")
    print("Accessing elements:", demo.access_elements())
    print("Length of tuple:", demo.tuple_length())
    print("Iterating over tuple:", demo.iterate_tuple())
    print("Checking immutability:", demo.check_immutable())

    input("\nPress Enter to continue...")


def demonstrate_dictionaries():
    demo = DictionaryDemo()
    print("\n=== Dictionary Operations ===")
    demo.add_item("name", "John")
    demo.add_item("age", 30)
    demo.add_item("city", "New York")

    print("\nCurrent dictionary:")
    demo.display_items()

    print(f"\nAccessing 'name': {demo.access_item('name')}")
    print(f"Accessing 'country': {demo.access_item('country')}")

    demo.remove_item("age")
    print("\nDictionary after removing 'age':")
    demo.display_items()

    input("\nPress Enter to continue...")


def demonstrate_sets():
    demo = SetOperations()
    print("\n=== Set Operations ===")
    demo.add_element(1)
    demo.add_element(2)
    demo.add_element(3)
    demo.add_element(2)  # Demonstrate that duplicates are ignored

    print(f"Current set: {demo.display()}")
    print(f"Is 2 in the set? {demo.check_membership(2)}")

    demo.remove_element(2)
    print(f"Set after removing 2: {demo.display()}")

    another_set = {3, 4, 5}
    print(f"Another set: {another_set}")
    print(f"Union: {demo.union(another_set)}")
    print(f"Intersection: {demo.intersection(another_set)}")
    print(f"Difference: {demo.difference(another_set)}")

    input("\nPress Enter to continue...")


def demonstrate_linked_list():
    linked_list = LinkedList()
    print("\n=== Linked List Operations ===")
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    print("Linked List after appending 10, 20, 30:")
    elements = linked_list.display()
    print(" -> ".join(map(str, elements)) + " -> None")

    print(f"\nIs 20 in the list? {linked_list.find(20)}")
    linked_list.remove(20)

    print("Linked List after removing 20:")
    elements = linked_list.display()
    print(" -> ".join(map(str, elements)) + " -> None")

    input("\nPress Enter to continue...")


def demonstrate_stack():
    stack = Stack()
    print("\n=== Stack Operations ===")
    print("Pushing elements 1, 2, 3 onto the stack...")
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(f"Current stack: {stack}")
    print(f"Top element: {stack.peek()}")
    print(f"Stack size: {stack.size()}")

    print("\nPopping elements:")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")

    print(f"Is stack empty? {stack.is_empty()}")

    input("\nPress Enter to continue...")


def demonstrate_queue():
    queue = Queue()
    print("\n=== Queue Operations ===")
    print("Enqueueing elements 1, 2, 3...")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(f"Current queue: {queue}")
    print(f"Front element: {queue.peek()}")
    print(f"Queue size: {queue.size()}")

    print("\nDequeueing elements:")
    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}")

    print(f"Is queue empty? {queue.is_empty()}")

    input("\nPress Enter to continue...")


def main():
    print("Welcome to Python Data Structures Demonstration!")

    while True:
        choice = display_menu()

        if choice == '1':
            demonstrate_lists()
        elif choice == '2':
            demonstrate_tuples()
        elif choice == '3':
            demonstrate_dictionaries()
        elif choice == '4':
            demonstrate_sets()
        elif choice == '5':
            demonstrate_linked_list()
        elif choice == '6':
            demonstrate_stack()
        elif choice == '7':
            demonstrate_queue()
        elif choice == '8':
            print("\nThank you for using Python Data Structures Demo. Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
