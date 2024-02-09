
class Book:

    def __init__(self, title, author, description, year=None, formats=[], labels=[]):
        self.title = title
        self.author = author
        self.description = description
        self.year = year
        self.formats = formats
        self.labels = labels
        self.account = 'Humble Bundle'
