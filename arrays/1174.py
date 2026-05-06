class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
            
        i=0
        j=0
        while i<n and j<n:
            if nums[i]!=0:
                i+=1
                
            else:

                for j in range(i, n):
                    if nums[j]==0 and j<n-1:
                        j+=1
                    else:
                        break
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                
            
lass Solution {
    public void moveZeroes(int[] nums) {
    int a=0;
    for(int i=0 ; i<nums.length ; i++){
        //Checking elements in array
        if(nums[i]!=0){
            nums[a]=nums[i];
            a++;
        }
       
    }
    
# *   //moving this loop from a****Bold*****
    for(int i=a ; i<nums.length ; i++){
        nums[i]=0;
    }

    }
    
}

class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1


