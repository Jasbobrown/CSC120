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
    if not root:
        return
    print(root.val)
    pre_order_traversal_print(root.left)
    pre_order_traversal_print(root.right)


def in_order_traversal_print(root):
    if not root:
        return
    in_order_traversal_print(root.left)
    print(root.val)
    in_order_traversal_print(root.right)


def post_order_traversal_print(root):
    if not root:
        return
    post_order_traversal_print(root.left)
    post_order_traversal_print(root.right)
    print(root.val)


def in_order_vals(root):
    out, stack = [], []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out


def bst_max(root):
    if not root:
        return
    if not root.right:
        return root.val
    return bst_max(root.right)


def tree_max(root):
    stack = [root]
    max_val = root.val
    while stack:
        node = stack.pop()
        if node.val > max_val:
            max_val = node.val
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return max_val

