from heapq import *
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return nums[0]
        if k==1:
            return sum(nums)
        
        n=len(nums)
        dq=deque([[nums[0],0]])
        
        for i in range(1,n):
            while dq and dq[0][1]<i-k:
                dq.popleft()
            
            maxSumEndingAtI=nums[i]+dq[0][0]
            
            while dq and dq[-1][0]<maxSumEndingAtI:
                dq.pop()
            
            dq.append([maxSumEndingAtI,i])
        
        return dq[-1][0]
                
            
            
       
        
        
        