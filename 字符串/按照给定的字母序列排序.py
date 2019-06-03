# priority = {'d': 0, 'f': 1, 'e': 2, 'c': 3, 'a': 4}
#
#
# def keyfunc(str):
#     return priority[str[0]]
#
#
# slist = {'deec', 'dac', 'ceef', 'fee'}
# result = sorted(slist, key=keyfunc)
def compare(str1, str2, char_int):
    len1 = len(str1)
    len2 = len(str2)
    i, j = 0, 0
    while i < len1 and j < len2:
        if list(str1)[i] not in char_int.keys():
            char_int[list(str1)[i]] = -1
        if list(str2)[j] not in char_int.keys():
            char_int[list(str2)[j]] = -1
        if char_int[list(str1)[i]] < char_int[list(str2)[j]]:
            return -1
        elif char_int[list(str1)[i]] > char_int[list(str2)[j]]:
            return 1
        else:
            i += 1
            j += 1
    if i == len1 and j == len2:
        return 0
    elif i == len1:
        return -1
    else:
        return 1


def bubble(s, char_int):
    lens = len(s)
    for i in range(lens):
        for j in range(lens - 1):
            if compare(s[j], s[j + 1], char_int) == -1:
                pass
            else:
                s[j], s[j + 1] = s[j + 1], s[j]


if __name__ == '__main__':
    s = ['bed', 'dog', 'dear', 'eye']
    sequeue = 'dgecfboa'
    lens1 = len(sequeue)
    char_int = dict()
    i = 0
    while i < lens1:
        char_int[list(sequeue)[i]] = i
        i += 1
    bubble(s, char_int)
    i = 0
    while i < len(s):
        print(s[i])
        i += 1
