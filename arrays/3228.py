class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n==1 and (1 in nums):
            return 1
        elif n==1 and (1 not in nums):
            return 0
        else:
            
            m=0
            i=0
            c=0
            while i<n:       
                if nums[i]==1:
                    c+=1
                    i+=1
                else:
                    m=max(c,m)
                    c=0
                    i+=1
            return max(m,c)
