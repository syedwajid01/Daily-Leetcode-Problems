class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        [1,2,5]
        11 
        
        1 ->  amount =11 
        
        n-1 
        
        amount==0:
        return 0
        
        n==0 
        return float("inf")
        
        '''
        n=len(coins)
        dp=[[-1 for i in range(amount+1)] for j in range(n+1)]
        
        def getMinCoins(coins,amount,n):
            if amount==0:
                return 0
            if n==0:
                return float("inf")
            if dp[n][amount]!=-1:
                return dp[n][amount]
            #we have two options 
            #select this coin
            if coins[n-1]<=amount:
                dp[n][amount] = min(1+getMinCoins(coins,amount-coins[n-1],n),getMinCoins(coins,amount,n-1))
            else:
                dp[n][amount] = getMinCoins(coins,amount,n-1)
            
            return dp[n][amount]
        
        ans= getMinCoins(coins,amount,n)
        
        return ans if ans!=float("inf") else -1
        