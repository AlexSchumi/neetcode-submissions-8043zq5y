# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")
        def dfs(root):
            nonlocal res
            if not root:
                return 
            left = self.getMax(root.left)
            right = self.getMax(root.right)
            res = max(res, root.val + left + right)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    def getMax(self, node):
        if not node:
            return 0
        left = self.getMax(node.left)
        right = self.getMax(node.right)
        path = root.val + max(left, right)
        return max(0, path)



class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum with split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # return maximum without splits
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            res[0] = max(res[0], node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)

        dfs(root)

        return res[0]
            
        