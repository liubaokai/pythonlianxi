def swap(str, i, j):
    str = list(str)
    tem = str[i]
    str[i] = str[j]
    str[j] = tem


def permutation(str, start):
    if str is None or start < 0:
        return False
    if start == len(str) - 1:
        print(''.join(str))
    else:
        i = start
        while i < len(str):
            swap(str, start, i)
            permutation(str, start + 1)
            swap(str, start, i)
            i += 1


s = 'abc'
permutation(s, 0)
