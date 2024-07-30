import time

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def shallow_word(tree, letter):
    def _shallow_word(tree, letter):
        if not tree:
            return None
        
        if tree.value.startswith(letter):
            return (0, tree.value)
        
        left_result = _shallow_word(tree.left, letter)
        right_result = _shallow_word(tree.right, letter)
        
        if left_result and right_result:
            if left_result[0] <= right_result[0]:
                return (left_result[0] + 1, left_result[1])
            else:
                return (right_result[0] + 1, right_result[1])
        elif left_result:
            return (left_result[0] + 1, left_result[1])
        elif right_result:
            return (right_result[0] + 1, right_result[1])
        else:
            return None
        
    result = _shallow_word(tree, letter)
    return result[1] if result else None
            
            
if __name__ == "__main__":
    root = TreeNode("root")
    left = TreeNode("apple")
    right = TreeNode("banana")
    left_left = TreeNode("cherry")
    left_right = TreeNode("apricot")
    right_left = TreeNode("blueberry")
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    right.left = right_left

    letter = "a"
    result = shallow_word(root, letter)
    print(result)  # Output: 'apple'


start = time.time()




end = time.time()
print(f"Elapsed Time: {end-start} seconds")