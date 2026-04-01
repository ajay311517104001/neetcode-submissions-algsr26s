class MinStack:

    def __init__(self):
        #  intialize the stack object
        self.stack = []
        #  i can have a sorted array means the stack can return the last element

        #  we can iterate the stack and check the minimum
       
        

    def push(self, val: int) -> None:
        #  push the element val onto the stack
        self.stack.append(val)
        

    def pop(self) -> None:
        # Should throw error if it stack is empty
        # else remove the element from the stack
        self.stack.pop()
        

    def top(self) -> int:
        # return the top element of the stack if it is not empty
        return self.stack[-1]

        

    def getMin(self) -> int:
        #  it retrives the minimum element in the stack
        self.mini = self.stack[0]
        for i in self.stack[1:]:
            if i <  self.mini:
                self.mini = i

        return self.mini

