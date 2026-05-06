from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        if len(nums)==1:
            return 0
        
        if nums[n-1]>nums[n-2]:
            return n-1
        if nums[0]>nums[1]:
            return 0

        for i in range(0,n-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i

#Time Complexity O(n)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n=len(nums)
        left=0
        right=n-1
        
        while left<right:
            mid=(left+right)//2
            print(mid)
            
            if nums[mid]>nums[mid-1] and nums[mid]>=nums[mid+1]:
                return mid
            elif nums[mid]>nums[left]:
                right=mid
            else:
                left=mid+1
        
        if nums[left]>nums[left-1] and nums[left]>=nums[left+1]:
                return left
        return -1


if __name__=='__main__':
    print("Test the code")

    m=[1,2,1,3,5,6,4]
    m2=[1,2,3,1]


    print("Test Solutio",Solution().findPeakElement(nums=m))
