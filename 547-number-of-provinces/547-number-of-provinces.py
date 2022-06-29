class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent=[i for i in range(len(isConnected))]
        
        def find(p):
            root=p
            while root!=parent[root]:
                root=parent[root]
            
            while p!=root:
                nextParent=parent[p]
                parent[p]=root
                p=nextParent
                
            return root
        
        def union(p,q):
            parent[p]=q
        
        
        for i in range(len(isConnected)):
            for j in range(i,len(isConnected)):
                root1=find(i)
                root2=find(j)
                if(isConnected[i][j] and root1!=root2):
                    union(root1,root2)
                    
        numOfConnectedComponents=len(set(find(i) for i in range(len(isConnected))))
        
        return numOfConnectedComponents 
                    
                
        
        
                