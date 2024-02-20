class Solution:
    def reverseWords(self, s: str) -> str:
        splitword = s.split()
        splitword.reverse()
        splitwordResult = ' '.join(splitword)
        print(splitwordResult.strip(" "))
        
reverse = Solution()


reverse.reverseWords('the sky is blue')

