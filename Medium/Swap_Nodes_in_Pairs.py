
# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        res=head.next
        current=head
        while current.next:
            sec=current.next
            current.next=current.next.next
            sec.next=current
            if current.next is not None:
                if current.next.next is not None:
                    mid=current.next
                    current.next=current.next.next
                    current=mid
                else:
                    current=current.next
            else:
                break
        return res

