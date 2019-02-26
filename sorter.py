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
        limits = [index, index + 2]  # [start, end]
        i = limits[1] + 1 # indicates the new 'end'
        while (i < len(attrslist)-1) and (attrslist[i] == attr):
            limits[1] = i
            i += 1
        return limits


class TitleSorter(BookSorter):

    def __init__(self, books):
        self._books = books

    def sort(self, attrfunc=None, reverse=False, start=0, end=-1):
        return super(TitleSorter, self).sort(Book.title, reverse, start, end)

    def equal_elements(self, attrfunc=None):
        return super(TitleSorter, self).equal_elements(attrfunc=Book.title)


class AuthorSorter(BookSorter):

    def __init__(self, books):
        self._books = books

    def sort(self, attrfunc=None, reverse=False, start=0, end=-1):
        return super(AuthorSorter, self).sort(Book.author, reverse, start, end)

    def equal_elements(self, attrfunc=None):
        return super(AuthorSorter, self).equal_elements(attrfunc=Book.author)


class EditionYearSorter(BookSorter):

    def __init__(self, books):
        self._books = books

    def sort(self, attrfunc=None, reverse=False, start=0, end=-1):
        return super(EditionYearSorter, self).sort(Book.edition_year, reverse, start, end)

    def equal_elements(self, attrfunc=None):
        return super(EditionYearSorter, self).equal_elements(attrfunc=Book.edition_year)

