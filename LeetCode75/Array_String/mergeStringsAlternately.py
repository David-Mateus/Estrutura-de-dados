
class Solution():
     def mergeAlternately(self, word1: str, word2: str) -> str:
          result = ''
          lenght = min(len(word1), len(word2))
          for i in range(lenght):
               result += word1[i] + word2[i]
          result += word1[lenght:] + word2[lenght:]
          return result
        

words = Solution()
print(words.mergeAlternately("abc", "pqr"))
               

    