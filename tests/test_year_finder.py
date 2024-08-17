import unittest
from extractor.book import Book
from extractor.year_finder import YearFinder


class TestYearFinder(unittest.TestCase):

    def setUp(self):
        self.book = Book("Head First C", "David Griffiths, Dawn Griffiths", "Test Description")
        self.year_finder = YearFinder()

    @unittest.skip("Skip the test as it uses real APIs")
    def test_find_year_with_real_apis(self):
        from dotenv import load_dotenv
        load_dotenv()
        answer = self.year_finder.find_year(self.book)
    
        self.assertEqual(answer, "2012")
        
if __name__ == '__main__':
    unittest.main()
