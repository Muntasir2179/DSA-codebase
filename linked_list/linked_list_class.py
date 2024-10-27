
# defining node
class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next


# defining the linked list class
class LinkedList:
    def __init__(self):
        self.head = None
    

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self.head
    

    def insert_at_tail(self, data):
        temp = self.head
        
        if temp == None:
            return self.insert_at_head(data)

        new_node = Node(data)
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        return self.head
    

    def insert_at_index(self, data, index):
        # if index is zero then it is the head we have to insert
        if index == 0:
            return self.insert_at_head(data)
        
        new_node = Node(data)
        temp = self.head
        count = 0

        # getting to the position before where we have to insert the node
        while temp is not None and count < index - 1:
            temp = temp.next
            count += 1
        
        # when given index is out of bound the temp will contain None
        if temp == None:
            print("Index is out of bounds, please check index.")
            return self.head
        
        new_node.next = temp.next   # connecting the right list head to the new node
        temp.next = new_node   # connecting the left head list with the new node
        return self.head


    def search_value(self, data):
        if self.head == None:
            print("List is empty")
            return -1
        temp = self.head
        index = 0
        while temp != None:
            if temp.data == data:
                return index
            temp = temp.next
            index += 1
        return -1

    
    def delete_value(self, data):
        temp = self.head

        if self.head.data == data:  # checking for head
            self.head = self.head.next
            return True

        # get to the point before where we have to perform delete
        while temp.next != None:
            if temp.next.data == data:
                temp.next = temp.next.next
                return True
            temp = temp.next
        return False


    def print_ll(self):
        temp = self.head
        while temp != None:
            if temp.next == None:
                print(f"{temp.data}")
            else:
                print(f"{temp.data} -> ", end="")
            temp = temp.next


    def length_ll(self):
        length = 0
        temp = self.head
        while temp != None:
            length += 1
            temp = temp.next
        return length


if __name__ == "__main__":
    linked_list = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        linked_list.insert_at_tail(value)

    print(f"The length of LL: {linked_list.length_ll()}")
    # linked_list.insert_at_index(3, 4)
    # print(f"The value is no index: {linked_list.search_value(7)}")
    print(linked_list.delete_value(1))
    print()
    linked_list.print_ll()

