class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans=0
        
        for i in range(len(nums)):
            maxVal=nums[i]
            minVal=nums[i]
            for j in range(i,len(nums)):
                maxVal=max(maxVal,nums[j])
                minVal=min(minVal,nums[j])
                ans+=(maxVal-minVal)
        
        return ans
                
        