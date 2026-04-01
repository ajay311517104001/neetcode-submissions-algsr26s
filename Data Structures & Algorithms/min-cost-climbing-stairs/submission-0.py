class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        cost.append(0)
        for i in range(len(cost) - 3 , -1 ,-1):
            cost[i]+= min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
        
        # i =0
        # l = len(cost)
        # total_cost = 0
        # while i < len(cost):
        #     total_cost+= cost[i]
        #     left = l -i
        #     if left >=2:
        #         i+=2
        #     else:
        #         i+=1
        # return total_cost
                

