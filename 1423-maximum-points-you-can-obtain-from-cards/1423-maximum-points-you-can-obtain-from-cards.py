class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        totalSum=sum(cardPoints)
        if n==k:
            return totalSum
        
        windowSize=n-k
        windowStart=0
        windowSum=0
        maxPoints=float("-inf")
        
        for windowEnd in range(n):
            windowSum+=cardPoints[windowEnd]
            
            if windowEnd-windowStart+1>=windowSize:
                maxPoints=max(maxPoints,totalSum-windowSum)
                windowSum-=cardPoints[windowStart]
                windowStart+=1
        
        return maxPoints
                
            
        
        
        
            
        
        