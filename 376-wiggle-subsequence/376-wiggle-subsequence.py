class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        
        if len(nums)==2:
            return 2 if nums[0]!=nums[1] else 1
        
        '''
        
        [1,7,4,9,2,5]
        
        +ve -ve 
        -ve +ve 
        
        [1,7,4,9,2,5]
        
        zigzag numbers increase then decrease
        
        [1,17,5,10,13,15,10,5,16,8]
        
        
        #can we get max wiggle subsequence by just finding zig zag or mountain sequence
        
        [100,3,10,15,13,8]
        
        '''
        #sign ==1 peak
        #sign ==-1 valley
        
        sign=0
        
        ans=1
        j=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1] and sign!=1: #current is peak and prev was valley 
                ans+=1
                sign=1
            elif nums[i]<nums[i-1] and sign!=-1: #current is valley and prev was peak 
                ans+=1
                sign=-1
        
        return ans
                
            
    
        
    
    
        