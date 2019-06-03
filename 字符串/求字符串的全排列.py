# def swap(str, i, j):
#
#     tem = str[i]
#     str[i] = str[j]
#     str[j] = tem
#
#
# def permutation(str, start):
#     if str is None or start < 0:
#         return False
#     if start == len(str) - 1:
#         print(''.join(str))
#     else:
#         i = start
#         while i < len(str):
#             swap(str, start, i)
#             permutation(str, start + 1)
#             swap(str, start, i)
#             i += 1
#
#
# s = 'abc'
# s = list(s)
# permutation(s, 0)


def permutation1(s, i):
    if i == len(s):
        print(s)
    else:
        for j in range(i, len(s)):
            s[j], s[i] = s[i], s[j]
            permutation1(s, i + 1)
            s[j], s[i] = s[i], s[j]


test = "abcd"
s = list(test)  # 字符串转为数组 ["a","b","c"]
permutation1(s, 0)

# s = 'abc'
# print(s)
# permutation(s, 0)
