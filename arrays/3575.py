class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        
        for elem in nums:
            if elem==val:
                c+=1
        h=0#reference position
        i=0#check
        n=len(nums)
        
        while i<n:
            if nums[i]!=val:
                nums[h]=nums[i]
                i+=1
                h+=1
            else:
                i+=1
        return h


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        idx=0
        j=0
        
        n=len(nums)
        
        while j<n:
            if nums[j]==val:
                nums[j]=None
                j+=1
            else:
                c+=1
                nums[idx]=nums[j]
                idx+=1
                j+=1
        return c
