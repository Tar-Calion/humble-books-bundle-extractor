
class Book:

    def __init__(self, title, author, description, year=None, formats=[], labels=[], purchase_date=None, source=None):
        self.title = title
        self.author = author
        self.description = description
        self.year = year
        self.formats = formats
        self.labels = labels
        self.account = 'Humble Bundle'
        self.purchase_date = purchase_date
        self.source = source
