from heapq import *
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        #dp[i]=maxSum ending at i 
        n=len(nums)
        dp=[-1]*n
        dp[0]=nums[0]        
        #dp[i] = nums[i] + maxDp we found previously till i-k index (becuase we can only come here with k jumps)
        
        heap=[]
        heappush(heap,(-dp[0],0))
        
        for i in range(1,n):
            while heap and heap[0][1]<i-k:
                heappop(heap)
            dp[i]=nums[i]+ (-1*heap[0][0])
            heappush(heap,(-dp[i],i))
        
        return dp[-1]
        
        
        