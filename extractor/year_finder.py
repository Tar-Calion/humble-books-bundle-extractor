
import re
from extractor.book import Book
import requests
from bs4 import BeautifulSoup
import googlesearch


class YearFinder:

    def cut_oreilly_link(self, link: str) -> str:
        match = re.search(r'(\d{13}/)', link)
        return link[:match.end()] if match else link

    def _try_find_year_in_orelly_links(self, links: list[str]) -> str:
        for link in links:
            if link.startswith("https://www.oreilly.com/library/view/"):
                print(f"O'Reilly link found: {link}")
                fixed_link = self.cut_oreilly_link(link)
                # Get the HTML content of the link
                print(f"Getting HTML content from {fixed_link}")
                response = requests.get(fixed_link)
                html_content = response.content

                # print beginning of the HTML content
                print(f"HTML content beginning: {html_content[:1000]}")

                # Parse the HTML content
                soup = BeautifulSoup(html_content, 'html.parser')

                # Find text from <div class="t-release-date">Released December 2022</div>
                release_date_div = soup.find('div', class_='t-release-date')
                release_date_text = release_date_div.get_text(
                    strip=True) if release_date_div else "Release date not found"
                print(f"Release date text: {release_date_text}")

                # Extract the year from the text
                year = release_date_text.split()[-1]
                # Check if the year is a reasonable number
                if year.isdigit() and 1900 <= int(year) <= 2100:
                    print(f"Year: {year}")
                    return year

                print(f"Year not found in the text: {release_date_text}")
                return None
        print("No O'Reilly links found")
        return None

    def find_year(self, book: Book) -> str:
        search_term = f"{book.title} {book.author} o'reilly"
        print(f"Searching for: {search_term}")

        # Get the HTML content of the Google search results and convert to list
        search_results = list(googlesearch.search(search_term, num_results=10))

        # print the search results
        print("Search results:")
        for result in search_results:
            print(result)

        year = self._try_find_year_in_orelly_links(search_results)

        return year
