class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l=1
        r=num//2
        if num==1:
            return True
        
        while l<=r:
            mid=(l+r)//2
            if mid*mid==num:
                if int(mid)==mid:
                    return True
                else:
                    return False
            elif mid*mid<num:
                l=mid+1
            else:
                r=mid-1
        
        return False
#Tamplate 2             
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l=1
        r=num//2
        if num==1:
            return True
        
        while l<r:
            mid=(l+r)//2
            if mid*mid==num:
                if int(mid)==mid:
                    return True
                else:
                    return False
            elif mid*mid<num:
                l=mid+1
            else:
                r=mid
                
        if l*l==num:
            return True
        
        return False
                
#Tamplate 3
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l=1
        r=num//2
        if num==1:
            return True
        
        while l+1<r:
            mid=(l+r)//2
            if mid*mid==num:
                if int(mid)==mid:
                    return True
                else:
                    return False
            elif mid*mid<num:
                l=mid
            else:
                r=mid
                
        if l*l==num:
            return True
        
        if r*r==num:
            return True
        return False
or