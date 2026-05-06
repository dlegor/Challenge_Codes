from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #silly solution
        
        n=len(arr)
        l,r=0,n-1
        first=0
        last=0
        
        while l<=r:
            mid=(l+r)//2
            if (abs(arr[mid]-x)<=abs(arr[mid+1]-x)) and (abs(arr[mid]-x)<=abs(arr[mid-1]-x)):
                
                #First element
                first=mid
                r=mid-1
                
                
            elif abs(arr[mid]-x)>abs(arr[mid+1]-x):
                    l=mid+1
            else:
                    r=mid-1
        
        #print(first, mid)
        
    
        l,r=0,n-1
        
        while l+1<r:
            mid=(l+r)//2
            print(mid)
            if (abs(arr[mid]-x)<=abs(arr[mid+1]-x)) and (abs(arr[mid]-x)<=abs(arr[mid-1]-x)):
                #First element
                last=mid
                l=mid
                
                
            elif abs(arr[mid]-x)>abs(arr[mid-1]-x):
                    r=mid-1
            else:
                    l=mid+1


        return arr[first:last]
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]: return arr[:k]
        if x >= arr[-1]: return arr[-k:]
       
        # binary search (rightmost x <= k)
        l, r = 0, len(arr)-1
        while l +1< r:
            m = l + (r - l + 1) // 2
            print(m)
            if abs(arr[m]-x) >= abs(arr[m-1]-x) and abs(arr[m]-x)>=abs(arr[m-1]-x) :
                l = m
            else:
                r = m 
        print(r,l,m)
        # window expansion
        while r - l + 1 < k:
            if r == len(arr)-1:
                return arr[-k:]
            elif l == 0:
                return arr[:k]
            else:
                if (arr[r+1] - x)<=(x - arr[l-1]) :
                    r += 1
                else:
                    l-= 1
        return arr[l+1:r+1]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r=0,len(arr)-k
        
        while l<r:
            m=(l+r)//2
            if (x-arr[m])>(arr[m+k]-x):
                l=m+1
            else:
                r=m
        
        return arr[l:l+k]

if __name__=='__main__':
    print("Test the code")

    m=[1,1,1,10,10,10]
    k=1
    x=9
    m=[0,0,0,1,3,5,6,7,8,8]
    k=2
    x=2


    print("Test Solutio",Solution().findClosestElements(arr=m,k=k,x=x))
