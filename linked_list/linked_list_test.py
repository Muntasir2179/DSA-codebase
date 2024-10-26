

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

first = Node(1)
second = Node(2)
third = Node(3)

head = first
first.next = second
second.next = third

del first
del second
del third

# recursive function to print linked list data
def print_linked_list(head: Node):
    if head is not None:
        print(head.data)
        print_linked_list(head.next)


print_linked_list(head)
print(head.data)
