# humble-books-bundle-extractor
Extracts book infos from the humble bundle pages: title, author, description, year, keywords, etc.

1. Finds title, author, description and formats from the file "bundle-info.html"
2. Uses the OpenAI GPT-3 API to find the keywords using the book info
3. Uses the Google Search to find websites with the book info. Scraps specific websites to find the year of the book. Currently only oreilly.com is supported
4. Saves the book info in a tab separated values file after each step

## Output format
- The output is a tab separated values file with the following columns:
  - Author
  - Title
  - Year
  - Description
  - Keywords (e.g. "Machine Learning, No-Code AI, Data Analysis")
  - Account "Humble Bundle"
  - Formats (e.g. "PDF, EPUB, MOBI")
  - Purchase date (date when the tool was run)


## Requirements
- OpenAI GPT-3 API key 

## Installation
- Install the requirements with `pip install -r requirements.txt`
- Configure the OpenAI GPT-3 API key and the model name in the file ".env". See the file ".env_example" for an example

## Usage
1. Download the humble bundle page and save it as "bundle-info.html"
1. Adjust flags in main.py to run the desired steps: stage_2_label_books_with_openai, stage_3_find_years
1. Run main.py
1. The book info will be saved in "book-info-before-labeling.tsv", "book-info-after-labeling.tsv" and "book-info-after-year-finding.tsv"

## Known issues
- The Google Search may be blocked by Google if the script is run too many times in a short period of time. The script will stop with an error message "429 Client Error: Too Many Requests for url..."

## Future work
- Use a SERP API to avoid the Google Search block and manual scrapping
- Add support for more websites to find the year of the book
  - Or use an AI API to find the year of the book from the scrapped websites
  - Or use an AI API for Internet search and scrapping to find the year of the book when such service is available (currently not available in the OpenAI API)
