import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [(-count, num) for num, count in Counter(nums).items()]
        heapq.heapify(res)

        topk = []
        total = 0
        while res and total < k:
            count, num = heapq.heappop(res)
            topk.append(num)
            total += 1
        
        return topk


        

        