# Sorting Service (SS)
A sorting and classification service for books.

## How to
The SS can be run with the following command:
```sh
$ python sorting_service.py <books.txt> [OPTIONAL <rules.txt>]
```
The first parameter is a file with a list of books. The books have to be registered
line by line, following the pattern `<title>,<authors>,<edition year>` (without spaces
between a commas and the words). An example of this can be found in [books.txt](resources/books.txt).

The optional parameter indicates the rules of sorting (e.g. title (ascending), author(descending)).
The rules have to be registered line by line, following the pattern `<book param numer> <descending flag>`,
where the numbers of the book parameters are: 1 (title), 2 (author), 3 (edition year); and
`<descending flag>` is 1 when you want the order to be "descendent" (otherwise it is 0).
Notice that an whitespace must be between the two numbers. An example of this can be found in
[sort.conf](resources/sort.conf)

## Spec
Language: [Python 3.7.1](https://www.python.org/downloads/release/python-371/)

