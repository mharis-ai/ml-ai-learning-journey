class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        result = [-1] * n

        for i in range((2*n) - 1, -1, -1):
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()
            if i < n and stack:
                result[i] = stack[-1]
            stack.append(nums[i % n])

        return result