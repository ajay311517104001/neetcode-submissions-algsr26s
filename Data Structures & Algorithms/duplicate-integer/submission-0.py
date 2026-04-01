class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Naive approach
        #  traker = []
        # TC -> O(N^2) SC -> w.c 0(N) best case 0(1)
        # traker = []

        # optimization
        traker = {}
        #  iterate thru all the elements in the number
        for element in nums: # TC 0(N) SPACE(N)
        #  check if the current element is present in the traker
            if traker.get(element): # search, insert and delete an element in dict -> 0(1)
                #  if yes return true
                return True
                
            # if not add it to traker
            else:
                traker[element]=1
        return False
        # if all the values are iterated return false