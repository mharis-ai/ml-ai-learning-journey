class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)

        current = sum(cardPoints[:k])
        maximum = current
        
        for i in range(1, k + 1):
            current += cardPoints[-i] - cardPoints[k - i] 
            maximum = max(current, maximum)
        return maximum