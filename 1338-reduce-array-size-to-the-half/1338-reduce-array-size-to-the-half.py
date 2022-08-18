from heapq import *
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrFreq=Counter(arr)
        
        maxHeap=[]
        
        numOfElements=len(arr)
        halfArrLen=len(arr)//2
        
        for num,freq in arrFreq.items():
            heappush(maxHeap,[-freq,num])
        
        count=0
        while numOfElements>halfArrLen:
            freq,_=heappop(maxHeap)
            freq=-freq
            numOfElements-=freq
            count+=1
        
        return count
        
        
        
        
        