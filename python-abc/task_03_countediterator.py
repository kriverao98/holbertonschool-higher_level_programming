#!/usr/bin/python3
"""Program that counts the num of items"""


class CountedIterator:
    """
    A class that represents a counted iterator.

    Attributes:
        iterator (iterable): The iterable object to iterate over.
        counter (int): The count of items iterated over.

    Methods:
        __next__(): Returns the next item in the iterator.
        get_count(): Returns the count of items iterated over.
        __iter__(): Returns the iterator object itself.
    """

    def __init__(self, iterable):
        """
        Initializes a CountedIterator object.

        Args:
            iterable (iterable): The iterable object to iterate over.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        Returns the next item in the iterator.

        Returns:
            The next item in the iterator.

        Raises:
            StopIteration: If there are no more items in the iterator.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Returns the count of items iterated over.

        Returns:
            The count of items iterated over.
        """
        return self.counter

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            The iterator object itself.
        """
        return self

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    counted_iter = CountedIterator(sample_list)

    for item in counted_iter:
        print(item)

    print("Total items iterated over:", counted_iter.get_count())
