def merge(head1, head2):
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    cur1 = head1.next
    cur2 = head2.next
    head = None
    cur = None
    if cur1.val <= cur2.val:
        head.next = cur1
        cur = cur1
        cur1 = cur1.next
    else:
        head.next = cur2
        cur = cur2
        cur2 = cur2.next
    while cur1.next is not None and cur2.next is not None:
        if cur1.val <= cur2.val:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur.next
            cur2 = cur2.next
    if cur1 is not None:
        cur.next = cur1
    if cur2 is not None:
        cur.next = cur2
    return head
