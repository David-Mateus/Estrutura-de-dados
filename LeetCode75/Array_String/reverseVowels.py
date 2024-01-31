
class Solution:
    def reverseVowels(self, s: str) -> str:
        vogais = 'aeiouAEIOU'
        p = []
        for i in s:
            if i in vogais:
                p.append(i)
        
        
        # Retorna tamanho da lista -1
        o = len(p)-1
        r=""
        for k in range(len(s)):
            if s[k] in vogais:
                r += p[o]
                o -= 1
            else:
                r += s[k]
                
        return r

        
               
reverse = Solution()
print(reverse.reverseVowels('leetcode'))


