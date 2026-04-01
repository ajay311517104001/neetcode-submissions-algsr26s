class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #  Brute force solution
        #  To try all possible combination we need sum all possible elements from the array
        # [1,2,3,4]
        #      i j
        for i in range(0,len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
