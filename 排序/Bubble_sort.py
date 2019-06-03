def bubble_sort(list):
    n = len(list)
    if n <= 1:
        return
    for i in range(0, n):  # 有没有-1 其实都能运行，就是运算量小一点
        for j in range(0, n - 1 - i):  # -j有没有一样 计算量的问题
            if list[j] <= list[j + 1]:
                pass
            else:
                list[j + 1], list[j] = list[j], list[j + 1]


if __name__ == '__main__':
    list = [1, 5, 7, 9, 4, 24, 43, 4, 4]
    print(list)
    bubble_sort(list)
    print(list)
