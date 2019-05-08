'''
Problem statement: Given a string S. The task is to print all permutations of a given string.
'''

permutations = []


def print_permutations(word):
    char_list = list(word)
    count = {}
    for i in char_list:
        if i not in count:
            count[i] = 0
        count[i] += 1

    __print_permutations(''.join(sorted(word)), count, [0] * len(word), 0)
    for permutation in permutations:
        print(permutation, end=" ")
    permutations.clear()
    print()


def __print_permutations(word, count_map, permutation, level):

    # If count is zero for every char in count_map then print permutation and return
    if sum(count_map.values()) == 0:
        permutations.append(''.join(permutation))
        return

    for letter in word:

        if not count_map[letter]:
            continue

        permutation[level] = letter
        count_map[letter] -= 1
        __print_permutations(word, count_map, permutation, level + 1)
        count_map[letter] += 1


def swap(i, j, string):
    char_list = list(string)
    char_list[i], char_list[j] = char_list[j], char_list[i]
    return ''.join(char_list)


if __name__== '__main__':
    test_cases = int(input())
    strings = []

    for i in range(test_cases):
        strings.append(input())

    for i in range(test_cases):
        print_permutations(strings[i])
