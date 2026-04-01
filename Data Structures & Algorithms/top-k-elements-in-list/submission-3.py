class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  i can return the output in any order
        # need to find the top K frequent elements
        #  k - number of frequent elements
       
        #  [1,2,3,4]

        # Brute force approach 
        #  result =[] - K elements - space - O(n) , tc -O(nlogn)
         # [1,2,2,3,3,3, 4,4,4,4] k = 2
        """ hashmap = {1:3 ,2:2 , 3:1 }"""
        """ result = [[3,1] , [2,2] , [1,3]]"""
        """ sort = [[1,3] , [2,2] , [3,1]]"""
        """ """
        hmap = {}
        result = []
        for n in nums:
            hmap[n] = 1 + hmap.get(n,0) 
        #  build a list like [ [frequency , number]]
        for key , value in hmap.items():
            result.append([value , key])
        result.sort()
        #  sort the array 
        #  return the last k elements of the array
        res = []
        while len(res) < k:
            res.append(result.pop()[1])
        return res
        
       

        