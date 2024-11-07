
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class QueueUsingLinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__length = 0
    
    def enqueue(self, data):
        new_node = Node(data)
        self.__length += 1
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
    
    def front(self):
        if self.__length == 0:
            print("The queue is empty, cannot show front")
            return None
        return self.__head.data
    
    def dequeue(self):
        if self.__length == 0:
            print("The queue is empty, cannot dequeue")
            return None
        
        element = self.__head.data
        self.__head = self.__head.next
        self.__length -= 1

        if self.__head == None:
            self.__tail = None
        return element
    
    def size(self):
        return self.__length
    
    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":
    queue = QueueUsingLinkedList()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Size of the queue after enqueue: {queue.size()}")
    print(f"Is the queue is empty or not: {queue.is_empty()}")
    print(f"The front of the queue: {queue.front()}")
    queue.dequeue()
    queue.dequeue()
    print(f"The front of the queue: {queue.front()}")
    print(f"Size of the queue after dequeue: {queue.size()}")
