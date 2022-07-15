class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows,cols=len(grid),len(grid[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        visited=set()
        self.area=0
        ans=0
        
        def dfs(i,j):
            if (i,j) in visited:
                return
            
            visited.add((i,j))
            self.area+=1
            
            for xx,yy in directions:
                next_i=i+xx
                next_j=j+yy
                
                if 0<=next_i<rows and 0<=next_j<cols and grid[next_i][next_j]==1:
                    dfs(next_i,next_j)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    self.area=0
                    dfs(i,j)
                    ans=max(ans,self.area)
        
        return ans
                    
        
        