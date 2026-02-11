class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = 2**31 - 1

    def push(self, val: int) -> None:
        if val <= self.minVal:              # remember to add \'euqals to\'
            self.stack.append(self.minVal)  # push the previous min value
            self.minVal = val               # update the min value
        self.stack.append(val)              # push the new val

    def pop(self) -> None:
        if self.stack.pop() == self.minVal: # when we pop the min val, 
            self.minVal = self.stack.pop()  # we pop the next(previous min value) of it as well and update the min value

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()