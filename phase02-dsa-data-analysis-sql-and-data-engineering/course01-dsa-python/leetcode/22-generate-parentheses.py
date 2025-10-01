class Solution:
    def generateParenthesis(self, n: int):
        result = []
        paranthesis = []
        self.helper(n, 0, 0, paranthesis, result)
        return result

    def helper(self, n, index, total, paranthesis, result):
        if total > n or total < 0:
            return
    
        elif index >= n * 2:
            if total == 0:
                result.append("".join(paranthesis))
            return

        paranthesis.append("(")
        self.helper(n, index + 1, total + 1, paranthesis, result)
        paranthesis.pop()

        paranthesis.append(")")
        self.helper(n, index + 1, total - 1, paranthesis, result)
        paranthesis.pop()