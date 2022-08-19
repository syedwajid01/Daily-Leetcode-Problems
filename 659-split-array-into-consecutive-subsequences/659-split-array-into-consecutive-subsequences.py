from heapq import *
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap=[]
        #heap interval = [end,length,start]
        for num in nums:
            while heap and heap[0][0]+1<num:
                _,length,_=heappop(heap)
                if length<3:
                    return False
            if len(heap)==0 or (heap and heap[0][0]==num):
                heappush(heap,[num,1,num])
            else:
                end,length,start=heappop(heap)
                heappush(heap,[num,length+1,start])
        
        while heap:
            _,length,_=heappop(heap)
            if length<3:
                return False
        
        return True
                
        
        
        
        
        
        