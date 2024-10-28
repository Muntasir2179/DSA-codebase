# defining node
class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next


# function for creating linked list from list
def create_linked_list_from_list(list: list):
    if len(list) == 0:
        return None

    head = tail = None
    for i, item in enumerate(list):
        if i == 0:
            head = tail = Node(item)
        else:
            new_node = Node(item)
            tail.next = new_node
            tail = new_node
    return head


# recursive function to print linked list data
def print_linked_list(head: Node):
    if head == None:
        return
    elif head.next == None:
        print(f"{head.data}")
    else:
        print(f"{head.data} -> ", end="")
        print_linked_list(head.next)


# function for merging two sorted linked list
def reverse_linked_list(head):
    if head == None or head.next == None:
        return head
    
    flag = True
    temp = head
    reversed_linked_list_head = None

    while temp != None:
        current_node = temp
        temp = temp.next
        
        if flag:
            reversed_linked_list_head = current_node
            current_node.next = None
            flag = False
        else:
            current_node.next = reversed_linked_list_head
            reversed_linked_list_head = current_node

    return reversed_linked_list_head


# function for merging two sorted linked list
def reverse_linked_list_optimized(head):
    if head == None or head.next == None:
        return head
    
    prev = None
    current = head

    while current != None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


if __name__ == "__main__":
    linked_list_head = create_linked_list_from_list([1, 2, 3, 4, 5])
    print_linked_list(linked_list_head)
    linked_list_head = reverse_linked_list_optimized(linked_list_head)
    print_linked_list(linked_list_head)
