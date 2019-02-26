from sorter import TitleSorter, AuthorSorter, EditionYearSorter

class BookReceiver(object):

    def __init__(self, books, cfgfilename=None):
        self._context = Context(books)
        self._strategies = [TitleSorter(self._context), AuthorSorter(self._context), EditionYearSorter(self._context)]
        self._curr_rule = None
        self._rulesraw = None
        if cfgfilename is not None:
            conf_file = open(cfgfilename, 'r')
            self._rulesraw = [raw for raw in conf_file.readlines()]
            self._rulesraw.reverse()


    def sort(self):
        '''Calls sort() of each specific BookSorter, consuming the file self._rulesraw.
        Over each iteration, a vector 'limits' is updated with the limits of the sublist
        of books that should be sorted by the next BookSorter/strategy.'''

        if self._rulesraw is None:
            return context.update(self._strategies[0]).sort()

        sorted_books = []
        limits = [0, len(self._context.books)]
        while self._rulesraw:
            self._define_curr_rule(self._rulesraw.pop())
            currstrategy, reverse = self._curr_rule
            sorted_books = self._context.update(currstrategy, limits=limits, reverse=reverse).sort()
            limits = self._context.equal_elements_indexes()
            if limits == []:
                break

        return sorted_books


    def _define_curr_rule(self, rawrule):
        '''Defines the next rule (strategy and reverse flag) to be followed'''
        r = rawrule.split(' ')
        strategy_index = int(r[0]) - 1
        reverse = int(r[1])  == 1
        self._curr_rule = [self._strategies[strategy_index], reverse]



class Context(object):

    def __init__(self, books, strategy=None, limits=None, reverse=False):
        self.strategy = strategy
        self.books = books
        if limits is None:
            self.start, self.end = 0, len(self.books)
        self.reverse = reverse

    def update(self, strategy, books=None, limits=None, reverse=False):
        self.strategy = strategy
        self.reverse = reverse
        if books is not None:
            self.books = books
        if limits is not None:
            self.start, self.end = limits
        return self

    def sort(self):
        return self.strategy.sort(self)

    def equal_elements_indexes(self):
        return self.strategy.equal_elements()
