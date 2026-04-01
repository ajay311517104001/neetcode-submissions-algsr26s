class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # coices : candidates
        # constrain: the sum of the subset should be the total
        # basecase: if the sum of subset matches add them to the subset or if the sum exceeds stop
        # backtrack: include / exclude


        # Time Complexity-> O(k.2^n.c)
        #  the depth goes till we find the target , which is the combination of total number of elements in candidates
        # for each candidates we make 2 choices along with the combination of n elements so 2^n and k is the time required to copy the subset elements
        # c is the time taken to search the elements in the candidate to find any duplicates
        # axuliary Complexity-> O(N) , where n is the height of the decision tree until we find the target
        # total space -> O(N) + 0(R.k) R is the number of valid subsets with each k elements in it
        # k is the number of elements in the subset
        # c is the result space to store all possible combination
        # n is the number of elements in the candidates



        # result choices (candidates)
        # call the dfs
        result = []
        subset =[]

        candidates.sort()


        def dfs(index , subset , total):
            # basecase
            if total == target:
                # if subset not in result: #O(n)
                result.append(subset.copy()) #O(k)
                return
            if total>target or index > len(candidates)-1:
                return 
            # constratin

            # backtracking
            # append the incoming index
            
            subset.append(candidates[index])
            # increment the index and share it to dfs (it returns only when we met the target or we are over the target)
            dfs(index+1 , subset , total+candidates[index])
            # pop the last
            subset.pop()
            # if the next element is same as the current element skip the element
            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index+=1
            dfs(index+1 , subset , total)
            # call the dfs to add the next element

        dfs(0,subset, 0)
        return result