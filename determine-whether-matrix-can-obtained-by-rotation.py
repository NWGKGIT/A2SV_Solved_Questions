class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m=len(mat)
        n=len(mat[0])
        for i in range(4):
            for i in range(m):
                for j in range(n):
                    if j<=i:
                        mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in range(m):
                mat[i]=mat[i][::-1]
            if mat == target:
                return True
        return False