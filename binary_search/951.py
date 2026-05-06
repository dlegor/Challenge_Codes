# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        right=n
        left=1
        while left<=right:
            mid=(right+left)//2
            
            flag=guess(mid)
            
            if flag==-1:
                right=mid-1
            elif flag==1:
                left=mid+1
            else:
                return mid
        