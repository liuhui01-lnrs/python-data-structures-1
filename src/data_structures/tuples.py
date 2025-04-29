class TupleDemo:
    def __init__(self):
        self.tuple_data = (1, 2, 3, 4, 5)

    def access_elements(self):
        return self.tuple_data[0], self.tuple_data[1], self.tuple_data[-1]

    def tuple_length(self):
        return len(self.tuple_data)

    def iterate_tuple(self):
        return [element for element in self.tuple_data]

    def check_immutable(self):
        try:
            self.tuple_data[0] = 10
        except TypeError as e:
            return str(e)

def main():
    demo = TupleDemo()
    print("Accessing elements:", demo.access_elements())
    print("Length of tuple:", demo.tuple_length())
    print("Iterating over tuple:", demo.iterate_tuple())
    print("Checking immutability:", demo.check_immutable())

if __name__ == "__main__":
    main()