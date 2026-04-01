class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # conditions
        # i,j,k all are unique
        #  output should not contains duplicates
        # I can return the ouput triplets in any order
        #  The sum i need to get is 0 when i add nums[i] + nums[j] + nums[k] == 0
        #  need to return as numbers not as index
        # Rough work
        #  [-1,0,1,2,-1,-4]
        #      i j    k

        # -1 + 0 + 1 = 0 add to array
        #  check if it exists in the array
        # -1 + 0 + 2 = 1
        # -1 + 0 -1 = -2
        # -1 + 0 -4 = -5

        # -1 + 1 + 2 = 2
        # -1+1-1 = 1
        # -1 + 1 -4 = -4
        # TC- O(n3) + nlogn = O(n3) , space O(n) n-> is the number of triplets
        #  set can only contains imutable object for hashing , mutable object when rehash it will tend to change the loction

        # result = set()
        # # This sort is to avoid the duplicates results which get adds to the result
        # nums.sort()
        # #  sort to handle the duplicates
        # for i in range(0,len(nums)-2):
        #     for j in range(i+1 , len(nums)-1):
        #         for k in range(j+1 , len(nums)):
        #             # check if the triplets making zero
        #             if nums[i] + nums[j] + nums[k] == 0 :
        #             #  if yes check tat triplet exists in the result
        #                 result.add(tuple([nums[i],nums[j],nums[k]]))
        #             # if not update the result
        # return list(result)



        #  Hashmap implementation - take i and j sum it check the 3rd value in hashmap
        # [-1,0,1,2,-1,-4]
        # sort it so we don't have duplicates - why sorting? so that we can check for the previous element if its duplicate

        #  res = []
        # res =set()
        # #  update the hashmap with the frequencey
        # hmap= defaultdict(int)
        # #  sort the nums
        # nums.sort()

        # for i in nums:
        #     hmap[i]= 1 + hmap.get(i,0)
        # # { -1 :1 , 
        # #   0: 0 ,
        # #  1 : 0 ,
        # #   2:1,
        # #   -4:1}
        # #  iterate i the element
        # #  [-4,-1,-1,0,1,2]   [-4,2,2] [-1,-1,2] [1,0,-1]
        # #            i j
        # for i in range(len(nums)):
        # #      reduce the frequency based on the current element
        #     hmap[nums[i]]-=1
        #     if i and nums[i] == nums[i-1]:
        #         continue
        # #   iterate the j element  j should be next to i
        #     for j in range(i+1 , len(nums)): 
        #     #       reduce the frequence based on the j element
        #         hmap[nums[j]]-=1
        #         if nums[j] == nums[j-1] and i < j-1 :
        #             continue
        #     #    target = -(nums[i] + nums[j])
        #         target = -(nums[i]+nums[j])
        #     #  if the target exists in the hmap
        #         if hmap[target] >0:
        #                 # update the res
        #                 res.add((nums[i],nums[j],target))
        #     # construct the map again for the next iteration
        #     for i in range(i+1,len(nums)):
        #         hmap[i]= 1 + hmap.get(i,0)
        # # return the res
        # return list(res)
        



        # optimized approach - implementation with two pointer
        #   0,1 ,2 ,3,4,5
        # [-4,-1,-1,0,1,2]
        #           i j k  
        
        # res =[[-1,-1,2],[-1,1,0]]
        # edge case
        # if i has duplicates ignore them an continue to next
        #  j and k has duplicate ignore them continue to next
        #  create a result array
        res = []
        #  iterate i  the elements
        nums.sort()
        for i in range(len(nums)-2):
        #   Two pointer implementation
        #    j , k = i+1 , len(arr)-1
            if i and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
        #    if sum of i +j+k is 0:
            while j < k:
                s = nums[i] + nums [j] + nums[k]
                if s == 0 :
                    res.append([nums[i],nums [j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j<k and i<j:
                        j+=1
                    while nums[k] == nums[k+1] and j<k and i<k:
                        k-=1


                elif s> 0 :
                    k-=1
                else:
                    j+=1
            #  if lower increase the k by 1
        return res



       





