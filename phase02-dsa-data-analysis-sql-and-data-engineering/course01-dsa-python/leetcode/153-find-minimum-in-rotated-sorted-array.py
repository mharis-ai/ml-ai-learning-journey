class Solution:
    def findMin(self, nums) -> int:
        low, high = 0, len(nums) - 1
        minimum = float("inf")

        while low <= high: 
            mid = (low + high)//2
            if nums[low] <= nums[mid]:
                if nums[low] < minimum:
                    minimum = nums[low]
                low = mid + 1

            elif nums[mid] <= nums[high]:
                if nums[mid] < minimum:
                    minimum = nums[mid]
                high = mid - 1

        return minimum