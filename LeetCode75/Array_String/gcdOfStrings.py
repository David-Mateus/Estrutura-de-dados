import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lenght1, lenght2 = len(str1), len(str2)
        mdc = math.gcd(lenght1, lenght2)
        if(str1  +str2) != (str2+str1):
            return ''
        elif str1 == str2:
            return str1
        return str1[:mdc]

        
str = Solution()
print(str.gcdOfStrings("ABCABC", "ABC"))

