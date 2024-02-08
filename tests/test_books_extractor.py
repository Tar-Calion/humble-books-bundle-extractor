import unittest
from bs4 import BeautifulSoup
from extractor.book import Book
from extractor.books_extractor import BooksExtractor

class TestBooksExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = BooksExtractor()
        with open('tests/resources/bundle-info.html', 'r', encoding='utf-8') as html_file:
            self.html_content = html_file.read()


    def test_extract(self):
        
        expected_books = [
            Book("The Cloud Data Lake",
                 "Rukmani Gopalan",	
                 "More organizations than ever understand the importance of data lake  architectures for deriving value from their data. Building a robust,  scalable, and performant data lake remains a complex proposition,  however, with a buffet of tools and options that need to work together  to provide a seamless end-to-end pipeline from data to insights.This book provides a concise yet comprehensive overview on the setup,   management, and governance of a cloud data lake. Author Rukmani  Gopalan, a product management leader and data enthusiast, guides data  architects and engineers through the major aspects of working with a  cloud data lake, from design considerations and best practices to data  format optimizations, performance optimization, cost management, and  governance.Learn the benefits of a cloud-based big data strategy for your organizationGet guidance and best practices for designing performant and scalable data lakesExamine architecture and design choices, and data governance principles and strategiesBuild a data strategy that scales as your organizational and business needs increaseImplement a scalable data lake in the cloudUse cloud-based advanced analytics to gain more value from your data "),
            Book("Title 2", "Author 2", "Description 2 ")
        ]
        actual_books = self.extractor.extract(self.html_content)
        self.assertEqual(actual_books[0].title, expected_books[0].title)
        self.assertEqual(actual_books[0].author, expected_books[0].author)
        self.assertEqual(actual_books[0].description, expected_books[0].description)
        self.assertEqual(actual_books[0].year, expected_books[0].year)


if __name__ == '__main__':
    unittest.main()