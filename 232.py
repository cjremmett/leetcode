from collections import deque

class MyQueue:

    def __init__(self):
        self.d = deque()

    def push(self, x: int) -> None:
        dt = deque()
        for i in range(0, len(self.d)):
            dt.append(self.d.pop())

        self.d.append(x)
        for i in range(0, len(dt)):
            self.d.append(dt.pop())     

    def pop(self) -> int:
        return self.d.pop() if len(self.d) > 0 else None        

    def peek(self) -> int:
        return self.d[-1] if len(self.d) > 0 else None

    def empty(self) -> bool:
        return len(self.d) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()