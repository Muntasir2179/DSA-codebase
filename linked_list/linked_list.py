# defining node
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

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


list_head = take_input()
# list_head = insert_head(list_head, 100)
list_head = insert_tail_recursively(list_head, 200)

print_linked_list(list_head)
