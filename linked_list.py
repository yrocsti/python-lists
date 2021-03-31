"""
Create and operate on a singly linked list.

Will help you understand the underlying mechanism of a built-in list object. Best to read over syntax for a better understanding.
Break the code and fix it so that you can go on to create your own styled linked list.
Then create a doubly linked list and a circular singly linked list and circular doubly linked list.
"""


class Node:
    """Create an object node to go into linked list."""

    def __init__(self, value):
        """
        Create a node with a specified value and do not specifiy next.

        This class is not to be instantiated alone. An instance of Node is
        created in the init, append and insert methods of LinkedList.
        """
        self.value = value
        self.next = None


class LinkedList:
    """Create a linked list with helper functions to operate on linked list."""

    def __init__(self, data=None):
        """Create head of a linked list."""
        self.head = Node(data)

    def __iter__(self):
        """Iterate method."""
        return self

    def __next__(self):
        """Return next item for iter."""
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next
        else:
            raise StopIteration

    def append(self, data):
        """Add item to end of linked list."""
        cur = self.head
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            while cur.next is not None:
                cur = cur.next
            else:
                cur.next = new_node

    def get_indexes_value(self, position):
        """Return the value at the given index."""
        cur = self.head
        counter = 0
        if position <= (self.get_length() - 1):
            while counter <= position:
                if counter == position:
                    return cur.value
                cur = cur.next
                counter += 1
        else:
            return False
            # print(f"{position} is out of index.") # comment out return False for feedback and uncomment this line.
        return None

    def get_values_index(self, val):
        """Return the given value's index."""
        cur = self.head
        counter = 0
        while cur.value != val and cur.next:
            cur = cur.next
            counter += 1
        if cur.value == val:
            return counter
        else:
            return False
            # print(f"{val} is not in the Linked List.") # comment out return False for feedback and uncomment this line.

    def insert(self, data, position):
        """Insert a new Node at a given index."""
        cur = self.head
        new_node = Node(data)
        counter = 0
        if 1 < position < self.get_length():
            while counter < position:
                if counter == position - 1:
                    new_node.next = cur.next
                    cur.next = new_node
                cur = cur.next
                counter += 1
        elif position == 0:
            new_node.next = cur
            self.head = new_node
        else:
            return False
            # print(f"{position} is out of index.") # comment out return False for feedback and uncomment this line.

    def delete_value(self, val):
        """Delete specified value."""
        cur = self.head
        previous = None
        while cur.value != val:
            previous = cur
            cur = cur.next
        if cur.value == val:
            if previous:
                previous.next = cur.next
                return cur
            else:
                self.head = cur.next
                return cur
        else:
            return False
            # print(f"{val} not found in linked list.") # comment out return False for feedback and uncomment this line.

    def delete_index(self, position):
        """Delete value at specified index."""
        cur = self.head
        previous = ''
        counter = 0
        if position <= self.get_length():
            while counter < position:
                previous = cur
                cur = cur.next
                counter += 1
        else:
            return False
            # print(f"{position} is out of index.") # comment out return False for feedback and uncomment this line.
        previous.next = cur.next
        return cur

    def get_length(self):
        """Return the length of the linked list."""
        cur = self.head
        counter = 1
        while cur.next is not None:
            cur = cur.next
            counter += 1
        return counter

    def get_next(self, value):
        """Return next value after input value."""
        if type(self.get_values_index(value)) is int:
            cur = self.head
            while cur.value is not value:
                cur = cur.next
            if cur.next is not None:
                return cur.next
            return False

    def get_prev(self, value):
        """Return previous item if there is a previous item, otherwise returns False."""
        if isinstance(self.get_values_index(value), int):
            cur = self.head
            prev = ''
            while cur.value is not value:
                prev = cur
                cur = cur.next
            if cur is self.head:
                return False
            return prev  # If you want the value and not the node object return prev.value

    def is_empty(self):
        """Check if head is None. If head is None it will return True the list is empty."""
        if self.head.value is not None:
            return False
        return True

    def bubble_sort(self):  # Also called Naive Approach
        """Largest item bubbles to the top. time: O(n^2) space: O(1) * in place sort."""
        cur = self.head
        while cur.next:  # Big O(n)
            if cur.value > cur.next.value:
                removed_item = self.delete_value(
                    cur.value
                )  # O(1) in this case, because we are only changing a nodes next pointer.
                self.append(
                    removed_item.value
                )  # would be O(1), but here it is O(n) due to having to go through the entire list to add an node.
                cur = self.head
            else:
                cur = cur.next

    def display(self):
        """Display is a Helper Function to show if code is working."""
        my_list = []
        cur = self.head
        while cur:
            my_list.append(cur.value)
            cur = cur.next
        return my_list
