from tree_node import TreeNode

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
    if not root:
        return None
    if root.val == val:
        return root
    L = tree_search(root.left, val)
    if L:
        return L
    return tree_search(root.right, val)
    

def bst_insert_loop(root, val):
    cur = root
    while True:
        if val < cur.val:
            if not cur.left:
                cur.left = TreeNode(val)
                break
            cur = cur.left
        else:
            if not cur.right:
                cur.right = TreeNode(val)
                break
            cur = cur.right


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

