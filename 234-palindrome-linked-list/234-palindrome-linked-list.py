# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #reverse the second half 
        #first go to middle 
        fast,slow=head,head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        
        #linked can be odd or even length 
        #so for even length linked list fast will become None
        #and for odd length linked list fast will point to tail 
        
        if fast:
            prev=slow
            slow=slow.next
        
        prev.next=None
        #reverse the linkedlist from slow to end
        prev=None
        q=slow
        
        while q!=None:
            temp=q.next
            q.next=prev
            prev=q
            q=temp
        
        first=head
        second=prev
        
        while first and second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        
            
        return True
        
        
        #1 2 2 1
        