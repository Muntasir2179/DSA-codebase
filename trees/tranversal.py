from genericTreesInput import predefined_generic_tree_inputs

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def preorder_traversal(root:TreeNode):
    if root == None:
        return
    
    print(root.data, end=" ")
    for each_child in root.children:
        preorder_traversal(each_child)


def postorder_traversal(root:TreeNode):
    if root == None:
        return
    
    for each_child in root.children:
        postorder_traversal(each_child)
    print(root.data, end=" ")


if __name__ == "__main__":
    root1, root2, root3 = predefined_generic_tree_inputs()
    preorder_traversal(root1)
    print()
    postorder_traversal(root1)
    print()
