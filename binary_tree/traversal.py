from predefinedBT import predefined_binary_tree_inputs


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(root:BinaryTreeNode):
    if root == None:
        return
    
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def postorder_traversal(root:BinaryTreeNode):
    if root == None:
        return
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")


def inorder_traversal(root:BinaryTreeNode):
    if root == None:
        return
    
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)


def inorder_traversal_list(root:BinaryTreeNode, ans_list:list):
    if root == None:
        return ans_list
    
    inorder_traversal_list(root.left, ans_list)
    ans_list.append(root.data)
    inorder_traversal_list(root.right, ans_list)
    return ans_list


if __name__ == "__main__":
    root1, root2, root3 = predefined_binary_tree_inputs()
    # print(f"Preorder traversal: ", end="")
    # preorder_traversal(root1)
    # print()
    # print(f"Postorder traversal: ", end="")
    # postorder_traversal(root1)
    # print()
    # print(f"Inorder traversal: ", end="")
    # inorder_traversal(root1)
    # print()
    ans_list = inorder_traversal_list(root1, [])
    print(ans_list)
