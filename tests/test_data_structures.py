import unittest
from src.data_structures.lists import ListDemo
from src.data_structures.tuples import TupleDemo
from src.data_structures.dictionaries import DictionaryDemo
from src.data_structures.sets import SetDemo
from src.data_structures.linked_lists import LinkedList
from src.data_structures.stacks import Stack
from src.data_structures.queues import Queue

class TestDataStructures(unittest.TestCase):

    def test_list_operations(self):
        demo = ListDemo()
        demo.append(1)
        demo.append(2)
        demo.append(3)
        self.assertEqual(demo.get_elements(), [1, 2, 3])
        demo.remove(2)
        self.assertEqual(demo.get_elements(), [1, 3])

    def test_tuple_operations(self):
        demo = TupleDemo()
        self.assertEqual(demo.get_element(1), 'b')
        self.assertEqual(demo.get_length(), 3)

    def test_dictionary_operations(self):
        demo = DictionaryDemo()
        demo.add('key1', 'value1')
        demo.add('key2', 'value2')
        self.assertEqual(demo.get('key1'), 'value1')
        demo.remove('key1')
        self.assertIsNone(demo.get('key1'))

    def test_set_operations(self):
        demo = SetDemo()
        demo.add(1)
        demo.add(2)
        demo.add(3)
        self.assertTrue(demo.contains(2))
        demo.remove(2)
        self.assertFalse(demo.contains(2))

    def test_linked_list_operations(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertTrue(linked_list.find(2))
        linked_list.remove(2)
        self.assertFalse(linked_list.find(2))

    def test_stack_operations(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertFalse(stack.is_empty())

    def test_queue_operations(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertFalse(queue.is_empty())

if __name__ == '__main__':
    unittest.main()