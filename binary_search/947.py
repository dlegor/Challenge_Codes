
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        
        if n==0:
            return -1
        if n==1:
            return 1
            
        left=1
        right=n
        #binary Search
        while left<right:
            mid=(left+right)//2
            
            a=isBadVersion(mid)
            
            if a:
                right=mid
            else:
                left=mid+1
        #Post-processing      
        if isBadVersion(left):
            return left
        
                
