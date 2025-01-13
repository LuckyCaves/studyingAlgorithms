class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = 'aeiou'

        newWords = [0] * (len(words) + 1)
        
        for i in range(len(words)):
            newWords[i + 1] = newWords[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                newWords[i + 1] += 1

        res = []

        for l, r in queries:
            res.append(newWords[r + 1] - newWords[l])

        return res
