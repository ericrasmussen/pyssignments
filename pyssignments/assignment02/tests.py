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

    def test_shared_words_in_string(self):
        """
        Get the words that are shared between two strings and check that they
        are the expected words.
        """

        base_string = """
            This is a string that has some words in it which will be shared
            with another string. Only time will tell which words these may be.
        """
        comparative_string = "This is just another string buying some time."
        expected_shared_words = ("this", "is", "another", "some", "string", "time")
        c = self._make_counter()
        c.read_text_string(base_string)
        shared_words = c.shared_words_in_string(comparative_string)
        self.assertItemsEqual(shared_words, expected_shared_words)

    def test_generate_word_count_strings(self):
        """
        Test that generate_word_count_strings generates the expected strings.
        """

        example_string = "Bob is bob and not dave. " \
            " Dave is a man and not a monkey." \
            " Oh Man! I wish I had a pet monkey."

        word_count_strings = ["The word 'bob' has been counted 2 times.",
            "The word 'is' has been counted 2 times.",
            "The word 'and' has been counted 2 times.",
            "The word 'not' has been counted 2 times.",
            "The word 'dave' has been counted 2 times.",
            "The word 'a' has been counted 3 times.",
            "The word 'man' has been counted 2 times.",
            "The word 'monkey' has been counted 2 times.",
            "The word 'oh' has been counted 1 time.",
            "The word 'i' has been counted 2 times.",
            "The word 'wish' has been counted 1 time.",
            "The word 'had' has been counted 1 time.",
            "The word 'pet' has been counted 1 time."
        ]

        c = self._make_counter()
        c.read_text_string(example_string)

        for word_count_string in c.generate_word_count_strings():
            word_count_strings.remove(word_count_string)

        self.assertSequenceEqual(word_count_strings, [])
