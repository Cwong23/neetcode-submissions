class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack:
                stack.append(a)
                continue
            temp = a
            # only hits when left is positive and right is negative
            while stack and stack[-1] > 0 and a < 0:
                left = stack.pop()
                if left > -temp:
                    stack.append(left)
                    temp = 0
                    break
                elif left == -temp:
                    temp = 0
                    break
            if temp == a:
                stack.append(a)


        return stack