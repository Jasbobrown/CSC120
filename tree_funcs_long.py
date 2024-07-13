from list_node import ListNode

def bst_search_loop(root, val):
    cur = root
    while cur:
        if cur.val == val:
            return cur
        elif val < cur.val:
            cur = cur.left
        else:
            cur = cur.right
    return None

def tree_search(root, val):
    pass

def bst_insert_loop(root, val):
    pass

def pre_order_traversal_print(root):
    pass

def in_order_traversal_print(root):
    pass

def post_order_traversal_print(root):
    pass

def in_order_vals(root):
    pass

def bst_max(root):
    pass

def tree_max(root):
    pass

