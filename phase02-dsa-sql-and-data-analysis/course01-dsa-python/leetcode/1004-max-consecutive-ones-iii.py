class Solution:
    def longestOnes(self, nums, k: int) -> int:
        left, maximum, zeroes = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            if zeroes <= k:
                maximum = max(maximum, right - left + 1)
                
        return maximum