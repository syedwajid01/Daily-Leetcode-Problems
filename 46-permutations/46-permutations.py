class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        self.getAllPermute(0,nums)
        return self.ans
        
    
    def getAllPermute(self,idx,nums):
        if idx==len(nums):
            self.ans.append(nums[:])
            return 
        
        for j in range(idx,len(nums)):
            self.swap(idx,j,nums)
            self.getAllPermute(idx+1,nums)
            self.swap(idx,j,nums)
    
    
    def swap(self,i,j,nums):
        nums[i],nums[j]=nums[j],nums[i]
            
        