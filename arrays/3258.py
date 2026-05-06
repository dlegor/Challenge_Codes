from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        H=Counter(nums)        
        idx=0
        n=len(nums)
        i=0
        
        
        while i<n:
            a=nums[i]
            w=H[a]
            nums[idx]=nums[i]
            i=i+w
            idx+=1
        return idx


from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx=1
        i=1
        n=len(nums)
        while i<n:
            if nums[i]!=nums[i-1]:
                nums[idx]=nums[i]
                i+=1
                idx+=1
            else:
                i+=1
        return idx
