class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Silly solution
        
        if target in nums:
            return nums.index(target)
        else:
            return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Binary search
        
        left=0
        right=len(nums)-1
        
        
        while left<=right:
            mid=(left+right)//2
            
            if nums[mid]==target:
                return mid
            
            elif target<nums[0]:
                
                if nums[0]<=nums[mid]:
                    left=mid+1
                else:
                    if nums[mid]<target:
                        left=mid+1
                    else:
                        right=mid-1
            else:
                
                
                if nums[mid]<nums[0]:
                    right=mid-1
                else:
                    if nums[mid]<target:
                        left=mid+1
                    else:
                        right=mid-1
                

        return -1
   