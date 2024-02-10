
from extractor.book import Book
import requests
from bs4 import BeautifulSoup
from googlesearch import search


class YearFinder:

    def _filter_links(self, search_results: list[str]) -> list[str]:
        bad_websites = ["amazon", "ebay"]
        good_links = []

        # filter out links that contain bad websites
        for result in search_results:
            if not any(bad_website in result for bad_website in bad_websites):
                good_links.append(result)

        return good_links

    def _try_find_year_in_orelly_links(self, links: list[str]) -> str:
        for link in links:
            if "oreilly.com" in link:
                # Get the HTML content of the link
                print(f"Getting HTML content from {link}")
                response = requests.get(link)
                html_content = response.content

                # print beginning of the HTML content
                print(f"HTML content beginning: {html_content[:1000]}")

                # Parse the HTML content
                soup = BeautifulSoup(html_content, 'html.parser')

                # Find text from <div class="t-release-date">Released December 2022</div>
                release_date_text = soup.find('div', class_='t-release-date').get_text(strip=True)
                print(f"Release date text: {release_date_text}")

                # Extract the year from the text
                year = release_date_text.split()[-1]
                print(f"Year: {year}")

                return year

        return None

    def find_year(self, book: Book) -> str:
        search_term = f"{book.title} {book.author} year of publication"
        print(f"Searching for: {search_term}")

        # Get the HTML content of the Google search results and convert to list
        search_results = list(search(search_term, num_results=10))

        # print the search results
        print("Search results:")
        for result in search_results:
            print(result)

        # filter out links that contain bad websites
        good_links = self._filter_links(search_results)
        print("Good links:")
        for link in good_links:
            print(link)

        year = self._try_find_year_in_orelly_links(good_links)

        return year
