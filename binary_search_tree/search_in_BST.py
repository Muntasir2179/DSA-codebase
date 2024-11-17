from predefinedBST import predefined_BST_inputs


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search_bst(root:BSTNode, value):
    if root == None:
        return False
    
    if value < root.data:
        return search_bst(root.left, value)
    elif value > root.data:
        return search_bst(root.right, value)
    else:
        return True


if __name__ == "__main__":
    root1, root2, root3 = predefined_BST_inputs()
    print(search_bst(root3, 155))
