class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<=1:
            return [[1]]
        
        ans=[[1],[1,1]]
        
        for i in range(2,numRows):
            curr=[1]
            prev=ans[-1]
            for j in range(1,len(prev)):
                curr.append(prev[j]+prev[j-1])
                
            curr.append(1)
            ans.append(curr)
        
        return ans
        
        
        