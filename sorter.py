class Sorter(object):
    _rules = None

    def __init__(self, rules=None):
        if rules != None:
            self._rules = rules

    def sort(self, books):
        if self._rules == None:
            return self.__sortbytitle(books)

    def __sortbytitle(self, books):
        titles = list(map(lambda x: x.title.lower(), books.values()))
        sorted_titles = sorted(titles)
        return [books[title] for title in sorted_titles]
