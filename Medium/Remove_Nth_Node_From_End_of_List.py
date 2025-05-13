# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        current=head
        total=1
        while current.next:
            current=current.next
            total+=1
        n=total+1-n
        node=head
        if n==1:
            head=head.next
            return head
        for _ in range(n-2):
            node=node.next
        remove=node.next
        if node.next.next is None:
            node.next=None
            return head
        node.next=node.next.next
        return head
