from predefinedBT import predefined_binary_tree_inputs

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_binary_tree(root:BinaryTreeNode):
    if root == None:  # base case
        return None
    
    print(f"{root.data}:", end=" ")
    if root.left != None:
        print(f"L->{root.left.data}", end=", ")
    else:
        print(f"L->None", end=", ")
    
    if root.right != None:
        print(f"R->{root.right.data}")
    else:
        print(f"R->None")
    
    print_binary_tree(root.left)
    print_binary_tree(root.right)


# root = BinaryTreeNode(1)
# root.left = BinaryTreeNode(2)
# root.right = BinaryTreeNode(3)
# root.left.left = BinaryTreeNode(4)
# root.right.right = BinaryTreeNode(5)

root1, root2, root3 = predefined_binary_tree_inputs()
print_binary_tree(root1)
