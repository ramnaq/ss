class Book(object):
    
    def __init__(self, title, author, edition_year):
        self._title = title
        self._author = author 
        self._edition_year = edition_year 

    def title(self):
        return self._title

    def author(self):
        return self._author

    def edition_year(self):
        return self._edition_year

    def __str__(self):
        return """Title: {}
Author: {}
Edition year: {}""".format(self._title, self._author, self._edition_year)
