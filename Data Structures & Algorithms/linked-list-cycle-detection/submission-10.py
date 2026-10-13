
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        cur = head

        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        