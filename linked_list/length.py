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


# function for finding the length of the linked list
def get_length(head:Node):
    temp = head
    count = 0
    while temp != None:
        temp = temp.next
        count += 1
    return count


# recursive function for getting the length of the linked list
def get_length_recursively(head):
    if head == None:  # base case
        return 0
    # current length + length of the forwarding nodes
    return 1 + get_length_recursively(head.next)



list_head = take_input()
print("Length of the linked list: ", get_length_recursively(head=list_head))
# print_linked_list(head=list_head)
