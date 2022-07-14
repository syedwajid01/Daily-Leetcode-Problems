# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap={}
        
        for i in range(len(inorder)):
            inorderMap[inorder[i]]=i
        
        self.preIdx=0
        return self.buildTreeHelper(preorder,inorderMap,0,len(preorder))
    
    
    def buildTreeHelper(self,preorder,inorderMap,left,right):
        if left>right or self.preIdx>=len(preorder):
            return None
        num=preorder[self.preIdx]
        root=TreeNode(num)
        self.preIdx+=1
        
        rootIdx=inorderMap[num]
        root.left=self.buildTreeHelper(preorder,inorderMap,left,rootIdx-1)
        root.right=self.buildTreeHelper(preorder,inorderMap,rootIdx+1,right)
        
        return root
    
        