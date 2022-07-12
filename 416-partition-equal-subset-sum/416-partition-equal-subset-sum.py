class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #simply check is the given array has even totalSum 
        #and there is a subset whose sum is totalSum //2 
        totalSum=sum(nums)
        
        if totalSum%2!=0:
            return False
        
        return self.containsSubsetSum(nums,totalSum//2)
        
    
    def containsSubsetSum(self,nums,subsetSum):
        if subsetSum==0:
            return True
        if len(nums)==0:
            return False
        
        n=len(nums)
        dp=[[False for i in range(subsetSum+1)] for j in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=True
        
        for i in range(1,n+1):
            for j in range(1,subsetSum+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[n][subsetSum]
            
        