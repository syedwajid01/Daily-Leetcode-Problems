class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump=0
        for idx,num in enumerate(nums):
            if idx>maxJump:
                return False
            maxJump=max(maxJump,idx+num)
        
        return True
        