# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q: # if it is None node, return None
            return None
        if (max(p.val, q.val) < root.val): # if maximum is less than root, then LCA is in the left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val): # otherwise, LCA is on the right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        else: # otherwise, it is the root
            return root


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root



        