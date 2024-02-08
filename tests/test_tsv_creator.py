# FILEPATH: /c:/Git/humble-books-bundle-extractor/tests/test_tsv_creator.py

import unittest
from extractor.book import Book
from extractor.tsv_creator import CsvCreator


class TestCsvCreator(unittest.TestCase):

    def setUp(self):
        self.creator = CsvCreator()
        self.books = [
            Book("Test Title 1", "Test Author 1", "Test Description 1"),
            Book("Test Title 2", "Test Author 2", "Test Description 2"),
            Book("Test Title 3", "Test Author 3", "Test Description 3 ")
        ]

    def test_create(self):
        result = self.creator.create(self.books)
        expected_output = (
            "Test Author 1\tTest Title 1\t\tTest Description 1\n"
            "Test Author 2\tTest Title 2\t\tTest Description 2\n"
            "Test Author 3\tTest Title 3\t\tTest Description 3 \n"
        )
        self.assertEqual(result, expected_output)

    def test_create_empty(self):
        result = self.creator.create([])
        expected_output = ""
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
