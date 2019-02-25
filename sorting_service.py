#!/usr/bin/python

from book import Book
from sorter import BookReceptor, TitleSorter
import sys

def booklist():
    books_file = open("books.txt", 'r')
    books_raw = [raw[:-1] for raw in books_file.readlines()]
    books = []
    for bstr in books_raw:
        infos = bstr.split(',')
        books.append(Book(infos[0], infos[1], infos[2]))

    return books


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error! More than 1 argument were provided.\n"\
                + "You should run 'python sorting_service.py <sort.conf>'.")
        exit(1)

    if len(sys.argv) == 1:
        print("No configuration file. Default sorting: Title ascending.")
        books = booklist()
        context = BookReceptor(TitleSorter(books))
        sorted_books = context.sort()
    elif len(sys.argv) == 2:
        conf_file_name = sys.argv[1]
        rules = book_receptor.sorting_rules(conf_file_name)
        sorted_books = book_receptor.sort_books(rules)
    
    for b in sorted_books:
        print(b, '\n')

