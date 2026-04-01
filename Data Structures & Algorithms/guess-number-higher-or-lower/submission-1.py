# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #  run loop unitl we get zero as result i.e we find the element
        # 20
        l , r =0 , n
        while True:
        # divide the n//2 
            mid = (l+r)//2
        #  send the divice to guess if it is > 0
            if guess(mid) > 0:
        #  n=n+1
                l = mid +1
        # if the guess returns the -1 < 0
            elif guess(mid) < 0:
        # n=n-1
                r = mid -1
        # else
            else:
                return mid

        #  return num
        