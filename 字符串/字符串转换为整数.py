class Solution:
    def StrToInt(self, s):
        # write code here
        if s == '':
            return 0
        ret = 0
        num = 0
        fuhao = 1
        for i in s[::-1]:
            if i < '0' or i > '9':
                if i == '-':
                    fuhao = -1
                    continue
                elif i == '+':
                    continue
                else:
                    return 0
            ret += int(i) * pow(10, num)
            num += 1
        return ret * fuhao
