class Solution:
    # Optimal solution
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L=0
        window = set()

        # [2,1,2], k = 1
        # set ={1,2}


        # ITERATE thru the element
        for R in range(len(nums)):
            # check if R exceeds K
            if R >k:
                # remove the L most elemnt from the set
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
                # increment the L
                # check if R exists in the set
                # return True
            window.add(nums[R])
                # add the elent to the set
        return False
        