# Python Data Structures Console Application

This project is a console application that demonstrates the use of various Python data structures, including lists, tuples, dictionaries, sets, linked lists, stacks, and queues. Each data structure is implemented in its own module, showcasing common operations and functionalities.

## Project Structure

```
python-data-structures
├── src
│   ├── main.py                  # Entry point of the application
│   ├── data_structures          # Package containing data structure modules
│   │   ├── __init__.py          # Initializes the data_structures package
│   │   ├── lists.py              # Demonstrates Python lists
│   │   ├── tuples.py             # Demonstrates Python tuples
│   │   ├── dictionaries.py        # Demonstrates Python dictionaries
│   │   ├── sets.py               # Demonstrates Python sets
│   │   ├── linked_lists.py       # Implements a linked list data structure
│   │   ├── stacks.py             # Implements a stack data structure
│   │   └── queues.py             # Implements a queue data structure
├── tests                         # Package containing unit tests
│   ├── __init__.py              # Initializes the tests package
│   └── test_data_structures.py   # Unit tests for data structure modules
├── requirements.txt              # Lists project dependencies
└── README.md                     # Project documentation
```

## Getting Started

To run the application, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-data-structures
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage Examples

- **Lists**: Demonstrates appending, removing, and iterating over elements.
- **Tuples**: Showcases the immutability of tuples and how to access their elements.
- **Dictionaries**: Illustrates adding, removing, and accessing key-value pairs.
- **Sets**: Demonstrates set operations like union, intersection, and membership checking.
- **Linked Lists**: Implements a linked list with methods for appending, removing, and finding elements.
- **Stacks**: Implements a stack with push, pop, and empty checks.
- **Queues**: Implements a queue with enqueue, dequeue, and empty checks.

## Running Tests

To run the unit tests, use the following command:

```
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.