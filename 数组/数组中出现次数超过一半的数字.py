def get_more_half_num(nums):
    hashes = dict()
    length = len(nums)
    for n in nums:
        if hashes.get(n):
            hashes[n] = hashes[n] + 1
        else:
            hashes[n] = 1

        if hashes[n] > length / 2:
            return n

def more_than(nums):
    nums = sorted(nums)
    length = len(nums)
    mid = int(length/2)
    if nums.count(nums[mid])>mid:
        return nums[mid]
    else:
        return o
