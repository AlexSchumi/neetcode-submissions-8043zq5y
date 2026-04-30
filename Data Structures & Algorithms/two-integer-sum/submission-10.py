# brutal force solution
# runtime complexity: O(N^2)
# space complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if nums[i] in res:
                return [res[nums[i]], i]
            else:
                res[remain] = i
        return []
        




        