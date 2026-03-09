class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        setRow=set()
        setCol=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    setCol.add(j)
                    setRow.add(i)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in setRow or j in setCol:
                    matrix[i][j]=0
        return matrix