#!/usr/bin/python

from book import Book
from sorter import Sorter
import sys

class BookReceptor(object):

    __instance = None

    @staticmethod
    def getInstance():
        if BookReceptor.__instance == None:
            BookReceptor()
        return BookReceptor.__instance
    

    def __init__(self):
        if BookReceptor.__instance != None:
            raise Exception("This class cannot be instantiated directly!")
        else:
            BookReceptor.__instance = self


    def sort_books(self, rules=None):
        books_file = open("books.txt", 'r')
        books_raw = [raw[:-1] for raw in books_file.readlines()]
        books = self.__books_dict(books_raw)

        sorter = Sorter(rules)
        return sorter.sort(books)
    

    def sorting_rules(conf_file_name):
        conf_file = open(conf_file_name, 'r')
        rules_raw = [raw for raw in conf_file.readlines()]
        return rules_raw.split()


    def __books_dict(self, books_raw):
        books = {}
        for book_str in books_raw:
            infos = book_str.split(',')
            title = infos[0]
            books[title.lower()] = Book(title, author=infos[1], edition_year=infos[2])
        return books



if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error! More than 1 argument were provided.\n"\
                + "You should run 'python sorting_service.py <sort.conf>'.")
        exit(1)

    book_receptor = BookReceptor()
    if len(sys.argv) == 1:
        print("No configuration file. Default sorting: Title ascending.")
        sorted_books = book_receptor.sort_books()
    elif len(sys.argv) == 2:
        conf_file_name = sys.argv[1]
        rules = book_receptor.sorting_rules(conf_file_name)
        sorted_books = book_receptor.sort_books(rules)
    
    for b in sorted_books:
        print(b, '\n')

