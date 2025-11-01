class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        k = 0
        for j in range(n):
            if nums[k]!=nums[j]:
                nums[k+1],nums[j] = nums[j],nums[k+1]
                k+=1
        return k+1