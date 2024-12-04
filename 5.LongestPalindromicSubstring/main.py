class Solution:
    def longestPalindrome(self, s: str) -> str:

        def recursive(s, l, r):
            
            while l >=0 and r < len(s) and s[l] == s[r]:
                r -= 1
                l += 1
            
            return r - l -1
    
        p1 = 0
        p2 = 0
        for i in range(len(s)):
            

        return s2

s = "aacabdkacaa"

print(Solution.longestPalindrome(Solution, s))
