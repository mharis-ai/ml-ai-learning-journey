class Solution:
    def combinationSum2(self, candidates, target: int):
        result = []
        candidates.sort()

        def backtrack(index, total, subset):
            if total == target:
                result.append(subset[:])
                return

            if total > target or index >= len(candidates):
                return
            
            subset.append(candidates[index])
            backtrack(index + 1, total + candidates[index], subset)
            subset.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            
            backtrack(index + 1, total, subset)
        
        backtrack(0, 0, [])
        return result