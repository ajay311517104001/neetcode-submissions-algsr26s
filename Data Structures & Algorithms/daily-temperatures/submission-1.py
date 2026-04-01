class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #  array of integers - temp
        # temp[i] represents the daily temperature on the ith day
        # return a result array where result[i] is the number of days after ith day
        # brute force approach
        # [30,38,30,36,35,40,28]
        #      i           j
        # [22,21,20]
        #        i  j
        # Time complexity - O(n2) space complexity would be O(n)
        # result = [0]*(len(temperatures))
        # # iterate the elements in the array
        # for i in range(len(temperatures)):
        # #  iterate the j element
        #     count=1
        #     for j in range(i+1 , len(temperatures)):
        # # if j > i :
        #         if temperatures[j] > temperatures[i]:
        #     #     update the count in result array
        #             result[i]=count
        #             break
        #     #     reset the count
        #     # else:
        #         else:
        #             count+=1
         
        # #    count+=1
        # return result

        # Two pointer approach
        # L to start and R to 
        # For loop O(n2)- same previous implementation
        #  while R >l
        #  count
        #  update the count


        # Stack approch
        # result array
        result = [0]* len(temperatures)
        stack =[]
        # [30,38,30,36,35,40,28]
        #                  i
        # [(40,5),(28,6)]
        # [1,4,1,2,1,0,0]
        # New pattern we gonna attempt now
        # Monotonic increasing stack
        # iterate the elment with index
        for i in range(len(temperatures)):
        # push element in the stack if it is empty with the index
            # if not stack  or  stack[-1][0] > temperatures[i]:
            #     stack.append((temperatures[i] , i))
        # else check the current value with the top element in stack
            # else:
        #  while if it is greater
            while stack and stack[-1][0] < temperatures[i]:
        #  take the stack element index as result and insert curr index - stack index
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i] , i))
                
        #  explore the stack till 
        return result
        # return the result array
        
        

