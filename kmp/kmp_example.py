def KMP(t, p, pnext):
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1

def _pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext

def _pnext_2(p):
    n = len(p)
    i = 0
    k = -1
    pnext = [-1] * n
    while i < n-1:
        if k == -1 or p[i] == p[k]:
            i += 1
            k += 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return  pnext





if __name__ == '__main__':
    s = 'assdadcaab'
    t = 'caab'
    print(KMP(s, t, _pnext_2(t)))
