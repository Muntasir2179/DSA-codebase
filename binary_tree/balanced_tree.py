from predefinedBT import predefined_binary_tree_inputs


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root:BinaryTreeNode):
    if root == None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


def check_balance_height(root:BinaryTreeNode):
    if root == None:
        return True, 0
    
    left_balanced, left_height = check_balance_height(root.left)
    right_balanced, right_height = check_balance_height(root.right)

    current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
    current_height = 1 + max(left_height, right_height)

    return current_balanced, current_height


if __name__ == "__main__":
    root1, root2, root3 = predefined_binary_tree_inputs()
    balanced, _ = check_balance_height(root2)
    print(balanced)

