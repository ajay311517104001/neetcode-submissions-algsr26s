class Solution:
    def isPalindrome(self, s: str) -> bool:
        # It is not just a palindrome check
        # we need to skip the alphanumeric values
        #  we need to create a new string which should be all in lower case and should not have alpha numeric values
        'wasitacaroracatisaw'
        # new_str = ''
        # # TC = 0(n) , SC = O(n)
        # for c in s: #0(n)
        #     if c.isalnum():
        #         new_str+=c.lower()
        # return new_str == new_str[::-1] #0(n)

        # optimum solution - using two pointers
        # point the first and last elment
        L,R = 0 , len(s)-1
        while L<R:
        # check if its a alpha num
            
        #  if its is not alpha num adjjust the position
            if not s[L].isalnum():
                L+=1
            elif not s[R].isalnum():
                R-=1
            else:
                if s[L].lower() != s[R].lower():
                    return False
                L+=1
                R-=1
        return True
            
        # if lower both and check if both are not equal return false
        # decrement or increment the spaces
        # return true


        



        