def max_sub(array):
    '''O(n^2)'''
    if not array:
        return
    max_sum = -2 ** 32
    i = 0
    while i < len(array):
        sums = 0
        j = i
        while j < len(array):
            sums += array[j]
            if sums > max_sum:
                max_sum = sums
            j += 1
        i += 1
    return max_sum


# 问题描述：
#
# 例如：[6,-3,-2,7,-15,1,2,2]求连续子数组中的最大和，此数组中最大和为8，从arr[0]到arr[3]。其余位置都比这个要小。
#
# 最大连续子数组的特点：
#
# (1)第一个不为负数
#
# (2)如果前面数的累加加上当前数小于当前数，说明这次累加对总体的结果是无效的；如果前面数的累加加上当前数大于当前数，说明这次累加对结果是具有促进效果的，结果在考虑的范围内。
#
def find_sub(arr):
    # 定义两个变量，一个用来存放之前的累加值，一个用来存储当前的最大和
    max_sum = int(arr[0])  # 定义为第一个为最大
    pre_sum = 0
    list1 = []
    for i in arr:  # 遍历数组中的元素
        if pre_sum < 0:
            pre_sum = int(i)
            list1 = []  # 如果之前的累加和是小于0的则应该从当前值进行累加
        else:
            list1.append(i)
            pre_sum += int(i)
            if pre_sum< 0:
                list1.pop()
            # 如果是大于等于0的则需要将当前的数加到当前最大子数组中
        if pre_sum > max_sum:
            max_sum = pre_sum
            print(list1)
    return max_sum


def find_greatest_sub_array(array):
    """
    sum_of_array记录当前子组和，当子组合<0,则重置为0，重新开始计和
    greatest_sum记录目前出现过最大的子组和
    """
    if not array:
        return

    sum_of_array = 0
    greatest_sum = array[0]

    for number in array:
        sum_of_array += number

        if sum_of_array > greatest_sum:
            greatest_sum = sum_of_array

        if sum_of_array < 0:
            sum_of_array = 0

    return greatest_sum


if __name__ == '__main__':
    numbers = [6, -3, -2, 7, -15, 1, 2, 2]
    print(find_sub(numbers))
    # numbers = eval(input("请输入一个整数数组:"))
    # print(find_sub(numbers))
