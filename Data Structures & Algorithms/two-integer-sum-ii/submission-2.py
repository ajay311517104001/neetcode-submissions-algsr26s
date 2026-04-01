class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #  Brute force solution
        #  To try all possible combination we need sum all possible elements from the array
        # [1,2,3,4]
        #      i j
        # TC -O(n2) SC - O(1)
        # for i in range(0,len(numbers)-1):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]

        # Optimal solution
        #  How it can be done in O(1)?
        # Since the array is sorted, How i can use try using hashmap or two pointers or both

        #[1,2,3,4]
        # i j
        # 1+4 = 5 > 3
        # 1+3 = 4 > 3
        # 1+2 = 3 == 3 return the index+1 since it is 1-indexed
        i=0
        j = len(numbers)-1
        while i < j :
            if numbers[i]+numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j] > target:
                j-=1
            else: 
                i+=1
