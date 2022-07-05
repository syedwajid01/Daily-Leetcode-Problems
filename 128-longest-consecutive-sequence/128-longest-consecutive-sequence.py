class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #longest consecutive sequence
        '''
        
        [100,4,200,1,3,2]
        
        1 2 3 4
        
        [0,3,7,2,5,8,4,6,0,1]
        
        0 1 2 3 4 5 6 7 8 
        
        '''
        
        numSet=set(nums)
        
        ans=0
        
        for num in nums:
            if num not in numSet:
                continue
            #if this is the start of a new sequence 
            if num-1 not in numSet:
                currLen=0
                currNum=num
                while currNum in numSet:
                    numSet.remove(currNum)
                    currLen+=1
                    currNum+=1
                ans=max(ans,currLen)
        
        return ans
                    