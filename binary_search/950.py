

class Solution:
    def mySqrt(self, x: int) -> int:
        
        left=0
        right=x
        
        while left<=right:

            
            mid=left+(right-left)/2
            print(mid)
            if 0<=(x-mid*mid) and (x-mid*mid)<=0.0001:
                return int(mid)
            else:
                if mid*mid>x:
                    right=mid+1
                else:
                    left=mid-1
        
        return -1
    
class Solution:
    def mySqrt(self, x: int) -> int:
        
        left=1
        right=x//2
        
        if x==0:
            return 0
        if x<0:
            return -1
        if x==1:
            return 1
        
            
        while left<=right:
            
            mid=(right+left)//2
            
            if mid*mid==x:
                return mid
            
            elif mid*mid<x:
                left=mid+1
                ans=mid
            else:
                right=mid-1
        
        return ans
  

if __name__=='__main__':
    print("Test the code")

    a=2147395599

    print("Test Solutio",Solution().mySqrt(x=a))
