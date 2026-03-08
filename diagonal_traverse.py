class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        res=[]
        _map=defaultdict(list)
        for i in range(m):
            for j in range(n):
                _map[i+j].append(mat[i][j])
            
        maxsum= (m-1) + (n-1)
        for i in range(m+n-1):
            if i%2==0:
                res.extend(_map[i][::-1])
            else:
                res.extend(_map[i])
            
        return res