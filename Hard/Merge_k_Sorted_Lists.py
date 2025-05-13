# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst=[]
        if len(lists)==0:
            return None
        else:
            for i in range(len(lists)):
                while lists[i]:
                    lst.append(lists[i].val)
                    lists[i]=lists[i].next
            lst.sort()
            lst.reverse()
            current=ListNode()
            head=current
            while lst:
                node=ListNode(lst.pop())
                head.next=node
                head=node
            return current.next
