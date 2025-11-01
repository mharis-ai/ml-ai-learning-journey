class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        freq = {}
        
        for i in range(n):
            req = target - nums[i]
            if req in freq:
                return [freq[req],i]
            freq[nums[i]] = i