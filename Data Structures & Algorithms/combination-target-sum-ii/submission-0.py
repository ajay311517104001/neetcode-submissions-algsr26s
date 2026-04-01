class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # coices : candidates
        # constrain: the sum of the subset should be the total
        # basecase: if the sum of subset matches add them to the subset or if the sum exceeds stop
        # backtrack: include / exclude


        # result choices (candidates)
        # call the dfs
        result = []
        subset =[]
        candidates.sort()



        def dfs(index , subset , total):
            # basecase
            if total == target:
                if subset not in result:
                    result.append(subset.copy())
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
            dfs(index+1 , subset , total)
            # call the dfs to add the next element






        dfs(0,subset, 0)
        return result