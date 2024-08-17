# humble-books-bundle-extractor
Extracts book infos from the humble bundle pages: title, author, description, year, keywords, etc.

1. Finds title, author, description and formats from the file "bundle-info.html"
2. Uses the OpenAI API to find the keywords using the book info
3. Uses the [Tavily Search](https://tavily.com/) to find websites with the book info. The year of the book is extracted from the websites using the OpenAI API
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
- OpenAI API key
- Tavily Search API key

## Installation
- Install the requirements with `pip install -r requirements.txt`
- Configure the OpenAI API key and the model name in the file ".env". See the file ".env_example" for an example
- Configure the Tavily Search API key in the file ".env". See the file ".env_example" for an example

## Usage
1. Download the humble bundle page (Save as "Webpage, Complete") and save it as "bundle-info.html" in the project folder
1. Adjust flags in main.py to run the desired steps: stage_2_label_books_with_openai, stage_3_find_years_with_tavily
1. Run main.py
1. The book info will be saved in "book-info-before-labeling.tsv", "book-info-after-labeling.tsv" and "book-info-after-year-finding.tsv"


## Future work
- Use Langchain instead of OpenAI client everywhere
- Automate the Humble Bundle Page download
