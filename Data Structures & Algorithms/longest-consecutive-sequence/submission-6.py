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
            





        