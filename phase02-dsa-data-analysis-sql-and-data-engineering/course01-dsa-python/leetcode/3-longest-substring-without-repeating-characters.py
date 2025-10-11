class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, maximum = 0, 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maximum = max(maximum, right - left + 1)
        return maximum