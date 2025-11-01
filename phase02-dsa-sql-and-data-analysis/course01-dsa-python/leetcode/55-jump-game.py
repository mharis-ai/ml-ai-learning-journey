class Solution:
    def canJump(self, nums) -> bool:
        maximum = 0
        for i in range(len(nums)):
            if i > maximum:
                return False
            maximum = max(nums[i] + i, maximum)
        return True