class Solution:
    def combinationSum(self, candidates, target: int):
        result = []
        self.helper(candidates, target, result, [], 0, 0)
        return result

    def helper(self, candidates, target, result, subset, index, total):
        if total == target:
            result.append(subset.copy())
            return

        if total > target or index >= len(candidates):
            return

        subset.append(candidates[index])
        self.helper(candidates, target, result, subset, index, total + candidates[index])

        subset.pop()
        self.helper(candidates, target, result, subset, index + 1, total)