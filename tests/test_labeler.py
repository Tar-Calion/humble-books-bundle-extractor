import unittest
from unittest.mock import patch, MagicMock
from extractor.book import Book
from extractor.labeler import Labeler


class TestLabeler(unittest.TestCase):

    def setUp(self):
        self.book = Book("Test Title", "Test Author", "Test Description")
        self.labeler = Labeler(openai_client=None, simulate=False)

    def test_get_labels(self):
        with patch.object(self.labeler, 'openai_client', new_callable=MagicMock) as mock_openai_client:
            mock_openai_client.chat.completions.create.return_value = MagicMock(
                choices=[MagicMock(message=MagicMock(content="Label 1, Label 2, Label 3"))])
            labels = self.labeler.get_labels(self.book)
            self.assertEqual(labels, ["Label 1", "Label 2", "Label 3"])

            # Assert that 'create' was called with the correct parameters
            expected_messages = [
                {
                    "role": "system",
                    "content": ("Analyze the book data provided and suggest 1 to 3 labels or themes that best characterize the book. "
                                "Consider the author, title, and description to determine the overarching themes or specific topics discussed in the book. "
                                "Once you have identified the themes, please provide them in your response, separated by commas. "
                                "Valid response may look like that: Java, Software Architecture")
                },
                {
                    "role": "user",
                    "content": "Title: {}\nAuthor: {}\nDescription: {}".format(self.book.title, self.book.author, self.book.description)
                }
            ]
            mock_openai_client.chat.completions.create.assert_called_with(
                messages=expected_messages,
                model=unittest.mock.ANY
            )
            self.assertTrue(mock_openai_client.chat.completions.create.call_args[1]['model'].startswith("gpt-3.5"))

    def test_get_labels_simulation(self):
        self.labeler.simulate = True
        labels = self.labeler.get_labels(self.book)
        self.assertEqual(labels, ["Label 1", "Label 2", "Label 3"])


if __name__ == '__main__':
    unittest.main()
