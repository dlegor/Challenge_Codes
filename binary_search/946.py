class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #size of the array
        n=len(nums)
        #condition 1
        
        if len(nums)==1:
            return 0
        #condition 2- tail
        if nums[n-1]>nums[n-2]:
            return n-1
        #Condition 3 - heat
        if nums[0]>nums[1]:
            return 0
        
        #binary search
        
        left=0
        right=n-1
        
        while left+1<right:
            
            mid=(left+right)//2
            
            if (nums[mid]>nums[mid-1]) and (nums[mid]>nums[mid+1]):
                return mid
            
            else:    
                if (nums[mid]<nums[mid-1]) or (nums[mid]<nums[mid+1]): 
                    r=mid-1
                else:
                    l=mid+1
                    
        return -1
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #size of the array
        n=len(nums)
        #condition 1
        
        if len(nums)==1:
            return 0
        #condition 2- tail
        if nums[n-1]>nums[n-2]:
            return n-1
        #Condition 3 - heat
        if nums[0]>nums[1]:
            return 0
        
        #binary search
        
        l=0
        r=n-1
        
        while l+1<r:
            mid=(l+r)//2
            
            if (nums[mid]>nums[mid-1]) and (nums[mid]>nums[mid+1]):
                return mid
            
            else:    
                if (nums[mid]<nums[mid-1]): 
                    r=mid+1
                else:
                    l=mid
                    
        if (nums[l]>nums[l-1]) and (nums[l]>nums[l+1]):
                return l
        if (nums[r]>nums[r-1]) and (nums[r]>nums[r+1]):
                return r
            
                    
        return -1

if __name__=='__main__':
    print("Test the code")
    nums=[1,2,3,1]



    print("Test Solutio",Solution().findPeakElement(nums=nums))
