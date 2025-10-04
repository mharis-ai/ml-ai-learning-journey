class Solution:
    def combinationSum3(self, k: int, n: int):
        result = []

        def backtrack(index, total, subset):
            if total == n and len(subset) == k:
                result.append(subset[:])
                return

            if total > n or len(subset) > k or index > 9:
                return
                
            subset.append(index)
            backtrack(index + 1, total + index, subset)
            subset.pop()

            backtrack(index + 1, total, subset)

        backtrack(1, 0, [])
        return result