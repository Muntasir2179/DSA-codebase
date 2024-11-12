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


def diameter(root:BinaryTreeNode):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)

    return max(left_diameter, right_diameter, left_height + right_height)


def diameter_optimized(root:BinaryTreeNode):
    if root == None:
        return 0, 0   # height and diameter
    
    left_height, left_diameter = diameter_optimized(root.left)
    right_height, right_diameter = diameter_optimized(root.right)

    diameter_through_root = left_height + right_height

    ans_diameter = max(diameter_through_root, left_diameter, right_diameter)
    current_tree_height = 1 + max(left_height, right_height)

    return current_tree_height, ans_diameter

if __name__ == "__main__":
    root1, root2, root3 = predefined_binary_tree_inputs()
    print(diameter_optimized(root2))
    # print(diameter(root3))
