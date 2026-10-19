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

        results = sorted(results)
        
        print(results)
        return results[k-1]


