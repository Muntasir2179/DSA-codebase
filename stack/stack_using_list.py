

class Stack:
    def __init__(self, list_elements:list=[]) -> None:
        self.__stack = list_elements   # very important to make it private
    
    def push(self, data):
        self.__stack.append(data)
        print(f"Pushed {data} into stack")
    
    def size(self):
        return len(self.__stack)

    def is_empty(self):
        return len(self.__stack) == 0
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop element")
            return None
        return self.__stack.pop()
    
    def top(self):
        if self.is_empty():
            print("Stack is empty, no top element")
            return None
        return self.__stack[-1]


if __name__ == "__main__":
    stack = Stack([1, 2, 3, 4, 5, 6])
    stack.pop()
    print(stack.is_empty())
    print(stack.size())
    stack.push(6)
    print(stack.size())

