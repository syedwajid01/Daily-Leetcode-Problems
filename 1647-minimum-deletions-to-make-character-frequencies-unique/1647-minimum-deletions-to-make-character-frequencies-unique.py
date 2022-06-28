class Solution:
    def minDeletions(self, s: str) -> int:
        charFreqMap=Counter(s)
        
        #greedy approach 
        #if we found a duplicate freq and we want to replace it with other freq
        #which is unique or not already present 
        #so for the given freq if we are able to know max allowed freq then we can replace it with that 
        
        freqCount=[0]*26
        
        for letter in s:
            freqCount[ord(letter)-ord('a')]+=1
        
        freqCount.sort(reverse=True)
        
        maxAllowedFreq=len(s)
        ans=0
        
        for freq in freqCount:
            if freq>maxAllowedFreq:
                ans+=freq-maxAllowedFreq
                freq=maxAllowedFreq
            
            maxAllowedFreq=max(0,freq-1)
        
        return ans
            
                 
    
        