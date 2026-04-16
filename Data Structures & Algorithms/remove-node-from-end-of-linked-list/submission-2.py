# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        total = 0
        while cur:
            next = cur.next
            cur = next
            total += 1
        # get total number and index to remove
        to_remove = total - n

        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head
        #prev.next = cur

        index = 0
        while cur:
            if index == to_remove:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                next = cur.next
                cur = next
            index += 1
        #return head
        return dummy.next
    


        