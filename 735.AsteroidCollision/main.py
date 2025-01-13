class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        s = []

        i = 0

        while i < len(asteroids):
            if asteroids[i] > 0:
                s.append(asteroids[i])
                asteroids.pop(i)
            elif asteroids[i] < 0 and  len(s) > 0 and s[-1] > 0:
                top = s.pop()
                if top == abs(asteroids[i]):
                    asteroids.pop(i)
                elif top > abs(asteroids[i]):
                    asteroids.pop(i)
                    s.append(top)
            else:
                s.append(asteroids[i])
                i += 1
            
        return s