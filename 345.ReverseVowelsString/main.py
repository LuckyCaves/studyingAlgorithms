class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        i = 0
        j = len(s) - 1

        while(i < j):

            if not(s[i].lower() in vowels):
                i += 1
                continue
            
            if not(s[j].lower() in vowels):
                j -= 1
                continue

            aux = s[i]
            s[i] = s[j]
            s[j] = aux
            # s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)
