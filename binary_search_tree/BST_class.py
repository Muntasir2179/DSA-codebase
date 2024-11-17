from collections import deque


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root:BSTNode = None

    def insert(self, data):
        self.root = self.insert_helper(self.root, data)

    # helper function 
    def insert_helper(self, node:BSTNode, data):
        if node == None:
            return BSTNode(data)
        
        if data < node.data:
            node.left = self.insert_helper(node.left, data)
        else:
            node.right = self.insert_helper(node.right, data)
        return node

    # main search function
    def search(self, data):
        return self.search_helper(self.root, data)

    # helper function for searching element in the BST
    def search_helper(self, root:BSTNode, data):
        if root == None:
            return False
        
        if root.data == data:
            return True
        
        if data < root.data:
            return self.search_helper(root.left, data)
        else:
            return self.search_helper(root.right, data)

    # main delete function
    def delete(self, data):
        self.delete_helper(self.root, data)

    # function for finding min value from right subtree
    def find_min(root:BSTNode):
        current_node = root
        while current_node.left != None:
            current_node = current_node.left
        return current_node

    # helper function for deleting a node from a BST
    def delete_helper(self, root:BSTNode, data):
        if root == None:
            return None
        
        if data < root.data:
            root.left = self.delete_helper(root.left, data)
        elif data > root.data:
            root.right = self.delete_helper(root.right, data)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                min_of_right = self.find_min(root.right)
                root.data = min_of_right.data
                root.right = self.delete_helper(root.right, min_of_right.data)
        return root

    def print_level_wise(self):
        if self.root is None:
            return
        
        queue = deque([self.root])  # Initialize the queue with the root node
        
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


if __name__ == "__main__":
    bst = BST()

    bst.insert(20)
    bst.insert(25)
    bst.insert(10)
    bst.insert(15)
    bst.print_level_wise()
    print()

    # print(bst.search(115))
    bst.delete(15)
    bst.print_level_wise()

