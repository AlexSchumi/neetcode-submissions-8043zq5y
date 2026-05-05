# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node.val == subRoot.val:
                if self.sameTree(node, subRoot):
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
    
    def sameTree(self, left_root, right_root):
        if not left_root and not right_root:
            return True
        if not left_root or not right_root or left_root.val != right_root.val:
            return False
        
        return self.sameTree(left_root.left, right_root.left) and self.sameTree(left_root.right, right_root.right)
        