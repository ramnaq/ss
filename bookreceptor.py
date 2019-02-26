from sorter import TitleSorter, AuthorSorter, EditionYearSorter

class BookReceptor(object):

    def __init__(self, books, cfgfilename=None):
        self._books = books
        self._strategies = [TitleSorter(books), AuthorSorter(books), EditionYearSorter(books)]
        self._curr_rule = None
        self._rulesraw = None
        if cfgfilename is not None:
            conf_file = open(cfgfilename, 'r')
            self._rulesraw = [raw for raw in conf_file.readlines()]
            self._rulesraw.reverse()


    def sort(self):
        if self._rulesraw is None:
            '''Default sorting strategy, by title (TitleSorter)'''
            return self._strategies[0].sort()

        sorted_books = []
        limits = [0, len(self._books)]
        while self._rulesraw:
            self._define_curr_rule(self._rulesraw.pop())
            currstrategy, sorting_order = self._curr_rule
            sorted_books = currstrategy.sort(reverse=sorting_order, start=limits[0], end=limits[1])
            limits = currstrategy.equal_elements()
            if limits == []:
                break

        return sorted_books


    def _define_curr_rule(self, rawrule):
        sorting_order = 0
        r = rawrule.split(' ')
        if len(r) == 2:
            sorting_order = int(r[1])  == 1
        strategy_index = int(r[0]) - 1
        self._curr_rule = [self._strategies[strategy_index], sorting_order]


    def _sublist_books(self, limits):
        for start, end in zip(*[iter(limits)]*2):
            self._books = self._books[start:end+1]



class OrderingException(Exception):

    def __init__(self, message):
        super().__init__(message)
