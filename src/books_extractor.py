from bs4 import BeautifulSoup
from book import Book


class BooksExtractor:

    # Function to replace line breaks with a space, adding a space if the line does not end with one
    def _replace_linebreaks_with_space(self, text):
        lines = text.split('\n')
        return ' '.join(line if line.endswith(' ') else line + ' ' for line in lines)

    def extract(self, html_content):
        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract book titles, authors, and descriptions
        books = []

        for title_tag in soup.find_all('h2', class_='heading-medium'):
            title = title_tag.get_text(strip=True)

            # Find the nearest author tag relative to the current title tag
            author_tag = title_tag.find_next('div', class_='publishers-and-developers')
            author = author_tag.find('span').get_text(strip=True) if author_tag else 'Unknown'

            # Find the nearest description tag relative to the current title tag
            description_tag = title_tag.find_next('section', class_='description')
            description = description_tag.get_text(strip=True) if description_tag else 'No description available'
            description = self._replace_linebreaks_with_space(description)

            if(author == 'Unknown' or description == 'No description available'):
                continue

            books.append(Book(title, author, description))
        return books
