def iSloop(head):
    if head is None or head.next is None:
        return None
    slow = head.next
    fast = head.next.next
    while fast.next is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None


def meetnode(head, meetnode):
    first = head
    second = meetnode
    while first != second:
        first = first.next
        second = second.next
    return first
