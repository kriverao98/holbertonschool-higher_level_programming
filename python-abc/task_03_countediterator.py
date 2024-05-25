#!/usr/bin/python3


class CountedIterator:
    """
    Represents an iterator that counts the number of items fetched.

    Attributes:
        iterator (iterable): The iterable object to iterate over.
        counter (int): The count of items fetched.

    Methods:
        get_count(): Returns the count of items fetched.
        __next__(): Retrieves the next item from the iterator.

    """

    def __init__(self, iterable):
        """
        Initializes a CountedIterator object.

        Args:
            iterable (iterable): The iterable object to iterate over.

        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Returns the count of items fetched.

        Returns:
            int: The count of items fetched.

        """
        return self.counter

    def __next__(self):
        """
        Retrieves the next item from the iterator.

        Returns:
            Any: The next item from the iterator.

        Raises:
            StopIteration: If there are no more items to iterate.

        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")

# Testing
my_list = [1, 2, 3, 4, 5]
my_iterator = CountedIterator(my_list)

for item in my_iterator:
    print(item)

print("Total items fetched:", my_iterator.get_count())