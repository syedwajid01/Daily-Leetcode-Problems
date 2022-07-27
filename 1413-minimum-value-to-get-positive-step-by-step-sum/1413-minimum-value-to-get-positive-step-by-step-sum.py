class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        right=0
        for num in nums:
            if num<0:
                right+=(-1*num)
              
        right+=1
        left=0
        
        
        def isfeasible(start):
            curr=start
            for num in nums:
                curr+=num
                if curr<1:
                    return False
            return True
        
        while left<right:
            mid=(left+right)//2
            
            curr=mid
            if isfeasible(mid):
                right=mid
            else:
                left=mid+1
        
        if left==0:
            return 1
        return left
            
            
            
        