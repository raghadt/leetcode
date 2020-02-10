# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# --------------------- Iteretivly -----------------
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        head=prev
        return head
            
# 1 -> 2 -> 3
# 3 -> 2 -> 1


