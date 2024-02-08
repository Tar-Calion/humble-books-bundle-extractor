from bs4 import BeautifulSoup
from extractor.book import Book


class BooksExtractor:

    # Function to replace line breaks with a space, adding a space if the line does not end with one
    def _replace_linebreaks_with_space(self, text):
        lines = text.split('\n')
        return ' '.join(line if line.endswith(' ') else line + ' ' for line in lines)

    def _get_formats(self, title_tag):
        # Find all 'delivery-and-oses' div tags relative to the current title tag
        delivery_and_oses_tags = title_tag.find_all_next('div', class_='delivery-and-oses')

        # Check if there are at least two such tags
        if len(delivery_and_oses_tags) >= 2:
            # Get the second 'delivery-and-oses' div tag
            second_delivery_and_oses_tag = delivery_and_oses_tags[1]
            # get text from span tag
            formats_text = second_delivery_and_oses_tag.find('span').get_text(strip=True)
            # remove ',', 'and' and make uppercase
            formats_text = formats_text.replace(',', '').replace('and', '').upper()
            # split by space, ignore empty strings
            return list(filter(None, formats_text.split(' ')))
        else:
            return []

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

            formats = self._get_formats(title_tag)

            if author != 'Unknown' and description != 'No description available':
                books.append(Book(title, author, description, formats=formats))

        return books
