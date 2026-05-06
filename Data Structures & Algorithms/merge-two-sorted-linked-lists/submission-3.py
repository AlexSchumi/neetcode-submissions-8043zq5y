# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        head = ListNode(-1)
        curnode = head

        while node1 and node2:
            if node1.val <= node2.val:
                curnode.next = node1
                node1 = node1.next
            else:
                curnode.next = node2
                node2 = node2.next
            curnode = curnode.next

        if node1:
            curnode.next = node1
        if node2:
            curnode.next = node2
        return head.next

        