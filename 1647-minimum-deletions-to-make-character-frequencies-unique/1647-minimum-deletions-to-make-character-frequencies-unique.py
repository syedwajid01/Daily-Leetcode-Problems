from heapq import *
class Solution:
    def minDeletions(self, s: str) -> int:
        '''
        
        a:2
        b:1 
        
        min number of string we need to remove 
        
        3 3 2 2 1 1
        
        do minimum number of deleteion to make all the numbers unique 
        
        3:2
        2:2
        1:1
         
        a:3
        b:3
        c:2
        
        3:1
        
        2:1
        
        1:1
        
        
        all are unique 
        
        '''
        charFreq=Counter(s)
        freqMap={}
        
        for _,freq in charFreq.items():
            freqMap[freq]=freqMap.get(freq,0)+1
        
        print(freqMap)
        
        heap=[]
        
        for freq,count in freqMap.items():
            if count>1:
                heappush(heap,[freq,count])
        
        ans=0
        while heap:
            freq,count=heappop(heap)
            
            while count!=1:
                count-=1
                temp=freq
                while temp!=0:
                    temp-=1
                    ans+=1
                    if temp not in freqMap:
                        freqMap[temp]=1
                        break
            freqMap[freq]=1
        print(freqMap)
        return ans
            
        
        
        