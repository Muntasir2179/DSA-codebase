

class QueueUsingList:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, data):
        self.__queue.append(data)
    
    def dequeue(self):
        if self.size() == 0:
            print("The queue is empty, cannot dequeue")
            return None
        return self.__queue.pop(0)
    
    def size(self):
        return len(self.__queue)
    
    def is_empty(self):
        return self.size() == 0
    
    def front(self):
        if self.size() == 0:
            print("The queue is empty, cannot show front")
            return None
        return self.__queue[0]


if __name__ == "__main__":
    queue = QueueUsingList()

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

