# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        while list1 and list2:
            if list1.val>=list2.val:
                tail.next=list2
                tail=list2
                list2=list2.next
            else:
                tail.next=list1
                tail=list1
                list1=list1.next
        if not list1:
            tail.next=list2
        else:
            tail.next=list1
        return dummy.next
