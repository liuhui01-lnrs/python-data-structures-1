# Python Data Structures

An interactive console application that demonstrates core Python data structures with hands-on examples.

## Description

This educational project provides a practical exploration of fundamental Python data structures, both built-in and custom implementations. The application features a user-friendly console interface that lets you interact with each data structure and observe its behavior in real-time.

The project covers:

- **Built-in Data Structures**: Lists, Tuples, Dictionaries, Sets
- **Custom Implementations**: Linked Lists, Stacks, Queues

Each data structure is implemented in its own dedicated module with clear, well-documented code that showcases common operations and use cases.

## Project Structure

```
python-data-structures
├── src/
│   ├── main.py                   # Application entry point with interactive menu
│   └── data_structures/          # Data structure implementations
│       ├── lists.py              # Python lists with common operations
│       ├── tuples.py             # Tuple operations and immutability demonstration
│       ├── dictionaries.py       # Key-value operations in dictionaries
│       ├── sets.py               # Set operations (union, intersection, etc.)
│       ├── linked_lists.py       # Custom linked list implementation
│       ├── stacks.py             # LIFO stack implementation
│       └── queues.py             # FIFO queue implementation
├── tests/                        # Unit tests
│   └── test_data_structures.py   # Tests for all data structure modules
├── requirements.txt              # Project dependencies (pytest)
└── README.md                     # Project documentation
```

## Key Files

- **[src/main.py](/src/main.py)**: The application's entry point with an interactive menu system to select and explore different data structures.
- **[src/data_structures/lists.py](/src/data_structures/lists.py)**: Demonstrates Python's dynamic arrays with methods for appending, removing, and iterating over elements.
- **[src/data_structures/dictionaries.py](/src/data_structures/dictionaries.py)**: Shows how to work with key-value pairs, including adding, removing, and accessing operations.
- **[src/data_structures/linked_lists.py](/src/data_structures/linked_lists.py)**: Custom implementation of a singly linked list with node traversal functionality.
- **[src/data_structures/stacks.py](/src/data_structures/stacks.py)**: LIFO (Last-In-First-Out) implementation with push, pop, and peek operations.

- **[src/data_structures/queues.py](/src/data_structures/queues.py)**: FIFO (First-In-First-Out) implementation with enqueue, dequeue, and peek operations.

## Usage

### Running the Application

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd python-data-structures
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python src/main.py
   ```

### Interactive Menu

The application provides an interactive console menu:

```
==== Python Data Structures Demo ====
1. Lists
2. Tuples
3. Dictionaries
4. Sets
5. Linked Lists
6. Stacks
7. Queues
8. Exit

Select a data structure to demonstrate (1-8):
```

Select any option to see a practical demonstration of that data structure with step-by-step operations and results.

### Running Tests

Execute the test suite with:

```bash
python -m unittest discover -s tests
```

or:

```bash
pytest
```

## License

This project is available under the MIT License. Feel free to use, modify, and distribute this code for educational and non-commercial purposes.

Copyright © 2023
