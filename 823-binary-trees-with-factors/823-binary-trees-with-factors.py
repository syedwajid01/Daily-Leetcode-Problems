class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        #dp 
        n=len(arr)
        dp=[1]*n
        arr.sort()
        
        index={}
        for i in range(len(arr)):
            index[arr[i]]=i
            
        
        
        for i in range(n):
            for j in range(i):
                if arr[i]%arr[j]==0:
                    #then j is left child
                    right=arr[i]//arr[j]
                    
                    if right in index:
                        dp[i]=dp[i]+(dp[j]*dp[index[right]])
                
        return sum(dp)%(10**9+7)
                        
        
        