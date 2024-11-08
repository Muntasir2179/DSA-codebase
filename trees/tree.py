
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def print_tree(root:TreeNode):
    if root == None:   # edge case
        return
    
    print(root.data)
    for subtree in root.children:   # base case is automatically handled by the loop
        print_tree(subtree)


def print_tree_detailed(root:TreeNode):
    if root == None:
        return
    
    print(f"{root.data}: ", end="")

    for each_child in root.children:
        print(each_child.data, end=",")
    
    print()
    
    for each_child in root.children:
        print_tree_detailed(each_child)


if __name__ == "__main__":
    root = TreeNode(1)

    root.children.append(TreeNode(2))
    root.children.append(TreeNode(3))
    root.children.append(TreeNode(4))

    # print(root.children[0].data)
    print_tree_detailed(root)

