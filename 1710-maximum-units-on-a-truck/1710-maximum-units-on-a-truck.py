class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        
        maxUnits=0
        
        for numOfBoxes,numOfUnitsPerBox in boxTypes:
            if numOfBoxes<truckSize:
                truckSize-=numOfBoxes
                maxUnits+=numOfBoxes*numOfUnitsPerBox
            else:
                maxUnits+=truckSize*numOfUnitsPerBox
                return maxUnits
        
        return maxUnits
        
        