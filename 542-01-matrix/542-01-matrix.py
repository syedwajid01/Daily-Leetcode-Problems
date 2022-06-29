class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue=deque()
        rows,cols=len(mat),len(mat[0])
        
        res=[[-1 for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    res[i][j]=0
                    queue.append([i,j])
        
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        
        while queue:
            r,c=queue.popleft()
            
            for x,y in directions:
                next_r,next_c=r+x,y+c
                
                if 0<=next_r<rows and 0<=next_c<cols and res[next_r][next_c]==-1:
                    res[next_r][next_c]=res[r][c]+1
                    queue.append([next_r,next_c])
        
        return res
            
                    
        