# FILEPATH: /c:/Git/humble-books-bundle-extractor/tests/test_tsv_creator.py

import unittest
from extractor.book import Book
from extractor.tsv_creator import CsvCreator


class TestCsvCreator(unittest.TestCase):

    def setUp(self):
        self.creator = CsvCreator()
        self.books = [
            Book("Test Title 1", "Test Author 1", "Test Description 1", 2021, ["PDF", "EPUB"]),
            Book("Test Title 2", "Test Author 2", "Test Description 2", 2020, ["PDF"]),
            Book("Test Title 3", "Test Author 3", "Test Description 3 ", None, ["PDF", "EPUB", "MOBI"])
        ]

    def test_create(self):
        result = self.creator.create(self.books)
        expected_output = (
            "Test Author 1\tTest Title 1\t2021\tTest Description 1\tPDF, EPUB\n"
            "Test Author 2\tTest Title 2\t2020\tTest Description 2\tPDF\n"
            "Test Author 3\tTest Title 3\t\tTest Description 3 \tPDF, EPUB, MOBI\n"
        )
        self.assertEqual(result, expected_output)

    def test_create_empty(self):
        result = self.creator.create([])
        expected_output = ""
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
