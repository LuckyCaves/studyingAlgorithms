class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        len1 = len(str1)
        len2 = len(str2)

        pos = 0

        for i in range(min(len1, len2), 0, -1):

            if len1 % i and len2 % i:
                continue
            
            n1 = len1 // i
            n2 = len2 // i
            prefix = str1[:i]

            if n1 * prefix == str1 and n2 * prefix == str2:
                return str1[:i]

        return ""
        