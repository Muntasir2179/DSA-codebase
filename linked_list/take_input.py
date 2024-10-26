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
    value = int(input("Enter the number for the node: "))
    head = None

    while value != -1:
        new_node = Node(value=value)
        if head == None:
            head = new_node
        else:
            # find the tail and insert the new node their
            temp = head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        
        value = int(input("Enter the number for the node: "))

    return head


list_head = take_input()

print_linked_list(list_head)


"""
Outer loop -> n
Inner loop -> n
Time complexity for linked list insertion: O(n^2)
"""