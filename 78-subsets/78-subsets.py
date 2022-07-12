class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #can be done using bfs 
        ans=[[]]
        for num in nums:
            size=len(ans)
            for i in range(size):
                newSubset=ans[i]+[num]
                ans.append(newSubset)
        
        return ans
            
        