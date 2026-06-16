# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

# Initialize an empty list to act as your heap
my_heap = []

# Correct way to add an element
heapq.heappush(my_heap, 10)
heapq.heappush(my_heap, 5)
heapq.heappush(my_heap, 20)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        bst_heap = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            heapq.heappush(bst_heap, node.val)
            dfs(node.right)
            return
        dfs(root)
        print(bst_heap)
        return bst_heap[k-1]

        