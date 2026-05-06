class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        l=0
        r=len(letters)-1
        m=ord('z')+100
        ans=''
        a1=ord(target)
        
        if a1<ord(letters[0]):
            return letters[0]
        
        if a1>=ord(letters[-1]):
            return letters[0]
        
        while l<=r:
            
            mid=(l+r)//2
            
            if ord(letters[mid])>a1 and (ord(letters[mid])-a1)<m:
                m=min(m,ord(letters[mid])-a1)
                ans=letters[mid]
                r=mid-1
            else:
                l=mid+1
                
        return ans
        
        