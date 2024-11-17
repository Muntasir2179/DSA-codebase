from predefinedBST import predefined_BST_inputs


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_in_range(root:BSTNode, low, high):
    if root == None:
        return
    
    if root.data > low:
        print_in_range(root.left, low, high)
    
    if low <= root.data <= high:
        print(root.data, end=" ")
    
    if high > root.data:
        print_in_range(root.right, low, high)


if __name__ == "__main__":
    root1, root2, root3 = predefined_BST_inputs()
    print_in_range(root3, 25, 50)
    print()
