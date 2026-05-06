class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        n=len(nums)
        i=0
        j=0
        #k=0
        M=0
        #while i<n and j<n:
        while i<n :
            if nums[i]==1:
                j=i
                k=0
                while j<n:
                    if nums[j]==1:
                        k+=1
                        j+=1
                        
                    else:
                        j=n
                
                M=max(M,k)
                i=i+k
            else:
                i+=1
                    
        return M 
            
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, windowSize = 0, 0
        for n in nums:
            if n == 1:
                windowSize += 1
            else:
                res = max(res, windowSize)
                windowSize = 0
        res = max(res, windowSize)

        return res
    

   public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int minLength = Integer.MAX_VALUE;
        int sum = 0;
        int left = 0;

        for(int right = 0; right < n; right ++){
            sum += nums[right];

            while(sum >= target){
                minLength = Math.min(minLength, right - left + 1);
                sum -= nums[left];
                left ++;
            }
        }
        return minLength == Integer.MAX_VALUE? 0 : minLength;
    }
}