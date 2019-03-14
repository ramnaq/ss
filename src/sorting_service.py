#!/usr/bin/python

from book import Book
from bookreceiver import BookReceiver
import sys


class OrderingException(Exception):
    def __init__(self, message):
        super().__init__(message)

def booklist(filename):
    books_file = open(filename, 'r')
    books_raw = [raw[:-1] for raw in books_file.readlines()]
    books = []
    for bstr in books_raw:
        infos = bstr.split(',')
        try:
            books.append(Book(infos[0], infos[1], infos[2]))
        except:
            raise OrderingException("Did you provide a file of a list of books?\nYou should run: "\
                    + "python sorting_service.py <books.txt> [OPTIONAL <sort.conf>]")
    return books

def printbooks(books):
    if not books:
        print("(Empty list)")
    else:
        last = books.pop()
        for b in books:
            print(b, '\n')
        print(last)

def main():
    numargs = len(sys.argv)

    if numargs > 3:
        print("Error! More than 2 argument were provided.\n"\
                + "You should run 'python sorting_service.py <booksfile> [OPTIONAL <sort.conf>]'.")
        exit(1)

    books = booklist(sys.argv[1])
    if numargs == 2:
        print("No configuration file was provided. Default sorting: Title ascending.")
        context = BookReceiver(books)
        sorted_books = context.organize()
    elif numargs == 3:
        context = BookReceiver(books, cfgfilename=sys.argv[2])
        sorted_books = context.organize()
    
    printbooks(sorted_books)


if __name__ == "__main__":
    main()

