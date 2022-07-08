class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.memo={}
        
        ans=self.findMinCost(houses,cost,target,0,0,0)
        
        return ans if ans!=float("inf") else -1
       
    
    def findMinCost(self,houses,cost,target,currIdx,prevColor,neighborhoodCount):
        if currIdx==len(houses):
            return 0 if neighborhoodCount==target else float("inf")
        
        if neighborhoodCount > target:
            return float("inf")
        
        key=(currIdx,prevColor,neighborhoodCount)
        
        if key in self.memo:
            return self.memo[key]
        
        #now we can paint the house at idx with one of the colors
        minimumCost=float("inf")
        
        #if house is already colored then update the currgroups accordingly
        if houses[currIdx]!=0:
            newNeighborhoodCount=neighborhoodCount + (prevColor!=houses[currIdx])
            minimumCost=self.findMinCost(houses,cost,target,currIdx+1,houses[currIdx],newNeighborhoodCount)
            
        else:
            totalColors=len(cost[0])
            for color in range(1,totalColors+1):
                newNeighborhoodCount=neighborhoodCount + (prevColor!=color)
                currCost= cost[currIdx][color-1]+ self.findMinCost(houses,cost,target,currIdx+1,color,newNeighborhoodCount)
                minimumCost=min(minimumCost,currCost)
        
        self.memo[key]= minimumCost
        return self.memo[key]

            
        
            
        