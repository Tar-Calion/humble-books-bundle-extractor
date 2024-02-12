from openai import OpenAI
from extractor.book import Book
from extractor.books_extractor import BooksExtractor
from extractor.tsv_creator import CsvCreator
from extractor.labeler import Labeler
from dotenv import load_dotenv

from extractor.year_finder import YearFinder
import time

stage_2_label_books_with_openai = False
stage_3_find_years = False


def save_books_as_tsv(books: list[Book], suffix: str = ''):
    tsv = CsvCreator().create(books)
    # Write the TSV content to file
    tsv_file_path = 'book-info-{}.tsv'.format(suffix)
    with open(tsv_file_path, 'w', encoding='utf-8') as tsv_file:
        tsv_file.write(tsv)


load_dotenv(override=True)


# Load the HTML content from file
html_file_path = 'bundle-info.html'
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

books = BooksExtractor().extract(html_content)
save_books_as_tsv(books, 'before-labeling')

if stage_2_label_books_with_openai:
    for book in books:
        book.labels = Labeler(openai_client=OpenAI(), simulate=False).get_labels(book)

    save_books_as_tsv(books, 'after-labeling')

if stage_3_find_years:
    books[3].year = YearFinder().find_year(books[3])
    for book in books:
        # Wait for 10 seconds
        print("Waiting for 10 seconds...")
        time.sleep(5)

        book.year = YearFinder().find_year(book)

    save_books_as_tsv(books, 'after-year-finding')
