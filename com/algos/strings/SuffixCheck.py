
'''
Program to check whether list contains any string which matches with given suffix.
'''


def suffix_check(list, suffix):

    if len(list) == 0 or suffix is None:
        return False

    for string in list:
        if string.lower().endswith(suffix.lower()):
            return True

    return False


if __name__ == "__main__":
    print("List contains 'geeks'") if suffix_check(("Paras", "Geeksforgeeks", "Game"), "Geeks") else print("List not contains geeks")
