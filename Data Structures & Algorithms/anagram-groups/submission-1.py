class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute force approach - 0(N.klogk) sorting happening n-times
        # space complexity - 3 * 3 = 9 , 5*3 = 15 0(N.K) N- is the number of strings , K is the length of each string
        # create a map
        #  get the total ascii of a character and add it to the dict interms of array
        #  iterate the dict and put all the value arrays in an array and return
        #  expected time complexity - 0(n)

        #  create a map
        # anagram_map = {}
        # #  iterate the input array
        # for i in range(0, len(strs)): # 0(n)
        # #  sort the string
        #     if anagram_map.get( "".join(sorted(strs[i]))): # 0(N. klogk)
        # #  if string exists in dict append the string in that value , else create a new array and append the current string
        #         anagram_map["".join(sorted(strs[i]))].append(strs[i])
        #     else:
        #         anagram_map["".join(sorted(strs[i]))] = [strs[i]]
        # # iterate the dict and add the value to an array and return them
        # result =[]
        # for value in anagram_map.values(): # 0(n)
        #     result.append(value)
        # return result


        # res = defaultdict(list)
        # for word in strs:
        #     sword = "".join(sorted(word))
        #     res[sword].append(word)
        # return list(res.values())

        # optimized solution - same solution, just removing sorted which causes n log n times the total number of sting
        # create a map. TC - N.M wher N is the number of words and M is the length of each word
        # SC - N.M*26 -> NM
        anagram_map = defaultdict(list)
        #  iterate the elements
        for word in strs:
        # create an array of size 26 - each index is refers to the alphabet order
            s = [0]* 26
        # increamt the array size index based on the input string char
            for i in word:
                s[ord(i) - ord('a')]+=1
        #  add to dict by tuple them , and add the actual string to the list
            # [1,0,2,0...1,0] -> (1,0,2,0...1,0) -> tuple just preseves the value
            anagram_map[tuple(s)].append(word)
        #  return the list
        return list(anagram_map.values())


        