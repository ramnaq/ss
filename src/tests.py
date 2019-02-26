import sorting_service

class TestSorting:

    def setup(self):
        books_file = "../resources/books.txt"
        rules1 = "../resources/sort.conf"
        rules2 = "../resources/sort.conf2"
        rules3 = "../resources/sort.conf3"

        books = booklist(books_file)

