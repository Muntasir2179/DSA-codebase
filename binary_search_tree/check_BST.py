from predefinedBST import predefined_BST_inputs

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_max(node:BSTNode):
    if node == None:
        return float("-inf")

    left_max = find_max(node.left)
    right_max = find_max(node.right)

    return max(left_max, right_max, node.data)


def find_min(node:BSTNode):
    if node == None:
        return float("inf")
    
    left_min = find_min(node.left)
    right_min = find_min(node.right)

    return min(left_min, right_min, node.data)


def check_BST(root:BSTNode):
    if root == None:
        return True   # base case: Empty tree is a BST
    
    left_max = find_max(root.left)
    right_min = find_min(root.right)

    left_BST = check_BST(root.left)
    right_BST = check_BST(root.right)

    ans = left_BST and right_BST and (left_max < root.data) and (right_min > root.data)
    return ans


def check_BST_range(root:BSTNode, minimum, maximum):
    if root == None:
        return True
    
    if root.data < minimum or root.data > maximum:
        return False

    ans_left = check_BST_range(root.left, minimum, root.data-1)
    ans_right = check_BST_range(root.right, root.data+1, maximum)

    return ans_left and ans_right


if __name__ == "__main__":
    root1, root2, root3 = predefined_BST_inputs()
    # print(check_BST(root3))
    print(check_BST_range(root3, float("-inf"), float("inf")))

    root4 = BSTNode(5)
    root4.left = BSTNode(10)
    root4.right = BSTNode(15)
    # print(check_BST(root4))
    print(check_BST_range(root4, float("-inf"), float("inf")))
