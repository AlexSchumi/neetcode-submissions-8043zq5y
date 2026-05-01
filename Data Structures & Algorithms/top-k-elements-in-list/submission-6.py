class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        # 注意：多了个 key=
        sorted_count = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

        res = []
        for key, value in sorted_count:
            res.append(key)
        return res[:k]
        