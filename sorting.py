alphabet = {'a': 1, 'c': 2, 'b': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
        'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
        'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'x': 23, 'w': 24,
        'y': 25, 'z': 26}

def sortbyname(titles):
    titles = list(map(lambda x: x.lower(), titles))
    return sorted(titles)




'''
    titles_length = list(map(lambda x: len(x), titles))

    order = {}
    i = 0
    #while i < min(titles_length):
    for title in titles:
        print(title)
        letter = title[i]
        order(alphabet[letter])  # append letter number (e.g. a = 1)
        #i += 1;
    print(sorted(order))


if __name__ == '__main__':
    titles = ["Java How To Program", "Patterns of Enterprise Application Architecture",
            "Head First Design Patterns", "Internet & World Wide Web: How to Program"]

    sortbyname(titles);
'''
