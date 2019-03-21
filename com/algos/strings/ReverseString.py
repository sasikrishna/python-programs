'''
Program to reverse given string.
'''

def reverse_string(string):

    # Reversing using slicing
    for char in string[ : : -1]:
        print(char, end = ' ')

    print()

    # Reversing using pre-defined reverse function
    print(list(reversed(string)))


if __name__ == '__main__':
    string = 'geeks'
    reverse_string(string)
