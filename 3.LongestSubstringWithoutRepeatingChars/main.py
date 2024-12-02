class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count = 0
        p1 = -1
        dict = {}

        for i, j in enumerate(s):

            p1 = max(p1, dict.get(j, -1))
            count = max(i - p1, count)
            dict[j] = i

        return count



s = "aab"

print(Solution.lengthOfLongestSubstring(Solution, s))