
'''
Program to remove numbers from given string.
'''


def remove_numbers(string):
    string = ''.join([i for i in string if not i.isdigit()])
    return string


if __name__ == '__main__':
    print('String after removing numbers from A1B2C3D4 is', remove_numbers('A1B2C3D4'))
    print('String after removing numbers from DEFR234DGE2 is', remove_numbers('DEFR234DGE2'))
