from predefinedBST import predefined_BST_inputs


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# inorder traversal of BST
def print_bst(root:BSTNode):
    if root == None:
        return
    
    print_bst(root.left)
    print(root.data, end=" ")
    print_bst(root.right)


root1, root2, root3 = predefined_BST_inputs()
print_bst(root1)
print()
