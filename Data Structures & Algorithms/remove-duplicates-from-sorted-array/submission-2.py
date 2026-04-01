class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums)) # to handle negative elements we are sorting and to remove duplicates we are using set
        #  set doesn't garentee its order. it remove duplicates and when it return i doesn't maintain any order
        print(unique)
        nums[:len(unique)] = unique
        return len(unique)
   
        