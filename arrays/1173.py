from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n=len(nums)
        i=0
        j=1
        k=1
        while i<n and j<n:
            
            if nums[i]==nums[j]:
                j+=1
            
            else:
                nums[i+1]=nums[j]
                i+=1
                k+=1
        
        return k

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
        
#         n=len(nums)
#         i=0
#         j=1
#         k=0
#         while i<n and j<n:
#             print("ite1",i,j)
#             print(nums)
#             if nums[i]<nums[j]:
#                 i+=1
#                 j+=1
#                 k+=1
            
#             if nums[i]==nums[j]:
#                 l=j
#                 while l<n:
#                     if nums[i]==nums[l]:
#                         l+=1
#                     else:
#                         break
                
#                 nums[j]=nums[l]
#                 i=j
#                 j=i+1
#                 k+=1
        
#         return k



if __name__=='__main__':
    print("Test the code")
    a=[1,1,2]
    b=[0,0,1,1,1,2,2,3,3,4]
    c="a good   example"

    print("Version 4, solution:", Solution().removeDuplicates(nums=a),"\n")
    #print("Version 4, solution:", Solution().reverseWords(s=b),"\n")
