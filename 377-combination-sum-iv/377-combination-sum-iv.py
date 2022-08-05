class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        
        dp=[-1]*(target+1)
        
        return self.solve(nums,0,target,dp)
    
    def solve(self,nums,currSum,target,dp):
        if currSum>target:
            return 0
        
        if currSum==target:
            return 1
        
        if dp[currSum]!=-1:
            return dp[currSum]
        
        res=0
        for i in range(len(nums)):
            res+=self.solve(nums,currSum+nums[i],target,dp)
        
        dp[currSum]=res
        return dp[currSum]
            
    
        