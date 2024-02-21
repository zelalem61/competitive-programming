class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

        

    def top(self) -> int:
        n = len(self.stack)
        return self.stack[n-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your self.MinStack object will be instantiated and called as such:
# obj = self.MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()