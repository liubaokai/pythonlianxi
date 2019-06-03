def isOutStack(push,pop):
    if push is None or pop is None:
        return Fasle
    pushlen = len(push)
    poplen = len(pop)
    if pushlen != poplen:
        return False
    pushIndex = popIndex = 0
    stack = Stack
    while pushIndex < pushlen:
        stack.push(push[pushIndex]
        pushIndex += 1
        while (not push.empty()) and stack.peek() == pop[popIndex]:
            stack.pop()
            popIndex += 1
    return stack.empty() and popIndex == poplen