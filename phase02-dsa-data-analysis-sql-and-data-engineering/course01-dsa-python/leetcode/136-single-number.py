class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result