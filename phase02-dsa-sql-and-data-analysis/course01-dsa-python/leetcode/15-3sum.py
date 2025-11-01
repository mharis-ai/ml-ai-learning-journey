class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left<right:
                third = nums[i]+nums[left]+nums[right]
                if third > 0:
                    right -= 1
                elif third < 0:
                    left += 1
                else:
                    temp = [nums[i],nums[left],nums[right]]
                    result.append(temp)

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                
                    left += 1
                    right -= 1
        return result  