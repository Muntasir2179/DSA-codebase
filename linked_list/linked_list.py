from copy import deepcopy


# defining node
class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

# recursive function to print linked list data
def print_linked_list(head: Node):
    if head is not None:
        print(head.data)
        print_linked_list(head.next)


# function for taking input
def take_input():
    """The time complexity is O(n)"""
    head = tail = None  # keeping the head and tail inline

    while True:
        value = int(input("Enter the number for the node: "))
        if value == -1:
            break
        new_node = Node(value=value)
        if head == None:
            head = tail = new_node
        else:
            # we have tail and we can easily insert new node their
            tail.next = new_node
            tail = new_node
    
    # return the linked list head
    return head


# function for finding the length of the linked list
def get_length(head:Node):
    """The time complexity is O(n)"""
    temp = head
    count = 0
    while temp != None:
        temp = temp.next
        count += 1
    return count


# recursive function for getting the length of the linked list
def get_length_recursively(head):
    """The time complexity is O(n)"""
    if head == None:  # base case
        return 0
    # current length + length of the forwarding nodes
    return 1 + get_length_recursively(head.next)


# function for inserting node into head
def insert_head(head, data):
    """The time complexity is O(1)"""
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head


# inserting at tail
def insert_tail(head, data):
    """The time complexity is O(n)"""
    temp = head
    new_node = Node(data)
    while temp.next != None:
        temp = temp.next
    temp.next = new_node
    return head


# recursive function for inserting data into tail
def insert_tail_recursively(head, data):
    """The time complexity is O(n)"""
    if head is None:  # base case
        return Node(data)

    # if head.next == None:
    #     head.next = Node(data)
    #     return head
    
    head.next = insert_tail_recursively(head.next, data)
    return head


# function for inserting node in specific index
def insert_at_index(head, data, index):
    # if index is zero then it is the head we have to insert
    if index == 0:
        return insert_head(head, data)
    
    new_node = Node(data)
    temp = head
    count = 0

    # getting to the position before where we have to insert the node
    while temp is not None and count < index - 1:
        temp = temp.next
        count += 1
    
    # when given index is out of bound the temp will contain None
    if temp == None:
        print("Index is out of bounds, please check index.")
        return head
    
    new_node.next = temp.next   # connecting the right list head to the new node
    temp.next = new_node   # connecting the left head list with the new node
    return head


# recursive function to insert node in a specific index
def insert_at_index_recursively(head, data, index):
    if index == 0:
        # when index reached to zero then we have to insert the node there
        return Node(value=data, next=head)
    
    if head == None:
        print("Index is out of bounds, please check index.")
        return head
    
    # decrementing index and making recursive call
    head.next = insert_at_index_recursively(head.next, data, index-1)
    return head


# function for deleting a specific node
def delete_at_index(head, index):
    """Time complexity of deletion is O(n)"""
    if head == None:   # when there is not element in the linked list
        print("No element to delete")
        return head
    
    if index == 0:   # when we have to delete the head element
        return head.next
        
    temp = head
    count = 0
    # get to the point before where we have to perform delete
    while count != index-1 and temp != None:
        temp = temp.next
        count += 1
    
    if temp == None or temp.next == None: # it means the index to delete is long after tail or just right after the tail, which is not valid index
        print("Index is out of bounds, please check index.")
    else:
        temp.next = temp.next.next  # just skip one node and point to the next after node
    return head


# function for deleting node at index recursively
def delete_at_index_recursively(head, index):
    """Time complexity of deletion is O(n)"""
    if head == None:  # when we have to delete the tail node
        print("Index is out of bounds, pleas check index.")
        return head
    
    if index == 0:  # when we have to delete the head node and when we reached at destination index
        return head.next
    
    head.next = delete_at_index_recursively(head.next, index-1)
    return head


# function to delete node by value using recursion
def delete_node_by_value_recursively(head, value):
    """Time complexity of deletion is O(n)"""
    if head == None:  # if the list is empty
        print("The list is empty.")
        return head
    if head.data == value:  # if we find the data
        return head.next
    if head.next == None:  # if we are at the last node and data is not found
        print("Value is not in the list.")
        return head
    
    head.next = delete_node_by_value_recursively(head.next, value)
    return head


# function for deleting tail recursively
def delete_tail_recursively(head):
    if head == None:
        return None
    if head.next == None:
        return None
    
    head.next = delete_tail_recursively(head.next)
    return head


# function for searching values in linked list
def search_value(head, data):
    """Time complexity of deletion is O(n)"""
    if head == None:
        print("List is empty")
        return -1
    temp = head
    index = 0
    while temp != None:
        if temp.data == data:
            return index
        temp = temp.next
        index += 1
    return -1


# function for searching value in linked list recursively
def search_value_recursively(head, data, index=0):
    """
    Time complexity of this function is O(n)
    This function changes the head. So, use deepcopy() to make a copy of the list head.
    """
    if head == None:
        return -1
    if head.data == data:
        return index
    return search_value_recursively(head.next, data, index+1)


if __name__ == "__main__":
    list_head = take_input()
    # list_head = insert_head(list_head, 100)
    # list_head = insert_tail_recursively(list_head, 200)
    # list_head = insert_at_index_recursively(list_head, 10, 2)
    # list_head = delete_at_index_recursively(list_head, 3)
    # list_head = delete_tail_recursively(list_head)
    # list_head = delete_node_by_value_recursively(list_head, 3)
    # index = search_value(list_head, 2)
    index = search_value_recursively(deepcopy(list_head), 3)
    print(index)
    print_linked_list(list_head)




"""
Delete a node --> We stop at a node before.
Insert a node --> We stop on the node where we insert
"""