class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        left, right, count = 0, 0, 0
            
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                left += 1
                right += 1
                count += 1
            else:
                right +=1

        return count