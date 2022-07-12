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
        
        #if amount ==0 then num of coins =0
        for i in range(n+1):
            dp[i][0]=0
        
        #if n==0 and amount>0 then coins= float("inf")
        for i in range(1,amount+1):
            dp[0][i]=float("inf")
        
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        
        ans=dp[n][amount]
        return ans if ans!=float("inf") else -1
        
      
        