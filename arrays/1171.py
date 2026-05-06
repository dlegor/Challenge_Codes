from typing import List

    
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def factorial(k:int)->int:
            
            if k==0:
                return 1
            if k==1:
                return 1
            a=1
            for i in range(1,k+1):
                a*=i
                
            return a
        
        def combination(n:int,k:int)->int:
            
            if (k==0) or (k==n):
                return 1
            
            if k==1 or k==n-1:
                return n
 
            
            temp=1
            
            for i in range(n,(n-k),-1):
                temp*=i
                
            d=factorial(k)
            
            return temp//d
        
        ans=[]
        
        for j in range(rowIndex+1):
            c=combination(rowIndex,j)
            ans.append(c)
        
        return ans



class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        prev = 1
        for k in range(1, rowIndex + 1):
            next_val = prev * (rowIndex - k + 1) // k
            res.append(next_val)
            prev = next_val
        return res

                
if __name__=='__main__':
    print("Test the code")

    print("Version 4, solution", Solution().getRow(rowIndex=3),"\n")
    print("Version 4, solution", Solution2().getRow(rowIndex=6),"\n")
