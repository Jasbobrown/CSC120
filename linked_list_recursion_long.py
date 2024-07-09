# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

#     def __str__(self):
#         vals = []
#         objs = set()
#         curr = self
#         while curr is not None:
#             curr_str = str(curr.val)
#             if curr in objs:
#                 vals.append("{} -> ... (to infinity and beyond)".format(curr_str))
#                 break
#             else:
#                 vals.append(curr_str)
#                 objs.add(curr)
#             curr = curr.next

#         return " -> ".join(vals)


def array_to_list_recursive(data):
    if not data:
        return None
    if len(data) == 1:
        return ListNode(data[0])
    out = ListNode(data[0])
    out.next = array_to_list_recursive(data[1:])
    return out

def accordian_recursive(head):
    if not head or not head.next:
        return None
    head = head.next
    head.next = accordian_recursive(head.next)
    return head

def pair_recursive(head1, head2):
    if not head1 or not head2:
        return None
    if not head1.next or not head2.next:
        return ListNode((head1.val, head2.val))
    out = ListNode((head1.val, head2.val))
    out.next = pair_recursive(head1.next, head2.next)
    return out
