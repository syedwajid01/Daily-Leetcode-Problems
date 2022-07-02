class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        '''
        Greedy approach 
        maxArea= max(horizontalDiff*verticalDiff)
        '''
        horizontalCuts.append(h)        
        horizontalCuts.sort()
        maxHorizontalCut=self.getMaxDiff(horizontalCuts)

        
        verticalCuts.append(w)
        verticalCuts.sort()
        maxVerticalCut=self.getMaxDiff(verticalCuts)
        return (maxHorizontalCut*maxVerticalCut)%(10**9+7)
        
    
    def getMaxDiff(self,arr):
        prevCut=0
        maxDiff=float("-inf")
        for i in range(len(arr)):
            currCut=arr[i]
            maxDiff=max(maxDiff,currCut-prevCut)
            prevCut=currCut
        
        return maxDiff
            
        
        