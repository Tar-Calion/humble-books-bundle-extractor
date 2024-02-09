# FILEPATH: /c:/Git/humble-books-bundle-extractor/tests/test_tsv_creator.py

import unittest
from extractor.book import Book
from extractor.tsv_creator import CsvCreator


class TestCsvCreator(unittest.TestCase):

    def setUp(self):
        self.creator = CsvCreator()
        self.books = [
            Book("Test Title 1", "Test Author 1", "Test Description 1", 2021, formats=["PDF", "EPUB"], labels=["Test Label 1"]),
            Book("Test Title 2", "Test Author 2", "Test Description 2", 2020, formats=["PDF"], labels=["Test Label 2", "Test Label 3"]),
            Book("Test Title 3", "Test Author 3", "Test Description 3 ", None, formats=["PDF", "EPUB", "MOBI"])
        ]

    def test_create(self):
        result = self.creator.create(self.books)
        expected_output = (
            '"Test Author 1"\t"Test Title 1"\t"2021"\t"Test Description 1"\t"Test Label 1"\t"Humble Bundle"\t"PDF, EPUB"\n'
            '"Test Author 2"\t"Test Title 2"\t"2020"\t"Test Description 2"\t"Test Label 2, Test Label 3"\t"Humble Bundle"\t"PDF"\n'
            '"Test Author 3"\t"Test Title 3"\t""\t"Test Description 3 "\t""\t"Humble Bundle"\t"PDF, EPUB, MOBI"\n'
        )
        self.assertEqual(result, expected_output)

    def test_create_empty(self):
        result = self.creator.create([])
        expected_output = ""
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
