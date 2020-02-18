#21. Merge Two Sorted Lists 

# https://leetcode.com/problems/merge-two-sorted-lists/

#O(n+m)

l1= ListNode([1,2,4])
l2 = ListNode([1,3,4])
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2