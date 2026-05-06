class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        n=len(nums)
        if n==1:
            return nums[0]
        
        
        l=0
        r=n-1
        
        while l<r:
            mid=(r+l)//2
            
            if nums[mid]>nums[r]:
                if nums[l]>nums[r]:
                    l=mid+1
                else:
                    r=mid
            else:
                if nums[l]>nums[mid]:
                    r=mid
                else:
                    r=mid
        
    
        return nums[l]
