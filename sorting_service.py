#!/usr/bin/python

from book import Book
from sorter import BookReceptor
import sys

def booklist():
    books_file = open("books.txt", 'r')
    books_raw = [raw[:-1] for raw in books_file.readlines()]
    books = []
    for bstr in books_raw:
        infos = bstr.split(',')
        books.append(Book(infos[0], infos[1], infos[2]))

    return books


def main():
    books = booklist()
    if len(sys.argv) == 1:
        print("No configuration file. Default sorting: Title ascending.")
        context = BookReceptor(books)
        sorted_books = context.sort()
    elif len(sys.argv) == 2:
        context = BookReceptor(books, cfgfilename=sys.argv[1])
        sorted_books = context.sort()
    
    for b in sorted_books:
        print(b, '\n')


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error! More than 1 argument were provided.\n"\
                + "You should run 'python sorting_service.py <sort.conf>'.")
        exit(1)

    main()

