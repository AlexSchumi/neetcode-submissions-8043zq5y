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

        def dfs(root, min_val, max_val):
            if not root:
                return True

            cur_val = root.val
            if cur_val >= max_val or cur_val <= min_val: # condition of not valid
                return False
            return dfs(root.left, min_val, cur_val) and dfs(root.right, cur_val, max_val)

        return dfs(root, -float("inf"), float("inf"))

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            
            if node.left:
                q.append((node.left, left, node.val))

            if node.right:
                q.append((node.right, node.val, right))
            
        return True
        