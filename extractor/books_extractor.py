import datetime
from bs4 import BeautifulSoup
from extractor.book import Book


class BooksExtractor:

    # Function to replace line breaks with a space and remove extra spaces
    def _butify_text(self, text):
        lines = text.split('\n')
        joined_description = ' '.join(line if line.endswith(' ') else line + ' ' for line in lines)

        return ' '.join(joined_description.split())

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
            author = self._butify_text(author)

            # Find the nearest description tag relative to the current title tag
            description_tag = title_tag.find_next('section', class_='description')
            description = description_tag.get_text(strip=True) if description_tag else 'No description available'
            description = self._butify_text(description)

            formats = self._get_formats(title_tag)

            # Get todays date as purchase date in the format DD.MM.YYYY
            purchase_date = datetime.date.today().strftime('%d.%m.%Y')
            # Find source from the 'content' attribute of the meta tag with name="title"
            source = soup.find('meta', attrs={'name': 'title'})['content']

            if author != 'Unknown' and description != 'No description available':
                books.append(Book(title, author, description, formats=formats, purchase_date=purchase_date, source=source))

        return books
