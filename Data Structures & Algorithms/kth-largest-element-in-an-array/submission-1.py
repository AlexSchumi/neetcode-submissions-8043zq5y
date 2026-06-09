import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -1 * num)
        
        for i in range(k):
            res = heapq.heappop(max_heap)
        
        return -1 * res
        

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. 先把前 k 个数放进最小堆
        min_heap = nums[:k]
        heapq.heapify(min_heap) # O(k) 原地建堆
        
        # 2. 从第 k+1 个数开始遍历
        for num in nums[k:]:
            # 如果当前的数比堆里最小的还大，说明它有资格进入前 k 名
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num) # 弹出堆顶并压入新数，比单独 pop + push 更高效
                
        # 3. 遍历结束，堆顶就是前 k 名里最小的那个，即第 k 大
        return min_heap[0]