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
        result = [0]*(len(temperatures))
        # iterate the elements in the array
        for i in range(len(temperatures)):
        #  iterate the j element
            count=1
            for j in range(i+1 , len(temperatures)):
        # if j > i :
                if temperatures[j] > temperatures[i]:
            #     update the count in result array
                    result[i]=count
                    break
            #     reset the count
            # else:
                else:
                    count+=1
         
        #    count+=1
        return result
