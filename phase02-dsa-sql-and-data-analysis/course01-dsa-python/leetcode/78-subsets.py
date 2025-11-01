class Solution:
    def subsets(self, nums):
        result = []
        self.recursive_tree(nums, result, 0, [])
        return result

    def recursive_tree(self, nums, result, index, subset):
        if index >= len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[index])
        self.recursive_tree(nums, result, index + 1, subset)
        subset.pop()
        self.recursive_tree(nums, result, index + 1, subset)