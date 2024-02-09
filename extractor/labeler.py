# This class can find labels from a book description. It uses the ChatGPT API in order to do it.
from openai import OpenAI
import os

from extractor.book import Book


class Labeler:

    def __init__(self, simulate: bool = False):
        self.simulate = simulate

    def get_labels(self, book: Book) -> list[str]:
        print("Getting labels for the book:\n" +
              f"Title: {book.title}\n" +
              f"Author: {book.author}\n" +
              f"Description: {book.description}")

        if self.simulate:
            print("Simulating the labeler...")
            return ["Label 1", "Label 2", "Label 3"]

        client = OpenAI(
            # This is the default and can be omitted
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": ("Analyze the book data provided and suggest 1 to 3 labels or themes that best characterize the book. "
                                "Consider the author, title, and description to determine the overarching themes or specific topics discussed in the book. "
                                "Once you have identified the themes, please provide them in your response, separated by commas."
                                "Valid response may look like that: Java, Software Architecture")
                },
                {
                    "role": "user",
                    "content": "Title: {}\nAuthor: {}\nDescription: {}""".format(book.title, book.author, book.description)
                }
            ],
            model="gpt-3.5-turbo-0125",
        )

        print("Used model: {}".format(chat_completion.model))

        response = chat_completion.choices[0].message.content

        print("Received response: {}".format(response))

        return response.split(', ')
