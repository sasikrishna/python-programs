'''
 Print first n permutations of given string such that no permutation is repeated.
'''

from itertools import permutations

def getpermutations(string, n):
    charlist = sorted(list(string))
    permlist = permutations(charlist)

    i = 0
    unique_perm_list = []
    while i < n:
        permutation = ''.join(permlist.__next__())

        if permutation not in unique_perm_list:
            unique_perm_list.append(permutation)
            i += 1

    return unique_perm_list


if __name__ == '__main__':
    string = 'geeks'
    print('10 permuations of geeks are', getpermutations(string, 10))
