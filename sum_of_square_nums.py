class Solution:
    def judgeSquareSum(self, c: int) -> bool:
    
        l=0
        r=int(c**(1/2))
        while l<=r:
            s=l**2+r**2
            if s==c:
                return True
            if s>c:
                r-=1
            else:
                l+=1
        return False