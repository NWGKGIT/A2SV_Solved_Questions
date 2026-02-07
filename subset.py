from collections import Counter
class Solution:

    def isSubset(self, a, b):
        countA=Counter(a)

        for x in b:
            if countA[x]>0:
                countA[x]-=1
            else:
                return False
        return True