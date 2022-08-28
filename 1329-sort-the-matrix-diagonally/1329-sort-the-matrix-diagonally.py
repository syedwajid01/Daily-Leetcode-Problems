class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        #insertion sort 
        
        row,col=len(mat),len(mat[0])
        
        for i in range(1,row):
            for j in range(1,col):
                currNum=mat[i][j]
                
                r,c=i-1,j-1
                
                while 0<=r<row and 0<=c<col and currNum<mat[r][c]:
                    mat[r+1][c+1]=mat[r][c]
                    r-=1
                    c-=1
                
                mat[r+1][c+1]=currNum
        
        return mat
                
        
        
        