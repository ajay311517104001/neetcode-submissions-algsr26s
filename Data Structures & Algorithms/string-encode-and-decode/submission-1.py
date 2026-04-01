class Solution:

    def encode(self, strs: List[str]) -> str: # TC -> O(n)
        #  we can encode the string in what are the ways we want
        #  the utf char means Ascii all the char in the keyboard is considered as askii one
        #  we need to implement a delimiter to find when the word ends or when the word starts
        # we can have delimiter with the count of the word
        res = ''
        #  iterate the words
        for word in strs:  
        # len(word) + '#' +word
            res += str(len(word)) + '#' + word
        # 4#Neet4#code4#love3#you
        return res

    def decode(self, s: str) -> List[str]:
        #  result string holder
        arr =[]
        i=0 
        while i < len(s):  #O(s) - where s is the length of the decoded string
            j = i #1
        # find hash first
            while s[j] !='#':
                j+=1
            limit = int(s[i:j])
            i = j+1
            j= i + limit
            arr.append(s[i:j])
            i = j
        return arr





        # # 4#Neet4#code
        #    |         i,
        #              j
        # arr =[]
        # i=0 
        # while i < len(s)
        # j = i #1
        # # find hash first
        #     while s[j] !='#':
        #         j+=1
        #     limit = int(s[i:j])
        #     i = j+1
        #     j= i + limit
        #     arr.append(s[i:j])
        #     i = j
        # return arr

