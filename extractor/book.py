
class Book:

    def __init__(self, title, author, description, year=None, formats=[]):
        self.title = title
        self.author = author
        self.description = description
        self.year = year
        self.formats = formats

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author and self.description == other.description and self.year == other.year and self.formats == other.formats
        return False
