class MinStack:

    def __init__(self):
        #  intialize the stack object
        self.stack = []
        # self.minStack=[]
        

        #  we can iterate the stack and check the minimum
        #  while we push elements to the stack we push the minimum to the
        #  another stack
        #    using only one stack and having encoded values
        self.mini = 0

        

    def push(self, val: int) -> None:
        #  push the element val onto the stack
        #  if the stack is empty whatever the first value is minimum
        # else peek the top of the minstack and compare with the incoming  value and update the minstack
        # if self.minStack == []:
        #     self.minStack.append(val)
        # else:
        #     if val < self.minStack[-1]:
        #         self.minStack.append(val)
        #     else:
        #         self.minStack.append(self.minStack[-1])
        # self.stack.append(val)

        if self.stack ==[]:
            self.stack.append(0)
            self.mini = val
        else:
            res = val - self.mini
            if res <0:
                self.mini = val
            self.stack.append(res)
            


        

    def pop(self) -> None:
        # Should throw error if it stack is empty
        # else remove the element from the stack
        # self.stack.pop()
        # self.minStack.pop()

        ele = self.stack.pop()
        if ele < 0:
            self.mini = self.mini - ele


        

    def top(self) -> int:
        # return the top element of the stack if it is not empty
        # return self.stack[-1]
        if self.stack[-1] < 0:
            return self.mini
        else:
            return self.stack[-1] + self.mini

        

    def getMin(self) -> int:
        #  it retrives the minimum element in the stack this runs in O(n) the solution they required is O(1)
        # self.mini = self.stack[0]
        # for i in self.stack[1:]:
        #     if i <  self.mini:
        #         self.mini = i

        # return self.minStack[-1]
        return self.mini

        # created some extra space for another stack to keep track of the minimum elements

