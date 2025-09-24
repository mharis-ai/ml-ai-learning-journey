class Solution:
    def maxFrequencyElements(self, nums) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        maximum = max(freq.values())
        total = 0
        for v in freq.values():
            if v == maximum:
                total += v
        return total