class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        

        dict = {}

        i = 0
        while(i < len(arr)):

            if((dict.get(arr[i] * 2) or (dict.get(arr[i] / 2) and arr[i] % 2 == 0))):
                return True

            dict[arr[i]] = 1
            i += 1
        
        return False