class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if a <= mass:
                mass += a
            else: return False
        return True

        # stack = []
        # for a in asteroids:
        #     stack.append(a)
        #     while stack and stack[-1] <= mass:
        #         mass += stack.pop()

        # return not stack