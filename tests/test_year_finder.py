import unittest
from unittest.mock import patch
from extractor.book import Book
from extractor.year_finder import YearFinder


class TestYearFinder(unittest.TestCase):

    def setUp(self):
        self.book = Book("Test Title", "Test Author", "Test Description")
        self.year_finder = YearFinder()

    @patch('requests.get')
    @patch('googlesearch.search')
    def test_find_year_oreilly(self, mock_search, mock_get):
        # Mock the search function to return a list of links
        mock_search.return_value = iter([
            "https://books.google.com/books?id=1234567890",
            "https://www.oreilly.com/library/view/scala-cookbook-2nd/9781492051534/ch16.html",
            "https://www.amazon.com/Test-Title/dp/1234567890/",
            "https://www.ebay.com/p/1234567890"
        ])

        # Mock the get function to return a response with a specific HTML content
        mock_get.return_value.content = b'<html><div class="t-release-date">Released December 2022</div></html>'

        # Call the find_year method and assert the returned year
        year = self.year_finder.find_year(self.book)
        self.assertEqual(year, "2022")

        # Assert that the search function was called with the correct search term
        mock_search.assert_called_once_with(
            f"Test Title Test Author o'reilly", num_results=10)

        # Assert that the get function was called with the correct URL
        mock_get.assert_called_once_with(
            "https://www.oreilly.com/library/view/scala-cookbook-2nd/9781492051534/")

    # link with "xhtml": https://www.oreilly.com/library/view/autotools-2nd-edition/9781098122577/xhtml/toc.xhtml
    @patch('requests.get')
    @patch('googlesearch.search')
    def test_find_year_oreilly_xhtml(self, mock_search, mock_get):
        # Mock the search function to return a list of links
        mock_search.return_value = iter([
            "https://books.google.com/books?id=1234567890",
            "https://www.oreilly.com/library/view/autotools-2nd-edition/9781098122577/xhtml/toc.xhtml",
            "https://www.amazon.com/Test-Title/dp/1234567890/",
            "https://www.ebay.com/p/1234567890"
        ])

        # Mock the get function to return a response with a specific HTML content
        mock_get.return_value.content = b'<html><div class="t-release-date">Released December 2022</div></html>'

        # Call the find_year method and assert the returned year
        year = self.year_finder.find_year(self.book)
        self.assertEqual(year, "2022")

        # Assert that the search function was called with the correct search term
        mock_search.assert_called_once_with(
            f"Test Title Test Author o'reilly", num_results=10)

        # Assert that the get function was called with the correct URL
        mock_get.assert_called_once_with(
            "https://www.oreilly.com/library/view/autotools-2nd-edition/9781098122577/")

    @patch('requests.get')
    @patch('googlesearch.search')
    def test_find_year_no_oreilly(self, mock_search, mock_get):
        # Mock the search function to return a list of links
        mock_search.return_value = iter([
            "https://books.google.com/books?id=1234567890",
            "https://www.amazon.com/Test-Title/dp/1234567890/",
            "https://www.ebay.com/p/1234567890",
            "https://www.oreilly.com/pub/au/764",
            "https://www.oreilly.com/search/?q=author%3A%22Scott+Oaks%22"
        ])

        # Call the find_year method and assert the returned year
        year = self.year_finder.find_year(self.book)
        self.assertIsNone(year)

        # Assert that the search function was called with the correct search term
        mock_search.assert_called_once_with(
            f"Test Title Test Author o'reilly", num_results=10)

        # Assert that the get function was not called
        mock_get.assert_not_called()

    # O'Reilly link is present, but the release date element is not present
    @patch('requests.get')
    @patch('googlesearch.search')
    def test_find_year_no_release_date(self, mock_search, mock_get):

        mock_search.return_value = iter([
            "https://www.oreilly.com/library/view/test-title/1234567890/",
        ])

        # Mock the get function to return a response with a specific HTML content
        mock_get.return_value.content = b'<html><div class="t-author">Oliver Oliver 2022</div></html>'

        # Call the find_year method and assert the returned year
        year = self.year_finder.find_year(self.book)
        self.assertIsNone(year)

        # Assert that the search function was called with the correct search term
        mock_search.assert_called_once_with(
            f"Test Title Test Author o'reilly", num_results=10)

        # Assert that the get function was called with the correct URL
        mock_get.assert_called_once_with(
            "https://www.oreilly.com/library/view/test-title/1234567890/")

    # O'Reilly link is present, but the release date element does not contain a year
    @patch('requests.get')
    @patch('googlesearch.search')
    def test_find_year_no_year(self, mock_search, mock_get):

        mock_search.return_value = iter([
            "https://www.oreilly.com/library/view/test-title/1234567890/",
        ])

        # Mock the get function to return a response with a specific HTML content
        mock_get.return_value.content = b'<html><div class="t-release-date">Released December 3000</div></html>'

        # Call the find_year method and assert the returned year
        year = self.year_finder.find_year(self.book)
        self.assertIsNone(year)

        # Assert that the search function was called with the correct search term
        mock_search.assert_called_once_with(
            f"Test Title Test Author o'reilly", num_results=10)

        # Assert that the get function was called with the correct URL
        mock_get.assert_called_once_with(
            "https://www.oreilly.com/library/view/test-title/1234567890/")

    # Google search returns no results
    @patch('requests.get')
    @patch('googlesearch.search')
    def test_find_year_no_results(self, mock_search, mock_get):

        mock_search.return_value = iter([])

        # Call the find_year method and assert the returned year
        year = self.year_finder.find_year(self.book)
        self.assertIsNone(year)

        # Assert that the search function was called with the correct search term
        mock_search.assert_called_once_with(
            f"Test Title Test Author o'reilly", num_results=10)

        # Assert that the get function was not called
        mock_get.assert_not_called()


if __name__ == '__main__':
    unittest.main()
