'''
Problem statement: Given a string s, recursively remove adjacent duplicate characters from the string s.
The output string should not have any adjacent duplicates.
'''


def remove_adjacent_letter(char_list):
    clean_str = ""

    if char_list[0] != char_list[1]:
        clean_str += char_list[0]

    i = 1
    while i < len(char_list):
        if char_list[i] != char_list[i - 1]:
            if i + 1 == len(char_list) or char_list[i] != char_list[i+1]:
                clean_str += char_list[i]
        i += 1

    if len(clean_str) == 0:
        return clean_str

    if len(clean_str) != len(char_list) and len(clean_str) > 1:
        return remove_adjacent_letter(list(clean_str))

    return clean_str


if __name__ == '__main__':
    test_cases = int(input())
    strings = []

    for i in range(test_cases):
        strings.append(input())

    for i in range(test_cases):
        print(remove_adjacent_letter(list(strings[i])))

