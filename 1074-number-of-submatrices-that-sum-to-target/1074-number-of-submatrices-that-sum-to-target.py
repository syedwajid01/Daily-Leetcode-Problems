class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        #find prefix sum of each row
        row,col=len(matrix),len(matrix[0])
        for i in range(row):
            for j in range(1,col):
                matrix[i][j]+=matrix[i][j-1]
        
        ans=0
        
        #for every possible matrix range between two columns 
        
        #for every matrix between i and j 
        #find its cumulative sum for each row
        #then this problem becomes similar to subarray sum equal k 
        for i in range(col):
            for j in range(i,col):
                curr=0
                sumArrOccuranceMap={0:1}
                
                #for every row
                #find cumulative sum 
                for k in range(row):
                    curr+=(matrix[k][j] - (matrix[k][i-1] if i>0 else 0))
                    ans+=sumArrOccuranceMap.get(curr-target,0)
                    sumArrOccuranceMap[curr]=sumArrOccuranceMap.get(curr,0)+1
        
        return ans 
                
                