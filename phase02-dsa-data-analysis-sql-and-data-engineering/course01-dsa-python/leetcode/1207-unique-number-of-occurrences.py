class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        freq = {}
        unique = set()
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        for i in freq.values():
            if i in unique:
                return False
            unique.add(i)
        return True