import unittest
import os

class TestWordCounter(unittest.TestCase):
    TOP_TEN_WORDS = ('the', 'and', 'of', 'to', 'a',
        'he', 'in', 'that', 'i', 'his')
    FORTY_TWO_COUNT_WORDS = ('ever', 'fight', 'though', 'behind',
        'ground', 'don','end', 'make')

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
        filepath = os.path.abspath(os.path.join(basepath, "jungle_book.txt"))
        return filepath

    def _get_jungle_book_counter(self):
        c = self._make_counter()
        c.read_text_file(self._get_jungle_book_filepath())
        return c

    def test_get_most_frequent_words(self):
        c = self._get_jungle_book_counter()
        freq_words = c.get_most_frequent_words(10)
        self.assertSequenceEqual(freq_words, self.TOP_TEN_WORDS)

    def test_get_words_by_count(self):
        c = self._get_jungle_book_counter()
        fourtytwo_count_words = c.get_words_by_count(42)
        self.assertItemsEqual(fourtytwo_count_words,
                              self.FORTY_TWO_COUNT_WORDS)

    def test_get_unique_words(self):
        c = self._make_counter()
        c.read_text_string(self.TEST_TEXT)
        unique_words = c.get_unique_words()
        self.assertItemsEqual(unique_words, self.UNIQUE_WORDS)
