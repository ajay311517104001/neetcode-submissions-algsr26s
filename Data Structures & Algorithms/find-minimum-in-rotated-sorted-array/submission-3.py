class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        golbal_min = float('+inf')
        while l<= r:
            m = (l+r)//2 
            if nums[l] <= nums[m]:
                golbal_min = min(golbal_min , nums[l])
                l+=1
            elif nums[m] <= nums[r]:
                golbal_min = min(nums[m] , golbal_min)
                r-=1
        return golbal_min if golbal_min != float('+inf') else 0
        