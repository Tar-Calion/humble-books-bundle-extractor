import io
import pandas as pd

from extractor.book import Book


class CsvCreator:

    def create(self, books: list[Book]):
        if not books:
            return ''

        # Convert to DataFrame
        df_books = pd.DataFrame([book.__dict__ for book in books])
        df_books_reordered = df_books[['title', 'author', 'year', 'description', 'labels', 'account', 'formats', 'purchase_date', 'source']]

        # Handle empty or non-numeric 'year' values, remove decimal part
        df_books_reordered['year'] = df_books_reordered['year'].apply(
            lambda x: '' if pd.isna(x) else str(int(x)))

        # join the labels list into a string, separated by ', '
        df_books_reordered['labels'] = df_books_reordered['labels'].apply(
            lambda x: ', '.join(x) if x else '')

        # join the formats list into a string, separated by ', '
        df_books_reordered['formats'] = df_books_reordered['formats'].apply(
            lambda x: ', '.join(x) if x else '')

        # Create a StringIO object to hold the CSV content
        csv_buffer = io.StringIO()

        # Write the DataFrame to the StringIO object as CSV
        df_books_reordered.to_csv(
            csv_buffer, sep='\t', index=False, header=False, lineterminator='\n', quoting=1, quotechar='"')

        # Get the CSV content as a string
        return csv_buffer.getvalue()
