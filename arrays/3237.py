class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #solution1
        n=0
        
        for elem in nums:
            if len(str(elem))%2==0:
                n+=1
        return n

class Solution:
    def num_digits(self,m:int)->int:
        
        
        if m<10:
            return 1
        else:
            q=m//10
            n=1
            while q>=10:
                q=q/10
                n+=1
            return n+1
                
    def findNumbers(self, nums: List[int]) -> int:
        #solution2
        n=0
        
        for elem in nums:
            d=self.num_digits(elem)
            
            if d%2==0:
                n+=1
        return n
        