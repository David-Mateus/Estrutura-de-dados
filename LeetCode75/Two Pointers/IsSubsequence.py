class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        lenght = len(s)
        count = 0
        
        for i in t:
            if i == s[count]:
                count+=1
        if(lenght == count ):
            return(True)
        return(False)
                    
                

subsequence = Solution()
print(subsequence.isSubsequence('bb', 'ahbgdc'))

