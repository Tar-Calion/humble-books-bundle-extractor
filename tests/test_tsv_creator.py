# FILEPATH: /c:/Git/humble-books-bundle-extractor/tests/test_tsv_creator.py

import unittest
from extractor.book import Book
from extractor.tsv_creator import CsvCreator


class TestCsvCreator(unittest.TestCase):

    def setUp(self):
        self.creator = CsvCreator()
        self.books = [
            Book("Test Title 1", "Test Author 1", "Test Description 1", 2021, formats=["PDF", "EPUB"],
                 labels=["Test Label 1"], purchase_date="01.01.2021", source="Humble Bundle Book Bundle: Test Bundle"),
            Book("Test Title 2", "Test Author 2", "Test Description 2", 2020, formats=["PDF"],
                 labels=["Test Label 2", "Test Label 3"], purchase_date="01.01.2021", source="Humble Bundle Book Bundle: Test Bundle"),
            Book("Test Title 3", "Test Author 3", "Test Description 3", None, formats=["PDF", "EPUB", "MOBI"],
                 purchase_date="01.01.2021", source="Humble Bundle Book Bundle: Test Bundle"),
            Book("Test Title 4", "Test Author 4", "Test Description 4", "N/A", formats=["PDF", "EPUB", "MOBI"],
                 purchase_date="01.01.2021", source="Humble Bundle Book Bundle: Test Bundle")
        ]

    def test_create(self):
        result = self.creator.create(self.books)
        expected_output = (
            '"Test Title 1"\t"Test Author 1"\t"2021"\t"Test Description 1"\t"Test Label 1"\t"Humble Bundle"\t'
            '"PDF, EPUB"\t"01.01.2021"\t"Humble Bundle Book Bundle: Test Bundle"\n'
            '"Test Title 2"\t"Test Author 2"\t"2020"\t"Test Description 2"\t"Test Label 2, Test Label 3"\t"Humble Bundle"\t'
            '"PDF"\t"01.01.2021"\t"Humble Bundle Book Bundle: Test Bundle"\n'
            '"Test Title 3"\t"Test Author 3"\t""\t"Test Description 3"\t""\t"Humble Bundle"\t'
            '"PDF, EPUB, MOBI"\t"01.01.2021"\t"Humble Bundle Book Bundle: Test Bundle"\n'
            '"Test Title 4"\t"Test Author 4"\t""\t"Test Description 4"\t""\t"Humble Bundle"\t'
            '"PDF, EPUB, MOBI"\t"01.01.2021"\t"Humble Bundle Book Bundle: Test Bundle"\n'
        )
        self.assertEqual(result, expected_output)

    def test_create_empty(self):
        result = self.creator.create([])
        expected_output = ""
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
