class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n<0:
            x=1/x
            n=-n
        curr=x
        res=1
        while n>0:
            if n%2==1:
                res*=curr
            curr*=curr
            n//=2

        return res