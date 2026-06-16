# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS Solution!!!!
import heapq
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
        return bst_heap[k-1]

from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        bst_heap = []
        queue = []
        queue.append(root)
        while queue:
            cur_level = len(queue)
            for i in range(cur_level):
                node = queue.pop(0)
                heapq.heappush(bst_heap, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return bst_heap[k-1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            # 1. 顺着左子树一路扎到底（因为越往左数字越小）
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. 弹出当前最左（最小）的节点
            curr = stack.pop()
            
            # 3. 计数：每弹出一个，说明我们捞到了一个更小的数
            k -= 1
            if k == 0:
                return curr.val  # 🌟 找到了！后面的百万节点碰都不用碰，直接下班
                
            # 4. 转向右子树
            curr = curr.right


        