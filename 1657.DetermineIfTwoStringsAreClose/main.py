class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False

        dictWord1 = Counter(word1)
        dictWord2 = Counter(word2)

        word1Values = sorted(dictWord1.values())
        word2Values = sorted(dictWord2.values())

        return word1Values == word2Values and dictWord1.keys() == dictWord2.keys()