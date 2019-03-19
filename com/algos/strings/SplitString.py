'''
 Program to split the string by every nth character.
'''


def split_string(string, n):
    list = []
    i = 0
    while i < len(string):
        list.append(string[i : (i + n)])
        i += n

    return list

if __name__ == '__main__':
    list = split_string("Geeksforgeeks", 3)
    print('Splitted strings are', list)
