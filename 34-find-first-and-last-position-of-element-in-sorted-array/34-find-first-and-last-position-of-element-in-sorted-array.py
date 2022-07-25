class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def getFirstElement():
            lo,hi=0,len(nums)
            
            while lo<hi:
                mid=lo+(hi-lo)//2
                if nums[mid]<target:
                    lo=mid+1
                else:
                    hi=mid
            
            return lo
        
        def getLastElement():
            lo,hi=0,len(nums)
            
            while lo<hi:
                mid=lo+(hi-lo)//2
                
                if nums[mid]>target:
                    hi=mid
                else:
                    lo=mid+1
            
            return lo
        
        first,last=getFirstElement(),getLastElement()
        print(first,last)
        last-=1
        return [first,last] if first<=last else [-1,-1]
        
        
        
        
    
            
            
        