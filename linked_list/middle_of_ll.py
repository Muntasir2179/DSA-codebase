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


# function to find the middle of the linked list
def find_middle(head):
    temp = head
    length = 0
    while temp != None:
        length += 1
        temp = temp.next

    if length == 0:
        return None
    if length == 1:
        return head.data
    
    middle_index = length // 2
    temp = head
    while middle_index != 0:
        temp = temp.next
        middle_index -= 1
    
    return temp.data


# finding middle using two pointers
def find_middle_using_two_pointers(head):
    if head == None:
        return None
    
    fast = slow = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow.data


if __name__ == "__main__":
    list_head = take_input()
    print(f"Middle of the list is: {find_middle(list_head)}")
    print(f"Middle of the list is: {find_middle_using_two_pointers(list_head)}")
