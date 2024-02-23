class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        a = self.q.pop()
        self.q.append(a)
        return a

    def empty(self) -> bool:
        return len(self.q) == 0