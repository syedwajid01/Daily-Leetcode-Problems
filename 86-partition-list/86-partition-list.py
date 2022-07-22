# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessThanXHead=ListNode(-1)
        greaterThanXHead=ListNode(-1)
        lessThanX=lessThanXHead
        greaterThanX=greaterThanXHead
        
        curr=head
        while curr!=None:
            if curr.val<x:
                lessThanX.next=curr
                lessThanX=lessThanX.next
            else:
                greaterThanX.next=curr
                greaterThanX=greaterThanX.next
            curr=curr.next
        
        
        greaterThanX.next=None
        
        lessThanX.next=greaterThanXHead.next
        
        return lessThanXHead.next