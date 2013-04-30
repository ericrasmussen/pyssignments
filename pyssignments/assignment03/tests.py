import unittest
from . import Node


class TestLinkedList(unittest.TestCase):
    def _makeOne(self, head=None):
        from . import LinkedList
        return LinkedList()

    def test_prepend(self):
        ll = self._makeOne()
        ll.prepend(Node('spam'))
        ll.prepend(Node('eggs'))
        self.assertEqual(ll.head.value, 'eggs')
        self.assertEqual(ll.head.next.value, 'spam')
        self.assertEqual(ll.size, 2)

    def test_get_values(self):
        ll = self._makeOne()
        ll.prepend(Node('spam'))
        ll.prepend(Node('eggs'))
        expected = ['eggs', 'spam']
        actual = list(ll.get_values())
        self.assertSequenceEqual(expected, actual)

    def test_append(self):
        ll = self._makeOne()
        ll.append(Node('spam'))
        ll.append(Node('eggs'))
        self.assertEqual(ll.head.value, 'spam')
        self.assertEqual(ll.head.next.value, 'eggs')
        self.assertEqual(ll.size, 2)

    def test_size(self):
        ll = self._makeOne()
        ll.prepend(Node('spam'))
        ll.append(Node('eggs'))
        self.assertEqual(ll.size, 2)

    def test_map(self):
        ll = self._makeOne()
        ll.prepend(Node('spam'))
        ll.prepend(Node('eggs'))
        new_ll = ll.map(lambda s: s.upper())
        self.assertEqual(new_ll.head.value, 'EGGS')
        self.assertEqual(new_ll.head.next.value, 'SPAM')

    def test_reverse(self):
        ll = self._makeOne()
        ll.prepend(Node('spam'))
        ll.prepend(Node('eggs'))
        new_ll = ll.reverse()
        self.assertEqual(new_ll.head.value, 'spam')
        self.assertEqual(new_ll.head.next.value, 'eggs')

    def test_reduce_empty_list(self):
        ll = self._makeOne()
        func = lambda x, y: x * y
        self.assertRaises(TypeError, ll.reduce, func)

    def test_reduce_singleton(self):
        ll = self._makeOne()
        ll.prepend(Node(1))
        result = ll.reduce(lambda x, y: x + y)
        self.assertEqual(result, 1)

    def test_reduce_multiple_items(self):
        ll = self._makeOne()
        ll.prepend(Node(6))
        ll.prepend(Node(7))
        result = ll.reduce(lambda x, y: x * y)
        self.assertEqual(result, 42)

    def test_filter(self):
        ll = self._makeOne()
        ll.prepend(Node(1))
        ll.prepend(Node(2))
        ll.prepend(Node(3))
        ll.prepend(Node(4))
        result = ll.filter(lambda x: x % 2 == 0)
        self.assertEqual(result.head.value, 4)
        self.assertEqual(result.head.next.value, 2)
