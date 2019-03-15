from sorter import TitleSorter, AuthorSorter, EditionYearSorter

class BookReceiver(object):

    def __init__(self, books, cfgfilename=None):
        self._books = books
        self._strategies = [TitleSorter(books), AuthorSorter(books), EditionYearSorter(books)]
        self._curr_rule = None  # has the form [BookSorter, int] (strategy and reverse order flag)
        self._rulesraw = None
        if cfgfilename is not None:
            conf_file = open(cfgfilename, 'r')
            self._rulesraw = [raw for raw in conf_file.readlines()]
            # _rulesraw will be consumed with pop() (from the end backwards)
            self._rulesraw.reverse()


    def organize(self):
        '''Calls sort() of each specific BookSorter, consuming the list self._rulesraw.
        Over each iteration, a vector 'limits' is updated with the limits of the sublist
        of books that should be sorted by the next BookSorter/strategy.'''

        if self._rulesraw is None:
            '''Default sorting strategy, by title (strategy TitleSorter)'''
            return self._strategies[0].sort()

        sorted_books = []
        limits = [0, len(self._books)]
        while self._rulesraw:
            self._define_curr_rule(self._rulesraw.pop())
            currstrategy, reverse = self._curr_rule
            sorted_books = currstrategy.sort(reverse=reverse, start=limits[0], end=limits[1])
            limits = currstrategy.equal_elements()
            if limits == []:
                break

        return sorted_books


    def _define_curr_rule(self, rawrule):
        '''Defines the next rule (strategy and reverse flag) to be followed'''
        r = rawrule.split(' ')
        strategy_index = int(r[0]) - 1
        reverse = int(r[1]) == 1
        self._curr_rule = [self._strategies[strategy_index], reverse]

