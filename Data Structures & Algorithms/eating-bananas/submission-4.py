import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #   [1,4,3,2]
        # 1  1,4,3,2 -> 10
        # 2  1 2 2 1 -> 6
        # 3  1 2 1 1 -> 5
        # 4  1 1 2 1 -> 
        # h=9
        # k=1
        # while True:
        #     total_hours=0
        #     for i in piles:
        #        total_hours+= math.ceil(i/k) 
        #     if total_hours <= h:
        #         return k
        #     else:
        #         k+=1

        # method
        def isMinimum(mid):
        #  check if the mid makes the min < h 
            total =0
            for i in piles:
                total+= math.ceil(i/mid)
            if total <= h:
                return 1
            else:
                return -1
        #  return 1
        # else return 0


        # pattern is binray search range
        #  find the lower bound
        
        # [1,4,3,2], h = 9
        # min = 2
        # max = 4
        # 3
        l = 1
        #  find the uppper bound
        r = max(piles)
        # while True
        res = 0
        while l<=r:
        # find the mid value = (upper bound + lower bound) /2
            mid = (l+r)//2
        # check if the mid value is the min 
            if isMinimum(mid) > 0:
                # if isMinimum(mid-1) < 0:
                #     return mid
        #  if yes check the previous value it sholud return false -> return the min
        #  else: r = mid -1
                # else: 
                res = mid
                r = mid -1

        #  check if the mid value is false
            elif isMinimum(mid) < 0 :
                l = mid+1
        #  left = mid +1
        # return mid
        return res

        