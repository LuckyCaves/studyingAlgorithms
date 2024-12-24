class Solution:
    def compress(self, chars: List[str]) -> int:
        
        currChar = chars[0]
        count = 0
        stringCompressed = ""

        for char in chars:
            if currChar != char:
                if count > 1:
                    stringCompressed += currChar + str(count)
                else:
                    stringCompressed += currChar
                count = 0
                currChar = char
            count += 1
        
        if count > 1:
            stringCompressed += currChar + str(count)
        else:
            stringCompressed += currChar

        chars.clear()

        for i in list(stringCompressed):
            chars.append(i)

        return len(chars)

