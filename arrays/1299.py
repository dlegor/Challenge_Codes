class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n=len(nums)
        minleght=n+1
        s=0
        left=0
        for i in range(n):
            s+=nums[i]
            
            while s>=target:
                minleght=min(minleght,i-left+1)
                s-=nums[left]
                left+=1
                
        
        
        return 0 if minleght==n+1 else minleght
    

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = rotated[i]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)