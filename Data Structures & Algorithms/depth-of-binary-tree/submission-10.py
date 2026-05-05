from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS solution -> traverse each level fully (n node)
# runtime: O(N)
# space: O(W)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        res = 0

        while queue:
            n_node = len(queue)
            for i in range(n_node):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res

# DFS Solution
# runtime: 
# space: 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stacks = [(root, 1)]
        max_depth = 1

        while stacks:
            n_node = len(stacks)
            node, level = stacks.pop()
            res = level
            max_depth = max(res, max_depth)
            if node.left:
                stacks.append((node.left, level+1))
                max_depth = max(level + 1, max_depth)
            if node.right:
                stacks.append((node.right, level+1))
                max_depth = max(level + 1, max_depth)
        return max_depth


        