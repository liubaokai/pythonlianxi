class test:
    def __init__(self):
        self.pos = 0

    def partition(self, array, first, last):

        low = first
        high = last
        key = array[first]
        while low < high:
            while low < high and array[high] >= key:
                high -= 1  # 这个地方写错了因为没有换位置啊，少写了
            array[low] = array[high]  # 后来补上了
            while low < high and array[low] < key:
                low += 1
            array[high] = array[low]
        array[low] = key
        self.pos = low

    def get_mid(self, array):
        low = 0
        n = len(array)
        high = n - 1
        # mid = (low + high) // 2 # 这个可以换成第几小的数
        mid = 4
        while True:
            self.partition(array, low, high)
            if self.pos == mid:
                break
            elif self.pos > mid:
                high = self.pos - 1
            else:
                low = self.pos + 1

        if (n % 2) != 0:
            return array[mid]

        else:
            return (array[mid] + array[mid + 1]) / 2


def partition(array, first, last):
    if first > last:  # 区别在于没有等号 因为有等号时表示一个元素，快排里不用判断了 可是我们这个情况下是要取这个数的所以要用的
        return 'aa'
    low = first
    high = last
    key = array[first]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1  # 这个地方写错了因为没有换位置啊，少写了
        array[low] = array[high]  # 后来补上了
        while low < high and array[low] < key:
            low += 1
        array[high] = array[low]
    array[low] = key
    low_1 = 0
    n = len(array)

    high_1 = n - 1
    # mid = 1
    k = (low_1 + high_1) // 2 + 1  # 这个可以换成第几小的数
    index = low
    if index == k:
        return array[low]
    elif index > k:
        return partition(array, first, low - 1)
    else:
        return partition(array, low + 1, last)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]  # 一乱序就不对了

    print(test().get_mid(arr))
