from list_node import ListNode

def is_sorted(head):
    cur = head
    if not cur or not cur.next:
        return True
    while cur.next != None:
        if cur.next < cur:
            return False
    return True
    

def list_sum():
    pass

def partition_list():
    pass

def accordion_3():
    pass

def pair():
    pass
