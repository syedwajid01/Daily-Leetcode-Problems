class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minVal=min(nums)
        
        ans=0
        for num in nums:
            ans+=num-minVal
        
        return ans
        