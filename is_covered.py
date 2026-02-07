class Solution(object):
    def isCovered(self, ranges, left, right):
        for i in range(left,right+1):
            covered=False
            for j in range(len(ranges)):
                if ranges[j][0]<=i<=ranges[j][1]:
                    covered=True
                    break
            if not covered:
                return False
        return True