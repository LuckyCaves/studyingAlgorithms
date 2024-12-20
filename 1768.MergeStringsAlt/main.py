class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        letter1 = 0
        letter2 = 0

        res = ""

        while(letter1 < len(word1) or letter2 < len(word2)):

            if(letter1 < len(word1)):
                res += word1[letter1]
                letter1 += 1

            if(letter2 < len(word2)):
                res += word2[letter2]
                letter2 += 1
        
        return res

