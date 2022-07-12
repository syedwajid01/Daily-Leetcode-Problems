class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used=[False]*len(nums)
        self.ans=[]
        self.getAllPermute(nums,[],used)
        return self.ans
        
    
    def getAllPermute(self,nums,curr,used):
        if len(curr)==len(nums):
            self.ans.append(curr[:])
            return 
        
        for i in range(len(nums)):
            if not used[i]:
                curr.append(nums[i])
                used[i]=True
                self.getAllPermute(nums,curr,used)
                used[i]=False
                curr.pop()
    
        