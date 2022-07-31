class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.n=len(nums)
        n=self.n
        powersOf2=1
        space=n
        for i in range(n):
            powersOf2*=2
            if powersOf2>=(2*n-1):
                space=powersOf2
                break
        
        self.segmentTree=[0 for _ in range(space)]
        self.buildSegmentTree(self.segmentTree,0,0,n-1)
    
    def buildSegmentTree(self,st,index,left,right):
        if left==right:
            st[index]=self.nums[left]
            return self.nums[left]
        
        mid=(left+right)//2
        leftSum=self.buildSegmentTree(st,2*index+1,left,mid)
        rightSum=self.buildSegmentTree(st,2*index+2,mid+1,right)
        st[index]=leftSum+rightSum
        return st[index]
        
        

    def update(self, index: int, val: int) -> None:
        difference=val-self.nums[index]
        self.nums[index]=val
        self.updateSegTree(self.segmentTree,0,0,self.n-1,index,difference)
    
    def updateSegTree(self,st,index,stLeft,stRight,pos,diff):
        if pos < stLeft or pos > stRight:
            return 
        st[index]+=diff
        if stLeft!=stRight:
            mid=(stLeft+stRight)//2
            self.updateSegTree(st,2*index+1,stLeft,mid,pos,diff)
            self.updateSegTree(st,2*index+2,mid+1,stRight,pos,diff)

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(self.segmentTree,0,0,self.n-1,left,right)
    
    
    def getSum(self,st,index,stLeft,stRight,left,right):
        #total overlap 
        if stLeft>=left and stRight<=right:
            return st[index]
        
        #no overlap 
        if stRight<left or stLeft>right:
            return 0
        
        #partial overlap 
        mid=(stLeft+stRight)//2
        return self.getSum(st,2*index+1,stLeft,mid,left,right) + self.getSum(st,2*index+2,mid+1,stRight,left,right)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)