# 题目一分析:
# * 相关数字的二进制表示为：
# * 2 = 0010       3 = 0011       4 = 0100
# * 5 = 0101       6 = 0110
# *
# * 步骤1 全体异或：2^4^3^6^3^2^5^5 = 4^6 = 0010
# * 步骤2 确定位置：对于0010，从右数的第二位为1，因此可以根据倒数第2位是否为1进行分组
# * 步骤3 进行分组：分成[2,3,6,3,2]和[4,5,5]两组
# * 步骤4 分组异或：2^3^6^3^2 = 6，4^5^5 = 4，因此结果为4，6。
class solution():
    def findnumonce(self, array):
        if not array:
            return None
        res = 0
        for i in array:
            res ^= i
        indexof1 = self.findfirst(res)
        num1 = num2 = 0
        for i in array:
            if self.isbit1(i, indexof1):
                num1 ^= i
            else:
                num2 ^= i
        return [num1, num2]

    def findfirst(self, num):
        indexbit = 0
        while num & 1 == 0:
            num = num >> 1
            indexbit += 1
        return indexbit

    def isbit1(self, num, indexof1):
        num = num >> indexof1
        return (num & 1)


# 在一个数组中除了一个数字只出现一次外，其他数字都出现了三次，请找出那个只出现一次的数字。
def singlenum(arr):
    return (3 * sum(set(arr)) - sum(set(arr))) // 2
# 从Python2.2开始，增加了一个操作符 // ，以执行地板除：//除法不管操作数为何种数值类型，总是会舍去小数部分，返回数字序列中比真正的商小的最接近的数字。