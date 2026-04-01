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
        #  TC- 0(nlogn) - sort , SC - O(n + h + k) -> O(n)
        # hmap = {}
        # result = []
        # for n in nums:
        #     hmap[n] = 1 + hmap.get(n,0) 
        # #  build a list like [ [frequency , number]]
        # for key , value in hmap.items():
        #     result.append([value , key])
        # result.sort()
        # #  sort the array 
        # #  return the last k elements of the array
        # res = []
        # while len(res) < k:
        #     res.append(result.pop()[1])
        # return res

        # optimized approach - using bucket sort in different way TC -> ->O(3.n) -> O(n) , SC -> O(3.n) -> O(n)
        
        # create map and load its key and repetation as count
        # {
        #     1:1,
        #     2:2,
        #     3:3,
        #     4:1
        # } 
        hmap = {}  # O(n)
        for n in nums:
            hmap[n]=1 + hmap.get(n,0)
        #  create an array with the size input array
        print('hmap' , hmap)
        build_arr = [[] for i in range(0,len(nums)+1)] #0(n)
        #  take the hash map consider value as index and key as element- note push them as array
        #  eg: [  , [1] , [2] , [3] , ] - Bucket sort
        #       0 ,    1  ,  2  , 3 ,4
        for key , value in hmap.items():
            build_arr[value].append(key)
        print('build arr' , build_arr)
        # pop the elements till k times and put them in the resultant array and return them
        res =[] # 0(n) - for worst case scenario - for [1,2,3] all sits in first index so res is just the size of the input array
        
        for i in range(len(build_arr)-1, 0 , -1):
            for j in build_arr[i]:
                res.append(j)
            if len(res) == k:
                return res


        
       

        