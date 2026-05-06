class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0) return 0; // corner case

        int left = 0; // left pointer
        int right = nums.length - 1; // right pointer
        int k = 0; // result
        while (left <= right) {
            if (nums[right] == val) { // find the first acceptable number from the right
                right--;
                continue;
            }

            if (nums[left] == val) { // found 'val'
                nums[left] = nums[right]; // set value on left side
                right--; // move right pointer
            }

            k++; // increment result
            if (left == right) break; // pointers met
            left++; // move left pointer
        }

        return k;
    }
}


#Python version 

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # n=len(nums)

        # if n==0:
        #     return 0
        
        # i=0
        # j=n-1
        # k=0
        # while i<=j:
        #     if nums[j]==val:
        #         j-=1

        #     if nums[i]==val:
        #         nums[i]=nums[j]
        #         j-=1
        #         k+=1
            
        #     if i==j:
        #         break

        #     i+=1

        # return k

            
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n=len(nums)
        counts=0
        for i in range(n):
            if nums[i]==val:
                counts+=1
        
        i=0
        while i<n:
            if nums[i]==val:
                j=i+1
                    
                while j<n:
                    if nums[j]!=val:
                        nums[i],nums[j]=nums[j],nums[i]
                            
                        j=n
                    else:
                        j+=1
                i+=1
            else:
                i+=1
        return n-counts

