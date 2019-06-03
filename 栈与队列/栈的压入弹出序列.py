def pop_order(push_stock, pop_stock):
    if not push_stock or not pop_order:
        return False
    stack = []
    while pop_stock:
        pop_val = push_stock[0]
        if stack and stack[-1] == pop_val:
            stack.pop()
            pop_stock.pop(0)
        else:
            while push_stock:
                if push_stock[0] != pop_val:
                    stack.append(push_stock.pop(0))
                else:
                    push_stock.pop(0)
                    pop_stock.pop(0)
                    break
        if not push_stock:
            while stack:
                if stack.pop() != pop_stock.pop(0):
                    return False
    if not pop_stock:
        return True
    return False


class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        for v in pushV:
            stack.append(v)
            while stack and stack[-1] == popV[0]:
                popV.pop(0)
                stack.pop()
        if len(stack):
            return False
        return True
