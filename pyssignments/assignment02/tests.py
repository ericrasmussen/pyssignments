import unittest
import os

class TestWordCounter(unittest.TestCase):
    # The following constants define input values and corresponding correct
    # output values for the tests below.
    INPUT_FILENAME = "jungle_book.txt"
    TOP_TEN_WORDS = ('the', 'and', 'of', 'to', 'a',
        'he', 'in', 'that', 'i', 'his')
    FORTY_TWO_COUNT_WORDS = ('ever', 'fight', 'though', 'behind',
        'ground', 'don', 'end', 'make')

    TEST_TEXT = """
    Now Rann the Kite brings home the night
        That Mang the Bat sets free--
     The herds are shut in byre and hut
        For loosed till dawn are we.
    """
    UNIQUE_WORDS = ('and', 'we', 'kite', 'that', 'loosed', 'brings',
        'rann', 'shut', 'free', 'hut', 'herds', 'are', 'in', 'home',
        'dawn', 'now', 'mang', 'bat', 'for', 'sets', 'byre', 'till',
        'night', 'the')

    def _make_counter(self):
        from . import WordCounter
        return WordCounter()

    def _get_jungle_book_filepath(self):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, self.INPUT_FILENAME))
        return filepath

    def _make_jungle_book_counter(self):
        c = self._make_counter()
        c.read_text_file(self._get_jungle_book_filepath())
        return c

    def test_get_most_frequent_words(self):
        """
        Get the top ten most frequent words in the jungle book text and check
        that they are the top 10 we expected.
        """
        c = self._make_jungle_book_counter()
        freq_words = c.get_most_frequent_words(10)
        self.assertSequenceEqual(freq_words, self.TOP_TEN_WORDS)

    def test_get_words_by_count(self):
        """
        Get all words that occur in the jungle book text 42 times and check
        that they are the words we expected.
        """
        c = self._make_jungle_book_counter()
        fortytwo_count_words = c.get_words_by_count(42)
        self.assertItemsEqual(fortytwo_count_words,
                              self.FORTY_TWO_COUNT_WORDS)

    def test_get_unique_words(self):
        """
        Get all of the unique words in our test string and check that they are
        the words we expected.
        """
        c = self._make_counter()
        c.read_text_string(self.TEST_TEXT)
        unique_words = c.get_unique_words()
        self.assertItemsEqual(unique_words, self.UNIQUE_WORDS)
