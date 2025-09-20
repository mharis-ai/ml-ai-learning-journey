class Solution:
    def searchRange(self, nums, target: int):
        first = self.lowerbound(nums,target)
        if first == -1:
            return [-1,-1]
        last = self.upperbound(nums,target)
        return[first,last - 1]

    def lowerbound(self,nums,target):
        low = 0
        high = len(nums) - 1
        lb = -1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] >= target:
                high = mid - 1
                if nums[mid] == target:
                    lb = mid
            else:
                low = mid + 1
        return lb

    def upperbound(self,nums,target):
        low = 0
        high = len(nums) - 1
        ub = len(nums)
        while low <= high:
            mid = (low + high)//2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub