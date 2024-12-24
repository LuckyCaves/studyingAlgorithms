class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        l, r = 0, k - 1

        vowels = "aeiou"
        maxCount = 0
        count = 0

        for i in range(r + 1):
            if s[i] in vowels:
                count += 1

        while r < len(s) - 1:

            maxCount = max(maxCount, count)

            l += 1
            r += 1
            if s[l - 1] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1

        return max(maxCount, count)