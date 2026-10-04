class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        max_seq = 1
        cur_seq = 1
        print(nums)
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                cur_seq += 1
                max_seq = max(max_seq, cur_seq)
            elif nums[i] == nums[i-1]:
                continue
            else:
                cur_seq = 1

        return max_seq
            


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_res = 1
        
        for num in nums:
            if (num - 1) not in num_set: 
                cur_res = 0
                while num + cur_res in num_set:
                    cur_res += 1
                    max_res = max(cur_res, max_res)
        return max_res


            


        