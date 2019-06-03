def compare(str1, str2):
    result = True
    bCount = [0] *256
    i = 0
    while i < len(str1):
        bCount[ord(str1[i]) - ord('0')] += 1
        i += 1
    j = 0
    while j < len(str2):
        bCount[ord(str2[j]) - ord('0')] -= 1
        j += 1
    i = 0
    while i < 256:
        if bCount[i] != 0:
            result = False
            break
        i += 1
    return  result