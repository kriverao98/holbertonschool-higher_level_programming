#!/usr/bin/python3


class VerboseList(list):
    """
    A subclass of the built-in list class that provides additional
    verbosity when modifying the list.

    Methods:
    - append(item): Appends an item to the list and prints a message.
    - extend(items): Extends the list with multiple items and prints a message.
    - remove(item): Removes an item from the list and prints a message if it exists.
    - pop(index=None): Removes and returns an item from the list at the specified index,
      or the last item if no index is provided. Prints a message.
    """

    def append(self, item):
        """
        Appends an item to the list and prints a message.

        Args:
        - item: The item to be appended to the list.
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, items):
        """
        Extends the list with multiple items and prints a message.

        Args:
        - items: A list of items to be added to the list.
        """
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        """
        Removes an item from the list and prints a message if it exists.

        Args:
        - item: The item to be removed from the list.
        """
        if item in self:
            print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=None):
        """
        Removes and returns an item from the list at the specified index,
        or the last item if no index is provided. Prints a message.

        Args:
        - index (optional): The index of the item to be removed.
          If not provided, the last item will be removed.
        """
        if index is None:
            index = len(self) - 1
        item = self[index]
        print(f"Popped {item} from the list.")
        super().pop(index)

# Testing
my_list = VerboseList()
my_list.append(10)
my_list.extend([20, 30, 40])
my_list.remove(20)
my_list.pop()
