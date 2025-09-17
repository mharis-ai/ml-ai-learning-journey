class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        maximum = nums[0]
        total = 0

        for i in range(n):
            total += nums[i]
            if total > maximum:
                maximum = total
            if total < 0:
                total = 0
                
        return maximum