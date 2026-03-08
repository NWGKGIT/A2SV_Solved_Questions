class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n=len(img[0])
        m=len(img)
        mat=[[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                count=0
                tot=0
                for ii in range(i-1,i+2):
                    for jj in range(j-1,j+2):
                        if ii<m and jj<n and ii>=0 and jj>=0:
                            tot+=img[ii][jj]
                            count+=1
                mat[i][j]=tot//count
        return mat
    