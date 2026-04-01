class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute force approach - 0(n log n )
        # create a map
        #  get the total ascii of a character and add it to the dict interms of array
        #  iterate the dict and put all the value arrays in an array and return
        #  expected time complexity - 0(n)

        #  create a map
        anagram_map = {}
        #  iterate the input array
        for i in range(0, len(strs)): # 0(n)
        #  sort the string
            if anagram_map.get( "".join(sorted(strs[i]))): # 0(n log n)
        #  if string exists in dict append the string in that value , else create a new array and append the current string
                anagram_map["".join(sorted(strs[i]))].append(strs[i])
            else:
                anagram_map["".join(sorted(strs[i]))] = [strs[i]]
        # iterate the dict and add the value to an array and return them
        result =[]
        for value in anagram_map.values(): # 0(n)
            result.append(value)
        return result

        