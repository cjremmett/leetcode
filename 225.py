from collections import deque

class MyStack:

    def __init__(self):
        self.d = deque()
        
    def push(self, x: int) -> None:
        self.d.append(x)
        for i in range(0, len(self.d) - 1):
            self.d.append(self.d.popleft())

    def pop(self) -> int:
        return self.d.popleft()        

    def top(self) -> int:
        return self.d[0] if len(self.d) != 0 else None        

    def empty(self) -> bool:
        return True if len(self.d) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyStack()
    obj.push(5)
    obj.push(3)
    obj.push(1)
    print(obj.pop())
    print(obj.top())
    print(obj.empty())