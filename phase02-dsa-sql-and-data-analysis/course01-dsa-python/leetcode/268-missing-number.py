class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        result = 0
        result1 = 0
        for i in range(n+1):
            result+=i
        for i in range(n):
            result1+=nums[i]
        return result - result1