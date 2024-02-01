import io
import pandas as pd

from book import Book


class CsvCreator:

    def create(self, books: list[Book]):
        # Convert to DataFrame
        df_books = pd.DataFrame([book.__dict__ for book in books])
        df_books_reordered = df_books[['author', 'title', 'description']]
        df_books_reordered.insert(2, '<empty>', '')

        # Create a StringIO object to hold the CSV content
        csv_buffer = io.StringIO()

        # Write the DataFrame to the StringIO object as CSV
        df_books_reordered.to_csv(csv_buffer, sep='\t', index=False, header=False, lineterminator='\n')

        # Get the CSV content as a string
        return csv_buffer.getvalue()