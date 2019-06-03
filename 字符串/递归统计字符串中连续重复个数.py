def get_max(s, s_index=0, curmax=1, lenmax=1):
    if s_index == len(s) - 1:
        return max(curmax, lenmax)
    if list(s)[s_index] == list(s)[s_index + 1]:
        return get_max(s, s_index + 1, curmax + 1, lenmax)
    else:
        return get_max(s, s_index + 1, 1, max(curmax, lenmax))


if __name__ == '__main__':
    print(str(get_max('abbbbccc')))
