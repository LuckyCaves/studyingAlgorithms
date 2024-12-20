class Solution:
    def reverseWords(self, s: str) -> str:
        
        sentence = s.strip().split()
        sentence.reverse()
        
        return " ".join(sentence)