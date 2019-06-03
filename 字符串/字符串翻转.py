def reverseStr(str):
    ch = list(str)
    lens = len(ch)
    i = 0
    j = lens - 1
    while i < j:
        ch[i], ch[j] = ch[j], ch[i]
        i += 1
        j -= 1
    return ''.join(ch)


str1 = 'abcdef'
print(reverseStr(str1))


def rev(str):
    str = str.split()
    len1 = len(str)
    i = 0
    j = len1 - 1
    while i < j:
        str[i], str[j] = str[j], str[i]
        i += 1
        j -= 1
    return ' '.join(str)
a = 'how   are you?'
print(rev(a))


def rotatestr(str,n):
    if not str or n == 0:
        return ''
    return str[n:]+str[:n]
print(str1)
print(rotatestr(str1,2))