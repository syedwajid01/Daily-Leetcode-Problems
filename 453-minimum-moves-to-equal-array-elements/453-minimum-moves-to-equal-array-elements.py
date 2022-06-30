class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #x*n = initialSum + (n-1)*m 
        #x= min+m
        #min*n + m*n = initialSum + m*n-m
        #m=initialSum - min*n 
        return sum(nums) - min(nums)*len(nums)