class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #  create an hashmap
        # update the hash map and check if it exits
        #  if exists return O(n) for space and O(n) for time
        

        # The intution is little tough to understand and basically it is easy
        #  floyd cycle detection and where the cycle is started

        # s,f = 0,0
        # while s!=f:
        #     s = nums[s]
        #     f = nums[nums[f]]
        # s2 = 0

        # while s!=s2:
        #     s = nums[s]
        #     s2=nums[s2]
        # return s2

        # The probelm wiht the previous apprach was the s and f initialized is 0 when the while starts basically it will never enter the loop
        # Inorder to inter the loop do a while loop or initilaize the s f to fist element of the array
             
                
        #  cycle detection algo garanteed that it takes O(n) to detect the cycle
        #  do while implementation
        s,f = 0,0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s==f:
                break
        s2 = 0

        #  cycle detection algo garanteed that it takes O(n) to find the element
        while True:
            s = nums[s]
            s2=nums[s2]
            if s == s2:
                break
        return s2
