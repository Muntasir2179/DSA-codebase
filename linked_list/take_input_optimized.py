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


list_head = take_input()
print_linked_list(list_head)


"""
Outer loop -> n
Inner loop -> 1
Time complexity for linked list insertion: O(n)

Note: By introducing a new variable tail we can reduce the time complexity from O(n^2) -> O(n)
"""