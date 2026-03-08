class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        i=0
        res=[]
        for i in range(n):
            ans=[]
            for j in range(m):
                ans.append(matrix[j][i])
            res.append(ans)
        return res