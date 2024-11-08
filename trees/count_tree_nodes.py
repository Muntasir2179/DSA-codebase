from genericTreesInput import predefined_generic_tree_inputs


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def count_nodes(root:TreeNode):
    if root == None:
        return 0
    
    number_of_nodes = 1
    for child in root.children:
        number_of_nodes += count_nodes(child)
    
    return number_of_nodes


def count_height(root:TreeNode):
    if root == None:
        return 0
    
    height = 1
    max_height = 0
    for each_sub_tree in root.children:
        max_height = max(max_height, count_height(each_sub_tree))

    return height + max_height


root1, root2, root3 = predefined_generic_tree_inputs()
# print(count_nodes(root1))
# print(count_nodes(root2))
# print(count_nodes(root3))

print(count_height(root1))
print(count_height(root2))
print(count_height(root3))
