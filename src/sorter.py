from book import Book
from abc import ABC, abstractmethod

class BookSorter(ABC):

    @abstractmethod
    def sort(self, attrfunc, reverse=False, start=0, end=-1):
        if end == -1:
            end = len(self._books)
        self._books[start:end] = sorted(self._books[start:end], key=attrfunc, reverse=reverse)
        return self._books

    @abstractmethod
    def equal_elements(self, attrfunc):
        '''Produces a list that is interpreted with two by two of its elements.
        Said a pair [...,start,end,...], 'start' and 'end' are the indexes of self._books
        where a sublist starts and ends. A "sublist" is a list of books that don't
        differ of each other for the BookSorter, which follows 'attrfunc' as criterion.'''
        sublists_limits = []
        attrs = [attrfunc(b) for b in self._books]
        i = 0  # indicates the end of a sublist
        while i < len(attrs)-1:
            if attrs[i] == attrs[i+1]:
                start, i = self._sublist_limits(attrs, i)
                sublists_limits.append(start)
                sublists_limits.append(i)
            i += 1
        if sublists_limits == []:
            sublists_limits = [-1 -1]
        return sublists_limits


    def _sublist_limits(self, attrslist, index):
        attr = attrslist[index]
        limits = [index, index + 2]  # limits = [start, end]
        i = limits[1] + 1  # indicates the new 'end'
        while (i < len(attrslist)-1) and (attrslist[i] == attr):
            limits[1] = i
            i += 1
        return limits


class TitleSorter(BookSorter):

    FTITLE = Book.title

    def __init__(self, books):
        self._books = books

    def sort(self, attrfunc=None, reverse=False, start=0, end=-1):
        return super(TitleSorter, self).sort(TitleSorter.FTITLE, reverse, start, end)

    def equal_elements(self, attrfunc=None):
        return super(TitleSorter, self).equal_elements(attrfunc=TitleSorter.FTITLE)


class AuthorSorter(BookSorter):

    FAUTHOR = Book.author

    def __init__(self, books):
        self._books = books

    def sort(self, attrfunc=None, reverse=False, start=0, end=-1):
        return super(AuthorSorter, self).sort(AuthorSorter.FAUTHOR, reverse, start, end)

    def equal_elements(self, attrfunc=None):
        return super(AuthorSorter, self).equal_elements(attrfunc=AuthorSorter.FAUTHOR)


class EditionYearSorter(BookSorter):

    F_EDITION_YEAR = Book.edition_year

    def __init__(self, books):
        self._books = books

    def sort(self, attrfunc=None, reverse=False, start=0, end=-1):
        return super(EditionYearSorter, self).sort(EditionYearSorter.F_EDITION_YEAR, reverse, start, end)

    def equal_elements(self, attrfunc=None):
        return super(EditionYearSorter, self).equal_elements(attrfunc=EditionYearSorter.F_EDITION_YEAR)

