class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #minimum number of steps to reach 404 i.e last idx 
        
        #100  - 100  
        # |      |
        #-23 -23 |
        #     /
        #404 --  |
        # | 
        #23 - 23 -23 
        
        #so for given index 
        #we have three choices
        #either we can go from index to index+1 or index -1 or any index which has arr[i]
        
        n=len(arr)
        
        if n<=1:
            return 0
        
        
        curs=[0] #store current layer
        visited={0}
        steps=0
        
        graph=collections.defaultdict(list)
    
        for index,num in enumerate(arr):
            graph[num].append(index)
        
        #if curr layer exist
        while curs:
            
            nex=[]
            
            #iterate the layer
            for node in curs:
                #check if reach end
                if node==n-1:
                    return steps
                
                #check  same value
                for nei in graph[arr[node]]:
                    if nei not in visited:
                        visited.add(nei)
                        nex.append(nei)
                
                #clear the list to prevent redundant search 
                #very imp 
                '''
                Without the step to clear the precomputed dictionary, the normal BFS will TLE.
                One case that would have TLEed is [7,7,7,7,...7, 2].
                Without clearing the precomputed dictionary, each 7 need to recheck the indexes of all other 7s.
                Code to clear the precomputed dictionary.
                '''
                graph[arr[node]].clear()
                
                #check neighbors
                for nei in [node+1,node-1]:
                    if( 0<=nei<n) and (nei not in visited):
                        visited.add(nei)
                        nex.append(nei)
            steps+=1
            curs=nex
        
        return -1
                        
                
            
        
        return len(arr)
                    
            
            
        
            
            
        
        
        
        