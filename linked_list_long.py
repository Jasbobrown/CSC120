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
    return sum


def partition_list():
    pass

def accordion_3():
    pass

def pair():
    pass
