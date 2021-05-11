"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """ Class to parse a word file and count number of words
    """

    def __init__(self, filepath):
        f = open(filepath)
        self.words = self.read_words(f)
        print(f"{len(self.words)} words read")

    def read_words(self, f):
        words = [line.strip() for line in f]
        return words

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """ Class to parse word files and exclude blank lines and comments
    >>> special = SpecialWordFinder("test.txt")
    4 words read

    >>> special.random() in ["word", "test", "apple", "orange"]
    True

    >>> "#" in special.words
    False

    """

    def read_words(self, f):
        words = [line.strip() for line in f if line.strip()
                 and not line.startswith("#")]
        return words
