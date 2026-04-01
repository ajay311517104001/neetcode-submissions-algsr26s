class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxi = 0 
        for r in range(1, len(prices)):
            while prices[r] - prices[l] < 0:
                l+=1
            else:
                maxi = max(maxi, prices[r] - prices[l])
        return maxi
