def getNumofCommonSubstr(str1):
    '''相当于将最长公关子串一个串反转自身'''
    lstr1 = len(str1)
    str2 = str1[::-1]
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位,并且注意顺序，之前书里的就是这个顺序找错了
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位
    print(record)
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
    str1 = 'abcdasdasadfe'
    res = getNumofCommonSubstr(str1)
    print(res)