class Solution:
    def spiralOrder(self,matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        toprow, bottomrow = 0, rows - 1
        leftcol, rightcol = 0, cols - 1
        res = []

        while len(res) < (cols * rows):
            for c in range(leftcol, rightcol + 1):
                res.append(matrix[toprow][c])
            toprow += 1

            for r in range(toprow, bottomrow + 1):
                res.append(matrix[r][rightcol])
            rightcol -= 1

            if len(res) < (cols * rows):
                for c in range(rightcol, leftcol - 1, -1):
                    res.append(matrix[bottomrow][c])
                bottomrow -= 1

            if len(res) < (cols * rows):
                for r in range(bottomrow, toprow - 1, -1):
                    res.append(matrix[r][leftcol])
                leftcol += 1

        return res