'''
    Test Program for Read.py
    Devin Quinn
'''

import unittest
from datetime import date

from read import get_start, is_pages
from book import Book

book = Book("On Truth", "Mad Max", 367, 12)


class TestGetPages(unittest.TestCase):

    def test_start(self):
        """
        Test the input of start returns a date object
        """
        start = get_start()
        day = date.fromisoformat('2024-10-31')
        self.assertEqual(start, day)

    def test_is_true(self):
        """
        Test the that is_pages returns true when input is pages
        """
        result = is_pages()
        self.assertTrue(result)

    def test_is_false(self):
        """
        Test the that is_pages returns false when input is chapters
        """
        result = is_pages()
        self.assertFalse(result)

    def test_book(self):
        """
        Test the input of book returns a string
        """
        self.assertEqual("On Truth", book.title)
        self.assertEqual("Mad Max", book.author)
        self.assertEqual(367, book.length)
        self.assertEqual(12, book.chapters)


if __name__ == "__main__":
    unittest.main()
