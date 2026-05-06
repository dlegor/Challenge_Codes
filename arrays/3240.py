class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=[e**2 for e in nums]#O(n)
        return sorted(nums) #nlogn
