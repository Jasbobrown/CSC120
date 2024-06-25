from list_node import ListNode

def is_sorted(head):
    cur = head
    if not cur or not cur.next:
        return True
    while cur.next != None:
        if cur.next.val < cur.val:
            return False
        cur = cur.next
    return True
    

def list_sum(head):
    cur = head
    sum = 0
    if not cur:
        return sum
    if not cur.next:
        return sum + cur.val
    while cur.next != None:
        sum += cur.val
        cur = cur.next
    return sum + cur.val

def partition_list(head):
    cur = head
    cur2 = head.next
    if not cur or cur.next:
        return
    while cur.next != None:
        cur.next = cur.next.next
        cur2.next = cur2.next.next
        cur = cur.next
    return cur, cur2


def accordion_3():
    pass

def pair():
    pass
