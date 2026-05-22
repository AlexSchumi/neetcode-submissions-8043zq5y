# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        order_list = {}
        node = head
        idx = 0
        while node: # store node in the list
            order_list[idx] = node
            node = node.next
            idx += 1
        length = len(order_list)
        
        node = head
        for i in range(length-1):
            if (i + 1) % 2 == 0: # next is on even index;
                next_index = (i + 1) // 2
            else:
                next_index = length - 1 - i // 2
            # get corresponding order by this index
            next_node = order_list[next_index]
            node.next = next_node
            node = next_node
            # Why it is stuck in endless loop?

        node.next = None



        
        
        