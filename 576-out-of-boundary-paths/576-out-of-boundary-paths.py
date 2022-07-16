class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        memo={}
        
        def dfs(i,j,moves):
            key=(i,j,moves)
            
            if key in memo:
                return memo[key]
            
            if moves<0:
                return 0
            if not (0<=i<m and 0<=j<n):
                return 1
            
            ans=0
            for x,y in directions:
                next_i=x+i
                next_j=y+j
                
                ans+=dfs(next_i,next_j,moves-1)
            
            memo[key]=ans
            return ans
        
        return dfs(startRow,startColumn,maxMove)% (10**9+7)
    