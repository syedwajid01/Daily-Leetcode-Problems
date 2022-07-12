class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks)<3:
            return False
        max_matchstick=float('-inf')
        total_sum=0
        for i in range(len(matchsticks)):
            max_matchstick=max(max_matchstick,matchsticks[i])
            total_sum+=matchsticks[i]
    
        if (total_sum%4!=0 or max_matchstick> total_sum//4):
            return False
        possible_side=total_sum//4
    
        return self.dfs(0,0,matchsticks,0,possible_side,set())
    
    def dfs(self,index,k,matchsticks,curr_square_length,possible_side,visited):
        if k==3:
            return True
        if curr_square_length==possible_side:
            return self.dfs(0,k+1,matchsticks,0,possible_side,visited)    
        for i in range(index,len(matchsticks)):
            if i not in visited:
                if matchsticks[i]+curr_square_length<=possible_side:
                    visited.add(i)
                    if(self.dfs(i+1,k,matchsticks,matchsticks[i]+curr_square_length,possible_side,visited)):
                        return True
                    visited.remove(i)
        return False
                
                