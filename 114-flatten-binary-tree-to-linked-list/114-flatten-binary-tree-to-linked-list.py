# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prevNode=None
        self.preorder(root)
        
        return root
    
    
    def preorder(self,root):
        if root is None:
            return root
        
        temp=root.right
        if self.prevNode:
            self.prevNode.right=root
        
        self.prevNode=root

        self.preorder(root.left)
        self.preorder(temp)
        
        root.left=None
        