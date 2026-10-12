# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur, next_node = head, head.next
        while next_node:
            prev_next = next_node.next
            next_node.next = cur
            cur = next_node
            next_node = prev_next
        return next_node

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next  # 1. Save next node
            curr.next = prev  # 2. Reverse pointer
            prev = curr      # 3. Step prev forward
            curr = nxt       # 4. Step curr forward

        return prev  # prev is at the new head



            
        