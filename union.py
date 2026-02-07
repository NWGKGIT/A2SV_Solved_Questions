class Solution:    
    def findUnion(self, a, b):
        unique=set()
        for i in a:
            unique.add(i)
        for j in b:
            unique.add(j)
        return list(unique)