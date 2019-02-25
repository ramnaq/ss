import abc

class BookReceptor(object):
    
    def __init__(self, strategy, cfgfilename=None):
        self._sortstrategy = strategy
        if cfgfilename:
            conf_file = open(self._cfgfilename, 'r')
            self._rules = [raw[:-1] for raw in conf_file.readlines()]

    def sort(self):
        return self._sortstrategy.sort()

class BookSorter(abc.ABC):
    @abc.abstractmethod
    def sort(self, reverse=False):
        pass


class TitleSorter(BookSorter):
    
    def __init__(self, books):
        self._books = {}
        for b in books:
            self._books[b.title.lower()] = b

    def sort(self, reverse=False):
        titles = list(map(lambda x: x.title.lower(), self._books.values()))
        sorted_titles = sorted(titles, reverse=reverse)
        return [self._books[title] for title in sorted_titles]


class AuthorSorter(BookSorter):

    def __init__(self, books):
        self._books = {}
        for b in books:
            self._books[b.author.lower()] = b

    def sort(self, reverse=False):
        authors = list(map(lambda x: x.title.lower(), self._books.values()))
        sorted_authors = sorted(authors, reverse=reverse)
        return [self._books[title] for title in sorted_authors]


class EditionYearSorter(BookSorter):

    def __init__(self, books):
        self._books = {}
        for b in books:
            self._books[b.edition_year.lower()] = b

    def sort(self, reverse=False):
        edyear = list(map(lambda x: x.title.lower(), self._books.values()))
        sorted_edyear = sorted(edyear, reverse=reverse)
        return [self._books[title] for title in sorted_edyear]

    '''
    def __init__(self, rules=None):
        self._rules = rules
        self.sorting_types = {\
            "__sortbytitle": self.__sortbytitle,\
            "__sortbyauthor": self.__sortbyauthor,\
            "__sortbyedition": self.__sortbyedition\
        }

    def sort(self, books):
        if self._rules == None:
            return self.__sortbytitle(books)

        sorted_books = []
        for rule_raw in self._rules:
            rule = rule_raw.split(' ')
            if len(rule) == 2:
                print(rule[0], ' ', rule[1])
                sorting_types[rule[0]](books, rule[1] == '1')
            else:
                self.sorting_types["__" + rule[0]](books)

    def __sortbytitle(self, books, reverse=False):
        titles = list(map(lambda x: x.title.lower(), books.values()))
        sorted_titles = sorted(titles, reverse=reverse)
        return [books[title] for title in sorted_titles]

    def __sortbyauthor(self, books, reverse=False):
        authors = list(map(lambda x: x.author.lower(), books.values()))
        sorted_authors = sorted(authors)
        return [books[title] for title in sorted_authors]

    def __sortbyedition(self, books, reverse=False):
        titles = list(map(lambda x: x.title.lower(), books.values()))
        sorted_titles = sorted(titles)
        return [books[title] for title in sorted_titles]
        '''
