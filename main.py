from extractor.books_extractor import BooksExtractor
from extractor.tsv_creator import CsvCreator


# Load the HTML content from file
html_file_path = 'bundle-info.html'
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

books = BooksExtractor().extract(html_content)

tsv = CsvCreator().create(books)

# Write the TSV content to file
tsv_file_path = 'book-info.csv'
with open(tsv_file_path, 'w', encoding='utf-8') as tsv_file:
    tsv_file.write(tsv)




