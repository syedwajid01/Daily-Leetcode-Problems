class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minCumSum=nums[0]
        currSum=nums[0]
        for i in range(1,len(nums)):
            currSum+=nums[i]
            minCumSum=min(minCumSum,currSum)
        
        if minCumSum>=1:
            return 1
        
        return 1-minCumSum
            
        