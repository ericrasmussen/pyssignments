import unittest


class TestTransformalizer(unittest.TestCase):
    def _makeOne(self, transformer):
        from . import Transformalizer
        return Transformalizer(transformer)

    def test_transform(self):
        """ We create a ``Transformalizer`` with a function that will take a
        string representation of an int and return an int. """
        transform_function = int
        transformalizer = self._makeOne(transform_function)
        result = transformalizer.transform("42")
        self.assertEqual(result, 42)

    def test_bulk_transform(self):
        """ Create a function that adds 2 to a number and use it as our
        ``transformer``. """
        def add_two(x):
            return x + 2
        transformalizer = self._makeOne(add_two)
        test_container = [1, 3, 5]
        result = transformalizer.bulk_transform(test_container)
        self.assertEqual(result, [3, 5, 7])


