from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        minHeap=[]
        
        for i in range(n):
            row=matrix[i]
            heappush(minHeap,[row[0],i,0])
        
        for i in range(k-1):
            val,r,c=heappop(minHeap)
            if c+1<n:
                heappush(minHeap,[matrix[r][c+1],r,c+1])
        
        ans,_,_=heappop(minHeap)
        return ans
            
            
        
        