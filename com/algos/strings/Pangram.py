
'''
 Program to check if that string is Pangram or not.
 A pangram is a sentence containing every letter in the English Alphabet.
'''


def ispangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
    return True


if __name__ == '__main__':
    string = 'Geek for geeks'
    if ispangram(string):
        print(string, 'is pangram')
    else:
        print(string, 'is not pangram')

    string = 'The quick brown fox jumps over the lazy dog'
    if ispangram(string):
        print(string, 'is pangram')
    else:
        print(string, 'is not pangram')

