from heapq import *
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
       
        stations.append([target,0])
        
        heap=[]
        
        currentFuel=startFuel
        count=0
        prevPos=0
        for i in range(len(stations)):
            currPos,fuel=stations[i]
            distanceTravelled=currPos-prevPos
            
            #if currentFuel is less than distance travelled
            #we need to refuel at one of the previous gas stations
            #we go greedy and update from the gasstations with max fuels so thats we get min count
            #we keep on doing this until we have enough fuel to reach this station
            while heap and currentFuel<distanceTravelled:
                currentFuel+=(-1*heappop(heap))
                count+=1
            
            if currentFuel<distanceTravelled:
                return -1
    
            heappush(heap,-fuel)
            currentFuel-=distanceTravelled
            prevPos=currPos
        
        
        return count
                
            
            
        