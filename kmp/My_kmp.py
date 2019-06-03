# def kmp(s,t,pnext):
#     i = j = 0
#     n = len(s)
#     m = len(t)
#     while j < n and i < m :
#         if i == -1 or t[j] == t[i]:
#             i += 1
#             j += 1
#         else:
#             i = pnext[i]
#     if i == m:
#         return  j - i
#     return -1
# def pnext_(p):
#     i = 0
#     k = -1
#     n = len(p)
#     pnext = [-1]*n
#     while i < n - 1 :
#         if k == -1 or p[i] == p[k]:
#             i += 1
#             k += 1
#             pnext[i] = k
#         else:
#             k = pnext[k]
#     return pnext


'''不巧，还真有，如果子串的第0个位置就
匹配失败了，怎么办呢？很明显，前面没有已匹配的
串，最长前缀的长度岂不是0？呵呵，要是你把next[0]=0，
你再代入上面的那个框架试试？很明显，陷入死循环了。再回
想原来的那个最暴力的算法，你会发现，那个算法匹配失败后是子
串的头部后挪一位，当然了程序中并没有挪的操作，准确来说是
m指针后移了一位，然后s指针还是指向子串的第0位。好的，为了编程
的方便，对之前的框架不做大的改动。把next[0]=-1好
了(因为if里面m、s都是同时自增的)。这样的话，判断
条件也要改一改，if s==-1 or mom_string[m]==son_string[0]:...也就
是说当s=-1的时候无条件都自增，这样不就
解决了嘛。然后如果子串的第1位匹配失
败了呢？它前面只有第0位的字符，这个串并没
有前缀（因为只有一个字符），next[1]=0。
'''


def my_kmp(s, t, pnext):
    i = j = 0
    n = len(s)
    m = len(t)
    while j < n and i < m:
        if i == -1 or s[j] == t[i]:
            i += 1
            j += 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1


def pnext_(p):
    i = 0
    k = -1
    n = len(p)
    pnext = [-1] * n
    while i < n - 1:
        if k == -1 or p[i] == p[k]:
            i += 1
            k += 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext


if __name__ == '__main__':
    s = 'adscaab'
    t = 'caab'
    print(my_kmp(s, t, pnext_(t)))
