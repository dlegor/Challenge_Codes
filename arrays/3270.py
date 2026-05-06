class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ans=[]
        n=len(nums)
        for i in range(0,n):
            a=abs(nums[i])
            if nums[a-1]>0:
                nums[a-1]=-nums[a-1]
                
        for i in range(0,n):
            if nums[i]>0:
                ans.append(i+1)
                
        
        return ans
