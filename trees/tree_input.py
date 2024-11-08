from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def print_tree_detailed(root:TreeNode):
    if root == None:
        return
    
    print(f"{root.data}: ", end="")

    for each_child in root.children:
        print(each_child.data, end=",")
    
    print()
    
    for each_child in root.children:
        print_tree_detailed(each_child)


def take_input():
    data = int(input("Enter the data for the node: "))
    node = TreeNode(data)

    num_children = int(input(f"Enter the number of children for {data}: "))

    for _ in range(num_children):
        child = take_input()
        node.children.append(child)
    
    return node


def take_input_level_wise():
    data = int(input("Enter the root data: "))
    root = TreeNode(data)

    queue = deque([root])

    while len(queue) != 0:
        current_node = queue.popleft()
        num_children = int(input(f"Enter the number of children for {current_node.data}: "))

        for i in range(num_children):
            child_data = int(input(f"Enter the data for {i+1} child of {current_node.data}: "))
            child_node = TreeNode(child_data)
            current_node.children.append(child_node)
            queue.append(child_node)
    
    return root


root = take_input_level_wise()
print_tree_detailed(root)
