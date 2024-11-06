
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackUsingLinkedList:
    def __init__(self):
        self.__head = None
        self.__length = 0

    def push(self, data):
        new_node = Node(data)
        if self.__head == None:
            self.__head = new_node
        
        new_node.next = self.__head
        self.__head = new_node
        self.__length += 1
    
    def pop(self):
        if self.__head == None:
            return None
        data = self.__head.data
        self.__head = self.__head.next
        self.__length -= 1
        return data
    
    def top(self):
        return self.__head.data if self.__length != 0 else None
    
    def size(self):
        return self.__length
    
    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":
    stack = StackUsingLinkedList()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(f"After push size of the stack is: {stack.size()}")
    print(f"Top of the stack is: {stack.top()}")
    stack.pop()
    stack.pop()
    print(f"After pop size of the stack is: {stack.size()}")
    stack.pop()
    stack.pop()
    stack.pop()
    print(f"After pop all elements size of the stack is: {stack.size()}")
    print(f"If stack is empty or not: {stack.is_empty()}")
    print(f"Top of the stack is: {stack.top()}")
