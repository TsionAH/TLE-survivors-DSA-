class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min_stack :
            value = min(self.min_stack[-1], value)
        
        self.min_stack.append(value)

    def pop(self) -> None:
        if not self.stack or not self.min_stack :
            print("the stack is empty")
        else:
            self.min_stack.pop()
            self.stack.pop()
        

    def top(self) -> int:
        if not self.stack :

            print(f"is empty")
        else:

            return self.stack[-1]

    def getMin(self) -> int:
        
        if not self.min_stack :

            print(f"is empty")
        else:

            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()