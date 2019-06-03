def getMaxSubStr(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    sb = ''
    maxs = 0
    maxl = 0
    matrix = [[0] * (len1 + 1) for i in range(len2 + 1)]
    while i < len2 + 1:
        j = 1
        while j < len1 + 1:
            if list(str1)[j - 1] == list(str2)[i - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > maxs:
                    maxs = matrix[i][j]
                    maxl = j
            else:
                matrix[i][j] = 0
            j += 1
        i += 1

    i = maxl - maxs
    while i < maxl:
        sb = sb + list(str1)[i]
        i += 1
    return sb


if __name__ == '__main__':
    str1 = 'absasdsdasfad'
    str2 = 'bssasdasfd'
    print(getMaxSubStr(str1, str2))

# coding:utf-8
'''
求两个字符串的最长公共子串 
思想：建立一个二维数组，保存连续位相同与否的状态
'''

def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位,并且注意顺序，之前书里的就是这个顺序找错了
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    return str1[p - maxNum:p], maxNum


if __name__ == '__main__':
    str1 = 'abcdfe'
    str2 = 'cdfe'

    res = getNumofCommonSubstr(str1, str2)
    print(res)
