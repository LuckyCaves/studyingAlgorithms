class Solution:
    def reverseWords(self, s: str) -> str:
        
        sentence = s.split(" ")

        res = ""

        for i in range(len(sentence) - 1, -1, -1):
            if sentence[i] != '':
                res += sentence[i] + ' '
        return res[:-1]