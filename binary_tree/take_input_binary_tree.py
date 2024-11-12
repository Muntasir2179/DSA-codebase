from collections import deque


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


def take_input_binary_tree():
    data = int(input("Enter the data for the node: "))
    if data == -1:
        return None
    
    node = BinaryTreeNode(data)

    print(f"\nEnter the left child of {node.data}")
    node.left = take_input_binary_tree()

    print(f"\nEnter the right child of {node.data}")
    node.right = take_input_binary_tree()
    return node


def take_input_level_wise():
    data = int(input("Enter the data for the node: "))
    if data == -1:
        return None
    
    root = BinaryTreeNode(data)
    queue = deque([root])

    while len(queue) != 0:
        current_node = queue.popleft()
        left_child_data = int(input(f"Enter left child for {current_node.data}: "))
        if left_child_data != -1:
            left_node = BinaryTreeNode(left_child_data)
            current_node.left = left_node
            queue.append(left_node)

        right_child_data = int(input(f"Enter right child for {current_node.data}: "))
        if right_child_data != -1:
            right_node = BinaryTreeNode(right_child_data)
            current_node.right = right_node
            queue.append(right_node)
    
    return root


def print_binary_tree_level_wise(root:BinaryTreeNode):
    if root == None:
        return

    queue = deque([root])

    while len(queue) != 0:
        current_node = queue.popleft()
        print(f"{current_node.data}:", end=" ")

        if current_node.left != None:
            print(f"L->{current_node.left.data}, ", end="")
            queue.append(current_node.left)
        else:
            print(f"L->None, ", end="")

        if current_node.right != None:
            print(f"R->{current_node.right.data}")
            queue.append(current_node.right)
        else:
            print("R->None")


if __name__ == "__main__":
    print("Enter the binary tree data (-1 for No node):")
    # root = take_input_binary_tree()
    root = take_input_level_wise()
    print()
    print_binary_tree_level_wise(root)
    # print_binary_tree(root)
