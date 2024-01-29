from bs4 import BeautifulSoup
import pandas as pd



# Load the HTML content from file
html_file_path = 'bundle-info.html'
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()


# Function to replace line breaks with a space, adding a space if the line does not end with one
def replace_linebreaks_with_space(text):
    lines = text.split('\n')
    return ' '.join(line if line.endswith(' ') else line + ' ' for line in lines)


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
    description = replace_linebreaks_with_space(description)  # Replace line breaks

    books.append({'Title': title, 'Author': author, 'Description': description})

# Filter out books without author and description
filtered_books = [book for book in books if book['Author'] != 'Unknown' and book['Description'] != 'No description available']

# Convert to DataFrame
df_books = pd.DataFrame(filtered_books)
df_books_reordered = df_books[['Author', 'Title', 'Description']]
df_books_reordered.insert(2, '<empty>', '')

# Convert the DataFrame to a TSV file without header and save it
tsv_file_path = 'book_info.tsv'
df_books_reordered.to_csv(tsv_file_path, sep='\t', index=False, header=False)