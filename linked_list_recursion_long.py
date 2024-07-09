from list_node import ListNode #e

def array_to_list_recursive(data):
    if not data:
        return None
    if len(data) == 1:
        return ListNode(data[0])
    out = ListNode(data[0])
    out.next = array_to_list_recursive(data[1:])
    return out

def accordion_recursive(head):
    if not head or not head.next:
        return None
    head = head.next
    head.next = accordion_recursive(head.next)
    return head

def pair_recursive(head1, head2):
    if not head1 or not head2:
        return None
    if not head1.next or not head2.next:
        return ListNode((head1.val, head2.val))
    out = ListNode((head1.val, head2.val))
    out.next = pair_recursive(head1.next, head2.next)
    return out
