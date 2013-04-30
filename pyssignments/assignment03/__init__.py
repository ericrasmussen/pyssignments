"""
A simple python implementation of a linked list, making heavy use of generators
and generator expressions.

For inspiration (if you have a little extra time), see David Beazley's excellent
talk on generators: http://www.slideshare.net/dabeaz/python-generator-hacking
"""

class Node(object):
    """
    Represents an individual node in a linked list, containing its own value
    along with a reference to the next node or None.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self) :
        self.head = None
        self.size = 0

    def __iter__(self):
        """
        This allows us to iterate over the nodes in a `LinkedList`. Note that
        there is a cleaner way to write it, but it was written this way to show
        how you can yield values in different sections of the function body
        but still produce a cohesive iterator (the consumer will never know!).
        """
        yield self.head

        if self.head and self.head.next:

            focus = self.head.next

            for i in xrange(self.size):
                if focus is not None:
                    yield focus
                    focus = focus.next

    def prepend(self, node):
        """
        Constant time implementation of a prepend (cons) function for
        `LinkedList`s.
        """
        node.next = self.head
        self.head = node
        self.size += 1

    def get_values(self):
        """
        Create a function to get all the values from `LinkedList` nodes.

        Additional requirements:
          1. this should return a generator expression that yields each value
        """
        pass

    def append(self, node):
        """
        Create an O(n) append function that will add the supplied `node` to
        the end of this `LinkedList`.
        """
        pass

    def reverse(self):
        """
        Create an O(n) reverse function.

        Additional requirements:
          1. return a new `LinkedList` (do not mutate `self`)
          2. make use of your `get_values` method
          3. make sure your implementation only traverses the list once
          4. warning: remember that nodes are mutable
        """
        pass

    def map(self, func):
        """
        Create a new `LinkedList` (with the same ordering as the original) by
        applying `func` to each node in `self`. Complexity should be O(2n).

        Additional requirements:
          1. return a new `LinkedList` (do not mutate `self`)
          2. make use of your `get_values` method
          3. create one generator expression to apply `func`
          4. create another expression that makes nodes from step 3's expression
        """
        pass

    def filter(self, pred):
        """
        Create a new `LinkedList` (with the same ordering as the original) but
        only including elements that satisify the predicate `pred`. Complexity
        should be O(2n).

        Additional requirements:
          1. return a new `LinkedList` (do not mutate `self`)
          2. make use of your `get_values` method
          3. create one generator expression to filter by `pred`
          4. create another expression that makes nodes from step 3's expression
        """
        pass

    def reduce(self, func):
        """
        Create an O(n) reduce function that takes an associative binary function
        (such as lambda x, y: x + y) and reduces the list to a single value
        by combining elements with the function.

        Additional requirements:
          1. make use of your `get_values` method
          2. make use of the `next()` method available on all generators
          3. make sure you handle all three cases in the test suite
              (empty list, singleton list, multiple item list)
        """
        pass
