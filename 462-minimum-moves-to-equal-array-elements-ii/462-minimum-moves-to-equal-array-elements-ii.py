class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        #minimum number of moves to make all the array elements equal
        #[1,2,3]
        #2 and we changed all the elements to 2
        #[1,10,2,9]
        #9
        #8 + 1+7 => 16
        # 5
        #4+5+3+4 => 16

        nums.sort()
        n=len(nums)
        if n%2==1:
            candidate=nums[n//2]
        else:
            candidate=(nums[n//2]+nums[n//2-1])//2
        
        ans=0
        for num in nums:
            ans+=abs(num-candidate)
        
        return ans
        