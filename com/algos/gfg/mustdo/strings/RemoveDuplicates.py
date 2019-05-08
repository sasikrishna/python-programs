'''
Problem statement: Given a string, the task is to remove duplicates from it. Expected time complexity O(n) and  O(1)
space.
'''


def remove_duplicates(char_list):
    counter, index = 0, 0

    for i in range(len(char_list)):
        char_index = ord(char_list[i]) - 97

        if char_index > 26:
            index += 1
            continue

        if counter & (1 << char_index) == 0:
            char_list[index] = chr(97 + char_index)
            counter = counter | (1 << char_index)
            index += 1

    return ''.join(char_list[:index])


if __name__ == '__main__':
    test_cases = int(input())
    strings = []

    for i in range(test_cases):
        strings.append(input())

    for i in range(test_cases):
        print(remove_duplicates(list(strings[i])))

