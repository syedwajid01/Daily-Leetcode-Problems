class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #recursive brute force appraoch will take O(n! * n) time complexity 
        #dynamic programming appraoch 
        #this question only has bottom up dp solution to it
        #it can't be solved using top down dp(memorization + recursion)
        
        #Appraoch : divide and conquer  + dynamic programming
        #intuition:
        #If I bust ith balloon , I get coins nums[i-1]*nums[i]*nums[i+1]
        #in the given array padd 1 on both sides 
        #[1, 3,1,5,8, 1 ]
        #remove any zeros if present because zero's will not give you any coins 
        #and now as we can see if we bust first balloon 3 we already know that its left side will be 1 and right side is 2 
        #so left side 1 is already defined and fixed
        #and same for last balloon 8, right side is fixed 1 
        #no matter which balloon you bust these left and right are fixed for first and last balloons
        #so if we have clear fixed boundries of left and right for the given balloons 
        #then we can easily solve the problem
        #we can have clear boundires if we know that given balloon is the last balloon to be bust 
        #to find max coins in the window 1 to N 
        #we need to check what will be the answer if 3 is the last balloon to be bust 
        #it will be 0+ 1*3*1 + dp[2:]
        #so bascially start from the last balloon to bust
        
        
        nums=[1]+ [i for i in nums if i>0] + [1]
        print(nums)
        n=len(nums)
        #ans = dp[1][n]
        dp=[[0]*n for i in range(n)]
        
        #n value without zeros and padded 1's
        n-=2
        #for every window size (1 to n)
        for windowSize in range(1,n+1):
            #for windowSize one left is from 1 to n
            #for 2 it will be from 1 to n-1 and so on
            #for 1 - we need to go from 1 to n-1+2 => 1 to n+1  (because in python range is from [1,n+1) )
            for left in range(1,n-windowSize+2):
                right=left+windowSize-1
                for i in range(left,right+1):
                    dp[left][right]=max(dp[left][right], dp[left][i-1] + dp[i+1][right] + nums[left-1]*nums[i]*nums[right+1])
        
        return dp[1][n]
                    
            
        