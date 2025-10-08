class Solution:
    def asteroidCollision(self, asteroids):
        n = len(asteroids)
        stack = []

        for i in range(n):
            if asteroids[i] < 0:
                while stack and abs(asteroids[i]) > stack[-1] and stack[-1] > 0:
                    stack.pop()

                if stack and abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroids[i])

            else:
                stack.append(asteroids[i])

        return stack