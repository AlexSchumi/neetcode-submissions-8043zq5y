# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # save dictionary of index -> node
        nodes = {}
        idx = 0
        curr = head
        # save node in dictionary to know the index
        while curr:
            nodes[idx] = curr
            idx += 1
            curr = curr.next

        new_head = ListNode(0)
        curr = new_head

        for i in range(idx):
            if i % 2 == 0:
                curr.next = nodes[i//2]
                curr = curr.next
            else:
                curr.next = nodes[idx-(i+1)//2]
                curr = curr.next
        curr.next = None
        #return new_head.next



        



            

        
        