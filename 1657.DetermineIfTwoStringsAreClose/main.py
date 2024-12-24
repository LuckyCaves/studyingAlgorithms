class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False

        dictWord1 = {}
        dictWord2 = {}

        for i in word1:
            if dictWord1.get(i, 0) == 0:
                dictWord1[i] = 1
            else:
                dictWord1[i] += 1
        
        for i in word2:
            if dictWord2.get(i, 0) == 0:
                dictWord2[i] = 1
            else:
                dictWord2[i] += 1
        
        dict3 = {}
        dict4 = {}
        print(dictWord1)
        print(dictWord2)
        for i in dictWord1:
            letter1 = dictWord1.get(i, 0)
            letter2 = dictWord2.get(i, 0)
            if letter1 != letter2:
                if dict4.get(letter1, 0) == 0:
                    dict3[letter1] = i
                else:
                    dict4.pop(letter1)
                if dict3.get(letter2, 0) == 0:
                    dict4[letter2] = i
                else:
                    dict3.pop(letter2)
            
        return len(dict3) + len(dict4) == 0
        