class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n=len(nums)
        
        if n==0:
            return [-1,-1]
        if n==1 and nums[0]!=target:
            return [-1,-1]
        if n==1. and nums[0]==target:
            return [0,0]
        
        l=0
        r=n-1
        a,b=-1,-1
        while l<r:
            mid=(l+r)//2
            
            if nums[mid]==target:
                s=mid #down
                while s>=0 and nums[s]==target :
                    s-=1
                a=s+1
                s=mid#up
                while s<n and nums[s]==target:
                    s+=1
                   
                b=s-1
                return [a,b]
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid
        
        #post-processing
        if nums[l]==target:
            return [l,l]
        else:
            return [-1,-1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1
        last=-1

        n=len(nums)

        l,r=0,n-1


        while l<=r:
            mid=(l+r)//2

            if nums[mid]==target:
                first=mid
                r=mid-1
            
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1

        
        l,r=0,n-1

        while l<=r:
            mid=(l+r)//2

            if nums[mid]==target:
                last=mid
                l=mid+1

            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1

        return [first,last]