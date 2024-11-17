class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to return complex binary trees
def predefined_BST_inputs():
    # Tree 1: Basic BST with height 2
    root1 = BinaryTreeNode(10)
    root1.left = BinaryTreeNode(5)
    root1.right = BinaryTreeNode(15)
    
    # Tree 2: Slightly complex BST with height 3
    root2 = BinaryTreeNode(20)
    root2.left = BinaryTreeNode(10)
    root2.right = BinaryTreeNode(30)
    root2.left.left = BinaryTreeNode(5)
    root2.left.right = BinaryTreeNode(15)
    root2.right.left = BinaryTreeNode(25)
    root2.right.right = BinaryTreeNode(35)
    
    # Tree 3: More complex BST with height 4
    root3 = BinaryTreeNode(40)
    root3.left = BinaryTreeNode(20)
    root3.right = BinaryTreeNode(60)
    root3.left.left = BinaryTreeNode(10)
    root3.left.right = BinaryTreeNode(30)
    root3.right.left = BinaryTreeNode(50)
    root3.right.right = BinaryTreeNode(70)
    root3.left.left.left = BinaryTreeNode(5)
    root3.left.left.right = BinaryTreeNode(15)
    root3.left.right.left = BinaryTreeNode(25)
    root3.left.right.right = BinaryTreeNode(35)
    root3.right.left.right = BinaryTreeNode(55)
    root3.right.right.left = BinaryTreeNode(65)
    root3.right.right.right = BinaryTreeNode(75)

    return root1, root2, root3

# Getting predefined binary trees
root1, root2, root3 = predefined_BST_inputs()


class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


from collections import deque

def print_level_wise(root):
    if root is None:
        return
    
    queue = deque([root])  # Initialize the queue with the root node
    
    while queue:
        current_node = queue.popleft()  # Dequeue the front node
        print(f"{current_node.data}: ", end=" ")
        
        if current_node.left:
            print(f"L->{current_node.left.data}", end=", ")
            queue.append(current_node.left)  # Enqueue the left child
        else:
            print("L->None", end=", ")
        
        if current_node.right:
            print(f"R->{current_node.right.data}")
            queue.append(current_node.right)  # Enqueue the right child
        else:
            print("R->None")

# # Example usage to print the binary tree level-wise
# print("Level-Wise Printing of Binary Tree:")
# root1,root2,root3 = predefined_binary_tree_inputs()
# print_level_wise(root1)
