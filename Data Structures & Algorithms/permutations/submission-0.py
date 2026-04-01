class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # to find the all permutations need to implement the tricky solution
        return self.helper(0 , nums)


    #TC->O(N^2) * n!
    # SC->O(n^2) * n!
    def helper(self, index , nums):
        # pass
        if index == len(nums):
            return [[]]


        perm = self.helper(index+1, nums)
        resPrem = []
        for p in perm:
            for j in range(len(p)+1):
                pc =p.copy()
                pc.insert(j,nums[index])
                resPrem.append(pc)
        return resPrem

                    


        