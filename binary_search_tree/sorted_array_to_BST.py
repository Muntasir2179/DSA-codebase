from predefinedBST import print_level_wise

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sorted_array_to_BST(arr:list):
    if len(arr) == 0:
        return None
    
    mid = len(arr) // 2
    root = BSTNode(arr[mid])
    root.left = sorted_array_to_BST(arr[:mid])
    root.right = sorted_array_to_BST(arr[mid+1:])

    return root


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    root = sorted_array_to_BST(arr)
    print_level_wise(root)
