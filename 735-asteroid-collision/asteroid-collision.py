class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                while len(stack) > 0 and stack[-1] < abs(ast):
                    stack.pop()
                if len(stack) == 0:
                    ans.append(ast)
                else:
                    if stack[-1] == abs(ast):
                        stack.pop()
        ans += stack
        return ans