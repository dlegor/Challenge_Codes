class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set([-1*i for i in nums]))
        heapq.heapify(nums)
        if len(nums) < 3:
            return -1*heapq.heappop(nums)
        else:
            for i in range(2):
                heapq.heappop(nums)
            return -1*heapq.heappop(nums)
        return 1


class Solution {
    public int thirdMax(int[] nums) {
        // Flags to check if second and third maximums exist
        boolean secondMax = false, thirdMax = false;
        
        // Initialize max, second max, and third max
        int max = Integer.MIN_VALUE, secMax = Integer.MIN_VALUE, thirMax = Integer.MIN_VALUE;
        
        for (int num : nums) {
            // Skip duplicates
            if (num == max || (secondMax && num == secMax) || (thirdMax && num == thirMax)) continue;

            if (num > max) {
                // Shift current max and second max down
                if (secondMax) thirdMax = true;
                if (!secondMax) secondMax = true;
                thirMax = secMax;
                secMax = max;
                max = num;
            } else if (!secondMax || num > secMax) {
                // Update second max
                if (secondMax && !thirdMax) thirdMax = true;
                secondMax = true;
                thirMax = secMax;
                secMax = num;
            } else if (!thirdMax || num > thirMax) {
                // Update third max
                thirdMax = true;
                thirMax = num;
            }
        }
        
        // Return third max if valid, else return max
        return thirdMax ? thirMax : max;
    }
}

Test Cases
Example 1:
Input: nums = [3, 2, 1]
Output: 1
Explanation: The third distinct maximum is 1.
Example 2:
Input: nums = [1, 2]
Output: 2
Explanation: There are fewer than three distinct numbers, so return the max.
Example 3:
Input: nums = [2, 2, 3, 1]
Output: 1
Explanation: The third distinct maximum is 1.
Edge Case:
Input: nums = [1, 1, 1]
Output: 1
Explanation: All elements are the same, so return the max.
This solution effectively handles edge cases, avoids duplication checks, and efficiently finds the third maximum while maintaining readability.


Comments: 0
DLego
 
Type comment here... (Markdown is supported)
