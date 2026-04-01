class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # make the position and speed as tuple and sort them interms of position
        # [4,1,0,7], speed = [2,2,1,1]
        
        # for i in range(len(position)):
        #     speed[i] = (position[i],speed[i])
        # speed.sort()
        # print(speed)
        # # [(0,1)(1,2)(4,2)(7,1)]
        # # create an empty stack
        # stack=[]
        # #  iterate the tuple from last
        # time = (target - speed[-1][0])/speed[-1][1]
        # for i in range(len(position)-1,-1,-1):
        # #  if stack is empty 
        # # calaculate the time it will take to reach
        #     if not stack:
        #         stack.append(speed[i])
        # # time = target - curr position / speed
        #     elif time < (target - speed[i][0])/speed[i][1]:
        # #  if time < curr time:
        #     # add to stack
        #         stack.append(speed[i])
        #         time = (target - speed[i][0])/speed[i][1]
        # #  add the tuple to stack
        # return len(stack)
        
        #  The above logic has some issue in it - it always compares it with the car timings near to its target

        res = [(p,s) for p,s in zip(position, speed)]
        res.sort(reverse=True) # Descending order
        stack=[]
        for p,s in res:
            stack.append((target-p)/s) #stack[-1] keep track of the previous car
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

