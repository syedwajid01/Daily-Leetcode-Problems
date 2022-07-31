class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.arr=nums
        n=self.n
        powerOf2=1
        space=0
        for i in range(n):
            powerOf2*=2
            if powerOf2>=(2*n-1):
                space=powerOf2
                break
       
        self.segmentTree=[0]*(space)
        self.constructSegmentTree(self.segmentTree,nums,0,0,self.n-1)
        
    def constructSegmentTree(self,segmentTree,arr,index,left,right):
        if left==right:
            segmentTree[index]=arr[left]
            return arr[left]
        mid=(left+right)//2
        leftPartitionSum=self.constructSegmentTree(segmentTree,arr,2*index+1,left,mid)
        rightPartitionSum=self.constructSegmentTree(segmentTree,arr,2*index+2,mid+1,right)
        segmentTree[index]=leftPartitionSum+rightPartitionSum
        return segmentTree[index]

    def update(self, index: int, val: int) -> None:
        diff=val-self.arr[index]
        self.arr[index]=val
        self.updateSegmentTree(self.segmentTree,0,0,self.n-1,index,diff)
    
    
    def updateSegmentTree(self,segmentTree,stIndex,left,right,position,diff):
        if not left<=position<=right:
            return
        segmentTree[stIndex]+=diff
        if left!=right:
            mid=(left+right)//2
            self.updateSegmentTree(segmentTree,2*stIndex+1,left,mid,position,diff)
            self.updateSegmentTree(segmentTree,2*stIndex+2,mid+1,right,position,diff)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(self.segmentTree,0,0,self.n-1,left,right)
    
    def getSum(self,segmentTree,stIndex,segmentTreeleft,segmentTreeright,l,r):
        #total overlap
        if segmentTreeleft>=l and r>=segmentTreeright:
            return segmentTree[stIndex]
        
        #No overlap
        if r<segmentTreeleft or l>segmentTreeright:
            return 0
        
        #partial overlap
        mid=(segmentTreeleft+segmentTreeright)//2
        leftPartitionSum=self.getSum(segmentTree,2*stIndex+1,segmentTreeleft,mid,l,r)
        rightPartitionSum=self.getSum(segmentTree,2*stIndex+2,mid+1,segmentTreeright,l,r)
        return leftPartitionSum+rightPartitionSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)