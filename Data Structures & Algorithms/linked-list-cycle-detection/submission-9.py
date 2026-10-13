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





        