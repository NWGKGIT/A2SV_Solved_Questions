class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        count=0
        flattend=[]
        for sub in grid:
            flattend.extend(sub)
        for i in flattend:
            if i<0:
                count+=1
        return count