# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        if left==right:
            return head
        
        
        prev=None
        current=head
        for i in range(left-1):
            prev=current
            current=current.next
        
        leftListEnd=prev
        subListEnd=current
        
        subListStart,rightListStart=self.reverse(subListEnd,right-left+1)
        
        if leftListEnd!=None:
            leftListEnd.next=subListStart
        else:
            head=subListStart
        
        subListEnd.next=rightListStart
        
        return head
        
    
    
    def reverse(self,head,length):
        prev=None
        curr=head
        while curr!=None and length>0:
            nextNodePtr=curr.next
            curr.next=prev
            prev=curr
            curr=nextNodePtr
            length-=1
        
        return [prev,curr]
        
        
    
    
        
        
        
        