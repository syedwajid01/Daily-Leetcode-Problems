from heapq import *
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row,col=len(mat),len(mat[0])
        mp=collections.defaultdict(list)
        
        for i in range(row):
            for j in range(col):
                heappush(mp[i-j],mat[i][j])
        
        for i in range(row):
            for j in range(col):
                mat[i][j]=heappop(mp[i-j])
                
    
        return mat
                
        
        
        