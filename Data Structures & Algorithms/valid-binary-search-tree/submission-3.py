# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, cur_max, cur_min):
            if not node:
                return True
            if node.val >= cur_max:
                return False
            if node.val <= cur_min:
                return False
            
            return dfs(node.left, node.val, cur_min) and dfs(node.right, cur_max, node.val)
        
        return dfs(root.left, root.val, -float('inf')) and dfs(root.right, float('inf'), root.val)


        