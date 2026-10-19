# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []
        
        def dfs(root):
            if not root:
                return 
            results.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        #results = sorted(results)
        heapq.heapify(results)
        return results[k-1]

# Time complexity: O(nlogn)
# Space complexity: O(n)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr[k-1]



