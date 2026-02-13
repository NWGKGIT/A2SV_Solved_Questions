class Solution:
    def isHappy(self,n):
        seen = set()
        while n != 1:
            possible = 0
            for i in str(n):
                possible += int(i) ** 2
            if possible in seen:
                return False
            seen.add(possible)
            n = possible
        return True

            
        
