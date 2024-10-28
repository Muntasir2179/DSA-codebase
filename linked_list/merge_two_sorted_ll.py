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
def merge_two_sorted_linked_list(head1, head2):
    # if any of the linked list is empty then other one is the answer
    if head1 == None:
        return head1
    if head2 == None:
        return head2
    
    # insert nodes into the final linked list till each of the linked list reaches none
    final_head = final_tail = None
    while head1 != None and head2 != None:
        if head1.data < head2.data:
            # when we inserting at the head
            if final_head == None:
                final_head = head1
                final_tail = head1
            else:
                # when we inserting at tail
                final_tail.next = head1
                final_tail = head1
            head1 = head1.next
        else:
            # when we inserting at the head
            if final_head == None:
                final_head = head2
                final_tail = head2
            else:
                # when we inserting at tail
                final_tail.next = head2
                final_tail = head2
            head2 = head2.next
    
    # if there are any list left then simply merge the left of the nodes to the final linked list
    if head1 != None:
        final_tail.next = head1
    if head2 != None:
        final_tail.next = head2
    return final_head
    


if __name__ == "__main__":
    linked_list_1_head = create_linked_list_from_list([1, 5])
    linked_list_2_head = create_linked_list_from_list([2])
    print_linked_list(linked_list_1_head)
    print_linked_list(linked_list_2_head)
    print_linked_list(merge_two_sorted_linked_list(linked_list_1_head, linked_list_2_head))
